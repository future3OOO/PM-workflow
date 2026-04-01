# Maintenance Lifecycle

**Version:** V2.10  
**Last updated:** 2026-04-01

---

## Goal
Handle maintenance quickly and consistently with clean approvals, multi-party comms, correct invoicing, and full sync to Property Tree.

## Trigger
1. **Tenant request via Concierge** — website chatbot portal; arrives as email notification with a "View full request" button linking to Tapi
2. **Inspection-captured item** — synced from Inspection Express into Tapi, tagged "Reported via inspection"
3. **Owner request** — PM or owner creates job manually in Tapi
4. **Landlord email or phone call** — logged manually by PM/VA

## Outputs (definition of done)
- Tenant acknowledged and update time set
- Triage completed with correct priority level assigned
- Owner approvals captured where required
- Contractor engaged (work order, quote request, or DIY referral)
- Invoice approved, coded, and synced to Property Tree
- Owner/tenant notified; job closed and filed

---

## The Tapi Dashboard — Daily Operating View
<span class="pp-verified-label">Verified from video analysis</span>

The Jobs dashboard is the VA's primary workspace. Tabs across the top: **Open | Paused | Closed | All | Planned**.

??? info "Dashboard reference — pipeline, filters, search"

    **Status pipeline (left-to-right progression)**

    Open jobs → Awaiting quotes → Awaiting approval → Scheduling job → Awaiting repair → Awaiting invoice → Awaiting confirmation

    **Filter bar**

    Job agent · Property agent · Priority · Source · Created — slice the queue by ownership or urgency.

    **Search**

    Slide-out panel with free-text search and an "Include archived" checkbox for closed/historical jobs.

    **Property detail page**

    Click a property name → tabs: Jobs | Invoices | Assets | Services | People | Settings.

### Daily routine
- Refresh the dashboard at the start of every shift
- Walk each status bucket: check for stuck jobs, overdue follow-ups, new intake

!!! info "Normal Volume"
    ~200 open jobs is normal — many are recommended (not required) inspection items that owners never respond to.

Full pipeline reference: [Intake, Triage & Work Orders § Status Pipeline](tapi-intake.md#status-pipeline-what-each-stage-means)

---

## Stage 1 — Intake and Acknowledgement

Jobs arrive from four sources. The VA's task is to accept, verify, and clean up each job before triaging.

| Source | Key action |
|---|---|
| Tenant concierge | Click **Accept** → confirm property match → clean up chatbot noise → acknowledge tenant |
| Inspection items | Cross-reference Inspection Express report against Tapi daily; clean descriptions |
| Owner request | Create job via **New job** → Source: Owner → add photos |
| Supplier-reported | Create job → Source: Supplier → link to original job if relevant |

!!! tip "Complete Instructions"
    For the full click-by-click intake process for each source type:
    [Intake, Triage & Work Orders § Intake](tapi-intake.md#intake)

---

## Stage 2 — Triage

Assess urgency and determine the action path.

| Level | SLA | When to use |
|---|---|---|
| Emergency | 24 h | Life/safety — flooding, gas leak, serious electrical |
| Urgent | Act promptly | Hot water outage, power outage, sewerage, significant leak |
| Routine | Standard flow | 90%+ of all jobs |
| Planned | Deferred | Scheduled future work |

??? info "Triage decision framework (expand)"

    | Condition | Action |
    |---|---|
    | Active leak, flooding, no hot water, power out, sewerage, electrical hazard | Send work order immediately (bypass owner approval) |
    | Oven, cooktop, dishwasher, rangehood, heat pump | Fast-track — send for approval immediately or work order if relationship allows |
    | Simple/cheap fix (<$200–300, obvious scope) | Send work order directly — not worth approval overhead |
    | Moderate routine ($300–500, clear scope) | Ask owner for approval, then work order |
    | Expensive or uncertain scope (>$500 or diagnostic needed) | Request quotes first, then present to owner |
    | Safety/compliance (fire doors, smoke alarms) | Inform owner + send work order — cannot wait |
    | Owner will handle it | Send to owner for DIY |
    | Non-urgent, recommended from inspection | Plan for later |

Full decision framework with trade categories: [Intake, Triage & Work Orders § Triage](tapi-intake.md#triage)

---

## Stage 3 — The Five Action Buttons
<span class="pp-verified-label">Verified from video analysis</span>

Every job in Tapi presents five action buttons. Selecting the right one is the core triage decision.

| # | Button | When to use |
|---|---|---|
| 1 | **Send work order** | Straightforward job, known scope, owner approved (or cheap enough to proceed) |
| 2 | **Request quotes** | Cost likely >$500 or scope uncertain |
| 3 | **Ask owner for approval** | Default for routine items |
| 4 | **Send to owner for DIY** | Owner arranges their own contractor |
| 5 | **Plan for later** | Non-urgent, deferred |

### Approval flow (summary)

1. **Check email first** — the inspection report may already have the owner's approval
2. In **Open jobs**, use the **Created** sort/filter to surface the newest **Choose action** jobs waiting for triage
3. Send Tapi approval request with a structured message (issue, risk, recommendation, cost estimate)
4. Dictation / voice-to-text is acceptable for speed, but clean any stray words before sending
5. Owner responds via Approve button (auto-updates) or message thread (VA manually approves via ⋮ menu)
6. Follow-up: Day 0 → Day 3 (business days) → Day 7 escalate to PM

??? info "Approval message template"

    > Hi [Owner first name],
    >
    > These items were noted during the routine inspection at [address]. Are you happy for me to arrange a contractor to attend to them?
    >
    > Kind regards,
    > [PM / VA name]

!!! tip "Complete Instructions"
    Full approval flow, owner response paths, follow-up protocol, declined items closure:
    [Intake, Triage & Work Orders § Approvals](tapi-intake.md#approvals)

    Quoting flow, DIY handoff, and merging related jobs:
    [Intake, Triage & Work Orders § Work Order / Quote / DIY](tapi-intake.md#work-order-quote-request-diy-choosing-the-right-action)

---

## Stage 4 — Contractor Engagement

??? info "Work order fields reference (expand)"

    | Field | Guidance |
    |---|---|
    | Select supplier | Choose based on trade category and preferred contractor list |
    | Compliance documents | Require for electrical / plumbing / gas; skip for handyman |
    | Cost limit (inc. GST) | Set per owner approval or PM guidance |
    | Require contractor to contact tenants | Almost always **yes** |
    | Message to supplier | Brief, clear instruction of what is needed |
    | Send reminder after | Default 3 days |
    | Copy to owner | Default yes |
    | Message to owner | Brief context |
    | Copy to tenant | Tick |
    | Message to tenant | Include specifics — tenants only see the job title, not the full description |
    | Health & safety hazards | Trip · Slip · Electrical · **Dogs (#1 hazard)** · Steep access · Asbestos · Working at height |

### "Call contractor first" for urgent jobs

When same-day attendance is needed:

1. **Phone** the contractor first to confirm availability
2. Then send the Tapi work order as the formal record — supplier message starts with *"As discussed…"*
3. Include manual tenant contact details in the message if not updated in Tapi

### Multi-trade job coordination
Some jobs need sequential trades (e.g. plumber → electrician). Create a **separate Tapi job** for each trade's scope.

### Contractor acceptance
- Usually within 1–2 days. If not, send a follow-up.
- Work is typically completed within 2 weeks.

Full work order panel reference: [Intake, Triage & Work Orders § Sending a Work Order](tapi-intake.md#sending-a-work-order-complete-panel-fields)

---

## Stage 5 — Mid-Job Updates

When a contractor calls back reporting a larger issue:

1. Take notes during the call
2. Update the owner via email (Shortwave AI can draft a professional message)
3. **Keep owners informed before a large invoice arrives — no surprises**

!!! warning "Scope Changes"
    Never let an owner receive an invoice significantly larger than what was approved without prior communication.

Two communication channels:

- **Email reply** — quick but not tracked in Tapi
- **Tapi "Send a message"** — tracked in the job timeline (preferred for audit trail)

---

## Stage 6 — Invoices and Sync to Property Tree

This is a critical stage with its own detailed SOP. The summary:

| Step | Action |
|---|---|
| Invoice arrives | Contractor uploads via Tapi portal or emails `propertypartner@tapi.co.nz` |
| Matching | Auto-match (Tapi reference number) or manual 3-step match (contractor → property → job) |
| Coding | Charge-to: Property (~95%) / Owner (rare) / Tenancy (system option used when charging the tenant; uncommon except for excess water charges). Set work type. |
| Notification | Always tick owner notification; add personalised message |
| Approve | Triggers: invoice approved → job auto-closes → owner notified → **syncs to Property Tree** |
| Holdback | Standard case: invoice is deducted from the owner's rent account in the Monday payment run. Using the **Tenancy** option means the tenant is being charged. The more common case is an excess water charge; otherwise tenant charging is uncommon and only applies where tenant liability has been established, for example careless or intentional damage. If multiple properties share one ownership profile, available funds are pooled across that profile; separate ownership profiles do not share funds |

??? info "Forwarding invoices sent to the wrong address"

    Some contractors send invoices to older addresses (`accounts@propertypartner.co.nz` etc.). When this happens:

    1. Forward the email to `propertypartner@tapi.co.nz`
    2. Ensure a **PDF is attached** before forwarding (Tapi requires an actual PDF — links won't work)
    3. If the email only has a link: click it, download the PDF, attach it to the forwarding email

!!! tip "Complete Instructions"
    Full invoice matching, coding, approval, Property Tree sync, and rent holdback mechanics:
    [Invoice Processing & Property Tree Sync](tapi-invoices.md)

---

## Stage 7 — Close-out

| Scenario | How to close |
|---|---|
| Invoice approved | Job auto-closes on approval |
| Owner declined / ignored | Close via More options → Close job; add summary + audit notes first |
| DIY completed | Close via More options → Close job; note owner's arrangement |

- File key artifacts to Property Tree
- Notify owner of invoice plan (paid from next rent funds or held if insufficient balance)

Declined item closure process: [Intake, Triage & Work Orders § Owner-Declined Maintenance](tapi-intake.md#owner-declined-maintenance-closure-flow)

---

## SOP References

<div class="grid cards" markdown>

-   :material-clipboard-text:{ .lg .middle } **[Intake, Triage & Work Orders](tapi-intake.md)**

    ---

    Click-by-click for intake, triage, approvals, work orders, quotes, DIY, merging, follow-ups, and daily checklist.

-   :material-receipt:{ .lg .middle } **[Invoice Processing & Property Tree Sync](tapi-invoices.md)**

    ---

    Invoice matching, coding, approval, Property Tree sync, rent holdback mechanics, and daily invoice checklist.

-   :material-clipboard-check:{ .lg .middle } **[Inspection Express Reports](../inspections/inspection-express.md)**

    ---

    Inspection report publish, daily review, and action sync into Tapi.

-   :material-calendar-check:{ .lg .middle } **[Daily Triage Checklist](../day-to-day/daily-triage.md)**

    ---

    Walk every Tapi pipeline bucket daily.

</div>
