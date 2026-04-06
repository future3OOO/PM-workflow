# Runbook — Video Analysis & Documentation Integration (Default)

**Purpose:** Default workflow for turning training videos into accurate documentation updates with maximum-detail evidence extraction, richer per-video reports, and stronger evidence preservation than the superseded standard runbook.

---

## Core Method

The current analysis method has two mandatory evidence streams:

1. **Transcript evidence** from Whisper
   - captures the PM's spoken explanation, rationale, exceptions, and workflow sequencing
2. **Frame evidence** from ffmpeg screenshots
   - captures exact UI labels, fields, button names, page layouts, status badges, and system behaviour visible on screen

Do **not** rely on transcript-only analysis when the video is demonstrating a software workflow. The transcript tells you what was said; the frames tell you what was actually on screen.

### Operating objective

This is now the **default** video-analysis workflow for the repository.

In this runbook:

- analysis depth is prioritised over speed
- dense evidence capture is the default, not an optional second pass
- per-video reports must preserve enough detail that another operator could update the docs without reopening the video
- concise summaries do **not** replace detailed evidence logs
- first-pass UI mapping must be complete enough that a second UI-only re-review is normally unnecessary

There are also three mandatory synthesis outputs for every batch:

1. **Per-video analysis reports**
   - one analysis artefact per video, even if a later batch summary also exists
   - preserves low-level details that are easy to lose in grouped write-ups
2. **Doc coverage matrix**
   - a batch-level table showing which docs were checked, what changed, what was intentionally left unchanged, and any residual gaps
   - the batch is **not complete** until this matrix exists
3. **Published video glossary update**
   - update `docs/day-to-day/video-analysis-glossary.md` with each processed video ID, its source label, and the published workflow docs created from or materially updated from that evidence
   - the batch is **not complete** until the glossary reflects the newly processed videos

The matrix must cover both:

1. **primary integration targets**
   - the lifecycle or SOP pages directly changed by the video finding
2. **dependency-cascade targets**
   - templates, checklists, triage pages, standards pages, and other downstream docs that may inherit the workflow change

---

## Repository Structure

```text
_video_analysis/
├── RUNBOOK.md                    # superseded standard runbook; retained as legacy reference
├── RUNBOOK_PERFORMANCE.md        # default runbook
├── batch_config.py
├── requirements.txt
├── normalize_legacy_artefacts.py # optional cleanup helper for tracked pre-standard artefacts
├── transcribe.py                 # single-video wrapper over the canonical dated-batch transcription flow
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
- The dated batch scripts now use `_video_analysis/batch_config.py` for the shared `VIDEOS` registry and current default batch date.
- `transcribe.py`, `transcribe_batch2.py`, and `extract_frames.py` all write to the same dated artefact structure.
- `transcribe_batch2.py` and `extract_frames.py` resolve either:
  - `videos/YYYY-MM-DD/`
  - or the legacy folder name `videos/D-M-YYYY/`
- Batch membership is **not** hard-coded by date. The scripts scope themselves to the actual source folder or artefact folder for the run.
- Use CLI overrides when the user provides a specific video location or when the source/output folder intentionally differs from the default dated batch path.
- If you are tidying tracked historical artefacts from before this standard, use `normalize_legacy_artefacts.py` rather than ad hoc manual renames.

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
2. Run transcription (audio extraction + Whisper) against the actual provided source folder or explicit video selection
          │
          ▼
 3. Run dense frame extraction into the canonical frame folder
          │
          ▼
 4. Run local batch validation
          │
          ▼
 5. Review transcript + frames together using a three-pass method
          │
          ▼
 6. Draft a maximum-detail analysis report per video
          │
          ▼
 6b. Draft batch synthesis + doc coverage matrix
         │
         ▼
 6c. Update the published video glossary
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

Set `DEFAULT_BATCH_DATE` to the current working batch date when you prepare a new dated batch:

```python
DEFAULT_BATCH_DATE = "2026-04-01"
```

The dated batch scripts will then resolve:

- source videos from `_video_analysis/videos/YYYY-MM-DD/` when present
- the matching artefacts folder under `_video_analysis/artefacts/YYYY-MM-DD/`
- a legacy source folder like `_video_analysis/videos/1-4-2026/` if that is what exists locally

Important:

- the scripts **do not** use a hard-coded date-to-video map
- when `--video-id` is omitted, they scope to the configured video files actually present in the selected source folder
- validation falls back to the artefact folder when transcripts/frames already exist
- if the user provides a specific video folder, prefer passing `--video-dir` so the run is explicitly tied to that batch location

---

## Step 3 — Run Transcription

Transcription is the spoken-evidence layer. It captures:

- exact PM explanations
- approvals logic
- exceptions and edge cases
- timing corrections
- terminology and internal shorthand

### Single video

The single-video wrapper is only a convenience entry point. It still uses the **same**
dated artefact layout and configured `video_id` registry as the batch workflow.

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
py -3 _video_analysis/transcribe_batch2.py --video-id video15 --force
py -3 _video_analysis/transcribe_batch2.py --video-id video15 --model base
```

### Transcription quality rule

The performance workflow now defaults to the **Whisper `medium` model** for better transcript accuracy.

Use:

- `--force` when an existing transcript needs to be regenerated
- `--model base` only when hardware limits force a lighter run

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
py -3 _video_analysis/extract_frames.py --video-id video15 --interval 2
```

### Output

Frames are written to the dated artefacts folder:

```text
_video_analysis/artefacts/YYYY-MM-DD/frames/video15/video15_frame_0001.jpg
_video_analysis/artefacts/YYYY-MM-DD/frames/video16/video16_frame_0001.jpg
```

### Canonical density rule

The canonical frame set always lives in `frames/` and is extracted at **3-second intervals by default**.

Use `--interval` only when you need an even tighter rerun for a specific video. A rerun replaces the prior canonical frames for that `video_id`; it should not create a second competing frame tree.

Use a tighter rerun when:

- the operator moves rapidly between screens
- a form is filled in across several short interactions
- validation errors appear briefly
- menu paths or dropdown options are only visible for a moment
- a before/after state change matters

Typical rerun pattern:

- canonical pass at the default 3-second interval
- tighter rerun at `--interval 1` or `--interval 2` for the relevant `--video-id`
- manual frame review focused on the transition points

The goal is to preserve enough visual evidence to reconstruct the UI sequence precisely, not just approximately.

### UI-mapping completion rule

Do not stop the frame review when you merely know the business step. Keep going until you can identify:

- the exact product
- the exact page title or screen title shown
- the entry path used to reach it
- the local tab / section / modal title involved
- the key button, dropdown, or row action used

If that level of UI mapping is not captured on the first run, the UI review is incomplete.

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

Before closing the batch, rerun the validator with the full closeout requirement enabled:

```powershell
py -3 _video_analysis/validate_batch.py --batch-date 2026-04-01 --require-batch-closeout
```

`--require-batch-closeout` checks the full batch-closeout artefacts:

- transcript + frame evidence for each selected video
- `analysis/doc_coverage_matrix.md`
- one per-video analysis report per selected `video_id`
- glossary coverage in `docs/day-to-day/video-analysis-glossary.md`

---

## Step 6 — Review Transcript and Frames Together

This is the key analysis step.

### Three-pass review method

Use all three passes for each video:

1. **Transcript pass**
   - pull out timestamps for every meaningful step, rule, exception, warning, and PM explanation
2. **Frame pass**
   - review frames in order and log exact UI facts:
     - visible page title / screen title
     - page names
     - left-nav section or top-level menu
     - local tab name
     - modal / dialog title
     - tabs
     - buttons
     - dropdowns
     - field labels
     - visible URLs
     - status changes
     - validation messages
3. **Synthesis pass**
   - reconcile transcript and frames into one clean interpretation of:
     - what was said
     - what was shown
     - what the system behaviour means

Do not collapse these into a single skim read. The point of the performance run is to preserve low-level detail deliberately.

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

### Performance extraction rule

For this runbook, every video should produce:

- a timestamped action sequence
- a screen / page ledger
- a field-and-label inventory for form-heavy workflows
- an explicit rules / exceptions list
- a clear distinction between:
  - UI labels
  - business meaning
  - PM interpretation

If the draft report feels like a summary rather than an evidence artefact, it is not detailed enough.

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

## Review Method

## UI Walkthrough

## Action Ledger

## Screen / Page Ledger

## Workflow Sequence

## Workflow Logic

## Rules, Exceptions, and Edge Cases

## PM Quotes & Context

## System Features Demonstrated

## Complete Field & Label Reference

## Validation / Error States Observed

## Evidence Notes by Timestamp

## Gap Analysis

## Integration Targets
```

### Analysis standard

The report should be specific enough that someone could update the docs **without rewatching the video**, because the report already synthesises:

- transcript evidence
- frame evidence
- workflow interpretation
- documentation gaps

For the performance variant, that standard is stricter:

- the report should preserve the workflow in enough detail that very little operational meaning is lost
- the report should explain both the UI sequence and the PM's reasoning
- the report should not optimise for brevity if brevity removes useful evidence

### Per-video requirement

Even when several videos cover the same topic, still produce a separate analysis report for each video ID first. Batch summaries are useful for synthesis, but the per-video report is the canonical evidence-preservation artefact.

### Navigation and webpage mapping requirement

Every per-video analysis report must explicitly capture **where** the workflow happens in the product:

- **System name** (TPS, BookMe, Property Tree, Tapi, Inspection Express, etc.)
- **Page / screen name**
- **Visible page title / modal title** where shown
- **URL or page address** if visible
- **Navigation path** used to reach it, e.g. `Properties → [property] → Agreements → Renewal`
- **Entry point** used in the video, e.g. left nav, dashboard tile, row action, three-dot menu, tab switch
- **Local section / tab** used once on the page
- **Key action points** in order, using the exact menu / button / tab labels shown on screen

The goal is that a user can identify both:

1. which webpage / screen the action belongs to
2. how to navigate there from the product's normal starting point

The goal is also that a future operator should not need a separate second-pass UI audit just to work out what exact screen was being used.

### Required detailed evidence sections

Every per-video report in this performance run must include the following minimum artefacts.

#### 1. Action ledger

A timestamped sequence of the meaningful actions in order.

Recommended columns:

| Column | Purpose |
|---|---|
| **Timestamp** | Where the action occurs in the source video |
| **System** | TPS, Property Tree, Tapi, BookMe, Inspection Express, etc. |
| **Page / screen** | Exact location shown |
| **Page title / UI anchor** | Visible heading, modal title, or table name that proves the location |
| **Action** | What the operator does |
| **UI labels used** | Exact button / menu / field wording |
| **Observed result** | What changes on screen |
| **Doc impact** | Which workflow instruction this affects |

#### 2. Screen / page ledger

A concise inventory of the pages visited in the video.

Recommended fields:

- system
- page / screen name
- visible page title / modal title
- visible URL if present
- navigation path
- entry mechanism used in the video
- local tab / section / modal
- purpose of that screen in the workflow

#### 3. Field-and-label inventory

Required for form-heavy videos.

Recommended columns:

| Column | Purpose |
|---|---|
| **Field / label** | Exact wording shown on screen |
| **Value / option shown** | The demonstrated value, choice, or state |
| **Entry type** | Manual entry / dropdown / checkbox / auto-fill / validation |
| **Rule or note** | Important logic, caveat, or PM instruction |
| **Doc impact** | Which published doc this detail should influence |

#### 4. Rules / exceptions list

Capture:

- business rules
- system quirks
- timing requirements
- exception cases
- common mistakes to avoid

#### 5. Evidence notes by timestamp

Preserve the important moments, especially where:

- the PM explains why a step matters
- a system limitation is demonstrated
- a hidden rule becomes visible
- a workflow branch or exception appears

#### 6. UI anchor checklist

Required for every software-workflow video:

- starting screen identified
- page title identified
- navigation path identified
- local tab / modal identified where relevant
- row action / button / three-dot / dropdown anchor identified where relevant
- any cross-check screen identified separately from the main workflow screen

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
| **UI anchor captured** | Confirm page title / modal title / local tab / row action were recorded where relevant |
| **Primary docs reviewed** | Which main lifecycle / SOP pages were checked |
| **Dependent docs checked** | Which templates, checklists, triage pages, standards pages, or related docs were checked because of the finding |
| **Detailed evidence complete** | Confirm action ledger / page ledger / field inventory were completed where relevant |
| **Glossary entry** | Confirm the published glossary row added or updated for this video |
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
5. every per-video report includes the detailed evidence sections required by this performance runbook
6. every software-workflow video has complete first-pass UI mapping, including page-title and entry-path anchors
7. the published glossary has been updated for every newly processed video

---

## Step 7c — Update the Published Video Glossary

Update:

```text
docs/day-to-day/video-analysis-glossary.md
```

This page is the published bridge between local video-analysis evidence and the workflow docs that now rely on it.

### Minimum entry fields

For every newly processed video, add or update:

- **batch date**
- **video ID**
- **source video label / filename**
- **published workflow docs created from or materially updated from that video**

### Glossary rule

Do not wait until a later cleanup pass. The glossary update is part of the same batch integration work as the SOP changes.

If a video produced no published doc changes, still record it with the relevant disposition in the coverage matrix before deciding whether the glossary should note it as reviewed-only or omit it with a reason.

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
9. **Update the published glossary** so the processed videos and their downstream docs are visible in the live documentation.
10. **Add navigation cues** so the user can find the screen, not just understand the rule.
11. **Use exact UI anchors** where helpful: page titles, tab names, modal names, row actions, and left-nav sections.
12. **Add a verified label** to sections materially updated from analysed video evidence.
13. **Do not compress away useful evidence** if the richer report materially improves later auditability.

### Dependency-cascade rule

Do not treat the main SOP update as the end of the change.

For each material video finding, explicitly check whether it also changes:

- **the published glossary** in `docs/day-to-day/video-analysis-glossary.md`
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
- `Page title shown: My Applicants`
- `Entry used: Agreements row → Edit`
- `Local tab: Tenancy Profile → Inspections`

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
- the published glossary includes the newly processed videos
- each per-video report includes the detailed evidence artefacts required by this runbook
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
- `_video_analysis/RUNBOOK_PERFORMANCE.md`
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
git add docs/ _video_analysis/*.py _video_analysis/RUNBOOK.md _video_analysis/RUNBOOK_PERFORMANCE.md CLAUDE.md AGENTS.md
git commit -m "docs: integrate training video findings and update agent guidance"
git push -u origin HEAD
```

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `ffmpeg` not found | Use `FFMPEG_PATH` env var or install ffmpeg into PATH |
| `python` not found | Use `py -3` launcher |
| Whisper memory pressure | Rerun with `--model base` or `--model tiny` temporarily |
| Transcript quality is weak | Re-check against the frames; NZ accents and product jargon often distort the transcript |
| Frame coverage is too sparse | Rerun `extract_frames.py` with a tighter `--interval` for the affected `--video-id` |
| The report still feels too summary-like | Go back and add the action ledger, field inventory, and timestamped evidence notes |
| The workflow is clear but the exact screen still isn't | Rerun frames at a tighter interval and capture the page title, entry path, local tab, and row action before closing the report |
| Script skips a video | Delete the prior output for that `video_id` or change the ID if the batch is intentionally new |
| Analysis report is missing key UI detail | Go back to the extracted frames before changing the docs |

---

## Non-Negotiables

- Use **both** transcripts and frames for workflow analysis
- Produce a **per-video analysis report** for every video in the batch
- Produce a **doc coverage matrix** before closing the batch
- Update the **published video glossary** before closing the batch
- Preserve a **timestamped action ledger** and other detailed evidence artefacts in each per-video report
- Capture **complete first-pass UI mapping** including page title, entry path, local tab / modal, and key row action where relevant
- Use the matrix to track **dependent docs checked**, not just the primary SOP targets
- Update `docs/`, not any legacy `workflow/` paths
- Treat the analysis report as a synthesis artefact, not as the final published documentation
- Never commit generated video artefacts
