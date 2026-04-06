# Property Management Workflow Documentation

**Owner:** Property Partner (Strathmore Property Limited)  
**Version:** V2.6  
**Last Updated:** 2026-04-01

---

## Live Documentation

- **Docs site:** https://future3OOO.github.io/PM-workflow/
- **Repository:** https://github.com/future3OOO/PM-workflow

This repository contains Property Partner's internal workflow documentation for NZ residential property management. The published documentation site is the primary reading experience; this repository is the source that drives it.

---

## What This Repository Contains

- `docs/`
  MkDocs source pages for onboarding, leasing, maintenance, inspections, renewals, and day-to-day operations
- `mkdocs.yml`
  Site configuration and navigation
- `_video_analysis/`
  Video-analysis tooling, runbook, local evidence workflow, and legacy-normalisation helper used to convert training videos into documentation updates
- `CLAUDE.md` and `AGENTS.md`
  Repository-specific agent guidance and dependency rules

Golden rule: if it is not recorded in Property Tree, or linked into the property record, it did not happen.

---

## Workflow Areas

The docs site is organised into:

- Getting Started
- Onboarding
- Leasing (TPS)
- Maintenance (Tapi)
- Inspections
- Renewals & Exits
- Day-to-Day

---

## Editing and Deployment

- Edit Markdown files in `docs/`
- Push to `main`
- GitHub Actions deploys the updated MkDocs site automatically

For local preview:

```powershell
py -3 -m mkdocs build --strict
py -3 -m mkdocs serve
```

---

## Video Analysis

Training videos are analysed with:

- Whisper transcripts for spoken workflow context
- extracted frames for exact UI evidence

Primary references:

- [_video_analysis/RUNBOOK_PERFORMANCE.md](_video_analysis/RUNBOOK_PERFORMANCE.md)
- [docs/day-to-day/contributing.md](docs/day-to-day/contributing.md)

---

## Change Control

When a process changes, update in this order:

1. lifecycle page
2. step-level SOP
3. templates
4. checklists / QA / triage pages
5. systems / standards pages if required

Use **Tapi** spelling consistently. Do not use `Tarpy`, `Tappy`, or similar variants.

<details>
<summary>Version History</summary>

| Version | Date | Summary |
|---|---|---|
| V2.0 | 2026-02-24 | Initial full documentation library |
| V2.1 | 2026-03-07 | Integrated Tapi inspection follow-up training videos |
| V2.2 | 2026-03-31 | Integrated Tapi video batch, runbook, and transcription tooling |
| V2.3 | 2026-03-31 | Migrated to MkDocs Material with `docs/` navigation |
| V2.4 | 2026-04-01 | Integrated April training videos and expanded workflow guidance |
| V2.5 | 2026-04-01 | Refreshed README and site theming, branding, and contrast tokens |

</details>
