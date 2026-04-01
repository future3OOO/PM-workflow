# Agreements & Signing (TPS)

**Version:** V2.4  
**Last updated:** 2026-04-01

---

Part of: [Leasing Lifecycle](leasing-lifecycle.md) → Stage 6

## New tenancy agreement

1) Generate agreement in TPS (tenancy type, dates, rent, parties)
2) Confirm compliance section is correct (agreement readiness)
3) Send for digital signing via tenant portal
4) Export signed agreement PDF
5) Upload to Property Tree docs (02 Tenancy Agreements)
6) Store compliance evidence in Property Tree (03 Compliance)

!!! warning "Compliance check"
    Step 2 is critical — incorrect compliance fields produce incorrect tenancy agreements and compliance statements. Always verify before sending for signing.

---

## Renewals — Full TPS Wizard Walkthrough
<span class="pp-verified-label">Verified from video analysis</span>

### Prerequisites

Before starting the renewal wizard:

- Written confirmation from **both** the landlord **and** the tenant agreeing to renew
- Rent increase already entered in Property Tree's rent schedule (see [Renewals & Rent Reviews — Stage 4](../renewals-exits/renewals-rent-reviews.md))
- Formal rent increase notice generated and saved (PDF)

### Access the renewal

1. In TPS, navigate to **Properties** → search for the property → click into **Agreements** tab
2. Set **Filter by Status** to "All" to ensure results appear
3. Click the **three-dot menu (⋮)** on the current agreement → select **Renewal**

### Step 1 — Property / Agreement Type

- Select **Managed Tenancy**
- Select **Renewal** from the four agreement type cards (New Standard / Renewal / Extension / Variation)
- Verify **agent details**: McKenzie Lawrence with correct email and mobile
- Verify **landlord/owner name** matches Property Tree — ownership names can change during a tenancy (company restructure, new bank account)

!!! warning "Check owner details"
    Always cross-reference the landlord name in TPS with Property Tree. If the owner has changed their company name or structure during the tenancy, Property Tree may have the updated details while TPS still shows the old name.

### Step 2 — Property Costs

**Current Tenancy Details:**

- Select **Fixed Term**
- **Current Tenancy Start Date** and **End Date**: verify these match Property Tree
- **Next Rent Payment Date**: get this from Property Tree → Lease & Rent → **Effective Paid To** date, then add one day. This date must not be before the rent-in-advance expiry.

!!! warning "Do not trust the current tenancy end date blindly"
    TPS sometimes shows the wrong current tenancy end date when you open a renewal. Always cross-check the current tenancy end date against Property Tree before using it to set the renewal start date.

**Renewal Details:**

- **Renewal Start Date**: the day after the current tenancy end date
- **Renewal End Date**: use the **52-week rule** — for weekly tenancies, 12 months = 52 weeks = 364 days. The end date is one day less than the start date (e.g., start 12 April → end 11 April the following year)
- **New Rent Amount**: enter the increased amount (must match Property Tree rent schedule)
- **Date New Rent Amount Takes Effect**: must match the effective date in Property Tree's rent schedule
- **Next Rent Review Date**: set approximately 3 months before the new tenancy end date

!!! info "TPS–Property Tree API"
    The TPS → Property Tree sync for the Next Rent Review Date is currently broken. You must manually update Property Tree's rent review date separately.

**Bond Details:**

- **Current General Bond Amount Held**: verify against Property Tree
- **General Bond Amount Top Up**: set to $0 unless specifically increasing the bond
- **New Bond Total**: should match current bond unless a top-up is being applied

### Step 3 — Tenant Details

- For each tenant on the agreement, change **STATUS** from "Joining" to **"Remaining"**

!!! warning "Known TPS bug"
    The tenant status defaults to "Joining" on renewals even though the tenants are remaining. This is a known bug — always manually change each tenant to "Remaining."

- Verify tenant contact details (name, phone, email)
- Confirm **Address for Service** is set to the tenancy address

### Step 4 — Bond Details

- If no bond change: ensure **"Do not send any bond forms to tenants"** is selected
- Leave the **Guarantor** section unselected (unless specifically required)

### Step 5 — Tenant Requirements

- **Pets**: select **"By Application"** — since December 2025, selecting "No" is no longer an option under NZ pet law changes. All pet requests must be considered by application.

### Step 6 — Compliance

**Smoke Alarms:**

- Update the **last check date** from the SATS smoke alarm testing website (`sats.co.nz`) or the last routine inspection date
- Navigate to SATS → My Properties → select property → check service date and expiry dates
- Verify expiry dates are correct in TPS
- The **smoke alarm assessment date** is when smoke alarms were first assessed (usually during the healthy homes report) — leave unchanged unless updated

**Insurance:**

- Verify insurance details haven't changed — check with the landlord if unsure

**Healthy Homes Statement:**

- Turn off **General Exemptions** (rarely used; known TPS bug re-enables this toggle on renewals)
- All healthy homes sections (heating, insulation, ventilation, moisture, draught stopping, drainage) should show **"Yes"**
- If any section shows "No": investigate in Property Tree invoices or Tapi work orders to confirm if the work was completed but not updated in TPS

??? info "Investigating a 'No' in healthy homes (expand)"
    1. Open Property Tree → **Documents** tab → look for owner invoices related to the non-compliant area
    2. Check Tapi for completed work orders at the property
    3. Draught stopping is the most commonly missed update (e.g., door seals added but TPS not updated)
    4. Tapi records only go back a few years; Property Tree goes back further

### Step 7 — Terms & Conditions (Varying Terms)

Add a varying term noting the rent increase:

> Rent will be increasing to $[amount] per week from [date]. A rent increase notice has been attached to form part of this agreement.

**Attach the rent increase notice:**

1. Click **"Add a property-specific attachment"**
2. Browse for the saved rent increase notice PDF
3. Select which tenants can view it
4. Set the category to **"Payments"** (most applicable option)
5. Tick the checkbox to include with the agreement
6. **View the attachment** to verify the date matches the TPS renewal details and Property Tree rent schedule

!!! warning "Triple date verification"
    Before sending the renewal for signing, verify that the rent increase effective date matches in all three places:
    
    1. TPS renewal — "Date New Rent Amount Takes Effect"
    2. Property Tree — Rent Schedule effective date
    3. Rent increase notice PDF — effective date shown on the document
    
    All three must be identical.

### Correcting an incorrect attachment

If you need to replace an attachment (e.g., wrong date on the notice):

1. Go to **Properties** tab → select the property → click the **pencil icon**
2. Navigate to **Files**
3. **Delete** the incorrect attachment
4. Re-upload the corrected version via the renewal wizard

!!! info "Cannot delete from within the wizard"
    TPS does not allow deleting attachments from within the renewal wizard. You must use the Properties → Files route.

### Step 8 — Send for Electronic Signing

1. Click **"Email to sign electronically"**
2. Review the email template — the default may say "no changes to rent" which is incorrect if rent is increasing
3. Update the message to mention the rent change
4. Click **Send Email** to send the renewal to tenants for electronic signing

---

## Known TPS Renewal Bugs

| Bug | Workaround |
|---|---|
| Tenant status defaults to "Joining" instead of "Remaining" | Manually change each tenant to "Remaining" in Step 3 |
| General Exemptions toggle re-enables on renewal | Turn it off in Step 6 |
| TPS–PT rent review date API broken | Manually update Property Tree separately |
| Cannot delete attachments from renewal wizard | Use Properties → pencil → Files route |
| E-sign email template defaults to "no changes to rent" | Edit the message before sending |

---

!!! info "What's Next"
    - [Bond Lodgement](bond-lodgement.md) — collect bond and lodge with Tenancy Services
    - [Tenancy Setup](tenancy-setup.md) — complete the full tenancy setup workflow
