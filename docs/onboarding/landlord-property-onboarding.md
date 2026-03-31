# Landlord & Property Setup

**Version:** V2.3  
**Last updated:** 2026-03-31

---

## Goal
Bring a new landlord and property into your full stack with zero missing information:
- Property Tree record (owner + property) is correct,
- Property Tree docs folders exist and key documents are filed,
- TPS is set up for leasing, compliance, agreements, and renewals,
- access and key handling is documented,
- compliance readiness is tracked (Healthy Homes and related).

## Trigger
Management authority signed OR takeover date confirmed.

## Outputs (definition of done)
- Owner + property created in Property Tree with correct fee/disbursement settings
- Property Tree docs folders created and linked in the property record
- TPS property created; compliance section populated enough to generate agreements
- Keys/access plan documented (including tenant-in-place viewings)
- Any compliance gaps converted into Tapi jobs (quote/work order plan)
- Owner welcome message sent (approval preferences recorded)

---

## Stage 1 — Intake (collect and verify)
Collect (and store in Property Tree docs "01 Management & Owner Docs"):
- Management authority / agreement (incl. spend threshold if present)
- Owner identity/contact details + bank account details
- Preferred communication method and approval style
- Insurance details (if supplied)
- Property details: chattels list, utilities notes, parking/access constraints
- Current tenancy status: vacant vs tenanted; key dates; rent; bond status

!!! warning "Takeover from another agency"
    If taking over from another agency, add a takeover checklist:

    - obtain last ingoing report, latest routine report, bond details, key notices, compliance evidence
    - confirm any arrears/disputes and document current status

---

## Stage 2 — Create the Property Tree master record
Follow SOP: [Property Tree — Create Owner & Property](pt-create-owner-property.md)

Complete:
- owner record
- property record
- fees and statement/disbursement settings
- establish the Property Tree property file structure (docs folders)

---

## Stage 3 — Create/verify TPS property setup
Follow SOP: [TPS — Property & Trade Me Setup](tps-property-setup.md)

Populate:
- property basics (so you can lease)
- compliance fields (so you can generate agreements and statements)
- landlord details required by TPS

---

## Stage 4 — Access plan and keys
Document in Property Tree property notes + "01 Management & Owner Docs":
- key count and where held
- lockbox info (if used)
- tenant-in-place viewings constraints and preferred windows
- contractor access protocol (contact order and times)

---

## Stage 5 — Compliance readiness (Healthy Homes and other)
Run the compliance playbook if anything is missing:
- [Compliance & Healthy Homes](compliance-healthy-homes.md)

Convert gaps into Tapi jobs (quote/work order) with owner approval plan.

---

## Stage 6 — Go-live QA
Run onboarding checklist:
- [Execution Checklists](../day-to-day/execution-checklists.md)

---

## Templates used
- Owner welcome email ([Notice & Email Templates](../day-to-day/notice-email-templates.md))
- Onboarding checklist

!!! info "What's Next"
    - [Property Tree — Create Owner & Property](pt-create-owner-property.md) — set up the master record
    - [TPS — Property & Trade Me Setup](tps-property-setup.md) — configure TPS for leasing and compliance
    - [Compliance & Healthy Homes](compliance-healthy-homes.md) — ensure pre-tenancy compliance
