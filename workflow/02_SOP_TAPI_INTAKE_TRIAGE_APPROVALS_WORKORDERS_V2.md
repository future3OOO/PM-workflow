# SOP — Tapi: Intake → Triage → Owner Approval → Quote vs Work Order (Version 2)

**Version:** V2.1 (Updated from video walkthrough)  
**Last updated:** 2026-03-07

---

## Overview

Maintenance jobs arrive in Tapi from two sources:
1. **Tenant requests** — submitted via the website form, landing directly in Tapi
2. **Inspection-captured items** — created by the PM in Inspection Express during a routine inspection, synced automatically into Tapi (tagged "Reported via inspection")

This SOP covers intake, triage, merging related jobs, obtaining owner approval, and issuing work orders or quote requests.

---

## Intake

### For tenant-submitted requests
1) Confirm job is attached to correct property and has photos/description
2) Acknowledge tenant and set next update time

### For inspection-captured items
1) Review Inspection Express daily for finalised inspections (see **02_SOP_INSPECTION_EXPRESS_REPORT_PUBLISH_ACTIONS_TO_TAPI_V2.md**)
2) Confirm each maintenance item from the inspection report has appeared in Tapi as an individual job
3) Each job will show: property address, description from PM's inspection notes, photos, and "Reported via inspection" tag
4) Review and clean up descriptions — remove any language directed at the landlord from the inspection report (e.g., "Are you happy for me to...") since this was part of the report narrative, not a work order instruction

---

## Triage

### Urgent (act immediately — issue work order without waiting for owner approval)
- Leak / flooding risk
- Hot water outage
- Power outage
- Sewerage
- Serious electrical hazard

### Priority chattels (often action quickly)
- Oven / cooktop
- Dishwasher
- Rangehood
- Heat pump

### Routine (standard approval flow)
- All other maintenance items — follow the approval process below

---

## Merging related jobs

When multiple jobs at the same property require the **same trade** (e.g., two plumbing issues found during an inspection), merge them into a single job before proceeding:

1) Open one of the related jobs in Tapi
2) Click **More options** (next to Edit job / Add note) → **Merge job**
3) Tapi shows a panel: "Select jobs to merge with" — only jobs at the same property that are "waiting to be actioned" will appear
4) Tick the related job(s) you want to merge
5) Tick **Edit description** to review the combined description
6) **Update the Title** to reflect the combined scope — e.g.:
   - Before: "Drip leak from shower mixer"
   - After: "Drip leak from shower mixer + potential leak under laundry floor"
7) Review and clean up the merged description:
   - Remove duplicate text
   - Remove questions directed at the landlord (these belong in the approval message, not the work order)
   - Keep context useful to the contractor (location, severity, what was observed)
8) Click **Merge** to confirm
9) **Refresh the page** — the Tapi UI may not update the job view immediately after merging
10) The Activity log will show the merge event for audit trail

> **When to merge:** Same property + same trade + both waiting to be actioned. Common examples:
> - Two plumbing issues → one plumber visit
> - Multiple electrical faults → one electrician visit
>
> **When NOT to merge:** Different trades, different urgency levels, or one job already has a contractor assigned.

---

## Approvals (routine inspection-captured items)

### Before requesting approval — check email first
Before sending an owner approval request in Tapi:
1) Check the PM's email inbox to see if the owner has **already responded** to the inspection report
2) The inspection report email includes all maintenance items — responsive owners may reply the same day approving work
3) If the owner has already approved → skip to **Work order** section below
4) If no response yet → proceed with the Tapi approval request

### Sending approval request in Tapi
1) Open the job and click **Ask owner for approval** in the Tapi Recommendation panel
2) The approval panel shows:
   - **Send an email notification** checkbox (keep ticked)
   - **Add personal message** text area
3) Write a clear approval message using this template:

> Hi [Owner first name],
>
> These items were noted during the routine inspection at [address]. Are you happy for me to arrange a contractor to attend to them?
>
> Kind regards,
> [PM / VA name]

4) Click **Send to owner**
5) The owner receives an email with:
   - Summary of the maintenance issue
   - Button to **view the full work order** details (photos, description)
   - Button to **Approve** the work directly
   - Ability to message back via Tapi's message thread

### What the owner experiences
- Owner receives email from Tapi with the maintenance request
- They can click through to see photos and full description
- They can click **Approve** to authorise the work
- They can also reply via the Tapi message thread
- Many owners respond by email to the PM instead of using the Tapi button — both are valid, check both channels

### Follow-up protocol for unanswered approvals
- **Day 0:** Approval request sent
- **Day 3 (business days):** If no response, send a follow-up message via the Tapi job thread
- **Day 7:** If still no response, escalate to PM for a phone call or direct email
- Monitor **Awaiting approval** bucket in Tapi daily — this shows all jobs waiting for owner response

> **Note on inspection-captured items:** Many inspection items are suggestions/improvements, not urgent. Landlords commonly ignore non-urgent items. The Tapi approval follow-up process ensures items don't get lost.

### Approvals for tenant-submitted requests (non-inspection)
- Send owner approval request in Tapi with: issue summary, risk, recommendation, cost estimate/quote-first, access plan
- Quote-first guideline: likely > $500 or uncertain scope (unless urgent)

---

## Work order / quote request

### Choosing the right action
| Tapi action | When to use |
|---|---|
| **Send work order** | Owner has approved (via Tapi, email, or message) — straightforward job, known scope |
| **Request quotes** | Cost likely > $500 OR scope uncertain — get quote before committing |
| **Send to owner for DIY** | Owner has stated they will handle it themselves |
| **Plan for later** | PM has flagged as non-urgent / future consideration |

### Sending a work order
1) Select contractor — search by name or trade (refer to **Contractor Key** for preferred suppliers per trade)
2) Fill in the **Send work order** panel:
   - **Compliance documents**: Usually not required (untick unless trade-specific)
   - **Require contractor to contact tenants**: Tick in most cases — contractor arranges access
   - **Cost limit**: Set if applicable (including GST)
   - **Message to supplier**: Brief, clear instruction — e.g., "Please replace 1x oyster light in the living room"
   - **Send reminder after**: Default 3 days
   - **Send copy to owner**: Ticked by default — owner is notified contractor is engaged
   - **Message to owner**: Usually blank if already in correspondence
   - **Send copy to tenant**: Tick this
   - **Message to tenant**: Brief heads-up — e.g., "Hi [tenant name], a contractor will be in contact with you to replace the light in the lounge"
   - **Health & safety hazards**: Add if relevant
3) Click **Send work order**
4) Job moves to **Scheduling** status in Tapi

> **Tenant notification detail:** The tenant receives an email notification with the **job title only** (e.g., "Lounge room light flickering"). They do NOT see the full description. Add a message to the tenant if the title alone does not provide enough context about what will happen.

### Work order best practices
- Include work order number — contractors must reference it on invoices
- Scope should be clear to the contractor without needing extra context
- If two merged jobs go to the same contractor, ensure the combined description is clear
- For preferred contractors by trade, refer to the Contractor Key (to be created separately)
