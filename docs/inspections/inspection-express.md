# Reports & Actions (Inspection Express)

**Version:** V2.6  
**Last updated:** 2026-04-01

---

## Overview
<span class="pp-verified-label">Verified from video analysis</span>

After each routine inspection is completed, the PM finalises the report in Inspection Express. The VA/PM Assistant then reviews it, ensures maintenance items have synced into Tapi, and initiates the landlord approval workflow. This SOP covers the full post-inspection handoff from Inspection Express through to Tapi action.

For **ingoing inspections**, the timing is different: complete the inspection as early as possible before move-in, then send the ingoing report or 360 report to the tenant on move-in morning with the key sheet so the tenant can review it during the statutory amendment window.

---

## Step 1 — Monitor Inspection Express daily

1) Log into Inspection Express → **Inspections** tab (the default view)
2) Filter to **This Week** to see all inspections conducted
3) Check the **Status** column for each inspection:
   - **Finalised** — ready for processing (proceed to Step 2)
   - **In Progress** — not yet complete; flag and remind PM to finalise
   - **Archived** — entry report or already processed
4) If an inspection is not finalised by the next business day, notify the PM

!!! tip "Timing"
    Check each morning. Ideally process the same day the inspection is finalised.

---

## Step 2 — Review the published inspection report

1) Click **View PDF Report** on each finalised inspection
2) Scroll to the **Maintenance Items** section of the PDF
3) For each maintenance item listed, note:
   - **Room / location** (e.g., Lounge room, Main Bathroom, Laundry)
   - **Category** (e.g., Overall)
   - **Title** (e.g., "Drip leak from shower mixer", "Tile cracking / floor movement")
   - **Description** — the PM's notes including severity, recommendation, and any photos referenced
4) Also review the **Inspection Findings** section for any tenant action items (these do NOT go to Tapi — they are tenant responsibilities with deadlines)

---

## Step 3 — Confirm maintenance items have synced to Tapi

1) Open **Tapi** (tapi.app/jobs) side-by-side with Inspection Express
2) In Tapi's Jobs list, look for newly created jobs matching the property address and maintenance item titles
3) Each maintenance item created in Inspection Express should appear as an individual job in Tapi with:
   - Status: **Open** (Choose action)
   - Source tag: **Reported via inspection**
   - Property address matching the inspection
   - Photos from the inspection attached
   - Description populated from the PM's notes
4) If any maintenance item from the report is **missing** in Tapi, notify the PM — the sync may have failed or the item was not created during the inspection

!!! warning "If the inspection is missing from Inspection Express or Tapi"
    First check the Property Tree inspection record. The inspection only syncs to Inspection Express when it is **Confirmed** and has a **future date/time**. If the date/time was edited, Property Tree may have pushed it back to **Tentative** and the sync will not occur until it is re-confirmed.

See also: [Maintenance Lifecycle](../maintenance/maintenance-lifecycle.md) for the full maintenance workflow after sync.

---

## Step 4 — Assess and prepare each Tapi job

For each inspection-created job in Tapi:

### 4a) Review the job description
- Check the description is clear enough for a contractor or landlord to understand
- Remove any language directed at the landlord (e.g., "Are you happy for me to...") — this is the PM's question in the inspection report, not needed in the work order
- Ensure the description focuses on: **what the issue is**, **what needs to be done**, and **what trade is required**

### 4b) Determine if jobs should be merged
- If multiple maintenance items at the same property require the **same trade** (e.g., two plumbing jobs), consider merging them:
  1) Open one of the jobs in Tapi
  2) Click **More options** → **Merge job**
  3) Tapi will show other open jobs at the same property — only jobs "waiting to be actioned" can be merged
  4) Select the related job(s) to merge
  5) Tick **Edit description** to review and clean up the combined description
  6) Update the **Title** to summarise both issues (e.g., "Drip leak from shower mixer + potential leak under laundry floor")
  7) Click **Merge** — the job will combine descriptions, photos, and context from both originals
  8) Refresh the page to see the merged job with updated Activity log

!!! note "Merge Audit Trail"
    The merged job's Activity section will show "McKenzie Lawrence merged the following job: [Job Title]" for audit trail.

### 4c) Determine the correct Tapi action
The Tapi Recommendation panel on each job offers these options:

| Action | When to use |
|---|---|
| **Ask owner for approval** | Default for routine inspection-captured items — use this unless the owner has already responded |
| **Send work order** | Owner has already approved (e.g., responded to the inspection report email) OR urgent item |
| **Request quotes** | Item is likely > $500 or scope is uncertain |
| **Send to owner for DIY** | Owner has stated they will handle it themselves |
| **Plan for later** | Non-urgent item that PM has flagged for future action |

---

## Step 5 — Check email before requesting approval

Before sending an approval request in Tapi:

1) Check the PM's email inbox (and any forwarded inspection report threads) to see if the landlord has **already responded** to the maintenance items listed in the inspection report
2) If the owner has already replied with approval (e.g., "OK to fix" or "go ahead"), **skip the approval step** — proceed directly to sending a work order (Step 7)
3) If no response yet, proceed with the approval request (Step 6)

!!! warning "Why This Matters"
    The inspection report email sent to the owner already lists maintenance items. Responsive landlords may reply the same day. Sending a duplicate approval request in Tapi when they've already approved wastes their time and looks disjointed.

---

## Step 6 — Ask owner for approval in Tapi

1) Open the job in Tapi
2) Click **Ask owner for approval** in the Tapi Recommendation panel
3) A notification panel appears with:
   - **Send an email notification** checkbox (keep ticked)
   - **Add personal message** text box
4) Write a clear approval message, e.g.:

> Hi [Owner name],
>
> These items were noted during the routine inspection at [address]. Are you happy for me to arrange a contractor to attend to them?
>
> Kind regards,
> [PM name]

5) Click **Send to owner**
6) The owner receives an email from Tapi with a button to view the full work order details and click **Approve** directly

### Follow-up protocol
- If no owner response after **3 business days**, send a follow-up message via the job's messaging thread in Tapi
- Continue checking Tapi daily for owner responses — owners may reply inside the Tapi message thread or approve via the button
- Some owners respond by email instead of using the Tapi button — check both channels

---

## Step 7 — Send work order to contractor (when approved)

When the owner has approved (either via Tapi approval button, Tapi message, or email reply):

1) Open the job in Tapi and click **Send work order**
2) **Select contractor** — search by name or trade (see Contractor Key for preferred suppliers per trade)
3) Fill in the **Send work order** panel:
   - **Insurance / compliance**: Required for electrical, plumbing, and gas work; untick for general handyman jobs
   - **Require contractor to contact tenants**: Tick this in most cases — contractor arranges access time
   - **Cost limit**: Set if applicable (inc. GST)
   - **Message to supplier**: Brief instruction, e.g., "Please replace 1x oyster light in the living room"
   - **Send reminder after**: Default 3 days
   - **Send a copy to the owner**: Ticked by default — owner gets notified a contractor has been engaged
   - **Message to owner**: Usually leave blank if already in correspondence; owner gets the work order copy automatically
   - **Send a copy to the tenant**: Tick this
   - **Message to tenant**: Brief heads-up, e.g., "Hi [tenant name], a contractor will be in contact with you to [brief description of work]"
   - **Health & safety / hazards**: Add if relevant to the property
4) Click **Send work order**
5) Job moves to **Scheduling** status — "Awaiting supplier to schedule job with tenant"

---

## Step 8 — File inspection report to Property Tree

1) Download the published PDF report from Inspection Express
2) File to Property Tree docs under **04 Inspections** using naming convention:
   `YYYY-MM-DD Routine Inspection Report - [Address]`

## Ingoing inspection distribution and finalisation
<span class="pp-verified-label">Verified from video analysis</span>

Use this flow for **ingoing** inspections rather than the routine-inspection owner-approval flow above:

1) Complete the ingoing inspection as soon as possible and well before the tenant moves in
2) On the morning of move-in, send the ingoing report or 360 report to the tenant together with the key sheet
3) Advise the tenant they have **14 days** to review the report and submit any corrections or additions
4) If amendments come back within the 14-day window, review and incorporate them according to the PM's decision
5) If no amendments come back within 14 days, treat the ingoing report as finalised
6) Once finalised, confirm the final copy has automatically synced back into Property Tree and is available to the landlord through the owner portal

---

## Key system screens reference

| System | URL | Key page |
|---|---|---|
| Inspection Express | admin.propertyexpress.com/console/inspections | Inspections list (filter: This Week) |
| Tapi | tapi.app/jobs | Jobs list (filter: Open, sort by Last action) |

---

## Tapi Jobs dashboard overview

The Tapi Jobs page shows status buckets across the top:
- **Open jobs** — new items needing action
- **Awaiting quotes** — quote requested from contractor
- **Awaiting approval** — sent to owner, waiting for response
- **Scheduling job** — work order sent, contractor scheduling
- **Awaiting repair** — contractor engaged, work in progress
- **Awaiting invoice** — job done, waiting for contractor invoice
- **Awaiting confirmation** — work complete, awaiting verification

---

!!! info "What's Next"
    - [Maintenance Lifecycle](../maintenance/maintenance-lifecycle.md) — handle items synced from inspections
    - [Intake, Triage & Work Orders](../maintenance/tapi-intake.md) — process the Tapi jobs created from inspections
