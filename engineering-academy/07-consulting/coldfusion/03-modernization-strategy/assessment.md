# Phase 3 Assessment: Modernization Strategy

> Test your ability to recommend and justify modernization approaches.

## Instructions

Answer all questions. Show your work.

**Time:** 1.5 hours
**Passing Score:** 70%

---

## Section A: Option Analysis (30 points)

### Scenario

**Client:** Healthcare billing company
**Application:** Patient billing system, CF 10, 250 CFM files, MSSQL, plain CFM with includes, built in 2009
**Context:** HIPAA compliance required, team of 4 CF developers, tight budget

### A1: Option Comparison (15 points)

For each modernization option, provide:

| Option | When It Makes Sense | Key Risks | Healthcare Fit |
|--------|--------------------| ----------|----------------|
| Stay on CF | | | |
| Migrate to Lucee | | | |
| Cloud migration | | | |
| Strangler fig | | | |

### A2: Recommendation (15 points)

**Your recommendation:** ___________________________________

**Top 3 reasons supporting this recommendation:**

1. _______________________________________________________
2. _______________________________________________________
3. _______________________________________________________

**Top 3 risks and mitigations:**

| Risk | Mitigation |
|------|------------|
| | |
| | |
| | |

---

## Section B: Business Case (25 points)

### B1: Cost Analysis (10 points)

Calculate ROI for a Lucee migration:

| Cost Item | Amount |
|-----------|--------|
| Assessment | $30,000 |
| Migration | $120,000 |
| Testing | $20,000 |
| Training | $10,000 |
| **Total Investment** | |

| Benefit Item | Annual Amount |
|--------------|---------------|
| Reduced maintenance | $25,000 |
| Faster development | $30,000 |
| Reduced security risk | $15,000 |
| **Annual Benefits** | |

**ROI (3-year):**
```
ROI = (Total Benefits - Investment) / Investment × 100 = ___%
```

### B2: Break-Even Analysis (8 points)

If annual benefits are $70,000 and investment is $180,000:

**Break-even point:** Month ___ of Year ___

**Explain your calculation:**
_______________________________________________________
_______________________________________________________

### B3: Risk-Adjusted Value (7 points)

| Scenario | Probability | Net Benefit | Weighted Value |
|----------|-------------|-------------|----------------|
| Base | 50% | $30,000 | |
| Optimistic | 30% | $100,000 | |
| Pessimistic | 20% | -$20,000 | |

**Expected Value:** ___________________________________

---

## Section C: Roadmap (20 points)

### C1: Phase Design (10 points)

Design 4 phases for the healthcare migration:

| Phase | Duration | Key Activities |
|-------|----------|----------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| **Total** | ___ weeks | |

### C2: Critical Path (10 points)

What must happen before you can start Phase 3 (Cloud)?

1. _______________________________________________________
2. _______________________________________________________
3. _______________________________________________________

What is the longest path through your roadmap?

_______________________________________________________

---

## Section D: Client Communication (25 points)

### D1: Executive Translation (15 points)

Translate this technical finding for a CEO:

**Technical:** "We found SQL injection vulnerabilities in the patient lookup form and recommend immediate remediation before pursuing any modernization work."

**CEO Translation:**
_______________________________________________________
_______________________________________________________
_______________________________________________________

### D2: Handling Objections (10 points)

**Objection:** "We don't have the budget for this right now."

**Your response:**
_______________________________________________________
_______________________________________________________
_______________________________________________________

---

## Answer Key

### Section A
- A1: Healthcare context favors Lucee (cost) with cloud for compliance/backup
- A2: Recommendation should address HIPAA, budget, and team capacity

### Section B
- B1: Total $180k investment, $70k annual benefits
- B2: Break-even = $180k / $70k = 2.57 years (month 7 of year 3)
- B3: Expected value = $30k (expected value calculation)

### Section C
- C1: Typical 4-phase: Assessment → Foundation → Migration → Testing
- C2: Cloud requires completed migration testing, compliance review

### Section D
- D1: Should focus on patient data risk, regulatory compliance, liability
- D2: Should offer phased approach, quick wins, or smaller scope

---

## Scoring Guide

| Section | Points | Your Score |
|---------|--------|------------|
| A: Option Analysis | 30 | |
| B: Business Case | 25 | |
| C: Roadmap | 20 | |
| D: Communication | 25 | |
| **Total** | **100** | |

**Passing Score:** 70/100
