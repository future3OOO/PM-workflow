# Invoice Processing & Property Tree Sync

**Version:** V2.6  
**Last updated:** 2026-04-01

---

## Overview

Invoice processing is the final stage of the maintenance lifecycle. Invoices arrive in Tapi from contractors, get matched to the originating work order, coded, approved, and automatically sync to Property Tree for the Monday night payment run.

---

## 1. Invoice Submission Methods

Contractors submit invoices through one of two channels:

| Method | How it works | Auto-match? |
|---|---|---|
| **Direct upload** | Contractor uploads through the Tapi portal | Yes — most reliable for auto-matching |
| **Email** | Contractor emails to `propertypartner@tapi.co.nz` | Appears on Invoice Dashboard; may need manual matching |

**Tapi reference number requirement:** Contractors are REQUIRED to include the Tapi work order reference number on all invoices. This is what enables auto-matching. When they omit it, the VA must manually match (see Path B below). Consider reminding contractors who repeatedly omit the reference.

### Forwarding invoices sent to the wrong address

Some contractors forget the Tapi email address and send invoices to an older address instead (e.g., `accounts@propertypartner.co.nz`, `mckenzie@propertypartner.co.nz`, or similar). When this happens:

1. **Forward the email** to `propertypartner@tapi.co.nz`
2. **Before forwarding, ensure a PDF is attached.** Tapi requires an actual PDF file — a link alone will not work.
   - If the contractor's invoice email contains only a **link** (no PDF attachment): click the link, download the invoice as a PDF, then attach the downloaded PDF to the forwarding email before sending
   - If the contractor's invoice email already has a PDF attached: forward as-is
3. Once the forwarded email arrives in Tapi, it will appear on the Invoice Dashboard like any other emailed invoice
4. Proceed with the normal matching and approval workflow (Path A or Path B below)

!!! warning "PDF Attachments Only"
    Tapi ingests PDF attachments only. Links to invoice portals, Google Drive, Xero, or similar will not be picked up. Always verify a PDF is physically attached to the email before forwarding.

---

## 2. Invoice Dashboard

- Tapi has a dedicated **Invoice Dashboard** (separate from the Jobs list) showing all incoming invoices
- Each invoice displays as either **matched** or **unmatched**
- VA should check this dashboard **daily** for new invoices

---

## 3. Path A — Auto-Matched Invoice (Happy Path)

When the contractor included the Tapi reference number, the system auto-links the invoice to the correct work order/job.

1. Open the invoice from the Invoice Dashboard
2. Confirm the **auto-match indicator** is visible at the top of the invoice detail view
3. Review the **activity log** — it shows the full timeline:
   - Work order sent → contractor scheduled → confirmed completion → uploaded invoice
4. Proceed to **Invoice Entry** (Section 5 below)

---

## 4. Path B — Unmatched Invoice (Manual Match)

When a contractor omits the Tapi reference number, auto-match fails. Use this 3-step manual process:

### Step 1 — Contractor Lookup

- Search for the contractor name in Tapi (e.g., "GT Property Maintenance")
- Source the name from the invoice header/letterhead

### Step 2 — Property Selection

- Select the correct property from the filtered list
- Source the address from the property reference on the invoice

### Step 3 — Job Selection

- Select the matching open job from the filtered list (e.g., "Repair window frame refit")
- **Quick verify:** match from the invoice description — "Usually you can just tell from the invoice description"
- **Deep verify:** if unsure, click into the job detail to review photos and the activity log

### Step 4 — Attach

- Click **Attach** to finalise the link between invoice and job
- The invoice now behaves identically to an auto-matched invoice

---

## 5. Invoice Entry Screen

Once the invoice is matched (auto or manual), complete the entry fields:

| Field | Description | Options / Notes |
|---|---|---|
| **Charge to** | Who bears the cost | **Property** (default ~95% — owner pays from rent account), **Owner** (rare — direct forward), **Tenancy** (uncommon — requires evidence + comms trail) |
| **Work type** | Category of maintenance | Dropdown. Most common in order: Plumbing > General repairs/maintenance > Electrical > Appliance servicing > Heat pump servicing > Gardening. Others rarely used |
| **Invoice amount** | Dollar value inc. GST | Pre-filled from the uploaded invoice |
| **Matched job** | Linked Tapi job | Auto-populated or manually matched in previous step |

??? info "Charge-to coding rules (expand)"
    ### Charge-to Coding Rules

    | Code | When to use | Notes |
    |---|---|---|
    | **Property** | Default for virtually all invoices (~95%) | Cost deducted from the owner's rent account balance |
    | **Owner** | Rare | Invoice forwarded directly to the owner for their own payment |
    | **Tenancy** | Tenant is responsible | Uncommon — requires documented evidence and a written communication trail before coding |

---

## 6. Send Notifications

### Owner Notification

1. **Tick** the "Notify owner" checkbox — always tick this
2. Add a **personalised message** (optional but recommended):

   **Standard template:**
   > The [work description] at [address] has been completed. Invoice: $[amount].

   **Late invoice template** (work completed >2 weeks before invoice submission):
   > The [work description] at [address] has been completed. Work was completed on [date]. Invoice: $[amount].

3. **Why personalise:** The standard Tapi notification already explains to owners they don't need to pay directly — costs are deducted from their rent account. However, some owners misinterpret the notification as a payment request. A brief personalised message reduces this confusion.

---

## 7. Late Invoice Handling

- Some contractors submit invoices **weeks or months** after work completion (e.g., work done in January, invoice submitted in March)
- When there is a significant gap (>2 weeks) between the work date and invoice submission:
  - Add a note in the owner notification stating when the work was actually done
  - This prevents owner confusion seeing a charge long after the work occurred
- **Known late invoicers:** GT Property Maintenance (specifically called out in training)

---

## 8. Approve

1. Click the **Approve** button
2. Four things happen automatically on approval:
   1. Invoice status changes to **Approved**
   2. The linked Tapi job **auto-closes** (moves to Closed jobs)
   3. Owner notification email is **sent**
   4. Invoice **syncs to Property Tree** automatically

---

## 9. Property Tree Verification

After approving in Tapi, verify the sync in Property Tree:

1. Open **Property Tree**
2. Search for the property
3. Navigate to **Ownership → Financials** tab
4. Verify the invoice appears as an **outstanding line item** (e.g., "$150")
5. Confirm the amount is deducted from the owner's **available balance** (accumulated rent funds)
6. Deduction is processed in the **Monday payment run** (weekly disbursement cycle)

> For full details on how Property Tree holds back rent to cover invoices and when landlords are paid, see **Section 10** below.

---

## 10. Property Tree — Rent Holdback & Invoice Payment

Once an approved invoice syncs from Tapi to Property Tree, the invoice amount is paid out of the **owner's rent account** (the accumulated rent funds held on behalf of the landlord). Property Tree handles this automatically — no manual intervention is required.

### Owner payment rule

The owner always pays the invoice.

- Standard case: code to **Property** and Property Tree pays it from the owner's rent account.
- If the property is vacant or short of funds, the invoice stays against the owner account until enough rent is available.
- If the landlord has agreed to pay directly, keep a clear email or phone-note record.

If a landlord has multiple properties under the same ownership profile, those rent funds operate as one combined owner balance. If properties sit under separate ownership profiles, funds are not shared across them.

### How the holdback works

- Property Tree compares the invoice amount against the current balance in the owner's rent account.
- If sufficient funds exist, the invoice amount is deducted immediately and the remainder is available for the landlord's next payout.
- If the balance is **less than** the invoice amount, Property Tree holds back **all** incoming rent until the full invoice amount has accumulated. Once covered in full, the invoice is paid and any surplus resumes flowing to the landlord.

!!! example "Worked Example — Rent Holdback"
    | Week | Rent received | Held back for invoice | Paid to landlord | Cumulative held |
    |---|---|---|---|---|
    | **Scenario A — $200 invoice, $500 weekly rent, $500 in account** | | | | |
    | Week 1 | $500 already in account | $200 | $300 | $200 (invoice paid) |
    | **Scenario B — $600 invoice, $500 weekly rent, $500 in account** | | | | |
    | Week 1 | $500 already in account | $500 | $0 | $500 |
    | Week 2 | $500 (new rent) | $100 | $400 | $600 (invoice paid) |

### Landlord notification

- Landlords receive a **copy of the invoice** attached to their **landlord statement**.
- Statements are sent out **weekly on Mondays** after all landlord payments have been processed.

### Tenant payment frequency

Most tenants pay weekly, but some pay **fortnightly** or **monthly**. The holdback principle is identical regardless of frequency — however, if a tenant pays fortnightly or monthly then the landlord's payout cycle matches that cadence (landlord is only paid when rent comes in).

---

??? example "End-to-end invoice flow (expand)"
    ## Quick Reference — End-to-End Flow

    ```
    Invoice arrives (upload or email)
            │
            ├─ Auto-matched? ──YES──→ Review activity log → Invoice Entry
            │
            └─ Unmatched? ──────────→ Contractor lookup → Property select → Job select → Attach → Invoice Entry
                                                                                                        │
                                                                                        Set charge-to (Property/Owner/Tenancy)
                                                                                        Set work type
                                                                                        Verify amount
                                                                                                        │
                                                                                        Tick notify owner + add message
                                                                                                        │
                                                                                                  Click Approve
                                                                                                        │
                                                                                  ┌─────────────────────┼─────────────────────┐
                                                                                  │                     │                     │
                                                                            Job auto-closes    Owner notified    Syncs to Property Tree
                                                                                                                              │
                                                                                                                  Rent holdback (auto) — §10
                                                                                                                              │
                                                                                                                  Monday payment run + statement
    ```

---

!!! info "Daily Invoice Processing Checklist"
    - [ ] Check Tapi Invoice Dashboard for new invoices
    - [ ] Process auto-matched invoices (Path A)
    - [ ] Manually match any unmatched invoices (Path B)
    - [ ] Code each invoice (charge-to, work type, amount)
    - [ ] Add personalised owner notification message
    - [ ] Flag late invoices with completion date in notification
    - [ ] Click Approve
    - [ ] Verify sync in Property Tree (Ownership → Financials)

!!! info "What's Next"
    - [Maintenance Lifecycle](maintenance-lifecycle.md) — full end-to-end maintenance process
    - [Daily Triage Checklist](../day-to-day/daily-triage.md) — daily invoice dashboard check
    - [Standards & SLAs](../getting-started/standards-slas.md) — approval thresholds and rules
