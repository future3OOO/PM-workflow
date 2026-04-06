"""Validate that a dated video-analysis batch has the required local evidence."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

from batch_config import (
    DEFAULT_BATCH_DATE,
    discover_videos_in_artefact_dir,
    discover_videos_in_dir,
    select_videos,
    resolve_artefact_dir,
    resolve_video_dir,
)

SCRIPT_DIR = Path(__file__).parent
DEFAULT_GLOSSARY_PATH = SCRIPT_DIR.parent / "docs" / "day-to-day" / "video-analysis-glossary.md"


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
        "--video-dir",
        help="Optional override for the source video directory",
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
    parser.add_argument(
        "--require-analysis-reports",
        action="store_true",
        help="Also require one per-video analysis report for every selected video.",
    )
    parser.add_argument(
        "--require-glossary",
        action="store_true",
        help="Also require the published glossary to reference every selected video_id.",
    )
    parser.add_argument(
        "--require-batch-closeout",
        action="store_true",
        help=(
            "Require the full closeout artefacts: coverage matrix, per-video analysis "
            "reports, and glossary coverage."
        ),
    )
    parser.add_argument(
        "--glossary-path",
        default=str(DEFAULT_GLOSSARY_PATH),
        help="Optional override for the published glossary path",
    )
    return parser.parse_args()


def discover_videos(
    artefact_dir: Path,
    video_dir: Path,
    video_ids: list[str] | None,
) -> list[tuple[str, str]]:
    """Resolve which configured videos should be validated."""
    if video_ids:
        return select_videos(video_ids)

    discovered: dict[str, tuple[str, str]] = {}
    for video_id, filename in discover_videos_in_artefact_dir(artefact_dir):
        discovered[video_id] = (video_id, filename)
    for video_id, filename in discover_videos_in_dir(video_dir):
        discovered[video_id] = (video_id, filename)
    return list(discovered.values())


def find_analysis_report(analysis_dir: Path, video_id: str) -> Path | None:
    """Return the first plausible per-video analysis report for a video_id."""
    if not analysis_dir.is_dir():
        return None

    candidates = sorted(
        path
        for path in analysis_dir.glob("*.md")
        if path.name != "doc_coverage_matrix.md" and video_id.lower() in path.stem.lower()
    )
    return candidates[0] if candidates else None


def glossary_mentions_video(glossary_text: str, video_id: str) -> bool:
    """Return True when the published glossary references the selected video."""
    pattern = re.compile(rf"`{re.escape(video_id)}`|\b{re.escape(video_id)}\b")
    return bool(pattern.search(glossary_text))


def main() -> int:
    """Return 0 when the batch has the required transcript, frame, and closeout artefacts."""
    args = parse_args()
    require_coverage_matrix = args.require_coverage_matrix or args.require_batch_closeout
    require_analysis_reports = args.require_analysis_reports or args.require_batch_closeout
    require_glossary = args.require_glossary or args.require_batch_closeout

    artefact_dir = resolve_artefact_dir(SCRIPT_DIR, args.batch_date, args.artefact_dir)
    video_dir = resolve_video_dir(SCRIPT_DIR, args.batch_date, args.video_dir)
    videos = discover_videos(artefact_dir, video_dir, args.video_ids)
    issues: list[str] = []

    print(f"Validating artefact directory: {artefact_dir}")

    if not artefact_dir.exists():
        print("ERROR: artefact directory does not exist")
        return 1

    if not videos:
        print(
            "ERROR: no configured videos were discovered for this batch. "
            "Pass --video-id, or point --video-dir / --artefact-dir at the correct batch location."
        )
        return 1

    analysis_dir = artefact_dir / "analysis"
    coverage_matrix = analysis_dir / "doc_coverage_matrix.md"
    if require_coverage_matrix and not coverage_matrix.is_file():
        issues.append(f"Missing doc coverage matrix: {coverage_matrix}")

    glossary_text = ""
    glossary_path = Path(args.glossary_path)
    if require_glossary:
        if not glossary_path.is_file():
            issues.append(f"Missing published glossary: {glossary_path}")
        else:
            glossary_text = glossary_path.read_text(encoding="utf-8")

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

        if require_analysis_reports and not find_analysis_report(analysis_dir, video_id):
            issues.append(
                f"Missing per-video analysis report for {video_id} in {analysis_dir}"
            )

        if (
            require_glossary
            and glossary_text
            and not glossary_mentions_video(glossary_text, video_id)
        ):
            issues.append(f"Published glossary does not mention {video_id}: {glossary_path}")

    if issues:
        print("VALIDATION FAILED")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print(f"VALIDATION PASSED for {len(videos)} video(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
