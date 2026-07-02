# Techversant Engineering Academy

The Techversant Engineering Academy organizes CoE learning into disciplines, shared foundations, learning levels, and career progression guidance.

Use this folder for learning paths and growth roadmaps. Use the repository root folders (`general/`, `git/`, `audit/`, `php/`, `nodejs/`, `cf/`, `ai/`) as source-of-truth standards and references.

## AI-Assisted Content Creation

The `.claude/` kit in the repository root provides AI agents and commands for creating and managing academy content:

- **`.claude/README.md`** — Quick-start guide for learning content commands
- **Commands** — `/create-learning-phase`, `/create-exercise`, `/create-assessment`, `/review-learning-phase`, `/update-learning-path-index`
- **Agents** — Learning path architect, coaches (QA, JS, Playwright), curriculum reviewer, repo maintainer
- **Skills & Rules** — Teaching methodologies and quality standards

For the full kit guide, see [`.claude/README.md`](../../.claude/README.md).

## Structure

```text
engineering-academy/
|-- 00-engineering-foundations/
|-- 01-software-engineering/
|-- 02-quality-engineering/
|-- 03-platform-engineering/
|-- 04-architecture/
|-- 05-engineering-leadership/
|-- 06-ai-engineering/
|-- learning-levels/
|-- career-progression/
|-- academy-todo.md
`-- README.md
```

## Disciplines

| Area | Use this for |
|---|---|
| [00. Engineering Foundations](./00-engineering-foundations/README.md) | Universal skills: Git, AI usage, secure engineering, communication, developer excellence |
| [01. Software Engineering](./01-software-engineering/README.md) | Web, mobile, backend, and full-stack engineering paths |
| [02. Quality Engineering](./02-quality-engineering/README.md) | Manual testing, automation, Playwright, QA strategy |
| [03. Platform Engineering](./03-platform-engineering/README.md) | DevOps, cloud, Kubernetes, observability - planned curriculum |
| [04. Architecture](./04-architecture/README.md) | Solution architecture, system design, distributed systems - planned curriculum |
| [05. Engineering Leadership](./05-engineering-leadership/README.md) | Team lead, engineering manager, technical leadership - planned curriculum |
| [06. AI Engineering](./06-ai-engineering/README.md) | AI-assisted development, AI-assisted testing, prompt engineering |

## Guidance Layers

| Layer | Purpose |
|---|---|
| [Learning Levels](./learning-levels/01-foundation.md) | Defines demonstrated competence: Foundation, Practitioner, Advanced, Expert |
| [Career Progression](./career-progression/01-transition-overview.md) | Guides transitions such as Junior to Senior, Senior to Team Lead, and Lead to Architect |
| [Academy TODO](./academy-todo.md) | Tracks migration status, known gaps, and next priorities |

## Recommended Starting Points

- New engineer: [Engineering Foundations](./00-engineering-foundations/README.md)
- Web developer: [React](./01-software-engineering/01-web-development/01-frontend/01-react/01-react-learning-path.md), then [Next.js](./01-software-engineering/01-web-development/01-frontend/02-nextjs/01-nextjs-learning-path.md)
- QA engineer: [Manual Tester to Automation Engineer](./02-quality-engineering/02-automation/playwright/01-manual-to-automation.md)
- Existing automation engineer: [Automation Engineer to Senior Automation Engineer](./02-quality-engineering/02-automation/playwright/02-senior-automation.md)
- Manager or mentor: [Career Progression](./career-progression/01-transition-overview.md)

---

**Maintained by:** Techversant CoE
**Last Updated:** June 2026
