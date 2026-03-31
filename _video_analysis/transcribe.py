"""Transcribe both video audio files using OpenAI Whisper with timestamps."""
import whisper
import json
import os

AUDIO_DIR = os.path.dirname(os.path.abspath(__file__))

# Use the 'base' model — good balance of speed and accuracy
print("Loading Whisper model (base)...")
model = whisper.load_model("base")

for idx, filename in enumerate(["video1_audio.wav", "video2_audio.wav"], start=1):
    path = os.path.join(AUDIO_DIR, filename)
    print(f"\n{'='*60}")
    print(f"Transcribing Video {idx}: {filename}")
    print(f"{'='*60}")
    
    result = model.transcribe(
        path,
        language="en",
        verbose=False,
        word_timestamps=True
    )
    
    # Save full JSON result
    json_path = os.path.join(AUDIO_DIR, f"video{idx}_transcript.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    print(f"  JSON saved: {json_path}")
    
    # Save readable text with timestamps
    txt_path = os.path.join(AUDIO_DIR, f"video{idx}_transcript.txt")
    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(f"# Transcript — Video {idx}\n")
        f.write(f"# Source: {filename}\n\n")
        for seg in result["segments"]:
            start_m = int(seg["start"] // 60)
            start_s = int(seg["start"] % 60)
            end_m = int(seg["end"] // 60)
            end_s = int(seg["end"] % 60)
            timestamp = f"[{start_m:02d}:{start_s:02d} - {end_m:02d}:{end_s:02d}]"
            f.write(f"{timestamp} {seg['text'].strip()}\n")
    print(f"  TXT saved: {txt_path}")
    
    # Print full text summary
    print(f"\n  Full text ({len(result['text'])} chars):")
    print(f"  {result['text'][:500]}...")

print("\n\nDone! Both transcripts saved.")
