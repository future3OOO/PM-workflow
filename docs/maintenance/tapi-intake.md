# Intake, Triage & Work Orders

**Version:** V2.2  
**Last updated:** 2026-03-31

---

## Overview

Maintenance jobs arrive in Tapi from four sources:
1. **Tenant requests** — submitted via the Tapi concierge chatbot, landing in Tapi and triggering a Gmail notification
2. **Inspection-captured items** — created by the PM in Inspection Express during a routine inspection, synced automatically into Tapi (tagged "Reported via inspection")
3. **Owner-initiated requests** — PM or VA creates a job manually in Tapi on behalf of the owner
4. **Supplier-reported items** — contractor discovers additional scope during a visit

This SOP covers intake, triage, merging related jobs, obtaining owner approval, issuing work orders or quote requests, DIY handoff, mid-job updates, and job closure.

---

## Tapi Dashboard Reference

### Left sidebar navigation
Inbox | New job | New Invoice | Jobs (main) | Invoices | Properties | Suppliers | Services | Owners | Compliance

### Jobs view — tabs and pipeline
- **Tabs across top:** Open | Paused | Closed | All | Planned
- **Status pipeline (column buckets):** Open jobs → Awaiting quotes → Awaiting approval → Scheduling job → Awaiting repair → Awaiting invoice → Awaiting confirmation
- **Job list columns:** Job (title + status tag) | Last action | Priority (colour badges) | Supplier | Job agent | Property agent | Created

### Filtering and reporting
- **Filter bar:** Job agent | Property agent | Priority | Source (Inspection / Tenant / Owner / Supplier / Compliance) | Created (date range)
- **Save view** button — saves the current filter combination for reuse
- **Export report** button — exports filtered job list
- Footer shows "X of Y items" with pagination controls

### Priority colour badges
| Badge colour | Level | Target response |
|---|---|---|
| Red | Emergency | Within 24 hours — life/safety (flooding, gas leak, serious electrical) |
| Red | Urgent | Act promptly — hot water outage, power outage, sewerage, significant leak |
| Amber | Routine | Standard flow (90%+ of jobs) |
| Grey/Blue | Planned | Scheduled for future |

---

## Intake

### A. Tenant concierge requests

1. Email notification arrives in Gmail from Tapi with labels: **Concierge** (green), **Maintenance** (blue), **Properties/[address]** (grey)
2. Email contains: Tapi logo, "New maintenance request" heading, property address, **View full request** button
3. Replying to the email sends a message directly to the tenant — do not use reply for internal notes
4. Click **View full request** → opens the job in Tapi
5. Click **Accept** → a modal asks you to confirm the property and tenancy match. Verify and confirm
6. Clean up the job description: the "Additional Info" section often contains garbled chatbot conversation data — remove this noise and rewrite a clear description for the contractor
7. The job now shows the standard action panel with five action buttons

### B. Inspection-captured items

1. Review Inspection Express daily for finalised inspections (see [Inspection Express Reports](../inspections/inspection-express.md))
2. Confirm each maintenance item from the inspection report has appeared in Tapi as an individual job
3. Each job will show: property address, description from PM's inspection notes, photos, and "Reported via inspection" tag
4. Review and clean up descriptions — remove any language directed at the landlord from the inspection report (e.g., "Are you happy for me to...") since this was part of the report narrative, not a work order instruction

### C. Owner-initiated jobs

1. Click **New job** in the Tapi left sidebar
2. Fill in the New Job form:
   - **Source:** Owner (dropdown options: Inspection, Tenant, Owner, Supplier, Compliance)
   - **Property:** search and select from property list
   - **Tenancy:** auto-fills when property is selected
   - **Title:** descriptive, include "Owner —" prefix when owner-requested (e.g., "Owner — Spouting clean")
   - **Description:** contractor-directed instructions — write as if briefing the tradesperson
3. Click **Create**
4. Add photos via drag-and-drop from File Explorer or the upload button. Include satellite imagery from Property Guru / Google Maps when useful for context (e.g., roof access, property layout)

### D. Supplier-reported items

When a contractor discovers additional scope during a visit, the PM or VA creates a new job in Tapi with Source set to "Supplier" and links it to the original job if relevant.

---

## Triage

### Decision framework

| Condition | Action | Reasoning |
|---|---|---|
| Active leak, flooding, no hot water, power out, sewerage, electrical hazard | Send work order immediately (bypass owner approval). Use "call contractor first" if same-day attendance needed | Life/health/property damage risk — cannot wait |
| Oven, cooktop, dishwasher, rangehood, heat pump not working | Fast-track — send for approval immediately OR send work order if owner relationship allows | Essential chattels — tenants cannot function without them |
| Simple/cheap fix (<$200–300, obvious scope, e.g., broken curtain bracket) | Send work order directly — not worth owner approval | Cost of approval process exceeds cost of the repair |
| Moderate routine item ($300–500 range, clear scope) | Ask owner for approval, then send work order | Reasonable spend requiring sign-off |
| Expensive or uncertain scope (>$500 or diagnostic needed) | Request quotes first, then send quote to owner for approval | Owner needs pricing before committing |
| Safety/compliance issue (fire doors, smoke alarms) | Inform owner + send work order — cannot wait for approval on safety | Legal/compliance obligation |
| Owner states they'll handle it themselves | Send to owner for DIY | Owner has opted to self-manage |
| Non-urgent, recommended from inspection | Plan for later | No immediate action needed |

??? note "Full list of Tapi trade categories"
    Building works · Carpentry · Cleaning · Drapery · Electrical · Exterior · Fencing · Fire protection · General · Grounds · HVAC · Insulation · Joinery · Locksmith · Painting · Pest control · Plumbing · Property management · Rangehood · Roofing · Security · Ventilation · Waterproofing

---

## Merging related jobs

When multiple jobs at the same property require the **same trade** (e.g., two plumbing issues found during an inspection), merge them into a single job before proceeding:

1. Open one of the related jobs in Tapi
2. Click **More options** (next to Edit job / Add note) → **Merge job**
3. Tapi shows a panel: "Select jobs to merge with" — only jobs at the same property that are "waiting to be actioned" will appear
4. Tick the related job(s) you want to merge
5. Tick **Edit description** to review the combined description
6. **Update the Title** to reflect the combined scope — e.g.:
   - Before: "Drip leak from shower mixer"
   - After: "Drip leak from shower mixer + potential leak under laundry floor"
7. Review and clean up the merged description:
   - Remove duplicate text
   - Remove questions directed at the landlord (these belong in the approval message, not the work order)
   - Keep context useful to the contractor (location, severity, what was observed)
8. Click **Merge** to confirm
9. **Refresh the page** — the Tapi UI may not update the job view immediately after merging
10. The Activity log will show the merge event for audit trail

> **When to merge:** Same property + same trade + both waiting to be actioned. Common examples:
> - Two plumbing issues → one plumber visit
> - Multiple electrical faults → one electrician visit
>
> **When NOT to merge:** Different trades, different urgency levels, or one job already has a contractor assigned.

---

## Approvals

### Step 1 — Check email first

Before sending an owner approval request in Tapi:
1. Check the PM's email inbox to see if the owner has **already responded** to the inspection report
2. The inspection report email includes all maintenance items — responsive owners may reply the same day approving work
3. If the owner has already approved → skip to **Work order** section below
4. If no response yet → proceed with the Tapi approval request

### Step 2 — Send approval request in Tapi

1. Open the job and click **Ask owner for approval** in the action panel
2. The approval panel shows:
   - **Send an email notification** checkbox (keep ticked)
   - **Add personal message** text area
3. Write a clear approval message using this template:

> Hi [Owner first name],
>
> These items were noted during the routine inspection at [address]. Are you happy for me to arrange a contractor to attend to them?
>
> Kind regards,
> [PM / VA name]

4. Click **Send to owner**
5. Status changes to **Awaiting approval** (amber banner on the job)
6. Activity log records: "requested approval for the job" with email sending confirmation (✓)

### What the owner experiences

- Owner receives email from Tapi with the maintenance request
- Email contains: approve button, view full work order details link, message thread access
- They can click through to see photos and full description
- They can click **Approve** to authorise the work directly
- They can reply via the Tapi message thread

### Two owner response paths

| Path | What happens | VA action |
|---|---|---|
| **Path A:** Owner clicks **Approve** button in email | Status auto-updates to "Job Approved" | Proceed to work order — no manual step needed |
| **Path B:** Owner replies via Tapi message thread (or emails PM directly) | Status remains "Awaiting approval" | VA must manually approve: click the three-dot menu (⋮) next to the owner's name → **Approve** |

**Three-dot menu (⋮) options:** Approve | Decline | Resend email

### Follow-up protocol for unanswered approvals

| Day | Action |
|---|---|
| Day 0 | Approval request sent |
| Day 3 | Send follow-up message via the Tapi job thread |
| Day 7 | Escalate to PM for a phone call or direct email |
| Daily | Monitor the **Awaiting approval** bucket in Tapi |

> **Note on inspection-captured items:** Many inspection items are suggestions/improvements, not urgent. Landlords commonly ignore non-urgent items. The follow-up protocol ensures items don't get lost, but don't escalate beyond Day 7 for low-priority suggestions.

---

## Work order / quote request / DIY — choosing the right action

| Tapi action | When to use |
|---|---|
| **Send work order** | Owner has approved (via Tapi, email, or message) — straightforward job, known scope |
| **Request quotes** | Cost likely >$500 OR scope uncertain — get quote before committing |
| **Send to owner for DIY** | Owner has stated they will handle it themselves |
| **Plan for later** | PM has flagged as non-urgent / future consideration |
| **Call contractor first** | Urgent/emergency — same-day attendance needed (see section below) |

---

## "Call Contractor First" Workflow (urgent/emergency)

For urgent jobs requiring same-day attendance:

1. **Phone** the preferred contractor for the trade to confirm availability today
2. Once the contractor confirms, open the job in Tapi → click **Send work order**
3. In the **Message to supplier** field: "As discussed, [instructions]. [Include tenant phone number if not already updated in Tapi]"
4. Before sending, notify the tenant via the tenant message: "Just letting you know [trade] will be in contact. They will contact you soon."
5. Click **Send work order** — this creates the formal record after the verbal arrangement

> The phone call secures same-day attendance. The work order in Tapi creates the paper trail. Both steps are required.

---

## Sending a Work Order — Complete Panel Fields

1. **Select supplier:** search by name or trade (refer to Contractor Key for preferred suppliers per trade)
2. **Compliance documents:** panel shows Indemnity / Licence / Insurance status per supplier
   - Checkbox: **"Do not require compliance documents for this work order"**
   - Tick for handyman / known general contractors
   - Leave unticked (require documents) for electrical, plumbing, gas, and any licensed trade work
3. **Require contractor to contact tenants:** tick in almost all cases
   - Exception: exterior-only work or vacant property
4. **Cost limit:** dollar amount with **"Incl. GST"** toggle
5. **Message to supplier:** brief, clear instruction — e.g., "Please replace 1x oyster light in the living room"
6. **Send reminder after:** default 3 days (Tapi auto-sends reminders at 12h–24h intervals until the contractor accepts)
7. **Send copy to owner:** ticked by default — owner is notified contractor is engaged
8. **Message to owner:** usually blank if already in correspondence
9. **Send copy to tenant:** tick this
10. **Message to tenant:** brief heads-up — e.g., "Hi [tenant name], a contractor will be in contact with you to replace the light in the lounge"
11. **Health & safety hazards:** select all applicable:
    - Trip | Slip | Electrical | Dogs | Steep access | Asbestos (potential) | Asbestos (confirmed) | Working at height | and others
    - **Dogs** is the #1 most common hazard — can be set as a property-level default so it pre-fills on every work order for that property
12. Click **Send work order**
13. Job moves to **Scheduling** status in Tapi

> **Tenant notification detail:** The tenant receives an email notification with the **job title only** (e.g., "Lounge room light flickering"). They do NOT see the full description or supplier messages. Always add a message to the tenant if the title alone does not provide enough context about what will happen.

### Work order best practices
- Scope should be clear to the contractor without needing extra context
- If two merged jobs go to the same contractor, ensure the combined description is coherent
- For preferred contractors by trade, refer to the Contractor Key (to be created separately)

---

## Request Quotes — Complete Flow

1. Open the job → click **Request quotes**
   - Similar panel to work order but key differences: plural suppliers possible, no compliance section, no cost limit field, no "require to contact tenants" checkbox
2. **Select contractor(s):** can choose multiple suppliers to get competing quotes
3. **Message to supplier:** MUST include the word "quote" or "estimate" — contractors may assume a request without these words is a work order
4. **Message to owner:** optional — use if you want to keep the owner informed that quotes are being sought
5. **Message to tenant:** only include if the contractor may need to visit the property for quoting
6. Click **Send**

### Quote request best practices

- **"Knowable scope" test:** Can the contractor price the job without visiting? Spouting clean = yes (send photos + satellite imagery). Plumbing leak = no (needs site visit)
- PM may give a verbal price range first — owner may still want a formal quote before proceeding
- Attach photos including satellite imagery (Property Guru / Google Maps) so the contractor can assess remotely where possible
- When the quote comes back, forward to owner for approval via the standard approval flow

---

## Send to Owner for DIY — Complete Flow

1. Open the job → click **Send to owner for DIY** — a slide-out panel appears
2. **Email notification to owner:** ticked by default. Untick if already in email correspondence with the owner about this job
3. **Message to owner:** optional free text. Use when the owner hasn't been told about the tenant notification yet
4. **Email notification to tenant(s):** tick this — the notification goes to ALL tenants on the lease
5. **Message to tenant(s):** include who / when / what / where — e.g., "The owner has arranged for someone to come on Sunday afternoon to fix the spouting"
6. Click **Send to owner**

> **Critical:** The job must still be actioned and eventually closed. Sending to owner for DIY does not auto-close the job — leaving it open causes backlog. Follow up with the owner to confirm completion, then close the job.

---

## Owner-Declined Maintenance — Closure Flow

When the owner declines a maintenance item (common for non-urgent inspection suggestions):

1. Monitor the PM's email inbox for owner responses to inspection reports
2. When the owner declines: open Tapi, search for the property
3. Open the specific job
4. Click **Add note** → type a summary: "Owner doesn't want to service yet"
5. **Assign to:** appropriate agent (Property Partner / VA name) from the dropdown (options: No agent assigned / McKenzie Lawrence / Property Partner)
6. Click **Save**
7. Click **Add note** again → paste the **exact owner email text** verbatim, including the date
   - This creates an audit trail — the owner's own words are on record
8. Click **Save**
9. Click **More options** → **Close job**
10. Verify the job has been removed from the open jobs list

### "More options" dropdown menu (complete list)
Add photos | Attach file | Search for jobs | Duplicate job | Merge job | Cancel job | Close job

### Add Note feature
- Slide-out panel with: **Note** (free text area) and **Assign to** (dropdown: No agent assigned / McKenzie Lawrence / Property Partner)
- Click **Save** to post
- Notes appear in the Activity timeline on the job
- Best practice: copy exact owner email content into notes for audit trail — never paraphrase owner instructions

---

## Contractor Follow-up and Timelines

### Acceptance timelines
- Work order acceptance: usually 1–2 days
- Tapi auto-sends reminders at 12h–24h intervals until the contractor accepts
- If not accepted within 2 days → send a follow-up message via Tapi

### Completion timelines
- Most routine maintenance: completed within 2 weeks
- Some jobs take months (overseas parts, compliance/building work, specialist trades)
- Jobs sitting in **Scheduling** for too long → follow up with contractor via Tapi message, text message, phone call, or email (escalate in that order)

### Mid-job updates (expanded scope)

When a contractor calls back during a job reporting expanded scope or additional costs:

1. Take notes during the call — capture what the contractor found and the revised cost
2. Update the owner via email (use Shortwave AI to draft a professional message if speed is needed)
3. Keep the owner informed **BEFORE** a large invoice arrives — no surprises
4. Two communication channels:
   - **Email** (via PM's inbox): quick, but not tracked in Tapi
   - **Tapi "Send a message"**: slower to compose, but creates a tracked record in the job's Activity log
5. Use email for speed, but add a note to the Tapi job summarising what was communicated

> **Rule:** Never let an owner receive an invoice that's significantly larger than what was approved without prior communication.

---

## Status Pipeline — What Each Stage Means

| Status | Meaning | VA action |
|---|---|---|
| **Open jobs** | New/unactioned jobs | Triage and take action (approval, work order, quotes, DIY, close) |
| **Awaiting quotes** | Quote request sent to contractor(s) | Monitor for quote responses, then forward to owner |
| **Awaiting approval** | Approval request sent to owner | Follow the Day 0/3/7 follow-up protocol |
| **Scheduling job** | Work order sent, contractor arranging visit | Monitor for acceptance; follow up after 2 days if no response |
| **Awaiting repair** | Contractor has accepted and is scheduled | Monitor for completion; follow up if exceeding expected timeline |
| **Awaiting invoice** | Work completed, waiting for contractor invoice | Follow up with contractor if invoice is overdue |
| **Awaiting confirmation** | Invoice received, pending PM review/closure | PM or VA reviews and closes the job |

---

## Daily Workflow Checklist

1. Check Gmail for overnight Tapi notifications (concierge requests, owner replies, contractor updates)
2. Review the **Open jobs** bucket — triage and action new jobs
3. Review **Awaiting approval** — send Day 3 / Day 7 follow-ups as needed
4. Review **Scheduling job** — chase contractors who haven't accepted after 2 days
5. Review **Awaiting repair** — check for overdue jobs
6. Review **Awaiting invoice** — nudge contractors for outstanding invoices
7. Process any owner decline emails — add notes and close jobs
8. Log any mid-job updates or scope changes communicated during the day

!!! info "What's Next"
    - [Maintenance Lifecycle](maintenance-lifecycle.md) — full end-to-end maintenance process
    - [Invoice Processing & Property Tree Sync](tapi-invoices.md) — once work is completed
    - [Inspection Express Reports](../inspections/inspection-express.md) — inspection items that feed into Tapi
