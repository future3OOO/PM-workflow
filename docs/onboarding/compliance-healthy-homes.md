# Compliance & Healthy Homes

**Version:** V2.4  
**Last updated:** 2026-04-01

---

## Goal
Ensure the property is compliant *before tenancy start* (where required) and remain compliant throughout the tenancy, with evidence stored in Property Tree and compliance fields correctly maintained in TPS for agreement generation.

## Trigger
- New management onboarding
- Pre-leasing readiness
- New tenancy/renewal/extension where compliance statement is required
- Compliance gap identified (missing evidence, incomplete work)

## Outputs (definition of done)
- Compliance evidence set stored in Property Tree docs (03 Compliance folder)
- TPS compliance fields populated enough for agreement and compliance statement
- Remediation actions created in Tapi (quotes/work orders) with approvals tracked
- Ongoing compliance review cadence established (monthly audit or as needed)

---

## Stage 1 — Gather evidence and determine gaps

### Assessment providers

- **Healthy Homes assessment**: HomelyHomes (or similar contractor) conducts the on-site assessment and produces a detailed report covering heating, insulation, ventilation, moisture/drainage, and draught stopping
- **Smoke alarm testing**: SETS (Smoke Alarm Testing Services) manages smoke alarm installation, testing, and certification. Check the SETS portal (`sets.co.nz`) under **My Properties** for service dates and expiry dates.

!!! info "Compliance deadline"
    All rental properties must be Healthy Homes compliant since **1 July 2025**. Any new tenancy or renewal requires a current compliance statement.

### Collect what exists:
- Healthy Homes assessment/report (from HomelyHomes or equivalent)
- Insulation details and evidence
- Heating specs and evidence
- Ventilation/extractor evidence
- Moisture ingress/drainage notes and remediation history
- Draught stopping notes (where relevant)
- Smoke alarm info — check SETS portal for last service date and expiry dates (not technically a Healthy Homes standard but operationally tracked alongside it, required since 2016)

### Document gaps:
- "Missing evidence" vs "Non-compliant / needs work"

Store in Property Tree: **03 Compliance**

---

## Stage 2 — Update TPS compliance section
Populate TPS compliance fields so tenancy agreements and compliance statements can be produced correctly (even if some work is pending, ensure it is recorded accurately).

SOP: [Healthy Homes Evidence (TPS)](compliance-healthy-homes-evidence.md)

---

## Stage 3 — Remediation through Tapi

!!! warning "Cost thresholds"
    For routine work, seek owner approval first. Apply the quote-first guideline for jobs > $500 or uncertain scope.

If work is required:
- create Tapi jobs with photos/notes
- issue work orders and keep tenant/owner informed

Playbook: [Maintenance Lifecycle](../maintenance/maintenance-lifecycle.md)

---

## Stage 4 — Ongoing tracking
- After each compliance job, file completion evidence (invoice + photos + certificate/report) in Property Tree.
- Monthly/quarterly audit: sample properties to ensure compliance evidence exists and TPS compliance fields are accurate.
- At each **renewal**: update the smoke alarm last-check date in TPS from the SETS website or the last routine inspection date. Verify smoke alarm expiry dates are still current.

QA: [Monthly Compliance Audit](../day-to-day/monthly-compliance.md)

!!! info "What's Next"
    - [Healthy Homes Evidence (TPS)](compliance-healthy-homes-evidence.md) — populate TPS compliance fields
    - [Maintenance Lifecycle](../maintenance/maintenance-lifecycle.md) — create remediation jobs in Tapi
    - [TPS — Property & Trade Me Setup](tps-property-setup.md) — verify compliance fields support agreement generation
