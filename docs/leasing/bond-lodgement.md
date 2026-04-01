# Bond Lodgement

**Version:** V2.7  
**Last updated:** 2026-04-01

---

## Purpose / Outcome
Bond is collected into trust first, then lodged with Tenancy Services via TPS workflow, with confirmation filed into Property Tree.

Part of: [Leasing Lifecycle](leasing-lifecycle.md) → Stage 6 (bond)

## Steps
<span class="pp-verified-label">Verified from video analysis</span>

### 1) Confirm the bond has actually been received

Navigate to:

- **Property Tree → Accounting → Bond or Deposit Authority**, or
- **Property Tree tenancy → Financials → Recent Transactions**

Check that the bond funds have actually been received before touching the TPS lodgement action.

### 2) Open the bond record in TPS

Navigate to: **TPS → Bonds → open incomplete bond → Edit**

- Review the bond lodgement details
- If the tenant/property details are incomplete, fix them before lodging

### 3) Mark the bond as fully received

- Enter the **Received General Bond** amount manually if it has not auto-filled
- Set **Received Status** to **Fully Paid**
- Save

!!! warning "Do not assume TPS has populated the received amount"
    The video shows that TPS can hold the general bond amount but still require the `Received General Bond` field to be manually completed before the record becomes ready.

### 4) Resolve any validation errors

- If TPS still does not move the bond to `Ready`, check for missing form fields such as postcode or other required bond details

### 5) Lodge the bond in TPS

Navigate to: **TPS → Bonds → three-dot menu → Lodge bond**

- Leave **Payment Method** as **Direct Credit**
- Do not alter the generated references
- Click **Lodge**

### 6) Pay Tenancy Services from the trust account

- Lodging in TPS sends the bond request to Tenancy Services
- It does **not** itself move the trust money
- Tenancy Services then emails back a payment-instruction email with the payment reference and bank account details
- Use that payment-instruction email to make the actual payment from the trust account

### 7) File the confirmation

- Track through to the later Tenancy Services bond lodgement confirmation / receipt email
- Upload the confirmation into Property Tree docs
- Store the email in the relevant labelled email folder for that property
- Update any internal bond status notes

## Timeframe

!!! warning "Statutory deadline"
    If tenant pays bond to landlord/agent, it **must be lodged within 23 working days** of receiving it. Track this deadline actively.

!!! info "What's Next"
    - [Tenancy Setup](tenancy-setup.md) — complete remaining tenancy setup steps
    - [Tenant Onboarding](tenant-onboarding.md) — send welcome pack and schedule ingoing inspection
