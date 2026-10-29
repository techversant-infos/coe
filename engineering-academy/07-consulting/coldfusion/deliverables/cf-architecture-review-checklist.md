# ColdFusion Architecture Review Checklist

> Systematic review of existing ColdFusion applications for modernization assessment.

## Purpose

Use this checklist when conducting technical assessments of legacy ColdFusion applications. Each section covers a key dimension of the application's health and modernization complexity.

## Metadata

| Field | Value |
|-------|-------|
| Version | 1.0 |
| Last Updated | |
| Author | |
| Client | |
| Application | |

---

## 1. Environment & Infrastructure

### Server Configuration

- [ ] **CF Version:** What version of ColdFusion is running?
- [ ] **Engine:** Adobe ColdFusion or Lucee?
- [ ] **Licensing:** Valid? Expiring?
- [ ] **Operating System:** Windows Server? Linux?
- [ ] **Java Version:** What JVM version?
- [ ] **Clustered:** Single server or cluster?
- [ ] **Load Balancer:** In use? Type?
- [ ] **Monitoring:** What tools? (FusionReactor, SeeFusion, etc.)

### Hosting

- [ ] **Location:** On-prem, AWS, Azure, other cloud?
- [ ] **Virtualization:** VMware, Hyper-V, containers?
- [ ] **Network:** VPN required? Firewall rules documented?

**Notes:**
-

---

## 2. Application Architecture

### Framework Detection

- [ ] **Framework:** What framework is used?
  - [ ] None (plain CFM with includes)
  - [ ] FW/1
  - [ ] ColdBox
  - [ ] Fusebox
  - [ ] Mango
  - [ ] Mura CMS
  - [ ] Custom MVC
  - [ ] Other: _______

- [ ] **Application.cfc:** Present? Active?
- [ ] **Application.cfm:** Present? Legacy pattern?
- [ ] **Component Structure:** Components (.cfc) or only tags (.cfm)?

### Directory Structure

```
Application Root/
├── /cfc          (Components)
├── /includes     (Included files)
├── /javascript   (JS files)
├── /css          (Stylesheets)
├── /images       (Assets)
├── /udfs         (User-defined functions)
├── /customtags   (Custom tags)
└── /api          (API endpoints)
```

- [ ] Structure follows consistent pattern?
- [ ] No deeply nested includes?
- [ ] Assets organized properly?

**Notes:**
-

---

## 3. Database Layer

### Database

- [ ] **Database Type:** MSSQL, MySQL, PostgreSQL, Oracle, other?
- [ ] **Version:**
- [ ] **Connection:** DSN configured? SSL?
- [ ] **Connection Pooling:** Configured? Max connections?

### Schema

- [ ] Tables documented?
- [ ] Indexes present?
- [ ] Foreign keys enforced?
- [ ] ERD available?
- [ ] Naming conventions consistent?

### Query Patterns

- [ ] `cfqueryparam` used consistently?
- [ ] Dynamic SQL (string concatenation)?
- [ ] N+1 query patterns?
- [ ] Large result sets loaded into memory?
- [ ] Query caching used?

**Notes:**
-

---

## 4. Security

### Authentication & Authorization

- [ ] **Method:** Built-in CF auth? Custom? Third-party?
- [ ] **Session Management:** How are sessions handled?
- [ ] **Roles/Permissions:** How are permissions managed?
- [ ] **Password Storage:** Hashed? Algorithm?
- [ ] **Session Tokens:** Secure? HttpOnly? SameSite?

### Common Vulnerabilities

- [ ] SQL injection in `cfquery`?
- [ ] XSS in `cfoutput` or user input?
- [ ] CSRF protection?
- [ ] File upload vulnerabilities?
- [ ] Exposure of CFIDE or admin paths?
- [ ] Hardcoded credentials?
- [ ] Secrets in code?

### Server Security

- [ ] CF Administrator secured?
- [ ] Debugging enabled in production?
- [ ] Error handling (custom 404, 500 pages)?
- [ ] SSL/TLS configured?
- [ ] Firewall rules documented?

**Notes:**
-

---

## 5. Performance

### Application Performance

- [ ] Common pages response time: ___ ms (target: < 500ms)
- [ ] Heavy pages identified?
- [ ] Caching implemented?
- [ ] Slow queries identified?
- [ ] External API calls causing delays?
- [ ] Large file processing?

### JVM & Server

- [ ] JVM heap size:
- [ ] Garbage collection logs reviewed?
- [ ] Thread pool settings?
- [ ] Request timeout configured?
- [ ] Connection pool settings?

### Frontend Performance

- [ ] Assets minified/compressed?
- [ ] Images optimized?
- [ ] CDN in use?
- [ ] Browser caching configured?
- [ ] Render-blocking JS?

**Notes:**
-

---

## 6. Dependencies & Integrations

### External Services

| Service | Type | Authentication | Status |
|---------|------|---------------|--------|
| | | | |
| | | | |
| | | | |

- [ ] All external integrations documented?
- [ ] API keys/secrets secured?
- [ ] Rate limiting in place?
- [ ] Timeout handling for external calls?

### Dependencies

- [ ] CF libraries/custom tags?
- [ ] Java libraries?
- [ ] Third-party components?
- [ ] Version information available?

**Notes:**
-

---

## 7. Code Quality

### Maintainability

- [ ] Naming conventions consistent?
- [ ] Code commented?
- [ ] Complex nested logic?
- [ ] Repeated code blocks?
- [ ] TODOs/FIXMEs outstanding?

### Testing

- [ ] Unit tests?
- [ ] Integration tests?
- [ ] Automated testing in CI/CD?

### Documentation

- [ ] README or documentation?
- [ ] API documentation?
- [ ] Architecture diagrams?
- [ ] Deployment procedures?

**Notes:**
-

---

## 8. Deployment & DevOps

### Deployment

- [ ] Deployment process documented?
- [ ] Manual or automated?
- [ ] Rollback procedure?
- [ ] Environment parity (dev/staging/prod)?

### CI/CD

- [ ] Version control (Git/SVN)?
- [ ] CI pipeline?
- [ ] Automated testing?
- [ ] Environment configuration management?

### Environments

| Environment | Purpose | CF Version | DB Version |
|-------------|---------|------------|------------|
| Development | Local dev | | |
| Staging | Testing | | |
| Production | Live | | |

**Notes:**
-

---

## 9. Technical Debt Assessment

### Debt Categories

| Category | Level (1-5) | Notes |
|----------|-------------|-------|
| Code Complexity | | |
| Testing Coverage | | |
| Documentation | | |
| Security Posture | | |
| Performance | | |
| Dependency Age | | |
| Deployment Process | | |

**Overall Debt Score:** ___/35

### High-Priority Issues

1. ________________________________________________
2. ________________________________________________
3. ________________________________________________

**Notes:**
-

---

## 10. Risk Assessment

### Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| CF version EOL | | | |
| Security vulnerabilities | | | |
| Performance degradation | | | |
| Dependency conflicts | | | |
| Knowledge loss | | | |

### Business Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Key person dependency | | | |
| Vendor lock-in | | | |
| Scalability limits | | | |
| Compliance gaps | | | |

**Notes:**
-

---

## Summary

### Quick Stats

| Metric | Value |
|--------|-------|
| Total CFM files | |
| Total CFC files | |
| Database tables | |
| External integrations | |
| Estimated age | |

### Overall Assessment

| Dimension | Score (1-5) |
|-----------|--------------|
| Architecture | |
| Security | |
| Performance | |
| Maintainability | |
| Modernization Readiness | |

### Recommendations Summary

1. ________________________________________________
2. ________________________________________________
3. ________________________________________________

### Next Steps

- [ ] Detailed technical report
- [ ] Proof-of-concept for migration
- [ ] Security audit
- [ ] Performance benchmark
- [ ] Quick wins implementation
