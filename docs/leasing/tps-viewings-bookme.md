# Viewings & BookMe (TPS)

**Version:** V2.4  
**Last updated:** 2026-04-01

---

## Purpose / Outcome
Viewings are created, bookings managed, tenant-in-place access is coordinated, and post-viewing application links are sent — all through the TPS BookMe module integrated with Trade Me.

Part of: [Leasing Lifecycle](leasing-lifecycle.md) → Stage 4

---

## Trade Me → TPS Integration
<span class="pp-verified-label">Verified from video analysis</span>

Before BookMe can receive enquiries, the Trade Me listing must be linked to TPS.

1. List the property on Trade Me with photos, details, and rent
2. Scroll to the bottom of the Trade Me listing and copy the **Listing ID**
3. In TPS, navigate to **Properties → [property] → Property Details**
4. Paste the Listing ID into the **TRADEME ID** field and save

This creates a webhook-like connection — all Trade Me email enquiries are automatically forwarded into TPS Enquiries, and the system sends an automated response to the tenant with a "Make a Booking" link.

!!! warning "Known Trade Me throttling"
    Duplicate enquiries from the same Trade Me account within a short timeframe may not be forwarded to TPS. This appears to be a Trade Me platform limitation.

---

## Creating a Viewing

Navigate to **Book a viewing → Create Viewing** in the TPS sidebar.

### Form fields

| Field | Setting | Notes |
|---|---|---|
| **DATE** | Select from calendar | — |
| **START TIME / END TIME** | Set 15-minute window | 15 minutes is the default for rental viewings (shorter than sales) |
| **VIEWING AGENT** | **McKenzie Lawrence** | When logged in as the VA, the dropdown defaults to your name — always change it to McKenzie Lawrence |
| **LIMIT VIEWING VISITORS BY** | Max Attendees / Max Bookings / Both | One booking can include multiple attendees (couples/groups) |
| **MAX NUMBER OF PEOPLE** | Default 50 | Lower if tenant or owner requests limited access |
| **Special Instructions** | Free text | Use for access instructions, parking restrictions, hard-to-find properties |

!!! warning "Calendar connection matters"
    TPS shows a warning under **VIEWING AGENT** if that agent does not have a calendar connected. If the selected viewing agent has no linked calendar, the calendar event is not sent.

### Current tenant notification

Toggle **AUTO UPDATE CURRENT TENANT → YES** to auto-populate the existing tenant's contact details. Select **EMAIL** as the notification type. The tenant receives a "Viewing Created" email with the date, time, and a note that the PM will arrive 10–15 minutes early.

!!! warning "Always confirm with tenant first"
    Arrange the viewing time with the existing tenant via email, text, or phone **before** scheduling it in BookMe. The auto-update feature is an additional reminder, not the primary notification.

---

## Tenant Booking Experience

When a tenant enquires via Trade Me and viewings are scheduled:

1. Tenant receives an automated email: "Great news, viewing times are available!" with a **Make a Booking** button
2. The booking page at `bookme.tenant.co.nz` shows available time slots and a form: name, email, mobile, number of people attending, comments/questions
3. After booking, the tenant receives a "Booking Successful" confirmation email with viewing details and a cancellation link
4. The confirmation page cross-promotes other available Property Partner listings

!!! info "Tenant portal accounts"
    Tenants must have a **tenant.co.nz** account (TPS tenant-facing portal) to submit rental applications. This is the same platform as TPS.

---

## Confirmation & Reminder SMS

BookMe sends automated SMS messages to all booked viewers:

| Timing | Message | Purpose |
|---|---|---|
| **24 hours before** | Confirmation SMS with link | Viewer clicks to confirm attendance |
| **2 hours before** | Reminder SMS | Reminds of viewing time and address |

- Typical confirmation rate: ~65% (11 of 17 in observed example)
- Some unconfirmed viewers still turn up; others no-show entirely
- TPS charges per SMS sent

!!! tip "Single-booking viewings"
    If only one person is booked, verify the viewing is confirmed before attending. A wasted trip to an empty viewing is avoidable.

---

## Post-Viewing: Sending Application Links

From the **Viewings** page, click the **Send Message** action on a completed viewing.

1. Select **EMAIL** as the message type
2. Select the **Send Tenant Application Url - Email** template
3. Use the filter buttons to select recipients: **Select All Attended** or **Select All Suitable**
4. Review the auto-populated subject and message
5. Click **SEND**

Available viewer filters in the dialog:

- **Select All**
- **Select All Suitable**
- **Select All Not Suitable**
- **Select All Attended**
- **Select All Not Attended**

The PM typically does this from his phone at the viewing itself.

---

## Daily Enquiry Monitoring & Replies

Check the **Book a viewing → Enquiries** page daily.

- Most enquiries are generic, but some tenants include specific questions about the property
- If a specific question requires an answer, either reply in TPS or forward to email
- Replies in TPS are sent to the reply address — currently routes to `hello@propertypartner.co.nz`
- The reply dialog supports **SMS / EMAIL**, template selection, subject editing, and a message editor with merge tags

!!! tip "Email is preferred for responses"
    The TPS reply interface is functional but limited. For detailed responses, use email directly. All enquiry replies route through the hello@propertypartner address.

---

## Viewings Dashboard

The **Viewings** page shows key statistics across the portfolio:

| Metric | Description |
|---|---|
| Today / Tomorrow / This Week | Upcoming viewing counts |
| Cancellations | Viewing cancellations |
| Past Viewings | Historical count |
| Unread Enquiries | Enquiries requiring attention |

Each viewing row shows confirmation status badges: **NOT CONFIRMED**, **VT CONFIRMED** (viewer confirmed), or **S/R CONFIRMED** (sent/received confirmed), along with booking and attendee counts.

---

## Property Overview & Reporting

BookMe also includes two reporting screens that are useful for portfolio-level visibility:

- **Property Overview** — shows each property's upcoming viewings and enquiry counts, with address search and agent filters
- **Owner's Report** — property-level reporting view; access depends on the account being used

These are reference/reporting pages rather than the main daily operating screens.

---

## BookMe Settings Reference

Key settings configured in **Book a viewing → Settings**:

??? info "Current BookMe configuration (expand)"
    | Setting | Status | Value |
    |---|---|---|
    | Send Viewing Confirmation SMS | ON | 24 hours before |
    | Send Reminder SMS (Viewers) | ON | 2 hours before |
    | Send Reminder SMS (Agents) | OFF | — |
    | Get Email Notification for New Bookings | ON | — |
    | Get Email Notification for New Enquiries | ON | — |
    | CC Viewing Agent for Current Tenant Notifications | ON | Viewing agent receives a copy of occupant notices |
    | Auto Cancel Viewing (no bookings) | OFF | — |
    | Enable Tenant Feedback | OFF | — |
    | Update Enquiry Prompt | ON | 14 days |
    | **Tenant Portal Contact Details** | **Viewing agent** | Planned change to **Office details** so the VA manages enquiries via hello@propertypartner.co.nz |
    | Remove Viewing | ON | 60 minutes before (stops new bookings) |
    | Max Number of People | 50 | Default; lower per property as needed |

---

## Template Library

BookMe includes 24+ email templates for the full viewing lifecycle. Key templates:

- **Booking Successful Tenant Notify** — confirmation with viewing details and cancellation link
- **Viewing Confirmation To Tenant** — 24h confirmation request with booking management link
- **Viewing Created Occupant Notify** — current tenant notification about upcoming viewing
- **Send Tenant Application Url** — application link sent after viewing
- **Forwarded enquiry auto response** — auto-response when viewings are available or not

Templates use merge tags like `{first_name}`, `{property_address}`, `{book_date}`, `{book_time}`, `{agent_full_name}`, `{viewing_agent_full_name}`, `{viewing_agent_email}`, `{viewing_agent_cell_phone}`, `{application_url}`, and `{special_instructions}`. Edit templates in **Settings → SELECT TEMPLATE TO EDIT**.

---

!!! info "What's Next"
    - [Application Processing (TPS)](tps-application-processing.md) — process applications received after viewings
    - [Leasing Lifecycle](leasing-lifecycle.md) — return to the full leasing workflow
