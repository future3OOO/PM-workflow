# CLAUDE.md — Project Intelligence for Property Management Workflow Docs

This file provides context, rules, and dependency maps so any AI agent working on this repository produces correct, consistent, and complete documentation updates.

---

## Project Overview

This is **Property Partner's** (Strathmore Property Limited) complete operational documentation library for NZ residential property management. It is the single source of truth for the PM and VA on how every workflow operates across all systems.

The documentation is **not code** — it is structured Markdown covering playbooks, SOPs, templates, and checklists. Changes must be treated with the same rigour as code: version-controlled, cross-referenced, and internally consistent.

---

## Repository Layout

```text
property_management_docs_v2/
├── README.md                    # Project overview and live site link
├── CLAUDE.md                    # This file — agent instructions
├── AGENTS.md                    # Mirror of CLAUDE.md for agent tooling
├── mkdocs.yml                   # MkDocs Material config + nav tree
├── requirements.txt             # Python deps for MkDocs site builds
├── .gitignore                   # Excludes site/ and video-analysis artefacts
├── .github/workflows/docs.yml   # Auto-deploy to GitHub Pages on push to main
├── docs/                        # All documentation (MkDocs source)
│   ├── index.md                 # Homepage with workflow cards
│   ├── stylesheets/extra.css    # Custom CSS
│   ├── getting-started/         # Systems overview, standards & SLAs
│   ├── onboarding/              # Landlord setup, PT, TPS, compliance
│   ├── leasing/                 # TPS lifecycle, viewings, apps, agreements
│   ├── maintenance/             # Tapi lifecycle, intake, invoices
│   ├── inspections/             # PT scheduling, Inspection Express
│   ├── renewals-exits/          # Rent reviews, Valua, end of tenancy
│   └── day-to-day/              # Email, notices, checklists, QA, templates, glossary
└── _video_analysis/             # Video integration tooling
    ├── RUNBOOK.md               # Transcript + frame-based video-to-docs process
    ├── batch_config.py          # Shared dated-batch video list + path helpers
    ├── requirements.txt         # Video-analysis-only Python deps
    ├── transcribe.py            # Single-video CLI transcription
    ├── transcribe_all_videos.py # Batch transcription pipeline
    ├── transcribe_batch2.py     # Dated-batch transcription pipeline
    ├── validate_batch.py        # Local evidence validation for a dated batch
    ├── extract_frames.py        # Frame extraction for visual review
    ├── artefacts/               # Dated outputs (gitignored)
    │   └── YYYY-MM-DD/
    │       ├── analysis/        # Per-video analysis reports
    │       └── frames/          # Extracted JPG review frames by video_id
    └── videos/                  # Source videos + transcript outputs (gitignored)
```

### Documentation Site

Docs are served via MkDocs Material. The site auto-deploys on every push to `main` via GitHub Actions.

- **File naming**: kebab-case `.md` in the appropriate `docs/` subdirectory
- **Cross-links**: Relative Markdown links, e.g. `[Title](../maintenance/tapi-intake.md)`
- **Nav**: Add new pages to `nav:` in `mkdocs.yml`
- **Authoring guide**: `docs/day-to-day/contributing.md`

---

## Video Analysis Method

Training videos are analysed using two evidence streams:

1. **Whisper transcripts**
   - capture spoken explanation, rationale, exceptions, and terminology
2. **Extracted frames**
   - capture exact UI labels, fields, button names, layout, and on-screen system behaviour

The synthesis of those two inputs becomes the dated analysis report stored under `_video_analysis/artefacts/YYYY-MM-DD/analysis/`.

Every batch also requires:

- a **per-video analysis report** for each video ID
- a **doc coverage matrix** that maps findings to reviewed docs and resulting actions
- an update to the published **video analysis glossary** in `docs/day-to-day/video-analysis-glossary.md`
- explicit **page / navigation mapping** for the screens involved in each analysed workflow
- an explicit **dependency-cascade check** so templates, checklists, triage pages, and standards pages are not skipped when an SOP changes

### Operating rule

Do **not** update workflow documentation from transcript-only notes when the video demonstrates a UI workflow. Use:

- transcripts for rationale and spoken context
- frames for exact interface facts
- the analysis report as the working synthesis artefact

Batch summaries are helpful, but they do **not** replace per-video analysis. The per-video report is the canonical evidence-preservation artefact.

Primary process reference: [`_video_analysis/RUNBOOK.md`](_video_analysis/RUNBOOK.md)

---

## Critical Naming Rules

| Term | Correct | Wrong |
|---|---|---|
| Maintenance CRM | **Tapi** | Tarpy, Tappy, Tarpie, TAPE |
| Invoice email | `propertypartner@tapi.co.nz` | PropertyPartner@tarpy.co.nz, any @tarpy domain |
| Playbook filename | `maintenance-lifecycle.md` | anything with TARPY in the name |

After any edit, run: `rg -i "tarpy\|tappy\|tarpie" docs/` to verify zero misspellings.

---

## Document Dependency Map

Changes to one document usually require updates to others. This map shows the dependencies.

### Tier 1 — Changes here cascade everywhere
- **`getting-started/systems-map.md`** — if a system's capabilities change, every doc that references that system needs checking
- **`getting-started/standards-slas.md`** — if policies/SLAs change, all workflow docs must align

### Tier 2 — Lifecycle pages drive step-level guides and templates
- **Lifecycle pages** (e.g. `maintenance/maintenance-lifecycle.md`, `leasing/leasing-lifecycle.md`) define the end-to-end workflow and decision logic
- When a lifecycle page changes, check:
  - the corresponding step-level guides (e.g. `maintenance/tapi-intake.md`, `maintenance/tapi-invoices.md`) for click-level accuracy
  - templates (`day-to-day/notice-email-templates.md`) for wording alignment
  - triage/operations checklists (`day-to-day/daily-triage.md`, `day-to-day/weekly-operations.md`) for coverage

### Tier 3 — Step-level guides drive templates and checklists
- When a step-level guide adds a new workflow step, check:
  - templates (`day-to-day/notice-email-templates.md`) for any new comms needed
  - triage/operations checklists (`day-to-day/daily-triage.md`, `day-to-day/weekly-operations.md`) for monitoring coverage

### Maintenance-specific dependency chain

```text
maintenance/maintenance-lifecycle.md (lifecycle)
  ├── maintenance/tapi-intake.md (intake → work orders)
  ├── maintenance/tapi-invoices.md (invoices → payment)
  ├── inspections/inspection-express.md (inspection source)
  ├── day-to-day/notice-email-templates.md (templates 7a–7k)
  ├── day-to-day/daily-triage.md (section 6: Tapi dashboard)
  ├── day-to-day/weekly-operations.md (Tapi items)
  ├── getting-started/systems-map.md (Tapi + invoice sections)
  └── getting-started/standards-slas.md (approval policy + contractor standards)
```

### Cross-document consistency checks

After any update, verify these are aligned:

| Check | Files involved |
|---|---|
| Priority levels (Emergency/Urgent/Routine/Planned) | `maintenance/maintenance-lifecycle.md`, `maintenance/tapi-intake.md`, `getting-started/standards-slas.md` |
| Tapi pipeline buckets (7 stages) | `maintenance/maintenance-lifecycle.md`, `maintenance/tapi-intake.md`, `day-to-day/daily-triage.md` |
| Invoice Approve effects (4 auto-effects) | `maintenance/maintenance-lifecycle.md`, `maintenance/tapi-invoices.md` |
| Triage cost thresholds | `maintenance/maintenance-lifecycle.md`, `maintenance/tapi-intake.md`, `getting-started/standards-slas.md` |
| Invoice email address | `maintenance/tapi-invoices.md`, `day-to-day/notice-email-templates.md`, `getting-started/systems-map.md`, `maintenance/maintenance-lifecycle.md` |
| File references / filenames | `README.md`, cross-links inside `docs/` |
| Version + Last updated date | every file that was changed |

---

## Update Protocol

### When updating existing documentation

1. **Read before editing.** Always read the full file before making changes.
2. **Preserve structure.** Follow the existing heading hierarchy and formatting conventions.
3. **Merge, don't duplicate.** If content already exists, enhance it. Don't create parallel sections.
4. **Be specific.** Use exact field names, button labels, and dropdown options as they appear in the UI.
5. **Write instructions, not narration.** Say "Click Approve to trigger auto-close" not "The PM then clicks Approve."
6. **Bump version + date** on every documentation file you change.
7. **Update README.md** if a file description, filename, or top-level repo guidance changed materially.

### When integrating new training videos

Follow the transcript + frame workflow in [`_video_analysis/RUNBOOK.md`](_video_analysis/RUNBOOK.md).

Key points:

- analyse software workflow videos using **both** transcript and extracted-frame evidence
- store working outputs under `_video_analysis/artefacts/YYYY-MM-DD/`
- keep MkDocs-only dependencies in root `requirements.txt`; keep Whisper/video-analysis dependencies in `_video_analysis/requirements.txt`
- run `_video_analysis/validate_batch.py` before doc integration to confirm transcript + frame evidence exists, then rerun it with `--require-coverage-matrix` before batch sign-off
- create a **per-video analysis report** for each video before relying on any grouped summary
- maintain a **doc coverage matrix** for the batch showing findings, target docs reviewed, actions taken, and residual gaps
- update the published **video analysis glossary** in `docs/day-to-day/video-analysis-glossary.md`
- use the coverage matrix to record both:
  - **primary docs reviewed**: the main lifecycle / SOP targets
  - **dependent docs checked**: templates, checklists, triage pages, standards pages, systems-map pages, or other downstream docs that may inherit the change
- capture **where the action happens**: system, page/screen name, visible URL if any, and navigation path
- update `docs/`, not any legacy `workflow/` paths
- only commit documentation pages and intentional script/instruction changes
- never commit source videos, audio, transcripts, frames, or analysis report drafts

### Batch completion rule

Do **not** mark a video batch complete until:

1. every video has its own analysis report
2. the coverage matrix exists for the batch
3. the published video glossary has been updated for the batch
4. each material finding is explicitly classified as:
   - documented via an update
   - already covered in the current docs
   - intentionally excluded from docs with a reason
5. each material finding has a recorded dependency-cascade result for:
   - templates
   - checklists / QA pages
   - triage / operations pages
   - standards / systems pages where relevant

### Dependency-cascade rule

When a video changes workflow understanding, the agent must not stop at the primary SOP page.

For each material finding, explicitly check whether it also affects:

- the published glossary in `docs/day-to-day/video-analysis-glossary.md`
- lifecycle pages
- step-level SOPs
- templates in `docs/day-to-day/notice-email-templates.md`
- daily / weekly operations pages
- execution / QA checklists
- standards / systems-map pages

The matrix must show that this pass happened even if the answer is **already aligned** or **not applicable**.

### Video-derived section marking rule

When a documentation section is materially updated from proper video analysis, mark it with the verified label:

```html
<span class="pp-verified-label">Verified from video analysis</span>
```

Use this only for sections that were genuinely checked against transcript + frame evidence. Do not add it to sections that were only lightly edited or inherited from older written material.

### When adding a new workflow document

1. Use kebab-case `.md` in the correct `docs/` subdirectory
2. Add it to `README.md` if the repo-level inventory changed
3. Add a `nav:` entry in `mkdocs.yml`
4. Cross-reference it from related lifecycle pages and step-level guides
5. Add monitoring items to `day-to-day/daily-triage.md` or `day-to-day/weekly-operations.md` if the new doc introduces daily/weekly checks

---

## Quality Gates (Pre-Commit)

Run these checks before every commit:

```powershell
# 1. No Tapi misspellings
rg -i "tarpy|tappy|tarpie" docs/

# 2. No wrong email addresses
rg "tarpy\.co\.nz" docs/ README.md

# 3. Version dates are visible across changed docs
rg "Last updated" docs/

# 4. Filenames in docs match expectation
Get-ChildItem docs/ -Recurse -Filter *.md -Name

# 5. No generated artefacts staged
git status
```

For video-driven doc updates, also verify:

- every video in the batch has a per-video analysis report
- the doc coverage matrix exists and reflects the changed files
- the published video glossary includes the newly processed videos
- no material finding was left without a disposition
- no material finding was left without a dependency-cascade disposition
- page / navigation mapping is captured for the relevant workflows
- any materially video-derived section that was updated is marked with the verified label
- templates, checklists, and triage pages were explicitly checked where the workflow changed

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
- tenants pay weekly (most common), fortnightly, or monthly
- landlords are paid after tenant pays — payout frequency matches tenant's payment frequency
- statements sent weekly on Mondays

### Contractor invoice submission
- direct upload via Tapi portal (auto-matches best)
- email to `propertypartner@tapi.co.nz` (may need manual matching)
- if sent to the wrong address: forward to the Tapi email with a PDF attached

---

## What NOT to Do

- Never commit video files, audio files, extracted frames, or transcript files
- Never use "Tarpy", "Tappy", or `tarpy.co.nz` in any documentation
- Never create parallel or duplicate sections when content already exists
- Never update software workflow docs from transcript-only notes when frame evidence is available
- Never treat a grouped batch summary as a substitute for per-video analysis
- Never close a batch without a doc coverage matrix
- Never close a batch without updating the published video glossary
- Never use the coverage matrix as a primary-SOP-only checklist; it must cover downstream dependent docs too
- Never omit page / navigation mapping when documenting a video-derived workflow
- Never apply the verified label to sections that were not actually checked against proper video analysis
- Never change a lifecycle page without checking the dependent step-level guides, templates, and triage/operations checklists
- Never add a new daily/weekly check without ensuring the underlying lifecycle and SOP pages support it
- Never hardcode absolute file paths in Python scripts when a repo-relative path will do
