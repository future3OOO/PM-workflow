"""Extract key frames from training videos for visual analysis."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import Iterable

from batch_config import (
    DEFAULT_BATCH_DATE,
    discover_videos_in_dir,
    resolve_artefact_dir,
    resolve_video_dir,
    select_videos,
)

SCRIPT_DIR = Path(__file__).parent
FFMPEG = os.environ.get("FFMPEG_PATH", "ffmpeg")
FFMPEG_TIMEOUT = 300
COMPLETE_MARKER = "EXTRACTION_COMPLETE"
FRAME_PROFILES = {
    "standard": {"interval": 10, "subdir": "frames"},
    "dense": {"interval": 3, "subdir": "frames_dense"},
}


def count_extracted_frames(out_dir: Path) -> int:
    """Return the number of extracted JPG frames in an output directory."""
    return len(list(out_dir.glob("*.jpg")))


def extract_frames_for_video(
    video_id: str,
    filename: str,
    video_dir: Path,
    frames_dir: Path,
    interval: int,
) -> int:
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
        f"fps=1/{interval}",
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
        "--artefact-dir",
        help="Optional override for the dated artefact directory",
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
    parser.add_argument(
        "--profile",
        choices=sorted(FRAME_PROFILES),
        default="standard",
        help="Extraction profile. 'dense' writes to frames_dense with a tighter interval.",
    )
    parser.add_argument(
        "--interval",
        type=int,
        help="Optional explicit seconds-between-frames override",
    )
    return parser.parse_args()


def resolve_inputs(
    batch_date: str,
    video_dir_override: str | None = None,
    artefact_dir_override: str | None = None,
    frames_dir_override: str | None = None,
    video_ids: Iterable[str] | None = None,
    profile: str = "standard",
    interval_override: int | None = None,
) -> tuple[Path, Path, list[tuple[str, str]], int]:
    """Resolve source videos, output folder, selection, and capture interval."""
    video_dir = resolve_video_dir(SCRIPT_DIR, batch_date, video_dir_override)
    artefact_dir = resolve_artefact_dir(SCRIPT_DIR, batch_date, artefact_dir_override)
    if frames_dir_override:
        frames_dir = Path(frames_dir_override)
    else:
        frames_dir = artefact_dir / FRAME_PROFILES[profile]["subdir"]

    videos = select_videos(video_ids) if video_ids else discover_videos_in_dir(video_dir)
    interval = (
        interval_override
        if interval_override is not None
        else int(FRAME_PROFILES[profile]["interval"])
    )
    if interval <= 0:
        raise ValueError("--interval must be a positive integer")
    return video_dir, frames_dir, videos, interval


def extract_batch(
    batch_date: str = DEFAULT_BATCH_DATE,
    video_dir_override: str | None = None,
    artefact_dir_override: str | None = None,
    frames_dir_override: str | None = None,
    video_ids: Iterable[str] | None = None,
    profile: str = "standard",
    interval_override: int | None = None,
) -> int:
    """Extract frames for the selected videos into the canonical artefact structure."""
    video_dir, frames_dir, videos, interval = resolve_inputs(
        batch_date=batch_date,
        video_dir_override=video_dir_override,
        artefact_dir_override=artefact_dir_override,
        frames_dir_override=frames_dir_override,
        video_ids=video_ids,
        profile=profile,
        interval_override=interval_override,
    )

    print(f"Source video directory: {video_dir}")
    print(f"Frames output directory: {frames_dir}")
    print(f"Frame extraction interval: {interval}s")

    if not videos:
        print(
            "No configured videos were found in the selected source folder. "
            "Register the new video in batch_config.py or pass --video-id explicitly."
        )
        return 1

    frames_dir.mkdir(parents=True, exist_ok=True)
    total = 0

    for video_id, filename in videos:
        print(f"\n{'=' * 60}")
        print(f"Extracting frames: {video_id} — {filename}")
        print(f"{'=' * 60}")
        count = extract_frames_for_video(
            video_id=video_id,
            filename=filename,
            video_dir=video_dir,
            frames_dir=frames_dir,
            interval=interval,
        )
        print(f"  -> {count} frames saved to {frames_dir / video_id}")
        total += count

    print(f"\n{'=' * 60}")
    print(f"DONE — {total} total frames across {len(videos)} videos")
    print(f"{'=' * 60}")
    return 0


def main() -> None:
    """Extract frames for the configured batch and report totals."""
    args = parse_args()
    sys.exit(
        extract_batch(
            batch_date=args.batch_date,
            video_dir_override=args.video_dir,
            artefact_dir_override=args.artefact_dir,
            frames_dir_override=args.frames_dir,
            video_ids=args.video_ids,
            profile=args.profile,
            interval_override=args.interval,
        )
    )


if __name__ == "__main__":
    main()
