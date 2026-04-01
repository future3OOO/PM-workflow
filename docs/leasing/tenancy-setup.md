# Tenancy Setup

**Version:** V2.6  
**Last updated:** 2026-04-01

---

## Goal
Turn an approved TPS application into a legally compliant tenancy with perfect records:
- signed agreement,
- bond collected into trust and lodged with Tenancy Services via TPS workflow,
- tenancy created in Property Tree with accurate dates and rent,
- property file updated (agreement, bond confirmation, compliance evidence),
- tenant onboarding triggered (welcome pack and ingoing inspection).

## Trigger
Tenant approved in TPS and proceeds with tenancy setup.

## Outputs (definition of done)
- Signed agreement stored in Property Tree docs
- Bond payment completed and confirmation stored
- Tenancy record in Property Tree matches agreement exactly
- Welcome pack sent and ingoing inspection scheduled
- Any compliance evidence stored in Property Tree (and TPS compliance section updated)

---

## Stage 1 — Agreement in TPS
<span class="pp-verified-label">Verified from video analysis</span>

- Mark the successful application in TPS
- Create the **draft agreement before sending the acceptance letter** so the payment reference exists
- Confirm the move-in date with the tenant
- Review agreement fields carefully:
  - dates
  - next rent payment date
  - liability
  - compliance
  - insurance excess
  - clauses
- Send for signing and track completion
- Export signed agreement PDF

SOP: [Agreements & Signing (TPS)](tps-agreements-signing.md)

---

## Stage 2 — Collect move-in funds into trust
- Use the TPS-generated payment reference in the tenant instructions
- Collect bond and initial rent into your trust account (your standard)
- Record receipt and allocate correctly for reporting

---

## Stage 3 — Lodge bond (TPS + Tenancy Services integration)
<span class="pp-verified-label">Verified from video analysis</span>

- Verify the bond has actually been received in Property Tree before lodging
- In TPS, enter `Received General Bond` if needed and set `Received Status` to `Fully Paid`
- Fix any missing bond-form details that stop the record reaching `Ready`
- Lodge the bond in TPS using `Direct Credit`
- Wait for the Tenancy Services payment-instruction email with the payment reference and bank account details
- Pay Tenancy Services from trust using those emailed details
- Track until the later bond lodgement confirmation / receipt arrives
- File confirmation into Property Tree docs

SOP: [Bond Lodgement](bond-lodgement.md)

---

## Stage 4 — Create tenancy in Property Tree
<span class="pp-verified-label">Verified from video analysis</span>

- Create tenancy record and enter rent + dates exactly as per agreement
- Add each tenant individually and copy names from TPS exactly
- Set the rent review date roughly 2 to 3 months before fixed-term end
- Upload agreement and bond confirmation to Property Tree docs
- Ensure landlord portal visibility is appropriate (docs are the owner-facing file)

SOP: [Property Tree — Create Tenancy & Dates](pt-create-tenancy.md)

---

## Stage 5 — Trigger onboarding and inspections
<span class="pp-verified-label">Verified from video analysis</span>

- Send welcome pack
- Add the ingoing inspection in Property Tree with a future time and `Confirmed` status so it syncs to Inspection Express

Playbook: [Tenant Onboarding](tenant-onboarding.md)

!!! info "What's Next"
    - [Tenant Onboarding](tenant-onboarding.md) — send welcome pack and schedule ingoing inspection
    - [Property Tree — Create Tenancy & Dates](pt-create-tenancy.md) — create the Property Tree tenancy record
