# AI-Assisted Testing Practice Guide

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

Use AI to help draft and investigate tests while keeping test intent, risk selection and final acceptance with the
engineer. This guide covers AI used in QA work; building AI-enabled products is in the
[AI Engineering Roadmap](../06-ai-engineering/README.md).

## Where AI can help

- Turn an existing requirement or manual scenario into candidate test cases
- Draft Playwright test scaffolding using the project's actual fixtures and locator conventions
- Suggest boundary, error and accessibility cases for a human to select
- Explain a Playwright trace, stack trace or API response using sanitized evidence
- Refactor duplicated test code without changing the behavior under test

## Workflow

1. **Choose the risk.** The tester names the user risk and expected behavior before asking for test ideas.
2. **Provide safe context.** Share only the relevant synthetic or approved information, test framework, existing
   fixture patterns and constraints. Do not paste secrets, credentials, production data, PII or client data.
3. **Ask for candidates.** Request a small set of cases tied to the named risk, including assumptions and missing
   information.
4. **Check against the product contract.** Compare suggestions with requirements, API schemas, accessibility
   expectations and existing tests. Reject invented behavior.
5. **Implement and run.** Adapt the useful cases, run them against the application and inspect failures and traces.
6. **Review and own.** The engineer verifies assertions, test data, selectors, cleanup and whether the test would
   fail for the intended regression before committing.

## Example prompt

```text
Context: Playwright, TypeScript. Use only the fixture and locator patterns shown below.
Risk: A user cannot submit a support request without a subject.
Task: Suggest three tests for the required-subject behavior.
Constraints: Do not invent copy or selectors. Do not modify production code. Mark assumptions.
Output: For each test, give the risk, setup, action, expected result and any missing requirement.
```

## Review checklist

- [ ] Every test maps to a requirement, risk or defect
- [ ] Assertions check user-visible behavior or a meaningful contract, not implementation trivia
- [ ] Selectors use the repository's accessible locator conventions
- [ ] The test includes setup, isolation and cleanup appropriate to the suite
- [ ] Generated assertions do not merely restate the code's current behavior
- [ ] Failure output and traces contain no secrets or sensitive data
- [ ] The test fails when the intended defect is introduced and passes for the correct behavior
- [ ] A human can explain why the test matters and maintain it

Use the [Playwright Automation path](./02-automation/playwright/README.md) for test implementation and
[Techversant's AI Era Coding Guidelines](../../standards/general/ai-era-coding-guidelines.md) for delegation and
data-handling boundaries.
