---
name: Property Partner Platform Architecture
overview: Full architecture blueprint for the Property Partner workflow management platform -- a self-hosted Next.js + FastAPI system integrating Property Tree, Valua, and the existing templates module with new capabilities for lease tracking, automated rent reviews, compliance management, and inspection scheduling with tenant self-service.
todos:
  - id: phase1-skeleton
    content: "Phase 1: Project skeleton -- Docker Compose, FastAPI, Next.js, PostgreSQL, auth"
    status: pending
  - id: phase1-pt-sync
    content: "Phase 1: Property Tree API adapter and initial full sync implementation"
    status: pending
    dependencies:
      - phase1-skeleton
  - id: phase1-property-views
    content: "Phase 1: Property and tenancy list/detail views in dashboard"
    status: pending
    dependencies:
      - phase1-pt-sync
  - id: phase2-lease-tracking
    content: "Phase 2: Lease expiry tracking pipeline and dashboard"
    status: pending
    dependencies:
      - phase1-property-views
  - id: phase2-valua-rent-review
    content: "Phase 2: Valua integration + automated rent review report pipeline"
    status: pending
    dependencies:
      - phase2-lease-tracking
  - id: phase2-templates-email
    content: "Phase 2: Templates module integration + email service for notice sending"
    status: pending
    dependencies:
      - phase2-valua-rent-review
  - id: phase3-calendar
    content: "Phase 3: Master calendar configuration and inspection scheduling engine"
    status: pending
    dependencies:
      - phase2-templates-email
  - id: phase3-tenant-confirm
    content: "Phase 3: Tenant confirmation flow (email link + calendar picker page)"
    status: pending
    dependencies:
      - phase3-calendar
  - id: phase3-inspection-sync
    content: "Phase 3: Bi-directional inspection status sync to Property Tree"
    status: pending
    dependencies:
      - phase3-tenant-confirm
  - id: phase4-compliance
    content: "Phase 4: Compliance manager (Healthy Homes) + document upload/storage"
    status: pending
    dependencies:
      - phase3-inspection-sync
  - id: phase5-automation-qa
    content: "Phase 5: Celery scheduled jobs, KPI dashboard, end-to-end testing, backups"
    status: pending
    dependencies:
      - phase4-compliance
---

# Property Partner Workflow Management Platform -- Architecture Blueprint

---

## 1. System Context and Integration Landscape

The platform sits at the centre of your existing ecosystem, acting as a **workflow orchestration layer** that connects all existing systems into a single operational surface.

```mermaid
graph TB
    subgraph externalSystems [External Systems]
        PT["Property Tree\n(System of Record)"]
        Valua["Valua\n(Rent Predictions API)"]
        TplModule["Templates Module\n(Existing Next.js App)"]
        IE["Inspection Express"]
    end

    subgraph platform [Property Partner Platform]
        Frontend["Next.js Frontend\n(Dashboard + Tenant Portal)"]
        Backend["FastAPI Backend\n(Python)"]
        DB["PostgreSQL Database"]
        Queue["Redis + Celery\n(Task Queue)"]
        FileStore["Local File Storage\n(Documents/Uploads)"]
    end

    subgraph emailLayer [Communication Layer]
        SMTP["SMTP / Transactional Email\n(e.g. Resend, Postmark, or self-hosted)"]
    end

    subgraph tenantAccess [Tenant-Facing]
        TenantEmail["Email Confirm Links"]
        TenantPortal["Calendar Picker Page"]
    end

    PT <-->|"REST API\nbi-directional sync"| Backend
    Valua -->|"REST API\nrent predictions"| Backend
    TplModule <-->|"Internal API\ntemplate rendering"| Backend
    IE <-->|"via Property Tree sync"| PT

    Backend --> DB
    Backend --> Queue
    Backend --> FileStore
    Backend --> SMTP
    Frontend --> Backend

    SMTP --> TenantEmail
    SMTP --> TenantPortal
    TenantEmail -->|"token-based confirm"| Backend
    TenantPortal -->|"slot selection"| Backend
```

---

## 2. Tech Stack

| Layer | Technology | Rationale |

|---|---|---|

| **Frontend** | Next.js 15 (React) with Tailwind CSS v4 | Modern React framework; SSR for tenant-facing pages; consistent with existing templates module |

| **Backend API** | Python / FastAPI | Async-capable, fast, auto-generated OpenAPI docs, strong typing with Pydantic |

| **Database** | PostgreSQL 16 | Relational data (properties, leases, compliance, inspections); JSONB for flexible metadata |

| **Task Queue** | Redis + Celery | Async jobs: scheduled sync, automated rent review pipeline, email sending, reminder crons |

| **File Storage** | Local disk (with structured directories) | Self-hosted; documents, compliance uploads, reports. Abstracted behind a storage service so you can later move to S3 if needed |

| **Email** | SMTP integration (Postmark, Resend, or self-hosted Mailgun) | Transactional email with delivery tracking, open/click tracking for confirmation links |

| **Auth** | NextAuth.js (frontend) + JWT tokens (API) | Staff login for dashboard; token-based auth for tenant confirmation links |

| **Reverse Proxy** | Nginx | Self-hosted entry point, SSL termination, static file serving |

---

## 3. Core Database Schema (Key Entities)

```mermaid
erDiagram
    Property ||--o{ Tenancy : has
    Property ||--o{ ComplianceRecord : tracks
    Property ||--o{ Inspection : scheduled_for
    Property ||--o{ Document : stores
    Tenancy ||--o{ RentReview : triggers
    Tenancy ||--o{ Notice : receives
    Tenancy }o--|| Tenant : occupied_by
    Tenancy }o--|| Owner : managed_for
    Inspection ||--o{ InspectionSlot : offers
    RentReview ||--o{ ValuaReport : references

    Property {
        int id PK
        string pt_property_id
        string address
        string type
        jsonb metadata
        datetime last_synced
    }

    Tenancy {
        int id PK
        int property_id FK
        int tenant_id FK
        int owner_id FK
        string pt_tenancy_id
        date lease_start
        date lease_end
        string lease_type
        decimal current_rent
        date next_rent_review
        string status
    }

    Tenant {
        int id PK
        string pt_tenant_id
        string name
        string email
        string phone
    }

    Owner {
        int id PK
        string pt_owner_id
        string name
        string email
        string phone
    }

    ComplianceRecord {
        int id PK
        int property_id FK
        string category
        string status
        jsonb details
        datetime last_checked
    }

    Inspection {
        int id PK
        int property_id FK
        int tenancy_id FK
        string type
        datetime proposed_datetime
        datetime confirmed_datetime
        string status
        string pt_inspection_id
        string confirm_token
    }

    InspectionSlot {
        int id PK
        int inspection_id FK
        datetime slot_start
        datetime slot_end
        boolean is_selected
    }

    RentReview {
        int id PK
        int tenancy_id FK
        date review_date
        decimal current_rent
        decimal recommended_rent
        string status
        datetime report_sent_at
    }

    ValuaReport {
        int id PK
        int rent_review_id FK
        jsonb prediction_data
        decimal market_change_pct
        datetime fetched_at
    }

    Notice {
        int id PK
        int tenancy_id FK
        string notice_type
        string recipient_type
        string recipient_email
        string status
        datetime sent_at
        datetime opened_at
        string template_id
    }

    Document {
        int id PK
        int property_id FK
        string category
        string filename
        string file_path
        datetime uploaded_at
    }
```

Key design notes:

- Every record stores the corresponding Property Tree ID (`pt_*_id`) to enable bi-directional sync
- `Notice` tracks full delivery lifecycle: drafted, sent, delivered, opened, failed
- `Inspection` has a `confirm_token` for secure email-based confirmation links
- `ComplianceRecord` uses JSONB `details` for flexible Healthy Homes sub-categories (heating, insulation, ventilation, moisture, draught stopping)

---

## 4. Backend Module Architecture

```mermaid
graph LR
    subgraph api [FastAPI Application]
        Router["API Routers\n/properties\n/tenancies\n/inspections\n/rent-reviews\n/compliance\n/notices\n/documents\n/calendar"]
    end

    subgraph services [Service Layer]
        PTSync["PropertyTree\nSync Service"]
        ValuaSvc["Valua\nIntegration Service"]
        TemplateSvc["Template\nService"]
        EmailSvc["Email\nService"]
        InspectionSvc["Inspection\nScheduling Service"]
        ComplianceSvc["Compliance\nService"]
        RentReviewSvc["Rent Review\nOrchestrator"]
        CalendarSvc["Calendar\nService"]
        NotificationSvc["Notification\nTracker"]
    end

    subgraph integrations [Integration Adapters]
        PTAdapter["Property Tree\nAPI Adapter"]
        ValuaAdapter["Valua\nAPI Adapter"]
        TplAdapter["Templates Module\nAdapter"]
        SMTPAdapter["SMTP\nAdapter"]
    end

    Router --> services
    services --> integrations
```

### 4.1 Property Tree Sync Service

This is the most critical integration. The architecture abstracts the Property Tree API behind an **adapter pattern** so the rest of the system is decoupled from Property Tree's specific API shape.

**Sync strategy:**

- **Initial full sync**: On first connection, pull all properties, owners, tenants, tenancies, and inspection records
- **Incremental sync**: Scheduled Celery job (e.g. every 15 minutes) fetches records modified since last sync using a `last_modified` watermark
- **Write-back sync**: When our platform updates inspection status or scheduling, push changes to Property Tree immediately via API
- **Conflict resolution**: Property Tree remains system of record for financial data (rent ledger, disbursements). Our platform is authoritative for inspection scheduling and notice tracking

**Adapter abstraction** -- if Property Tree's API has gaps, the adapter can be extended to support CSV import/export or manual data entry as a fallback path without changing the rest of the codebase.

### 4.2 Rent Review Orchestrator (Automated Pipeline)

This is the automated workflow that ties Valua predictions to landlord communications:

```mermaid
sequenceDiagram
    participant Cron as Celery Scheduler
    participant RR as RentReview Service
    participant DB as Database
    participant VA as Valua API
    participant TPL as Templates Module
    participant Email as Email Service
    participant PT as Property Tree

    Cron->>DB: Query tenancies with rent review due in 90 days
    DB-->>RR: List of upcoming reviews
    loop Each tenancy due for review
        RR->>VA: GET /predict (property_id, last_increase_date)
        VA-->>RR: Market prediction + recommended rent
        RR->>DB: Create RentReview + ValuaReport records
        RR->>TPL: Render rent review report template
        TPL-->>RR: HTML/PDF report
        RR->>Email: Send report to landlord
        Email-->>RR: Delivery confirmation
        RR->>DB: Update Notice record (sent_at, status)
        RR->>PT: Sync rent review note to property record
    end
```

Pipeline runs on a schedule (e.g. daily at 8am). Each step is idempotent -- if a review already has a report sent, it skips. Landlord follow-ups at 42 and 14 days are also scheduled as Celery tasks.

### 4.3 Inspection Scheduling and Calendar

This replaces the current manual Property Tree workflow with a managed calendar system:

**Master Calendar:**

- Admin sets recurring availability slots (e.g. Tuesdays 9am-12pm, Thursdays 1pm-4pm)
- Slots have configurable duration (e.g. 30 min per property)
- System auto-proposes inspection dates based on the quarterly cadence and available slots

**Tenant Confirmation Flow:**

```mermaid
sequenceDiagram
    participant System as Platform
    participant Email as Email Service
    participant Tenant as Tenant
    participant Portal as Calendar Picker Page
    participant DB as Database
    participant PT as Property Tree

    System->>Email: Send inspection notice (10 days out)
    Email->>Tenant: Email with CONFIRM link + RESCHEDULE link

    alt Tenant confirms proposed time
        Tenant->>System: GET /confirm/{token}
        System->>DB: Set inspection status = confirmed
        System->>PT: Sync confirmed datetime to PT
        System->>Email: Send confirmation receipt to tenant
    else Tenant wants different time
        Tenant->>Portal: Click RESCHEDULE link
        Portal->>System: GET /inspections/{id}/available-slots
        System-->>Portal: Available slots from master calendar
        Tenant->>Portal: Select new slot
        Portal->>System: POST /inspections/{id}/reschedule
        System->>DB: Update inspection datetime + status = confirmed
        System->>PT: Sync new datetime to PT
        System->>Email: Send updated confirmation to tenant
    end

    System->>Email: 24hr reminder (day before)
```

Key design points:

- Confirmation links use a signed JWT token (single-use, time-limited) for security
- The calendar picker is a public-facing Next.js page (no login required, token-authenticated)
- All status changes immediately sync to Property Tree
- SMS reminders can be added via a Twilio/Vonage adapter alongside email

---

## 5. Frontend Architecture

```mermaid
graph TB
    subgraph nextApp [Next.js Application]
        subgraph staffDashboard [Staff Dashboard - Auth Required]
            DashHome["Dashboard Home\n(KPIs + Alerts)"]
            PropList["Properties List\n+ Detail View"]
            TenancyMgmt["Tenancy Management\n(Lease Expiry + Rent Reviews)"]
            InspectionMgmt["Inspection Scheduling\n+ Calendar View"]
            ComplianceMgmt["Compliance Manager\n(Healthy Homes)"]
            NoticeMgmt["Notice Tracker\n(Sent/Pending/Overdue)"]
            DocManager["Document Manager\n(Upload + Browse)"]
            ReportBuilder["Reports\n(Rent Review + Inspection)"]
        end

        subgraph tenantPages [Tenant-Facing Pages - Token Auth]
            ConfirmPage["Inspection Confirm\n(one-click)"]
            CalendarPicker["Calendar Slot Picker\n(reschedule)"]
        end
    end
```

### Staff Dashboard Pages

1. **Dashboard Home** -- KPI cards: properties under management, upcoming lease expiries (30/60/90 day), overdue rent reviews, upcoming inspections, compliance gaps. Alert feed for items needing attention.

2. **Properties** -- Filterable/searchable list of all synced properties. Detail view shows: tenancy info, compliance status, inspection history, rent review history, notices sent, documents.

3. **Tenancy Management** -- Pipeline view of lease expiries and rent reviews. Filters by date range, status (not started, in progress, landlord contacted, tenant notified, completed). Bulk actions for triggering rent review workflows.

4. **Inspection Scheduling** -- Calendar view (week/month). Drag-and-drop scheduling onto master calendar slots. Bulk scheduling for quarterly batches. Status indicators (proposed, sent, confirmed, completed).

5. **Compliance Manager** -- Property-by-property compliance checklist (heating, insulation, ventilation, moisture/drainage, draught stopping). Upload evidence documents per category. Status traffic light (compliant, gap identified, remediation in progress).

6. **Notice Tracker** -- Full audit trail of every notice sent: type, recipient, template used, sent date, delivery status, open status. Filterable by property, type, status.

7. **Document Manager** -- Upload, categorize, and browse documents per property. Categories align with Property Tree folder structure (01 Management, 02 Agreements, 03 Compliance, 04 Inspections, etc.).

### Tenant-Facing Pages

- **Inspection Confirm Page**: Token-authenticated landing page. Shows proposed date/time, property address. Single "Confirm" button. Success/already-confirmed states.

- **Calendar Slot Picker**: Token-authenticated. Shows available alternative slots from master calendar. Tenant selects preferred slot. Confirmation shown on success.

---

## 6. Templates Module Integration

The existing Next.js templates module will be integrated as a **service dependency** rather than being rebuilt:

- **Approach**: The templates module gets a new API layer (a small set of endpoints) that accepts template ID + merge data, and returns rendered HTML/PDF
- **Email functionality**: The new platform's Email Service handles all sending -- the templates module focuses only on rendering
- **Template types** to wire up: rent increase notice, move-out notice, inspection scheduling notice, inspection reminder, rent review report (landlord), lease expiry notice (tenant), lease expiry notice (landlord)

The templates module remains its own codebase but is deployed alongside the platform and called internally via HTTP.

---

## 7. Deployment Architecture (Self-Hosted)

```mermaid
graph TB
    subgraph server [Self-Hosted Server / VPS]
        Nginx["Nginx\n(Reverse Proxy + SSL)"]

        subgraph docker [Docker Compose Stack]
            NextJS["Next.js Frontend\n(Port 3000)"]
            FastAPIApp["FastAPI Backend\n(Port 8000)"]
            CeleryWorker["Celery Worker\n(Background Jobs)"]
            CeleryBeat["Celery Beat\n(Scheduler)"]
            Redis["Redis\n(Queue + Cache)"]
            Postgres["PostgreSQL 16\n(Port 5432)"]
            TemplatesApp["Templates Module\n(Port 3001)"]
        end

        FileVol["File Storage Volume\n(/data/documents)"]
        DBVol["Database Volume\n(/data/postgres)"]
    end

    Internet["Internet"] --> Nginx
    Nginx --> NextJS
    Nginx --> FastAPIApp
    Nginx -->|"/tenant/*"| NextJS
    NextJS --> FastAPIApp
    FastAPIApp --> Postgres
    FastAPIApp --> Redis
    FastAPIApp --> TemplatesApp
    FastAPIApp --> FileVol
    CeleryWorker --> Postgres
    CeleryWorker --> Redis
    CeleryBeat --> Redis
    Postgres --> DBVol
```

Everything runs in a single Docker Compose stack:

- **Nginx** handles SSL termination, routes `/api/*` to FastAPI, everything else to Next.js
- **Celery Beat** triggers scheduled jobs (Property Tree sync, rent review pipeline, inspection reminders)
- **Celery Worker(s)** execute async tasks (email sending, API calls to Valua/PT, report generation)
- **Volumes** persist database data and uploaded documents across container restarts
- **Backup**: Scheduled `pg_dump` to a backup location; file storage rsync to backup

---

## 8. Scheduled Jobs (Celery Beat)

| Job | Frequency | Description |

|---|---|---|

| `sync_property_tree` | Every 15 min | Incremental sync of properties, tenancies, tenants, owners from PT |

| `scan_lease_expiries` | Daily 7am | Flag tenancies with lease expiry in 90/60/42/14 days; create reminder tasks |

| `run_rent_review_pipeline` | Daily 8am | For tenancies due for rent review: fetch Valua predictions, generate reports, send to landlords |

| `send_inspection_notices` | Daily 8am | Send 10-day scheduling emails for upcoming inspections |

| `send_inspection_reminders` | Daily 8am | Send 24-hour reminders for confirmed inspections |

| `chase_unconfirmed_inspections` | Daily 9am | Follow up on inspections with no tenant confirmation after 2 days |

| `sync_inspection_status_to_pt` | Every 5 min | Push any pending inspection status changes to Property Tree |

| `chase_landlord_renewals` | Daily 9am | Follow up on landlord renewal decisions per escalation cadence (42-day, 14-day) |

---

## 9. Security Considerations

- **Staff auth**: NextAuth.js with credentials provider (email/password) or OAuth (Google Workspace if used). Role-based: Admin, Property Manager, VA.
- **Tenant token auth**: Signed JWT tokens embedded in email links. Single-use for confirmation. Short expiry (7 days). No tenant login required.
- **API security**: All FastAPI endpoints require valid JWT. CORS restricted to frontend origin.
- **File uploads**: Validated file types (PDF, JPG, PNG, DOCX). Max size limits. Stored outside web root.
- **HTTPS**: Nginx with Let's Encrypt certificates.

---

## 10. Project Structure

```
property-partner-platform/
  docker-compose.yml
  nginx/
    nginx.conf
  backend/
    app/
      main.py                    # FastAPI app entry
      config.py                  # Settings (env vars)
      models/                    # SQLAlchemy models
      schemas/                   # Pydantic request/response schemas
      routers/                   # API route handlers
        properties.py
        tenancies.py
        inspections.py
        rent_reviews.py
        compliance.py
        notices.py
        documents.py
        calendar.py
        auth.py
        webhooks.py              # PT callback endpoints
      services/                  # Business logic
        property_tree_sync.py
        valua_integration.py
        template_service.py
        email_service.py
        inspection_scheduler.py
        rent_review_orchestrator.py
        compliance_service.py
        notification_tracker.py
        calendar_service.py
      adapters/                  # External system adapters
        property_tree_adapter.py
        valua_adapter.py
        template_adapter.py
        smtp_adapter.py
      tasks/                     # Celery tasks
        sync_tasks.py
        review_tasks.py
        inspection_tasks.py
        notification_tasks.py
      migrations/                # Alembic migrations
    requirements.txt
    Dockerfile
  frontend/
    src/
      app/                       # Next.js App Router
        (dashboard)/             # Staff dashboard (auth-protected)
          page.tsx               # Dashboard home
          properties/
          tenancies/
          inspections/
          compliance/
          notices/
          documents/
          reports/
        tenant/                  # Tenant-facing (token-auth)
          confirm/[token]/
          reschedule/[token]/
        api/                     # Next.js API routes (auth proxy)
      components/                # Shared UI components
      lib/                       # Utilities, API client
    package.json
    Dockerfile
    tailwind.css                 # Tailwind v4 (CSS-first config)
```

---

## 11. Implementation Phases

### Phase 1 -- Foundation (Weeks 1-3)

Set up the project skeleton: Docker Compose, FastAPI app with database models and migrations, Next.js frontend shell with auth, Property Tree adapter with initial full sync, basic property/tenancy list views.

### Phase 2 -- Lease and Rent Review Tracking (Weeks 4-5)

Lease expiry pipeline, rent review date tracking, Valua API integration, automated rent review report generation, notice sending with templates module integration, notice tracker dashboard.

### Phase 3 -- Inspection Management (Weeks 6-8)

Master calendar configuration, inspection scheduling engine, tenant confirmation flow (email confirm + calendar picker), bi-directional Property Tree sync for inspections, inspection dashboard with calendar view.

### Phase 4 -- Compliance and Documents (Weeks 9-10)

Compliance manager (Healthy Homes categories), document upload/storage/browsing, compliance status dashboard, link compliance records to Property Tree filing structure.

### Phase 5 -- Polish, QA, and Automation (Weeks 11-12)

All Celery scheduled jobs tested and running, full end-to-end workflow testing, dashboard KPIs and alerts, backup strategy deployed, documentation.

---

## 12. Key Risks and Mitigations

| Risk | Impact | Mitigation |

|---|---|---|

| Property Tree API has limited or undocumented endpoints | Cannot sync data automatically | Adapter pattern allows fallback to CSV import or manual data entry; investigate PT API access with MRI Software early |

| Email deliverability issues | Tenant confirmation links not received | Use a reputable transactional email provider (Postmark/Resend); implement delivery status tracking; SMS fallback via Twilio |

| Valua API downtime | Rent review pipeline stalls | Queue-based retry logic; manual override to enter predictions directly |

| Data conflicts between PT and platform | Inconsistent records | Clear ownership rules: PT owns financial data, platform owns scheduling/notices; conflict detection in sync service |