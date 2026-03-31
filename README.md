# Property Management Workflow Documentation

**Owner:** Property Partner (Strathmore Property Limited)
**Version:** V2.3
**Last Updated:** 2026-03-31
**Audience:** Property Manager, Property Management Assistant / VA, Operations Support

---

## Documentation Site

This documentation is served as a searchable, navigable website via [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

- **Auto-deploys** on every push to `main` via GitHub Actions
- **Search:** Full-text search across all documents (Ctrl+K)
- **Light/dark mode** toggle
- **Edit workflow:** Edit any `.md` file in `docs/`, push to `main`, site updates in ~60 seconds

---

## What This Is

The complete operational documentation library for NZ residential property management. Covers every stage of the property management lifecycle, organised by workflow area and the systems you use.

**Golden rule:** if it isn't recorded in Property Tree (or linked into the property record), it didn't happen.

---

## Site Structure

| Tab | What's in it | Primary systems |
|---|---|---|
| **Getting Started** | Systems overview, standards & SLAs | All systems |
| **Onboarding** | Landlord & property setup, compliance | Property Tree, TPS |
| **Leasing (TPS)** | Listing, viewings, applications, agreements, bonds, tenancy setup | TPS, Trade Me, Property Tree |
| **Maintenance (Tapi)** | Lifecycle, intake & triage, invoice processing | Tapi, Property Tree |
| **Inspections** | Scheduling, reports, actions | Property Tree, Inspection Express |
| **Renewals & Exits** | Rent reviews, renewals, end of tenancy | Valua, TPS |
| **Day-to-Day** | Email, notices, checklists, QA, templates | Shortwave AI, Property Tree |

---

## Source Files (`docs/`)

All documentation lives in the `docs/` directory, organised into subdirectories matching the site tabs:

```
docs/
├── index.md                     # Homepage
├── getting-started/             # Systems overview, standards
├── onboarding/                  # Landlord setup, PT, TPS, compliance
├── leasing/                     # TPS lifecycle, viewings, apps, agreements
├── maintenance/                 # Tapi lifecycle, intake, invoices
├── inspections/                 # PT scheduling, Inspection Express
├── renewals-exits/              # Rent reviews, Valua, end of tenancy
├── day-to-day/                  # Email, notices, checklists, QA, templates
└── stylesheets/                 # Custom CSS
```

See `docs/day-to-day/contributing.md` for the full authoring guide.

---

## Video Analysis Tooling (`_video_analysis/`)

| File | Purpose |
|---|---|
| [`RUNBOOK.md`](_video_analysis/RUNBOOK.md) | 9-step process for integrating new training videos into the documentation |
| [`transcribe.py`](_video_analysis/transcribe.py) | Single-video CLI transcription helper |
| [`transcribe_all_videos.py`](_video_analysis/transcribe_all_videos.py) | Batch audio extraction and transcription pipeline |

---

## Change Control

When a process changes, update in this order:

1. Lifecycle page (main workflow guide)
2. Step-by-step pages (system-specific instructions)
3. Templates (email/notice wording)
4. QA checklists (monitoring coverage)
5. Systems overview and standards (if system capabilities or policies changed)
6. `mkdocs.yml` nav (if new documents were added)
7. Bump version and date on every file touched

### Naming conventions

- The system is called **Tapi** (not Tarpy, Tappy, or any variant)
- The invoice email is `propertypartner@tapi.co.nz`
- File naming: kebab-case `.md` in the appropriate `docs/` subdirectory

### Version history

| Version | Date | Summary |
|---|---|---|
| V2.0 | 2026-02-24 | Initial full documentation library (35 workflow files) |
| V2.1 | 2026-03-07 | Integrated 2 Tapi inspection follow-up training videos |
| V2.2 | 2026-03-31 | Integrated 12 Tapi training videos. Added RUNBOOK and transcription tooling. Fixed Tarpy naming. Added invoice forwarding SOP and Property Tree rent holdback documentation |
| V2.3 | 2026-03-31 | MkDocs Material portal. Migrated from `workflow/` to `docs/` with system-based navigation. Reformatted all pages with admonitions, contextual navigation, and clean titles |
