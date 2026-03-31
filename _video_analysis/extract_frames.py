"""Extract key frames from training videos for visual analysis.

Captures one frame every INTERVAL seconds from each video, saving them
as numbered JPEG files in the artefacts/frames directory.
"""

import os
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEO_DIR = os.path.join(SCRIPT_DIR, "videos", "1-4-2026")
FRAMES_DIR = os.path.join(SCRIPT_DIR, "artefacts", "2026-04-01", "frames")
FFMPEG = os.environ.get(
    "FFMPEG_PATH", r"C:\ProgramData\chocolatey\bin\ffmpeg.exe"
)

INTERVAL = 10  # seconds between frame captures

VIDEOS = [
    ("video15", "1. TPS Book me - creating viewings.mp4"),
    ("video16", "2. TPS Book me - correction.mp4"),
    ("video17", "General example- liability nuance.mp4"),
    ("video18", "Inspections- Changing an inspections time.mp4"),
    ("video19", "Inspections- Entering an ingoing.mp4"),
    ("video20", "Property tree- entering a rent increase.mp4"),
    ("video21", "TPS Portal- entering a new property.mp4"),
    ("video22", "TPS- Lease renewal and increase - 1.mp4"),
    ("video23", "TPS- Lease renewal and increase - 2.mp4"),
    ("video24", "TPS- Lease renewal and increase - 3.mp4"),
]


def extract_frames(video_id: str, filename: str) -> int:
    src = os.path.join(VIDEO_DIR, filename)
    if not os.path.isfile(src):
        print(f"  SKIP — file not found: {src}")
        return 0

    out_dir = os.path.join(FRAMES_DIR, video_id)
    os.makedirs(out_dir, exist_ok=True)

    existing = [f for f in os.listdir(out_dir) if f.endswith(".jpg")]
    if existing:
        print(f"  Already extracted {len(existing)} frames — skipping")
        return len(existing)

    cmd = [
        FFMPEG, "-i", src,
        "-vf", f"fps=1/{INTERVAL}",
        "-q:v", "2",
        "-vsync", "vfr",
        os.path.join(out_dir, f"{video_id}_frame_%04d.jpg"),
    ]

    result = subprocess.run(
        cmd, capture_output=True, text=True, timeout=300
    )
    if result.returncode != 0:
        print(f"  ERROR: ffmpeg returned {result.returncode}")
        print(f"  stderr: {result.stderr[-500:]}")
        return 0

    frames = [f for f in os.listdir(out_dir) if f.endswith(".jpg")]
    return len(frames)


def main():
    os.makedirs(FRAMES_DIR, exist_ok=True)
    total = 0

    for video_id, filename in VIDEOS:
        print(f"\n{'='*60}")
        print(f"Extracting frames: {video_id} — {filename}")
        print(f"{'='*60}")
        count = extract_frames(video_id, filename)
        print(f"  -> {count} frames saved to {os.path.join(FRAMES_DIR, video_id)}")
        total += count

    print(f"\n{'='*60}")
    print(f"DONE — {total} total frames across {len(VIDEOS)} videos")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
