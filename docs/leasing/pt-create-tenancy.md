# Property Tree — Create Tenancy & Dates

**Version:** V2.5  
**Last updated:** 2026-04-01

---

## Purpose / Outcome
Create a tenancy record in Property Tree that matches the signed TPS agreement exactly, stores the core documents in the property file, and sets up the first inspection correctly.

Part of: [Leasing Lifecycle](leasing-lifecycle.md) → Stage 7

## Trigger
TPS tenancy agreement signed or ready to be mirrored in Property Tree; bond workflow initiated.

## Inputs
- Signed TPS agreement PDF
- Tenant names and contacts
- Start/end dates (if fixed) and rent amount/frequency
- Bond confirmation (when available)
- TPS application / agreement view for exact tenant name formatting

---

## Steps
<span class="pp-verified-label">Verified from video analysis</span>

### 1) Open the property and create the tenancy

Navigate to: **Property Tree → property → add tenancy**

- Create the tenancy under the correct property
- Select the correct tenancy type
- Use the TPS agreement as the source of truth for tenancy dates

### 2) Enter rent and lease dates exactly

- Enter the rent amount exactly as per the TPS agreement
- Enter the lease start and end dates exactly as per the TPS agreement
- Do not rely on the management agreement alone for rent, because it can be stale by the time the tenancy is created
- Set the bond amount to **4 weeks rent**
- For the normal Christchurch case, leave water-charging in Property Tree aligned with the agreement position that the tenant only pays **excess charges**

### 3) Add the tenants carefully

Navigate to: **Property Tree tenancy record → tenants / occupants section**

- Add each tenant individually
- Copy the tenant names from TPS rather than retyping them from memory
- Check spelling and ordering carefully
- For each tenant, tick:
  - auto email receipts
  - do not contact for promotional offers / marketing
- Set the correct primary tenant before saving

### 4) Set future review dates and internal tenancy settings

- Enter the next rent review date roughly **2 to 3 months before** the fixed-term end date
- Check any internal tenancy notes or special terms that need to be visible to the PM

### 5) File the core documents

Upload documents into Property Tree docs:

- agreement → `02 Tenancy Agreements`
- bond confirmation → `02 Tenancy Agreements` or `06 Notices & Key Correspondence` if that is your chosen house standard
- compliance docs → `03 Compliance`

### 6) Add the ingoing inspection immediately after save
<span class="pp-verified-label">Verified from video analysis</span>

Navigate to: **Property Tree tenancy record → Inspections → (+)**

- Add an **Ingoing** inspection after the tenancy is saved
- Assign it to the PM
- Use a **future** time, even if that is only a few hours later on the same day
- Save it as **Confirmed**
- This is required for the inspection to sync through to Inspection Express

---

## Quality checks

!!! warning "Record accuracy"
    - Dates must match the signed agreement exactly
    - Rent must match the signed agreement exactly
    - Tenant names must match TPS exactly
    - Agreement PDF must be stored in the property record
    - Bond status must be tracked until confirmed
    - Rent review date should be set in advance rather than left blank
    - Ingoing inspection must be future-dated and confirmed so it syncs correctly

## Close-out
- Trigger tenant onboarding and ingoing inspection scheduling

!!! info "What's Next"
    - [Tenant Onboarding](tenant-onboarding.md) — send welcome pack and schedule ingoing inspection
    - [Property Tree — Filing & Naming](../onboarding/pt-filing-naming.md) — use correct naming conventions for uploaded docs
