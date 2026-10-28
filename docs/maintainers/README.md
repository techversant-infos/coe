# Maintainer Docs

> Working documents for the people who maintain this repository. Learners and developers do not need these.

| Document | Purpose |
|----------|---------|
| [Restructure Plan](./restructure-plan.md) | Decisions, phases and open items for the repository cleanup |
| [Repository Inventory](./repo-inventory.csv) | Every tracked file with its status, owner and planned action |
| [Academy TODO](./academy-todo.md) | Gaps and planned work in the Engineering Academy |

## Gap Analyses

Reviewer-only coverage matrices that show what a learning path covers and what it leaves out.

| Document | Compares |
|----------|----------|
| [Developer Excellence gap analysis](./gap-analyses/90-gap-analysis.md) | The Developer Excellence curriculum with the wider developer-discipline landscape |
| [React roadmap gap analysis](./gap-analyses/90-roadmap-gap-analysis.md) | The React path with the full React ecosystem |
| [Next.js gap analysis](./gap-analyses/90-nextjs-gap-analysis.md) | The Next.js path with the wider Next.js ecosystem |

## Checks

Run the relative link and legacy path check before you open a pull request:

```bash
python scripts/check-links.py --orphans
```
