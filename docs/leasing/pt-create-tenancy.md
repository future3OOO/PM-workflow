# Property Tree — Create Tenancy & Dates

**Version:** V2.3  
**Last updated:** 2026-03-31

---

## Purpose / Outcome
Create a tenancy record in Property Tree that matches the signed TPS agreement exactly and stores key documents in the property file.

Part of: [Leasing Lifecycle](leasing-lifecycle.md) → Stage 7

## Trigger
TPS tenancy agreement signed; bond workflow initiated.

## Inputs
- Signed TPS agreement PDF
- Tenant names and contacts
- Start/end dates (if fixed) and rent amount/frequency
- Bond confirmation (when available)

---

## Steps
1) Create tenancy under the property (fixed/periodic)
2) Add tenants (names/contacts match agreement)
3) Enter rent + key dates exactly as per signed agreement
4) Upload documents into Property Tree docs:
   - agreement → 02 Tenancy Agreements
   - bond confirmation → 02 Tenancy Agreements (or 06 Notices, but be consistent)
   - compliance docs → 03 Compliance
5) Add internal notes (if needed) about bond status and any special terms

---

## Quality checks

!!! warning "Record accuracy"
    - Dates must match the signed agreement exactly
    - Rent must match the signed agreement exactly
    - Agreement PDF must be stored in the property record
    - Bond status must be tracked until confirmed

## Close-out
- Trigger tenant onboarding and ingoing inspection scheduling

!!! info "What's Next"
    - [Tenant Onboarding](tenant-onboarding.md) — send welcome pack and schedule ingoing inspection
    - [Property Tree — Filing & Naming](../onboarding/pt-filing-naming.md) — use correct naming conventions for uploaded docs
