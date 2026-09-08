# CoE Security Audit Reference

**Status:** **DRAFT — not yet mandatory policy**
**Version:** 2.0-draft
**Issued by:** Techversant Center of Excellence (CoE)
**Supersedes:** v1.0 (May 2026)
**Audience:** CoE Audit Team, Security Team, Engineering Leads
**Next Review:** December 2026

> **This is a draft circulated for review.** It becomes mandatory policy only on Security Lead
> sign-off, at which point the status line above changes and an effective date is set. Audits run
> against it in the meantime should record findings as advisory.
>
> **Looking for the short version?** Most engineers want the
> [CoE Security Checklist](./security-audit-checklist.md) — 10 mandatory items plus about six per OWASP category.
> This document is the depth behind it: 358 controls, evidence rules, compliance mapping, and testing
> requirements. Every section here is linked from the corresponding block in the checklist.

Use this document when you are running a **release review, a quarterly deep audit, or an
incident investigation** — not when reviewing a routine pull request.

It supports the [CoE Audit Framework](./coe-audit-framework.md) and is structured to map one-to-one
against the [OWASP Top 10:2025](https://owasp.org/Top10/2025/), with additional cross-cutting sections
for API, AI/LLM, mobile, privacy, and operational security.

---

## 1. How to Use This Reference

### 1.1 Who runs it and when

| Trigger | Scope | Owner | Depth |
|---|---|---|---|
| Per PR | Changed code only | Reviewer | Minimum Bar (§1.4) |
| Per sprint | Feature-level | Team Lead | Sections relevant to the change |
| Per release | Whole application | QA + CoE | All applicable sections |
| Quarterly deep audit | Whole application + infrastructure | Audit Lead + Security | Full checklist |
| Incident-triggered | Affected component | Security Lead | Affected sections + §18 |

### 1.2 Marking items

Each item is marked as one of:

| Mark | Meaning |
|---|---|
| `[x]` | Verified in place, with evidence recorded |
| `[ ]` | Not verified, or verified as failing — raise a finding |
| `N/A` | Genuinely not applicable to this system — **reason must be written next to it** |

An unexplained `N/A` is itself a finding. "We don't do that yet" is a `[ ]`, not an `N/A`.

### 1.3 Severity

Security vulnerabilities are scored with CVSS v4.0 and remediated against the deadlines in
[§18.2](#182-slas), which are authoritative for vulnerabilities.
[CoE Audit Framework §5](./coe-audit-framework.md) severity applies to **audit findings** — process,
quality and compliance deviations. A finding that is both takes the stricter deadline.

Items marked **(B)** are **release-blocking**, which is a separate gate from the SLA clock: a release
cannot ship with an open **(B)** item regardless of remaining SLA time, and an expired SLA requires
remediation even with no release planned. Either may be waived only by a documented exception approved
by the Security Lead ([CoE Audit Framework §8](./coe-audit-framework.md)).

### 1.4 The Minimum Bar

If a team reads nothing else, these are non-negotiable on every change. They mirror the
[Secure Engineering Minimum Bar](../engineering-academy/00-engineering-foundations/03-secure-engineering.md).

- [ ] **(B)** No secrets in source code, config, CI logs, or commit history
- [ ] **(B)** Authorization enforced server-side on every protected operation
- [ ] **(B)** All database access uses parameterized queries or safe query builders
- [ ] **(B)** All user input validated server-side at the trust boundary
- [ ] **(B)** All output encoded for its rendering context
- [ ] **(B)** No PII, credentials, or tokens written to logs
- [ ] **(B)** No dependency with a known Critical CVE, or one listed in the
      [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [ ] **(B)** TLS enforced end to end; no plaintext transport of credentials or personal data
- [ ] **(B)** Errors fail closed and do not leak internal detail to the client
- [ ] **(B)** Authentication and authorization events are logged and alerted on

### 1.5 Evidence

Every `[x]` needs evidence that an auditor can re-check independently. Acceptable evidence:

| Control type | Acceptable evidence |
|---|---|
| Code control | PR link + file:line reference |
| Configuration | Config file excerpt, or screenshot of the setting with timestamp |
| Automated check | CI run URL + job name |
| Process control | Ticket, runbook link, or signed approval |
| Test | Test name + passing CI run |

"I checked it" is not evidence. Record evidence in the finding template in
[CoE Audit Framework §7.2](./coe-audit-framework.md).

---

## 2. OWASP Top 10:2025 Alignment

This checklist is structured so that sections 3 to 12 are the OWASP Top 10:2025 categories in order. Coverage is
therefore structural, not just a mapping table.

| Category | Checklist section | Primary CoE control | Audit evidence |
|---|---|---|---|
| [A01:2025 Broken Access Control](https://owasp.org/Top10/2025/) | §3 | Server-side authz, object ownership checks, SSRF allowlists | Code review + authz tests |
| [A02:2025 Security Misconfiguration](https://owasp.org/Top10/2025/) | §4 | Hardening baseline, security headers, IaC scanning | Config review + scanner report |
| [A03:2025 Software Supply Chain Failures](https://owasp.org/Top10/2025/) | §5 | SCA, lockfiles, pinned CI actions, SBOM, provenance | CI logs + SBOM + attestations |
| [A04:2025 Cryptographic Failures](https://owasp.org/Top10/2025/) | §6 | TLS policy, approved primitives, managed keys | Config review + code review |
| [A05:2025 Injection](https://owasp.org/Top10/2025/) | §7 | Parameterization, allow-listing, contextual encoding | SAST + DAST + code review |
| [A06:2025 Insecure Design](https://owasp.org/Top10/2025/) | §8 | Threat modeling, abuse cases, quotas, safe defaults | Design review + threat model |
| [A07:2025 Authentication Failures](https://owasp.org/Top10/2025/) | §9 | Vetted identity provider, MFA, session rotation | Config + code review |
| [A08:2025 Software or Data Integrity Failures](https://owasp.org/Top10/2025/) | §10 | Signed artifacts, safe deserialization, SRI, webhook signatures | Pipeline review + code review |
| [A09:2025 Security Logging and Alerting Failures](https://owasp.org/Top10/2025/) | §11 | Structured security logs, protected storage, actionable alerts | Log audit + alert test |
| [A10:2025 Mishandling of Exceptional Conditions](https://owasp.org/Top10/2025/) | §12 | Fail-closed defaults, bounded resources, tested failure paths | Code review + failure tests |

### 2.1 What changed from OWASP Top 10:2021

Most Techversant engineers were trained on the 2021 list. This table is the migration note — brief it in the next
team security session.

| 2021 | 2025 | Change |
|---|---|---|
| A01 Broken Access Control | A01 Broken Access Control | Still #1. **SSRF has been merged into this category.** |
| A02 Cryptographic Failures | A04 Cryptographic Failures | Moved down |
| A03 Injection | A05 Injection | Moved down |
| A04 Insecure Design | A06 Insecure Design | Moved down |
| A05 Security Misconfiguration | A02 Security Misconfiguration | **Moved up to #2** |
| A06 Vulnerable and Outdated Components | A03 Software Supply Chain Failures | **Renamed and broadened** |
| A07 Identification and Authentication Failures | A07 Authentication Failures | Renamed |
| A08 Software and Data Integrity Failures | A08 Software or Data Integrity Failures | Supply chain moved to A03 |
| A09 Security Logging and Monitoring Failures | A09 Security Logging and Alerting Failures | **Alerting added** |
| A10 Server-Side Request Forgery | *(merged into A01)* | No longer a standalone category |
| *(new)* | A10 Mishandling of Exceptional Conditions | **New** — error handling, fail-open |

**Three practical consequences for our teams:**

1. Misconfiguration and supply chain now outrank injection. Audit effort should shift accordingly.
2. Error handling is a first-class security category, not a code-quality nicety (§12).
3. "We scan dependencies" no longer satisfies A03 — build and distribution integrity are in scope (§5).

A ColdFusion-specific worked example of all ten categories is available at
[OWASP Top 10:2025 — ColdFusion view](../engineering-academy/cf-consulting/01-coldfusion-deep-expertise/assets/owasp-top-10-2025-coldfusion.svg).

---

## 3. A01:2025 — Broken Access Control

Reference: [Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

### 3.1 Authorization

- [ ] **(B)** Authorization enforced server-side on every protected endpoint and operation
- [ ] **(B)** Deny by default — access requires an explicit grant, not the absence of a denial
- [ ] Authorization checked **after** authentication and **before** any data access
- [ ] Permissions checked, not role name strings (`can('invoice:approve')`, not `role === 'manager'`)
- [ ] Vertical privilege escalation prevented (standard user cannot reach admin functions)
- [ ] Horizontal privilege escalation prevented (user A cannot reach user B's data)
- [ ] Authorization logic centralized, not re-implemented per endpoint
- [ ] UI-level hiding is never the only control — every hidden action is also blocked server-side
- [ ] Static resources and file downloads are access-controlled, not just the pages that link to them

### 3.2 Object-level access and IDOR

Reference: [IDOR Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html)

- [ ] **(B)** Before returning a record, verify the caller is authorized for the **requested action on
      that resource**, including tenant boundaries. Ownership is one input, not the test — it does not
      cover shared records, delegated access, support and admin roles, or service accounts
- [ ] Sequential/guessable identifiers avoided for externally exposed resources (prefer UUID v4)
- [ ] Bulk and export endpoints apply the same ownership checks as single-record endpoints
- [ ] Denied access returns `403 Forbidden`, per
      [RFC 9110 §15.5.4](https://www.rfc-editor.org/rfc/rfc9110.html#section-15.5.4). Substitute `404`
      **only** where the existence of the resource is itself confidential — most commonly across tenant
      boundaries. Whichever rule applies to a resource type, apply it consistently: a `403` on one path
      and a `404` on another for the same resource re-introduces the enumeration leak that `404` prevents

### 3.3 Multi-tenant isolation

Applies to any shared-database or shared-infrastructure product. Mark `N/A` with a reason for single-tenant systems.

- [ ] **(B)** Every query touching tenant data is scoped by tenant identifier at the data-access layer
- [ ] Tenant context derived from the authenticated session — never accepted as a request parameter
- [ ] A cross-tenant access test exists and runs in CI
- [ ] Background jobs, exports, and admin tooling carry tenant scope

### 3.4 Server-Side Request Forgery (SSRF)

Moved here from its standalone 2021 category.
Reference: [SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)

- [ ] **(B)** User-supplied URLs are validated against an allowlist of hosts/schemes, not a denylist
- [ ] Cloud instance metadata endpoints blocked at the network layer (for example `169.254.169.254`)
- [ ] Private, loopback, and link-local IP ranges blocked after DNS resolution, not before
- [ ] Redirects are not followed automatically, or are re-validated at each hop
- [ ] Outbound egress restricted by security group / firewall, not only in application code
- [ ] Response content and status not reflected verbatim to the caller (prevents blind SSRF exfiltration)
- [ ] Features that accept URLs (webhooks, importers, PDF/preview renderers, avatar fetchers) explicitly reviewed

### 3.5 Cross-Site Request Forgery (CSRF)

Reference: [CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

- [ ] State-changing requests protected by anti-CSRF tokens or equivalent
- [ ] Cookies set with `SameSite=Lax` or `Strict`; `None` only with a documented reason
- [ ] `GET` requests never change state
- [ ] Token-based APIs using the `Authorization` header confirmed not to also accept cookie auth

---

## 4. A02:2025 — Security Misconfiguration

Now the #2 risk. Audit effort should reflect that.

### 4.1 Application and server hardening

- [ ] **(B)** Debug mode disabled in all non-development environments
- [ ] **(B)** Default credentials changed on every component (database, admin console, message broker, cache)
- [ ] Administrative consoles not reachable from the public internet
      (ColdFusion Administrator, phpMyAdmin, Actuator, Kibana, and similar)
- [ ] Directory listing disabled
- [ ] Sample, demo, and installer files removed from deployed artifacts
- [ ] Server, framework, and language version banners suppressed
- [ ] Unused features, modules, ports, and HTTP methods disabled
- [ ] Environment parity documented — dev/staging/production differ only by configuration, not by security posture
- [ ] Verbose error pages replaced with generic ones (see §12.1)

### 4.2 Security headers

Reference: [Content Security Policy Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html)
· [MDN HTTP headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers)

| Header | Purpose | Required | Notes |
|---|---|---|---|
| `Strict-Transport-Security` | Force HTTPS | Yes | `max-age=31536000; includeSubDomains` |
| `Content-Security-Policy` | Restrict script/resource origins | Yes | Use nonce or hash; avoid `unsafe-inline` |
| `X-Content-Type-Options` | Prevent MIME sniffing | Yes | `nosniff` |
| `Referrer-Policy` | Limit referrer leakage | Yes | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | Disable unused browser features | Yes | Deny camera/microphone/geolocation by default |
| `Cross-Origin-Opener-Policy` | Process isolation | Yes | `same-origin` |
| `Cross-Origin-Resource-Policy` | Limit cross-origin embedding | Yes | `same-origin` or `same-site` |
| `Cache-Control` | Prevent caching of sensitive responses | Yes | `no-store` on authenticated responses |
| `X-Frame-Options` | Clickjacking protection | Legacy | Prefer CSP `frame-ancestors`; keep for old browsers |
| `X-XSS-Protection` | Legacy XSS auditor | No | **Set to `0` or remove.** Retaining it can introduce risk |

- [ ] Headers verified on **API responses and error responses**, not only on the home page
- [ ] CSP has no `unsafe-eval`, and `unsafe-inline` only with a documented, time-boxed exception
- [ ] CSP `frame-ancestors` configured
      ([Clickjacking Defense](https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html))
- [ ] CSP reporting endpoint configured and monitored

### 4.3 CORS

- [ ] **(B)** No wildcard `Access-Control-Allow-Origin` on endpoints that return authenticated data
- [ ] Origin allowlist is explicit and reviewed; the request `Origin` is never reflected unvalidated
- [ ] `Access-Control-Allow-Credentials: true` never combined with a reflected or wildcard origin
- [ ] Preflight responses cached with a sane `Access-Control-Max-Age`

### 4.4 Cloud and Infrastructure as Code

Reference: [IaC Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Infrastructure_as_Code_Security_Cheat_Sheet.html)

- [ ] **(B)** No storage bucket, database, or cache exposed publicly without documented justification
- [ ] IaC scanned in CI (for example [Trivy](https://trivy.dev/), Checkov) with failures blocking merge
- [ ] Cloud IAM follows least privilege; no wildcard `*` actions on production roles
- [ ] No long-lived static cloud access keys where workload identity / OIDC federation is available
- [ ] Network segmentation enforced — data stores not reachable from the public internet
- [ ] Security group / firewall rules reviewed; no `0.0.0.0/0` on management ports
- [ ] Encryption at rest enabled on all managed data services
- [ ] Cloud audit logging enabled and shipped off-account
- [ ] Backups exist, are encrypted, and **restore has been tested** within the last 6 months

### 4.5 Containers and orchestration

Mark `N/A` with a reason if the team does not deploy containers.
Reference: [Docker Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Docker_Security_Cheat_Sheet.html)
· [Kubernetes Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Kubernetes_Security_Cheat_Sheet.html)

- [ ] Containers run as a non-root user
- [ ] Base images come from a trusted registry and are pinned by digest
- [ ] Images scanned for vulnerabilities in CI before push
- [ ] No secrets baked into image layers or `ENV` instructions
- [ ] Read-only root filesystem and dropped Linux capabilities where feasible
- [ ] Resource limits set on every workload (see also §12.3)
- [ ] Kubernetes RBAC least-privileged; default service account tokens not auto-mounted

### 4.6 Access and account hygiene

- [ ] Production access follows least privilege and is reviewed quarterly
- [ ] Privileged access (production, cloud console, database, repository admin) requires MFA
- [ ] Offboarding revokes all access within 24 hours, including tokens and SSH keys
- [ ] Shared accounts eliminated, or justified with compensating controls and logged usage
- [ ] Repository branch protection enforced per
      [Techversant Git Workflow](../git/Techversant_Git_Workflow.md)

---

## 5. A03:2025 — Software Supply Chain Failures

New and broadened category. Dependency scanning alone no longer satisfies it — how software is **built,
distributed, and updated** is in scope.
Reference: [Vulnerable Dependency Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Vulnerable_Dependency_Management_Cheat_Sheet.html)

### 5.1 Dependency hygiene

- [ ] **(B)** No dependency with a known Critical CVE, or one listed in the
      [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [ ] Software Composition Analysis runs in CI on every commit
      ([Dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-alerts/about-dependabot-alerts),
      Snyk, `npm audit`, `composer audit`, or equivalent)
- [ ] Lockfile committed and CI installs from the lockfile (`npm ci`, `composer install --no-dev`)
- [ ] Transitive dependencies are in scope of scanning, not just direct ones
- [ ] New dependencies reviewed for maintenance status, license, and maintainer count before adoption
- [ ] Dependency confusion prevented — internal package names reserved or scoped to a private registry
- [ ] Package install scripts (`postinstall` and equivalents) reviewed or disabled in CI
- [ ] Unsupported runtimes and frameworks tracked with an upgrade plan
      (end-of-life ColdFusion, PHP, Node.js, JDK versions)
- [ ] Outdated-package review performed at least monthly

### 5.2 Build and CI/CD pipeline security

Reference: [CI/CD Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/CI_CD_Security_Cheat_Sheet.html)
· [GitHub Actions hardening](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions)

- [ ] **(B)** CI secrets stored in the platform secret store — never in workflow YAML or repository files
- [ ] Third-party CI actions/plugins pinned to a full commit SHA, not a mutable tag
- [ ] Pipeline tokens scoped to least privilege and short-lived
- [ ] Workflows from forked pull requests cannot access secrets
- [ ] Build runners are ephemeral, or are hardened and patched if self-hosted
- [ ] Only the pipeline can deploy to production — no manual artifact uploads
- [ ] Pipeline configuration changes require the same review as application code
- [ ] Build logs checked for secret leakage; masking verified

### 5.3 Artifact integrity and provenance

Reference: [SLSA](https://slsa.dev/) · [Sigstore](https://www.sigstore.dev/)

- [ ] Build artifacts are signed, or provenance attestations are generated
- [ ] Deployment verifies artifact signature/digest before release
- [ ] Artifacts are immutable once published; no in-place overwrite of a released version
- [ ] Release tags are protected and traceable to a reviewed commit

### 5.4 SBOM

- [ ] SBOM generated per release in [CycloneDX](https://cyclonedx.org/) or [SPDX](https://spdx.dev/) format
- [ ] SBOM stored with the release artifact and retained per the evidence policy
- [ ] SBOM is used — it is re-checked against new advisories, not just produced

### 5.5 Third-party services and vendors

- [ ] Third-party processors inventoried, with a signed Data Processing Agreement where personal data is involved
- [ ] Vendor security posture reviewed annually for services in the critical path
- [ ] Third-party JavaScript inventoried and justified
      ([Third Party JavaScript Management](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html))
- [ ] A documented plan exists for revoking a compromised third-party integration

---

## 6. A04:2025 — Cryptographic Failures

Reference: [Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html)
· [Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html)

### 6.1 Data in transit

- [ ] **(B)** TLS 1.2 minimum everywhere; TLS 1.3 preferred. TLS 1.0/1.1 and SSL disabled
- [ ] **(B)** HTTP redirects to HTTPS, and HSTS is set (§4.2)
- [ ] Certificate validation enabled on **all** outbound connections — no disabled verification anywhere in code
- [ ] No self-signed or expired certificates in production
- [ ] Certificate expiry monitored with alerting ahead of renewal
- [ ] Internal service-to-service traffic encrypted, not only edge traffic

### 6.2 Data at rest

- [ ] **(B)** Data classified as Confidential or Restricted is encrypted at rest (AES-256 or equivalent)
- [ ] Backups and database snapshots encrypted with the same strength as the primary store
- [ ] Full disk encryption is not treated as sufficient for field-level sensitive data
- [ ] Data classification documented per data store (Public / Internal / Confidential / Restricted)

### 6.3 Keys and secrets management

Reference: [Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)

- [ ] **(B)** No secrets in source code, configuration files, or `.env` files committed to version control
- [ ] **(B)** Secret scanning runs in CI on every commit
      ([Gitleaks](https://github.com/gitleaks/gitleaks), [TruffleHog](https://github.com/trufflesecurity/trufflehog))
- [ ] Secret scanning covers **git history**, not only the current working tree
- [ ] Secrets held in a managed secret store (AWS Secrets Manager, Azure Key Vault, HashiCorp Vault)
- [ ] Key rotation policy defined, with a documented rotation interval per secret type
- [ ] A documented, rehearsed revocation procedure exists for a leaked credential
- [ ] Any historically committed secret has been **revoked**, not merely deleted from the tree
- [ ] Encryption keys separated from the data they protect, with restricted key access
- [ ] Crypto agility documented — algorithms are configurable, and long-lived encrypted data is inventoried
      for future post-quantum migration

### 6.4 Password and credential storage

Reference: [Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
· [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html)

#### Length

Length requirements depend on whether the password stands alone. Both are `SHALL` in
[SP 800-63B-4 §3.1.1.2](https://pages.nist.gov/800-63-4/sp800-63b.html).

| Use | Minimum |
|---|---|
| Password as the **only** authentication factor | **15 characters** |
| Password as **one factor within MFA** | 8 characters |

- [ ] **(B)** Single-factor passwords are at least 15 characters
- [ ] Passwords inside an MFA flow are at least 8 characters
- [ ] Maximum length permits at least 64 characters; long passphrases accepted
- [ ] All printable ASCII plus space accepted; Unicode accepted, each code point counting as one character

#### Hashing

Naming an algorithm is not a strength claim — the work factor is what makes it strong. Record the
parameters in use and review them annually.

| Algorithm | Status | Minimum parameters |
|---|---|---|
| **Argon2id** | Preferred | 19 MiB memory, 2 iterations, 1 degree of parallelism (or stronger) |
| **scrypt** | Acceptable | N = 2^17, r = 8, p = 1 (or stronger) |
| **bcrypt** | Legacy only | cost ≥ 10; **pre-hash inputs over 72 bytes** — bcrypt silently truncates beyond that |

- [ ] **(B)** Passwords hashed with Argon2id, scrypt, or bcrypt. Never MD5, SHA-1, or plain SHA-256
- [ ] **(B)** Parameters meet or exceed the table above, and the values in use are documented
- [ ] Per-user salt applied (handled automatically by the algorithms above)
- [ ] Where bcrypt is retained, long inputs are pre-hashed so nothing is silently truncated
- [ ] Hashing parameters reviewed annually against current guidance

#### Policy

- [ ] Passwords checked against a breached-password list
- [ ] **No forced periodic password expiry** — current NIST guidance advises against it. Rotate on evidence of
      compromise instead. *(This reverses the v1.0 guidance in this document.)*
- [ ] **No composition rules** — SP 800-63B-4 makes this a `SHALL NOT`. Do not require character-type mixes

---

## 7. A05:2025 — Injection

Reference: [Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html)

### 7.1 Input validation

- [ ] **(B)** All input validated server-side at the trust boundary — type, length, format, range, allowed values
- [ ] Server-side validation is independent of, and never replaced by, client-side validation
- [ ] Validation is allow-list based wherever the set of valid values is known
- [ ] Validation applied to **all** input sources: body, query string, path, headers, cookies, file contents,
      message queues, and third-party callbacks
- [ ] Mass assignment prevented — request fields explicitly bound, not auto-mapped to models
      ([Mass Assignment Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mass_Assignment_Cheat_Sheet.html))

### 7.2 SQL and data store injection

Reference: [SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
· [Database Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html)

- [ ] **(B)** All queries parameterized — no string concatenation or interpolation, even for values believed safe
- [ ] Dynamic identifiers (table, column, sort direction) resolved through an allow-list, never interpolated
- [ ] Stored procedures also use bound parameters internally
- [ ] ORM raw-query escape hatches audited individually
- [ ] NoSQL query construction reviewed for operator injection (for example a `$where` or `$ne` payload)
- [ ] Application database account has least privilege — no `DROP`, no schema rights in production

### 7.3 Cross-site scripting and output encoding

Reference: [XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

- [ ] **(B)** Output encoded for its context — HTML body, attribute, JavaScript, URL, or CSS
- [ ] Framework auto-escaping left enabled; every bypass reviewed
      (`dangerouslySetInnerHTML`, `v-html`, `|raw`, `WriteOutput` of unescaped input)
- [ ] User-supplied HTML sanitized with a maintained library, never with a hand-written regex
- [ ] No `eval`, `Function()`, dynamic `include`, or template evaluation on user input
- [ ] JSON responses served with `Content-Type: application/json`, not `text/html`
- [ ] Redirect targets validated against an allow-list (prevents open redirect)
- [ ] DOM-based sinks reviewed (`innerHTML`, `document.write`, `location`, `postMessage` handlers)

### 7.4 Command, template, and other injection contexts

| Context | Required control |
|---|---|
| OS command | Never build a shell string from input; use argument arrays and an allow-list of commands |
| LDAP | Escape per LDAP rules; bind with parameterized filters |
| XPath / XQuery | Parameterized expressions; no string building |
| Template engines | No user input compiled as a template (server-side template injection) |
| Expression languages | User input never evaluated as an expression |
| XML | External entity resolution disabled (XXE); DTD processing off |
| HTTP headers | CR/LF stripped from any value derived from input (response splitting) |
| Log entries | Newlines and control characters neutralized before writing (log injection) |
| Email headers | CR/LF stripped from address and subject fields |

- [ ] Each context above verified or marked `N/A` with a reason

### 7.5 File upload

Reference: [File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html)

File upload defense is layered. No single check is sufficient — a forged file signature defeats
content sniffing, and an allowed extension says nothing about the bytes inside.

- [ ] **(B)** Extension checked against an **allowlist** of permitted types (never a denylist)
- [ ] **(B)** File content inspected and consistent with the claimed type
- [ ] **(B)** Client-supplied MIME type never trusted as the basis for any decision
- [ ] Filename length, character set, and Unicode normalization constrained before use
- [ ] Size limits enforced before the file is processed or persisted
- [ ] Uploads stored outside the web root, or on separate storage, and never executed
- [ ] Stored filenames generated by the server; original names never used as paths (path traversal)
- [ ] Archive extraction bounded — no zip-slip, no unbounded decompression
- [ ] Malware scanning applied where files are shared between users
- [ ] Uploads served from a separate origin or with `Content-Disposition: attachment` and `nosniff`

---

## 8. A06:2025 — Insecure Design

Reference: [Threat Modeling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html)
· [OWASP Proactive Controls](https://owasp.org/www-project-proactive-controls/)

### 8.1 Threat modeling

- [ ] Threat model exists for the system and is refreshed when architecture changes materially
- [ ] Trust boundaries documented — where untrusted data enters and where privilege changes
- [ ] Security requirements captured in the specification, not retrofitted at review
- [ ] Security review triggered for changes listed in
      [Secure Engineering — Security Review Triggers](../engineering-academy/00-engineering-foundations/03-secure-engineering.md)
- [ ] The [security-engineer skill](../ai/claude/skills/security-engineer/SKILL.md) or an equivalent structured
      method is used for the STRIDE pass

### 8.2 Business logic and abuse cases

Often missed because each individual request is technically valid.

- [ ] Abuse cases documented alongside use cases ("how would someone misuse this?")
- [ ] Workflow state machine enforced server-side — steps cannot be skipped or replayed out of order
- [ ] Quantity, price, and discount fields validated server-side; negative and zero values considered
- [ ] Time-of-check/time-of-use race conditions considered on balance, stock, and quota operations
- [ ] Idempotency enforced on financially or legally significant writes
      ([REST API Best Practices](../general/rest-api-best-practices.md))
- [ ] Bulk or automated abuse considered (mass signup, scraping, enumeration, coupon farming)
- [ ] Account enumeration prevented — login, registration, and reset responses do not reveal account existence

### 8.3 Rate limiting and quotas

Reference: [Denial of Service Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html)

- [ ] **(B)** Authentication endpoints throttled with progressive delays as failures accumulate
- [ ] **(B)** Any account lockout is **temporary and self-clearing**. A lockout that persists until an
      administrator intervenes is a denial-of-service primitive: an attacker who knows a username can
      lock the owner out on demand
- [ ] Throttling keyed on more than the username alone (source address, device, and reputation signals),
      so one attacker cannot lock out arbitrary accounts
- [ ] A self-service recovery path exists that does not depend on the locked factor
- [ ] Lockout events logged and alerted on — a spike is an attack indicator, not routine noise (§11.4)
- [ ] Write endpoints rate-limited per user and per IP
- [ ] Expensive operations (search, export, report, AI inference) have their own tighter limits
- [ ] Per-tenant or per-account quotas prevent one customer exhausting shared capacity
- [ ] Rate limit responses use `429` with `Retry-After`

### 8.4 Privacy by design

- [ ] Privacy impact assessed before new personal data processing begins
- [ ] Data minimization applied — every collected field has a documented purpose
- [ ] Secure defaults — the most private setting is the default
- [ ] Retention period defined for each data category at design time (see §16)

---

## 9. A07:2025 — Authentication Failures

Reference: [Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html)

### 9.1 Authentication controls

- [ ] **(B)** No hardcoded or default credentials anywhere in the codebase or configuration
- [ ] A vetted identity library or provider is used — authentication is not hand-rolled
- [ ] **(B)** Failed login attempts throttled and logged, with any lockout temporary and self-clearing
      (§8.3 — a permanent lockout is a denial-of-service primitive)
- [ ] Credential stuffing defenses in place (breach-list checks, device/IP anomaly detection, or CAPTCHA)
- [ ] Authentication errors are generic — they never reveal whether the account exists
- [ ] No credentials transmitted in URLs, query strings, or logs

### 9.2 Multi-factor authentication

- [ ] **(B)** MFA enforced for administrative and production access
- [ ] MFA available to all end users where the product handles personal or financial data
- [ ] Phishing-resistant factors (WebAuthn/passkeys, hardware keys) offered for privileged roles
- [ ] SMS used only as a fallback, with the risk documented
- [ ] MFA re-prompted on sensitive operations, not only at login
- [ ] MFA recovery codes issued, hashed at rest, and single-use

### 9.3 Session management

Reference: [Session Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)

- [ ] **(B)** Session identifiers are cryptographically random and of sufficient length
- [ ] **(B)** Session regenerated on login and on any privilege change (session fixation defense)
- [ ] Both idle timeout and absolute timeout enforced
- [ ] Logout invalidates the session server-side, not only in the browser
- [ ] Cookies set `Secure`, `HttpOnly`, and `SameSite`
- [ ] Session state held server-side where revocation matters; tokens are not stored in `localStorage`
- [ ] Concurrent session policy defined; users can view and revoke active sessions
- [ ] Password change or reset invalidates all other active sessions

### 9.4 Tokens — JWT, OAuth 2.0, OIDC

Reference: [OAuth 2.0 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OAuth2_Cheat_Sheet.html)
· [RFC 9700 — OAuth 2.0 Security Best Current Practice](https://datatracker.ietf.org/doc/html/rfc9700)

- [ ] **(B)** JWT algorithm pinned server-side; `alg: none` and algorithm substitution rejected
- [ ] Signature verified before any claim is read
- [ ] `iss`, `aud`, `exp`, and `nbf` all validated
- [ ] `kid` header treated as untrusted input — never used to build a file path or URL
- [ ] Access token lifetime short (15–60 minutes); refresh tokens rotated with reuse detection
- [ ] A revocation path exists — deny-list, short lifetimes, or server-side session lookup
- [ ] Authorization Code flow with PKCE used for all public clients; implicit flow not used
- [ ] `state` parameter validated on the callback (CSRF defense)
- [ ] Redirect URIs matched exactly against a registered allow-list — no wildcard or prefix matching
- [ ] Tokens never placed in URLs, logs, or analytics events

### 9.5 Account recovery

Reference: [Forgot Password Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)

- [ ] Reset tokens are random, single-use, short-lived, and hashed at rest
- [ ] Reset response is identical whether or not the account exists
- [ ] Reset flow rate-limited
- [ ] Security questions not used as a sole recovery factor
- [ ] The user is notified out-of-band on password, email, or MFA change

### 9.6 Machine and service identity

- [ ] Service-to-service authentication uses short-lived credentials or workload identity, not shared static keys
- [ ] API keys are scoped, individually revocable, and attributable to an owner
- [ ] API keys hashed at rest, shown to the user once at creation
- [ ] Unused service accounts and API keys reviewed and removed quarterly

---

## 10. A08:2025 — Software or Data Integrity Failures

Distinct from A03: this is about trusting **untrusted code or data at runtime**, at a lower level than the supply
chain itself.

### 10.1 Code and configuration integrity

- [ ] Application does not load code, plugins, or configuration from an unverified remote source
- [ ] Auto-update mechanisms verify a signature before applying an update
- [ ] Configuration changes are version-controlled and reviewed
- [ ] Critical data has integrity protection where tampering is a realistic threat (signed or hash-verified)

### 10.2 Deserialization and untrusted structured data

- [ ] **(B)** Native/binary deserialization is never applied to untrusted input
      (`unserialize`, `pickle`, Java native serialization, `ObjectInputStream`)
- [ ] Structured formats parsed with safe settings — no type resolution from the payload
- [ ] XML parsers configured with external entity resolution disabled (see §7.4)
- [ ] YAML parsed in safe mode
- [ ] Deserialized objects validated against a schema before use

### 10.3 Client-side integrity

- [ ] Third-party scripts loaded with Subresource Integrity where the source is not fully controlled
- [ ] Scripts loaded from an owned or contractually governed origin; no unpinned public CDN for critical paths
- [ ] Payment and authentication pages carry the strictest script policy
- [ ] `postMessage` handlers validate `origin` before acting on the message

### 10.4 Inbound integrations and webhooks

- [ ] **(B)** Inbound webhooks verify a cryptographic signature before processing
- [ ] Timestamp checked and replay window enforced
- [ ] Signature comparison uses a constant-time function
- [ ] Webhook handlers are idempotent
- [ ] Imported or synchronized third-party data is validated, not trusted because of its source

---

## 11. A09:2025 — Security Logging and Alerting Failures

Renamed for 2025: producing logs is not enough — someone or something must be **alerted**.
Reference: [Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
· [Application Logging Vocabulary](https://cheatsheetseries.owasp.org/cheatsheets/Application_Logging_Vocabulary_Cheat_Sheet.html)

### 11.1 What must be logged

- [ ] **(B)** Authentication attempts — both success and failure
- [ ] **(B)** Authorization failures
- [ ] Input validation failures
- [ ] Administrative and privileged actions, with actor, action, target, and timestamp
- [ ] Changes to permissions, roles, and account state
- [ ] Data export, bulk read, and download events
- [ ] Secret and key access where the platform supports it
- [ ] Every entry carries correlation context (trace/request ID, user ID, tenant ID)
- [ ] Logs are structured (JSON) and timestamps are ISO 8601 UTC

### 11.2 What must never be logged

- [ ] **(B)** Passwords, in any form
- [ ] **(B)** Session tokens, API keys, and secrets
- [ ] **(B)** Full payment card numbers or equivalent financial identifiers
- [ ] PII masked or omitted — email, phone, address, national identifiers
- [ ] Request and response bodies not logged by default on endpoints handling personal data
- [ ] Log redaction verified by test, not just by policy

### 11.3 Log protection and retention

- [ ] Logs shipped off-host to storage the application cannot modify
- [ ] Log storage access-controlled and tamper-evident
- [ ] Retention period defined and enforced (12 months minimum where ISO 27001 applies)
- [ ] Clock synchronization in place across hosts

### 11.4 Alerting and detection

The 2025 addition. A log nobody reads is not a control.

- [ ] **(B)** Alerts configured for repeated authentication failure and for authorization-failure spikes
- [ ] Alerts configured for privilege escalation and new admin account creation
- [ ] Alerts configured for anomalous data export volume
- [ ] Each alert has a named owner and a documented response action
- [ ] Alert routing tested within the last quarter — an alert has actually reached a human
- [ ] Alert noise reviewed; chronically ignored alerts are fixed or removed
- [ ] Error and exception monitoring is in place and triaged, not just collected

### 11.5 Incident readiness

- [ ] Incident response playbook documented, with severity classification
- [ ] On-call or escalation path defined and current
- [ ] Breach notification process defined
      (GDPR: supervisory authority within 72 hours of discovery, where applicable)
- [ ] Post-incident review conducted for every major incident, with actions tracked
- [ ] A security contact is publicly discoverable for external reporters
      ([security.txt](https://securitytxt.org/))
- [ ] **(B)** Internal reporters know that vulnerabilities in Techversant or client systems go to the
      Security Lead directly, never to a public tracker, regardless of severity (§18.4)

---

## 12. A10:2025 — Mishandling of Exceptional Conditions

**New category for 2025.** Covers improper error handling, logic errors on failure paths, failing open, and
unbounded resource consumption. Historically treated as a code-quality concern; it is now a named security risk.
Reference: [Error Handling Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html)

### 12.1 Error handling

- [ ] **(B)** Errors returned to clients are generic — no stack traces, SQL text, file paths, or internal hostnames
- [ ] Detailed diagnostics logged server-side with full context (§11.1)
- [ ] A correlation/error ID is returned to the user so support can trace the event
- [ ] Custom error pages configured for 4xx and 5xx at the web server layer as well as the application
- [ ] Unhandled exceptions caught at a top-level boundary and logged
- [ ] **(B)** No empty catch blocks — every caught error is handled, re-thrown, or logged with context
- [ ] Error message content does not differ in a way that leaks state (timing or wording oracles)

### 12.2 Fail-closed behavior

- [ ] **(B)** Security decisions fail closed — if an authorization, token, or policy check errors, access is denied
- [ ] Dependency unavailability (identity provider, permission service, feature flag store) denies rather
      than defaults to allow
- [ ] Fallback and degraded modes reviewed for the privileges they grant
- [ ] Circuit breakers and retries do not bypass validation or authorization on the retry path
- [ ] Feature flag default values are the safe values

### 12.3 Resource exhaustion and limits

- [ ] Timeouts set on every outbound call — database, HTTP, queue, cache
- [ ] Request body size limits enforced at the edge and in the application
- [ ] Pagination mandatory on collection endpoints; unbounded result sets rejected
- [ ] Query complexity/depth limited where the API allows client-shaped queries
- [ ] Regular expressions reviewed for catastrophic backtracking on user input
- [ ] Recursion, loop, and batch sizes bounded
- [ ] Memory and CPU limits set on workloads (§4.5)
- [ ] Connection pools bounded, with exhaustion behavior defined

### 12.4 Concurrency and partial failure

- [ ] Multi-step operations are transactional, or have a defined compensating action
- [ ] Partial failure cannot leave a record in a state that grants unintended access
- [ ] Concurrent updates protected by optimistic locking or equivalent
- [ ] Background job failures are visible, retried safely, and idempotent
- [ ] Failure paths are covered by tests, not only happy paths

---

## 13. API Security

Cross-cutting. Applies alongside sections 3 to 12.
Reference: [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
· [REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
· CoE: [REST API Best Practices](../general/rest-api-best-practices.md)

### 13.1 General API controls

- [ ] **(B)** Authentication required on all non-public endpoints; public endpoints explicitly documented as such
- [ ] **(B)** Authorization checked per request, including object-level ownership (§3.2)
- [ ] Rate limiting and request size limits enforced (§8.3, §12.3)
- [ ] CORS configured with an explicit allowlist (§4.3)
- [ ] No sensitive data in query parameters or path segments
- [ ] Responses return only the fields the caller needs — no over-fetching of internal fields
- [ ] Sensitive fields excluded at the data layer, not filtered in the presentation layer
- [ ] API versioning implemented; deprecation communicated before removal
- [ ] Error envelope consistent and free of internal detail
- [ ] API inventory maintained — no undocumented or forgotten endpoints (shadow/zombie APIs)
- [ ] Non-production API instances are not internet-reachable with production data

### 13.2 GraphQL and flexible query APIs

Mark `N/A` with a reason where not used.

- [ ] Introspection disabled in production
- [ ] Query depth, complexity, and cost limits enforced
- [ ] Batching abuse limited
- [ ] Field-level authorization applied, not only at the resolver root

---

## 14. AI and LLM Security

New in v2.0. Techversant uses AI-assisted development across teams, and increasingly ships AI features.
This section is mandatory for any team using AI coding tools; §14.2 and §14.3 apply to any team shipping an
AI-backed feature.

CoE references: [Neural Security Guidelines](../neural/neural-security-guidelines.md)
· [AI Era Coding Guidelines](../general/ai-era-coding-guidelines.md)
· [AI Team Best Practices](../ai/ai-team-best-practices.md)
External: [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
· [LLM Prompt Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html)

### 14.1 AI-assisted development

- [ ] **(B)** No secrets, credentials, customer data, or PII pasted into AI prompts or tools
- [ ] **(B)** AI-generated code covering authentication, authorization, cryptography, or personal data is
      reviewed by a senior engineer (Red Zone rule, per
      [AI Era Coding Guidelines](../general/ai-era-coding-guidelines.md))
- [ ] AI usage disclosed on pull requests per the CoE standard
- [ ] AI-suggested dependencies verified to exist and to be the intended package before installation
      (guards against hallucinated-package typosquatting)
- [ ] AI-generated code is covered by tests written or reviewed by a human
- [ ] Approved AI tools list maintained; data-retention terms of each tool reviewed
- [ ] Client contractual restrictions on AI usage checked before use on that codebase

### 14.2 LLM application security

- [ ] Prompt injection treated as untrusted input — model output is never implicitly trusted
- [ ] Retrieved and third-party content is delimited and labelled as untrusted in the prompt
- [ ] Model output validated and encoded before rendering, storing, or executing (§7.3)
- [ ] Model output never used directly to build SQL, shell commands, or file paths
- [ ] System prompts contain no secrets and are not treated as a confidentiality boundary
- [ ] Output filtering applied for harmful, leaked, or out-of-scope content
- [ ] Per-user and per-tenant quotas on inference calls (cost and abuse control, §8.3)
- [ ] Model and provider inventory maintained, including data residency and retention terms
- [ ] Training or fine-tuning data governed per [Neural Security Guidelines](../neural/neural-security-guidelines.md)

### 14.3 Agents, tools, and MCP integrations

- [ ] Agent tool permissions least-privileged and explicitly enumerated
- [ ] Destructive or outward-facing actions require human confirmation
- [ ] Agent actions are logged and attributable (§11.1)
- [ ] Third-party MCP servers and plugins reviewed before connection; provenance verified (§5.5)
- [ ] Agent network egress restricted (§3.4)
- [ ] Blast radius bounded — agent credentials are scoped and revocable

---

## 15. Mobile Application Security

Mark the whole section `N/A` with a reason for teams that ship no mobile application.
Reference: [OWASP MASVS](https://owasp.org/www-project-mobile-app-security/)
· [Mobile Application Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Mobile_Application_Security_Cheat_Sheet.html)

- [ ] **(B)** No secrets, API keys, or credentials embedded in the app binary or bundle
- [ ] Sensitive data stored in the platform keystore/keychain, not in shared preferences or plain files
- [ ] Certificate validation enforced; pinning considered for high-value flows
- [ ] The backend re-validates everything — client-side checks are treated as advisory only
- [ ] Deep links and custom URL schemes validated and authorized
- [ ] Screenshots, clipboard, and backup exposure of sensitive screens considered
- [ ] Logging disabled or redacted in release builds
- [ ] Third-party SDKs inventoried, with the data they collect documented (§5.5)
- [ ] Root/jailbreak and tamper posture decided and documented

---

## 16. Privacy and Data Protection

Applies where the system processes personal data. Reference: [GDPR text](https://gdpr-info.eu/)
· CoE: [Compliance Auditor skill](../ai/claude/skills/compliance-auditor/SKILL.md)

### 16.1 Lawful basis and consent

- [ ] Lawful basis documented for each processing activity
- [ ] Where consent is the basis, it is freely given, specific, informed, and unambiguous
- [ ] Consent records capture timestamp, mechanism, and the notice version shown
- [ ] Consent withdrawal is as easy as giving it

### 16.2 Data subject rights

- [ ] Access — users can obtain their personal data in a machine-readable format
- [ ] Rectification — users can correct inaccurate data
- [ ] Erasure — deletion cascades to related records, backups policy documented; a `deleted_at` flag alone is
      not erasure
- [ ] Portability — export available as JSON or CSV
- [ ] Requests can be fulfilled within 30 days, with a documented owner and process

### 16.3 Handling and retention

- [ ] **(B)** No PII in logs, URLs, error messages, or analytics events
- [ ] PII fields identified, classified, and inventoried per data store
- [ ] Data minimization applied — no field collected "just in case"
- [ ] Special-category data collected only where explicitly required and documented
- [ ] Retention period defined per data category, with automated purge or anonymization at expiry
- [ ] Backups subject to the same retention rules
- [ ] Cross-border transfer mechanism documented where data leaves its origin region
- [ ] Test and staging environments do not contain unmasked production personal data

---

## 17. Security Testing Requirements

| Test type | Frequency | Tool examples | Owner |
|---|---|---|---|
| **SAST** | Every PR | [Semgrep](https://semgrep.dev/), SonarQube, ESLint security rules | CI/CD |
| **SCA (dependencies)** | Every commit | Dependabot, Snyk, `npm audit`, `composer audit` | CI/CD |
| **Secret scanning** | Every commit + full history | [Gitleaks](https://github.com/gitleaks/gitleaks), [TruffleHog](https://github.com/trufflesecurity/trufflehog) | CI/CD |
| **IaC scanning** | Every PR touching infrastructure | [Trivy](https://trivy.dev/), Checkov | CI/CD |
| **Container image scanning** | Every image build | Trivy, Grype | CI/CD |
| **DAST** | Monthly, and per release | [OWASP ZAP](https://www.zaproxy.org/), Burp Suite | Security team |
| **Authenticated DAST** | Per release | ZAP with session context | Security team |
| **Security unit/integration tests** | Every PR | Authz, tenant isolation, and failure-path tests | Development team |
| **Manual security review** | Per release, and on Red Zone changes | This checklist | Audit team |
| **Penetration test** | Annually, and before major releases | External tester | Security Lead |
| **Supply chain posture** | Quarterly | [OpenSSF Scorecard](https://openssf.org/projects/scorecard/) | CoE |

### 17.1 Test coverage requirements

Every protected feature ships with, at minimum:

- [ ] A test proving unauthenticated access is rejected (`401`)
- [ ] A test proving an authenticated but unauthorized user is rejected (`403` or `404`)
- [ ] A test proving cross-account or cross-tenant access is rejected
- [ ] A test covering at least one failure path (§12.4)

---

## 18. Vulnerability Management and Response

### 18.1 Prioritization

Severity uses [CVSS v4.0](https://www.first.org/cvss/v4-0/) as the base score, adjusted by exploitability context:

- **Escalate one level** if the vulnerability appears in the
  [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — known exploited in the wild
- **Escalate one level** if the affected component is internet-facing and handles personal or financial data
- **Consider [EPSS](https://www.first.org/epss/)** when triaging a large backlog of Medium findings
- **De-escalate** only with a documented compensating control, approved by the Security Lead

### 18.2 SLAs

> **This table is the single authoritative deadline for security vulnerabilities.** Where any other
> CoE document states a different figure for a vulnerability, this one governs.
> [CoE Audit Framework §5.1 and §10.3](./coe-audit-framework.md) cover **audit findings** — process,
> quality and compliance deviations — which are a different class of finding with different deadlines.
> A finding that is both takes the **stricter** of the two.

Three clocks, not one. They run concurrently from the moment the report is received.

| Severity | Acknowledge | Contain | Remediate |
|---|---|---|---|
| Critical (CVSS 9.0–10.0) | 24 hours | 72 hours | 7 days |
| High (CVSS 7.0–8.9) | 48 hours | 7 days | 30 days |
| Medium (CVSS 4.0–6.9) | 1 week | 30 days | 90 days |
| Low (CVSS < 4.0) | Next sprint | N/A | Next release |
| **KEV-listed, any score** | 24 hours | 72 hours | 7 days |

| Clock | Means |
|---|---|
| **Acknowledge** | A named owner has the report, has confirmed it is real, and has assigned severity per §18.1 |
| **Contain** | Exploitation blocked or materially reduced by a compensating control. Not the fix |
| **Remediate** | The root cause is fixed, tested, deployed, and covered by a regression test |

Containment stops the clock on exposure, not on remediation. Shipping a mitigation does **not**
extend the remediate deadline.

#### How this interacts with release blockers

The `(B)` markers in this document and the checklist gate **releases**. These SLAs gate **calendar
time**. They are independent, and the tighter one wins:

- A `(B)` item that is open blocks the release **regardless** of how much SLA time remains.
- An SLA that expires requires remediation **even if no release is planned**. "We are not shipping"
  is not an extension.
- A Critical or KEV-listed vulnerability found in a release candidate blocks that release outright.
- Missing an SLA requires a written exception per
  [CoE Audit Framework §8](./coe-audit-framework.md), approved by the Security Lead, with a
  compensating control and a fixed expiry date. Exceptions do not renew silently.

### 18.3 Response process

1. **Triage** — verify, assess impact and reachability, assign severity per §18.1
2. **Contain** — apply an immediate fix or a compensating control
3. **Remediate** — develop, test, and deploy the fix
4. **Verify** — confirm the original reproduction no longer succeeds; add a regression test
5. **Review** — post-incident review, update controls, record the lesson

### 18.4 Reporting a vulnerability

**This repository is public.** Route by *what* the finding is about, not by how urgent it feels.

| What you found | Route |
|---|---|
| A vulnerability in any Techversant or client system | **Security Lead, directly.** Never a GitHub issue |
| An active incident or live exploitation | **Security Lead, immediately** |
| A gap in these standards documents | [Security Issue template](../.github/ISSUE_TEMPLATE/security-issue.md) |
| An audit finding against a project | [Audit Finding template](../.github/ISSUE_TEMPLATE/audit-finding.md) |
| External reporter | Published security contact ([security.txt](https://securitytxt.org/)) |

If unsure which row applies, treat it as the first and ask. Over-reporting privately costs a message;
under-reporting publicly cannot be undone.

---

## 19. Compliance Mapping

This checklist provides the technical evidence for the compliance obligations tracked in
[CoE Audit Framework §3](./coe-audit-framework.md).

### 19.1 ISO/IEC 27001:2022 Annex A

| Annex A theme | Representative controls | Checklist sections |
|---|---|---|
| Organizational (A.5) | Supplier security, threat intelligence, incident management | §5.5, §11.5, §18 |
| People (A.6) | Access on employment change, security awareness | §4.6, §20.2 |
| Physical (A.7) | Out of scope for application audit — covered by facilities policy | N/A |
| Technological (A.8) | Access control, cryptography, secure development, logging | §3 to §12, §17, §18 |

### 19.2 GDPR

| Requirement | Checklist section |
|---|---|
| Lawful basis and consent | §16.1 |
| Data subject rights | §16.2 |
| Data minimization and retention | §16.3, §8.4 |
| Security of processing (Art. 32) | §6, §11, §17 |
| Processor agreements | §5.5 |
| Breach notification | §11.5 |

### 19.3 SOC 2

| Trust services criterion | Checklist section |
|---|---|
| Security | §3, §4, §5, §6, §9 |
| Availability | §12.3, §4.4 (backup and restore) |
| Processing integrity | §7, §10, §12.4 |
| Confidentiality | §6, §11.2 |
| Privacy | §16 |

---

## 20. Quick Reference Cards

### 20.1 Secrets never in code

```text
WRONG  $apiKey = "sk_live_abc123";
WRONG  connectionString = "Server=...;User=admin;Password=secret";
WRONG  const JWT_SECRET = "my-secret-key";
WRONG  committing a .env file containing real values

RIGHT  Read from a managed secret store at runtime
RIGHT  AWS Secrets Manager, Azure Key Vault, HashiCorp Vault
RIGHT  Commit .env.example with placeholder values only
RIGHT  If a secret was ever committed: revoke and rotate it, do not just delete the line
```

### 20.2 Input validation and output encoding

```text
VALIDATE  type, length, format, range, allowed values — server-side, at the boundary
PREFER    allow-lists over deny-lists
ENCODE    at the point of output, for the specific context (HTML / attribute / JS / URL / CSS)
REJECT    unexpected formats, excessive length, unknown fields

NEVER     trust client-side validation alone
NEVER     concatenate input into SQL, shell commands, templates, or file paths
NEVER     trust model output from an LLM any more than you trust user input
```

### 20.3 Security headers baseline

```text
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: default-src 'self'; frame-ancestors 'none'; object-src 'none'
X-Content-Type-Options: nosniff
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Resource-Policy: same-origin
Cache-Control: no-store          (on authenticated responses)
```

### 20.4 The five questions for any pull request

```text
1. What untrusted input enters here, and where is it validated?
2. Who is allowed to do this, and where is that checked server-side?
3. What happens when this fails — does it fail closed?
4. What does this log, and does it leak anything it should not?
5. What new dependency, service, or permission does this introduce?
```

---

## 21. Related Documents and References

### 21.1 CoE internal

| Document | Purpose |
|---|---|
| [CoE Security Checklist](./security-audit-checklist.md) | **The short version** — 231 lines, for pull-request and sprint review |
| [CoE Audit Framework](./coe-audit-framework.md) | Audit scope, schedule, severity, evidence, exception process |
| [Secure Engineering](../engineering-academy/00-engineering-foundations/03-secure-engineering.md) | Foundation-level minimum bar and review triggers |
| [AI Era Coding Guidelines](../general/ai-era-coding-guidelines.md) | Red Zone rules and AI usage disclosure |
| [AI Team Best Practices](../ai/ai-team-best-practices.md) | Team-level AI working agreements |
| [Neural Security Guidelines](../neural/neural-security-guidelines.md) | Model, training data, and inference security |
| [REST API Best Practices](../general/rest-api-best-practices.md) | API contract, envelope, and error standards |
| [PHP Coding Standards](../php/php-coding-standards.md) · [PHP Best Practices](../php/php-best-practices.md) | PHP security patterns |
| [ColdFusion Style Guide](../cf/coldfusion-style-guide.md) · [CF Code Review Checklist](../cf/coldfusion-code-review-checklist.md) | CFML security practices |
| [CF Security Review Checklist](../engineering-academy/cf-consulting/DELIVERABLES/cf-security-review-checklist.md) | ColdFusion engagement-level review |
| [Node.js/TypeScript Best Practices](../nodejs/nodejs-typescript-best-practices.md) · [Review Checklist](../nodejs/nodejs-typescript-code-review-checklist.md) | Node.js security patterns |
| [Techversant Git Workflow](../git/Techversant_Git_Workflow.md) | Branch protection, review, and merge rules |
| [Security Engineer skill](../ai/claude/skills/security-engineer/SKILL.md) | Threat modeling and secure review method |
| [Compliance Auditor skill](../ai/claude/skills/compliance-auditor/SKILL.md) | Gap assessment and evidence collection method |
| [Contributing](../CONTRIBUTING.md) | How to propose a change to this document |

### 21.2 External standards and guidance

| Resource | Use |
|---|---|
| [OWASP Top 10:2025](https://owasp.org/Top10/2025/) | The taxonomy this checklist is built on |
| [OWASP Top 10:2025 — Introduction](https://owasp.org/Top10/2025/0x00_2025-Introduction/) | Methodology and what changed |
| [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) | Implementation guidance per control |
| [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) | Deeper verification requirements when a client asks for a level |
| [OWASP API Security Top 10](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) | API-specific risks (§13) |
| [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) | AI feature risks (§14) |
| [OWASP MASVS](https://owasp.org/www-project-mobile-app-security/) | Mobile verification standard (§15) |
| [OWASP SAMM](https://owasp.org/www-project-samm/) | Maturing the security programme itself |
| [CISA KEV Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | Exploited-in-the-wild prioritization (§18.1) |
| [CVSS v4.0](https://www.first.org/cvss/v4-0/) | Severity scoring |
| [EPSS](https://www.first.org/epss/) | Exploit-likelihood triage |
| [CWE Top 25](https://cwe.mitre.org/top25/) | Weakness taxonomy for findings |
| [NIST SP 800-63B](https://pages.nist.gov/800-63-3/sp800-63b.html) | Authenticator and password guidance (§6.4) |
| [NIST SP 800-218 (SSDF)](https://csrc.nist.gov/pubs/sp/800/218/final) | Secure software development framework |
| [SLSA](https://slsa.dev/) · [Sigstore](https://www.sigstore.dev/) | Build provenance and artifact signing (§5.3) |
| [CycloneDX](https://cyclonedx.org/) · [SPDX](https://spdx.dev/) | SBOM formats (§5.4) |
| [RFC 9700 — OAuth 2.0 BCP](https://datatracker.ietf.org/doc/html/rfc9700) | Current OAuth security practice (§9.4) |
| [GDPR](https://gdpr-info.eu/) | Privacy obligations (§16) |

---

## Appendix A — Change Log

| Version | Date | Changes |
|---|---|---|
| 2.0-draft | September 2026 | Review fixes. Added section anchors to all cross-document links. Corrected password requirements to [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b.html): 15 characters for single-factor, 8 within MFA, with work-factor minimums per algorithm, bcrypt marked legacy with its 72-byte limit, and composition rules prohibited. Scoped the public reporting route so vulnerabilities in Techversant or client systems never go to a public tracker. Made §18.2 the single authoritative vulnerability deadline, split into acknowledge/contain/remediate, with [CoE Audit Framework](./coe-audit-framework.md) §5.1/§10.3 scoped to audit findings and the stricter deadline governing overlaps; documented how release blockers interact with SLA clocks. Reframed authorization from ownership to action-on-resource and made `404` conditional on existence being confidential. Replaced signature-only upload validation with layered extension-allowlist plus content inspection. Qualified account lockout as temporary and self-clearing to remove the denial-of-service primitive. Marked both documents DRAFT pending Security Lead sign-off. |
| 2.0 | September 2026 | Restructured around [OWASP Top 10:2025](https://owasp.org/Top10/2025/) (sections 3 to 12). Added A03 Software Supply Chain Failures with CI/CD and provenance controls, A10 Mishandling of Exceptional Conditions, CSRF, multi-tenant isolation, cloud/IaC, containers, access hygiene, account recovery, machine identity, client-side integrity, webhook verification, alerting, AI/LLM security, mobile security, and compliance mapping. Added "How to Use" with the Minimum Bar, N/A handling, and evidence rules. Moved SSRF into A01. Updated password guidance to remove forced expiry, security headers to add COOP/CORP and deprecate `X-XSS-Protection`, and vulnerability prioritization to CVSS v4.0 with KEV and EPSS. Added internal and external links throughout. Fixed the malformed section 8 heading from v1.0. Split into two documents on the same day it shipped: this reference keeps the full depth, while [security-audit-checklist.md](./security-audit-checklist.md) became a 74-item working checklist, because 358 items is not usable at pull-request time. |
| 1.0 | May 2026 | Initial release, aligned to OWASP Top 10:2021 |

---

**Document Owner:** CoE Security Team
**Review Cycle:** Quarterly, and within 30 days of any OWASP Top 10 or regulatory update
**Change process:** [CONTRIBUTING.md](../CONTRIBUTING.md) — security documents require 2 approvals including the
Security Lead
