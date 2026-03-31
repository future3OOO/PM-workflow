# CLAUDE.md — Project Intelligence for Property Management Workflow Docs

This file provides context, rules, and dependency maps so any AI agent working on this repository produces correct, consistent, and complete documentation updates.

---

## Project Overview

This is **Property Partner's** (Strathmore Property Limited) complete operational documentation library for NZ residential property management. It is the single source of truth for the PM and VA on how every workflow operates across all systems.

The documentation is **not code** — it is structured Markdown covering playbooks, SOPs, templates, and checklists. Changes must be treated with the same rigour as code: version-controlled, cross-referenced, and internally consistent.

---

## Repository Layout

```
property_management_docs_v2/
├── README.md                    # Project overview and full file index
├── CLAUDE.md                    # This file — agent instructions
├── .gitignore                   # Excludes video/audio/frames/analysis drafts
├── workflow/                    # All operational documentation (35 files)
│   ├── 00.x_*                   # Foundation: index, systems map, standards
│   ├── 01_PLAYBOOK_*            # Lifecycle processes (what + when)
│   ├── 02_SOP_*                 # Click-by-click system instructions (how)
│   ├── 03_TEMPLATES_*           # Copy-paste templates + checklists
│   ├── 04_QA_*                  # Daily/weekly/monthly quality checks
│   └── 99_SOURCES_NOTE_*        # External references
├── _video_analysis/             # Video integration tooling
│   ├── RUNBOOK.md               # 9-step video-to-workflow process
│   ├── transcribe.py            # Single-video CLI transcription
│   ├── transcribe_all_videos.py # Batch transcription pipeline
│   └── artefacts/               # All generated outputs organised by date (gitignored)
│       ├── 2026-03-07/          # Batch 1: reports + transcripts (video1–2)
│       └── 2026-03-31/          # Batch 2: 12 Tapi training videos
│           ├── *.md             # Analysis reports
│           ├── transcripts/     # Whisper JSON + plaintext transcripts
│           ├── audio/           # Extracted WAV files
│           └── frames/          # Extracted video frame JPGs (per-video dirs)
└── videos/                      # Source video files (gitignored)
```

---

## Critical Naming Rules

| Term | Correct | Wrong |
|---|---|---|
| Maintenance CRM | **Tapi** | Tarpy, Tappy, Tarpie, TAPE |
| Invoice email | `propertypartner@tapi.co.nz` | PropertyPartner@tarpy.co.nz, any @tarpy domain |
| Playbook filename | `01_PLAYBOOK_MAINTENANCE_TAPI_V2.md` | anything with TARPY in the name |

After any edit, run: `rg -i "tarpy\|tappy\|tarpie" workflow/` to verify zero misspellings.

---

## Document Dependency Map

Changes to one document usually require updates to others. This map shows the dependencies.

### Tier 1 — Changes here cascade everywhere
- **`00.2_SYSTEMS_MAP_DATA_FLOW_V2.md`** — if a system's capabilities change, every doc that references that system needs checking
- **`00.3_STANDARDS_SLAS_APPROVALS_RECORDS_V2.md`** — if policies/SLAs change, playbooks and SOPs must align

### Tier 2 — Playbooks drive SOPs and templates
- **Playbooks (01_)** define the lifecycle and decision logic
- When a Playbook changes, check:
  - The corresponding SOP(s) for click-level accuracy
  - Templates for email wording alignment
  - QA checklists for daily/weekly coverage

### Tier 3 — SOPs drive templates and checklists
- When an SOP adds a new workflow step, check:
  - Templates for any new comms needed
  - QA checklists for monitoring coverage

### Maintenance-specific dependency chain

```
01_PLAYBOOK_MAINTENANCE_TAPI_V2.md (lifecycle)
  ├── 02_SOP_TAPI_INTAKE_TRIAGE_APPROVALS_WORKORDERS_V2.md (intake → work order)
  ├── 02_SOP_TAPI_INVOICES_OWNER_TENANT_DIY_SYNC_TO_PROPERTYTREE_V2.md (invoices → payment)
  ├── 02_SOP_INSPECTION_EXPRESS_REPORT_PUBLISH_ACTIONS_TO_TAPI_V2.md (inspection source)
  ├── 03_TEMPLATES_NOTICES_EMAILS_V2.md (templates 7a–7k)
  ├── 04_QA_DAILY_TRIAGE_CHECKLIST_V2.md (section 6: Tapi dashboard)
  ├── 04_QA_WEEKLY_OPERATIONS_CHECKLIST_V2.md (Tapi items)
  ├── 00.2_SYSTEMS_MAP_DATA_FLOW_V2.md (Tapi + invoice sections)
  └── 00.3_STANDARDS_SLAS_APPROVALS_RECORDS_V2.md (approval policy + contractor standards)
```

### Cross-document consistency checks

After any update, verify these are aligned:

| Check | Files involved |
|---|---|
| Priority levels (Emergency/Urgent/Routine/Planned) | Playbook, SOP Intake (badge table), Standards |
| Tapi pipeline buckets (7 stages) | Playbook, SOP Intake, QA Daily Checklist |
| Invoice Approve effects (4 auto-effects) | Playbook (Stage 6), SOP Invoices (Section 8) |
| Triage cost thresholds | Playbook, SOP Intake, Standards |
| Invoice email address | SOP Invoices, Templates, Systems Map, Playbook |
| File references / filenames | Master Index, README.md, Healthy Homes Playbook (cross-ref) |
| Version + Last updated date | Every file that was changed |

---

## Update Protocol

### When updating existing documentation

1. **Read before editing.** Always read the full file before making changes.
2. **Preserve structure.** Follow the existing section numbering, heading hierarchy, and formatting conventions of the target document.
3. **Merge, don't duplicate.** If content already exists, enhance it. Don't create parallel sections.
4. **Be specific.** Use exact field names, button labels, dropdown options as they appear in the system UI.
5. **Write instructions, not narration.** Say "Click Approve to trigger auto-close" not "The PM then clicks Approve."
6. **Bump version + date** on every file you change: `**Version:** V2.X` and `**Last updated:** YYYY-MM-DD`.
7. **Update README.md** if any file description or filename changed.
8. **Update Master Index** if the high-level summary for a workflow area changed.

### When integrating new training videos

Follow the 9-step process in [`_video_analysis/RUNBOOK.md`](_video_analysis/RUNBOOK.md).

Key points:
- Only commit workflow docs and Python scripts to git — never video files, audio, transcripts, frames, or analysis reports
- The `.gitignore` is configured to exclude these; verify with `git status` before committing
- Video analysis reports (`_video_analysis/VIDEO_*.md`) are local working documents

### When adding a new workflow document

1. Follow the naming convention: `{NN}_{TYPE}_{TOPIC}_V2.md`
2. Add it to the file index in `README.md`
3. Add it to the Master Index (`00.1_MASTER_INDEX_WORKFLOW_V2.md`)
4. Cross-reference it from related playbooks/SOPs
5. Add monitoring items to the appropriate QA checklist if the new doc introduces daily/weekly checks

---

## Quality Gates (Pre-Commit)

Run these checks before every commit:

```powershell
# 1. No Tapi misspellings
rg -i "tarpy|tappy|tarpie" workflow/

# 2. No old playbook filename references
rg "TAPI_TARPY" workflow/ README.md

# 3. No wrong email addresses
rg "tarpy\.co\.nz" workflow/ README.md

# 4. Version dates are consistent across changed files
rg "Last updated" workflow/

# 5. Filenames in Master Index match actual files
rg "\.md" workflow/00.1_MASTER_INDEX_WORKFLOW_V2.md
Get-ChildItem workflow/*.md -Name

# 6. No generated artefacts staged
git status
```

---

## Key Domain Knowledge

### Systems hierarchy
- **Property Tree** is the system of record. Everything must eventually be reflected there.
- **Tapi** is the maintenance workflow engine. Jobs live here until invoice approval, then sync to Property Tree.
- **TPS** handles leasing lifecycle. Tenancy data syncs to Property Tree.
- **Inspection Express** handles inspection execution. Maintenance items sync to Tapi.

### Maintenance pipeline (Tapi)
7 status buckets: Open jobs → Awaiting quotes → Awaiting approval → Scheduling job → Awaiting repair → Awaiting invoice → Awaiting confirmation

5 action buttons per job: Send work order | Request quotes | Ask owner for approval | Send to owner for DIY | Plan for later

### Invoice flow
Tapi → approve → auto-close job + sync to Property Tree → rent holdback from owner's account → Monday payment run → landlord statement with invoice copy

### Payment cadence
- Tenants pay weekly (most common), fortnightly, or monthly
- Landlords are paid after tenant pays — payout frequency matches tenant's payment frequency
- Statements sent weekly on Mondays

### Contractor invoice submission
- Direct upload via Tapi portal (auto-matches best)
- Email to `propertypartner@tapi.co.nz` (may need manual matching)
- If sent to wrong address (accounts@, mckenzie@, etc.): forward to Tapi email with PDF attached (links don't work)

---

## What NOT to Do

- Never commit video files, audio files, extracted frames, or transcript files
- Never use "Tarpy", "Tappy", or "tarpy.co.nz" in any documentation
- Never create parallel/duplicate sections when content already exists
- Never change a Playbook without checking the dependent SOPs, Templates, and QA Checklists
- Never add a new daily/weekly check to the QA checklists without ensuring the pipeline buckets match the Playbook
- Never hardcode absolute file paths in Python scripts (use relative paths from script location)
