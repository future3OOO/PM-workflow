# Runbook — Video Analysis & Documentation Integration

**Purpose:** Step-by-step process for turning new training videos into accurate workflow documentation updates using both speech transcription and frame-by-frame visual evidence.

---

## Core Method

The current analysis method has two mandatory evidence streams:

1. **Transcript evidence** from Whisper
   - captures the PM's spoken explanation, rationale, exceptions, and workflow sequencing
2. **Frame evidence** from ffmpeg screenshots
   - captures exact UI labels, fields, button names, page layouts, status badges, and system behaviour visible on screen

Do **not** rely on transcript-only analysis when the video is demonstrating a software workflow. The transcript tells you what was said; the frames tell you what was actually on screen.

There are also two mandatory synthesis outputs for every batch:

1. **Per-video analysis reports**
   - one analysis artefact per video, even if a later batch summary also exists
   - preserves low-level details that are easy to lose in grouped write-ups
2. **Doc coverage matrix**
   - a batch-level table showing which docs were checked, what changed, what was intentionally left unchanged, and any residual gaps
   - the batch is **not complete** until this matrix exists

---

## Repository Structure

```text
_video_analysis/
├── RUNBOOK.md
├── transcribe.py
├── transcribe_all_videos.py
├── extract_frames.py
├── videos/                         # source videos + transcript outputs (gitignored)
│   └── YYYY-MM-DD/                 # optional date-based source batch folders
└── artefacts/                      # generated review outputs (gitignored)
    └── YYYY-MM-DD/
        ├── analysis/               # per-video analysis reports
        └── frames/
            └── videoXX/            # extracted JPG frames per video
```

### Important structure notes

- The **documentation source** now lives in `docs/`, not the old `workflow/` folder.
- Analysis outputs should be grouped by date under `_video_analysis/artefacts/YYYY-MM-DD/`.
- The current scripts are still batch-oriented:
  - `transcribe_all_videos.py` writes transcript outputs to `_video_analysis/videos/`
  - `extract_frames.py` uses explicit `VIDEO_DIR`, `FRAMES_DIR`, and `VIDEOS` values that should be updated for the current batch before running

---

## Prerequisites

### Software

| Tool | Purpose | Install |
|---|---|---|
| **Python 3.12+** | Runs transcription / extraction scripts | `winget install Python.Python.3.12` or [python.org](https://www.python.org/downloads/) |
| **ffmpeg** | Audio extraction and frame capture | `choco install ffmpeg` or [ffmpeg.org](https://ffmpeg.org/download.html) |
| **openai-whisper** | Speech-to-text transcription | `pip install openai-whisper` |

### Verify installation

```powershell
py -3 --version
ffmpeg -version
py -3 -c "import whisper; print(whisper.__version__)"
```

---

## Process Overview

```text
 Place new videos in the current batch folder
          │
          ▼
 1. Register video IDs and filenames in the scripts
          │
          ▼
 2. Run transcription (audio extraction + Whisper)
          │
          ▼
 3. Run frame extraction (JPG screenshots every N seconds)
          │
          ▼
 4. Review transcript + frames together
          │
          ▼
 5. Draft analysis report per video
          │
          ▼
 6. Draft batch synthesis + doc coverage matrix
          │
          ▼
 7. Read affected docs/ pages for baseline context
          │
          ▼
 8. Integrate findings into the documentation
          │
          ▼
 9. Verify cross-document consistency against the coverage matrix
          │
          ▼
10. Commit documentation/script changes only
```

---

## Step 1 — Stage the New Video Batch

Place the raw video files in `_video_analysis/videos/`.

For larger review sessions, keep the source files in a date-based batch folder:

```text
_video_analysis/videos/2026-04-01/
```

Typical examples:

- `_video_analysis/videos/2026-04-01/1. TPS Book me - creating viewings.mp4`
- `_video_analysis/videos/2026-04-01/2. TPS Book me - correction.mp4`

The analysis outputs for that batch should go under:

```text
_video_analysis/artefacts/2026-04-01/
```

---

## Step 2 — Register Videos in the Scripts

### `transcribe_all_videos.py`

Add each new video to the `VIDEOS` list:

```python
VIDEOS = [
    ("video15", "1. TPS Book me - creating viewings.mp4"),
    ("video16", "2. TPS Book me - correction.mp4"),
]
```

Use sequential numbering from the latest existing video ID. The `video_id` determines the transcript and frame folder names.

### `extract_frames.py`

Before running the frame capture script, update:

- `VIDEO_DIR` to the current source batch folder
- `FRAMES_DIR` to the current dated artefacts folder
- `VIDEOS` to match the current batch

Example:

```python
VIDEO_DIR = os.path.join(SCRIPT_DIR, "videos", "2026-04-01")
FRAMES_DIR = os.path.join(SCRIPT_DIR, "artefacts", "2026-04-01", "frames")
```

---

## Step 3 — Run Transcription

Transcription is the spoken-evidence layer. It captures:

- exact PM explanations
- approvals logic
- exceptions and edge cases
- timing corrections
- terminology and internal shorthand

### Single video

```powershell
py -3 _video_analysis/transcribe.py video15 "_video_analysis/videos/2026-04-01/1. TPS Book me - creating viewings.mp4"
```

### Batch

```powershell
py -3 _video_analysis/transcribe_all_videos.py
```

### Outputs

Current outputs are written into `_video_analysis/videos/`:

- `{video_id}_audio.wav`
- `{video_id}_transcript.json`
- `{video_id}_transcript.txt`

The `.txt` transcript is the main review artefact for reading. The `.json` is useful when deeper timestamp inspection is needed.

---

## Step 4 — Run Frame Extraction

Frame extraction is the visual-evidence layer. It captures what the transcript cannot be trusted to describe precisely:

- page layouts
- field names
- button labels
- status badges
- dropdown options
- template names
- exact order of UI interactions

Run:

```powershell
py -3 _video_analysis/extract_frames.py
```

### Output

Frames are written to the dated artefacts folder:

```text
_video_analysis/artefacts/YYYY-MM-DD/frames/video15/video15_frame_0001.jpg
_video_analysis/artefacts/YYYY-MM-DD/frames/video16/video16_frame_0001.jpg
```

### Default cadence

The current script captures one frame every `INTERVAL` seconds. At present that value is:

```python
INTERVAL = 10
```

Lower the interval if the workflow is moving quickly and you need denser UI evidence.

---

## Step 5 — Review Transcript and Frames Together

This is the key analysis step.

### What the transcript is best for

- direct PM quotes
- reasoning behind a decision
- policy explanations
- timing corrections
- commentary about system quirks or bugs

### What the frames are best for

- exact page names and URLs
- field labels and option names
- button text
- visible warnings and notes
- dashboard metrics
- tenant-facing emails, portals, and forms

### Review rule

When transcript and frame evidence appear to conflict:

1. Use the **frame** for UI facts
2. Use the **transcript** for intent, rationale, and commentary
3. Note the discrepancy explicitly in the analysis report

---

## Step 6 — Draft the Analysis Report

Create the report in the dated analysis folder:

```text
_video_analysis/artefacts/YYYY-MM-DD/analysis/
```

Example:

```text
_video_analysis/artefacts/2026-04-01/analysis/video15_analysis.md
```

If a grouped topic summary is useful, create it **in addition to** the per-video reports, not instead of them.

### Recommended report structure

```markdown
# Video Analysis Report: [Topic]

## Executive Summary

## Video Details

## UI Walkthrough

## Workflow Logic

## PM Quotes & Context

## System Features Demonstrated

## Complete Field & Label Reference

## Gap Analysis

## Integration Targets
```

### Analysis standard

The report should be specific enough that someone could update the docs **without rewatching the video**, because the report already synthesises:

- transcript evidence
- frame evidence
- workflow interpretation
- documentation gaps

### Per-video requirement

Even when several videos cover the same topic, still produce a separate analysis report for each video ID first. Batch summaries are useful for synthesis, but the per-video report is the canonical evidence-preservation artefact.

---

## Step 6b — Create the Batch Coverage Matrix

Before editing is considered complete, create a batch-level **doc coverage matrix** in the dated analysis folder.

Recommended filename:

```text
_video_analysis/artefacts/YYYY-MM-DD/analysis/doc_coverage_matrix.md
```

### Required columns

| Column | Purpose |
|---|---|
| **Video ID** | Which source video produced the finding |
| **Finding / workflow** | The operational detail, UI fact, or rule identified |
| **Evidence source** | Transcript, frames, or both |
| **Target docs reviewed** | Which `docs/` pages were checked |
| **Action taken** | Updated / already covered / intentionally not documented |
| **Result** | File(s) changed or reason no change was needed |
| **Residual risk / follow-up** | Anything still uncertain or deferred |

### Closing rule

Do **not** close a batch, commit the batch as complete, or state that integration is finished until:

1. every video has a per-video analysis report
2. the doc coverage matrix exists
3. every material finding is mapped to:
   - a doc update, or
   - an explicit “already covered” judgment, or
   - an explicit “not suitable for docs” judgment with reason

---

## Step 7 — Read the Current Documentation Baseline

Before editing anything, read the relevant pages in `docs/`.

### Core baseline docs

| File | Why it matters |
|---|---|
| `docs/getting-started/systems-map.md` | System roles, ownership, and data flows |
| `docs/getting-started/standards-slas.md` | Policies, approval thresholds, and service rules |
| `docs/day-to-day/contributing.md` | Authoring conventions and update order |

### Topic-specific examples

| Topic | Primary docs |
|---|---|
| Leasing / TPS / BookMe | `docs/leasing/leasing-lifecycle.md`, `docs/leasing/tps-viewings-bookme.md`, `docs/onboarding/tps-property-setup.md` |
| Maintenance / Tapi | `docs/maintenance/maintenance-lifecycle.md`, `docs/maintenance/tapi-intake.md`, `docs/maintenance/tapi-invoices.md` |
| Inspections | `docs/inspections/inspection-lifecycle.md`, `docs/inspections/pt-scheduling.md`, `docs/inspections/inspection-express.md` |
| Renewals / Rent increases | `docs/renewals-exits/renewals-rent-reviews.md`, `docs/day-to-day/notices-comms.md`, `docs/day-to-day/sources.md` |
| Templates / operational follow-up | `docs/day-to-day/notice-email-templates.md`, `docs/day-to-day/daily-triage.md`, `docs/day-to-day/weekly-operations.md` |

---

## Step 8 — Integrate Findings into `docs/`

Update the relevant documentation pages using the analysis report as the synthesis source.

### Integration rules

1. **Merge, don't duplicate.**
2. **Preserve structure.**
3. **Write operational instructions, not video narration.**
4. **Use exact UI wording** from the frames where possible.
5. **Use transcript quotes sparingly** and only when the PM's wording adds important context.
6. **Update all dependent docs** if a lifecycle, SOP, template, or checklist is affected.
7. **Bump version and date** on every changed documentation file.
8. **Update the coverage matrix** as you go so every material finding has a documented disposition.

### Typical dependency pattern

If a new video changes workflow understanding:

1. lifecycle page
2. step-level SOP
3. templates
4. checklist / QA pages
5. systems map / standards if policy or system capability changed

---

## Step 9 — Verify Consistency

After the docs are updated, run a consistency pass.

### 1. Naming checks

```powershell
rg -i "tarpy|tappy|tarpie" docs/
rg "tarpy\.co\.nz" docs/ README.md
```

### 2. Version dates

```powershell
rg "Last updated" docs/
```

### 3. Cross-reference sanity

```powershell
Get-ChildItem docs/ -Recurse -Filter *.md -Name
```

### 4. Staged files check

```powershell
git status
```

Only documentation pages and intentional script/instruction changes should be staged.

### 5. Coverage matrix closure check

Before considering the batch done, confirm:

- every analysed video has a per-video report
- the batch coverage matrix exists
- each meaningful finding has a recorded disposition
- no changed doc is missing from the matrix

---

## Step 10 — Commit the Right Files

Commit:

- `docs/` pages that were intentionally updated
- `_video_analysis/*.py` if scripts changed
- `_video_analysis/RUNBOOK.md`
- `CLAUDE.md`
- `AGENTS.md`

Do **not** commit:

- source video files
- converted videos
- audio files
- transcripts
- extracted frames
- analysis report drafts

Example:

```powershell
git checkout -b feature/video-workflow-update
git add docs/ _video_analysis/*.py _video_analysis/RUNBOOK.md CLAUDE.md AGENTS.md
git commit -m "docs: integrate training video findings and update agent guidance"
git push -u origin HEAD
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `ffmpeg` not found | Use `FFMPEG_PATH` env var or install ffmpeg into PATH |
| `python` not found | Use `py -3` launcher |
| Whisper memory pressure | Switch from `base` to `tiny` temporarily |
| Transcript quality is weak | Re-check against the frames; NZ accents and product jargon often distort the transcript |
| Frame coverage is too sparse | Lower `INTERVAL` in `extract_frames.py` |
| Script skips a video | Delete the prior output for that `video_id` or change the ID if the batch is intentionally new |
| Analysis report is missing key UI detail | Go back to the extracted frames before changing the docs |

---

## Non-Negotiables

- Use **both** transcripts and frames for workflow analysis
- Produce a **per-video analysis report** for every video in the batch
- Produce a **doc coverage matrix** before closing the batch
- Update `docs/`, not any legacy `workflow/` paths
- Treat the analysis report as a synthesis artefact, not as the final published documentation
- Never commit generated video artefacts
