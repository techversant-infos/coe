# Pinnacle Regional Health System

> A fictional healthcare organization used for consulting practice scenarios.

---

## Overview

**Client:** Pinnacle Regional Health System
**Industry:** Healthcare (HIPAA-regulated)
**Scenario Type:** Multi-facility hospital and clinic network

---

## Why This Scenario

This scenario provides realistic healthcare consulting constraints:

- HIPAA compliance requirements
- Multi-facility operations
- Medical integration complexity (lab, pharmacy, insurance)
- High availability requirements
- Security-first mindset

> **Note:** This is a fictional organization. There is no codebase — use BlogCFC5 for all technical exercises. This scenario is for consulting practice only.

---

## Organization

| Detail | Value |
|--------|-------|
| Hospitals | 3 |
| Clinics | 12 |
| Physicians | 450 |
| Nurses | 1,200 |
| Admin Staff | 300 |
| Annual Revenue | $850M |

---

## Business Context

Pinnacle operates a legacy Patient Management System built in ColdFusion 10 (2012). They are considering modernization options and have engaged your consulting team.

### Key Concerns

1. **HIPAA Compliance** — System was built before current HIPAA requirements
2. **Performance** — Slow page loads during peak hours (Monday mornings)
3. **Mobile** — No mobile support for physicians
4. **Integration** — Manual processes with lab and pharmacy systems
5. **Scalability** — Cannot handle acquisition growth

### Known Constraints

- **Budget:** $150K for assessment, $500K for modernization
- **Timeline:** Assessment in 4 weeks, modernization in 12 months
- **Downtime Tolerance:** Maximum 4 hours planned downtime
- **Staff:** 3 internal CF developers (need training on modern stack)

---

## Role-Play Persona

### CTO: James Morrison

**Background:** IT leader, 15 years at Pinnacle, familiar with legacy systems, cautious about change.

**Talking Points:**
- "We can't afford to break patient care"
- "Our physicians are set in their ways"
- "We've invested so much in this system"
- "What happens to our integrations?"

**Questions to Ask:**
- What would happen if the system went down for 4 hours?
- Which physicians would feel the impact most?
- What's the cost of a security breach?

---

## Discovery Workshop Guide

Use this context for Phase 9 discovery workshop practice.

### Opening

"Thank you for making time today. We're here to understand your situation with the Patient Management System so we can explore the best path forward — whether that's staying with what you have, modernizing, or something in between."

### Key Questions

| Category | Question |
|----------|----------|
| Business | What would happen if you couldn't access patient records for 4 hours? |
| Technical | What integrations are most critical? |
| Users | Which physicians would be hardest to change? |
| Compliance | When was your last HIPAA audit? |
| Future | Where do you see healthcare IT in 5 years? |

### Listen For

- Regulatory pressure
- Competitive threats
- Patient expectations
- Staff satisfaction
- Integration pain points

---

## Assessment Focus Areas

For this scenario, focus your assessment on:

1. **Security** — HIPAA gap analysis
2. **Integration** — Lab and pharmacy connectivity
3. **Performance** — Peak-hour bottlenecks
4. **Compliance** — Audit trail requirements
5. **Mobile** — Physician access needs

---

## Common Objections

| Objection | Response |
|-----------|----------|
| "We can't afford downtime" | "Let's design a migration with zero-downtime deployment" |
| "Our staff won't learn new systems" | "Let's discuss change management — it's as important as technology" |
| "It was expensive last time" | "Let's look at the total cost of ownership, not just upfront cost" |
| "It's working fine now" | "Fine today doesn't mean secure tomorrow. Let's quantify the risk." |

---

## Reference

This scenario is used for consulting practice. The technical codebase for all exercises is [BlogCFC5](./README.md).
