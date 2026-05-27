# CoE Security Audit Checklist

**Version:** 1.0
**Issued by:** Techversant Center of Excellence (CoE)
**Effective Date:** May 2026
**Audience:** CoE Audit Team, Security Team, Development Leads

> This checklist supports the CoE Audit Framework by providing security-specific audit criteria aligned with OWASP Top 10, ISO 27001, and GDPR requirements.

---

## 1. Authentication & Authorization

### 1.1 Authentication
- [ ] No hardcoded credentials in source code
- [ ] Passwords hashed with bcrypt/Argon2/PBKDF2 (not MD5/SHA1)
- [ ] Password policy enforced (min length, complexity, expiry)
- [ ] MFA/2FA available for privileged accounts
- [ ] Session tokens are random, signed, and expire appropriately
- [ ] No credentials in URLs or logs
- [ ] Failed login attempts rate-limited and logged
- [ ] Credential storage uses salts

### 1.2 Authorization
- [ ] Role-based access control (RBAC) implemented correctly
- [ ] Vertical privilege escalation prevented (regular user → admin)
- [ ] Horizontal privilege escalation prevented (user A → user B's data)
- [ ] Authorization checks on every protected endpoint
- [ ] No IDOR vulnerabilities (Insecure Direct Object Reference)
- [ ] API keys managed via secrets manager, not hardcoded

---

## 2. Input Validation & Output Encoding

### 2.1 Input Validation
- [ ] All user input validated (type, length, format, range)
- [ ] Server-side validation independent of client-side
- [ ] File upload validation (extension, MIME type, size, content)
- [ ] SQL injection prevention (prepared statements/ORM only)
- [ ] No string concatenation in queries (even for non-user input)
- [ ] Stored procedures also use parameterized queries

### 2.2 Output Encoding
- [ ] HTML encoding applied (XSS prevention)
- [ ] URL encoding applied for links and redirects
- [ ] JavaScript encoding for inline scripts
- [ ] JSON encoding for API responses
- [ ] No `eval()` or dynamic code execution with user input
- [ ] Content-Security-Policy headers configured

### 2.3 Injection Preventions

| Type | Prevention | Audit Check |
|------|------------|-------------|
| SQL Injection | Prepared statements | Code review + SAST |
| XSS | Output encoding | DAST + code review |
| Command Injection | Never build shell commands from input | Code review |
| LDAP Injection | Input sanitization | Code review |
| XXE | Disable XML entity expansion | Code review |
| SSRF | URL validation, allowlist for fetch targets | Code review |

---

## 3. Data Protection

### 3.1 Encryption
- [ ] Data encrypted at rest (AES-256 or equivalent)
- [ ] TLS 1.2+ for data in transit
- [ ] Certificate validation enabled for external connections
- [ ] No self-signed certificates in production
- [ ] Encryption keys rotated according to policy
- [ ] Keys stored in secrets manager, not in code/.env

### 3.2 GDPR-Specific
- [ ] PII fields identified and classified
- [ ] No PII in logs (check email, phone, address fields)
- [ ] Data minimization applied (only necessary fields collected)
- [ ] Consent mechanism documented and auditable
- [ ] Right to erasure implemented (soft delete, cascade cleanup)
- [ ] Data retention policy defined and enforced

### 3.3 Sensitive Data Handling
- [ ] Credit card/PII never stored in plain text
- [ ] API keys/secrets not in code, .env, or version control
- [ ] Stack traces not exposed to users
- [ ] Sensitive data not in error messages
- [ ] Debug mode disabled in production
- [ ] Log sanitization applied (mask email domains, phone numbers)

---

## 4. API Security

### 4.1 General API
- [ ] Authentication required for all non-public endpoints
- [ ] Authorization checked per request
- [ ] Rate limiting implemented
- [ ] Request size limits enforced
- [ ] CORS configured with allowlist (not wildcard `*`)
- [ ] No sensitive data in query parameters (POST body for sensitive input)
- [ ] API versioning implemented
- [ ] Deprecation warnings issued before endpoint removal

### 4.2 REST API
- [ ] No verbs in URLs (use HTTP methods)
- [ ] Idempotency for POST endpoints (Idempotency-Key header)
- [ ] CORS preflight requests handled correctly
- [ ] OPTIONS method not exposing allowed methods

### 4.3 Authentication Tokens
- [ ] JWTs signed with strong keys (RS256/ES256 preferred)
- [ ] JWT expiry set appropriately (access: 15-60 min, refresh: 7-30 days)
- [ ] Refresh token rotation implemented
- [ ] Token audience and issuer validated
- [ ] Tokens not exposed in URLs or logs
- [ ] Revocation mechanism implemented (blacklist or short-lived tokens)

---

## 5. Session Management

- [ ] Session tokens are cryptographically random
- [ ] Session timeout enforced (idle + absolute)
- [ ] Session invalidation on logout
- [ ] Session fixation prevention
- [ ] Secure, HttpOnly, SameSite cookies configured
- [ ] Session stored server-side (not JWT in localStorage unless necessary)
- [ ] Session regeneration after privilege escalation

---

## 6. Configuration & Operations

### 6.1 Secure Configuration
- [ ] Default credentials changed
- [ ] Debug mode disabled in production
- [ ] Error pages generic (no stack traces)
- [ ] Directory listing disabled
- [ ] Server/software versions hidden
- [ ] Unnecessary features/ports disabled
- [ ] Cloud storage buckets not publicly accessible

### 6.2 Dependency Management
- [ ] No known critical vulnerabilities in dependencies
- [ ] Dependency scanning in CI/CD
- [ ] Third-party packages reviewed (license, maintenance, security)
- [ ] Provenance verified for open-source packages
- [ ] Supply chain security (no malicious packages)
- [ ] SBOM generated and reviewed

### 6.3 Security Headers

| Header | Purpose | Required |
|--------|---------|----------|
| Strict-Transport-Security | Force HTTPS | Yes |
| Content-Security-Policy | Prevent XSS/injection | Yes |
| X-Content-Type-Options | Prevent MIME sniffing | Yes |
| X-Frame-Options | Clickjacking protection | Yes |
| X-XSS-Protection | Legacy XSS filter (deprecated but audit) | No |
| Referrer-Policy | Control referrer information | Yes |
| Permissions-Policy | Control browser features | Yes |

---

## 7. Error Handling & Logging

### 7.1 Error Handling
- [ ] Generic error messages for users (no internal details exposed)
- [ ] Detailed errors logged server-side with stack traces
- [ ] Custom error pages configured
- [ ] Unhandled exceptions caught and logged
- [ ] Error IDs returned to users for support correlation
- [ ] Fail-safe defaults (deny on error)

### 7.2 Logging
- [ ] All authentication attempts logged (success + failure)
- [ ] Authorization failures logged
- [ ] Input validation failures logged
- [ ] Errors and exceptions logged with context
- [ ] Sufficient detail for forensic analysis
- [ ] Logs protected from tampering (immutability)
- [ ] Log retention policy defined
- [ ] Structured logging (JSON) for searchability

### 7.3 What NOT to Log
- [ ] Passwords never logged
- [ ] Tokens/keys never logged
- [ ] Full credit card numbers never logged
- [ ] PII minimized (masked if needed)
- [ ] Request bodies not logged by default (optional for debugging)

---

 | 8. OWASP Top 10 Alignment

| OWASP Category | CoE Control | Audit Evidence |
|---------------|------------|----------------|
| A01 Broken Access Control | RBAC, authorization checks | Code review + tests |
| A02 Cryptographic Failures | Encryption, key management | Config review + code review |
| A03 Injection | Prepared statements, input validation | SAST + DAST |
| A04 Insecure Design | Threat modeling, secure defaults | Design review + architecture |
| A05 Security Misconfiguration | Hardening checklist, security headers | Config review + scanner |
| A06 Vulnerable Components | Dependency scanning, SBOM | CI/CD + vulnerability report |
| A07 Auth Failures | MFA, password policy, session management | Config + code review |
| A08 Data Integrity Failures | Version control, signed updates, CI/CD | Git history + pipeline review |
| A09 Logging Failures | Structured logging, error IDs | Log audit |
| A10 SSRF | URL validation, allowlists | Code review |

---

## 9. Security Testing Requirements

| Test Type | Frequency | Tool Examples | Owner |
|-----------|-----------|---------------|--------|
| **SAST** | Every PR | SonarQube, ESLint security | CI/CD |
| **DAST** | Weekly/Monthly | OWASP ZAP, Burp Suite | Security team |
| **Dependency Scan** | Every commit | Snyk, npm audit, dependabot | CI/CD |
| **Secret Scanning** | Every commit | GitLeaks, TruffleHog | CI/CD |
| **Penetration Test** | Annually | External tester | Security lead |
| **Security Review** | Per release | Manual review | Audit team |

---

## 10. Vulnerability Response

### SLAs

| Severity | Response Time | Remediation Time |
|----------|---------------|------------------|
| Critical (CVSS 9-10) | 24 hours | 7 days |
| High (CVSS 7-8.9) | 48 hours | 30 days |
| Medium (CVSS 4-6.9) | 1 week | 90 days |
| Low (CVSS < 4) | Next sprint | Next release |

### Response Process

1. **Triage** (within SLA) — Verify vulnerability, assess impact, assign severity
2. **Containment** — Immediate fix or compensating control
3. **Remediation** — Develop and test fix
4. **Verification** — Confirm fix resolves issue
5. **Post-Incident** — Review, lessons learned, update controls

---

## 11. Related Documents

| Document | Purpose |
|----------|---------|
| `audit/coe-audit-framework.md` | CoE audit scope and schedule |
| `general/ai-era-coding-guidelines.md` | AI-assisted security review |
| `php/php-coding-standards.md` | PHP security standards |
| `cf/coldfusion-style-guide.md` | CFML security practices |
| `nodejs/nodejs-typescript-best-practices.md` | Node.js security patterns |
| `general/rest-api-best-practices.md` | API security considerations |

---

## 12. Quick Reference Cards

### Secrets Never in Code
```
❌ $apiKey = "sk_live_abc123"
❌ connectionString = "Server=...;Database=...;User=admin;Password=secret"
❌ const JWT_SECRET = "my-secret-key"

✅ Use environment variables / secrets manager
✅ Azure Key Vault, AWS Secrets Manager, HashiCorp Vault
```

### Input Validation Rules
```
✅ Validate: type, length, format, range, expected values
✅ Sanitize: HTML, SQL, OS commands after validation
✅ Reject: unexpected formats, excessive length, injection patterns
❌ Never trust client-side validation alone
❌ Never concatenate user input into queries/logic
```

### Security Headers Check
```
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: default-src 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

---

**Document Owner:** CoE Security Team
**Review Cycle:** Quarterly
**Next Review:** August 2026