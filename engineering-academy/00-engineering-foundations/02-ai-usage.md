# AI Usage

**Level:** Foundation
**Next:** [Secure Engineering](./03-secure-engineering.md)

The source of truth is [AI Era Coding Guidelines](../../general/ai-era-coding-guidelines.md).

Use it for:

- Delegation levels
- AI-assisted commit disclosure
- Red Zone work
- Two-layer review
- Prompting and review discipline

## Minimum Bar

- Tag AI-assisted commits as required by the project.
- Review every AI-generated change before committing.
- Never delegate auth, encryption, PII handling, payments, or production database migrations.
- Use AI for explanation, scaffolding, test generation, and review assistance where appropriate.

## Delegation Rule Of Thumb

| Work type | Default stance |
|---|---|
| Explanation, summarization, examples | Green: full delegate is usually fine |
| Boilerplate, tests, docs, refactors | Yellow: collaborate and review carefully |
| Business logic, public APIs, architecture choices | Orange: human-led with AI support |
| Auth, encryption, PII, payments, prod migrations | Red: never delegate |

## Minimum Evidence Before Commit

- You can explain every AI-generated change.
- You checked edge cases and failure paths, not only happy paths.
- You ran or documented relevant verification.
- You disclosed AI assistance according to the repo standard.
- You did not paste secrets, customer data, tokens, or proprietary data into tools that are not approved for that data.

## Practice Task

Pick one AI-assisted change and write a short review note:

```text
What AI helped with:
What I changed after review:
What I verified:
What I did not delegate:
Residual risk:
```

## Useful References

- [Techversant AI Era Coding Guidelines](../../general/ai-era-coding-guidelines.md)
- [AI team best practices](../../ai/ai-team-best-practices.md)
