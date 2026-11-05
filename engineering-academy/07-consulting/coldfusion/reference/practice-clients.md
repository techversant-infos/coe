# Practice Clients

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

Fictional clients for practicing consulting work. The projects in stages 06 and 10 of the
[Senior ColdFusion Consultant roadmap](../README.md) use them. The companies, people and numbers are invented.

## How to Use

1. Pick a scenario that fits the skill you are practicing.
2. One person plays the consultant; a senior colleague plays the client and uses the stakeholder notes and role-play
   scripts below.
3. Afterwards, score the session with the [evaluation rubric](#evaluation-rubric).

| Scenario | Complexity | Best for | Time |
|----------|-----------|----------|------|
| [BlogCFC5 media client](#scenario-0-blogcfc5-media-client) | Low | Linking your practice app work to a client conversation | 1 hour |
| [Summit Manufacturing](#scenario-1-summit-manufacturing) | Medium | Discovery and assessment | 2 hours |
| [Metro Regional Hospital](#scenario-2-metro-regional-hospital) | High | Regulated data, uptime and security | 3 hours |
| [Coastal Insurance](#scenario-3-coastal-insurance) | High | Security, audit readiness and APIs | 3 hours |
| [Greenfield Logistics](#scenario-4-greenfield-logistics) | Medium | Cloud, scaling and AI opportunities | 2 hours |
| [TechStart E-commerce](#scenario-5-techstart-e-commerce) | Low | A quick win on a small budget | 1 hour |

## Scenario 0: BlogCFC5 Media Client

A mid-sized media company has run its company blog on [BlogCFC5](./practice-app-blogcfc5.md) since 2012. The blog is
slow, has had security concerns, does not work well on phones, and nobody who built it still works there.

| Field | Value |
|-------|-------|
| Client | MediaCorp Inc. |
| Application | BlogCFC5, company blog |
| In use since | 2012 |
| Current issues | Slow pages, security concerns, poor mobile support |
| The client's question | "Should we upgrade, migrate or rebuild?" |

Use your findings from the stage 01–05 projects as the evidence for this conversation.

---

## Scenario 1: Summit Manufacturing

### Overview

| Field | Value |
|-------|-------|
| Company | Summit Manufacturing |
| Industry | Industrial manufacturing |
| Size | 500 employees |
| Location | Midwest US |
| Revenues | $150M/year |

### The Application

**Order Management System (OMS)**

- Built in 2011 on ColdFusion 9
- 120 CFM files, plain CFM with includes
- MSSQL database (45 tables)
- Handles 200-500 orders/day
- Custom authentication (stored in database)
- Integrates with: ERP system (SAP), shipping (FedEx API)

### Business Context

Summit is preparing for rapid growth following a recent acquisition. They need to:

- Scale the order system to handle 3x current volume
- Integrate with the acquired company's systems
- Reduce order processing time (currently 15 minutes/order)
- Improve visibility into order status

### Key Stakeholders

| Role | Name | Notes |
|------|------|-------|
| VP Operations | Sarah Chen | Decision maker |
| IT Director | Marcus Johnson | Technical contact |
| Operations Manager | Lisa Patel | End user champion |
| CFO | Robert Williams | Budget authority |

### Known Pain Points

1. **Performance** — Order lookup takes 30+ seconds during peak hours
2. **Manual steps** — 40% of orders require manual intervention
3. **No mobile** — Field sales can't access the system
4. **Reporting** — Excel exports only, no real-time dashboards

### Budget and Timeline

- Budget: $150,000-$200,000
- Timeline: 6-9 months preferred
- Constraint: System must remain operational during modernization

### Discussion Questions for Practice

**Discovery:**

- "Walk me through how an order is processed today."
- "What does 'manual intervention' mean in practice?"
- "Which customers are most affected by the slowness?"

**Technical:**

- "Walk me through your integration with SAP."
- "How is authentication currently handled?"
- "What's your disaster recovery setup?"

**Business:**

- "What would 'success' look like in 12 months?"
- "What's the cost of slow order processing to the business?"
- "Who else should be involved in this decision?"

---

## Scenario 2: Metro Regional Hospital

### Overview

| Field | Value |
|-------|-------|
| Company | Metro Regional Hospital |
| Industry | Healthcare |
| Size | 2,000 employees |
| Location | Urban, Northeast |
| Type | Non-profit health system |

### The Application

**Patient Management System (PMS)**

- Built in 2008 on ColdFusion 8
- 200+ CFM files, plain CFM with includes
- MSSQL database (60 tables)
- 1,500 concurrent users (clinical staff)
- HIPAA compliance required
- Integrates with: Lab systems (2), Insurance verification (2), Pharmacy

### Business Context

Metro Regional is facing several pressures:

- Merger with another health system (need integration)
- EHR replacement project (PMS must interface with new Epic system)
- Patient satisfaction scores below target
- Security audit findings requiring remediation
- Competitive pressure from outpatient clinics

### Key Stakeholders

| Role | Name | Notes |
|------|------|-------|
| CIO | Dr. Amanda Foster | Strategic leader |
| IT Director | James Morrison | Operational contact |
| Compliance Officer | Nancy Huang | HIPAA focus |
| Chief Medical Officer | Dr. Michael Torres | Clinical champion |

### Known Pain Points

1. **Security** — Last audit found 12 high-severity findings
2. **Performance** — Patient lookup slow during shift changes
3. **Integration** — Lab results take hours to appear
4. **UI** — Not mobile-friendly for rounding physicians
5. **Legacy** — CF8 is past end-of-life

### Budget and Timeline

- Budget: $300,000-$500,000
- Timeline: 12-18 months
- Constraint: HIPAA compliance non-negotiable, must maintain 99.9% uptime

### Healthcare-Specific Questions

- "Walk me through your last HIPAA audit findings."
- "How do you handle PHI in development environments?"
- "What are your business associate agreements?"
- "Walk me through the lab integration architecture."

---

## Scenario 3: Coastal Insurance

### Overview

| Field | Value |
|-------|-------|
| Company | Coastal Insurance Group |
| Industry | Insurance |
| Size | 800 employees |
| Location | Southeast US |
| Revenues | $200M/year |

### The Application

**Policy Management System**

- Built in 2013 on ColdFusion 10
- 80 CFM files, FW/1 framework
- Oracle database (80 tables)
- Handles 10,000 policies
- Complex business rules
- Integrates with: Rating engine, Document management, Payment processor

### Business Context

Coastal Insurance is preparing for an IPO and needs to:

- Modernize technology for audit readiness
- Reduce policy processing time (3 days → same day)
- Enable agent mobile access
- Prepare for API-first architecture (insurtech competition)

### Key Stakeholders

| Role | Name | Notes |
|------|------|-------|
| CTO | David Park | Technology strategy |
| VP Product | Jennifer Adams | Business owner |
| IT Manager | Michael Brown | Technical contact |
| Compliance Director | Susan Garcia | Regulatory focus |

### Known Pain Points

1. **Audit risk** — Legacy code is difficult to audit
2. **Speed** — Policy issuance takes 3+ days
3. **Mobile** — Agents work from paper when in field
4. **API** — No APIs for modern integrations
5. **Technical debt** — Framework is outdated

### Regulatory Context

- State insurance regulations
- SOC 2 Type II audit in 6 months
- State consumer privacy laws for policyholder data

---

## Scenario 4: Greenfield Logistics

### Overview

| Field | Value |
|-------|-------|
| Company | Greenfield Logistics |
| Industry | Logistics/Transportation |
| Size | 150 employees |
| Location | Southwest US |
| Revenues | $40M/year |

### The Application

**Fleet Management System**

- Built in 2016 on ColdFusion 2016
- 50 CFM files, custom MVC
- MSSQL database (25 tables)
- Real-time GPS tracking
- Mobile app (separate)
- Integrates with: GPS vendor, Fuel cards, ELD compliance

### Business Context

Greenfield is growing fast (30% YoY) and needs to:

- Scale infrastructure for 3x growth
- Improve driver dispatch efficiency
- Reduce fuel costs
- Enable real-time customer tracking

### Key Stakeholders

| Role | Name | Notes |
|------|------|-------|
| CEO | Tom Richardson | Founder, hands-on |
| Operations VP | Maria Santos | End user champion |
| IT Lead | Chris Taylor | Solo IT |

### Known Pain Points

1. **Scalability** — System crashes during peak dispatch
2. **Real-time** — GPS updates delayed 15 minutes
3. **Mobile** — Separate mobile app doesn't sync well
4. **Cloud** — On-prem server at HQ is a single point of failure

### Opportunity

- AI for predictive maintenance
- Route optimization
- Customer self-service portal

---

## Scenario 5: TechStart E-commerce

### Overview

| Field | Value |
|-------|-------|
| Company | TechStart Direct |
| Industry | E-commerce (B2C) |
| Size | 50 employees |
| Location | Remote-first |
| Revenues | $5M/year |

### The Application

**E-commerce Platform**

- Built in 2019 on Lucee (migrated from Adobe CF)
- 60 CFM files, FW/1 framework
- MySQL database (30 tables)
- 500-1000 daily orders
- Payment: Stripe integration
- Shipping: EasyPost API

### Business Context

TechStart Direct sells specialty tech accessories. They're growing but facing:

- Platform instability (Lucee crashes)
- Cart abandonment (checkout slow)
- Limited marketing automation
- Competitive pressure on price

### Key Stakeholders

| Role | Name | Notes |
|------|------|-------|
| Founder | Alex Kim | Solo decision maker |
| Operations | Jordan Lee | Day-to-day contact |

### Known Pain Points

1. **Stability** — Lucee crashes 2-3x/week
2. **Performance** — Checkout takes 45+ seconds
3. **Features** — Need subscription/reorder capability
4. **Support** — No dedicated IT

### Opportunity

- Move to stable hosting
- Performance optimization
- Subscription model

---

## Role Play Scripts

### Client: Skeptical Operations VP

> "We've had consultants before. They just gave us a report and left."

**How to respond:**

- "I understand. My goal is to understand your situation deeply first, then recommend practical next steps."
- "What would be more useful than a report in your experience?"

### Client: Budget-Constrained CFO

> "This sounds great, but we only have $50,000."

**How to respond:**

- "Let's understand what we can accomplish in that budget. What's the most pressing issue right now?"
- "We can phase the work to deliver value early. What would you consider a quick win?"

### Client: Technically Savvy IT Director

> "We've already evaluated Lucee and it won't work for us."

**How to respond:**

- "I'd love to understand what led to that conclusion. What specific concerns do you have?"
- "Our experience has found that each situation is unique. What if we looked at this specific constraint together?"

---

## Evaluation Rubric

Assess each practice session:

| Competency | 1 (Needs Work) | 3 (Competent) | 5 (Excellent) |
|------------|----------------|---------------|---------------|
| Discovery questions | Few questions asked | Good coverage | Probing, revealing |
| Listening | Interrupted often | Let client speak | Active listening |
| Documentation | Poor notes | Key points captured | Full capture |
| Technical accuracy | Errors made | Accurate | Confident |
| Business framing | Technical only | Some business focus | Full business value |
| Handling objections | Defensive | Neutral | Turns to advantage |
