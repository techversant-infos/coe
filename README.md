# Techversant Engineering Academy

A standardized engineering reference for Techversant teams, covering learning paths, coding standards, security, AI-assisted development, and career growth.

This repository is maintained by the **Center of Excellence (CoE)**. Use it as the baseline for project onboarding, skill development, code review, and engineering standards.

> **AI can write code. Engineers build systems.** Human review is mandatory for all AI-assisted contributions.

---

## Academy Structure

```text
coe/
|-- 00-engineering-foundations/
|   |-- README.md
|   |-- git-workflow.md
|   |-- ai-usage.md
|   |-- secure-engineering.md
|   |-- communication.md
|   `-- dev-excellence/
|-- 01-software-engineering/
|   |-- README.md
|   `-- web-development/
|       `-- frontend/
|           |-- react/
|           `-- nextjs/
|-- 02-quality-engineering/
|   |-- README.md
|   |-- manual-testing/
|   |-- automation/
|   |   `-- playwright/
|   `-- strategy/
|-- 06-ai-engineering/
|   |-- README.md
|   |-- ai-assisted-development/
|   |-- ai-assisted-testing/
|   `-- prompt-engineering/
|-- learning-levels/
|   |-- foundation.md
|   |-- practitioner.md
|   |-- advanced.md
|   `-- expert.md
|-- general/
|-- git/
|-- audit/
|-- php/
|-- nodejs/
|-- cf/
`-- ai/
```

The academy folders organize learning. The existing stack folders (`php/`, `nodejs/`, `cf/`, `general/`, `audit/`, `git/`, `ai/`) remain the source of truth for standards and reference material.

---

## Quick Start

### New Engineer

1. Start with [Engineering Foundations](./00-engineering-foundations/README.md).
2. Read the [Git workflow](./00-engineering-foundations/git-workflow.md).
3. Complete the [Developer Excellence Curriculum](./00-engineering-foundations/dev-excellence/curriculum.md).
4. Pick your discipline path:
   - [Software Engineering](./01-software-engineering/README.md)
   - [Quality Engineering](./02-quality-engineering/README.md)
   - [AI Engineering](./06-ai-engineering/README.md)

### Web Developer

1. Complete [Developer Excellence](./00-engineering-foundations/dev-excellence/curriculum.md).
2. Use [React](./01-software-engineering/web-development/frontend/react/intermediate.md) as the frontend foundation.
3. Continue to [Next.js](./01-software-engineering/web-development/frontend/nextjs/intermediate.md) for App Router, Server Components, and production frontend delivery.

### QA Engineer

1. Start with [Quality Engineering](./02-quality-engineering/README.md).
2. If you are moving from manual testing to automation, follow [Manual Tester to Automation Engineer](./02-quality-engineering/automation/playwright/manual-to-automation.md).
3. If you already write automation, follow [Automation Engineer to Senior Automation Engineer](./02-quality-engineering/automation/playwright/senior-automation.md).

---

## Standards Reference

| Area | Source of truth |
|---|---|
| Git workflow | [git/Techversant_Git_Workflow.md](./git/Techversant_Git_Workflow.md) |
| AI-assisted development | [general/ai-era-coding-guidelines.md](./general/ai-era-coding-guidelines.md) |
| REST API design | [general/rest-api-best-practices.md](./general/rest-api-best-practices.md) |
| Security review | [audit/security-audit-checklist.md](./audit/security-audit-checklist.md) |
| PHP / Laravel | [php/php-coding-standards.md](./php/php-coding-standards.md), [php/php-best-practices.md](./php/php-best-practices.md) |
| Node.js / TypeScript | [nodejs/nodejs-typescript-best-practices.md](./nodejs/nodejs-typescript-best-practices.md), [nodejs/nodejs-typescript-code-review-checklist.md](./nodejs/nodejs-typescript-code-review-checklist.md) |
| ColdFusion / CFML | [cf/coldfusion-style-guide.md](./cf/coldfusion-style-guide.md), [cf/coldfusion-code-review-checklist.md](./cf/coldfusion-code-review-checklist.md) |

---

## Current Migration Status

The academy structure is being introduced in phases. See [academy-todo.md](./academy-todo.md) for migration status, gaps, and the next cleanup order.

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for how to propose changes, update standards, or report issues.

---

## Document Control

| Document | Version | Owner | Review Cycle |
|---|---|---|---|
| Techversant Engineering Academy | 0.1 | CoE | Quarterly |
| Git Workflow | 1.3 | DevOps Lead | Quarterly |
| REST API Best Practices | 3.0 | CoE | Semi-annual |
| React Learning Path | v0.3 | CoE Web WG | Quarterly |
| Next.js Learning Path | v0.6 | CoE Web WG | Quarterly |
| Developer Excellence Curriculum | v0.1 | CoE Web WG, cross-team | Quarterly |
| Automation Engineer Learning Path | v0.2 draft | CoE QA WG | Quarterly |

---

**Maintained by:** Techversant CoE  
**Last Updated:** June 2026