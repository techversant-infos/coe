# Academy Migration TODO

This file tracks the migration from standalone learning paths to the Techversant Engineering Academy structure.

## Priority Order

1. Keep the academy folder structure and internal links clean.
2. Pilot the completed Software Engineering and Quality Engineering paths.
3. Build missing backend and mobile curricula.
4. Build Platform, Architecture, Leadership, and AI curricula in that order.
5. Remove compatibility copies only after links are migrated and owners approve deletion.

## Current Status

| Area | Status | Rating | Notes |
|---|---|---:|---|
| Academy root navigation | Complete | 9/10 | Root README links to all disciplines and guidance layers |
| Engineering foundations | Complete | 8/10 | Dev Excellence + foundation one-pagers migrated and ordered |
| Software engineering | In progress | 7/10 | React and Next.js pilot-ready; backend/mobile planned |
| Quality engineering | In progress | 8/10 | Manual testing + Playwright split-track pilot-ready; advanced QA add-ons planned |
| Platform engineering | Planned | 2/10 | Scope and missing paths defined; full curricula needed |
| Architecture | Planned | 2/10 | Scope and missing paths defined; full curricula needed |
| Engineering leadership | Planned | 2/10 | Scope and missing paths defined; full curricula needed |
| AI engineering | Planned | 2/10 | Scope and missing paths defined; full curricula needed |
| Learning levels | Complete | 9/10 | All four levels defined and ordered |
| Career progression | Complete | 8/10 | Four ordered transition guides |

## Polish Phase (v1.0) - Done

- Added Level labels (Foundation/Practitioner/Advanced/Expert) to content files.
- Added Next Level links in content file headers where useful.
- Added Guidance Layers section to discipline READMEs.
- Prefixed academy folders and files with `01-`, `02-`, etc. where reading order matters.
- Removed low-value legacy QA migration files after review.

## Known Gaps

- Backend learning paths need academy-native curricula for PHP/Laravel, Node.js/TypeScript, and ColdFusion/CFML.
- Mobile learning paths need dedicated curricula for iOS, Android, and any adopted cross-platform stack.
- Platform engineering needs curricula for CI/CD, cloud foundations, containers, Kubernetes, IaC, observability, incident response, and release engineering.
- Architecture needs curricula for ADRs, system design, API/integration architecture, data architecture, reliability, security architecture, and modernization.
- Engineering leadership needs curricula for team lead fundamentals, mentoring, delivery leadership, review culture, stakeholder communication, and engineering management basics.
- AI-assisted development/testing/prompt engineering paths need full curricula with delegation-level guardrails.
- Frontend add-ons needed: i18n policy, PWA/offline guidance, design-system integration.
- Quality add-ons needed: contract testing, visual regression, mobile/device testing, accessibility depth, performance/load testing, quality dashboard template.
- Legacy `learning-paths/` folders remain as compatibility copies until existing links are migrated.

## Useful External Resources To Curate

Use these as starting links when building the missing paths. Prefer official docs, maintained learning portals, and stable video/tutorial hubs over one-off videos that can go stale quickly.

| Area | Starting resources |
|---|---|
| React | [React Learn](https://react.dev/learn) |
| Next.js | [Next.js Learn](https://nextjs.org/learn), [Next.js App Router docs](https://nextjs.org/docs/app) |
| Playwright | [Playwright getting started](https://playwright.dev/docs/intro) |
| CI/CD | [GitHub Actions docs](https://docs.github.com/en/actions) |
| Containers | [Docker Get Started](https://docs.docker.com/get-started/) |
| Kubernetes | [Kubernetes tutorials](https://kubernetes.io/docs/tutorials/) |
| Reliability | [Google SRE Workbook](https://sre.google/workbook/table-of-contents/) |
| Architecture | [Azure Architecture Center](https://learn.microsoft.com/en-us/azure/architecture/) |

## QA Path Next Steps

1. Review [Manual Tester to Automation Engineer](./02-quality-engineering/02-automation/playwright/01-manual-to-automation.md).
2. Review [Automation Engineer to Senior Automation Engineer](./02-quality-engineering/02-automation/playwright/02-senior-automation.md).
3. Pilot [Manual Testing](./02-quality-engineering/01-manual-testing/README.md) with one QA cohort and collect examples.
4. Pilot the [QA Capstone Rubric](./02-quality-engineering/04-capstone-qa-rubric.md) with managers.
5. Add topic-specific learning links only where they support a precise skill.

## Deletion Candidates - Review Before Removing

Do not delete these without owner approval:

| Candidate | Reason to consider removal | Safer alternative |
|---|---|---|
| Reviewer-only gap-analysis files | Useful for CoE reviewers, but noisy for learners | Keep with `90-` prefix unless learner navigation becomes cluttered |
| Roadmap images | Helpful visual context but may become stale | Keep if source/date is documented; otherwise replace with maintained diagrams |
| Legacy `learning-paths/` compatibility folders | Duplicate academy content after migration | Remove only after `rg "learning-paths/"` shows no live references |
