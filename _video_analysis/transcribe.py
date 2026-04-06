"""Transcribe one configured video using the canonical dated-batch workflow.

Usage:
    py -3 _video_analysis/transcribe.py <video_id> <path_to_video>

Example:
    py -3 _video_analysis/transcribe.py video15 "_video_analysis/videos/2026-04-01/1. TPS Book me - creating viewings.mp4"

This wrapper enforces the same output layout and processing path as `transcribe_batch2.py`.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from batch_config import (
    configured_filename_for,
    infer_batch_date_from_path,
)
from transcribe_batch2 import transcribe_batch


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for canonical single-video transcription."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video_id", help="Configured video ID from batch_config.py")
    parser.add_argument("video_path", help="Path to the source video file")
    parser.add_argument(
        "--batch-date",
        help=(
            "Optional batch date override in YYYY-MM-DD format. "
            "When omitted, the wrapper infers the date from the video path."
        ),
    )
    parser.add_argument(
        "--artefact-dir",
        help="Optional dated artefact directory override",
    )
    parser.add_argument(
        "--model",
        default="medium",
        help="Whisper model to use for transcription (default: %(default)s)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate transcripts even if existing outputs look complete.",
    )
    parser.add_argument(
        "--allow-filename-mismatch",
        action="store_true",
        help=(
            "Skip the safety check that the provided filename matches the configured "
            "filename for this video_id."
        ),
    )
    return parser.parse_args()


def main() -> None:
    """Run the canonical single-video transcription workflow."""
    args = parse_args()
    video_path = Path(args.video_path).expanduser().resolve()

    if not video_path.is_file():
        print(f"[ERROR] Video file not found: {video_path}")
        sys.exit(1)

    try:
        configured_filename = configured_filename_for(args.video_id)
    except ValueError as exc:
        print(f"[ERROR] {exc}")
        sys.exit(1)
    if (
        not args.allow_filename_mismatch
        and video_path.name != configured_filename
    ):
        print(
            "[ERROR] Provided filename does not match batch_config.py for this video_id.\n"
            f"        video_id: {args.video_id}\n"
            f"        configured: {configured_filename}\n"
            f"        provided:   {video_path.name}\n"
            "        Rename the source file or use the configured filename so the "
            "single-video and batch workflows remain identical."
        )
        sys.exit(1)

    batch_date = args.batch_date or infer_batch_date_from_path(video_path)
    if not batch_date:
        print(
            "[ERROR] Could not infer a batch date from the video path. "
            "Pass --batch-date explicitly so outputs still land in the canonical "
            "dated artefact folder."
        )
        sys.exit(1)

    sys.exit(
        transcribe_batch(
            batch_date=batch_date,
            video_dir_override=str(video_path.parent),
            artefact_dir_override=args.artefact_dir,
            video_ids=[args.video_id],
            model_name=args.model,
            force=args.force,
        )
    )


if __name__ == "__main__":
    main()
