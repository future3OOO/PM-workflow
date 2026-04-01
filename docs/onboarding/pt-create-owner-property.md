# Property Tree — Create Owner & Property

**Version:** V2.5  
**Last updated:** 2026-04-01

---

## Purpose / Outcome
A complete Property Tree record for the owner and property, with standard docs folders created so the property file stays consistent across the business.

## Trigger
New management authority signed OR new property onboard instruction.

## Inputs
- Owner legal name(s), email, phone, postal address, bank details
- Management agreement details (fees, spend threshold if any)
- Property details (address, chattels, access plan)
- Any existing compliance/insurance documents

---

## Steps (field checklist)
<span class="pp-verified-label">Verified from video analysis</span>

!!! info "Field names"
    Button names may vary; treat this as the required data list.

### 1) Create Owner
Navigate to: **Property Tree → add owner / contact**

- Create owner/client record
- Enter and verify:
  - full legal names
  - email + phone
  - postal address
  - bank account
- Verify the bank account against the owner's bank statement before any payment is ever made to that owner
- Notes:
  - approvals preference (approve/decline/quote first)
  - any spend threshold from management agreement

### 2) Create Property
Navigate to: **Property Tree → add property**

- Create property record
- Enter and verify:
  - correct property address
  - chattels list
  - access notes (keys/lockbox/tenant constraints)
  - compliance notes (what exists/what missing)
  - preferred contractors (if any)
- Use the **management agreement commencement date** for **Authority Start Date**
- Use the **management agreement** for the **Expenditure Limit**
- Property type is usually `House` or `Townhouse`

### 3) Apply financial settings
- management fee settings (per agreement)
- disbursement rules and statement frequency
- set owner statements to the normal operating preference
- do not assume the default management fee is correct; override it if the agreement is different
- account for GST in the effective percentage where needed

### 4) Create Property Tree "property file" docs folders
Create:
- 01 Management & Owner Docs
- 02 Tenancy Agreements
- 03 Compliance (Healthy Homes + related)
- 04 Inspections (ingoing/routine/outgoing)
- 05 Maintenance (approvals, quotes, invoices)
- 06 Notices & Key Correspondence
- 07 Insurance & Certificates

### 5) Upload/link key documents
Upload to 01 / 07 / 03 as appropriate:
- management authority
- insurance (if supplied)
- compliance evidence (if supplied)

---

## Quality checks

!!! warning "Verify before closing"
    - Bank details match the bank statement
    - Address correct
    - Fees correct for this management agreement
    - Docs folders exist
    - Any missing items captured as tasks

## Close-out
- Mark onboarding checklist complete

!!! info "What's Next"
    - [TPS — Property & Trade Me Setup](tps-property-setup.md) — configure TPS for leasing
    - [Property Tree — Filing & Naming](pt-filing-naming.md) — naming conventions for uploaded docs
    - [Compliance & Healthy Homes](compliance-healthy-homes.md) — check compliance readiness
