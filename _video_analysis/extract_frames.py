"""Extract key frames from training videos for visual analysis."""

import argparse
import subprocess
from pathlib import Path

from batch_config import (
    DEFAULT_BATCH_DATE,
    resolve_frames_dir,
    resolve_video_dir,
    select_videos,
)

SCRIPT_DIR = Path(__file__).parent
FFMPEG = __import__("os").environ.get("FFMPEG_PATH", "ffmpeg")

INTERVAL = 10  # seconds between frame captures
FFMPEG_TIMEOUT = 300
COMPLETE_MARKER = "EXTRACTION_COMPLETE"


def count_extracted_frames(out_dir: Path) -> int:
    """Return the number of extracted JPG frames in an output directory."""
    return len(list(out_dir.glob("*.jpg")))


def extract_frames(video_id: str, filename: str, video_dir: Path, frames_dir: Path) -> int:
    """Extract frames for a single video and mark success on completion."""
    src = video_dir / filename
    if not src.is_file():
        print(f"  SKIP — file not found: {src}")
        return 0

    out_dir = frames_dir / video_id
    out_dir.mkdir(parents=True, exist_ok=True)

    marker_path = out_dir / COMPLETE_MARKER
    if marker_path.exists():
        existing_count = count_extracted_frames(out_dir)
        if existing_count > 0:
            print(f"  Already extracted {existing_count} frames — skipping")
            return existing_count
        print("  Marker exists but no frames found — re-extracting")
        marker_path.unlink()

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

    extracted_count = count_extracted_frames(out_dir)
    if extracted_count == 0:
        print("  ERROR: ffmpeg completed but produced no frames")
        return 0
    marker_path.write_text("ok\n", encoding="utf-8")
    return extracted_count


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for the frame extraction batch."""
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
        "--frames-dir",
        help="Optional override for the output frames directory",
    )
    parser.add_argument(
        "--video-id",
        action="append",
        dest="video_ids",
        help="Optional video_id filter. Repeat to process multiple specific videos.",
    )
    return parser.parse_args()


def main() -> None:
    """Extract frames for the configured batch and report totals."""
    args = parse_args()
    video_dir = resolve_video_dir(SCRIPT_DIR, args.batch_date, args.video_dir)
    frames_dir = resolve_frames_dir(SCRIPT_DIR, args.batch_date, args.frames_dir)
    videos = select_videos(args.video_ids)

    print(f"Source video directory: {video_dir}")
    print(f"Frames output directory: {frames_dir}")

    frames_dir.mkdir(parents=True, exist_ok=True)
    total = 0

    for video_id, filename in videos:
        print(f"\n{'='*60}")
        print(f"Extracting frames: {video_id} — {filename}")
        print(f"{'='*60}")
        count = extract_frames(video_id, filename, video_dir, frames_dir)
        print(f"  -> {count} frames saved to {frames_dir / video_id}")
        total += count

    print(f"\n{'='*60}")
    print(f"DONE — {total} total frames across {len(videos)} videos")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
