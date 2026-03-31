"""Extract audio and transcribe the 10 new training videos (2026-04-01 batch)."""

import json
import os
import subprocess
import sys
import time
from pathlib import Path

import whisper

SCRIPT_DIR = Path(__file__).parent
VIDEO_DIR = SCRIPT_DIR / "videos" / "1-4-2026"
ARTEFACT_DIR = SCRIPT_DIR / "artefacts" / "2026-04-01"
AUDIO_DIR = ARTEFACT_DIR / "audio"
FFMPEG = os.environ.get("FFMPEG_PATH", "ffmpeg")
FFMPEG_TIMEOUT = 900

VIDEOS = [
    ("video15", "1. TPS Book me - creating viewings.mp4"),
    ("video16", "2. TPS Book me - correction.mp4"),
    ("video17", "General example- liability nuance.mkv"),
    ("video18", "Inspections- Changing an inspections time.mp4"),
    ("video19", "Inspections- Entering an ingoing.mp4"),
    ("video20", "Property tree- entering a rent increase.mp4"),
    ("video21", "TPS Portal- entering a new property.mp4"),
    ("video22", "TPS- Lease renewal and increase - 1.mp4"),
    ("video23", "TPS- Lease renewal and increase - 2.mp4"),
    ("video24", "TPS- Lease renewal and increase - 3.mp4"),
]


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


def transcribe_batch() -> None:
    """Transcribe the configured video batch into JSON and readable TXT files."""
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)

    print("Loading Whisper model (base)...")
    model = whisper.load_model("base")
    print("Model loaded.\n")

    for vid_id, filename in VIDEOS:
        src = VIDEO_DIR / filename
        wav_path = AUDIO_DIR / f"{vid_id}_audio.wav"
        json_path = ARTEFACT_DIR / f"{vid_id}_transcript.json"
        txt_path = ARTEFACT_DIR / f"{vid_id}_transcript.txt"

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
    print(f"ALL DONE — All transcripts saved to {ARTEFACT_DIR}")
    print("=" * 70)


def main() -> None:
    """Run the configured batch transcription workflow."""
    transcribe_batch()


if __name__ == "__main__":
    main()
