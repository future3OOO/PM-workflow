# Standards & SLAs

**Version:** V2.3  
**Last updated:** 2026-03-31

---

## Service standards

!!! warning "Golden Rule"
    **Always respond sooner rather than later.** If a full answer will take time, send an acknowledgement with a promised update time.

### Tenants

- **Urgent / essential services** (leaks, no hot water, power, sewerage, security risk, serious electrical hazard): acknowledge and act immediately
- **Priority chattels** (oven/cooktop, dishwasher, rangehood, heat pump): action quickly and keep owner informed
- **Routine maintenance:** acknowledge quickly; set a next-update time; do not let requests idle
- **Lease/admin requests:** respond promptly; if awaiting owner, give tenant a next-update date/time

### Landlords

- Approvals must be easy: "Approve / Decline / Quote first" + short recommendation
- Notify owner when a work order is issued and when invoice is approved for payment
- For urgent items: act immediately and notify owner at the same time

### Contractors

- Work orders must include: scope, access plan, urgency, deadline, work order number, invoice instructions
- Follow-up cadence: urgent same-day chases; routine within 1-2 business days if stalled
- Acceptance timeline: expect contractor to accept within 1-2 days (Tapi auto-sends reminders every 12-24 h). If not accepted in 2 days, send manual follow-up
- Work completion: most routine maintenance within 2 weeks. Some jobs (overseas parts, compliance, building work) may take months
- For urgent/same-day jobs: **phone the contractor first**, then send Tapi work order as formal record
- Invoice requirement: contractors must include the Tapi work order reference number on all invoices for auto-matching

See: [Maintenance Lifecycle](../maintenance/maintenance-lifecycle.md) · [Tapi Intake SOP](../maintenance/tapi-intake.md)

---

## Maintenance approvals policy

### Triage decision framework

!!! tip "Quick Reference — Approval Thresholds"
    - **Under $200-300** (obvious scope): no approval needed — send work order directly
    - **$300-500** (clear scope): owner approval required
    - **Over $500** (or uncertain scope): request quotes first, then present to owner

#### Act immediately (no approval needed)

- Active leak, flooding, no hot water, power outage, sewerage, serious electrical hazard
- Safety/compliance issue (fire doors, smoke alarms)
- **Action:** Send work order immediately. Phone contractor first if same-day needed. Notify owner simultaneously.

#### Fast-track (approval preferred but not blocking)

- Priority chattels broken (oven, cooktop, dishwasher, rangehood, heat pump)
- **Action:** Fast-track approval request or send work order directly if owner relationship allows.

#### Get owner approval first

- Moderate routine item ($300-500, clear scope)
- Non-urgent inspection recommendation
- **Action:** Ask owner for approval in Tapi with personalised message. Follow up at Day 3 (business days), Day 7 escalate.

#### Get quotes first

- Expensive or uncertain scope (over $500 or diagnostic needed)
- **Action:** Request quotes first, then present to owner for decision.

#### Owner DIY

- Owner states they will handle it themselves
- **Action:** Send to owner for DIY in Tapi. Notify all tenants on the lease.

### Approval follow-up cadence

- **Day 0:** Approval request sent via Tapi
- **Day 3 (business days):** If no response, send follow-up message via Tapi job thread
- **Day 7:** If still no response, escalate to PM for phone call or direct email
- Monitor the **Awaiting approval** bucket in Tapi daily

See: [Maintenance Lifecycle — Stage 3](../maintenance/maintenance-lifecycle.md)

### Owner response channels

Owners may respond via:

1. **Tapi Approve button** in the email (auto-updates job status)
2. **Tapi message thread** (VA must manually approve via three-dot menu → Approve)
3. **Email reply** to the PM (check PM inbox; bridge to Tapi by sending work order or adding notes)

### Quote-first guide

If likely over $500, large scope, or uncertainty about work required:

- Request quote first (unless urgent)
- Use the "knowable scope" test: can the contractor estimate without visiting? (e.g. spouting clean = yes, plumbing leak behind a wall = no)
- PM may give a verbal price range first; owner may still want a formal quote

### Owner-declined maintenance

When an owner declines recommended maintenance:

1. Add a note in Tapi summarising the decision
2. Copy the exact owner email text into a second note (audit trail)
3. Close the job via More options → Close job

---

## Communications rules

1. Keep important communication in writing (TPS/Tapi/email)
2. Use the **three-line update**: what happened, what we're doing next, when you'll hear from us again
3. No verbal-only approvals; capture approvals in Tapi or email and file to Property Tree
4. Don't go silent on tenants while waiting on approvals — update them

---

## Routine inspection standards

- Routine inspections are **quarterly** (every 3 months)
- Cadence:
    - ~10 days out: email advising inspection is being scheduled (proposed window)
    - ~9 days out: SMS asking tenant to confirm proposed time
    - **Do not attend unless tenant has confirmed**
    - 24 hours before: final reminder
- Property Tree: update inspection status to **Confirmed** once tenant confirms (manual)

See: [Inspection Lifecycle](../inspections/inspection-lifecycle.md) · [PT Scheduling SOP](../inspections/pt-scheduling.md)

---

## Tenant issues found at inspection

- Minor/one-off cleanliness → photos by deadline or remedy by next inspection
- Careless damage or multiple serious issues → schedule follow-up inspection; consider formal escalation
- Repeat issues → escalate (written warning → formal notice where appropriate)

File evidence (photos/report) into Property Tree.

---

## Renewals structure

Current outreach:

- landlord ~90 days before fixed term end
- tenant notified once landlord direction received (~80 days target)
- follow-ups around 42 days and 14 days

Escalation rule: 2 email chases → 1 phone call attempt → final deadline email.

See: [Renewals & Rent Reviews](../renewals-exits/renewals-rent-reviews.md)

---

## Recordkeeping non-negotiables

!!! warning "Non-Negotiable"
    Every tenancy file in Property Tree must contain:

    - Signed agreement + any renewals/extensions
    - Bond confirmation + any bond refund documents
    - Healthy Homes evidence set / statement info
    - Inspection reports
    - Major notices
    - Major maintenance approvals + invoices + completion evidence

---

!!! info "What's Next"
    - [Systems Overview](systems-map.md) — source-of-truth rules and data flow for every system
    - [Maintenance Lifecycle](../maintenance/maintenance-lifecycle.md) — the workflow with the most approval and SLA rules
