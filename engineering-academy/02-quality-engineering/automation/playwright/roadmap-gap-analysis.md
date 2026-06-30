# Automation Engineer Learning Path Gap Analysis (Reviewer-Only)

> **Audience:** CoE QA Working Group, automation leads, and curriculum reviewers not a reader-facing document.
> **Purpose:** Map this path to the testing-landscape and show what's covered, covered lightly, or deliberately skipped. Used during pilot review to validate scope decisions.

---

## How to read this document

- **Covered in depth** the path explicitly teaches this with a mini-task and self-check
- **Covered lightly** the path names the concept but does not have a full topic; pairs with a stack path or future version for the rest
- **Not covered (with reason)** the path deliberately skips this; the reason is given so a reviewer can challenge the call

A reviewer should scan this table and ask: *does the depth match the CoE's automation engineering needs for 2026?*

---

## Gap analysis: automation path vs. testing landscape

The automation engineering landscape is broad. The major branches a Techversant automation engineer needs to think about are: **E2E automation**, **API automation**, **CI/CD integration**, **test design**, **maintenance**, and **leadership**.

| Branch / topic | Status | Where / Why |
|---|---|---|
| **E2E Automation with Playwright** | Covered in depth | Phase 2-3 full coverage of Playwright fundamentals, locators, interactions, assertions |
| **Locator Strategies** | Covered in depth | Phase 2, Topic 5 prioritization from test IDs to CSS/XPath fallback |
| **Page Object Model** | Covered in depth | Phase 3, Topic 9 POM pattern with CoE standard application |
| **Test Parameterization** | Covered in depth | Phase 3, Topic 10 data-driven testing, fixtures, env configs |
| **API Automation** | Covered in depth | Phase 4 full coverage: request API, auth, data lifecycle, assertions |
| **CI/CD Integration** | Covered in depth | Phase 5 GitHub Actions, parallel execution, artifact reporting |
| **Performance Testing** | Covered lightly | Senior path covers lightweight performance awareness; dedicated load/performance tooling is not yet standardized |
| **Accessibility Testing** | Covered lightly | Senior path covers axe-core checks; manual keyboard/screen-reader review needs deeper guidance |
| **Mobile Testing** | Covered lightly | Playwright supports mobile emulation (`deviceScaleFactor`), but no dedicated topic. Pairs with the mobile-specific path for device-level testing. |
| **Visual Regression** | Covered lightly | Playwright supports screenshot comparison (`toHaveScreenshot()`), but no dedicated topic. Pairs with a future "visual regression" add-on if needed. |
| **Contract Testing** | Covered lightly | Referenced in passing via REST API testing, but no dedicated topic. Pairs with API contract testing standards if the team adopts that. |
| **Security Testing** | Covered lightly | Security testing is its own discipline. Pairs with the Security Audit Checklist. |
| **Test Reporting & Metrics** | Covered lightly | Senior path covers reports and flake tracking; dashboard templates are still missing |
| **Mentoring & Leadership** | Covered in depth | Senior automation Phase 10 includes review, mentoring, standards, and team guidance |
| **Unit Testing for Test Logic** | Not covered (with reason) | Test logic should be simple. If test assertions need unit tests, the test is too complex. Refactor instead. |
| **BDD/Gherkin Syntax** | Not covered (with reason) | Not the CoE standard. The CoE uses standard Playwright `test()` / `describe()` syntax. |
| **Manual Testing Techniques** | Covered separately | The manual testing baseline now covers exploratory testing, test design, bug reporting, regression, data, and release sign-off. |
| **Specific Framework Alternatives** | Not covered (with reason) | This path teaches Playwright, the CoE standard. Cypress/Selenium/Puppeteer alternatives are not covered. |

---

## What we deliberately skipped (and why)

These topics don't appear in this path. Listing the rationale for reviewer challenge:

- **Unit testing of test logic** if your test assertions need unit tests, your test is too complex. Refactor: split the test, simplify the assertion, or move logic to a service. The simpler your test logic, the more maintainable your suite.

- **BDD/Gherkin syntax** this syntax (`Given/When/Then`) is common but creates an extra translation layer. The CoE standard is direct Playwright: `test('should do X', async ({ page }) => { ... })`. No intermediate language needed.

- **Manual testing techniques** this path is for *on-ramping* manual testers to automation. The techniques (exploratory testing, mind-mapping, session-based testing) are the domain of manual testing training, not automation engineering.

- **Alternative frameworks (Cypress, Selenium, Puppeteer)** Playwright is the CoE standard. Teaching alternatives creates confusion. If a team has legacy tests in another framework, that's a migration conversation, not a learning path.

---

## Gaps that should probably be closed before full-team rollout

1. **Visual regression testing** one topic on `toHaveScreenshot()` for snapshot-based verification. Defer to v0.2 if visual regression is part of the workflow.
2. **Mobile device testing** a topic on Playwright's device emulation and configuring projects for different viewports. Defer to v0.2 if mobile testing is frequent.
3. **Contract testing** a topic on API contract verification (pact/consumer-driven contracts). Defer to v0.2 if the team adopts contract testing.

---

## Reviewer questions

1. For every **Covered lightly** row: *is the depth enough for our pilot batch, or does it block the transition from manual to automation?*
2. For every **Not covered** row: *is the reason still valid in 2026?*
3. Does the phase structure align with how your team on-boards manual testers?
4. **Pre-full-team rollout:** the items in "Gaps that should probably be closed" can we land them in v0.2 before the full-team rollout?

---

## Document control

| Field | Value |
|---|---|
| Document | Automation Engineer Learning Path Gap Analysis |
| Version | 0.1 (draft maps against testing landscape) |
| Owner | CoE QA Working Group |
| Review Cycle | Quarterly |
| Status | Internal review document |
| Related | [intermediate.md](./intermediate.md), [README.md](./README.md), [Dev Excellence Curriculum](../../../00-engineering-foundations/dev-excellence/curriculum.md), [REST API Best Practices](../../../../general/rest-api-best-practices.md) |
