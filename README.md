# Techversant Center of Excellence (CoE)

A standardized engineering reference for Techversant teams — covering best practices, coding standards, security audits, and compliance requirements.

---

## Purpose

This repository is maintained by the **Center of Excellence (CoE)** to ensure consistency, quality, and compliance across all engineering teams. Use these standards as the baseline for any project.

> **AI can write code. Engineers build systems.** — Human review is mandatory for all AI-assisted contributions.

---

## Repository Structure

```
coe/
├── README.md              ← You are here
├── CLAUDE.md              ← Claude Code guidance (AI tools read this)
├── audit/                 ← Compliance & audit materials
│   ├── coe-audit-framework.md
│   └── security-audit-checklist.md
├── cf/                    ← ColdFusion / CFML standards
│   ├── coldfusion-best-practices.md
│   ├── coldfusion-code-review-checklist.md
│   └── coldfusion-style-guide.md
├── general/               ← Cross-stack standards
│   ├── ai-era-coding-guidelines.md
│   └── rest-api-best-practices.md
├── git/                   ← Git workflow & governance
│   ├── Techversant_Git_Workflow.md
│   └── README.md
├── nodejs/                ← Node.js / TypeScript standards
│   ├── nodejs-typescript-best-practices.md
│   ├── nodejs-typescript-code-review-checklist.md
│   └── nodejs-typescript-style-guide.md
├── php/                   ← PHP / Laravel standards
│   ├── php-best-practices.md
│   └── php-coding-standards.md
└── ai/                    ← AI development tools & prompts
    ├── prompts/
    └── claude/
```

---

## Quick Start

### For a New Project

1. **Read the Git workflow** — `git/Techversant_Git_Workflow.md`
2. **Choose your stack** — PHP, Node.js, or ColdFusion
3. **Apply coding standards** — Style guide + best practices for your stack
4. **Set up CI** — Use the workflow templates (coming soon)

### For Code Review

1. **Check the code review checklist** — Stack-specific (`*-code-review-checklist.md`)
2. **Verify AI disclosures** — All AI-assisted commits tagged `[ai-assisted: claude]`
3. **Run linting** — Config per stack (coming soon)

### For Compliance Audit

1. **Start with the Audit Framework** — `audit/coe-audit-framework.md`
2. **Use the Security Checklist** — `audit/security-audit-checklist.md`
3. **Track findings** — Use the remediation tracker in Section 10

---

## Standards by Stack

| Stack | Style Guide | Best Practices | Code Review |
|-------|-------------|----------------|-------------|
| PHP / Laravel | `php/php-coding-standards.md` | `php/php-best-practices.md` | PHP checklist |
| Node.js / TypeScript | `nodejs/nodejs-typescript-style-guide.md` | `nodejs/nodejs-typescript-best-practices.md` | Node.js checklist |
| ColdFusion / CFML | `cf/coldfusion-style-guide.md` | `cf/coldfusion-best-practices.md` | CFML checklist |

---

## Key Principles

### Git Workflow
- Branch from `main`, PR to `dev` → `main` → tag for release
- Conventional Commits: `feat(module): description`
- Branch naming: `feature/<JIRA-ID>-<description>`

### AI-Assisted Development
- **Two-Layer Review:** AI pre-review + human review
- **Tag AI commits:** `[ai-assisted: claude]`
- **Red Zone (Manual Only):** Auth, encryption, PII, payments, prod DB migrations

### Security
- No hardcoded secrets
- Input validation + output encoding
- OWASP Top 10 alignment

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to propose changes, update standards, or report issues.

---

## Document Control

| Document | Version | Owner | Review Cycle |
|----------|---------|-------|--------------|
| Git Workflow | 1.3 | DevOps Lead | Quarterly |
| AI Era Guidelines | — | CoE | Quarterly |
| REST API Best Practices | 3.0 | CoE | Semi-annual |
| PHP Standards | 1.1 | CoE | Quarterly |
| CFML Standards | 1.0 | CoE | Quarterly |
| Audit Framework | 1.0 | Audit Team | Quarterly |
| Security Checklist | 1.0 | Security Team | Quarterly |

---

**Maintained by:** Techversant CoE
**Last Updated:** May 2026