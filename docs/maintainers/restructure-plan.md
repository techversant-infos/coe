# Repository Restructure Plan

> Tracks the cleanup of the CoE repository: one obvious folder structure, no duplicate content, working
> cross-links, and every document marked with its status.

**Status:** Phases 0 to 6 complete. Waiting for review and merge
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
| 5 | Status header on every document. Update outdated content in order of risk | Done |
| 6 | Rewrite root and academy READMEs, `CONTRIBUTING.md`, academy TODO | Done |

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
- **Lint backlog.** 14 markdownlint rules are off because existing content breaks them. The config lists each rule
  with its count. Turn a rule back on when its count reaches 0. The largest are line length (857), list indentation
  (387) and code blocks without a language (181). MD060 (table pipe spacing, 4,814) was added in Phase 6, after
  local runs were pinned to the markdownlint-cli2 version CI uses (0.23.2).
- **Folder indexes added:** `standards/`, `security/`, `ai/`, `docs/maintainers/`.
- **Rendering bug fixed:** the branch patterns in `standards/git/git-workflow.md` showed as `feature/fix--` on GitHub,
  because `<JIRA-ID>` and `<desc>` were read as HTML tags.

Found during Phase 4 and moved to Phase 5:

<!-- cspell:ignore Enginearden boxlucee -->

- **Unverifiable Lucee content.** The Lucee module refers to "Enginearden licensing" and a `boxlucee migrate` command.
  Neither exists in any source found. Lucee is free under LGPL v2.1, and paid support comes from Lucee Association
  Switzerland members.
- **Lost characters.** An earlier edit dropped dashes and emoji from some academy files, for example "New joiner
  (13 months in)" where "1-3 months" was meant, and "Suggested 68 Week Plan".

## Phase 5 Results

### Status headers

Every document in `standards/`, `security/` and `ai/` (except the skills library and index READMEs), and every
README in the academy, starts with one line:

```text
**Status:** Needs review · **Owner:** TBD · **Last updated:** 2025-11-13 · **Next review:** 2026-05-13
```

- **Next review** is the last content change before this restructure plus 6 months (3 months for `ai/`).
- **Status** is `Needs review` once that date has passed. 22 documents are overdue, including every stack
  standard (last changed November 2025) and all AI guides and prompts.
- 7 documents kept the status they already declared (the two draft security documents and five draft or planned
  academy paths). Three planned disciplines show `Planned`.
- **Owner** is `TBD` until the CoE lead names owners.

### Outdated content fixed, highest risk first

| Area | Was | Now |
|------|-----|-----|
| ColdFusion support status in client deliverables | CF2021 "Current", CF2018 "Extended support", "CF2018 is end-of-life in December" | Dated table from Adobe's matrix: CF2021 extended support ends 2026-11-10, CF2023 to 2028-05-16, CF2025 to 2030-04-08 |
| Claude API examples (ColdFusion) | Retired `claude-3-5-sonnet-20241022`, reads `content[1].text`, no refusal check | `claude-sonnet-5-5`, reads the first text block, checks `stop_reason`, quoted JSON keys, server-side fallback |
| Lucee module | "Enginearden licensing", `boxlucee migrate` command | LGPL licence and Lucee Association Switzerland support; CFConfig commands checked against its docs |
| Claude Code token guide | Sonnet 4.6 and Opus 4.6, Codex "API playground free tier" | Claude 5.5 models, Haiku 5.5 as the low-cost option, Codex through ChatGPT sign-in |
| Supported versions | Lucee 5+, ColdFusion 2018+ or 2021+ | Lucee 6.2+, ColdFusion 2023+ |
| Example stacks in prompts | Node.js 20, PostgreSQL 14, React 18, Laravel 11, PHP 8.2 | Node.js 24, PostgreSQL 17, React 19, Laravel 13, PHP 8.4 |
| Branch naming | Three conventions | The git standard; the PR prompt and the automation rule link to it |

- **Lost characters restored.** 791 lines in 13 files got their dashes, arrows and emoji back from the intact
  originals in `learning-paths/` (commit `e4425af^`). About 286 characters stay missing, in lines edited since.
- **Anchors.** `scripts/check-links.py` now also checks `#heading` links into other files. It found 91 broken ones,
  all now fixed. Slugs were confirmed against pages GitHub rendered.

Not changed on purpose: Java 17 and Python 3.11 in examples (both still supported), the ColdFusion migration hour
benchmarks (a note says CF2025 benchmarks are missing), and the Ollama model list.

## Phase 6 Results

- **Root README** describes the new layout and the status line, and starts with a task-based "Start Here" table.
- **AGENTS.md** is the one guide for every AI agent. It is tool-neutral, links to the standards instead of repeating
  stack and REST rules, and no longer points to the non-existent `ai/Codex/` folder.
- **CLAUDE.md** imports AGENTS.md with `@AGENTS.md` and keeps only Claude Code details: the `.claude` kit and the
  commit tag.
- **CONTRIBUTING.md** documents the status line, branch names from the git standard, a consistent versioning
  table, how to move or retire a document, and the checks to run before a pull request.
- **Academy README** lists `07-consulting/` and links to the standards, security and AI indexes.
- **Academy TODO** drops the finished migration items and adds the consulting discipline.
- Local check commands are pinned to the versions CI uses: markdownlint-cli2 0.23.2 and cspell 10.4.0.

## Parked Work

These sit on local branches so they do not mix with the restructure:

| Branch | Content | Next step |
|--------|---------|-----------|
| `feature/COE-ai-architect-path` | AI Architect learning path outline | Rebase onto the restructured academy, then open a PR |
| `feature/COE-security-checklist-v1` | Part A and Part B checklist, v1.0 | Reconcile with the v2.0 checklist and reference now on `main` |

## Open Items

- Push `chore/COE-repo-restructure` and open a pull request to `main`. Nothing is pushed yet.
- Name an owner for each area. Status lines and the inventory say `TBD`.
- Run the Lychee external link check in CI. It cannot run locally; every URL changed here was checked by hand.
- Decide how to reconcile `origin/dev`, which has 8 commits that `main` lacks.
- Confirm the Red Zone list (see Phase 3 Results). Branch naming now follows the git standard.
- Review the 22 documents marked `Needs review`, starting with the stack standards.
- Delete the 16 redirect stubs after the next release.
- Work down the markdownlint backlog in `.markdownlint-cli2.jsonc`, one rule per pull request.
