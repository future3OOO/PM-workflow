# Systems Overview

**Version:** V2.3  
**Last updated:** 2026-03-31

---

## Source of truth by system

### Property Tree — System of Record

| What | Detail |
|---|---|
| Master records | Property, owner, tenant |
| Financials | Tenancy dates, rent ledger, weekly disbursements (Monday night run) |
| Inspections | Schedule source synced to Inspection Express |
| Documents | Agreements, compliance evidence, insurance, inspection reports, notices, key correspondence |

See workflow: [Onboarding](../onboarding/landlord-property-onboarding.md) · [Leasing](../leasing/leasing-lifecycle.md) · [Inspections](../inspections/inspection-lifecycle.md)

### TPS / Tenancy.co.nz — Leasing Engine

| What | Detail |
|---|---|
| Viewings | BookMe bookings, confirmations, reminders |
| Applications | Tenant portal, TPS checks (background/credit) |
| Agreements | Generation + digital signing |
| Renewals | Extensions workflow |
| Compliance | Agreement readiness section |
| Bonds | Workflow initiation (funds collected into trust first) |

See workflow: [Leasing Lifecycle](../leasing/leasing-lifecycle.md) · [TPS Property Setup](../onboarding/tps-property-setup.md)

### Trade Me — Marketing Channel

- Listing content and public marketing presence
- Enquiry origin (routed into TPS via listing ID)

See workflow: [Leasing Lifecycle](../leasing/leasing-lifecycle.md)

### Tapi — Maintenance CRM

??? info "Full Tapi reference (expand)"

    **Intake channels**

    - Concierge (tenant website portal/chatbot) — description, photos, video
    - Inspection Express sync — items tagged "Reported via inspection"
    - Owner requests — PM or owner creates manually
    - Supplier-reported items

    **Triage**

    - Priority levels: Emergency / Urgent / Routine / Planned
    - 24 trade categories

    **Five actions per job**

    - Send work order · Request quotes · Ask owner for approval · Send to owner for DIY · Plan for later

    **Approvals**

    - Owner receives email with Approve button + message thread
    - Auto-updates or manual approval via three-dot menu

    **Work orders**

    - Multi-party notifications (supplier, owner, tenant)
    - Compliance document tracking, health and safety hazards, auto-reminders

    **Invoices**

    - Auto-match via Tapi reference number or manual 3-step match (contractor, property, job)
    - Coding: Property (~95%), Owner (rare), Tenancy (uncommon, needs evidence)
    - Approve triggers: job auto-closes, owner notified, syncs to Property Tree

    **Pipeline statuses**

    Open jobs → Awaiting quotes → Awaiting approval → Scheduling job → Awaiting repair → Awaiting invoice → Awaiting confirmation

    **Navigation**

    Inbox · New job · New Invoice · Jobs · Invoices · Properties · Suppliers · Services · Owners · Compliance

See workflow: [Maintenance Lifecycle](../maintenance/maintenance-lifecycle.md) · [Tapi Intake SOP](../maintenance/tapi-intake.md) · [Tapi Invoices SOP](../maintenance/tapi-invoices.md)

### Inspection Express — Inspections & Reporting

- Ingoing / routine / outgoing reports and photos
- Inspection-captured maintenance items sync into Tapi

See workflow: [Inspection Lifecycle](../inspections/inspection-lifecycle.md) · [Inspection Express SOP](../inspections/inspection-express.md)

### Valua — Rent Evidence

- Comparable set and rent recommendation rationale

See workflow: [Renewals & Rent Reviews](../renewals-exits/renewals-rent-reviews.md) · [Valua SOP](../renewals-exits/valua-rent-research.md)

### Email (hello@ + owner mailbox)

- Exceptions, escalations, and anything not captured cleanly in TPS/Tapi/Property Tree
- Written confirmations where needed

See: [Email Management](../day-to-day/email-management.md)

---

## Data flows

??? example "Leasing and tenancy creation (7 steps)"

    1. Property and owner created in Property Tree; docs folders created
    2. Property created in TPS; compliance fields populated — [TPS Property Setup](../onboarding/tps-property-setup.md)
    3. Trade Me listing published; listing ID entered into TPS; enquiries route into BookMe
    4. Viewings booked; applicants apply via TPS; checks run; application approved — [Viewings](../leasing/tps-viewings-bookme.md) · [Applications](../leasing/tps-application-processing.md)
    5. Agreement generated and signed in TPS; export final PDF — [Agreements](../leasing/tps-agreements-signing.md)
    6. Bond workflow via TPS; collect into trust first; lodge with Tenancy Services — [Bond Lodgement](../leasing/bond-lodgement.md)
    7. Tenancy created/updated in Property Tree with exact dates and rent — [PT Create Tenancy](../leasing/pt-create-tenancy.md)

    Full workflow: [Leasing Lifecycle](../leasing/leasing-lifecycle.md)

??? example "Inspections (7 steps)"

    1. Inspection scheduled in Property Tree; sync to Inspection Express — [Scheduling SOP](../inspections/pt-scheduling.md)
    2. Tenant confirmations managed; Property Tree status set to Confirmed
    3. Report published; sent to tenant and landlord (link + access code valid 30 days); filed to Property Tree — [Inspection Express SOP](../inspections/inspection-express.md)
    4. PM creates maintenance items in Inspection Express; auto-sync to Tapi as individual jobs
    5. VA reviews Tapi daily: cleans descriptions, merges related jobs, checks PM email for owner responses
    6. Owner approval requested in Tapi (unless already approved via inspection report) — [Maintenance Lifecycle](../maintenance/maintenance-lifecycle.md)
    7. Once approved: work order sent to contractor; job moves to Scheduling

    Full workflow: [Inspection Lifecycle](../inspections/inspection-lifecycle.md)

??? example "Maintenance (7 steps)"

    1. Request arrives via Concierge, Inspection Express, owner, or phone/email
    2. VA triages: assess urgency, assign trade category, determine action path
    3. Five action paths: work order, request quotes, ask owner for approval, DIY, plan for later — [Tapi Intake SOP](../maintenance/tapi-intake.md)
    4. For urgent jobs: phone contractor first, then send Tapi work order as formal record
    5. Multi-trade jobs: create a separate Tapi job for each trade scope
    6. Contractor engagement: work order sent → accepts (1-2 days) → schedules → completes → uploads invoice
    7. Mid-job updates: if scope expands, update owner via email before large invoice arrives

    Full workflow: [Maintenance Lifecycle](../maintenance/maintenance-lifecycle.md)

??? example "Invoices — Tapi to Property Tree (6 steps)"

    1. Contractor submits invoice via Tapi portal or email to propertypartner@tapi.co.nz
    2. Auto-match (Tapi reference number) or manual 3-step match (contractor → property → job)
    3. Code the invoice: Charge-to (Property ~95% / Owner / Tenancy), Work type dropdown
    4. Notify owner (always tick; personalise the message; note late invoices)
    5. Approve → job auto-closes, owner notified, invoice syncs to Property Tree
    6. Verify in Property Tree: Ownership → Financials → deducted in Monday night payment run

    Full SOP: [Invoice Processing & Property Tree Sync](../maintenance/tapi-invoices.md)

---

## Recordkeeping rule

!!! warning "Non-negotiable"
    Everything that would matter in a dispute, audit, sale handover, or tribunal must be stored in **Property Tree docs**:

    - Signed agreements + renewals/extensions/variations
    - Bond confirmation and refund outcomes
    - Healthy Homes evidence set and compliance statement
    - Ingoing/routine/outgoing inspection reports
    - Major notices (rent increase, breach, termination, lease break)
    - Major maintenance approvals, quotes, invoices, completion evidence
    - Any critical email thread (saved as PDF)

---

## Naming and filing

See: [Property Tree Filing & Naming](../onboarding/pt-filing-naming.md)

---

!!! info "What's Next"
    - [Standards & SLAs](standards-slas.md) — response times, approval rules, recordkeeping requirements
    - [Maintenance Lifecycle](../maintenance/maintenance-lifecycle.md) — end-to-end maintenance workflow
    - [Leasing Lifecycle](../leasing/leasing-lifecycle.md) — end-to-end leasing workflow
