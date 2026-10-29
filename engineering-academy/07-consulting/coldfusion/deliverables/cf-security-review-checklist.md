# ColdFusion Security Review Checklist

> Focused security audit for ColdFusion applications.

## Purpose

Use this checklist when conducting security assessments of ColdFusion applications. Covers both CF-specific vulnerabilities and general web security.

## Metadata

| Field | Value |
|-------|-------|
| Version | 1.0 |
| Last Updated | |
| Author | |
| Client | |
| Application | |

---

## 1. Authentication & Session Management

### Authentication

- [ ] Authentication method implemented?
- [ ] Password requirements enforced?
- [ ] Password hashing algorithm: _______________
- [ ] Brute force protection?
- [ ] Account lockout after failed attempts?
- [ ] Multi-factor authentication available?

### Session Management

- [ ] Session token format secure?
- [ ] Session timeout configured?
- [ ] Session fixation protection?
- [ ] HttpOnly cookies?
- [ ] Secure flag on cookies?
- [ ] SameSite attribute set?

**Notes:**
-

---

## 2. Input Validation & Injection

### SQL Injection

- [ ] All queries use `cfqueryparam`?
- [ ] No dynamic SQL construction?
- [ ] ORM queries parameterized?
- [ ] Query-of-queries safe?

### XSS (Cross-Site Scripting)

- [ ] User input encoded for output?
- [ ] `encodeForHTML()` used?
- [ ] `encodeForURL()` used?
- [ ] Rich text handled safely?
- [ ] CSP headers configured?

### Command Injection

- [ ] `cfexecute` used safely?
- [ ] No shell injection possible?
- [ ] File paths validated?

**Notes:**
-

---

## 3. Access Control

### Authorization

- [ ] Roles/permissions implemented?
- [ ] Authorization checked on every request?
- [ ] Horizontal privilege escalation prevented?
- [ ] Vertical privilege escalation prevented?
- [ ] Admin functions properly protected?

### Direct Object References

- [ ] No predictable IDs in URLs?
- [ ] Resource ownership verified?
- [ ] Sensitive files protected?

**Notes:**
-

---

## 4. Data Protection

### Sensitive Data

- [ ] PII identified and documented?
- [ ] PII encrypted at rest?
- [ ] PII transmitted securely?
- [ ] Data retention policy?
- [ ] Data export/deletion capability?

### Configuration

- [ ] Secrets in environment variables?
- [ ] Database credentials secured?
- [ ] API keys not in code?
- [ ] Encryption keys managed properly?

**Notes:**
-

---

## 5. ColdFusion-Specific Security

### CF Administrator

- [ ] Admin path changed from default `/CFIDE/`?
- [ ] Admin access restricted?
- [ ] RDS disabled in production?
- [ ] Debugging disabled in production?
- [ ] Stack trace displayed in errors?

### CFML Security

- [ ] `cffile` uploads validated?
- [ ] File type checking robust?
- [ ] Path traversal prevented?
- [ ] `cfinclude` paths restricted?
- [ ] Dangerous functions disabled?

### Server Configuration

- [ ] Missing X-Frame-Options header?
- [ ] Missing Content-Security-Policy?
- [ ] SSL/TLS configured?
- [ ] Old SSL protocols disabled?
- [ ] Secure cookie settings?

**Notes:**
-

---

## 6. API Security

### REST/JSON APIs

- [ ] Authentication required?
- [ ] Rate limiting implemented?
- [ ] Input validation on API endpoints?
- [ ] CORS configured properly?
- [ ] API keys secured?
- [ ] Error messages don't leak info?

### SOAP Services

- [ ] WSDL exposure limited?
- [ ] Input validation on SOAP params?
- [ ] Authentication on services?

**Notes:**
-

---

## 7. OWASP Top 10 Check

| OWASP Category | Finding | Severity | Status |
|----------------|---------|----------|--------|
| A01 Broken Access Control | | | |
| A02 Cryptographic Failures | | | |
| A03 Injection | | | |
| A04 Insecure Design | | | |
| A05 Security Misconfiguration | | | |
| A06 Vulnerable Components | | | |
| A07 Auth Failures | | | |
| A08 Data Integrity Failures | | | |
| A09 Logging Failures | | | |
| A10 SSRF | | | |

**Notes:**
-

---

## 8. Logging & Monitoring

### Logging

- [ ] Security events logged?
- [ ] Failed login attempts logged?
- [ ] Admin actions logged?
- [ ] Sensitive data excluded from logs?
- [ ] Log retention policy?

### Monitoring

- [ ] Intrusion detection?
- [ ] Anomaly detection?
- [ ] Real-time alerting?
- [ ] Security dashboard?

**Notes:**
-

---

## 9. Vulnerability Summary

| ID | Vulnerability | Location | Severity | Remediation |
|----|--------------|----------|----------|-------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

---

## 10. Remediation Priority

### Critical (Fix Immediately)

1. ________________________________________________

### High (Fix Within 30 Days)

1. ________________________________________________

### Medium (Fix Within 90 Days)

1. ________________________________________________

### Low (Plan for Next Release)

1. ________________________________________________

---

## Recommendations

1. ________________________________________________
2. ________________________________________________
3. ________________________________________________
