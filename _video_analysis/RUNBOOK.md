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

The matrix must cover both:

1. **primary integration targets**
   - the lifecycle or SOP pages directly changed by the video finding
2. **dependency-cascade targets**
   - templates, checklists, triage pages, standards pages, and other downstream docs that may inherit the workflow change

---

## Repository Structure

```text
_video_analysis/
├── RUNBOOK.md
├── batch_config.py
├── requirements.txt
├── transcribe.py
├── transcribe_all_videos.py
├── transcribe_batch2.py
├── validate_batch.py
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
- The dated batch scripts now use `_video_analysis/batch_config.py` for the shared `VIDEOS` list and default batch date.
- `transcribe_batch2.py` and `extract_frames.py` resolve either:
  - `videos/YYYY-MM-DD/`
  - or the legacy folder name `videos/D-M-YYYY/`
- Use CLI overrides only when the source or output folder intentionally differs from the default dated batch path.

---

## Prerequisites

### Software

| Tool | Purpose | Install |
|---|---|---|
| **Python 3.12+** | Runs transcription / extraction scripts | `winget install Python.Python.3.12` or [python.org](https://www.python.org/downloads/) |
| **ffmpeg** | Audio extraction and frame capture | `choco install ffmpeg` or [ffmpeg.org](https://ffmpeg.org/download.html) |
| **openai-whisper** | Speech-to-text transcription | `py -3 -m pip install -r _video_analysis/requirements.txt` |

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
 1. Register video IDs and filenames in `batch_config.py`
          │
          ▼
 2. Run transcription (audio extraction + Whisper)
          │
          ▼
 3. Run frame extraction (JPG screenshots every N seconds)
          │
          ▼
 4. Run local batch validation
          │
          ▼
 5. Review transcript + frames together
          │
          ▼
 6. Draft analysis report per video
          │
          ▼
 6b. Draft batch synthesis + doc coverage matrix
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
- `_video_analysis/videos/1-4-2026/1. TPS Book me - creating viewings.mp4` (legacy folder naming still supported)

The analysis outputs for that batch should go under:

```text
_video_analysis/artefacts/2026-04-01/
```

---

## Step 2 — Register Videos in the Batch Config

Update `_video_analysis/batch_config.py`.

Add each new video to the shared `VIDEOS` list:

```python
VIDEOS = [
    ("video15", "1. TPS Book me - creating viewings.mp4"),
    ("video16", "2. TPS Book me - correction.mp4"),
]
```

Use sequential numbering from the latest existing video ID. The `video_id` determines the transcript and frame folder names.

Set `DEFAULT_BATCH_DATE` to the current batch date when you prepare a new dated batch:

```python
DEFAULT_BATCH_DATE = "2026-04-01"
```

The dated batch scripts will then resolve:

- source videos from `_video_analysis/videos/YYYY-MM-DD/` when present
- the matching artefacts folder under `_video_analysis/artefacts/YYYY-MM-DD/`
- a legacy source folder like `_video_analysis/videos/1-4-2026/` if that is what exists locally

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
py -3 _video_analysis/transcribe_batch2.py
```

Useful overrides:

```powershell
py -3 _video_analysis/transcribe_batch2.py --batch-date 2026-04-01
py -3 _video_analysis/transcribe_batch2.py --video-id video15 --video-id video16
py -3 _video_analysis/transcribe_batch2.py --video-dir "_video_analysis/videos/1-4-2026"
```

### Outputs

Outputs are written into the dated artefacts folder:

- `_video_analysis/artefacts/YYYY-MM-DD/audio/{video_id}_audio.wav`
- `_video_analysis/artefacts/YYYY-MM-DD/{video_id}_transcript.json`
- `_video_analysis/artefacts/YYYY-MM-DD/{video_id}_transcript.txt`

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

Useful overrides:

```powershell
py -3 _video_analysis/extract_frames.py --batch-date 2026-04-01
py -3 _video_analysis/extract_frames.py --video-id video15 --video-id video16
py -3 _video_analysis/extract_frames.py --video-dir "_video_analysis/videos/1-4-2026"
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

## Step 5 — Run Local Batch Validation

Before drafting analysis or updating docs, validate that the batch has the minimum required evidence:

```powershell
py -3 _video_analysis/validate_batch.py --batch-date 2026-04-01
```

Optional targeted validation:

```powershell
py -3 _video_analysis/validate_batch.py --video-id video15 --video-id video16
```

The validator checks for:

- transcript `.json` and `.txt` outputs for each configured video
- at least one extracted `.jpg` frame for each configured video

Do **not** proceed to doc integration while this validation fails.

Before closing the batch, rerun the validator with the coverage matrix requirement enabled:

```powershell
py -3 _video_analysis/validate_batch.py --batch-date 2026-04-01 --require-coverage-matrix
```

---

## Step 6 — Review Transcript and Frames Together

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

## Step 7 — Draft the Analysis Report

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

## System Location Mapping

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

### Navigation and webpage mapping requirement

Every per-video analysis report must explicitly capture **where** the workflow happens in the product:

- **System name** (TPS, BookMe, Property Tree, Tapi, Inspection Express, etc.)
- **Page / screen name**
- **URL or page address** if visible
- **Navigation path** used to reach it, e.g. `Properties → [property] → Agreements → Renewal`
- **Key action points** in order, using the exact menu / button / tab labels shown on screen

The goal is that a user can identify both:

1. which webpage / screen the action belongs to
2. how to navigate there from the product's normal starting point

---

## Step 7b — Create the Batch Coverage Matrix

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
| **Page / navigation mapping** | System, page name, visible URL if any, and navigation path |
| **Primary docs reviewed** | Which main lifecycle / SOP pages were checked |
| **Dependent docs checked** | Which templates, checklists, triage pages, standards pages, or related docs were checked because of the finding |
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
4. every material finding has an explicit dependency-cascade check recorded for:
   - templates
   - checklists / QA
   - triage / operations pages
   - standards / systems-map pages where relevant

---

## Step 8 — Read the Current Documentation Baseline

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

## Step 9 — Integrate Findings into `docs/`

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
9. **Add navigation cues** so the user can find the screen, not just understand the rule.
10. **Add a verified label** to sections materially updated from analysed video evidence.

### Dependency-cascade rule

Do not treat the main SOP update as the end of the change.

For each material video finding, explicitly check whether it also changes:

- **templates** in `docs/day-to-day/notice-email-templates.md`
- **daily / weekly operations pages** such as `daily-triage.md` and `weekly-operations.md`
- **execution / QA checklists**
- **lifecycle pages**
- **systems / standards pages**

The coverage matrix must record that dependency pass even when the result is **already aligned** or **not applicable**.

### Verified label convention

When a section has been materially updated from proper video analysis, add this subtle label directly under the heading or opening line of the section:

```html
<span class="pp-verified-label">Verified from video analysis</span>
```

Use it when:

- the section was materially updated from transcript + frame review
- the workflow, UI wording, or decision logic was checked against analysed video evidence

Do **not** use it when:

- the section is only based on prior written docs
- the section only received wording cleanup or formatting changes
- the source evidence was incomplete or uncertain

### Navigation cue convention

For workflow sections derived from video analysis, include explicit location cues where helpful, for example:

- `Navigate to: Properties → [property] → Agreements`
- `Location: Book a viewing → Enquiries`
- `URL observed: tpportal.co.nz/clients/bookme/overview`

Prefer concise cues that help the user find the correct page quickly.

### Typical dependency pattern

If a new video changes workflow understanding:

1. lifecycle page
2. step-level SOP
3. templates
4. checklist / QA pages
5. systems map / standards if policy or system capability changed

---

## Step 10 — Verify Consistency

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
- each meaningful finding has a recorded dependency-cascade disposition
- templates, checklists, and triage pages have been explicitly marked as updated / already aligned / not applicable

---

## Step 11 — Commit the Right Files

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
| Frame coverage is too sparse | Lower `INTERVAL` in `extract_frames.py` and rerun the affected `--video-id` batch |
| Script skips a video | Delete the prior output for that `video_id` or change the ID if the batch is intentionally new |
| Analysis report is missing key UI detail | Go back to the extracted frames before changing the docs |

---

## Non-Negotiables

- Use **both** transcripts and frames for workflow analysis
- Produce a **per-video analysis report** for every video in the batch
- Produce a **doc coverage matrix** before closing the batch
- Use the matrix to track **dependent docs checked**, not just the primary SOP targets
- Update `docs/`, not any legacy `workflow/` paths
- Treat the analysis report as a synthesis artefact, not as the final published documentation
- Never commit generated video artefacts
