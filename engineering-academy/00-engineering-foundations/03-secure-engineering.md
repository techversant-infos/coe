# Secure Engineering

**Level:** Foundation
**Next:** [Engineering Communication](./04-communication.md)

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

## Security Review Triggers

Pause and request senior or security review when a change touches:

- Authentication, authorization, session handling, or password reset flows.
- Encryption, key rotation, token signing, secrets, or certificate handling.
- PII, payment data, audit logs, exports, or production database changes.
- File upload, SSRF-sensitive integrations, webhooks, or user-controlled URLs.
- Admin privileges, RBAC, tenant isolation, or data access boundaries.

## Practice Task

Review one recent PR and write down:

```text
Input boundaries:
Authorization checks:
Secrets / PII exposure:
Logging risk:
Rollback or incident risk:
Human review needed? yes/no and why:
```

## Useful References

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [OWASP WebGoat](https://owasp.org/www-project-webgoat/)
