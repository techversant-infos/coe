# CoE Compliance Audit Framework

**Version:** 1.0
**Issued by:** Techversant Center of Excellence (CoE)
**Effective Date:** May 2026
**Audience:** CoE Audit Team, Engineering Leads, Project Managers

> This document defines the audit scope, schedule, and procedures for verifying that engineering teams follow CoE standards for code quality, security, and compliance.

---

## 1. Audit Scope

### 1.1 What to Audit

| Area | What to Check | Source Document |
|------|---------------|-----------------|
| **Code Quality** | Linting passes, code complexity limits, naming conventions | Stack-specific style guides |
| **Best Practices** | Architecture patterns, error handling, logging | `*-best-practices.md` per stack |
| **Coding Standards** | Formatting, documentation, naming | `*-style-guide.md` per stack |
| **PR Process** | Reviews completed, standards acknowledged, no direct-to-main merges | `Techversant_Git_Workflow.md` |
| **AI-Assisted Code** | Human review documented, AI commits tagged, Red Zone not bypassed | `ai-era-coding-guidelines.md` |
| **Security** | No hardcoded secrets, input validation, prepared statements, OWASP compliance | Security checklist per stack |
| **API Standards** | Response format, error envelope, boolean naming, filtering | `rest-api-best-practices.md` |

### 1.2 Who to Audit

| Scope | Frequency | Teams |
|-------|-----------|-------|
| **Project Level** | Per release/sprint | Active projects with CoE standards applied |
| **Team Level** | Monthly | All engineering teams using CoE standards |
| **Individual Level** | Quarterly (spot check) | Engineers flagged for repeated violations |

---

## 2. Audit Schedule

### 2.1 Recurring Audits

| Audit Type | Frequency | Trigger | Owner |
|------------|-----------|---------|-------|
| **Sprint Review** | Every 2 weeks | End of sprint | Team Lead |
| **Monthly Compliance** | Monthly | Calendar | Audit Team |
| **Quarterly Deep Audit** | Quarterly | Quarter start | Audit Lead + Security |
| **Release Gate** | Per release | Pre-deployment | QA + CoE |
| **Ad-hoc Spot Check** | As needed | Issue flagged | Audit Team |

### 2.2 Audit Triggers

Audits trigger immediately when:
- New project onboarded to CoE
- Major security incident reported
- Repeated pattern of PR review failures
- Regulatory requirement change (ISO/GDPR update)

---

## 3. Compliance Standards

### 3.1 ISO 27001 Alignment

| CoE Control | ISO 27001 Clause | Evidence Required |
|-------------|------------------|-------------------|
| Code review process | A.14.2 Protection of systems | PR review records, reviewer sign-off |
| Access control for code | A.9.4 Access control policy | Branch protection rules, no direct pushes |
| Change management | A.12.1 Change management | Commit history, branch model adherence |
| Secure development | A.14.1 Security requirements | Linting, SAST, dependency scan results |
| Data protection | A.18.1 Compliance | No PII in code, secrets management |

### 3.2 GDPR Alignment

| Requirement | CoE Control | Audit Check |
|-------------|-------------|-------------|
| **Data minimization** | No unnecessary fields logged | Log audit: check for PII fields |
| **Right to erasure** | Soft delete patterns, no hardcoded data | Code review: deletion patterns |
| **Consent logging** | API returns minimal data | API response audit |
| **Breach notification** | Structured logging with traceId | Log format verification |

### 3.3 SOC 2 Alignment (if applicable)

| Trust Principle | CoE Control |
|-----------------|-------------|
| Security | Branch protection, secret scanning, access reviews |
| Availability | Uptime monitoring, error rate thresholds |
| Processing Integrity | Input validation, error handling, data validation |
| Confidentiality | Encryption, access controls, data classification |
| Privacy | GDPR controls + data retention policies |

---

## 4. Audit Checklist

### 4.1 Pre-Audit (Preparation)

- [ ] Define scope: which teams/projects
- [ ] Pull PR history for review period
- [ ] Collect linting reports and SAST results
- [ ] Verify branch protection settings
- [ ] Prepare evidence templates

### 4.2 During Audit

#### Code Review Process
- [ ] PR reviews completed before merge (not after)
- [ ] At least one reviewer sign-off per PR
- [ ] No force-pushes to protected branches
- [ ] Branch naming follows convention
- [ ] Commits follow Conventional Commits format
- [ ] No direct commits to main/develop

#### AI-Assisted Code
- [ ] AI-generated commits tagged `[ai-assisted: claude]`
- [ ] Human review documented in PR
- [ ] Red Zone code (auth, encryption, PII) reviewed by senior
- [ ] No secrets pasted into prompts (incident if found)

#### Security
- [ ] No hardcoded credentials or API keys
- [ ] All user input validated (sanitization + validation)
- [ ] SQL uses prepared statements / ORM bindings
- [ ] Output encoding applied (XSS prevention)
- [ ] Secrets stored in `.env` or secrets manager
- [ ] Dependencies scanned for vulnerabilities

#### API Standards
- [ ] Response format matches envelope (success/error)
- [ ] Boolean fields use `is`/`has`/`can` prefix
- [ ] Date format is ISO 8601
- [ ] HTTP status codes correct (2xx/4xx/5xx)
- [ ] Validation errors include field-level details
- [ ] Sensitive data not returned in responses

#### Documentation
- [ ] Code comments explain WHY (not WHAT)
- [ ] Public methods have PHPDoc/JSDoc where required
- [ ] API endpoints documented (OpenAPI/Swagger)
- [ ] Migration scripts documented

### 4.3 Post-Audit

- [ ] Findings classified (Critical/High/Medium/Low)
- [ ] Remediation timeline agreed with team
- [ ] Evidence collected and archived
- [ ] Audit report generated
- [ ] Follow-up scheduled

---

## 5. Finding Classification

### 5.1 Severity Levels

| Level | Definition | SLA |
|-------|------------|-----|
| **Critical** | Security breach risk, data leak, non-compliance | 24 hours |
| **High** | Significant quality/security gap | 1 week |
| **Medium** | Process deviation, moderate risk | 2 weeks |
| **Low** | Style deviation, documentation gap | Next sprint |

### 5.2 Scoring Matrix

| Criteria | Weight | Score (1-5) |
|----------|--------|-------------|
| Security Impact | 30% | |
| Compliance Impact (ISO/GDPR) | 25% | |
| Frequency of occurrence | 20% | |
| Ease of exploitation | 15% | |
| Business impact | 10% | |

**Total Score:** Weighted sum. Critical ≥ 4.0, High ≥ 3.0, Medium ≥ 2.0, Low < 2.0

---

## 6. Audit Reporting

### 6.1 Report Structure

```
1. Executive Summary
   - Scope, period, overall compliance score
   - Key risks and recommendations

2. Findings Detail
   - Finding ID, description, evidence
   - Severity, affected teams/projects
   - Remediation owners and timeline

3. Metrics
   - PR review completion rate
   - Linting pass rate
   - AI disclosure rate
   - Time to remediate findings

4. Recommendations
   - Process improvements
   - Tooling additions
   - Training needs

5. Appendices
   - Evidence links
   - Raw data
```

### 6.2 Metrics to Track

| Metric | Target | Formula |
|--------|--------|---------|
| PR Review Completion Rate | ≥ 95% | Reviews completed / Total PRs |
| First-Time Pass Rate | ≥ 80% | PRs passing lint without rework |
| AI Disclosure Rate | 100% | AI-tagged PRs / Total AI-assisted PRs |
| Finding Remediate Rate | ≥ 90% | Remediated within SLA / Total findings |
| Avg Remediation Time | < 5 days | Total days / Findings remediated |

---

## 7. Evidence Collection

### 7.1 What to Archive

| Evidence Type | Retention | Storage |
|---------------|-----------|---------|
| PR review records | 3 years | Git history + project folder |
| Linting/SAST reports | 1 year | CI/CD artifacts |
| Audit reports | 5 years | CoE audit archive |
| Training records | 5 years | HR system |
| Exception approvals | 5 years | CoE documentation |

### 7.2 Evidence Template

For each finding, collect:
1. **Screenshot/URL** of the violation
2. **PR/Commit reference**
3. **Policy violated** (document + section)
4. **Date discovered**
5. **Owner notified** (name + date)
6. **Remediation confirmed** (screenshot + date)

---

## 8. Exception Process

When teams cannot comply (technical constraint, timeline pressure):

1. **Request Exception:** Team Lead submits exception request to CoE
2. **Risk Assessment:** CoE evaluates security/compliance impact
3. **Approval:** CoE Lead or Security Lead approves
4. **Documentation:** Exception logged with:
   - Reason for exception
   - Compensating controls
   - Review date
   - Approver signature
5. **Monitoring:** Exception reviewed at next audit

---

## 10. Remediation Tracker

Use this tracker to monitor open findings until resolution.

### 10.1 Finding Record Template

```
| Finding ID | F-[TEAM]-[SEQ] | Example: F-PHP-001 |
|------------|----------------|--------------------|
| Description | What was found | |
| Severity | Critical/High/Medium/Low | |
| Policy Violated | Document + Section | |
| Found Date | YYYY-MM-DD | |
| Owner | Team Lead name | |
| Due Date | SLA deadline | |
| Status | Open / In Progress / Resolved / Waived | |
| Evidence of Fix | PR link / screenshot | |
| Resolved Date | YYYY-MM-DD | |
| Auditor Sign-off | Name + Date | |
```

### 10.2 Status Workflow

```
Open → In Progress → Resolved → (Audit Closed)
                    ↘ Waived → (Exception approved)
```

### 10.3 SLA Tracking

| Severity | Target | Escalation at |
|----------|--------|----------------|
| Critical | 24 hours | 12 hours |
| High | 1 week | 3 days |
| Medium | 2 weeks | 1 week |
| Low | Next sprint | N/A |

---

## 11. Training & Certification

### 11.1 Required Training

| Training | Audience | Frequency | Renewal |
|----------|----------|-----------|---------|
| CoE Standards Overview | All engineers | Onboarding | Annual |
| AI-Assisted Development | All engineers | Quarterly | Annual |
| Security Fundamentals (OWASP) | All engineers | Annual | Annual |
| GDPR/ISO 27001 Awareness | Leads + Auditors | Annual | Annual |
| Code Review Mastery | PR reviewers | Annual | Biennial |

### 11.2 Training Records

Maintain records per engineer:

| Field | Description |
|-------|-------------|
| Engineer Name | Full name |
| Employee ID | HR system ID |
| Training Completed | Training name |
| Completion Date | YYYY-MM-DD |
| Expiry Date | YYYY-MM-DD |
| Certificate Number | If applicable |
| Verified By | Training administrator |

### 11.3 Compliance with Training Requirements

- Engineers without current training **cannot be PR approvers**
- Leads must verify training status before assigning review duties
- Lapsed training flagged at next audit cycle

---

## 12. Audit Team Responsibilities

| Role | Responsibilities |
|------|------------------|
| **Audit Lead** | Overall audit schedule, report sign-off, escalation |
| **Auditor** | Conduct audits, document findings, follow up |
| **Security Liaison** | Security findings review, vulnerability triage |
| **Compliance Officer** | ISO/GDPR alignment, regulatory updates |
| **Team Lead** | Provide access, evidence, remediate findings |

---

## 13. Related Documents

| Document | Purpose |
|----------|---------|
| `Techversant_Git_Workflow.md` | Branching, commits, PR process |
| `general/ai-era-coding-guidelines.md` | AI-assisted development standards |
| `cf/coldfusion-code-review-checklist.md` | CFML review checklist |
| `nodejs/nodejs-typescript-code-review-checklist.md` | Node.js review checklist |
| `general/rest-api-best-practices.md` | API standards |
| `git/secrets.env` | (Template) Secret management |

---

**Document Owner:** CoE Audit Team
**Review Cycle:** Quarterly
**Next Review:** August 2026