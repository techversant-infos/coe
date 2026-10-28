# Repository Restructure Plan

> Tracks the cleanup of the CoE repository: one obvious folder structure, no duplicate content, working
> cross-links, and every document marked with its status.

**Status:** In progress (Phases 0, 1 and 2 complete)
**Branch:** `chore/COE-repo-restructure`

## Decisions

| Topic | Decision |
|-------|----------|
| Structure | Group by purpose: `standards/`, `security/`, `ai/`, `engineering-academy/`, `docs/maintainers/` |
| Removed or superseded content | Move to `archive/` (mirrors the old path) until a person verifies it. Do not delete |
| `git/secrets.env` | Untrack and ignore. Not archived. Values confirmed invalid by the owner, so no history purge |
| Exact duplicates | Delete only when byte-identical to a kept file (the `git/` dotfiles) |
| Owners | To be named by the CoE lead. The inventory shows `TBD` until then |

## Target Structure

```text
coe/
|-- README.md  CONTRIBUTING.md  AGENTS.md  CLAUDE.md
|-- standards/           general/  git/  php/  nodejs/  coldfusion/
|-- security/            audit/  ai-security/
|-- ai/                  guides/  prompts/  skills-library/  presentations/
|-- engineering-academy/ 00-06 disciplines, 07-consulting/, learning-levels/, career-progression/
|-- docs/maintainers/    restructure-plan.md, repo-inventory.csv, academy-todo.md, gap-analyses/
|-- archive/             superseded content, with a banner and a replacement link
|-- scripts/             check-links.py
`-- .github/  .claude/   tooling only
```

## Phases

| Phase | Scope | Status |
|-------|-------|--------|
| 0 | Baseline: sync with `origin/main`, park open work, add link checker and inventory | Done |
| 1 | Safety fixes: untrack `secrets.env`, ignore rules, Claude permissions, file encoding | Done |
| 2 | Move files with `git mv` and kebab-case names. Fix links in the same change | Done |
| 3 | De-duplicate: one canonical source per topic, superseded copies to `archive/` | Not started |
| 4 | Cross-links: fix broken links, add folder indexes, add CI checks | Not started |
| 5 | Status header on every document. Update outdated content in order of risk | Not started |
| 6 | Rewrite root and academy READMEs, `CONTRIBUTING.md`, academy TODO | Not started |

## Baseline (origin/main, 2026-10-27)

| Measure | Count |
|---------|-------|
| Tracked files | 271 |
| Markdown files checked | 240 |
| Broken relative links | 9 |
| References to the removed `learning-paths/` folder | 6 |
| Markdown files with no inbound links | 43 |
| Markdown files with no declared status | 230 |
| Files with outdated version or model signals | 12 |

Run `python scripts/check-links.py --orphans` to reproduce.

## Redirect Stubs

Sixteen files at the old `audit/`, `cf/`, `general/`, `git/`, `neural/`, `nodejs/` and `php/` paths are one-line
stubs that point to the new location. They keep bookmarked GitHub links, Drive links and Slack links working.

- Each stub starts with `<!-- redirect-stub: delete after the next release -->`.
- Delete them all once the CoE lead confirms that external links are updated.
- The academy and `ai/` folders have no stubs. Their links are internal.
- `git/Git & Git workflow.pdf` moved to `standards/git/git-and-git-workflow.pdf` and has no stub.

## Parked Work

These sit on local branches so they do not mix with the restructure:

| Branch | Content | Next step |
|--------|---------|-----------|
| `feature/COE-ai-architect-path` | AI Architect learning path outline | Rebase onto the restructured academy, then open a PR |
| `feature/COE-security-checklist-v1` | Part A and Part B checklist, v1.0 | Reconcile with the v2.0 checklist and reference now on `main` |

## Open Items

- Name an owner for each area (inventory column `owner`).
- Decide how to reconcile `origin/dev`, which has 8 commits that `main` lacks.
- Compare `cf/` standards with the `cf-consulting` deliverables for overlap before Phase 3.
