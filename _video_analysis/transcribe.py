"""Transcribe a single video file using OpenAI Whisper.

Usage:
    py -3 _video_analysis/transcribe.py <video_id> <path_to_video>

Example:
    py -3 _video_analysis/transcribe.py video15 "videos/New Training Video.mp4"

Output is written to _video_analysis/videos/{video_id}_transcript.{json,txt}
Audio is extracted to _video_analysis/videos/{video_id}_audio.wav
"""
import whisper
import json
import os
import subprocess
import sys
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "videos")
FFMPEG = os.environ.get("FFMPEG_PATH", "ffmpeg")
FFMPEG_TIMEOUT = 900  # 15 min safety bound per file


def transcribe_video(vid_id: str, src_path: str) -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    wav_path = os.path.join(OUTPUT_DIR, f"{vid_id}_audio.wav")
    json_path = os.path.join(OUTPUT_DIR, f"{vid_id}_transcript.json")
    txt_path = os.path.join(OUTPUT_DIR, f"{vid_id}_transcript.txt")

    if not os.path.exists(src_path):
        print(f"[ERROR] Video file not found: {src_path}")
        sys.exit(1)

    if os.path.exists(txt_path):
        print(f"[SKIP] {vid_id} — transcript already exists at {txt_path}")
        print("       Delete it to force re-processing.")
        return

    if not os.path.exists(wav_path):
        print(f"Extracting audio from {src_path}...")
        t0 = time.time()
        cmd = [FFMPEG, "-y", "-i", src_path, "-vn", "-acodec", "pcm_s16le",
               "-ar", "16000", "-ac", "1", wav_path]
        try:
            subprocess.run(
                cmd, capture_output=True, text=True,
                check=True, timeout=FFMPEG_TIMEOUT,
            )
        except subprocess.TimeoutExpired:
            print(f"[ERROR] ffmpeg timed out after {FFMPEG_TIMEOUT}s")
            if os.path.exists(wav_path):
                os.remove(wav_path)
            sys.exit(1)
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] ffmpeg failed: {e.stderr[:500] if e.stderr else 'no stderr'}")
            if os.path.exists(wav_path):
                os.remove(wav_path)
            sys.exit(1)
        print(f"Audio extracted in {time.time() - t0:.1f}s")

    print("Loading Whisper model (base)...")
    model = whisper.load_model("base")

    print("Transcribing...")
    t0 = time.time()
    transcript = model.transcribe(wav_path, language="en", verbose=False, word_timestamps=True)
    print(f"Transcription done in {time.time() - t0:.1f}s")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(transcript, f, indent=2, ensure_ascii=False)

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(f"# Transcript — {vid_id}\n")
        f.write(f"# Source: {os.path.basename(src_path)}\n\n")
        for seg in transcript["segments"]:
            start_m, start_s = int(seg["start"] // 60), int(seg["start"] % 60)
            end_m, end_s = int(seg["end"] // 60), int(seg["end"] % 60)
            f.write(f"[{start_m:02d}:{start_s:02d} - {end_m:02d}:{end_s:02d}] {seg['text'].strip()}\n")

    seg_count = len(transcript["segments"])
    char_count = len(transcript["text"])
    print(f"Done — {seg_count} segments, {char_count} chars")
    print(f"  JSON: {json_path}")
    print(f"  TXT:  {txt_path}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    transcribe_video(sys.argv[1], sys.argv[2])
