"""Normalize legacy tracked artefacts into the canonical dated-batch layout.

This script is intentionally narrow. It codifies the specific historical cleanups
needed for the tracked artefacts that pre-date the current performance workflow:

- move legacy top-level analysis markdown into `analysis/`
- flatten the old `transcripts/` subfolder into the batch root
- rename `frames/frames_vNN` directories to `frames/videoNN`
- move stray unmapped files out of the active batch root
- rewrite stale markdown references that still point at removed legacy paths
"""

from __future__ import annotations

import argparse
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

SCRIPT_DIR = Path(__file__).parent
ARTEFACTS_DIR = SCRIPT_DIR / "artefacts"


@dataclass(frozen=True)
class BatchPlan:
    """Normalization operations for a specific legacy batch folder."""

    analysis_moves: dict[str, str] = field(default_factory=dict)
    frame_dir_renames: dict[str, str] = field(default_factory=dict)
    legacy_unmapped_files: dict[str, str] = field(default_factory=dict)
    flatten_transcripts: bool = False
    regex_replacements: tuple[tuple[str, str | Callable[[re.Match[str]], str]], ...] = ()


PLANS: dict[str, BatchPlan] = {
    "2026-03-07": BatchPlan(
        analysis_moves={
            "VIDEO_ANALYSIS_REPORT.md": "analysis/video01_video02_inspection_follow_up_approval_analysis.md",
        },
    ),
    "2026-03-31": BatchPlan(
        analysis_moves={
            "VIDEO_04_ANALYSIS_REPORT.md": "analysis/video04_tapi_overview_and_management_2_analysis.md",
            "VIDEO_ANALYSIS_REPORT_CALL_CONTRACTOR_FIRST.md": "analysis/video05_call_contractor_first_analysis.md",
            "VIDEO_ANALYSIS_INVOICES_1.md": "analysis/video06_invoices_1_analysis.md",
            "VIDEO_ANALYSIS_INVOICES_2.md": "analysis/video07_invoices_2_analysis.md",
            "VIDEO_ANALYSIS_INSPECTION_APPROVAL_REQUEST.md": "analysis/video08_inspection_approval_request_analysis.md",
            "VIDEO_ANALYSIS_INSPECTION_APPROVAL_REQUEST_2.md": "analysis/video09_inspection_approval_request_2_analysis.md",
            "VIDEO_10_ANALYSIS_REPORT_JOB_APPROVED.md": "analysis/video10_job_approved_analysis.md",
            "VIDEO_11_ANALYSIS_REPORT_NEW_TENANT_MAINTENANCE_REQUEST_VIA_CONCIERGE.md": (
                "analysis/video11_new_tenant_maintenance_request_via_concierge_analysis.md"
            ),
            "VIDEO_ANALYSIS_QUOTE_REQUEST_FROM_OWNER.md": "analysis/video12_quote_request_from_owner_analysis.md",
            "VIDEO_ANALYSIS_QUOTE_REQUEST_EXAMPLE_2.md": "analysis/video13_quote_request_example_2_analysis.md",
            "VIDEO_ANALYSIS_SEND_TO_OWNER_DIY.md": "analysis/video14_send_to_owner_for_diy_analysis.md",
            "VIDEO_ANALYSIS_REPORT_BATCH2.md": "analysis/batch_summary.md",
        },
        frame_dir_renames={
            "frames_v04": "video04",
            "frames_v05": "video05",
            "frames_v09": "video09",
            "frames_v10": "video10",
            "frames_v11": "video11",
            "frames_v13": "video13",
        },
        flatten_transcripts=True,
        regex_replacements=(
            (
                re.escape("_video_analysis/VIDEO_ANALYSIS_REPORT.md"),
                "_video_analysis/artefacts/2026-03-07/analysis/"
                "video01_video02_inspection_follow_up_approval_analysis.md",
            ),
            (
                re.escape("_video_analysis/VIDEO_ANALYSIS_INSPECTION_APPROVAL_REQUEST.md"),
                "_video_analysis/artefacts/2026-03-31/analysis/"
                "video08_inspection_approval_request_analysis.md",
            ),
            (
                re.escape("_video_analysis/VIDEO_ANALYSIS_REPORT_CALL_CONTRACTOR_FIRST.md"),
                "_video_analysis/artefacts/2026-03-31/analysis/video05_call_contractor_first_analysis.md",
            ),
            (
                re.escape("_video_analysis/VIDEO_04_ANALYSIS_REPORT.md"),
                "_video_analysis/artefacts/2026-03-31/analysis/video04_tapi_overview_and_management_2_analysis.md",
            ),
            (
                r"_video_analysis/videos/(video(0[3-9]|1[0-4])_transcript\.(txt|json))",
                lambda match: f"_video_analysis/artefacts/2026-03-31/{match.group(1)}",
            ),
            (
                r"_video_analysis/videos/frames_v(\d{2})/",
                lambda match: f"_video_analysis/artefacts/2026-03-31/frames/video{match.group(1)}/",
            ),
        ),
    ),
    "2026-04-01": BatchPlan(
        legacy_unmapped_files={
            "video15b_transcript.json": "legacy_unmapped/video15b_transcript.json",
            "video15b_transcript.txt": "legacy_unmapped/video15b_transcript.txt",
        },
    ),
}


def parse_args() -> argparse.Namespace:
    """Parse CLI arguments for legacy artefact normalization."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply the normalization changes. Without this flag, the script runs in dry-run mode.",
    )
    return parser.parse_args()


def log(message: str) -> None:
    """Emit a normalization log line."""
    print(message)


def ensure_parent(path: Path, apply: bool) -> None:
    """Create parent directories for a target path when applying changes."""
    if apply:
        path.parent.mkdir(parents=True, exist_ok=True)


def move_path(src: Path, dst: Path, apply: bool) -> None:
    """Move a file or directory unless already normalized."""
    if not src.exists():
        return

    if dst.exists():
        raise FileExistsError(f"Refusing to overwrite existing path: {dst}")

    log(f"MOVE {src} -> {dst}")
    ensure_parent(dst, apply)
    if apply:
        shutil.move(str(src), str(dst))


def flatten_transcripts_dir(batch_dir: Path, apply: bool) -> None:
    """Move transcript artefacts out of the legacy transcripts/ folder."""
    transcripts_dir = batch_dir / "transcripts"
    if not transcripts_dir.is_dir():
        return

    for transcript_path in sorted(transcripts_dir.iterdir()):
        target = batch_dir / transcript_path.name
        if target.exists():
            if transcript_path.read_bytes() != target.read_bytes():
                raise ValueError(
                    f"Transcript destination already exists with different content: {target}"
                )
            log(f"DELETE duplicate transcript {transcript_path}")
            if apply:
                transcript_path.unlink()
            continue
        move_path(transcript_path, target, apply)

    if not any(transcripts_dir.iterdir()):
        log(f"RMDIR {transcripts_dir}")
        if apply:
            transcripts_dir.rmdir()


def rewrite_markdown_paths(
    batch_dir: Path,
    replacements: tuple[tuple[str, str | Callable[[re.Match[str]], str]], ...],
    apply: bool,
) -> None:
    """Rewrite stale legacy references inside markdown files for a batch."""
    if not replacements:
        return

    for markdown_path in sorted(batch_dir.rglob("*.md")):
        original = markdown_path.read_text(encoding="utf-8")
        updated = original
        for pattern, replacement in replacements:
            updated = re.sub(pattern, replacement, updated)
        if updated == original:
            continue

        log(f"REWRITE {markdown_path}")
        if apply:
            markdown_path.write_text(updated, encoding="utf-8")


def normalize_batch(batch_name: str, plan: BatchPlan, apply: bool) -> None:
    """Apply a batch-specific normalization plan."""
    batch_dir = ARTEFACTS_DIR / batch_name
    if not batch_dir.is_dir():
        raise FileNotFoundError(f"Batch directory not found: {batch_dir}")

    for legacy_name, target_relative in plan.analysis_moves.items():
        move_path(batch_dir / legacy_name, batch_dir / target_relative, apply)

    if plan.flatten_transcripts:
        flatten_transcripts_dir(batch_dir, apply)

    for legacy_name, target_name in plan.frame_dir_renames.items():
        move_path(batch_dir / "frames" / legacy_name, batch_dir / "frames" / target_name, apply)

    for legacy_name, target_relative in plan.legacy_unmapped_files.items():
        move_path(batch_dir / legacy_name, batch_dir / target_relative, apply)

    rewrite_markdown_paths(batch_dir, plan.regex_replacements, apply)


def main() -> int:
    """Run the configured legacy artefact normalization plan."""
    args = parse_args()
    mode = "APPLY" if args.apply else "DRY-RUN"
    log(f"{mode} normalization for tracked legacy artefacts")

    for batch_name, plan in PLANS.items():
        log(f"\n== {batch_name} ==")
        normalize_batch(batch_name, plan, args.apply)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
