# PLAYBOOK — Maintenance (Tapi-first) (Version 2)

**Version:** V2.1 (Updated from video walkthrough)  
**Last updated:** 2026-03-07

---

## Goal
Handle maintenance quickly and consistently with clean approvals, multi-party comms, correct invoicing, and full sync to Property Tree.

## Trigger
- Tenant request via website form
- Inspection-captured item (synced from Inspection Express into Tapi)
- Owner request

## Outputs (definition of done)
- Tenant acknowledged and update time set (for tenant-submitted requests)
- Triage completed (urgent vs routine)
- Owner approvals captured where required
- Contractor engaged (work order or quote)
- Invoice approved/coded and synced to Property Tree
- Owner/tenant notified appropriately; job closed and filed

---

## Stage 1 — Intake and acknowledgement

### Tenant-submitted requests
- Request lands in Tapi; PM/VA acknowledges tenant and sets next update time

### Inspection-captured items
- PM creates maintenance items in Inspection Express during the routine inspection
- Items auto-sync into Tapi (tagged "Reported via inspection")
- VA/PM Assistant reviews daily in Tapi, cross-referencing against the published inspection report PDF
- See **02_SOP_INSPECTION_EXPRESS_REPORT_PUBLISH_ACTIONS_TO_TAPI_V2.md** for full daily review process

---

## Stage 2 — Triage (urgent vs routine)

Urgent examples (act immediately — issue work order without owner pre-approval):
- Water leaks / flooding risk
- Hot water outage
- Power outage
- Sewerage
- Serious electrical hazard

Priority chattels (often handled quickly):
- Oven / cooktop
- Dishwasher
- Rangehood
- Heat pump

Routine: proceed to Stage 3 (approvals)

---

## Stage 3 — Approvals and quote-first

### Standard approval flow
- Send owner approval request in Tapi with: issue summary, risk, recommendation, cost estimate/quote-first, access plan
- Quote-first guideline for likely > $500 or uncertain scope

### Inspection-captured items — check before requesting approval
For items originating from an inspection:
1) **Check the PM's email inbox first** — the inspection report email already listed the maintenance items and the owner may have already replied with approval
2) If owner has already approved → skip the Tapi approval step and go directly to Stage 4 (send work order)
3) If no response → send the Tapi approval request using a structured message template:

> Hi [Owner name],
>
> These items were noted during the routine inspection at [address]. Are you happy for me to arrange a contractor to attend to them?
>
> Kind regards,
> [PM / VA name]

### Merging related jobs
If multiple inspection items at the same property require the same trade:
- Merge them in Tapi (More options → Merge job) before requesting approval or sending a work order
- Update the merged job title to reflect the combined scope
- Clean up the merged description — remove landlord-directed language, keep contractor-relevant detail

### Owner follow-up
- If no response after 3 business days → send follow-up via Tapi message thread
- Many inspection items are suggestions/improvements; landlords commonly don't respond to non-urgent items
- The Tapi follow-up process prevents items from falling through

---

## Stage 4 — Contractor engagement

- Work order includes scope, access, work order #, urgency, invoice instructions
- Select contractor based on trade and preference (refer to Contractor Key)
- Message to supplier: clear, brief instruction of what is needed
- Tick "Require contractor to contact tenants" for access arrangement
- Send a copy to the owner (default)
- Send a copy to the tenant with a brief message explaining what will happen

> **Note:** The tenant only sees the job title in their notification, not the full description. Add a message to the tenant with specifics if the title is not self-explanatory.

- Keep tenant and owner informed (Tapi allows multi-party messages)

---

## Stage 5 — Invoices and sync to Property Tree

- Invoices to PropertyPartner@tarpy.co.nz, matched by work order number
- Approve and code (owner vs tenant vs DIY) in Tapi
- Confirm sync to Property Tree before Monday night run

---

## Stage 6 — Close-out

- Notify owner invoice plan (paid from next rent funds or held if insufficient)
- Close the job with completion evidence and notes
- File key artifacts into Property Tree

SOPs:
- **02_SOP_INSPECTION_EXPRESS_REPORT_PUBLISH_ACTIONS_TO_TAPI_V2.md**
- **02_SOP_TAPI_INTAKE_TRIAGE_APPROVALS_WORKORDERS_V2.md**
- **02_SOP_TAPI_INVOICES_OWNER_TENANT_DIY_SYNC_TO_PROPERTYTREE_V2.md**
