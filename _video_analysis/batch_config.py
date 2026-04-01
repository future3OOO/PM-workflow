"""Shared configuration helpers for dated video-analysis batches."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Iterable

DEFAULT_BATCH_DATE = "2026-04-02"

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
    ("video25", "Property tree- entering an ingoing inspection v2.mp4"),
    ("video26", "Property tree- entering new property, landlord and tenancy.mkv"),
    ("video27", "TPS- application approved (A).mp4"),
    ("video28", "TPS- application approved- Create Tenancy agreement (B).mp4"),
    ("video29", "TPS- Bond lodgement.mp4"),
    ("video30", "Inspection confirmations.mp4"),
]


def batch_date_aliases(batch_date: str) -> list[str]:
    """Return supported folder-name aliases for a batch date."""
    aliases = [batch_date]
    try:
        parsed = datetime.strptime(batch_date, "%Y-%m-%d")
    except ValueError:
        return aliases

    legacy = f"{parsed.day}-{parsed.month}-{parsed.year}"
    if legacy not in aliases:
        aliases.append(legacy)
    return aliases


def resolve_video_dir(script_dir: Path, batch_date: str, override: str | None = None) -> Path:
    """Return the source-video directory for a batch, supporting legacy folder names."""
    if override:
        return Path(override)

    for alias in batch_date_aliases(batch_date):
        candidate = script_dir / "videos" / alias
        if candidate.exists():
            return candidate
    return script_dir / "videos" / batch_date


def resolve_artefact_dir(
    script_dir: Path, batch_date: str, override: str | None = None
) -> Path:
    """Return the dated artefacts directory for a batch."""
    if override:
        return Path(override)
    return script_dir / "artefacts" / batch_date


def resolve_frames_dir(script_dir: Path, batch_date: str, override: str | None = None) -> Path:
    """Return the frame output directory for a batch."""
    if override:
        return Path(override)
    return resolve_artefact_dir(script_dir, batch_date) / "frames"


def select_videos(
    video_ids: Iterable[str] | None = None,
) -> list[tuple[str, str]]:
    """Return configured videos, optionally filtered by explicit video_id."""
    if not video_ids:
        return list(VIDEOS)

    requested = list(video_ids)
    selected = [item for item in VIDEOS if item[0] in requested]
    missing = [video_id for video_id in requested if video_id not in {item[0] for item in selected}]
    if missing:
        raise ValueError(f"Unknown video_id(s): {', '.join(missing)}")
    return selected


def discover_videos_in_dir(video_dir: Path) -> list[tuple[str, str]]:
    """Return configured videos whose source files exist in the selected source folder."""
    if not video_dir.exists():
        return []
    return [item for item in VIDEOS if (video_dir / item[1]).is_file()]


def discover_videos_in_artefact_dir(artefact_dir: Path) -> list[tuple[str, str]]:
    """Return configured videos that already have evidence in the selected artefact folder."""
    if not artefact_dir.exists():
        return []

    selected: list[tuple[str, str]] = []
    frames_root = artefact_dir / "frames"

    for video_id, filename in VIDEOS:
        has_transcript = (
            (artefact_dir / f"{video_id}_transcript.json").is_file()
            or (artefact_dir / f"{video_id}_transcript.txt").is_file()
        )
        has_frames = (frames_root / video_id).exists()
        if has_transcript or has_frames:
            selected.append((video_id, filename))

    return selected
