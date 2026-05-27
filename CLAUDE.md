# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **Center of Excellence (CoE) standards repository** — not an application. It contains Techversant's engineering guidelines, best practices, and AI-assisted development standards for multiple technology stacks.

## Git Workflow

**Multi-Stage Promotion Model:**
```
feature branch → dev (auto-deploy) → staging (manual) → main (verified) → tag (prod deploy)
```

**Branch naming:** `feature/<JIRA-ID>-<description>`

**Commit format:** [Conventional Commits](https://www.conventionalcommits.org/)
```
feat(module): add user login
fix(module): handle null pointer
docs(module): update API guide
```

**Merge rules:** PR review + CI required. Never force-push to shared branches.

## AI-Assisted Development Standards

These standards apply to all code in this repository:

**Human-in-the-Loop (Mandatory):**
- Review every line of AI output before committing
- Never commit code you cannot explain
- Tag AI-assisted commits: `[ai-assisted: claude]`
- Use delegation levels: 🟢 FULL DELEGATE → 🟡 COLLABORATE → 🟠 HUMAN-LED → 🔴 NEVER DELEGATE

**Red Zone (Manual Only — Never Delegate):**
- Authentication & authorization
- Encryption & key management
- PII handling & payment processing
- Production database migrations

**Two-Layer Review:**
1. AI Pre-Review (logic gaps, edge cases, tests)
2. Human Review (business logic, security, architecture fit)

## Coding Standards by Stack

### PHP / Laravel
- PSR-12 compliance (4 spaces, 120 char line limit)
- Use prepared statements — never concatenate SQL
- Use `password_hash()` / `password_verify()` for passwords
- Controllers slim; business logic in Services/Actions

### ColdFusion / CFML
- CFScript for business logic
- Always use `<cfqueryparam>`
- Query results prefixed with `q` (e.g., `qUsers`)
- Cache long-running queries with `cachedwithin`

### Node.js / TypeScript
- Use Zod for validation + type inference
- Pino for structured logging with requestId
- Follow hexagonal architecture (ports/adapters)
- Add Zod validation for every public endpoint

## REST API Conventions

**Response format:**
```json
{
  "success": true,
  "data": { ... },
  "meta": { "traceId": "abc123" }
}
```

**Error format:**
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "...",
    "details": {}
  }
}
```

**Boolean naming:** Always use `is`/`has`/`can` prefix (`isActive`, `hasPermission`, `canRedeem`)

**Date format:** ISO 8601 only (`2025-01-20T14:30:00Z`)

**Filtering operators:** `_gt`, `_gte`, `_lt`, `_lte`, `_ne`, `_in`, `_between`

**Sorting:** `sort=field` (asc), `sort=-field` (desc)

## Key Files Reference

| File | Purpose |
|------|---------|
| `git/Techversant_Git_Workflow.md` | Full branching, commits, rollback, CI/CD governance |
| `general/ai-era-coding-guidelines.md` | AI-assisted development principles |
| `general/rest-api-best-practices.md` | API design, naming, error handling, filtering |
| `php/php-coding-standards.md` | PHP/Laravel standards (PSR-12, security) |
| `cf/coldfusion-style-guide.md` | CFML conventions (2-space indent, `q` prefix for queries) |
| `nodejs/nodejs-typescript-best-practices.md` | Node.js service patterns (Zod, Pino, hexagonal) |
| `ai/claude/claude-dev-cheatsheet.md` | Claude Code prompts, session controls, delegation levels |
| `ai/prompts/developer_handbook_Full.md` | AI prompt templates for full development lifecycle |

## Editor Config

Uses `.editorconfig`: UTF-8, 2-space indentation (except PHP uses 4), LF line endings.