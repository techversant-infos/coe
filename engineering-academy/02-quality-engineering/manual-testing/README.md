# Manual Testing

This path gives testers the baseline needed before automation. Automation can run checks quickly, but manual testing still provides judgment: risk discovery, exploratory learning, product empathy, and release confidence.

> **Audience:** Junior QA engineers, manual testers, and automation learners who need stronger testing fundamentals.
> **Length:** 4-6 weeks, around 3-4 hours/week.
> **Goal:** Design, execute, and report useful tests for real product risk.
> **Level:** Foundation.
> **Next Level:** [Manual Tester to Automation Engineer](../automation/playwright/manual-to-automation.md).

## Learning Outcomes

By the end of this path, the learner should be able to:

1. Convert requirements into clear test scenarios.
2. Use equivalence partitioning and boundary value analysis.
3. Plan exploratory testing with a charter, not random clicking.
4. Report bugs with enough evidence for developers to reproduce and fix.
5. Identify regression risk for a release.
6. Prepare and clean up test data.
7. Give a release sign-off with risks, blockers, and known limitations.

## Suggested 6-Week Plan

| Week | Focus | Output / Definition of Done |
|---|---|---|
| 1 | Testing mindset and risk | Risk list for one feature area |
| 2 | Test case design | Test cases using happy path, edge cases, equivalence classes, and boundaries |
| 3 | Exploratory testing | Session charter, notes, and findings |
| 4 | Bug reporting | Three high-quality bug reports or sample defects |
| 5 | Regression and test data | Regression checklist and test data setup/teardown notes |
| 6 | Release sign-off | One-page test summary with risks, evidence, and recommendation |

---

## Phase 1 - Testing Mindset and Risk

**Goal:** Test the product risk, not only the requirement text.

**Learn:**

- Quality attributes: correctness, usability, accessibility, performance, security, reliability
- Risk-based testing
- User journeys and business impact
- Positive, negative, and destructive scenarios
- What should be checked manually vs. automated later

**Mini-task:** Pick one feature. List the top 10 things that could go wrong, who would be affected, and how serious each failure would be.

**Useful resource:** [Google Testing Blog - Test Pyramid](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)

---

## Phase 2 - Test Case Design

**Goal:** Design tests that find meaningful defects instead of repeating the same happy path.

**Learn:**

- Test scenarios vs. test cases
- Equivalence partitioning
- Boundary value analysis
- Decision tables
- State transitions
- Acceptance criteria traceability

**Mini-task:** For a form or workflow, create test cases covering valid inputs, invalid inputs, boundary values, missing fields, duplicate submission, and permission errors.

**Useful resource:** [ISTQB Glossary](https://glossary.istqb.org/)

---

## Phase 3 - Exploratory Testing

**Goal:** Explore with discipline and evidence.

**Learn:**

- Session-based testing
- Test charters
- Note taking
- Heuristics: input, interruption, permissions, browser/device, data state
- When exploratory findings should become regression checks

**Mini-task:** Run a 60-minute exploratory session using a charter. Capture notes, screenshots/video where useful, bugs found, and follow-up test ideas.

**Useful resource:** [Ministry of Testing](https://www.ministryoftesting.com/)

---

## Phase 4 - Bug Reporting

**Goal:** Make defects easy to understand, reproduce, prioritize, and fix.

**Learn:**

- Clear title
- Environment and build/version
- Preconditions and test data
- Steps to reproduce
- Expected vs. actual result
- Evidence: screenshots, video, logs, network details
- Severity vs. priority
- Duplicate and intermittent bug handling

**Mini-task:** Rewrite three existing vague bug reports into developer-ready reports.

**Bug report template:**

```md
## Summary

## Environment

## Preconditions / Test Data

## Steps to Reproduce

## Expected Result

## Actual Result

## Evidence

## Severity / Priority Suggestion
```

---

## Phase 5 - Regression Planning and Test Data

**Goal:** Make regression testing repeatable without pretending every old test has equal value.

**Learn:**

- Smoke vs. sanity vs. regression
- Critical path selection
- Test data setup and teardown
- Data privacy: no production PII in lower environments
- Browser/device coverage
- Defect retesting and impacted-area testing

**Mini-task:** Create a regression checklist for one feature area. Mark each item as smoke, critical regression, or optional regression.

**Internal standard:** [Security Audit Checklist](../../../audit/security-audit-checklist.md)

---

## Phase 6 - Release Sign-Off

**Goal:** Communicate product readiness clearly.

**Learn:**

- Test summary reports
- Open defects and risk acceptance
- Blocker vs. known issue
- Evidence links
- Go / no-go recommendation
- Handoff to support or implementation team

**Mini-task:** Write a release test summary for a small feature release.

**Sign-off template:**

```md
## Scope Tested

## Not Tested / Out of Scope

## Environments

## Test Evidence

## Open Defects

## Known Risks

## Recommendation
Go / No-Go / Go with accepted risks
```

## Readiness Checklist

- [ ] I can explain the main product risks before writing test cases.
- [ ] I can design tests using boundaries and equivalence classes.
- [ ] I can run an exploratory session with a charter.
- [ ] I can write a reproducible bug report.
- [ ] I can plan regression by risk.
- [ ] I can write a release sign-off with evidence and known risks.

## Related Paths

- [Manual Tester to Automation Engineer](../automation/playwright/manual-to-automation.md)
- [Automation Strategy](../strategy/automation-strategy.md)
- [QA Capstone Rubric](../capstone-qa-rubric.md)
