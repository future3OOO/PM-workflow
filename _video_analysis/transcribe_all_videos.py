"""Extract audio and transcribe all 12 Tapi training videos using OpenAI Whisper."""
import whisper
import json
import os
import subprocess
import sys
import time

VIDEO_DIR = r"C:\Users\Property Partner\Downloads\property_management_docs_v2\videos"
OUTPUT_DIR = r"C:\Users\Property Partner\Downloads\property_management_docs_v2\_video_analysis\videos"
FFMPEG = r"C:\ProgramData\chocolatey\bin\ffmpeg.exe"

VIDEOS = [
    ("video03", "3. Tapi overview and management 1.mkv"),
    ("video04", "4. Tapi overview and management 2.mkv"),
    ("video05", "Tapi- call contract first example.mkv"),
    ("video06", "Tapi- Entering Invoices 1.mp4"),
    ("video07", "Tapi- Entering Invoices 2.mp4"),
    ("video08", "Tapi- Inspection approval request.mkv"),
    ("video09", "Tapi- Inspection approval request 2.mkv"),
    ("video10", "Tapi- Job approved.mp4"),
    ("video11", "Tapi- New maintinace request from tenant via concierge.mp4"),
    ("video12", "Tapi- Quote request from owner- example 1.mp4"),
    ("video13", "Tapi- Quote request from owner- example 2.mkv"),
    ("video14", "Tapi- Send to owner for DIY.mp4"),
]

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("Loading Whisper model (base)...")
model = whisper.load_model("base")
print("Model loaded.\n")

for vid_id, filename in VIDEOS:
    src = os.path.join(VIDEO_DIR, filename)
    wav_path = os.path.join(OUTPUT_DIR, f"{vid_id}_audio.wav")
    json_path = os.path.join(OUTPUT_DIR, f"{vid_id}_transcript.json")
    txt_path = os.path.join(OUTPUT_DIR, f"{vid_id}_transcript.txt")

    if not os.path.exists(src):
        print(f"[SKIP] {filename} — file not found")
        continue

    if os.path.exists(txt_path):
        print(f"[SKIP] {vid_id} ({filename}) — transcript already exists")
        continue

    print(f"\n{'='*70}")
    print(f"Processing {vid_id}: {filename}")
    print(f"{'='*70}")

    # Step 1: Extract audio
    if not os.path.exists(wav_path):
        print(f"  Extracting audio...")
        t0 = time.time()
        cmd = [FFMPEG, "-y", "-i", src, "-vn", "-acodec", "pcm_s16le",
               "-ar", "16000", "-ac", "1", wav_path]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"  [ERROR] ffmpeg failed: {result.stderr[:500]}")
            continue
        elapsed = time.time() - t0
        print(f"  Audio extracted in {elapsed:.1f}s")
    else:
        print(f"  Audio already extracted, skipping ffmpeg")

    # Step 2: Transcribe
    print(f"  Transcribing...")
    t0 = time.time()
    transcript = model.transcribe(
        wav_path,
        language="en",
        verbose=False,
        word_timestamps=True,
    )
    elapsed = time.time() - t0
    print(f"  Transcription done in {elapsed:.1f}s")

    # Step 3: Save JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(transcript, f, indent=2, ensure_ascii=False)
    print(f"  JSON saved: {json_path}")

    # Step 4: Save readable text with timestamps
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(f"# Transcript — {vid_id}\n")
        f.write(f"# Source: {filename}\n\n")
        for seg in transcript["segments"]:
            start_m = int(seg["start"] // 60)
            start_s = int(seg["start"] % 60)
            end_m = int(seg["end"] // 60)
            end_s = int(seg["end"] % 60)
            timestamp = f"[{start_m:02d}:{start_s:02d} - {end_m:02d}:{end_s:02d}]"
            f.write(f"{timestamp} {seg['text'].strip()}\n")
    print(f"  TXT saved: {txt_path}")

    # Print summary
    char_count = len(transcript["text"])
    seg_count = len(transcript["segments"])
    duration_s = transcript["segments"][-1]["end"] if transcript["segments"] else 0
    duration_m = int(duration_s // 60)
    duration_r = int(duration_s % 60)
    print(f"  Duration: {duration_m}m{duration_r}s | Segments: {seg_count} | Chars: {char_count}")
    print(f"  Preview: {transcript['text'][:300]}...")

    sys.stdout.flush()

print("\n\n" + "="*70)
print("ALL DONE — All transcripts saved.")
print("="*70)
