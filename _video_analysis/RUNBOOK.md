# Runbook — Video Analysis & Workflow Integration

**Purpose:** Step-by-step process for taking new training videos, extracting their content, and integrating the learnings into the agentic workflow documentation.

---

## Prerequisites

### Software

| Tool | Purpose | Install |
|---|---|---|
| **Python 3.12+** | Runs transcription scripts | `winget install Python.Python.3.12` or [python.org](https://www.python.org/downloads/) |
| **ffmpeg** | Extracts audio from video files | `choco install ffmpeg` or [ffmpeg.org](https://ffmpeg.org/download.html) |
| **openai-whisper** | Speech-to-text transcription | `pip install openai-whisper` |

### Verify installation

```powershell
py -3 --version          # Python 3.12.x
ffmpeg -version          # ffmpeg 6.x+
py -3 -c "import whisper; print(whisper.__version__)"
```

---

## Process Overview

```
 Upload videos to _video_analysis/videos/
          │
          ▼
 1. Register new videos in transcribe_all_videos.py
          │
          ▼
 2. Run transcription script (audio extraction + Whisper)
          │
          ▼
 3. Convert any MKV files to MP4 (for visual review)
          │
          ▼
 4. Review each video (visual UI walkthrough + transcript)
          │
          ▼
 5. Draft analysis report per video
          │
          ▼
 6. Read all current workflow docs to understand baseline
          │
          ▼
 7. Integrate findings into workflow documentation
          │
          ▼
 8. Verify consistency across all docs
          │
          ▼
 9. Commit workflow changes and open PR
```

---

## Step 1 — Place Videos & Register Them

1. Place all new video files (MP4 or MKV) into `_video_analysis/videos/`.

2. Open `_video_analysis/transcribe_all_videos.py` and add entries to the `VIDEOS` list. Each entry is a tuple of `(video_id, filename)`:

```python
VIDEOS = [
    # Existing entries...
    ("video15", "New Training Video Title.mp4"),
    ("video16", "Another Training Video.mkv"),
]
```

Use sequential numbering from the last video ID. The `video_id` determines output filenames.

---

## Step 2 — Run Transcription

The script extracts audio via ffmpeg, then transcribes using Whisper (base model). It skips already-processed videos automatically.

```powershell
cd <repo-root>
py -3 _video_analysis/transcribe_all_videos.py
```

**Output per video** (saved to `_video_analysis/videos/`):
- `{video_id}_audio.wav` — extracted audio (16kHz mono)
- `{video_id}_transcript.json` — full Whisper output with word-level timestamps
- `{video_id}_transcript.txt` — human-readable timestamped transcript

**Expect:** ~1-3 minutes per video depending on length and hardware. The script prints progress and a preview of each transcript.

---

## Step 3 — Convert MKV to MP4 (If Needed)

MKV files need conversion to MP4 for visual review in Cursor's video review tools. MP4 files can be skipped.

```powershell
$ffmpeg = "C:\ProgramData\chocolatey\bin\ffmpeg.exe"
$inputDir = "videos"
$outputDir = "_video_analysis\videos"

Get-ChildItem "$inputDir\*.mkv" | ForEach-Object {
    $out = Join-Path $outputDir ($_.BaseName + ".mp4")
    if (-not (Test-Path $out)) {
        & $ffmpeg -i $_.FullName -c:v libx264 -c:a aac -movflags +faststart $out
    }
}
```

---

## Step 4 — Review Each Video

Each video must be reviewed for **both** spoken content and visual UI context. Transcripts alone miss critical information like button locations, screen layouts, and workflow sequences visible on screen.

### What to capture per video

- **UI walkthrough:** Every screen, panel, button, dropdown, and field shown
- **Workflow logic:** Decision points, branching paths, system behaviour
- **PM quotes:** Direct quotes where the PM explains rationale or gives tips
- **System features:** Tapi/Property Tree/Inspection Express functionality demonstrated
- **Contractor/trade references:** Named contractors, trade categories, pricing
- **Terminology:** System-specific terms, internal jargon, abbreviations
- **Gaps:** Anything the video demonstrates that isn't in the current workflow docs

### Using Cursor's video review

In Cursor, use the Task tool with video review subagents to analyse MP4 files. Provide the transcript alongside the video for combined context. Example prompt structure:

> Analyse this Tapi training video. The transcript is provided below. Capture: (1) complete UI walkthrough with every screen/button/field, (2) workflow logic and decision points, (3) direct PM quotes, (4) system features demonstrated, (5) gap analysis against existing workflow docs.

---

## Step 5 — Draft Analysis Reports

For each video, produce a structured analysis report. These are working documents used during integration — they don't need to be committed to the repo. Store them in the `artefacts/` folder organised by date:

```
_video_analysis/artefacts/YYYY-MM-DD/
```

For example, analysis reports from a session on 2026-04-15 would go in `_video_analysis/artefacts/2026-04-15/`. This folder is gitignored.

### Recommended report structure

```markdown
# Video Analysis — [Video Title]

## Video Details
- **File:** filename.mp4
- **Duration:** Xm Ys
- **Topic:** Brief description

## UI Walkthrough
Step-by-step of every screen shown...

## Workflow Logic
Decision trees, branching paths...

## PM Quotes & Context
Direct quotes with timestamps...

## System Features Demonstrated
Buttons, fields, automations...

## Gap Analysis
What's new vs. what's already documented...

## Integration Targets
Which workflow docs need updating and what to add...
```

---

## Step 6 — Read Current Workflow Documentation

Before making any changes, read all the workflow docs that may be affected. The key files for maintenance/Tapi topics are:

| File | Content |
|---|---|
| `workflow/00.1_MASTER_INDEX_WORKFLOW_V2.md` | Top-level index with system summaries |
| `workflow/00.2_SYSTEMS_MAP_DATA_FLOW_V2.md` | System descriptions and data flows |
| `workflow/00.3_STANDARDS_SLAS_APPROVALS_RECORDS_V2.md` | Policies, SLAs, approval rules |
| `workflow/01_PLAYBOOK_MAINTENANCE_TAPI_V2.md` | High-level maintenance lifecycle |
| `workflow/02_SOP_TAPI_INTAKE_TRIAGE_APPROVALS_WORKORDERS_V2.md` | Detailed Tapi operations |
| `workflow/02_SOP_TAPI_INVOICES_OWNER_TENANT_DIY_SYNC_TO_PROPERTYTREE_V2.md` | Invoice processing & Property Tree sync |
| `workflow/02_SOP_INSPECTION_EXPRESS_REPORT_PUBLISH_ACTIONS_TO_TAPI_V2.md` | Inspection Express to Tapi flow |
| `workflow/03_TEMPLATES_NOTICES_EMAILS_V2.md` | Email templates |
| `workflow/04_QA_DAILY_TRIAGE_CHECKLIST_V2.md` | Daily checklist |
| `workflow/04_QA_WEEKLY_OPERATIONS_CHECKLIST_V2.md` | Weekly checklist |

For non-Tapi topics (leasing, onboarding, compliance, etc.), consult the corresponding playbooks and SOPs in `workflow/`.

---

## Step 7 — Integrate Findings

Update each affected workflow document with the new information. Follow these principles:

### Integration rules

1. **Merge, don't duplicate.** If the video confirms something already documented, leave it. Only add what's new or corrects what's wrong.
2. **Preserve structure.** Follow the existing section numbering, formatting, and heading conventions of each document.
3. **Be specific.** Include exact field names, button labels, dropdown options, and system behaviour as shown in the video.
4. **Add context, not narration.** Write operational instructions ("Click Approve to trigger auto-close and Property Tree sync"), not video summaries ("In the video, the PM clicks Approve").
5. **Update version and date.** Bump the version number and set `Last updated` to today's date on every file you change.
6. **Cross-reference.** If a new workflow spans multiple documents (e.g., invoice entry in the SOP and a template in Templates), update all of them and add section cross-references.

### Common integration targets by video topic

| Video topic | Primary doc | Also update |
|---|---|---|
| Dashboard / overview | Playbook, Systems Map | Master Index |
| Triage / intake | Intake SOP | Standards (approval rules) |
| Work orders / dispatch | Intake SOP | Templates (contractor emails) |
| Invoices | Invoice SOP | QA Daily Checklist, Systems Map |
| Approvals | Intake SOP, Standards | Templates (owner emails) |
| Inspections | Inspection Express SOP | Playbook |
| Tenant requests | Intake SOP | Templates (tenant comms) |

---

## Step 8 — Verify Consistency

After all updates, run a consistency check:

1. **Spelling:** Grep for common misspellings (the system is called **Tapi**, the email is `propertypartner@tapi.co.nz`)
   ```powershell
   rg -i "tarpy|tappy|tarpie" workflow/
   ```

2. **Cross-references:** Confirm all filenames referenced in the Master Index match actual files
   ```powershell
   rg "\.md" workflow/00.1_MASTER_INDEX_WORKFLOW_V2.md
   Get-ChildItem workflow/*.md -Name
   ```

3. **Version dates:** All updated files should show the same `Last updated` date
   ```powershell
   rg "Last updated" workflow/
   ```

4. **Section numbering:** Skim each updated doc to confirm sections are sequential and no numbers were skipped or duplicated.

---

## Step 9 — Commit & PR

Only commit the **workflow documentation changes** and the **Python scripts**. Do not commit:
- Video files (MP4, MKV, WAV)
- Extracted frames
- Video analysis report drafts
- Transcript files (JSON, TXT)

```powershell
git checkout -b feature/tapi-workflow-vX.X-description
git add workflow/ _video_analysis/*.py _video_analysis/RUNBOOK.md
git commit -m "docs: integrate N new training videos into workflow VX.X"
git push -u origin HEAD
gh pr create --title "docs: ..." --body "..."
```

The PR description should list which videos were processed and which workflow docs were changed.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `ffmpeg` not found | Use full path: `C:\ProgramData\chocolatey\bin\ffmpeg.exe` or add to PATH |
| `python` not found | Use `py -3` launcher, or full path: `C:\Users\Property Partner\AppData\Local\Programs\Python\Python312\python.exe` |
| Whisper runs out of memory | Switch to `tiny` model in the script (`whisper.load_model("tiny")`) — less accurate but lower RAM |
| MKV conversion fails | Check ffmpeg supports the codec: `ffmpeg -i input.mkv` to inspect streams |
| Transcript has poor accuracy | NZ accents and property jargon may cause errors — cross-reference with the video visually |
| Script skips a video | It skips if the transcript `.txt` already exists — delete it to force re-processing |
