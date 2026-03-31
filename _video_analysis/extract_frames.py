"""Extract key frames from training videos for visual analysis.

Captures one frame every INTERVAL seconds from each video, saving them
as numbered JPEG files in the artefacts/frames directory.
"""

import os
import subprocess
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
VIDEO_DIR = SCRIPT_DIR / "videos" / "1-4-2026"
FRAMES_DIR = SCRIPT_DIR / "artefacts" / "2026-04-01" / "frames"
FFMPEG = os.environ.get("FFMPEG_PATH", "ffmpeg")

INTERVAL = 10  # seconds between frame captures
FFMPEG_TIMEOUT = 300
COMPLETE_MARKER = "EXTRACTION_COMPLETE"

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


def count_extracted_frames(out_dir: Path) -> int:
    """Return the number of extracted JPG frames in an output directory."""
    return len(list(out_dir.glob("*.jpg")))


def extract_frames(video_id: str, filename: str) -> int:
    """Extract frames for a single video and mark success on completion."""
    src = VIDEO_DIR / filename
    if not src.is_file():
        print(f"  SKIP — file not found: {src}")
        return 0

    out_dir = FRAMES_DIR / video_id
    out_dir.mkdir(parents=True, exist_ok=True)

    marker_path = out_dir / COMPLETE_MARKER
    if marker_path.exists():
        existing_count = count_extracted_frames(out_dir)
        print(f"  Already extracted {existing_count} frames — skipping")
        return existing_count

    existing_frames = list(out_dir.glob("*.jpg"))
    if existing_frames:
        print(f"  Removing {len(existing_frames)} partial frames before re-extracting")
        for frame in existing_frames:
            frame.unlink()

    cmd = [
        FFMPEG,
        "-i",
        str(src),
        "-vf",
        f"fps=1/{INTERVAL}",
        "-q:v",
        "2",
        "-vsync",
        "vfr",
        str(out_dir / f"{video_id}_frame_%04d.jpg"),
    ]

    try:
        subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=FFMPEG_TIMEOUT,
            check=True,
        )
    except FileNotFoundError:
        print(
            f"  ERROR: ffmpeg not found: {FFMPEG}. "
            "Set FFMPEG_PATH or install ffmpeg on PATH."
        )
        return 0
    except subprocess.TimeoutExpired:
        print(f"  ERROR: ffmpeg timed out after {FFMPEG_TIMEOUT}s")
        return 0
    except subprocess.CalledProcessError as exc:
        print(f"  ERROR: ffmpeg returned {exc.returncode}")
        if exc.stderr:
            print(f"  stderr: {exc.stderr[-500:]}")
        return 0

    marker_path.write_text("ok\n", encoding="utf-8")
    return count_extracted_frames(out_dir)


def main() -> None:
    """Extract frames for the configured batch and report totals."""
    FRAMES_DIR.mkdir(parents=True, exist_ok=True)
    total = 0

    for video_id, filename in VIDEOS:
        print(f"\n{'='*60}")
        print(f"Extracting frames: {video_id} — {filename}")
        print(f"{'='*60}")
        count = extract_frames(video_id, filename)
        print(f"  -> {count} frames saved to {FRAMES_DIR / video_id}")
        total += count

    print(f"\n{'='*60}")
    print(f"DONE — {total} total frames across {len(VIDEOS)} videos")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
