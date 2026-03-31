# MASTER INDEX — Property Management Workflow (Version 2 — Full)

**Version:** V2.2 (Updated from 12 video walkthroughs)  
**Last updated:** 2026-03-31  
**Owner:** Property Partner (Strathmore Property Limited)  
**Audience:** Property Manager, Property Management Assistant / VA, Operations Support

---

## 1) What this documentation set covers
This library documents your **end-to-end** NZ property management workflow:

- **Landlord + property onboarding** (new management, takeover, setup)
- **Leasing** (Trade Me → TPS BookMe → applications → checks → approval → agreement)
- **Tenancy setup** (agreement + bond via TPS → Property Tree tenancy record + property file)
- **Compliance (Healthy Homes + related)** (pre-tenancy readiness + ongoing tracking + evidence storage)
- **Tenant onboarding** (welcome pack + ingoing condition report)
- **Inspections** (quarterly routine + ingoing/outgoing, confirmations, follow-ups, escalation)
- **Maintenance** (Tapi: triage, approvals, work orders, invoices, closeout)
- **Renewals + rent reviews** (Valua evidence + TPS renewals/extensions)
- **End of tenancy + lease breaks** (vacate, outgoing, bond, relisting, cost recovery)
- **Notices + comms** (rent increases, breaches, admin notices, recordkeeping)
- **Email management** (VA-owned loop closure; filing into Property Tree)
- **Daily/weekly/monthly QA** (nothing falls through)

**Non‑negotiable:** anything that matters must end up in the **Property Tree property record**.

---

## 2) How to use the library
- **Playbooks (01_)**: lifecycle “what happens + when” (day-to-day process).
- **SOPs (02_)**: exact “how to do it” in each system (click-by-click and field checklists).
- **Templates (03_)**: copy/paste messages + website copy (lease break guide included).
- **QA (04_)**: daily/weekly/monthly controls and hygiene.

**Golden rule:** if it isn’t recorded in Property Tree (or linked into the property record), it didn’t happen.

---

## 3) Systems map (quick)
See: [Systems Map & Data Flow](systems-map.md)

### TPS / Tenancy.co.nz (leasing + agreements + renewals + compliance + apps)
- BookMe viewings (enquiry routing via Trade Me listing ID)
- Tenant portal accounts, applications, checks
- Agreement generation and digital signing
- Renewals/extensions
- Bond workflow integration (you still collect into trust first)

### Trade Me for Rent (marketing channel)
- Listing published on Trade Me
- Trade Me listing number added in TPS to route enquiries → BookMe

### Property Tree (system of record + trust accounting + property file)
- Property/owner/tenant master data, ledgers, tenancy dates
- Inspection scheduling (sync to Inspection Express)
- Weekly disbursements (Monday night run)
- **Document repository** (agreements, compliance evidence, insurance, inspection reports, notices)

### Tapi (maintenance CRM)
- Four intake sources: Concierge (tenant portal), Inspection Express sync, owner requests, phone/email
- Dashboard with status pipeline: Open → Awaiting quotes → Awaiting approval → Scheduling → Awaiting repair → Awaiting invoice → Awaiting confirmation
- Five actions per job: Send work order, Request quotes, Ask owner for approval, Send to owner for DIY, Plan for later
- Approvals: owner gets email with Approve button + message thread; follow-up at Day 3/7
- Invoices: auto-match or manual 3-step match; approve → auto-closes job → syncs to Property Tree

### Inspection Express (inspection execution + reporting)
- Receives inspection schedule from Property Tree
- Reports published to tenant/landlord
- Inspection-captured maintenance syncs into Tapi

### Valua (rent evidence + recommendations)
- Market evidence set and recommended rent range for owners

### Email (hello@ + owner mailbox)
- Exceptions + escalations + “edge cases”
- VA owns loop closure and filing key comms into Property Tree

---

## 4) “Most used” routes (do this, not memory)

### A) Onboard landlord + property
1) Playbook: [Landlord & Property Onboarding](../playbooks/landlord-property-onboarding.md)  
2) SOP: [PropertyTree — Create Owner & Property](../sops/propertytree-create-owner-property.md)  
3) SOP: [TPS Property Setup & Trade Me ID](../sops/tps-property-setup.md)  
4) Playbook: [Compliance & Healthy Homes](../playbooks/compliance-healthy-homes.md) (if gaps)  
5) Checklist: [Checklists](../templates/checklists.md)

### B) Lease a property (end-to-end)
1) Playbook: [Leasing](../playbooks/leasing.md)  
2) SOPs: TPS BookMe + TPS applications + TPS agreement generation  
3) Handover: [Tenancy Setup](../playbooks/tenancy-setup.md)

### C) Maintenance
1) Playbook: [Maintenance (Tapi)](../playbooks/maintenance-tapi.md)  
2) SOP: [Tapi Intake, Triage & Work Orders](../sops/tapi-intake.md)  
3) SOP: [Tapi Invoices & PropertyTree Sync](../sops/tapi-invoices.md)

### D) Inspections
1) Playbook: [Inspections](../playbooks/inspections.md)  
2) SOP: [Inspection Scheduling & Confirmation](../sops/propertytree-inspection-scheduling.md)  
3) SOP: [Inspection Express Reports & Actions](../sops/inspection-express.md)

### E) Renewals + rent reviews
1) Playbook: [Renewals & Rent Reviews](../playbooks/renewals-rent-reviews.md)  
2) SOP: [Valua Rent Research](../sops/valua-rent-research.md)  
3) SOP: [TPS Agreements & Signing](../sops/tps-agreements-signing.md)

### F) End of tenancy / lease break
1) Playbook: [End of Tenancy & Break Lease](../playbooks/end-of-tenancy.md)  
2) Template: [Notices & Emails](../templates/notices-emails.md) (lease break guide + emails)  
3) File everything into Property Tree

---

## 5) Full library map

### START HERE
- [Systems Map & Data Flow](systems-map.md)
- [Standards, SLAs & Approvals](standards-slas.md)

### PLAYBOOKS (Lifecycle)
- [Landlord & Property Onboarding](../playbooks/landlord-property-onboarding.md)
- [Leasing](../playbooks/leasing.md)
- [Tenancy Setup](../playbooks/tenancy-setup.md)
- [Compliance & Healthy Homes](../playbooks/compliance-healthy-homes.md)
- [Tenant Onboarding](../playbooks/tenant-onboarding.md)
- [Inspections](../playbooks/inspections.md)
- [Maintenance (Tapi)](../playbooks/maintenance-tapi.md)
- [Renewals & Rent Reviews](../playbooks/renewals-rent-reviews.md)
- [End of Tenancy & Break Lease](../playbooks/end-of-tenancy.md)
- [Notices & Comms](../playbooks/notices-comms.md)
- [Email & Recordkeeping](../playbooks/email-recordkeeping.md)

### SOPs (How-To)
- [PropertyTree — Create Owner & Property](../sops/propertytree-create-owner-property.md)
- [PropertyTree — Create Tenancy & Dates](../sops/propertytree-create-tenancy-dates.md)
- [Inspection Scheduling & Confirmation](../sops/propertytree-inspection-scheduling.md)
- [TPS Property Setup](../sops/tps-property-setup.md)
- [TPS Viewings & BookMe](../sops/tps-viewings-bookme.md)
- [TPS Application Processing](../sops/tps-application-processing.md)
- [TPS Agreements & Signing](../sops/tps-agreements-signing.md)
- [Bond Lodgement via TPS](../sops/tenancy-services-bond.md)
- [Compliance & Healthy Homes Evidence](../sops/compliance-healthy-homes-evidence.md)
- [Tapi Intake, Triage & Work Orders](../sops/tapi-intake.md)
- [Tapi Invoices & PropertyTree Sync](../sops/tapi-invoices.md)
- [Inspection Express Reports & Actions](../sops/inspection-express.md)
- [Valua Rent Research](../sops/valua-rent-research.md)
- [Email Management & Shared Inbox](../sops/email-management.md)
- [PropertyTree Filing & Naming](../sops/propertytree-filing-naming.md)

### TEMPLATES + QA
- [Notices & Emails](../templates/notices-emails.md)
- [Checklists](../templates/checklists.md)
- [Daily Triage Checklist](../qa/daily-triage.md)
- [Weekly Operations Checklist](../qa/weekly-operations.md)
- [Monthly Compliance Audit](../qa/monthly-compliance.md)
- [Sources & References](../reference/sources.md)

---

## 6) Change control
- Update the **Playbook** first when the process changes.
- Update the **SOP** second (system steps).
- Update **Templates** last (wording).
- Log changes at the top of the doc (version + last updated).
