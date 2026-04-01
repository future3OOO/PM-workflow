# Contributing Guide

*How to add new documents, update existing ones, and keep the site consistent.*

**Version:** V2.4  
**Last updated:** 2026-04-01

---

## How the Site Works

The documentation site is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and auto-deploys to GitHub Pages whenever changes are pushed to `main`. Build takes about 60 seconds.

```
Edit .md file in docs/ → push to main → GitHub Actions builds → site updates
```

---

## Updating an Existing Document

1. Open the file in its `docs/` subdirectory
2. Edit the Markdown as normal
3. Update the version and date line at the top of the page
4. Push to `main` — the site rebuilds automatically

If the section was materially updated from proper video analysis, add the verified label under the relevant heading:

```html
<span class="pp-verified-label">Verified from video analysis</span>
```

---

## Adding a New Document

### 1. Create the file

Place it in the correct subdirectory based on which workflow tab it belongs in:

| Workflow area | Directory |
|---|---|
| Onboarding (Property Tree, TPS, compliance) | `docs/onboarding/` |
| Leasing (TPS, Trade Me, bonds) | `docs/leasing/` |
| Maintenance (Tapi) | `docs/maintenance/` |
| Inspections (Property Tree, Inspection Express) | `docs/inspections/` |
| Renewals & end of tenancy | `docs/renewals-exits/` |
| Day-to-day (email, notices, checklists, QA) | `docs/day-to-day/` |
| Getting started (systems, standards) | `docs/getting-started/` |

Use **kebab-case** filenames (lowercase, hyphens, no spaces or underscores).

### 2. Add the standard header

```markdown
# Clear Descriptive Title

**Version:** V2.x  
**Last updated:** YYYY-MM-DD
```

No "PLAYBOOK --", "SOP --", or other prefixes. The navigation tells users where they are.

### 3. Add a nav entry in mkdocs.yml

Open `mkdocs.yml` at the repo root and add one line under the correct tab:

```yaml
nav:
  - Maintenance (Tapi):
    - New Page Title: maintenance/new-file.md   # add here
```

### 4. Add cross-links

Link to related documents using relative Markdown links:

```markdown
[Systems Overview](../getting-started/systems-map.md)
[Tapi Intake](../maintenance/tapi-intake.md)
```

### 5. Add a "What's Next" block at the bottom

```markdown
!!! info "What's Next"
    - [Related Page](../section/file.md) — brief description
```

### 6. Push to main

```bash
git add docs/maintenance/new-file.md mkdocs.yml
git commit -m "docs: add new page for X"
git push
```

---

## Previewing Locally

```bash
pip install -r requirements.txt
mkdocs serve
```

Open `http://127.0.0.1:8000`. Changes hot-reload.

---

## Change Control Order

When a process changes, update documents in this order:

1. Lifecycle page (the main workflow guide)
2. Step-by-step pages (system-specific instructions)
3. Templates (email/notice wording)
4. QA checklists (monitoring coverage)
5. Systems overview and standards (if system capabilities or policies changed)

Bump the version and date on every file you touch.

---

## Video-Derived Section Conventions

When documentation is updated from transcript + frame-based video analysis:

### 1. Show users where the action happens

Include concise location cues so users can find the correct screen quickly. Good patterns:

- `Navigate to: Properties → [property] → Agreements`
- `Location: Book a viewing → Enquiries`
- `URL observed: tpportal.co.nz/clients/bookme/overview`

Use exact menu, tab, and button wording taken from the analysed UI where possible.

### 2. Mark materially verified sections

Use this subtle label for sections that were materially updated from proper video analysis:

```html
<span class="pp-verified-label">Verified from video analysis</span>
```

Use it when:

- the section was updated from transcript + frame evidence
- the workflow or UI wording was checked against analysed video material

Do not use it when:

- the edit was only wording cleanup
- the section was copied forward from older written docs without fresh evidence review
- the source video evidence was incomplete or uncertain
