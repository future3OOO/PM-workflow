"""Extract audio and transcribe the configured dated training-video batch."""

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

import whisper
from batch_config import (
    DEFAULT_BATCH_DATE,
    resolve_artefact_dir,
    resolve_video_dir,
    select_videos,
)

SCRIPT_DIR = Path(__file__).parent
FFMPEG = os.environ.get("FFMPEG_PATH", "ffmpeg")
FFMPEG_TIMEOUT = 900


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
    return parser.parse_args()


def transcribe_batch() -> None:
    """Transcribe the configured video batch into JSON and readable TXT files."""
    args = parse_args()
    video_dir = resolve_video_dir(SCRIPT_DIR, args.batch_date, args.video_dir)
    artefact_dir = resolve_artefact_dir(SCRIPT_DIR, args.batch_date, args.artefact_dir)
    audio_dir = artefact_dir / "audio"
    videos = select_videos(args.video_ids, args.batch_date)

    print(f"Source video directory: {video_dir}")
    print(f"Artefact output directory: {artefact_dir}")

    audio_dir.mkdir(parents=True, exist_ok=True)

    print("Loading Whisper model (base)...")
    model = whisper.load_model("base")
    print("Model loaded.\n")

    for vid_id, filename in videos:
        src = video_dir / filename
        wav_path = audio_dir / f"{vid_id}_audio.wav"
        json_path = artefact_dir / f"{vid_id}_transcript.json"
        txt_path = artefact_dir / f"{vid_id}_transcript.txt"

        if not src.exists():
            print(f"[SKIP] {filename} — file not found at {src}")
            continue

        if outputs_are_complete(json_path, txt_path):
            print(f"[SKIP] {vid_id} ({filename}) — transcript already exists")
            continue

        print(f"\n{'='*70}")
        print(f"Processing {vid_id}: {filename}")
        print(f"{'='*70}")

        if not wav_path.exists():
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
                continue
            except subprocess.TimeoutExpired:
                print(f"  [ERROR] ffmpeg timed out after {FFMPEG_TIMEOUT}s")
                remove_if_exists(wav_path)
                continue
            except subprocess.CalledProcessError as exc:
                message = exc.stderr[:500] if exc.stderr else "no stderr"
                print(f"  [ERROR] ffmpeg failed: {message}")
                remove_if_exists(wav_path)
                continue
            print(f"  Audio extracted in {time.time() - t0:.1f}s")
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
        except Exception as exc:
            print(f"  [ERROR] transcription failed for {vid_id} ({wav_path}): {exc}")
            continue
        elapsed = time.time() - t0
        print(f"  Transcription done in {elapsed:.1f}s")

        with json_path.open("w", encoding="utf-8") as handle:
            json.dump(transcript, handle, indent=2, ensure_ascii=False)
        print(f"  JSON saved: {json_path}")

        with txt_path.open("w", encoding="utf-8") as handle:
            handle.write(f"# Transcript — {vid_id}\n")
            handle.write(f"# Source: {filename}\n\n")
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

        seg_count = len(transcript["segments"])
        if seg_count == 0:
            print(f"  WARNING: No segments transcribed for {vid_id}")
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

    print("\n\n" + "=" * 70)
    print(f"ALL DONE — All transcripts saved to {artefact_dir}")
    print("=" * 70)


def main() -> None:
    """Run the configured batch transcription workflow."""
    transcribe_batch()


if __name__ == "__main__":
    main()
