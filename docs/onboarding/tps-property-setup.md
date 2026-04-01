# TPS — Property & Trade Me Setup

**Version:** V2.4  
**Last updated:** 2026-04-01

---

## Purpose / Outcome
TPS property is fully configured so you can run BookMe viewings, receive applications, run checks, generate tenancy agreements, and execute renewals/extensions.

## Trigger
New property onboarded OR ready to lease.

---

## Step 1 — Create the Property in TPS
<span class="pp-verified-label">Verified from video analysis</span>

Navigate to **Properties → + New Property** and complete the setup fields.

### Rent / Move-in Costs

| Field | Guidance |
|---|---|
| **Available Date** | First date a tenant can move in — from the management agreement or owner correspondence |
| **Rent** | Weekly rent amount |
| **Period** | **Weekly** or **Fortnightly** only — under the Residential Tenancies Act, a landlord can only ask for up to 2 weeks' rent in advance, so monthly is not an option |
| **In Advance** | 1 Week (weekly) or 2 Weeks (fortnightly) |
| **Bond** | 4 weeks' rent — this is the maximum general bond allowed |
| **Pet Bond** | 2 weeks' rent additional — apply if a tenant will have a pet at the property |

### Property Details

| Field | Source |
|---|---|
| Unit / Street Number / Street Name | Management agreement or Google |
| Suburb / City / Post Code | Management agreement or Google |
| Notes/Details | Only if specific notes are needed |
| Alarm Details | Alarm code from management agreement (if any) |
| **TRADEME ID** | Paste the Trade Me Listing ID here after listing — this enables BookMe inquiry forwarding |

### Agent Details

- Always select **McKenzie Lawrence** as the Property Manager
- When logged in as the VA, verify the agent is set correctly — it may default to your name

### Landlord / Owner Details

- **Full Name**: from the management agreement (individual, trust, or company name)
- **Email**: landlord's email address

!!! warning "Ownership changes"
    Landlords sometimes change their ownership structure during a tenancy (e.g., move to a company or trust). Always verify the landlord name in TPS matches Property Tree, especially at renewal time.

---

## Step 2 — Property Configuration Tabs

### Pets

Select **"By Negotiation"** (or "By Application") — since late 2025, NZ pet laws require landlords to consider all pet requests. You cannot select "No" outright.

### Smoking

Always set to **No** for indoors — smoking is never permitted indoors at any property.

### Dwelling Type & Specifications

| Field | Guidance |
|---|---|
| Dwelling Type | House, Townhouse, Apartment, etc. — most properties are House or Townhouse |
| Bedrooms | Bedroom count from listing or management agreement |
| Bathrooms | Bathroom count |
| Car Parks | Garage + off-street parking count |
| Max Residents | PM's judgment — roughly 2 per bedroom as a guideline (e.g., 2-bed = 4 max). The tenancy agreement specifies approved residents; more than approved = potential tenancy breach |

### Images

Upload property images — source from the Trade Me listing or request from the PM.

---

## Step 3 — Chattels

The Chattels section contains a checklist of items present at the property (approximately 21 checkbox items). Tick what is known to be at the property.

All chattels data entered here flows directly onto the tenancy agreement. For a comprehensive list, add: *"A full list of chattels plus key sheet will be provided with the ingoing condition report."*

---

## Step 4 — Liability

The Liability section determines who pays for utilities and maintenance:

| Item | Typical Setting | Notes |
|---|---|---|
| **Power** | Tenant | ~99% of properties. Rare exceptions where landlord pays (e.g., no separate meter) |
| **Gas** | Tenant | If applicable |
| **Water** | Tenant (excess charges only) | In Christchurch, water is not consumption-based unless usage exceeds ~600–700 litres/day, at which point excess charges apply. A clause in the tenancy agreement covers this. |
| **Gardens / Lawns** | Tenant | Sometimes an owner takes responsibility for part of a garden, or a body corporate manages shared grounds in multi-unit complexes |

---

## Step 5 — Compliance (Healthy Homes)

All properties must be **Healthy Homes compliant** (deadline: 1 July 2025). The compliance section covers:

- **Heating** — adequate fixed heating in the main living area
- **Insulation** — ceiling and underfloor insulation meeting standards
- **Ventilation** — functioning extractor fans in kitchen, bathroom, and any rooms with a cooking/bathing/shower appliance
- **Moisture ingress and drainage** — no unaddressed moisture or drainage issues
- **Draught stopping** — external doors and windows reasonably draught-free
- **Smoke alarms** — working smoke alarms (legally required since 2016, operationally tracked alongside Healthy Homes)

Transfer information from the **Healthy Homes assessment report** (e.g., from HomelyHomes or similar assessment provider) into the compliance fields. If any item is non-compliant, the remediation must be completed before the tenancy start date.

See: [Compliance & Healthy Homes](compliance-healthy-homes.md)

---

## Step 6 — Insurance

Enter the landlord's insurance details from their policy documents:

| Field | Source |
|---|---|
| Insurance Type | From landlord's insurance certificate |
| **Excess Amount** | From landlord's policy — this is the most important field for the tenancy agreement's insurance statement |

The insurance information is included in the tenancy agreement and must be disclosed to the tenant.

---

## Step 7 — Clauses

TPS provides a clause management system with four sub-sections:

| Section | Content |
|---|---|
| **E-Bundle** | Standard TPS clauses |
| **Office Specific** | Property Partner custom clauses |
| **Property Specific** | Unique clauses for individual properties (parking restrictions, owner garden access, etc.) |
| **Total Tenancy** | Additional TPS package clauses |

Toggle clauses on/off using the selection panel on the right. The PM will advise on property-specific clauses as needed.

---

## Step 8 — Attachments

Upload supporting documents that will be included with or available alongside the tenancy agreement:

- Healthy Homes assessment report
- Owner's insurance certificate
- Any other relevant property-specific documents

---

## Step 9 — Trade Me Listing & BookMe Link

1. Publish the Trade Me listing with property photos, details, and rent
2. Copy the **Listing ID** from the bottom of the Trade Me listing page
3. Paste into the **TRADEME ID** field in TPS Property Details
4. Confirm enquiries appear in the **BookMe** dashboard (test with a sample inquiry if needed)

See: [Viewings & BookMe (TPS)](../leasing/tps-viewings-bookme.md)

---

## Property Status Flow

| Status | Trigger |
|---|---|
| **Available** | Default when property is created and ready for leasing |
| **Under Offer** | Automatic when an application is approved in TPS |
| **Occupied** | Manual change — update once the tenant has moved in |

---

## Tenancy Agreement Generation

All data entered across the property tabs (details, chattels, liability, compliance, insurance, clauses) is used to generate the tenancy agreement. When you create or renew an agreement, TPS populates it from these fields.

See: [Agreements & Signing (TPS)](../leasing/tps-agreements-signing.md)

---

## Quality Checks

!!! tip "Verification checklist"
    - TPS property data accurate and complete
    - Compliance fields match the Healthy Homes assessment report
    - Insurance excess amount entered
    - Landlord/owner name matches Property Tree
    - Pet setting is "By Negotiation/Application" (not "No")
    - Agent set to McKenzie Lawrence
    - BookMe routing confirmed (Trade Me ID entered, test inquiry if needed)

---

!!! info "What's Next"
    - [Leasing Lifecycle](../leasing/leasing-lifecycle.md) — start marketing and leasing the property
    - [Viewings & BookMe (TPS)](../leasing/tps-viewings-bookme.md) — set up viewings once enquiries flow in
    - [Compliance & Healthy Homes](compliance-healthy-homes.md) — ensure compliance fields are backed by evidence
