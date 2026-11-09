# Techversant Engineering Academy

**Status:** Active · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

The Techversant Engineering Academy organizes CoE learning into disciplines, shared foundations, learning levels, and career progression guidance.

Use this folder for learning paths and growth roadmaps. The rules the paths teach live outside it, in
[standards](../standards/README.md), [security](../security/README.md) and [ai](../ai/README.md).

## AI-Assisted Content Creation

The `.claude/` kit in the repository root provides AI agents and commands for creating and managing academy content:

- **`.claude/README.md`** — Quick-start guide for learning content commands
- **Commands** — `/create-learning-phase`, `/create-exercise`, `/create-assessment`, `/review-learning-phase`, `/update-learning-path-index`
- **Agents** — Learning path architect, coaches (QA, JS, Playwright), curriculum reviewer, repo maintainer
- **Skills & Rules** — Teaching methodologies and quality standards

For the full kit guide, see [`.claude/README.md`](../.claude/README.md) in the repository root.

## Structure

```text
engineering-academy/
|-- 00-engineering-foundations/
|-- 01-software-engineering/
|-- 02-quality-engineering/
|-- 04-architecture/
|-- 05-engineering-leadership/
|-- 06-ai-engineering/
|-- 07-consulting/
|-- 08-forward-deployed-engineering/
|-- learning-levels/
|-- career-progression/
`-- README.md
```

## Disciplines

| Area | Use this for |
|---|---|
| [00. Engineering Foundations](./00-engineering-foundations/README.md) | Roadmap for every engineer: Git and pull requests, AI tools, clean code, design, APIs, testing, security, code review and communication |
| [01. Software Engineering](./01-software-engineering/README.md) | Back end, front-end and full-stack paths for each stack Techversant delivers, with mobile planned |
| [02. Quality Engineering](./02-quality-engineering/README.md) | Manual testing, automation, Playwright, QA strategy |
| [04. Architecture](./04-architecture/README.md) | Roadmap for senior and lead developers moving into a software architect role: system design, APIs, data, reliability, security, cloud cost, AI and modernization |
| [05. Engineering Leadership](./05-engineering-leadership/README.md) | Team lead, engineering manager, technical leadership - planned curriculum |
| [06. AI Engineering](./06-ai-engineering/README.md) | AI-assisted development, AI-assisted testing, prompt engineering |
| [07. Consulting: ColdFusion](./07-consulting/coldfusion/README.md) | Roadmap for senior ColdFusion consultants: maintaining, assessing, modernizing and migrating CFML applications, and managing clients |
| [08. Forward Deployed Engineering](./08-forward-deployed-engineering/README.md) | Roadmap for engineers who embed with clients and take AI-enabled solutions to production |

## Guidance Layers

| Layer | Purpose |
|---|---|
| [Learning Levels](./learning-levels/01-foundation.md) | Defines demonstrated competence: Foundation, Practitioner, Advanced, Expert |
| [Career Progression](./career-progression/01-transition-overview.md) | Guides role transitions and specialist growth paths, including FDE |

## Recommended Starting Points

- New engineer: [Engineering Foundations](./00-engineering-foundations/README.md)
- Front-end developer: [React and Next.js Developer Roadmap](./01-software-engineering/02-frontend/react-nextjs/README.md)
- QA engineer: [Manual Tester to Automation Engineer](./02-quality-engineering/02-automation/playwright/01-manual-to-automation.md)
- Existing automation engineer: [Automation Engineer to Senior Automation Engineer](./02-quality-engineering/02-automation/playwright/02-senior-automation.md)
- Senior or lead developer moving into architecture: [Software Architect Roadmap](./04-architecture/README.md)
- Manager or mentor: [Career Progression](./career-progression/01-transition-overview.md)
- ColdFusion developer moving into consulting: [Senior ColdFusion Consultant Roadmap](./07-consulting/coldfusion/README.md)
- Senior developer, lead developer, software architect or AI engineer moving into client-embedded delivery: [Forward Deployed Engineer Roadmap](./08-forward-deployed-engineering/README.md)
