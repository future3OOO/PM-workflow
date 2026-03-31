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
├── README.md                    # Project overview and live site link
├── CLAUDE.md                    # This file — agent instructions
├── mkdocs.yml                   # MkDocs Material config + nav tree
├── requirements.txt             # Python deps (mkdocs-material)
├── .gitignore                   # Excludes site/, video artefacts
├── .github/workflows/docs.yml  # Auto-deploy to GitHub Pages on push to main
├── docs/                        # All documentation (MkDocs source, 36 pages)
│   ├── index.md                 # Homepage with workflow cards
│   ├── stylesheets/extra.css    # Custom CSS
│   ├── getting-started/         # Systems overview, standards & SLAs
│   ├── onboarding/              # Landlord setup, PT, TPS, compliance (6 pages)
│   ├── leasing/                 # TPS lifecycle, viewings, apps, agreements (8 pages)
│   ├── maintenance/             # Tapi lifecycle, intake, invoices (3 pages)
│   ├── inspections/             # PT scheduling, Inspection Express (3 pages)
│   ├── renewals-exits/          # Rent reviews, Valua, end of tenancy (3 pages)
│   └── day-to-day/              # Email, notices, checklists, QA, templates (10 pages)
├── _video_analysis/             # Video integration tooling
│   ├── RUNBOOK.md               # 9-step video-to-workflow process
│   ├── transcribe.py            # Single-video CLI transcription
│   ├── transcribe_all_videos.py # Batch transcription pipeline
│   ├── artefacts/               # Generated outputs by date (gitignored)
│   └── videos/                  # Source video files (gitignored)
```

### Documentation Site

Docs are served via MkDocs Material. The site auto-deploys on every push to `main` via GitHub Actions.

- **File naming**: kebab-case `.md` in the appropriate `docs/` subdirectory
- **Cross-links**: Relative Markdown links, e.g. `[Title](../maintenance/tapi-intake.md)`
- **Nav**: Add new pages to `nav:` in `mkdocs.yml`
- **Authoring guide**: `docs/day-to-day/contributing.md`

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
  - The corresponding step-level guides (e.g. `maintenance/tapi-intake.md`, `maintenance/tapi-invoices.md`) for click-level accuracy
  - Templates (`day-to-day/notice-email-templates.md`) for email wording alignment
  - Triage/operations checklists (`day-to-day/daily-triage.md`, `day-to-day/weekly-operations.md`) for daily/weekly coverage

### Tier 3 — Step-level guides drive templates and checklists
- When a step-level guide adds a new workflow step, check:
  - Templates (`day-to-day/notice-email-templates.md`) for any new comms needed
  - Triage/operations checklists (`day-to-day/daily-triage.md`, `day-to-day/weekly-operations.md`) for monitoring coverage

### Maintenance-specific dependency chain

```
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
| Priority levels (Emergency/Urgent/Routine/Planned) | `maintenance/maintenance-lifecycle.md`, `maintenance/tapi-intake.md` (badge table), `getting-started/standards-slas.md` |
| Tapi pipeline buckets (7 stages) | `maintenance/maintenance-lifecycle.md`, `maintenance/tapi-intake.md`, `day-to-day/daily-triage.md` |
| Invoice Approve effects (4 auto-effects) | `maintenance/maintenance-lifecycle.md` (Stage 6), `maintenance/tapi-invoices.md` (Section 8) |
| Triage cost thresholds | `maintenance/maintenance-lifecycle.md`, `maintenance/tapi-intake.md`, `getting-started/standards-slas.md` |
| Invoice email address | `maintenance/tapi-invoices.md`, `day-to-day/notice-email-templates.md`, `getting-started/systems-map.md`, `maintenance/maintenance-lifecycle.md` |
| File references / filenames | README.md, `onboarding/compliance-healthy-homes.md` (cross-ref) |
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

### When integrating new training videos

Follow the 9-step process in [`_video_analysis/RUNBOOK.md`](_video_analysis/RUNBOOK.md).

Key points:
- Only commit workflow docs and Python scripts to git — never video files, audio, transcripts, frames, or analysis reports
- The `.gitignore` is configured to exclude these; verify with `git status` before committing
- Video analysis reports (`_video_analysis/VIDEO_*.md`) are local working documents

### When adding a new workflow document

1. Follow the naming convention: kebab-case `.md` in the correct `docs/` subdirectory
2. Add it to the file index in `README.md`
3. Add a `nav:` entry in `mkdocs.yml`
4. Cross-reference it from related lifecycle pages and step-level guides
5. Add monitoring items to `day-to-day/daily-triage.md` or `day-to-day/weekly-operations.md` if the new doc introduces daily/weekly checks

---

## Quality Gates (Pre-Commit)

Run these checks before every commit:

```powershell
# 1. No Tapi misspellings
rg -i "tarpy|tappy|tarpie" docs/

# 2. No old playbook filename references
rg "TAPI_TARPY" docs/ README.md

# 3. No wrong email addresses
rg "tarpy\.co\.nz" docs/ README.md

# 4. Version dates are consistent across changed files
rg "Last updated" docs/

# 5. Filenames in README match actual files
Get-ChildItem docs/ -Recurse -Filter *.md -Name

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
- Never change a lifecycle page without checking the dependent step-level guides, templates, and triage/operations checklists
- Never add a new daily/weekly check to `day-to-day/daily-triage.md` or `day-to-day/weekly-operations.md` without ensuring the pipeline buckets match the lifecycle page
- Never hardcode absolute file paths in Python scripts (use relative paths from script location)
