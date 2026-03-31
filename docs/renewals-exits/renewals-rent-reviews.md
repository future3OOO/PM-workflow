# Renewals & Rent Reviews

**Version:** V2.4  
**Last updated:** 2026-04-01

---

## Goal
Secure owner decisions early, notify tenants promptly, and execute renewals/extensions cleanly with correct records in TPS and Property Tree.

## Trigger
Fixed term end approaching or annual rent review cycle.

## Outputs (definition of done)
- owner decision recorded in writing
- tenant notified and outcome recorded
- TPS renewal/extension executed if applicable
- Property Tree updated (dates/rent) and docs filed
- rent evidence saved (Valua) when used

---

## Cadence (your current structure)
- ~90 days: landlord contacted with renewal options
- aim to notify tenant promptly once landlord direction is received (~80 days target)
- follow-ups ~42 days and ~14 days

!!! warning "Escalation Rule"
    No response after: 2 follow-up emails → 1 phone call attempt → final deadline email.

---

## Stage 1 — Weekly pipeline review
- maintain a "next 120 days" list (VA/PM)
- schedule outreach and follow-ups

See: [Weekly Operations](../day-to-day/weekly-operations.md) for the weekly pipeline review process.

---

## Stage 2 — Rent evidence (Valua) when needed
- run Valua rent research and prepare a short recommendation
- store evidence in Property Tree

SOP: [Valua — Rent Research](valua-rent-research.md)

---

## Stage 3 — Owner consultation and written decision
- present options (renew fixed, periodic, end at expiry)
- capture decision in writing
- if rent change: confirm timing and notice requirements before serving

See: [Notices & Communications](../day-to-day/notices-comms.md) for notice requirements.

---

## Stage 4 — Entering a Rent Increase in Property Tree

Once the owner has agreed to a rent increase amount, enter it into Property Tree **before** sending the formal notice to the tenant. This ensures the system entry isn't forgotten.

### Calculate the effective date

1. The Residential Tenancies Act requires at least **60 days' written notice** for any rent increase
2. Use [timeanddate.com](https://www.timeanddate.com/date/dateadd.html) to calculate 60 days from today
3. The effective date must be the **first rent payment due date after** the 60-day minimum — not the exact 60-day date itself. This aligns with the tenant's existing rent cycle and avoids partial payment amounts.

### Enter into Property Tree

1. Open the tenant's **Tenancy Profile → Lease & Rent** tab
2. Scroll to the **Rent Schedule** section and click the **(+)** button
3. In the **Scheduled Rent Change** dialog:
    - **EFFECTIVE**: use the calendar picker — the **orange-highlighted boxes** show the tenant's rent cycle dates (payment due dates). Select the first orange date that falls after the 60-day minimum.
    - **AMOUNT**: enter the new weekly rent amount
    - **PERIOD**: keep as Weekly (or Fortnightly if applicable)
    - **DAILY RATE**: auto-calculated
4. **Bond Increase** section: legally you can increase the bond up to 4 weeks' rent alongside a rent increase — but in practice this is generally **not enforced** to avoid additional tenant frustration
5. Click **Save**

After saving, the Rent Schedule shows the new row with the effective date, new amount, and percentage increase.

### Automated rent change reminder

Property Tree's **Automated Communications** system sends a "Rent Change Reminder" email to tenants **10 days before** the effective date, reminding them to update their automatic payments.

### Send the formal rent increase notice

After entering the rent schedule, generate and send the formal **Rent Increase Notice** to the tenant. The notice must include:

- Tenant names and property address
- Current rent and new rent amount
- Effective date and percentage increase
- Legislative context (60-day notice under the Residential Tenancies Act 1986)

!!! tip "Enter rent schedule first, notice second"
    Always enter the rent increase into Property Tree's rent schedule first, then send the tenant the formal notice. This order prevents the common mistake of notifying the tenant but forgetting to update the system.

---

## Stage 5 — Tenant comms and execution
- send tenant renewal offer once owner direction confirmed
- track replies; chase per cadence

---

## Stage 6 — Execute in TPS and update Property Tree

### Prerequisites
Before creating a renewal in TPS, confirm you have:

- Written confirmation from **both** the landlord and the tenant agreeing to renew
- The rent increase already entered in Property Tree's rent schedule (Stage 4)
- The formal rent increase notice generated and ready to attach

### TPS Renewal Wizard

1. Navigate to **Properties → [property] → Agreements** tab
2. Click the **three-dot menu (⋮)** on the current agreement
3. Select **Renewal** (use this 90% of the time — it combines Extension and Variation capabilities)

!!! info "Extension vs Variation vs Renewal"
    - **Extension**: renew for the same period with no changes to terms
    - **Variation**: modify specific terms (add a pet, change a condition) without a full renewal
    - **Renewal**: effectively a new tenancy agreement — can change terms, increase rent, and extend the period. Use this by default.

4. Complete the 8-step wizard — see [Agreements & Signing (TPS)](../leasing/tps-agreements-signing.md) for the full click-level walkthrough
5. Verify all dates match across TPS, Property Tree, and the rent increase notice
6. Upload signed renewal documents to Property Tree

SOP: [Agreements & Signing (TPS)](../leasing/tps-agreements-signing.md) — full TPS renewal wizard walkthrough.

---

## Templates used
- landlord renewal email
- tenant renewal offer + reminders
- rent review summary
- rent increase notice (attach formal notice letter)

---

!!! info "What's Next"
    - [Valua — Rent Research](valua-rent-research.md) — get market evidence for the rent review
    - [Agreements & Signing (TPS)](../leasing/tps-agreements-signing.md) — generate the renewal agreement
