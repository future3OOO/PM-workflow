# PLAYBOOK — Maintenance (Tapi-first) (Version 2)

**Version:** V2.2 (Updated from 12 video walkthroughs)  
**Last updated:** 2026-03-31

---

## Goal
Handle maintenance quickly and consistently with clean approvals, multi-party comms, correct invoicing, and full sync to Property Tree.

## Trigger
1. **Tenant request via Concierge** — website chatbot portal; arrives as email notification labelled (Concierge, Maintenance, property tag) with a "View full request" button linking to Tapi
2. **Inspection-captured item** — synced from Inspection Express into Tapi, tagged "Reported via inspection"
3. **Owner request** — PM or owner creates job manually in Tapi (New job form → Source dropdown: Inspection / Tenant / Owner / Supplier / Compliance)
4. **Landlord email or phone call** — logged manually by PM/VA

## Outputs (definition of done)
- Tenant acknowledged and update time set (for tenant-submitted requests)
- Triage completed (urgent vs routine) with correct priority level assigned
- Owner approvals captured where required
- Contractor engaged (work order, quote request, or DIY referral)
- Invoice approved, coded, and synced to Property Tree
- Owner/tenant notified appropriately; job closed and filed

---

## The Tapi Dashboard — Daily Operating View

The Jobs dashboard is the VA's primary workspace. Tabs across the top: **Open | Paused | Closed | All**.

### Status pipeline (left-to-right progression)
Open jobs → Awaiting quotes → Awaiting approval → Scheduling job → Awaiting repair → Awaiting invoice → Awaiting confirmation

### Filter bar
Job agent · Property agent · Priority · Source · Created — use these to slice the queue by ownership or urgency.

### Search
Slide-out panel with free-text search and an "Include archived" checkbox for closed/historical jobs.

### Property detail page
Accessed by clicking a property name. Tabs: **Jobs | Invoices | Assets | Services | People | Settings**.

### Daily routine
- Refresh the dashboard at the start of every shift
- Walk each status bucket: check for stuck jobs, overdue follow-ups, new intake
- ~200 open jobs is normal — many are recommended (not required) inspection items that owners never respond to

---

## Stage 1 — Intake and Acknowledgement

### 1a. Tenant request via Concierge
- Email notification arrives → click "View full request" → opens Tapi
- Click **Accept** in Tapi; confirm property/tenancy match in the modal
- Clean up chatbot noise from the "Additional Info" field (Concierge often captures extraneous text)
- Acknowledge the tenant and set a next-update time

### 1b. Inspection-captured items
- PM creates maintenance items in Inspection Express during the routine inspection
- Items auto-sync into Tapi (tagged "Reported via inspection")
- VA reviews daily in Tapi, cross-referencing against the published inspection report PDF
- See [Inspection Express Report & Actions](../sops/inspection-express.md) for full daily review process

### 1c. Owner request
- PM or owner creates job directly in Tapi via the New Job form
- Source dropdown set to **Owner**

### 1d. Landlord email or phone call
- VA creates job in Tapi manually, sets appropriate source

---

## Stage 2 — Triage

### Priority levels in Tapi
| Level | SLA | When to use |
|---|---|---|
| Emergency | 24 h | Life/safety — flooding, gas leak, serious electrical |
| Urgent | Act promptly | Hot water outage, power outage, sewerage, significant leak |
| Routine | Standard flow | 90%+ of all jobs |
| Planned | Deferred | Scheduled future work |

### Urgent items (act immediately — bypass owner pre-approval)
- Water leaks / flooding risk
- Hot water outage
- Power outage
- Sewerage
- Serious electrical hazard

### Priority chattels (handle quickly, still seek approval if time allows)
- Oven / cooktop
- Dishwasher
- Rangehood
- Heat pump

### Routine
Proceed to Stage 3 (approvals).

### Trade categories in Tapi
Building works · Carpentry · Cleaning · Drapery · Electrical · Exterior · Fencing · Fire protection · General · Grounds · HVAC · Insulation · Joinery · Locksmith · Painting · Pest control · Plumbing · Property management · Rangehood · Roofing · Security · Ventilation · Waterproofing

---

## Stage 3 — Decision: The Five Action Buttons

Every job in Tapi presents five action buttons. Selecting the right one is the core triage decision.

| # | Button | When to use |
|---|---|---|
| 1 | **Send work order** | Straightforward job, known scope, owner approved (or simple/cheap enough to proceed) |
| 2 | **Request quotes** | Cost likely >$500 or scope uncertain — apply the "knowable scope" test |
| 3 | **Ask owner for approval** | Default for routine items; sends via Tapi with personalised message |
| 4 | **Send to owner for DIY** | Owner arranges their own contractor/friend |
| 5 | **Plan for later** | Non-urgent, deferred |

### 3a. Ask owner for approval (standard approval flow)

**Before requesting Tapi approval:** check the PM's email inbox first — the inspection report email already listed the items and the owner may have replied with approval. If already approved, skip straight to Stage 4.

If no prior approval exists, send the Tapi approval request with: issue summary, risk, recommendation, cost estimate or quote-first note, and access plan.

**Template (inspection items):**

> Hi [Owner name],
>
> These items were noted during the routine inspection at [address]. Are you happy for me to arrange a contractor to attend to them?
>
> Kind regards,
> [PM / VA name]

**Owner response — two paths:**
- **Path A:** Owner clicks the Approve button in the email → automatic approval in Tapi
- **Path B:** Owner replies via the message thread → VA must manually approve via the three-dot menu (⋮) → Approve

Three-dot menu options on an approval: **Approve | Decline | Resend email**.

**Follow-up cadence:**
- Day 0 — approval sent
- Day 3 — follow-up via Tapi message thread
- Day 7 — escalate to PM

Monitor the **Awaiting approval** bucket daily.

### 3b. Request quotes

Apply the **"knowable scope" test**: can the contractor estimate without visiting the property? (Spouting clean = yes → send work order; plumbing leak behind a wall = no → request quote.)

- PM may give a verbal price range first; the owner may still want a formal quote
- Attach photos: inspection photos + satellite imagery from Property Guru / Google Maps where useful
- Message to contractor must include the word **"quote"** or **"estimate"** — contractors may assume it's a work order otherwise
- Tenant notification is optional for quotes (include if the contractor may need property access)

### 3c. Send to owner for DIY

- Owner has arranged their own person
- Owner notification: optional (untick if you are already in email correspondence)
- Tenant notification: important — goes to ALL tenants on the lease; include who / when / what / where
- Must still action the job in Tapi to remove it from open jobs — failure to do so causes backlog

### 3d. Owner-declined closure

When an owner declines or ignores an item:
1. Add a summary note (e.g. "Owner doesn't want to service at this time")
2. Add a second note with the exact owner email text (audit trail)
3. Assign notes to the appropriate agent
4. Close via **More options → Close job**

### Merging related jobs
If multiple inspection items at the same property require the same trade:
- Merge them in Tapi (More options → Merge job) before requesting approval or sending a work order
- Update the merged job title to reflect the combined scope
- Clean up the merged description — remove landlord-directed language, keep contractor-relevant detail

---

## Stage 4 — Contractor Engagement

### Work order details panel
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
| Message to tenant | Important — the tenant only sees the job title, not the full description; add specifics here |
| Health & safety hazards | Trip · Slip · Electrical · **Dogs (#1 hazard — can be set as property default)** · Steep access · Asbestos potential/confirmed · Working at height |

### "Call contractor first" for urgent jobs
When same-day attendance is needed:
1. **Phone** the contractor first to confirm availability
2. Then send the Tapi work order as the formal record — supplier message starts with *"As discussed…"*
3. Include manual tenant contact details in the message if not updated in Tapi

### Multi-trade job coordination
Some jobs need sequential trades (e.g. plumber installs water pump → electrician wires it; plumber replaces hot water cylinder → electrician connects):
- Create a **separate Tapi job** for each trade's scope
- Use "call contractor first" for the urgent second trade once the first completes

### Contractor acceptance
- Usually within 1–2 days. If not, send a follow-up.
- Work is typically completed within 2 weeks.

---

## Stage 5 — Mid-Job Updates

### Contractor callback with expanded scope
- Contractor may call back reporting a larger issue than originally scoped
- Take notes during the call
- Update the owner via email (can use Shortwave AI to draft a professional message)
- **Key rule:** keep owners informed when scope expands so they don't receive an unexpected large invoice

### Communication channels
- **Email reply** — quick but not tracked in Tapi
- **Tapi "Send a message"** — tracked in the job timeline (preferred for audit trail)

---

## Stage 6 — Invoices and Sync to Property Tree

### Submission methods
1. Contractor uploads via the Tapi portal
2. Contractor emails to **propertypartner@tapi.co.nz**

### Matching
- **Auto-match:** contractor included the Tapi reference number → invoice attaches automatically
- **Manual match (3-step):** select contractor → select property → select job → Attach

### Charge-to coding
| Code | When | Frequency |
|---|---|---|
| Property | Owner pays from rent account | ~95% of jobs |
| Owner | Direct-forward to owner | Rare |
| Tenancy | Charged to tenant | Uncommon; requires evidence |

### Work type dropdown
Plumbing (most common) · General repairs · Electrical · Appliance servicing · Heat pump servicing · Gardening · others rarely used.

### Owner notification
- Always tick owner notification
- Add a personalised message, especially for owners who misinterpret the notification as a payment request

### Late invoices (>2 week gap)
- Add a note about when the work was actually done for the owner's context

### Approve
Clicking **Approve** triggers four automatic effects:
1. Invoice status changes to **Approved**
2. The linked Tapi job **auto-closes**
3. Owner notification email is **sent** (with the personalised message added above)
4. Invoice **syncs to Property Tree** (Ownership → Financials)

The invoice amount is deducted from the owner's available rent balance in the Monday payment run (see Invoice SOP § 10 for holdback mechanics).

---

## Stage 7 — Close-out

| Scenario | How to close |
|---|---|
| Invoice approved | Job auto-closes on approval |
| Owner declined / ignored | Close via More options → Close job; add summary + audit notes first |
| DIY completed | Close via More options → Close job; note owner's arrangement |

- File key artifacts to Property Tree
- Notify owner of invoice plan (paid from next rent funds or held if insufficient balance)

---

## SOP References

- [Inspection Express Report & Actions](../sops/inspection-express.md) — Inspection report publish, daily review, action sync
- [Tapi Intake, Triage, Approvals & Work Orders](../sops/tapi-intake.md) — Click-by-click for intake, triage, approvals, work orders, quotes, DIY
- [Tapi Invoices & Property Tree Sync](../sops/tapi-invoices.md) — Invoice matching, coding, approval, Property Tree sync
