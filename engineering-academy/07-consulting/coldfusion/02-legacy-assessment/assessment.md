# Phase 2 Assessment: Legacy Application Assessment

> Test your ability to assess and document legacy ColdFusion applications.

## Instructions

Answer all questions. Show your work where applicable.

**Time:** 2 hours
**Passing Score:** 70%

---

## Section A: Framework Detection (20 points)

### A1. Identify the Framework (10 points)

For each directory structure, identify the framework:

**A.** `/handlers /models /views /layouts /Application.cfc (extends FW1)`
Framework: _______________________

**B.** `/coldbox /config /handlers /models /wirebox`
Framework: _______________________

**C.** `/cfc /cfm /udf application.cfm`
Framework: _______________________

### A2. Migration Difficulty Ranking (10 points)

Rank these frameworks by migration difficulty (1 = easiest, 5 = hardest):

| Framework | Rank |
|-----------|------|
| Plain CFM | |
| FW/1 | |
| ColdBox | |
| Fusebox | |
| Custom MVC | |

---

## Section B: Technical Debt Assessment (25 points)

### B1. Score this Application (15 points)

Rate each category 1-5 and calculate debt:

| Category | Score (1-5) | Evidence/Notes |
|----------|--------------|----------------|
| Code Complexity | | Complex nested cfifs |
| Code Documentation | | No comments |
| Test Coverage | | 0% |
| Dependency Age | | CF 9, jQuery 1.4 |
| Security Posture | | SQL injection present |
| | **Subtotal: ___/25** | |

### B2. Interpret the Score (10 points)

Total Score: ___/25

| Score | Rating | Recommendation |
|-------|--------|----------------|
| 0-5 | Excellent | Continue as-is |
| 6-10 | Good | Minor improvements |
| 11-15 | Moderate | Plan improvements |
| 16-20 | High | Modernization needed |
| 21-25 | Critical | Urgent action required |

**Your Interpretation:** _____________________

**Priority Remediation Items (3):**

1. _______________________________________________________
2. _______________________________________________________
3. _______________________________________________________

---

## Section C: Security Assessment (25 points)

### C1. Identify Vulnerabilities (15 points)

For each code snippet, identify the vulnerability:

**Snippet 1:**
```cfml
<cfquery>
    SELECT * FROM users 
    WHERE id = #url.id#
</cfquery>
```

Vulnerability: _______________________________________
Risk: _______________________________________________

**Snippet 2:**
```cfml
<cfoutput>
    #userComment#
</cfoutput>
```

Vulnerability: _______________________________________
Risk: _______________________________________________

**Snippet 3:**
```cfml
<cffile action="upload" 
        destination="#ExpandPath('./uploads/')#">
```

Vulnerability: _______________________________________
Risk: _______________________________________________

### C2. Risk Assessment (10 points)

Rate the likelihood and impact of these findings:

| Finding | Likelihood (1-5) | Impact (1-5) | Risk Score |
|---------|------------------|--------------|------------|
| SQL injection in login | | | |
| Session fixation | | | |
| Exposed CFIDE | | | |
| No CSRF tokens | | | |

(Risk Score = Likelihood × Impact)

---

## Section D: Assessment Documentation (15 points)

### D1. Executive Summary (8 points)

Rewrite this vague summary as a professional one:

**Vague:** "We looked at the code and there's some stuff that needs fixing. The main issues are security and old code."

**Professional Rewrite:**
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________

### D2. Prioritization (7 points)

The client can only afford to fix 3 issues. Which do you prioritize and why?

| # | Issue | Priority | Justification |
|---|-------|----------|----------------|
| 1 | SQL injection | | |
| 2 | CF version EOL | | |
| 3 | No tests | | |
| 4 | Performance issues | | |
| 5 | Missing docs | | |

**Top 3:** 1, ___, ___

---

## Section E: Consultation Skills (15 points)

### E1. Client Communication (8 points)

Client asks: "How bad is our situation on a scale of 1-10?"

Rate and respond professionally:

| Technical Score | Client Translation | Response |
|-----------------|---------------------|----------|
| 8/10 | "Your codebase is well-maintained" | "Your application is in good shape with minimal issues to address" |
| 15/25 | | |
| 22/25 | | |

### E2. Recommendation Framing (7 points)

How would you frame this recommendation to a non-technical CEO?

**Technical Fact:** "We recommend migrating from CF9 to CF2023 due to end-of-life status and security vulnerabilities."

**CEO Translation:**
_______________________________________________________________
_______________________________________________________________
_______________________________________________________________

---

## Answer Key

### Section A
- A1: A = FW/1, B = ColdBox, C = Plain CFM
- A2: Plain CFM (1), FW/1 (2), ColdBox (3), Fusebox (4), Custom MVC (5)

### Section B
- B1: Scoring based on evidence provided
- B2: Any score 16+ = High/Critical, priority items depend on score

### Section C
- C1: SQL injection, XSS, File upload vulnerability
- C2: Risk scores calculated as Likelihood × Impact

### Section D
- D1: Should be specific, quantified, professional
- D2: Security and EOL typically highest priority

### Section E
- E1: Score / 25 × 10 = Client scale
- E2: Business impact, not technical terms

---

## Scoring Guide

| Section | Points | Your Score |
|---------|--------|------------|
| A: Framework Detection | 20 | |
| B: Technical Debt | 25 | |
| C: Security | 25 | |
| D: Documentation | 15 | |
| E: Consultation | 15 | |
| **Total** | **100** | |

**Passing Score:** 70/100
