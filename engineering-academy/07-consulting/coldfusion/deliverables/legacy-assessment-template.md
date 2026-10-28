# Legacy Application Assessment Template

> Standard template for documenting ColdFusion application assessments.

---

## Assessment Metadata

| Field | Value |
|-------|-------|
| Report ID | ASSESS-[YEAR]-[NUMBER] |
| Client | |
| Application Name | |
| Assessment Date | |
| Assessor(s) | |
| Version | 1.0 |
| Classification | Confidential |

---

## Executive Summary

### Overview

[2-3 sentence description of the application and assessment scope]

### Key Findings

| Finding | Severity | Recommendation |
|---------|----------|-----------------|
| 1. | | |
| 2. | | |
| 3. | | |

### Recommended Path Forward

[One paragraph stating the recommended approach]

### Investment Summary

| Item | Estimate |
|------|----------|
| Assessment | Included |
| Modernization | $XX,XXX |
| Timeline | X months |

---

## 1. Application Overview

### 1.1 Purpose and Business Context

**Business Function:**
_______________________________________

**Users:**
- Internal: _______________
- External: _______________
- Total users: _______________

**Business Criticality:**
- [ ] Mission Critical
- [ ] Business Important
- [ ] Business Standard
- [ ] Departmental

### 1.2 Technical Environment

| Component | Current State |
|-----------|--------------|
| **ColdFusion Version** | |
| **Engine (Adobe/Lucee)** | |
| **Operating System** | |
| **Web Server** | |
| **Database** | |
| **JVM Version** | |
| **Hosting** | On-prem / AWS / Azure / Other |
| **Monitoring** | |
| **Last Updated** | |

### 1.3 Application Metrics

| Metric | Value |
|--------|-------|
| CFM files | |
| CFC files | |
| Custom tags | |
| Database tables | |
| External integrations | |
| API endpoints | |
| Scheduled tasks | |
| Estimated code lines | |

---

## 2. Architecture Assessment

### 2.1 Framework Analysis

| Aspect | Finding |
|--------|---------|
| Framework in use | None / FW/1 / ColdBox / Fusebox / Custom |
| Framework version | |
| Architecture pattern | |
| Code organization | |

**Assessment:** [ ] Strong [ ] Moderate [ ] Weak [ ] Critical

### 2.2 Directory Structure

```
[Insert directory tree or description]
```

### 2.3 Data Architecture

**Database Schema:**
| Table Count | Complexity |
|-------------|------------|
| | Simple / Moderate / Complex |

**Key Tables:**
| Table | Purpose | Row Count | Foreign Keys |
|-------|---------|-----------|--------------|
| | | | |
| | | | |

**Data Relationships Diagram:**
```
[Insert ERD summary or relationship description]
```

### 2.4 Integration Map

| Integration | Type | Criticality | Status |
|-------------|------|-------------|--------|
| | REST / SOAP / Database / File | | |
| | | | |

---

## 3. Technical Debt Assessment

### 3.1 Code Quality Score

**Scoring:** 1 = Excellent, 5 = Critical

| Dimension | Score | Evidence |
|-----------|-------|----------|
| Complexity | /5 | |
| Documentation | /5 | |
| Testing | /5 | |
| Structure | /5 | |
| Dependencies | /5 | |
| **Total** | **__/25** | |

**Rating:** [ ] Excellent [ ] Good [ ] Moderate [ ] High [ ] Critical

### 3.2 Dependency Age

| Dependency | Version | Age | Risk |
|-----------|---------|-----|------|
| ColdFusion | | | High/Med/Low |
| Database driver | | | |
| JavaScript libs | | | |
| CSS framework | | | |

### 3.3 Technical Debt Summary

| Category | Debt Level | Description |
|----------|------------|-------------|
| Code Quality | | |
| Testing | | |
| Documentation | | |
| Dependencies | | |
| **Overall** | | |

---

## 4. Security Assessment

### 4.1 Security Posture

**Overall Rating:** [ ] Secure [ ] Adequate [ ] Vulnerable [ ] Critical

### 4.2 Security Findings

| Finding | Severity | CVSS | Location | Recommendation |
|---------|----------|------|----------|----------------|
| | Critical / High / Med / Low | | | |

### 4.3 Compliance Considerations

| Standard | Applicable? | Status |
|----------|-------------|--------|
| OWASP Top 10 | | Compliant / Non-Compliant / Partial |
| GDPR | | |
| HIPAA | | |
| PCI-DSS | | |

---

## 5. Performance Assessment

### 5.1 Performance Baseline

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Avg response time | | < 2s | |
| P95 response time | | < 5s | |
| Error rate | | < 0.1% | |
| DB query time | | < 500ms | |

### 5.2 Bottlenecks Identified

| Area | Issue | Impact | Recommendation |
|------|-------|--------|----------------|
| | | | |

---

## 6. Findings Summary

### 6.1 Critical Findings (Fix Immediately)

| # | Finding | Risk | Recommendation |
|---|---------|------|----------------|
| 1 | | | |

### 6.2 High Priority Findings (Fix Within 90 Days)

| # | Finding | Risk | Recommendation |
|---|---------|------|----------------|
| 1 | | | |

### 6.3 Medium Priority Findings (Plan for Fix)

| # | Finding | Risk | Recommendation |
|---|---------|------|----------------|
| 1 | | | |

### 6.4 Low Priority Findings (Monitor)

| # | Finding | Risk | Recommendation |
|---|---------|------|----------------|
| 1 | | | |

---

## 7. Modernization Options

### 7.1 Option Analysis

| Option | Investment | Timeline | Risk | Recommendation |
|--------|-----------|----------|------|----------------|
| A: Stay on CF | | | | |
| B: Upgrade CF | | | | |
| C: Lucee Migration | | | | |
| D: Full Modernization | | | | |

### 7.2 Recommended Approach

**Recommended:** _______________________________________

**Rationale:**
_______________________________________________________________

### 7.3 Roadmap Overview

| Phase | Activities | Timeline | Investment |
|-------|-----------|----------|------------|
| Phase 0 | Discovery & Planning | | |
| Phase 1 | Foundation | | |
| Phase 2 | Core Migration | | |
| Phase 3 | Testing & Deploy | | |

---

## 8. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| | Low/Med/High | | |
| | | | |

---

## 9. Appendices

### Appendix A: Files Reviewed
[List of key files analyzed]

### Appendix B: Interview Notes
[Summary of stakeholder interviews]

### Appendix C: Screenshots
[Architecture diagrams, code samples, etc.]

---

## Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| Assessor | | | |
| Reviewer | | | |
| Client Ack | | | |

---

*This assessment is confidential and intended solely for the use of the named client.*
