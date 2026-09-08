# CoE Security Checklist

**Version:** 2.0
**Issued by:** Techversant Center of Excellence (CoE)
**Effective Date:** September 2026
**Audience:** Every engineer, on every pull request
**Next Review:** December 2026

> The working security checklist for Techversant engineering. Structured against the
> [OWASP Top 10:2025](https://owasp.org/Top10/2025/).
>
> **Need more depth?** Every block below links to the
> [CoE Security Audit Reference](./security-audit-reference.md) — 358 controls, evidence rules,
> compliance mapping, and testing requirements. Use the reference for release reviews and audits;
> use this page for everyday work.

---

## How to use this

- **Every pull request** — run the [Minimum Bar](#minimum-bar). Ten items, two minutes.
- **Every feature** — run the [OWASP blocks](#a012025--broken-access-control) relevant to what you changed.
- **Release and audit** — use the [full reference](./security-audit-reference.md) instead.
- Items marked **(B)** are **release-blocking**. Shipping with one open needs a written exception
  approved by the Security Lead ([Audit Framework §8](./coe-audit-framework.md)).
- If something genuinely does not apply, mark it `N/A` **and write why**. An unexplained `N/A` is a finding.

---

## Minimum Bar

Non-negotiable on every change. If you read nothing else on this page, read this.

- [ ] **(B)** No secrets in code, config, CI logs, or commit history
- [ ] **(B)** Authorization enforced server-side on every protected operation
- [ ] **(B)** All database access uses parameterized queries
- [ ] **(B)** All user input validated server-side at the trust boundary
- [ ] **(B)** All output encoded for its rendering context
- [ ] **(B)** No PII, credentials, or tokens written to logs
- [ ] **(B)** No dependency with a known Critical CVE, or one listed in
      [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [ ] **(B)** TLS enforced end to end
- [ ] **(B)** Errors fail closed and leak no internal detail
- [ ] **(B)** Authentication and authorization events are logged

---

## A01:2025 — Broken Access Control

Still the #1 risk. **SSRF now lives here**, not in A10.
· [Reference §3](./security-audit-reference.md) · [OWASP](https://owasp.org/Top10/2025/)
· [Cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

- [ ] **(B)** Every record fetched by ID is verified as belonging to the caller
- [ ] **(B)** Deny by default — access needs an explicit grant, not the absence of a denial
- [ ] **(B)** User-supplied URLs validated against an allowlist; cloud metadata endpoints blocked
- [ ] Permissions checked, not role name strings
- [ ] Unauthorized access to someone else's record returns `404`, not `403`
- [ ] State-changing requests are CSRF-protected; cookies are `SameSite`

## A02:2025 — Security Misconfiguration

Up from #5 to #2. Give it more attention than you used to.
· [Reference §4](./security-audit-reference.md) · [OWASP](https://owasp.org/Top10/2025/)

- [ ] **(B)** Debug mode off outside development
- [ ] **(B)** Default credentials changed on every component
- [ ] **(B)** No storage bucket, database, or cache publicly exposed
- [ ] Admin consoles unreachable from the public internet
- [ ] Security headers set — HSTS, CSP, `nosniff`, `Referrer-Policy`, `Permissions-Policy`
      ([full table](./security-audit-reference.md))
- [ ] CORS uses an explicit origin allowlist, never a wildcard on authenticated data

## A03:2025 — Software Supply Chain Failures

New for 2025 and broader than the old "Vulnerable Components". **Dependency scanning alone no
longer satisfies this** — how you build and ship is in scope.
· [Reference §5](./security-audit-reference.md) · [OWASP](https://owasp.org/Top10/2025/)

- [ ] **(B)** No Critical CVE or KEV-listed dependency
- [ ] **(B)** CI secrets in the platform secret store, never in workflow files
- [ ] Lockfile committed; CI installs from it
- [ ] Third-party CI actions pinned to a commit SHA, not a mutable tag
- [ ] New dependencies checked for maintenance, license, and typosquatting before adoption
- [ ] SBOM produced per release ([CycloneDX](https://cyclonedx.org/) or [SPDX](https://spdx.dev/))

## A04:2025 — Cryptographic Failures

· [Reference §6](./security-audit-reference.md) · [OWASP](https://owasp.org/Top10/2025/)
· [Cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)

- [ ] **(B)** TLS 1.2 minimum, 1.3 preferred; certificate validation never disabled
- [ ] **(B)** Confidential data encrypted at rest
- [ ] **(B)** Passwords hashed with Argon2id, scrypt, or bcrypt (cost ≥ 12)
- [ ] **(B)** Secret scanning in CI, covering git history — not just the working tree
- [ ] Secrets in a managed store; a leaked secret is **revoked**, not just deleted
- [ ] No forced password expiry — rotate on evidence of compromise
      ([NIST 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html))

## A05:2025 — Injection

Down from #3 to #5, but unchanged in what it demands of you.
· [Reference §7](./security-audit-reference.md) · [OWASP](https://owasp.org/Top10/2025/)
· [Cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html)

- [ ] **(B)** Queries parameterized — no concatenation, even for values you believe are safe
- [ ] **(B)** Output encoded for its context: HTML, attribute, JavaScript, URL, CSS
- [ ] **(B)** File uploads validated by magic bytes, not extension or client MIME type
- [ ] Dynamic identifiers (table, column, sort) resolved through an allowlist
- [ ] Framework auto-escaping left on; every bypass reviewed
- [ ] Mass assignment prevented — request fields bound explicitly
- [ ] Command, LDAP, XPath, template, XML, header, and log injection considered
      ([context table](./security-audit-reference.md))

## A06:2025 — Insecure Design

· [Reference §8](./security-audit-reference.md) · [OWASP](https://owasp.org/Top10/2025/)
· [Cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)

- [ ] **(B)** Authentication endpoints rate-limited with lockout
- [ ] Abuse cases considered, not just use cases — "how would someone misuse this?"
- [ ] Workflow steps enforced server-side; they cannot be skipped or replayed
- [ ] Quantity, price, and discount validated server-side, including negative values
- [ ] Account enumeration prevented on login, registration, and reset
- [ ] Expensive operations (search, export, report, AI inference) have their own limits

## A07:2025 — Authentication Failures

· [Reference §9](./security-audit-reference.md) · [OWASP](https://owasp.org/Top10/2025/)
· [Cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)

- [ ] **(B)** MFA enforced for administrative and production access
- [ ] **(B)** Session regenerated on login and on any privilege change
- [ ] **(B)** JWT algorithm pinned server-side; `alg: none` rejected; signature verified first
- [ ] A vetted identity library or provider is used — authentication is not hand-rolled
- [ ] Logout invalidates server-side; cookies are `Secure`, `HttpOnly`, `SameSite`
- [ ] OAuth uses Authorization Code + PKCE, validated `state`, exact redirect-URI matching
      ([RFC 9700](https://datatracker.ietf.org/doc/html/rfc9700))
- [ ] Reset tokens are random, single-use, short-lived, and hashed at rest

## A08:2025 — Software or Data Integrity Failures

Trusting untrusted code or data **at runtime** — narrower than A03.
· [Reference §10](./security-audit-reference.md) · [OWASP](https://owasp.org/Top10/2025/)

- [ ] **(B)** Native deserialization never applied to untrusted input
- [ ] **(B)** Inbound webhooks verify a signature, in constant time, with a replay window
- [ ] XML external entity resolution disabled; YAML parsed in safe mode
- [ ] No code, plugin, or config loaded from an unverified remote source
- [ ] Third-party scripts loaded with Subresource Integrity
- [ ] `postMessage` handlers validate `origin`

## A09:2025 — Security Logging and Alerting Failures

Renamed for 2025. **Producing logs is no longer enough — something must alert.**
· [Reference §11](./security-audit-reference.md) · [OWASP](https://owasp.org/Top10/2025/)
· [Cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)

- [ ] **(B)** Authentication attempts and authorization failures logged
- [ ] **(B)** Passwords, tokens, keys, and card numbers never logged
- [ ] **(B)** Alerts configured for repeated auth failure and authorization-failure spikes
- [ ] PII masked or omitted in logs
- [ ] Logs structured, correlated by trace ID, and shipped somewhere the app cannot modify
- [ ] Each alert has a named owner and a documented response
- [ ] Alert routing tested in the last quarter — an alert actually reached a human

## A10:2025 — Mishandling of Exceptional Conditions

**New for 2025.** Error handling is now a named security risk, not a code-quality nicety.
· [Reference §12](./security-audit-reference.md) · [OWASP](https://owasp.org/Top10/2025/)
· [Cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html)

- [ ] **(B)** Client-facing errors are generic — no stack traces, SQL, paths, or hostnames
- [ ] **(B)** Security decisions fail closed — an errored authorization check denies access
- [ ] **(B)** No empty catch blocks; every caught error is handled, re-thrown, or logged
- [ ] Timeouts set on every outbound call; request size limits enforced
- [ ] Collection endpoints paginated; no unbounded result sets
- [ ] Regular expressions checked for catastrophic backtracking on user input
- [ ] Failure paths are covered by tests, not just happy paths

---

## Does your change need more than this page?

Use the [full reference](./security-audit-reference.md) when your change touches:

| Area | Reference section |
|---|---|
| A public or partner API | [§13 API Security](./security-audit-reference.md) |
| AI tooling, an LLM feature, or an agent | [§14 AI and LLM Security](./security-audit-reference.md) |
| A mobile application | [§15 Mobile Application Security](./security-audit-reference.md) |
| Personal data or GDPR obligations | [§16 Privacy and Data Protection](./security-audit-reference.md) |
| Cloud, IaC, or container configuration | [§4.4–4.5 Cloud and Containers](./security-audit-reference.md) |
| Multi-tenant data boundaries | [§3.3 Tenant Isolation](./security-audit-reference.md) |

## Stop and escalate

Pull in a senior engineer or the Security Lead before merging when a change touches
authentication, authorization, session handling, password reset, encryption, key rotation, secrets,
PII, payment data, audit logs, production data, file upload, user-controlled URLs, webhooks, or
tenant isolation boundaries.

See [Secure Engineering — Security Review Triggers](../engineering-academy/00-engineering-foundations/03-secure-engineering.md)
and the Red Zone rules in [AI Era Coding Guidelines](../general/ai-era-coding-guidelines.md).

## Reporting

| Situation | Route |
|---|---|
| Active incident or live exploitation | Contact the Security Lead directly — do not file a public issue |
| Non-urgent finding | [Security Issue template](../.github/ISSUE_TEMPLATE/security-issue.md) |
| Audit finding | [Audit Finding template](../.github/ISSUE_TEMPLATE/audit-finding.md) |

---

## Where to go next

| Resource | Use |
|---|---|
| [CoE Security Audit Reference](./security-audit-reference.md) | The full 358-control version, with evidence and compliance mapping |
| [CoE Audit Framework](./coe-audit-framework.md) | Audit scope, severity, SLAs, exception process |
| [OWASP Top 10:2025](https://owasp.org/Top10/2025/) | The source taxonomy |
| [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) | Implementation guidance per control |
| [Secure Engineering](../engineering-academy/00-engineering-foundations/03-secure-engineering.md) | Foundation-level training |
| [PHP](../php/php-coding-standards.md) · [ColdFusion](../cf/coldfusion-style-guide.md) · [Node.js](../nodejs/nodejs-typescript-best-practices.md) | Stack-specific standards |
| [REST API Best Practices](../general/rest-api-best-practices.md) | API contract and error standards |

---

**Document Owner:** CoE Security Team
**Review Cycle:** Quarterly, and within 30 days of any OWASP Top 10 or regulatory update
**Change process:** [CONTRIBUTING.md](../CONTRIBUTING.md)
