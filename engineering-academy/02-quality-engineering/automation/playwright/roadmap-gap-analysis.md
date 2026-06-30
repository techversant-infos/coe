# Automation Engineer Learning Path Gap Analysis (Reviewer-Only)

> **Audience:** CoE QA Working Group, automation leads, and curriculum reviewers not a reader-facing document.
> **Purpose:** Map this path to the testing-landscape and show what's covered, covered lightly, or deliberately skipped. Used during pilot review to validate scope decisions.

---

## How to read this document

- ** covered in depth** the path explicitly teaches this with a mini-task and self-check
- ** covered lightly** the path names the concept but does not have a full topic; pairs with a stack path or future version for the rest
- ** not covered (with reason)** the path deliberately skips this; the reason is given so a reviewer can challenge the call

A reviewer should scan this table and ask: *does the depth match the CoE's automation engineering needs for 2026?*

---

## Gap analysis: automation path vs. testing landscape

The automation engineering landscape is broad. The major branches a Techversant automation engineer needs to think about are: **E2E automation**, **API automation**, **CI/CD integration**, **test design**, **maintenance**, and **leadership**.

| Branch / topic | Status | Where / Why |
|---|---|---|
| **E2E Automation with Playwright** | | Phase 2-3 full coverage of Playwright fundamentals, locators, interactions, assertions |
| **Locator Strategies** | | Phase 2, Topic 5 prioritization from test IDs to CSS/XPath fallback |
| **Page Object Model** | | Phase 3, Topic 9 POM pattern with CoE standard application |
| **Test Parameterization** | | Phase 3, Topic 10 data-driven testing, fixtures, env configs |
| **API Automation** | | Phase 4 full coverage: request API, auth, data lifecycle, assertions |
| **CI/CD Integration** | | Phase 5 GitHub Actions, parallel execution, artifact reporting |
| **Performance Testing** | | Phase 6, Topic 21 Playwright performance profiling |
| **Accessibility Testing** | | Phase 6, Topic 21 axe-core integration |
| **Mobile Testing** | covered lightly | Playwright supports mobile emulation (`deviceScaleFactor`), but no dedicated topic. Pairs with the mobile-specific path for device-level testing. |
| **Visual Regression** | covered lightly | Playwright supports screenshot comparison (`toHaveScreenshot()`), but no dedicated topic. Pairs with a future "visual regression" add-on if needed. |
| **Contract Testing** | covered lightly | Referenced in passing via REST API testing (Phase 4), but no dedicated topic. Pairs with the API contract testing standards if the team adopts that. |
| **Security Testing** | covered lightly | Mentioned in Phase 6 as "test what you protect" security testing is its own discipline. Pairs with the Security Audit Checklist. |
| **Performance Profiling** | | Phase 6, Topic 21 CI thresholds, flaky detection |
| **Test Reporting & Metrics** | | Phase 6, Topic 20 flaky rates, coverage segmentation |
| **Mentoring & Leadership** | | Phase 6, Topic 22 career path documentation |
| **Unit Testing for Test Logic** | deliberately skipped | Test logic (the assertions themselves) should be simple. If your test logic needs unit tests, the test is too complex. Refactor instead. |
| **BDD/Gherkin Syntax** | deliberately skipped | Not the CoE standard. The CoE uses standard Playwright `test()` / `describe()` syntax. |
| **Manual Testing Techniques** | deliberately skipped | This is a manual tester *on-ramping* path, not manual technique training. Pairs with the Dev Excellence curriculum for the testing mindset. |
| **Specific Framework Alternatives** | deliberately skipped | This path teaches Playwright, the CoE standard. Cypress/Selenium/Puppeteer alternatives are not covered. |

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

1. For every ** covered lightly** row: *is the depth enough for our pilot batch, or does it block the transition from manual to automation?*
2. For every ** not covered** row: *is the reason still valid in 2026?*
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
