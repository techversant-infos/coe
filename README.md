# Techversant Center of Excellence (CoE)

Engineering standards, security checklists, AI guidance and the Engineering Academy for Techversant teams.

## Start Here

| You want to | Go to |
|-------------|-------|
| Write or review code in your stack | [Engineering Standards](./standards/README.md) |
| Branch, commit and open a pull request | [Git Workflow](./standards/git/git-workflow.md) |
| Use AI tools safely (delegation levels, Red Zone) | [AI Era Coding Guidelines](./standards/general/ai-era-coding-guidelines.md) |
| Check a feature or release for security issues | [CoE Security Checklist](./security/audit/security-audit-checklist.md) |
| Learn a skill or plan your next career step | [Engineering Academy](./engineering-academy/README.md) |

## Repository Layout

```text
coe/
|-- standards/            coding standards, style guides and review checklists, one folder per stack
|-- security/             security checklist, audit reference, audit framework, AI security
|-- ai/                   AI guides, prompt templates, a skills library and presentations
`-- engineering-academy/  learning paths, learning levels and career progression
```

`.github/` and `.claude/` hold CI, templates and agent tooling.

| Folder | Contents |
|--------|----------|
| [standards](./standards/README.md) | General, Git, PHP / Laravel, Node.js / TypeScript, ColdFusion / CFML |
| [security](./security/README.md) | OWASP Top 10:2025 checklist and reference, CoE audit framework, AI security |
| [ai](./ai/README.md) | Usage standards, Claude cheat sheet, prompt handbook, skills library |
| [engineering-academy](./engineering-academy/README.md) | Disciplines 00 to 07, learning levels, career progression |

## Document Status

Every standard, security document, AI guide and academy README starts with a status line:

```text
**Status:** Needs review · **Owner:** TBD · **Last updated:** 2025-11-13 · **Next review:** 2026-05-13
```

`Needs review` means a full review is due or overdue. Use the document, but check versions and dates before you rely
on them.

## Contributing

Read [CONTRIBUTING.md](./CONTRIBUTING.md) before you open a pull request. Run the link check first:

```bash
python .github/scripts/check-links.py
```
