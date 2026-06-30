# Automation Strategy

Automation strategy answers a different question from automation scripting.

- Scripting asks: "How do I automate this?"
- Strategy asks: "Should this be automated, at which layer, and how will we maintain it?"

**Level:** Advanced
**Next Level:** [Career Progression: QA Leadership](../../career-progression/lead-to-architect.md)

## Core Questions

1. What risk does this test reduce?
2. Is UI automation the right layer, or would an API/component/unit test be better?
3. How often will this test run?
4. How expensive will it be to maintain?
5. What data does it need?
6. What failure should block a release?
7. How will flaky tests be detected and handled?
8. What test data does this require, and who owns cleanup?
9. What evidence will the test produce when it fails?
10. How will this test stay useful when the product changes?

## Automation ROI Rule

Automate when the test is:

- high-value,
- repeatable,
- stable enough to maintain,
- tied to a real release risk,
- and likely to run many times.

Keep manual when the test is exploratory, one-off, highly visual, or based on fast-changing requirements.

## Layer Selection Guide

| Risk / question | Preferred layer | Notes |
|---|---|---|
| Pure business rule | Unit or service test | Fastest feedback; no browser required |
| API contract, validation, status codes, error shape | API test | Pair with [REST API Best Practices](../../../general/rest-api-best-practices.md) |
| Integration between services or adapters | Integration test | Use realistic dependencies where practical |
| Critical user journey | UI E2E test | Keep count small; cover only release-critical journeys |
| Layout, visual polish, exploratory usability | Manual review or visual regression | Automate screenshots only when the UI is stable |
| Accessibility rules | Automated axe check plus manual keyboard/screen-reader review | Automation catches only part of accessibility |
| Performance regression | Lightweight timing check or dedicated performance tool | Use baselines; avoid noisy thresholds |

## Quality Gates

Use gates to protect delivery, not to create noise.

| Gate | Blocks release? | Owner |
|---|---|---|
| Smoke suite fails on main user journey | Yes | QA + feature owner |
| Critical API contract fails | Yes | Backend/API owner |
| New blocker or critical defect open | Yes | Product + QA + engineering lead |
| Known flaky test fails | No, if quarantined and tracked | Automation owner |
| Accessibility violation on critical flow | Depends on severity and user impact | QA + UX + engineering lead |
| Performance regression against agreed baseline | Depends on threshold and impact | QA + engineering lead |

## Metrics That Matter

Track metrics that lead to action:

- Escaped defects by feature area and root cause
- Automation pass rate and flaky-test rate
- Average time to diagnose failed CI automation
- Smoke-suite duration
- Critical journey coverage
- Defect reopen rate
- Accessibility and performance findings by severity

Avoid metrics that only create theater:

- Raw number of test cases
- Raw automation count without risk context
- Line coverage as a release-quality proxy
- Pass percentage without severity or scope

## Test Data Strategy

Every automation plan should answer:

1. What data is created by the test?
2. Can the test run in parallel?
3. How is data cleaned up?
4. Does the test depend on shared state?
5. Are secrets and PII avoided?
6. Can failed data be inspected after CI runs?

## Strategy Template

```md
## Feature / Area

## Critical Risks

## Test Layers

## Automated Coverage

## Manual / Exploratory Coverage

## Test Data

## CI / Release Gates

## Flake and Maintenance Risks

## Metrics to Watch
```

## Related Paths

- [Manual Tester to Automation Engineer](../automation/playwright/manual-to-automation.md)
- [Automation Engineer to Senior Automation Engineer](../automation/playwright/senior-automation.md)
- [REST API Best Practices](../../../general/rest-api-best-practices.md)
- [Security Audit Checklist](../../../audit/security-audit-checklist.md)
