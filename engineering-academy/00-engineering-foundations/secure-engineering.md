# Secure Engineering

The source of truth is [Security Audit Checklist](../../audit/security-audit-checklist.md).

Pair this with:

- [AI Era Coding Guidelines](../../general/ai-era-coding-guidelines.md) for Red Zone work
- [REST API Best Practices](../../general/rest-api-best-practices.md) for API boundary design
- Stack-specific standards for parameterized queries, validation, logging, and secrets

## Minimum Bar

- Never commit secrets.
- Validate inputs at system boundaries.
- Use parameterized queries or framework-safe query builders.
- Protect authorization checks server-side.
- Avoid logging PII, tokens, passwords, or payment data.
- Escalate auth, encryption, and production data changes for human-led review.
