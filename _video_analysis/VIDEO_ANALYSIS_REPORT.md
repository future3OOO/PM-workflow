# Video Analysis Report — Tapi Inspection Follow-Up Approval Workflow

**Date:** 2026-03-07  
**Videos analysed:**
1. `1. Tapi - Inspection follow up approval.mkv` (14:55)
2. `2. Tapi - inspection follow up approval example.mkv` (6:21)

---

## Video 1 — Step-by-Step Transcript Summary

### Context
PM (McKenzie Lawrence) demonstrates to a VA/PM Assistant how to process maintenance items that originate from a routine inspection, flow into Tapi, and then need owner approval.

### Step-by-step workflow observed

| Timestamp | System | Action | Detail |
|---|---|---|---|
| 00:00–00:38 | Inspection Express | Open Inspections tab, filter to "This Week" | Shows list of 9 inspections with Status column (Archived, Finalised, In Progress) |
| 00:38–01:32 | Inspection Express | Explain daily monitoring task | VA should check daily for finalised inspections; flag any still "In Progress" |
| 01:53–02:21 | Inspection Express | View 360 inspection (test property) | Shows 360 walk-through — only used for ingoing reports, not routine |
| 02:22–02:55 | Inspection Express | Click "View PDF Report" on finalised inspection (2/467 Tuam St) | Opens PDF in-browser; scrolls to "Maintenance Items" section |
| 02:55–03:10 | Inspection Express + Tapi | Cross-reference maintenance items | 3 items visible in PDF; same 3 appear in Tapi Jobs list for the property |
| 03:11–04:11 | Tapi | Open first job: "Tile cracking / floor movement" (Laundry) | Photos, description from inspection. Tagged "Reported via inspection". Action panel shows: Send work order, Request quotes, Ask owner for approval, Send to owner for DIY, Plan for later |
| 04:12–04:31 | Tapi | Open second job: "Drip leak from shower mixer" (Main Bathroom) | Notes it's a plumber job. Description includes question to landlord ("You happy for me to get this serviced...") |
| 04:33–05:10 | Tapi | Decide to merge two plumbing jobs | Both are plumber jobs at same property — should be merged into one |
| 05:01–05:29 | Tapi | More options → Merge job | Panel shows other open jobs at same property. Selects "Tile cracking / floor movement". Skips unrelated heat pump job |
| 05:30–06:06 | Tapi | Edit description during merge | Reviews combined description. Notes that landlord-directed questions should be removed before sending to contractor |
| 06:06–07:16 | Tapi | Clean up merged description | Removes "Are you happy for me to..." text. Keeps contractor-relevant detail. Context about floor history retained for plumber |
| 07:21–07:52 | Tapi | Complete merge | Refreshes page (UI doesn't auto-update). Merged job now shows both descriptions in Activity log |
| 07:54–08:38 | Tapi | Edit merged job title | Updates to: "Drip leak from shower mixer + potential leak under laundry floor" |
| 08:43–09:18 | Tapi | Navigate other inspection jobs | Reviews remaining items. Emphasises every maintenance item must be processed |
| 09:18–10:08 | Tapi | Explain approval workflow | Every inspection maintenance item should be sent to owner for approval. Tapi sends email with approve button + reminder. Should be done immediately after inspection is finalised |
| 10:08–10:42 | Tapi | Click "Ask owner for approval" | Types message: "Are you happy for me to arrange a plumber to service this shower mixer and check under laundry for leak" |
| 10:42–11:25 | Tapi | Discuss approval message template | Will create structured template: "Hi [owner], these items were noted during your routine inspection. Are you happy for me to arrange a contractor?" |
| 11:25–12:24 | Tapi | Send approval to owner | Owner receives email with: maintenance details, approve button, message thread access |
| 12:24–13:07 | Tapi | Explain follow-up protocol | Can send direct follow-ups in Tapi. Check daily for responses. Chase if no reply after a few days |
| 13:07–14:01 | Tapi | Show responsive landlord example (46 Quinns Rd) | This owner replied same day — no need for Tapi approval request |
| 14:01–14:53 | Tapi + Email | Explain skip-approval scenario | Check PM's email first. If owner already responded to inspection report → skip Tapi approval → send work order directly |

---

## Video 2 — Step-by-Step Transcript Summary

### Context
PM shows a real example of an owner (David Hunt) who responded immediately to an inspection report, approving a light replacement. Demonstrates sending a work order directly to a contractor.

### Step-by-step workflow observed

| Timestamp | System | Action | Detail |
|---|---|---|---|
| 00:00–00:33 | Email (Outlook/Gmail) | Show owner's email response | FWD: Routine Inspection Report | 515B Pages Road. Owner David Hunt replied: "OK to fix the LED you mention" + approved window replacement |
| 00:36–01:07 | Email + Tapi | Cross-reference | Email shows the inspection report email sent to owner. Tapi shows the corresponding job: "[Lounge room - Overall] Light flickering" |
| 01:07–01:33 | Tapi | Open job: Light flickering | Description: "Oyster led not working. Hard wired led light. Would need replacing." Tagged "Reported via inspection" |
| 01:34–02:19 | — | Explain trade knowledge | Replacement vs repair decision for LED lights. Minimum labour charge makes repair uneconomical. This context informs the work order |
| 02:20–02:53 | Tapi | Skip approval → send work order directly | Owner already approved via email. Click "Send work order" |
| 02:53–03:28 | Tapi | Select contractor | Searches for "Carl" — preferred electrician. Also does handyman work. Selected for being well-priced |
| 03:28–03:59 | Tapi | Work order panel: message to supplier | Typed: "please replace 1x oyster light in the living room" |
| 03:59–04:15 | Tapi | Work order panel: compliance/insurance | Not required for this job. "Require contractor to contact tenants" ticked |
| 04:16–04:44 | Tapi | Work order panel: owner notification | Copy sent to owner (default). No additional message needed — already in correspondence |
| 04:44–05:12 | Tapi | Work order panel: tenant notification | Copy sent to tenant. Message: "Hi John, a contractor will be in contact with you to replace the oyster light in the lounge" |
| 05:13–05:51 | — | Explain tenant notification detail | Tenant only sees job title in email ("Lounge room light flickering"), not full description. Adding a message gives them useful context |
| 05:52–06:00 | Tapi | Health & safety | No hazards for this property |
| 06:00–06:16 | Tapi | Send work order | Job moves to "Scheduling" status. Tapi shows "Work order sent successfully" |
| 06:16–06:21 | Tapi | Jobs list updated | New status counts updated. Job now in "Scheduling job" bucket |

---

## Gap Analysis

| # | What Videos Show | Relevant Doc | Gap Type | Detail |
|---|---|---|---|---|
| 1 | VA must monitor Inspection Express daily for finalised inspections | 02_SOP_INSPECTION_EXPRESS | **MISSING** | SOP had only 5 bullet points, no daily monitoring workflow |
| 2 | Cross-reference PDF maintenance items against Tapi jobs | 02_SOP_INSPECTION_EXPRESS | **MISSING** | No mention of cross-reference step |
| 3 | Clean up job descriptions (remove landlord-directed language) | 02_SOP_TAPI_INTAKE | **MISSING** | Not documented |
| 4 | Merge related jobs (More options → Merge job) | 02_SOP_TAPI_INTAKE | **MISSING** | Merge workflow not documented at all |
| 5 | Edit merged job title to reflect combined scope | 02_SOP_TAPI_INTAKE | **MISSING** | Not documented |
| 6 | Check PM email before requesting Tapi approval | 02_SOP_TAPI_INTAKE | **MISSING** | Skip-approval scenario not documented |
| 7 | Structured approval message template | 03_TEMPLATES_NOTICES | **INCOMPLETE** | Template 7 exists for email but no Tapi-specific approval template |
| 8 | Owner receives email with approve button + message thread | 02_SOP_TAPI_INTAKE | **MISSING** | Owner experience not described |
| 9 | Follow-up protocol (3 days → chase in Tapi) | 02_SOP_TAPI_INTAKE | **MISSING** | No follow-up timeline documented |
| 10 | Send work order with message to supplier, owner copy, tenant message | 02_SOP_TAPI_INTAKE | **INCOMPLETE** | WO instructions existed but lacked the detail shown in video |
| 11 | Tenant only sees job title, not full description | 02_SOP_TAPI_INTAKE | **MISSING** | Important UX detail not documented |
| 12 | Tapi Jobs dashboard status buckets | 02_SOP_INSPECTION_EXPRESS | **MISSING** | No reference to Tapi dashboard layout |
| 13 | "Reported via inspection" tag on Tapi jobs | 00.2_SYSTEMS_MAP | **INCOMPLETE** | Systems map mentioned sync but not the tag |
| 14 | Inspection report email includes link + access code (30 days) | 01_PLAYBOOK_INSPECTIONS | **MISSING** | Report distribution detail not documented |
| 15 | Contractor Key / preferred supplier list needed | 02_SOP_TAPI_INTAKE | **MISSING** | Referenced in video, does not exist yet |

---

## Files Updated

1. `workflow/02_SOP_INSPECTION_EXPRESS_REPORT_PUBLISH_ACTIONS_TO_TAPI_V2.md` — **Major rewrite** (5 bullets → 8 detailed steps)
2. `workflow/02_SOP_TAPI_INTAKE_TRIAGE_APPROVALS_WORKORDERS_V2.md` — **Major rewrite** (added merge workflow, approval templates, follow-up protocol, work order detail)
3. `workflow/01_PLAYBOOK_INSPECTIONS_PROPERTYTREE_TO_INSPECTIONEXPRESS_V2.md` — **Expanded Stage 4** (added VA daily task sub-steps 4a–4f)
4. `workflow/01_PLAYBOOK_MAINTENANCE_TAPI_TARPY_V2.md` — **Expanded Stage 1 and 3** (added inspection-captured item sub-workflow, skip-approval scenario, merge instructions)
5. `workflow/03_TEMPLATES_CHECKLISTS_V2.md` — **Expanded checklists 4 and 5** (added post-inspection Tapi follow-up checklist, expanded maintenance checklist)
6. `workflow/03_TEMPLATES_NOTICES_EMAILS_V2.md` — **Added templates 7b, 7c, 7d** (Tapi approval message, contractor work order message, tenant notification message)
7. `workflow/04_QA_DAILY_TRIAGE_CHECKLIST_V2.md` — **Added section 2** (Inspection Express → Tapi daily follow-up checklist)
8. `workflow/00.2_SYSTEMS_MAP_DATA_FLOW_V2.md` — **Expanded inspections data flow** (4 steps → 7 steps with VA workflow)

---

## Automation Opportunities Identified

| Manual Step | Automated Version | Systems Involved |
|---|---|---|
| VA checks Inspection Express daily for finalised reports | Auto-detect finalised inspections and trigger alert | Inspection Express API → Workflow platform |
| VA cross-references PDF maintenance items against Tapi | Auto-verify sync completeness; flag missing items | Inspection Express → Tapi API |
| VA checks PM email for owner responses before requesting Tapi approval | Auto-detect owner replies to inspection report emails and link to Tapi jobs | Email API → Tapi API |
| VA manually types approval message in Tapi | Pre-populated approval template with property/owner details auto-filled | Workflow platform → Tapi API |
| VA manually merges related jobs | Auto-suggest merges (same property + same trade + both pending) | Tapi API analysis |
| VA sends follow-up after 3 days | Auto-follow-up scheduler for unanswered approvals | Tapi API + scheduling engine |
| Owner approval by email vs Tapi button creates inconsistency | Unified approval tracking regardless of channel | Email API + Tapi API → central status |
