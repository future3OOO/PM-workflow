# Contributing to This Documentation

This guide explains how to add new documents, update existing ones, and keep the documentation site consistent.

---

## How the Site Works

The documentation site is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and automatically deploys to GitHub Pages whenever changes are pushed to the `main` branch. The build takes about 60 seconds.

```
Edit .md file in docs/ → git push to main → GitHub Actions builds → Site auto-updates
```

---

## Updating an Existing Document

1. Open the file in its `docs/` subdirectory
2. Edit the Markdown as normal — headings, tables, bold, lists, checkboxes all work
3. Update the **Version** and **Last updated** header at the top of the file
4. Commit and push to `main`

The site rebuilds automatically. No manual build step needed.

---

## Adding a New Document

### 1. Create the file

Place it in the correct subdirectory:

| Document type | Directory | Example filename |
|---|---|---|
| Foundation / overview | `docs/foundation/` | `new-overview.md` |
| Playbook | `docs/playbooks/` | `arrears-management.md` |
| SOP | `docs/sops/` | `propertytree-new-feature.md` |
| Template | `docs/templates/` | `arrears-notices.md` |
| QA checklist | `docs/qa/` | `quarterly-review.md` |

Use **kebab-case** filenames (lowercase, hyphens, no spaces or underscores).

### 2. Add the standard header

Every document starts with:

```markdown
# TITLE — Description (Version 2)

**Version:** V2.x
**Last updated:** YYYY-MM-DD
```

### 3. Add a nav entry

Open `mkdocs.yml` at the repo root and add one line under the appropriate section:

```yaml
nav:
  - Playbooks:
    - New Playbook Title: playbooks/new-file.md   # ← add here
```

### 4. Add cross-links

Link to related documents using relative Markdown links:

```markdown
See: [Systems Map](../foundation/systems-map.md)
SOP: [Tapi Intake](../sops/tapi-intake.md)
```

Path patterns from any subdirectory:

| Linking to | From same dir | From another dir |
|---|---|---|
| Same category | `filename.md` | N/A |
| Playbooks | `filename.md` | `../playbooks/filename.md` |
| SOPs | `../sops/filename.md` | `../sops/filename.md` |
| Foundation | `../foundation/filename.md` | `../foundation/filename.md` |
| Templates | `../templates/filename.md` | `../templates/filename.md` |
| QA | `../qa/filename.md` | `../qa/filename.md` |

### 5. Push to main

```bash
git add docs/playbooks/new-file.md mkdocs.yml
git commit -m "docs: add new playbook for X"
git push
```

The site rebuilds automatically.

---

## Previewing Locally

```bash
pip install -r requirements.txt
mkdocs serve
```

Open `http://127.0.0.1:8000` to preview. Changes are hot-reloaded.

---

## MkDocs Features You Can Use

| Feature | Syntax |
|---|---|
| Admonition (tip) | `!!! tip "Title"` followed by indented content |
| Admonition (warning) | `!!! warning "Title"` followed by indented content |
| Collapsible section | `??? note "Title"` followed by indented content |
| Task list | `- [x] Done` / `- [ ] Not done` |
| Keyboard keys | `++ctrl+k++` renders as a key combo |
| Tabbed content | `=== "Tab 1"` followed by indented content |

---

## Change Control Order

When a process changes, update documents in this order:

1. **Playbook** (lifecycle logic)
2. **SOP** (system steps)
3. **Templates** (email/notice wording)
4. **QA Checklists** (monitoring coverage)
5. **Systems Map + Standards** (if system capabilities or policies changed)
6. **Master Index** (if new documents were added)

Bump the version and last-updated date on every file you touch.
