# Property Management Workflow Documentation

**Owner:** Property Partner (Strathmore Property Limited)  
**Version:** V2.3 (MkDocs Material portal)  
**Last Updated:** 2026-03-31  
**Audience:** Property Manager, Property Management Assistant / VA, Operations Support

**[View the live documentation site](https://future3OOO.github.io/PM-workflow/)**

---

## Documentation Site

This documentation is served as a searchable, navigable website via [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

- **Live site:** https://future3OOO.github.io/PM-workflow/
- **Auto-deploys** on every push to `main` via GitHub Actions
- **Search:** Full-text search across all documents
- **Edit workflow:** Edit any `.md` file in `docs/`, push to `main`, site updates in ~60 seconds

See `docs/contributing.md` for the full authoring guide.

---

## What This Is

This is the complete operational documentation library for Property Partner's end-to-end New Zealand residential property management workflow. It covers every stage of the property management lifecycle, from landlord onboarding through to end of tenancy, with detailed playbooks, step-by-step SOPs, copy-paste templates, and quality assurance checklists.

**Golden rule:** if it isn't recorded in Property Tree (or linked into the property record), it didn't happen.

---

## Systems Covered

| System | Role |
|---|---|
| **Property Tree** | System of record — property/owner/tenant master data, tenancy dates, rent ledger, inspection scheduling, document repository, trust accounting, Monday payment run |
| **TPS / Tenancy.co.nz** | Leasing — BookMe viewings, applications, checks, agreement generation, renewals, compliance fields, bond workflow |
| **Trade Me for Rent** | Marketing channel — listing publication, enquiry routing into TPS via listing ID |
| **Tapi** | Maintenance CRM — 4 intake sources (Concierge, Inspection Express, owner, phone/email), 7-stage status pipeline, triage, approvals, work orders, quote requests, DIY handoff, invoices (auto-match + manual match), sync to Property Tree |
| **Inspection Express** | Inspection execution — receives schedule from Property Tree, report publishing, maintenance item capture syncing to Tapi |
| **Valua** | Rent evidence — comparable market analysis and recommended rent range for rent reviews |
| **Shortwave AI** | Email drafting — used by PM for composing professional owner/tenant communications |

---

## Source files (`docs/`)

Operational Markdown for the live site lives under **`docs/`** (kebab-case filenames). Use the [site navigation](https://future3OOO.github.io/PM-workflow/) and search as the primary way to browse; the repo mirrors that structure.

| Area | Path |
|---|---|
| Foundation | [`docs/foundation/`](docs/foundation/) — master index, systems map, standards & SLAs |
| Playbooks | [`docs/playbooks/`](docs/playbooks/) — lifecycle processes (e.g. [`maintenance-tapi.md`](docs/playbooks/maintenance-tapi.md)) |
| SOPs | [`docs/sops/`](docs/sops/) — click-by-click system steps (e.g. [`tapi-intake.md`](docs/sops/tapi-intake.md), [`tapi-invoices.md`](docs/sops/tapi-invoices.md)) |
| Templates | [`docs/templates/`](docs/templates/) — notices, emails, checklists |
| QA | [`docs/qa/`](docs/qa/) — daily / weekly / monthly checklists |
| Reference | [`docs/reference/`](docs/reference/) — sources and external links |

**Entry points:** [`docs/index.md`](docs/index.md) (site home), [`docs/foundation/master-index.md`](docs/foundation/master-index.md) (full index and quick-start routes).

Config: [`mkdocs.yml`](mkdocs.yml) · Authoring: [`docs/contributing.md`](docs/contributing.md)

### Video analysis tooling (`_video_analysis/`)

| File | Description |
|---|---|
| [`RUNBOOK.md`](_video_analysis/RUNBOOK.md) | 9-step process for integrating new training videos into the `docs/` library (prerequisites, transcription, review, integration, verification, commit) |
| [`transcribe.py`](_video_analysis/transcribe.py) | Single-video CLI transcription helper: `py -3 _video_analysis/transcribe.py <video_id> <path>` |
| [`transcribe_all_videos.py`](_video_analysis/transcribe_all_videos.py) | Batch audio extraction (ffmpeg) and transcription (Whisper) pipeline for all registered videos |

---

## Change Control

When a process changes:

1. Update the **Playbook** first (the lifecycle process)
2. Update the **SOP** second (the system steps)
3. Update **Templates** third (the wording)
4. Update **QA Checklists** if the change affects daily/weekly checks
5. Update **Systems Map** and **Standards** if the change affects system behaviour or policies
6. Update **`docs/foundation/master-index.md`** and **`mkdocs.yml` nav** if filenames or high-level descriptions changed
7. Log changes at the top of the document (version + last updated)

### Naming conventions

- The system is called **Tapi** (not Tarpy, Tappy, or any variant)
- The invoice email is `propertypartner@tapi.co.nz`
- Source files in `docs/` use **kebab-case** `.md` names (e.g. `docs/sops/tapi-intake.md`); add new pages to `mkdocs.yml` `nav:`

### Version history

| Version | Date | Summary |
|---|---|---|
| V2.0 | 2026-02-24 | Initial full documentation library (35 workflow files) |
| V2.1 | 2026-03-07 | Integrated 2 Tapi inspection follow-up training videos |
| V2.2 | 2026-03-31 | Integrated 12 Tapi training videos covering dashboard, triage, invoices, approvals, quotes, DIY, Concierge. Added video analysis RUNBOOK and transcription tooling. Fixed all Tarpy→Tapi naming. Added invoice forwarding SOP and Property Tree rent holdback documentation |
| V2.3 | 2026-03-31 | Documentation moved from `workflow/` to `docs/` with kebab-case filenames; published as MkDocs Material site with search; auto-deploy to GitHub Pages on push to `main` |
