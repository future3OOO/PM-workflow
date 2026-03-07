# Property Management Workflow Documentation

**Owner:** Property Partner (Strathmore Property Limited)  
**Version:** V2.1 (Updated from video walkthrough analysis)  
**Last Updated:** 2026-03-07  
**Audience:** Property Manager, Property Management Assistant / VA, Operations Support

---

## What This Is

This is the complete operational documentation library for Property Partner's end-to-end New Zealand residential property management workflow. It covers every stage of the property management lifecycle, from landlord onboarding through to end of tenancy, with detailed playbooks, step-by-step SOPs, copy-paste templates, and quality assurance checklists.

**Golden rule:** if it isn't recorded in Property Tree (or linked into the property record), it didn't happen.

---

## Systems Covered

| System | Role |
|---|---|
| **Property Tree** | System of record -- property/owner/tenant master data, tenancy dates, rent ledger, inspection scheduling, document repository, trust accounting |
| **TPS / Tenancy.co.nz** | Leasing -- BookMe viewings, applications, checks, agreement generation, renewals, compliance fields, bond workflow |
| **Trade Me for Rent** | Marketing channel -- listing publication, enquiry routing into TPS via listing ID |
| **Tapi (Tarpy)** | Maintenance CRM -- request intake, triage, approvals, work orders, contractor comms, invoices, sync to Property Tree |
| **Inspection Express** | Inspection execution -- receives schedule from Property Tree, report publishing, maintenance item capture syncing to Tapi |
| **Valua** | Rent evidence -- comparable market analysis and recommended rent range for rent reviews |

---

## Document Structure

### How to Read This Library

- **Playbooks (01_)** -- Lifecycle processes: what happens and when. Start here to understand a workflow end to end.
- **SOPs (02_)** -- Step-by-step system instructions: how to do it, click by click, in each platform.
- **Templates (03_)** -- Copy/paste email templates, notices, website copy, and execution checklists.
- **QA (04_)** -- Daily, weekly, and monthly quality control checklists to make sure nothing falls through.

All documentation files live inside the [`workflow/`](workflow/) folder.

### Start Here

| Document | Purpose |
|---|---|
| [`00.1_MASTER_INDEX_WORKFLOW_V2.md`](workflow/00.1_MASTER_INDEX_WORKFLOW_V2.md) | Full index of every document with "most used" quick-start routes |
| [`00.2_SYSTEMS_MAP_DATA_FLOW_V2.md`](workflow/00.2_SYSTEMS_MAP_DATA_FLOW_V2.md) | Source of truth rules per system and end-to-end data flows |
| [`00.3_STANDARDS_SLAS_APPROVALS_RECORDS_V2.md`](workflow/00.3_STANDARDS_SLAS_APPROVALS_RECORDS_V2.md) | SLAs, approval policies, comms rules, recordkeeping requirements |

---

## Full File Index

### Foundation (00.x)

| File | Description |
|---|---|
| [`00.1_MASTER_INDEX_WORKFLOW_V2.md`](workflow/00.1_MASTER_INDEX_WORKFLOW_V2.md) | Master index and quick-start routes for all workflows |
| [`00.2_SYSTEMS_MAP_DATA_FLOW_V2.md`](workflow/00.2_SYSTEMS_MAP_DATA_FLOW_V2.md) | Systems map, source of truth rules, and data flow diagrams |
| [`00.3_STANDARDS_SLAS_APPROVALS_RECORDS_V2.md`](workflow/00.3_STANDARDS_SLAS_APPROVALS_RECORDS_V2.md) | SLAs, comms rules, approval policies, inspection cadence, recordkeeping |

### Playbooks (01_) -- Lifecycle Processes

| File | Description |
|---|---|
| [`01_PLAYBOOK_LANDLORD_PROPERTY_ONBOARDING_V2.md`](workflow/01_PLAYBOOK_LANDLORD_PROPERTY_ONBOARDING_V2.md) | New landlord and property onboarding (intake through go-live) |
| [`01_PLAYBOOK_LEASING_TRADEME_TPS_BOOKME_V2.md`](workflow/01_PLAYBOOK_LEASING_TRADEME_TPS_BOOKME_V2.md) | End-to-end leasing (Trade Me listing through to approved application) |
| [`01_PLAYBOOK_TENANCY_SETUP_TPS_TO_PROPERTYTREE_V2.md`](workflow/01_PLAYBOOK_TENANCY_SETUP_TPS_TO_PROPERTYTREE_V2.md) | Tenancy creation from signed agreement through to Property Tree record |
| [`01_PLAYBOOK_COMPLIANCE_HEALTHY_HOMES_V2.md`](workflow/01_PLAYBOOK_COMPLIANCE_HEALTHY_HOMES_V2.md) | Healthy Homes compliance (evidence gathering, TPS fields, remediation, tracking) |
| [`01_PLAYBOOK_TENANT_ONBOARDING_V2.md`](workflow/01_PLAYBOOK_TENANT_ONBOARDING_V2.md) | Tenant welcome pack, ingoing inspection, first-week check |
| [`01_PLAYBOOK_INSPECTIONS_PROPERTYTREE_TO_INSPECTIONEXPRESS_V2.md`](workflow/01_PLAYBOOK_INSPECTIONS_PROPERTYTREE_TO_INSPECTIONEXPRESS_V2.md) | Inspection lifecycle (scheduling, confirmations, reporting, maintenance capture, VA daily Tapi follow-up) |
| [`01_PLAYBOOK_MAINTENANCE_TAPI_TARPY_V2.md`](workflow/01_PLAYBOOK_MAINTENANCE_TAPI_TARPY_V2.md) | Maintenance lifecycle (intake, triage, approvals, job merging, work orders, invoices, close-out) |
| [`01_PLAYBOOK_RENEWALS_RENT_REVIEWS_VALUA_TPS_V2.md`](workflow/01_PLAYBOOK_RENEWALS_RENT_REVIEWS_VALUA_TPS_V2.md) | Renewals and rent reviews (Valua evidence, owner consultation, TPS execution) |
| [`01_PLAYBOOK_END_OF_TENANCY_BREAK_LEASE_V2.md`](workflow/01_PLAYBOOK_END_OF_TENANCY_BREAK_LEASE_V2.md) | End of tenancy and fixed-term lease breaks |
| [`01_PLAYBOOK_NOTICES_AND_COMMS_V2.md`](workflow/01_PLAYBOOK_NOTICES_AND_COMMS_V2.md) | Notices, escalation ladder, and communications rules |
| [`01_PLAYBOOK_EMAIL_AND_RECORDKEEPING_V2.md`](workflow/01_PLAYBOOK_EMAIL_AND_RECORDKEEPING_V2.md) | Email management, loop closure, and filing to Property Tree |

### SOPs (02_) -- Step-by-Step System Instructions

| File | Description |
|---|---|
| [`02_SOP_PROPERTYTREE_CREATE_OWNER_PROPERTY_V2.md`](workflow/02_SOP_PROPERTYTREE_CREATE_OWNER_PROPERTY_V2.md) | Create owner and property records in Property Tree |
| [`02_SOP_PROPERTYTREE_CREATE_TENANCY_DATES_V2.md`](workflow/02_SOP_PROPERTYTREE_CREATE_TENANCY_DATES_V2.md) | Create tenancy with correct dates and rent in Property Tree |
| [`02_SOP_PROPERTYTREE_INSPECTION_SCHEDULING_CONFIRMATION_V2.md`](workflow/02_SOP_PROPERTYTREE_INSPECTION_SCHEDULING_CONFIRMATION_V2.md) | Schedule inspections and manage tenant confirmations in Property Tree |
| [`02_SOP_PROPERTYTREE_FILING_AND_NAMING_V2.md`](workflow/02_SOP_PROPERTYTREE_FILING_AND_NAMING_V2.md) | Document filing and naming conventions in Property Tree |
| [`02_SOP_TPS_PROPERTY_SETUP_TRADEME_ID_BOOKME_V2.md`](workflow/02_SOP_TPS_PROPERTY_SETUP_TRADEME_ID_BOOKME_V2.md) | TPS property setup with Trade Me listing ID and BookMe |
| [`02_SOP_TPS_VIEWINGS_BOOKME_V2.md`](workflow/02_SOP_TPS_VIEWINGS_BOOKME_V2.md) | BookMe viewing management in TPS |
| [`02_SOP_TPS_APPLICATION_PROCESSING_CHECKS_APPROVAL_V2.md`](workflow/02_SOP_TPS_APPLICATION_PROCESSING_CHECKS_APPROVAL_V2.md) | Application processing, checks, and approval in TPS |
| [`02_SOP_TPS_AGREEMENT_GENERATION_SIGNING_RENEWALS_V2.md`](workflow/02_SOP_TPS_AGREEMENT_GENERATION_SIGNING_RENEWALS_V2.md) | Agreement generation, signing, and renewals in TPS |
| [`02_SOP_TENANCY_SERVICES_BOND_LODGEMENT_VIA_TPS_V2.md`](workflow/02_SOP_TENANCY_SERVICES_BOND_LODGEMENT_VIA_TPS_V2.md) | Bond lodgement workflow via TPS |
| [`02_SOP_COMPLIANCE_HEALTHY_HOMES_EVIDENCE_V2.md`](workflow/02_SOP_COMPLIANCE_HEALTHY_HOMES_EVIDENCE_V2.md) | Healthy Homes evidence gathering and TPS compliance fields |
| [`02_SOP_TAPI_INTAKE_TRIAGE_APPROVALS_WORKORDERS_V2.md`](workflow/02_SOP_TAPI_INTAKE_TRIAGE_APPROVALS_WORKORDERS_V2.md) | Tapi: intake, triage, job merging, owner approvals, follow-up protocol, work orders |
| [`02_SOP_TAPI_INVOICES_OWNER_TENANT_DIY_SYNC_TO_PROPERTYTREE_V2.md`](workflow/02_SOP_TAPI_INVOICES_OWNER_TENANT_DIY_SYNC_TO_PROPERTYTREE_V2.md) | Tapi: invoice matching, coding, and sync to Property Tree |
| [`02_SOP_INSPECTION_EXPRESS_REPORT_PUBLISH_ACTIONS_TO_TAPI_V2.md`](workflow/02_SOP_INSPECTION_EXPRESS_REPORT_PUBLISH_ACTIONS_TO_TAPI_V2.md) | Inspection Express: daily monitoring, report review, Tapi sync verification, approval workflow, work orders |
| [`02_SOP_VALUA_RENT_RESEARCH_V2.md`](workflow/02_SOP_VALUA_RENT_RESEARCH_V2.md) | Valua: rent research and recommendation preparation |
| [`02_SOP_EMAIL_MANAGEMENT_SHARED_INBOX_V2.md`](workflow/02_SOP_EMAIL_MANAGEMENT_SHARED_INBOX_V2.md) | Shared inbox email management and labelling |

### Templates and Checklists (03_)

| File | Description |
|---|---|
| [`03_TEMPLATES_NOTICES_EMAILS_V2.md`](workflow/03_TEMPLATES_NOTICES_EMAILS_V2.md) | All email templates, Tapi message templates, formal notices, and website copy (including lease break guide) |
| [`03_TEMPLATES_CHECKLISTS_V2.md`](workflow/03_TEMPLATES_CHECKLISTS_V2.md) | Execution checklists for onboarding, leasing, tenancy setup, inspections (incl. post-inspection Tapi follow-up), maintenance, renewals, and end of tenancy |

### Quality Assurance (04_)

| File | Description |
|---|---|
| [`04_QA_DAILY_TRIAGE_CHECKLIST_V2.md`](workflow/04_QA_DAILY_TRIAGE_CHECKLIST_V2.md) | Daily triage checklist (maintenance, inspection follow-up in Tapi, leasing, inspections, inbox) |
| [`04_QA_WEEKLY_OPERATIONS_CHECKLIST_V2.md`](workflow/04_QA_WEEKLY_OPERATIONS_CHECKLIST_V2.md) | Weekly operations review checklist |
| [`04_QA_MONTHLY_COMPLIANCE_AUDIT_V2.md`](workflow/04_QA_MONTHLY_COMPLIANCE_AUDIT_V2.md) | Monthly compliance and records audit (sample 10 properties) |

### Reference

| File | Description |
|---|---|
| [`99_SOURCES_NOTE_V2.md`](workflow/99_SOURCES_NOTE_V2.md) | External sources and regulatory references (Tenancy Services, vendor integrations) |

### Video Analysis

| File | Description |
|---|---|
| [`_video_analysis/VIDEO_ANALYSIS_REPORT.md`](_video_analysis/VIDEO_ANALYSIS_REPORT.md) | Gap analysis report from Tapi inspection follow-up training videos (15 gaps identified, 7 automation opportunities) |
| [`_video_analysis/video1_transcript.txt`](_video_analysis/video1_transcript.txt) | Timestamped transcript — Video 1: Tapi inspection follow-up approval workflow (14:55) |
| [`_video_analysis/video2_transcript.txt`](_video_analysis/video2_transcript.txt) | Timestamped transcript — Video 2: Tapi inspection follow-up approval example (6:21) |

---

## Change Control

When a process changes:

1. Update the **Playbook** first (the lifecycle process)
2. Update the **SOP** second (the system steps)
3. Update **Templates** last (the wording)
4. Log changes at the top of the document (version + last updated)
