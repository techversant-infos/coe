# AGENTS.md

Guidance for AI coding agents (Claude Code, Codex, Copilot and others) working in this repository.
Claude Code also reads [CLAUDE.md](./CLAUDE.md), which imports this file.

## What This Repository Is

A **standards and learning repository**, not an application. It holds Techversant's engineering standards,
security checklists, AI guidance and the Engineering Academy. Almost every change is to a markdown document.

## Layout

```text
coe/
|-- standards/            general/  git/  php/  nodejs/  coldfusion/
|-- security/             audit/  ai-security/
|-- ai/                   guides/  prompts/  skills-library/  presentations/
|-- engineering-academy/  00-07 disciplines, learning-levels/, career-progression/
|-- docs/maintainers/     restructure plan, inventory, academy TODO, gap analyses
|-- archive/              superseded documents, never linked from live content
`-- scripts/              check-links.py
```

Each top-level folder has a README index. Files at the old paths (`audit/`, `cf/`, `general/`, `git/`, `neural/`,
`nodejs/`, `php/`) are redirect stubs. Do not edit them or add new files there.

## Rules for AI-Assisted Work

The rules live in [AI Era Coding Guidelines](./standards/general/ai-era-coding-guidelines.md). In short:

- Review every line of AI output before committing, and never commit what you cannot explain.
- Pick a delegation level for each task: Full delegate, Collaborate, Human-led or Never delegate
  ([section 2.1](./standards/general/ai-era-coding-guidelines.md#21-delegation-levels)).
- Never generate Red Zone content: authentication and authorization, encryption and key management, PII and payment
  handling, production database migrations ([section 2.2](./standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only)).
- Tag AI-assisted commits with `[ai-assisted: <tool>]`, for example `[ai-assisted: claude]`.

## Git

This repository holds documents, so it skips the `dev` → `staging` promotion that product teams follow in
[Git Workflow](./standards/git/git-workflow.md):

- Branch from `main` as `feature/<type>-<JIRA-ID>-<description>`, for example `feature/fix-AGL-881-rounding`.
- Write [Conventional Commits](https://www.conventionalcommits.org/): `docs(security): add SSRF checks`.
- Open pull requests against `main`. CI runs the checks on every pull request to `main`, and a change takes effect
  when it merges.
- Never force-push to a shared branch.

## Writing and Editing Documents

- Keep the status line under each document title up to date
  (`**Status:** · **Owner:** · **Last updated:** · **Next review:**`). See [CONTRIBUTING.md](./CONTRIBUTING.md).
- Use kebab-case file names and relative links.
- Move a superseded document to `archive/` with a banner. Do not delete it.
- Academy content follows the rules in `.claude/rules/` and the templates in `.claude/templates/`.
- Files use UTF-8 and LF line endings (`.gitattributes`). Indent with 2 spaces, 4 in PHP code.

## Checks

Run these before you open a pull request. CI runs the same checks.

```bash
python scripts/check-links.py
npx markdownlint-cli2@0.23.2 "**/*.md"
npx cspell@10.4.0 --no-progress "**/*.md"
```

- `check-links.py` finds broken relative links, links to missing headings, references to removed folders and
  status lines whose next review comes before their last update.
- markdownlint rules are in `.markdownlint-cli2.jsonc`. Some rules are off as a backlog; do not turn one on in an
  unrelated change.
- Add new technical words to `.cspell/project-words.txt`, not to a document.

## Key Files

| File | Purpose |
|------|---------|
| [standards/README.md](./standards/README.md) | Index of every coding standard |
| [standards/git/git-workflow.md](./standards/git/git-workflow.md) | Branching, commits, promotion, rollback |
| [standards/general/ai-era-coding-guidelines.md](./standards/general/ai-era-coding-guidelines.md) | AI review rules, delegation levels, Red Zone |
| [standards/general/rest-api-best-practices.md](./standards/general/rest-api-best-practices.md) | API naming, responses, errors, filtering |
| [security/audit/security-audit-checklist.md](./security/audit/security-audit-checklist.md) | Security checklist for every pull request |
| [ai/prompts/developer-handbook-full.md](./ai/prompts/developer-handbook-full.md) | Prompt templates for the development lifecycle |
| [engineering-academy/README.md](./engineering-academy/README.md) | Academy disciplines and starting points |
| [docs/maintainers/restructure-plan.md](./docs/maintainers/restructure-plan.md) | Current cleanup decisions and open items |
