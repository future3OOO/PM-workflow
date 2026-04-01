# Scheduling & Confirmation (Property Tree)

**Version:** V2.4  
**Last updated:** 2026-04-01

---

## Purpose / Outcome
Schedule inspections and obtain tenant confirmation properly, with correct sync to Inspection Express.

## Trigger
Quarterly routine inspection due OR ingoing/outgoing inspection required.

---

## Auto-Scheduling Behaviour
<span class="pp-verified-label">Verified from video analysis</span>

When a new tenancy is created in Property Tree, the system **automatically creates a routine inspection 3 months from the tenancy start date**.

!!! warning "Check weekday scheduling"
    Property Tree has no weekday-only scheduling option. The auto-created inspection may fall on a Saturday or Sunday. Always check the date and adjust if needed — routine inspections are never conducted on weekends.

To adjust: open the inspection → click the **pencil icon** → change the date to the nearest weekday (1–2 days either side) → save.

---

## Inspection Status Pipeline
<span class="pp-verified-label">Verified from video analysis</span>

Property Tree uses a 5-stage status pipeline for inspections:

**Tentative → Proposed → Confirmed → Conducted → Closed**

| Status | Tenant communication triggered | Inspection Express sync |
|---|---|---|
| **Tentative** | Sends a "proposing that date" email — can confuse tenants if the date is already agreed | No sync |
| **Proposed** | Sends proposal notification | No sync |
| **Confirmed** | Sends proper confirmation email **the day before** the inspection (**only** when status is Confirmed) | Syncs to Inspection Express |
| **Conducted** | — | — |
| **Closed** | — | — |

!!! warning "Inspection Express sync requirements"
    An inspection only syncs to Inspection Express when it has **Confirmed** status AND a **future date/time**. Both conditions must be met.

---

## Scheduling a Routine Inspection
<span class="pp-verified-label">Verified from video analysis</span>

1. Navigate to **Inspections** tab on the Tenancy Profile (or use the Inspections Summary page)
2. Check whether a **Routine** inspection already exists:
   - for the **first** routine inspection in a tenancy, Property Tree usually auto-creates it 3 months from the tenancy start date
   - if that auto-created routine already exists, **open and edit it** instead of creating a duplicate
3. Only click the **(+)** button to add a new inspection if no suitable routine inspection already exists
4. Set **Inspection Type**: Routine
5. Set **Assign To**: McKenzie Lawrence
6. Set the **Inspection Date** and **time window** (agreed with tenant via email/text)
7. Set **Status**: leave as **Proposed** initially (triggers proposal notification to tenant)
8. Click **Save**
9. Property Tree **automatically** sends the **~10-day** scheduling email and **~9-day** SMS (Automated Communications) — **do not** treat these as manual PM sends; confirm they appear in the **Communications Log**
10. Follow up **non-responders** manually if needed (email/SMS) until the tenant confirms
11. Once the tenant confirms, update status to **Confirmed** (manual). **Until Confirmed:** the tenant **does not** receive the **automatic day-before confirmation email**, the inspection **does not** sync to Inspection Express, and **do not attend** the property for the inspection
12. After **Confirmed**, the tenant receives the **automatic** day-before confirmation email

### Inspections Summary Page

The **Inspections Summary** page provides a portfolio-wide view with filters:

| Filter | Options |
|---|---|
| Portfolio | PM folio selection |
| Date From / To | Date range |
| Property Type | All / Residential |
| Assigned To | Agent dropdown |
| Inspection Type | All / Routine / Ingoing / Outgoing |
| Status | All / Tentative / Proposed / Confirmed / Conducted / Closed |
| Suburb | Text search |

Additional tools: **Bulk Edit**, **Bulk Assign**, **Tags**, column customisation.

---

## Rescheduling an Inspection
<span class="pp-verified-label">Verified from video analysis</span>

When a tenant or PM needs to change an inspection date:

1. Open the inspection from the Inspections Summary or Tenancy Profile
2. Click the **pencil icon** (top right of Inspection Details section)
3. In the **Edit Inspection** dialog:
    - Change **Assign To** if needed
    - Change **Inspection Date** to the new date (based on email correspondence with tenant)
    - Change **Between** start and end times
4. Click **Save**

!!! warning "Status resets to Tentative"
    Editing the inspection date or time **automatically pushes the status back to Tentative**. The system displays a warning: "Editing inspection date or times will push the inspection back to 'Tentative' status." You must immediately click **Update to Confirmed** after saving — otherwise the tenant receives a confusing "proposing" email instead of a proper confirmation.

The Edit Inspection dialog also shows an **"Inspections on [date]"** section listing any other inspections already scheduled for the chosen date, helping avoid double-booking.

---

## Adding an Ingoing Inspection
<span class="pp-verified-label">Verified from video analysis</span>

Ingoing inspections are conducted before a new tenant moves in, while the property is vacant.

1. Navigate to **Tenancy Profile → Inspections** tab
2. Click the **(+)** button
3. Set **Inspection Type**: Ingoing
4. Set **Assign To**: McKenzie Lawrence
5. Set **Inspection Date**: today or near future (a few hours ahead of current time)
6. Set **Between**: a narrow time window (e.g., 12:00 PM – 1:00 PM)
7. Set **Status**: **Confirmed** (select from the status dropdown before saving)
8. Click **Save**

!!! tip "No tenant coordination needed"
    Ingoing inspections don't require any correspondence with the incoming tenant — the property is vacant and hasn't been moved into yet. The only scheduling constraint is the PM's calendar availability. Set the status to Confirmed immediately so it syncs to Inspection Express.

---

## Communications Log
<span class="pp-verified-label">Verified from video analysis</span>

Each inspection in Property Tree maintains a full communications log showing:

- **Category** (e.g., Inspection Notice Reminder)
- **To/From** (tenant name)
- **Subject** of each auto-generated email
- **Reference** (e.g., "Inspection date - Confirmed, 1 Days Before")
- **Delivery status** and **date/time**

Use this log to verify that the tenant has received the correct notifications.

---

## Quality Checks
<span class="pp-verified-label">Verified from video analysis</span>

- **Communications Log** shows Property Tree **automatic** ~10-day email and ~9-day SMS (not assumed manual sends)
- Property Tree status **Confirmed** after tenant confirms (required for day-before auto email, IE sync, and attending)
- Inspection appears in Inspection Express (requires **Confirmed** + future time)
- Tenant confirmation recorded
- Auto-scheduled routine inspections verified to fall on weekdays

---

!!! info "What's Next"
    - [Reports & Actions (Inspection Express)](inspection-express.md) — conduct the inspection and publish
    - [Inspection Lifecycle](inspection-lifecycle.md) — full inspection process overview
