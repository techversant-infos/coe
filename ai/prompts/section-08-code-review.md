# 🔍 Section 8 — Prompt for Code Review

> **Module:** Employee Management (Create / Update / Delete / Get Employee)
> **Purpose:** Get a structured, thorough code review with severity-rated findings — not vague comments like *"this could be improved"*.

---

## 📋 Table of Contents

- [Why Use a Structured Review Prompt?](#why-use-a-structured-review-prompt)
- [The Prompt](#the-prompt)
- [Review Coverage Summary](#review-coverage-summary)
- [What Each Issue Report Includes](#what-each-issue-report-includes)
- [Severity Level Reference](#severity-level-reference)
- [Tips for Code Review Prompts](#tips-for-code-review-prompts)

---

## Why Use a Structured Review Prompt?

A vague prompt like `"review my code"` produces surface-level feedback with no priorities and no fixes.

> ❌ **Vague prompt:** "The naming could be better. Consider adding more error handling."
>
> ✅ **This prompt:** File name, method, severity rating (HIGH/MEDIUM/LOW), exact description of the problem, and corrected code snippet.

---

## The Prompt

```
You are a senior software engineer with 10+ years of experience,
specialising in code quality, security, and best practices.

Please conduct a thorough code review of my Employee Management
Module code provided below.

Review the following areas and check each one systematically:

CODE QUALITY
  1. Clean code principles (readability, naming, single responsibility)
  2. SOLID principles — identify any violations with explanation
  3. DRY principle — identify any duplicated logic

SECURITY
  4. SQL Injection vulnerabilities
  5. Input validation gaps — missing or insufficient validation
  6. Sensitive data exposure in logs or API responses

PERFORMANCE
  7. N+1 query problems
  8. Missing or incorrect database index usage
  9. Inefficient loops, queries, or data processing

BEST PRACTICES
  10. Correct and appropriate use of framework annotations
  11. Exception handling completeness and meaningful error messages
  12. API response structure consistency across all endpoints
  13. Language naming conventions (class, method, variable)

TESTING
  14. Missing unit or integration tests
  15. Edge cases not covered by existing tests

For EACH issue found, provide:
  - File name and method / line reference (if applicable)
  - Clear description of the problem
  - Severity: HIGH / MEDIUM / LOW
  - Corrected code snippet showing the fix

End with:
  - Overall code quality score out of 10
  - Summary of top 3 priority fixes

[PASTE YOUR CODE BELOW THIS LINE]
```

---

## Review Coverage Summary

| Area | What Gets Checked |
|------|------------------|
| **Code Quality** | Clean code, SOLID principles, DRY violations, naming conventions |
| **Security** | SQL injection, validation gaps, sensitive data in logs |
| **Performance** | N+1 queries, missing indexes, inefficient processing |
| **Best Practices** | Annotations, exception handling, API response consistency |
| **Testing** | Missing unit or integration tests, uncovered edge cases |

---

## What Each Issue Report Includes

For every issue the AI finds, it provides all four of these:

```
File:      EmployeeService.java — method: createEmployee()
Problem:   Salary is accepted as a String and not validated for negative values.
           A negative salary passes validation and gets saved to the database.
Severity:  HIGH
Fix:
  // Before
  public Employee createEmployee(String salary) { ... }

  // After
  @Positive(message = "Salary must be a positive value")
  @DecimalMin(value = "0.01", message = "Salary cannot be zero or negative")
  private BigDecimal salary;
```

---

## Severity Level Reference

| Severity | Meaning | Action Required |
|----------|---------|----------------|
| 🔴 **HIGH** | Security vulnerability, data loss risk, or critical bug | Fix before merging — do not ship |
| 🟡 **MEDIUM** | Performance issue or incorrect behaviour under certain conditions | Fix in the same sprint if possible |
| 🟢 **LOW** | Style, naming, or minor readability issue | Fix when touching the file next time |

---

## Tips for Code Review Prompts

| Tip | Why It Helps |
|-----|-------------|
| Paste one file or layer at a time | Keeps the review focused and detailed |
| Specify the language and framework | Allows framework-specific annotation checks |
| Ask for severity ratings | Helps you prioritise what to fix first |
| Request corrected snippets | Gives you ready-to-use fixes, not just descriptions |
| Ask for a score out of 10 | Gives a trackable quality metric across sprints |
| End with top 3 priority fixes | Ensures you know exactly what to tackle first |

---

> 💡 **Pro Tip:** Replace `[PASTE YOUR CODE BELOW THIS LINE]` with your actual code. For best results, paste one layer at a time — for example, paste only the Service layer first, then the Controller separately. This gives more detailed, focused feedback per layer.

---

*Section 8 of 9 · Developer Prompt Handbook · Employee Management Module*
