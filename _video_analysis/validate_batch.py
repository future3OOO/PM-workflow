"""Validate that a dated video-analysis batch has the required local evidence."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from batch_config import DEFAULT_BATCH_DATE, resolve_artefact_dir, select_videos

SCRIPT_DIR = Path(__file__).parent


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for batch validation."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--batch-date",
        default=DEFAULT_BATCH_DATE,
        help="Batch date in YYYY-MM-DD format (default: %(default)s)",
    )
    parser.add_argument(
        "--artefact-dir",
        help="Optional override for the dated artefact directory",
    )
    parser.add_argument(
        "--video-id",
        action="append",
        dest="video_ids",
        help="Optional video_id filter. Repeat to validate specific videos only.",
    )
    parser.add_argument(
        "--require-coverage-matrix",
        action="store_true",
        help="Also require analysis/doc_coverage_matrix.md for batch sign-off validation.",
    )
    return parser.parse_args()


def main() -> int:
    """Return 0 when the batch has the required transcript, frame, and coverage artefacts."""
    args = parse_args()
    artefact_dir = resolve_artefact_dir(SCRIPT_DIR, args.batch_date, args.artefact_dir)
    videos = select_videos(args.video_ids, args.batch_date)
    issues: list[str] = []

    print(f"Validating artefact directory: {artefact_dir}")

    if not artefact_dir.exists():
        print("ERROR: artefact directory does not exist")
        return 1

    coverage_matrix = artefact_dir / "analysis" / "doc_coverage_matrix.md"
    if args.require_coverage_matrix and not coverage_matrix.is_file():
        issues.append(f"Missing doc coverage matrix: {coverage_matrix}")

    for video_id, _filename in videos:
        json_path = artefact_dir / f"{video_id}_transcript.json"
        txt_path = artefact_dir / f"{video_id}_transcript.txt"
        frame_dir = artefact_dir / "frames" / video_id
        frame_count = len(list(frame_dir.glob("*.jpg"))) if frame_dir.exists() else 0

        if not json_path.is_file():
            issues.append(f"Missing transcript JSON for {video_id}: {json_path}")
        if not txt_path.is_file():
            issues.append(f"Missing transcript TXT for {video_id}: {txt_path}")
        if frame_count == 0:
            issues.append(f"Missing extracted frames for {video_id}: {frame_dir}")

    if issues:
        print("VALIDATION FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print(f"VALIDATION PASSED for {len(videos)} video(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
