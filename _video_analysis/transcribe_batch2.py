"""Extract audio and transcribe the configured dated training-video batch."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path
from typing import Iterable

import whisper
from batch_config import (
    DEFAULT_BATCH_DATE,
    discover_videos_in_dir,
    resolve_artefact_dir,
    resolve_video_dir,
    select_videos,
)

SCRIPT_DIR = Path(__file__).parent
FFMPEG = os.environ.get("FFMPEG_PATH", "ffmpeg")
FFMPEG_TIMEOUT = 900
DEFAULT_WHISPER_MODEL = "medium"


def remove_if_exists(path: Path) -> None:
    """Delete a file if it exists."""
    if path.exists():
        path.unlink()


def outputs_are_complete(json_path: Path, txt_path: Path) -> bool:
    """Return True when both transcript outputs exist and the JSON parses."""
    if not json_path.exists() or not txt_path.exists():
        if json_path.exists() or txt_path.exists():
            print("  [WARN] Incomplete transcript outputs found — regenerating")
            remove_if_exists(json_path)
            remove_if_exists(txt_path)
        return False

    try:
        with json_path.open("r", encoding="utf-8") as handle:
            json.load(handle)
    except json.JSONDecodeError:
        print(f"  [WARN] Corrupt transcript JSON at {json_path} — regenerating")
        remove_if_exists(json_path)
        remove_if_exists(txt_path)
        return False

    return True


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for the transcription batch."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--batch-date",
        default=DEFAULT_BATCH_DATE,
        help="Batch date in YYYY-MM-DD format (default: %(default)s)",
    )
    parser.add_argument(
        "--video-dir",
        help="Optional override for the source video directory",
    )
    parser.add_argument(
        "--artefact-dir",
        help="Optional override for the dated artefact directory",
    )
    parser.add_argument(
        "--video-id",
        action="append",
        dest="video_ids",
        help="Optional video_id filter. Repeat to process multiple specific videos.",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_WHISPER_MODEL,
        help=(
            "Whisper model to use for transcription "
            f"(default: {DEFAULT_WHISPER_MODEL})"
        ),
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate transcripts even if existing outputs look complete.",
    )
    return parser.parse_args()


def resolve_inputs(
    batch_date: str,
    video_dir_override: str | None = None,
    artefact_dir_override: str | None = None,
    video_ids: Iterable[str] | None = None,
) -> tuple[Path, Path, list[tuple[str, str]]]:
    """Resolve the canonical source directory, artefact directory, and video selection."""
    video_dir = resolve_video_dir(SCRIPT_DIR, batch_date, video_dir_override)
    artefact_dir = resolve_artefact_dir(SCRIPT_DIR, batch_date, artefact_dir_override)
    videos = select_videos(video_ids) if video_ids else discover_videos_in_dir(video_dir)
    return video_dir, artefact_dir, videos


def extract_audio(src: Path, wav_path: Path) -> bool:
    """Extract a mono 16kHz WAV for transcription."""
    print("  Extracting audio...")
    t0 = time.time()
    cmd = [
        FFMPEG,
        "-y",
        "-i",
        str(src),
        "-vn",
        "-acodec",
        "pcm_s16le",
        "-ar",
        "16000",
        "-ac",
        "1",
        str(wav_path),
    ]
    try:
        subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=True,
            timeout=FFMPEG_TIMEOUT,
        )
    except FileNotFoundError:
        print(
            f"  [ERROR] ffmpeg not found: {FFMPEG}. "
            "Set FFMPEG_PATH or install ffmpeg on PATH."
        )
        remove_if_exists(wav_path)
        return False
    except subprocess.TimeoutExpired:
        print(f"  [ERROR] ffmpeg timed out after {FFMPEG_TIMEOUT}s")
        remove_if_exists(wav_path)
        return False
    except subprocess.CalledProcessError as exc:
        message = exc.stderr[:500] if exc.stderr else "no stderr"
        print(f"  [ERROR] ffmpeg failed: {message}")
        remove_if_exists(wav_path)
        return False
    print(f"  Audio extracted in {time.time() - t0:.1f}s")
    return True


def save_transcript_outputs(
    video_id: str,
    filename: str,
    model_name: str,
    transcript: dict,
    json_path: Path,
    txt_path: Path,
) -> None:
    """Persist the machine-readable and review-friendly transcript artefacts."""
    transcript["_analysis_metadata"] = {
        "whisper_model": model_name,
    }
    with json_path.open("w", encoding="utf-8") as handle:
        json.dump(transcript, handle, indent=2, ensure_ascii=False)
    print(f"  JSON saved: {json_path}")

    with txt_path.open("w", encoding="utf-8") as handle:
        handle.write(f"# Transcript — {video_id}\n")
        handle.write(f"# Source: {filename}\n\n")
        handle.write(f"# Whisper model: {model_name}\n\n")
        for seg in transcript["segments"]:
            start_m = int(seg["start"] // 60)
            start_s = int(seg["start"] % 60)
            end_m = int(seg["end"] // 60)
            end_s = int(seg["end"] % 60)
            handle.write(
                f"[{start_m:02d}:{start_s:02d} - {end_m:02d}:{end_s:02d}] "
                f"{seg['text'].strip()}\n"
            )
    print(f"  TXT saved: {txt_path}")


def transcribe_videos(
    videos: list[tuple[str, str]],
    video_dir: Path,
    artefact_dir: Path,
    model_name: str,
    force: bool = False,
) -> None:
    """Transcribe the selected videos into the canonical dated artefact layout."""
    audio_dir = artefact_dir / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading Whisper model ({model_name})...")
    model = whisper.load_model(model_name)
    print("Model loaded.\n")

    for video_id, filename in videos:
        src = video_dir / filename
        wav_path = audio_dir / f"{video_id}_audio.wav"
        json_path = artefact_dir / f"{video_id}_transcript.json"
        txt_path = artefact_dir / f"{video_id}_transcript.txt"

        if not src.exists():
            print(f"[SKIP] {filename} — file not found at {src}")
            continue

        if not force and outputs_are_complete(json_path, txt_path):
            print(f"[SKIP] {video_id} ({filename}) — transcript already exists")
            continue
        if force:
            remove_if_exists(json_path)
            remove_if_exists(txt_path)

        print(f"\n{'=' * 70}")
        print(f"Processing {video_id}: {filename}")
        print(f"{'=' * 70}")

        if not wav_path.exists():
            if not extract_audio(src, wav_path):
                continue
        else:
            print("  Audio already extracted, skipping ffmpeg")

        print("  Transcribing...")
        t0 = time.time()
        try:
            transcript = model.transcribe(
                str(wav_path),
                language="en",
                verbose=False,
                word_timestamps=True,
            )
        except Exception as exc:  # pragma: no cover - whisper runtime failure path
            print(f"  [ERROR] transcription failed for {video_id} ({wav_path}): {exc}")
            continue
        elapsed = time.time() - t0
        print(f"  Transcription done in {elapsed:.1f}s")

        save_transcript_outputs(
            video_id,
            filename,
            model_name,
            transcript,
            json_path,
            txt_path,
        )

        seg_count = len(transcript["segments"])
        if seg_count == 0:
            print(f"  WARNING: No segments transcribed for {video_id}")
        else:
            char_count = len(transcript["text"])
            duration_s = transcript["segments"][-1]["end"]
            duration_m = int(duration_s // 60)
            duration_r = int(duration_s % 60)
            print(
                f"  Duration: {duration_m}m{duration_r}s | "
                f"Segments: {seg_count} | Chars: {char_count}"
            )
            print(f"  Preview: {transcript['text'][:300]}...")

        sys.stdout.flush()


def transcribe_batch(
    batch_date: str = DEFAULT_BATCH_DATE,
    video_dir_override: str | None = None,
    artefact_dir_override: str | None = None,
    video_ids: Iterable[str] | None = None,
    model_name: str = DEFAULT_WHISPER_MODEL,
    force: bool = False,
) -> int:
    """Transcribe the requested batch selection into dated artefact folders."""
    video_dir, artefact_dir, videos = resolve_inputs(
        batch_date=batch_date,
        video_dir_override=video_dir_override,
        artefact_dir_override=artefact_dir_override,
        video_ids=video_ids,
    )

    print(f"Source video directory: {video_dir}")
    print(f"Artefact output directory: {artefact_dir}")

    if not videos:
        print(
            "No configured videos were found in the selected source folder. "
            "Register the new video in batch_config.py or pass --video-id explicitly."
        )
        return 1

    transcribe_videos(
        videos=videos,
        video_dir=video_dir,
        artefact_dir=artefact_dir,
        model_name=model_name,
        force=force,
    )

    print("\n\n" + "=" * 70)
    print(f"ALL DONE — All transcripts saved to {artefact_dir}")
    print("=" * 70)
    return 0


def main() -> None:
    """Run the configured batch transcription workflow."""
    args = parse_args()
    sys.exit(
        transcribe_batch(
            batch_date=args.batch_date,
            video_dir_override=args.video_dir,
            artefact_dir_override=args.artefact_dir,
            video_ids=args.video_ids,
            model_name=args.model,
            force=args.force,
        )
    )


if __name__ == "__main__":
    main()
