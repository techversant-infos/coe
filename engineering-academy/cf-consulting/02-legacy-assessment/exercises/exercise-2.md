# Exercise 2: Technical Debt Scoring

> Score an application across technical debt dimensions.

## Objective

Learn to systematically assess and score technical debt in ColdFusion applications.

## Scenario

**Application:** E-commerce platform built in 2010
- ~150 CFM files
- Plain CFM with includes
- MSSQL database (40 tables)
- No version control
- Custom authentication
- No tests

## Instructions

### Part 1: Code Quality Assessment

Score each dimension 1-5:

| Dimension | Score (1-5) | Evidence |
|-----------|--------------|----------|
| **Complexity** | | |
| Naming conventions | | |
| Function/component size | | |
| Nested logic depth | | |
| Code duplication | | |
| | **Subtotal: ___** | |
| **Documentation** | | |
| Code comments | | |
| README files | | |
| API documentation | | |
| Architecture diagrams | | |
| | **Subtotal: ___** | |
| **Structure** | | |
| File organization | | |
| Naming consistency | | |
| Separation of concerns | | |
| Component design | | |
| | **Subtotal: ___** | |

### Part 2: Testing Coverage

Assess testing coverage:

| Aspect | Status | Evidence |
|--------|--------|----------|
| Unit tests | | |
| Integration tests | | |
| E2E tests | | |
| Code coverage tool | | |
| CI/CD with tests | | |

**Testing Debt Score:** ___/5

### Part 3: Dependency Assessment

| Dependency | Version | Risk | Notes |
|-----------|---------|------|-------|
| ColdFusion | 10 | High | EOL in 2020 |
| jQuery | 1.x | Medium | |
| Bootstrap | 3.x | Low | |
| MSSQL Driver | Unknown | | |

**Dependency Debt Score:** ___/5

### Part 4: Security Posture

| Security Aspect | Score | Notes |
|----------------|-------|-------|
| Authentication | | |
| Authorization | | |
| SQL injection protection | | |
| XSS protection | | |
| CSRF protection | | |
| Password storage | | |
| Session management | | |
| SSL/TLS | | |

**Security Debt Score:** ___/5

### Part 5: Calculate Overall Debt Score

**Scoring Formula:**

```
Code Quality Debt = (Complexity + Documentation + Structure) / 3
Testing Debt = Testing Coverage Score
Dependency Debt = Dependency Assessment Score
Security Debt = Security Posture Score

Total Debt = (Code Quality + Testing + Dependency + Security) / 4
```

| Category | Score |
|----------|-------|
| Code Quality Debt | ___/5 |
| Testing Debt | ___/5 |
| Dependency Debt | ___/5 |
| Security Debt | ___/5 |
| **Total Debt Score** | ___/20 |

### Part 6: Interpret the Score

| Score | Rating | Recommendation |
|-------|--------|----------------|
| 0-5 | Excellent | Minimal debt |
| 6-10 | Good | Minor improvements |
| 11-15 | Moderate | Address high-priority items |
| 16-20 | High | Significant modernization needed |
| 20+ | Critical | Rewrite likely cheaper |

**Your Score:** ___ → Rating: ________________

### Part 7: Remediation Priority

Create a prioritized list:

| Priority | Issue | Estimated Effort | Impact |
|----------|-------|-----------------|--------|
| P1 - Critical | | | |
| P2 - High | | | |
| P3 - Medium | | | |
| P4 - Low | | | |

## Expected Outcome

1. Completed debt scoring tables
2. Overall debt score with interpretation
3. Prioritized remediation list

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Scoring thoroughness | 25 |
| Evidence provided | 20 |
| Score calculation correct | 15 |
| Interpretation accurate | 20 |
| Remediation priority logical | 15 |
| Professional presentation | 5 |
| **Total** | **100** |

**Passing Score:** 70/100
