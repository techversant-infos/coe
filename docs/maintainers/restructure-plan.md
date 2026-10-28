# Repository Restructure Plan

> Tracks the cleanup of the CoE repository: one obvious folder structure, no duplicate content, working
> cross-links, and every document marked with its status.

**Status:** In progress (Phases 0 to 4 complete)
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
| 3 | De-duplicate: one canonical source per topic, superseded copies to `archive/` | Done (`AGENTS.md` / `CLAUDE.md` moved to Phase 6) |
| 4 | Cross-links: fix broken links, add folder indexes, add CI checks | Done |
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

## Phase 3 Results

A line-level similarity scan of every markdown file outside `archive/` found no whole-file duplicates after
`ai-team-best-practices.md` was archived in Phase 2.

| Topic | Canonical source | Change |
|-------|------------------|--------|
| Delegation levels and Red Zone | `standards/general/ai-era-coding-guidelines.md` sections 2.1 and 2.2 | Added. The standard was cited for these rules but did not define them. The cheatsheet and `ai-team-best-practices.md` now link to it instead of keeping their own tables, which had drifted apart |
| Developer prompts, sections 4 to 9 | `ai/prompts/section-04-*.md` to `section-09-*.md` | The handbook keeps sections 1 to 3, the checklist and anti-patterns, and summarises 4 to 9 with a link each |
| ColdFusion standards and consulting deliverables | Both kept | No shared text. Different audiences (developers, client audits). Cross-link in Phase 4 |
| Stack translation files | All three kept | Overlap is the shared template only |
| `AGENTS.md` and `CLAUDE.md` | `AGENTS.md` | Done in Phase 6 with the README rewrite |

Conflicts found that need an owner's decision (Phase 5):

- **Red Zone list.** The standard uses the list from `CLAUDE.md`: auth, encryption and keys, PII and payments,
  production migrations. The old cheatsheet also listed security middleware. The old team guide also listed
  production incidents and architecture decisions.
- **Branch naming.** Three conventions disagree. `standards/git/git-workflow.md` uses `feature/fix-<JIRA-ID>-<desc>`
  and promotes through `dev`. `ai/prompts/section-09-pull-request.md` teaches `bugfix/`, `hotfix/`, `release/` and
  targets `develop`. `.claude/rules/automation-engineering-standards.md` uses `fix/<description>`.

## Phase 4 Results

| Measure | Before | After |
|---------|--------|-------|
| Broken relative links | 9 | 0 |
| References to the removed `learning-paths/` folder | 6 | 0 |
| Markdown files with no inbound links (tooling and redirect stubs excluded) | 13 | 0 |
| Dead or moved external URLs in the last CI run | 12 | 0 (checked by hand; Lychee confirms on the next CI run) |
| markdownlint errors with the enabled rules | not run | 0 |
| Spelling issues | 978 | 7, all in content held for Phase 5 |

- **CI was failing on every run.** The markdownlint step used `DavidAnson/vscode-markdown-lint-action`, which does not
  exist. It now uses `DavidAnson/markdownlint-cli2-action`. A fourth job runs `scripts/check-links.py`.
- **Config files:** `.markdownlint-cli2.jsonc` (rules and ignored folders), `.lycheeignore` (sites that block bots,
  checked by hand), `cspell.json` with `.cspell/project-words.txt`. All three skip `archive/`.
- **Lint backlog.** 13 markdownlint rules are off because existing content breaks them. The config lists each rule
  with its count. Turn a rule back on when its count reaches 0. The largest are line length (857), list indentation
  (387) and code blocks without a language (181).
- **Folder indexes added:** `standards/`, `security/`, `ai/`, `docs/maintainers/`.
- **Rendering bug fixed:** the branch patterns in `standards/git/git-workflow.md` showed as `feature/fix--` on GitHub,
  because `<JIRA-ID>` and `<desc>` were read as HTML tags.

Found during Phase 4 and moved to Phase 5:

- **Unverifiable Lucee content.** The Lucee module refers to "Enginearden licensing" and a `boxlucee migrate` command.
  Neither exists in any source found. Lucee is free under LGPL v2.1, and paid support comes from Lucee Association
  Switzerland members.
- **Lost characters.** An earlier edit dropped dashes and emoji from some academy files, for example "New joiner
  (13 months in)" where "1-3 months" was meant, and "Suggested 68 Week Plan".

## Parked Work

These sit on local branches so they do not mix with the restructure:

| Branch | Content | Next step |
|--------|---------|-----------|
| `feature/COE-ai-architect-path` | AI Architect learning path outline | Rebase onto the restructured academy, then open a PR |
| `feature/COE-security-checklist-v1` | Part A and Part B checklist, v1.0 | Reconcile with the v2.0 checklist and reference now on `main` |

## Open Items

- Name an owner for each area (inventory column `owner`).
- Decide how to reconcile `origin/dev`, which has 8 commits that `main` lacks.
- Confirm the Red Zone list and pick one branch naming convention (see Phase 3 Results).
