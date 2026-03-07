# PLAYBOOK — Inspections (Property Tree → Inspection Express → Tapi) (Version 2)

**Version:** V2 (Full)  
**Last updated:** 2026-02-24

---

## Goal
Run inspections consistently, with tenant confirmations, strong reporting, correct follow-up decisions, and maintenance captured into Tapi.

## Trigger
- Routine inspections (quarterly)
- Ingoing/outgoing inspections
- Follow-up inspections when warranted

## Outputs (definition of done)
- Inspection scheduled and tenant confirmed
- Report published and sent to tenant and owner
- Follow-up actions created (tenant tasks, Tapi jobs, escalation)
- Evidence filed to Property Tree

---

## Stage 1 — Scheduling and confirmations (Property Tree)
- schedule in Property Tree; ensure it appears in Inspection Express
- send 10-day email and 9-day SMS to confirm
- do not attend unless tenant confirms
- update to “Confirmed” in Property Tree (manual)
- send 24-hour reminder

SOP: **02_SOP_PROPERTYTREE_INSPECTION_SCHEDULING_CONFIRMATION_V2.md**

---

## Stage 2 — Inspection execution (Inspection Express)
- photos: wide + detail for issues
- notes: location + severity + required action

---

## Stage 3 — Publish report and distribution
- publish report; send to tenant and owner
- tenant action list with deadlines where needed

SOP: **02_SOP_INSPECTION_EXPRESS_REPORT_PUBLISH_ACTIONS_TO_TAPI_V2.md**

---

## Stage 4 — Maintenance captured into Tapi
- create maintenance items in Inspection Express during inspection where relevant
- confirm they sync into Tapi for approvals/work orders

---

## Stage 5 — Follow-up decision rules (tenant issues)
- Minor/one-off → photos by deadline or remedy by next inspection
- Careless damage / multiple issues → follow-up inspection; consider formal escalation
- Repeat issues → escalation ladder per Notices playbook

Playbook: **01_PLAYBOOK_NOTICES_AND_COMMS_V2.md**
