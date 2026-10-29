# Engineering Standards

> Coding standards, style guides and review checklists for every Techversant stack.

Use these when you write or review code. Each stack folder has the same three documents: best practices, a style
guide and a code review checklist.

## General

| Document | Use it for |
|----------|------------|
| [AI Era Coding Guidelines](./general/ai-era-coding-guidelines.md) | Human review of AI output, delegation levels, Red Zone rules |
| [REST API Best Practices](./general/rest-api-best-practices.md) | Resource naming, status codes, versioning, error format |

## Git

| Document | Use it for |
|----------|------------|
| [Git Workflow](./git/git-workflow.md) | Branch naming, commit format, promotion from `dev` to `main`, rollback |
| [Git and Git Workflow (slides, PDF)](./git/git-and-git-workflow.pdf) | Training deck for the workflow above |
| [secrets.env.example](./git/secrets.env.example) | Template for local secrets. Never commit the real file |

## Stacks

| Stack | Best practices | Style guide | Code review checklist |
|-------|----------------|-------------|-----------------------|
| PHP / Laravel | [Best practices](./php/php-best-practices.md) | [Coding standards](./php/php-coding-standards.md) | Not written yet |
| Node.js / TypeScript | [Best practices](./nodejs/nodejs-typescript-best-practices.md) | [Style guide](./nodejs/nodejs-typescript-style-guide.md) | [Checklist](./nodejs/nodejs-typescript-code-review-checklist.md) |
| ColdFusion / CFML | [Best practices](./coldfusion/coldfusion-best-practices.md) | [Style guide](./coldfusion/coldfusion-style-guide.md) | [Checklist](./coldfusion/coldfusion-code-review-checklist.md) |

ColdFusion client work (assessments, migrations, security reviews) has its own playbooks in the
[ColdFusion consulting path](../engineering-academy/07-consulting/coldfusion/deliverables/).

## Related

- [Security checklists and audit framework](../security/)
- [AI guides and prompts](../ai/)
