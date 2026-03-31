# Inspection Lifecycle

**Version:** V2.3  
**Last updated:** 2026-03-31

---

## Goal
Run inspections consistently, with tenant confirmations, strong reporting, correct follow-up decisions, and maintenance captured into Tapi with owner approval obtained promptly.

## Trigger
- Routine inspections (quarterly)
- Ingoing/outgoing inspections
- Follow-up inspections when warranted

## Outputs (definition of done)
- Inspection scheduled and tenant confirmed
- Report published and sent to tenant and owner
- VA/PM Assistant has reviewed all maintenance items in Tapi
- Owner approval requested (or already received) for each maintenance item
- Follow-up actions created (tenant tasks, Tapi jobs, escalation)
- Evidence filed to Property Tree

---

## Stage 1 — Scheduling and confirmations (Property Tree)
- Schedule in Property Tree; ensure it appears in Inspection Express
- Send 10-day email and 9-day SMS to confirm
- Do not attend unless tenant confirms
- Update to "Confirmed" in Property Tree (manual)
- Send 24-hour reminder

SOP: [Scheduling & Confirmation (Property Tree)](pt-scheduling.md)

---

## Stage 2 — Inspection execution (Inspection Express)
- Photos: wide + detail for issues
- Notes: location + severity + required action
- PM creates maintenance items in Inspection Express during the inspection where relevant
- PM should describe each item clearly: what the issue is, what trade is needed, and any urgency context

SOP: [Reports & Actions (Inspection Express)](inspection-express.md)

---

## Stage 3 — Publish report and distribution
- PM finalises and publishes report in Inspection Express
- Report sent to tenant and owner via email (includes link + access code valid for 30 days)
- Email includes: maintenance items noted (room, title, description, photos) and a request for the owner to respond regarding any maintenance
- Tenant action list with deadlines where needed

SOP: [Reports & Actions (Inspection Express)](inspection-express.md)

---

## Stage 4 — Maintenance captured into Tapi (VA/PM Assistant daily task)

This is a critical daily workflow for the VA/PM Assistant:

??? info "Daily inspection review process (expand)"
    ### 4a) Daily review of Inspection Express
    - Log into Inspection Express each morning
    - Check "This Week" for any new finalised inspections
    - Flag any inspections still "In Progress" — remind PM to finalise

    ### 4b) Cross-reference with Tapi
    - Open Tapi side-by-side
    - For each finalised inspection, confirm every maintenance item from the PDF report appears as a job in Tapi
    - Missing items = sync failure → notify PM

    ### 4c) Prepare each Tapi job
    - Review and clean up job descriptions (remove landlord-directed questions, ensure contractor-friendly language)
    - Merge related jobs if applicable (e.g., two plumbing issues at the same property → merge into one job)
    - Determine the correct action for each job (approval, work order, quote, plan for later)

    ### 4d) Check email before actioning
    - Before requesting owner approval in Tapi, check the PM's inbox
    - The inspection report email already lists maintenance items — responsive owners may have already replied
    - If owner has approved → skip approval, send work order directly
    - If no response → send approval request in Tapi

    ### 4e) Request owner approval or send work order
    - For items needing approval: use "Ask owner for approval" in Tapi with a structured message
    - For items already approved: send work order directly, selecting the appropriate contractor

    ### 4f) Monitor and follow up
    - Check Tapi's "Awaiting approval" bucket daily
    - If no owner response after 3 business days, send follow-up via Tapi message thread
    - Some owners respond via email rather than the Tapi approval button — check both

!!! tip "Key Principle"
    Every maintenance item listed in an inspection report must be sent to the owner for approval (or actioned directly if already approved). Do not let items sit in Tapi without action.

SOP: [Reports & Actions (Inspection Express)](inspection-express.md)  
SOP: [Intake, Triage & Work Orders (Tapi)](../maintenance/tapi-intake.md)

---

## Stage 5 — Follow-up decision rules (tenant issues)
- Minor / one-off → photos by deadline or remedy by next inspection
- Careless damage / multiple issues → follow-up inspection; consider formal escalation
- Repeat issues → escalation ladder per Notices playbook

Playbook: [Notices & Comms](../day-to-day/notices-comms.md)

---

!!! info "What's Next"
    - [Scheduling & Confirmation](pt-scheduling.md) — set up inspections in Property Tree
    - [Reports & Actions](inspection-express.md) — publish reports and sync maintenance to Tapi
    - [Maintenance Lifecycle](../maintenance/maintenance-lifecycle.md) — handle inspection-captured maintenance items
