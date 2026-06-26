# Automation Strategy

Automation strategy answers a different question from automation scripting.

- Scripting asks: "How do I automate this?"
- Strategy asks: "Should this be automated, at which layer, and how will we maintain it?"

## Core Questions

1. What risk does this test reduce?
2. Is UI automation the right layer, or would an API/component/unit test be better?
3. How often will this test run?
4. How expensive will it be to maintain?
5. What data does it need?
6. What failure should block a release?
7. How will flaky tests be detected and handled?

## Automation ROI Rule

Automate when the test is:

- high-value,
- repeatable,
- stable enough to maintain,
- tied to a real release risk,
- and likely to run many times.

Keep manual when the test is exploratory, one-off, highly visual, or based on fast-changing requirements.

## Related Paths

- [Manual Tester to Automation Engineer](../automation/playwright/manual-to-automation.md)
- [Automation Engineer to Senior Automation Engineer](../automation/playwright/senior-automation.md)
- [REST API Best Practices](../../general/rest-api-best-practices.md)