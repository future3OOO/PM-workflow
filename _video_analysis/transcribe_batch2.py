"""Extract audio and transcribe the 10 new training videos (2026-04-01 batch)."""
import whisper
import json
import os
import subprocess
import sys
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEO_DIR = os.path.join(SCRIPT_DIR, "videos", "1-4-2026")
ARTEFACT_DIR = os.path.join(SCRIPT_DIR, "artefacts", "2026-04-01")
AUDIO_DIR = os.path.join(ARTEFACT_DIR, "audio")
FFMPEG = os.environ.get(
    "FFMPEG_PATH", r"C:\ProgramData\chocolatey\bin\ffmpeg.exe"
)
FFMPEG_TIMEOUT = 900

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

os.makedirs(AUDIO_DIR, exist_ok=True)

print("Loading Whisper model (base)...")
model = whisper.load_model("base")
print("Model loaded.\n")

for vid_id, filename in VIDEOS:
    src = os.path.join(VIDEO_DIR, filename)
    wav_path = os.path.join(AUDIO_DIR, f"{vid_id}_audio.wav")
    json_path = os.path.join(ARTEFACT_DIR, f"{vid_id}_transcript.json")
    txt_path = os.path.join(ARTEFACT_DIR, f"{vid_id}_transcript.txt")

    if not os.path.exists(src):
        print(f"[SKIP] {filename} — file not found at {src}")
        continue

    if os.path.exists(txt_path):
        print(f"[SKIP] {vid_id} ({filename}) — transcript already exists")
        continue

    print(f"\n{'='*70}")
    print(f"Processing {vid_id}: {filename}")
    print(f"{'='*70}")

    if not os.path.exists(wav_path):
        print(f"  Extracting audio...")
        t0 = time.time()
        cmd = [FFMPEG, "-y", "-i", src, "-vn", "-acodec", "pcm_s16le",
               "-ar", "16000", "-ac", "1", wav_path]
        try:
            subprocess.run(
                cmd, capture_output=True, text=True,
                check=True, timeout=FFMPEG_TIMEOUT,
            )
        except subprocess.TimeoutExpired:
            print(f"  [ERROR] ffmpeg timed out after {FFMPEG_TIMEOUT}s")
            if os.path.exists(wav_path):
                os.remove(wav_path)
            continue
        except subprocess.CalledProcessError as e:
            print(f"  [ERROR] ffmpeg failed: {e.stderr[:500] if e.stderr else 'no stderr'}")
            if os.path.exists(wav_path):
                os.remove(wav_path)
            continue
        print(f"  Audio extracted in {time.time() - t0:.1f}s")
    else:
        print(f"  Audio already extracted, skipping ffmpeg")

    print(f"  Transcribing...")
    t0 = time.time()
    transcript = model.transcribe(
        wav_path, language="en", verbose=False, word_timestamps=True,
    )
    elapsed = time.time() - t0
    print(f"  Transcription done in {elapsed:.1f}s")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(transcript, f, indent=2, ensure_ascii=False)
    print(f"  JSON saved: {json_path}")

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(f"# Transcript — {vid_id}\n")
        f.write(f"# Source: {filename}\n\n")
        for seg in transcript["segments"]:
            start_m = int(seg["start"] // 60)
            start_s = int(seg["start"] % 60)
            end_m = int(seg["end"] // 60)
            end_s = int(seg["end"] % 60)
            f.write(f"[{start_m:02d}:{start_s:02d} - {end_m:02d}:{end_s:02d}] {seg['text'].strip()}\n")
    print(f"  TXT saved: {txt_path}")

    seg_count = len(transcript["segments"])
    if seg_count == 0:
        print(f"  WARNING: No segments transcribed for {vid_id}")
    else:
        char_count = len(transcript["text"])
        duration_s = transcript["segments"][-1]["end"]
        duration_m = int(duration_s // 60)
        duration_r = int(duration_s % 60)
        print(f"  Duration: {duration_m}m{duration_r}s | Segments: {seg_count} | Chars: {char_count}")
        print(f"  Preview: {transcript['text'][:300]}...")

    sys.stdout.flush()

print("\n\n" + "="*70)
print("ALL DONE — All transcripts saved to " + ARTEFACT_DIR)
print("="*70)
