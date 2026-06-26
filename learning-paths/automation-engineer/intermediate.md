# Automation Engineer Learning Path (Manual Tester → Automation Engineer)

> **Objective:** Transform manual testers into automation engineers who can own end-to-end and API test automation — using Playwright as the CoE standard.
> **Audience:** Manual testers who want to automate + existing automation engineers who want to mature. Two tracks in one path.
> **Read alongside:** [README.md](./README.md) (prerequisites, entry points), [REST API Best Practices](../../general/rest-api-best-practices.md) (Phase 4), [Dev Excellence Curriculum](../dev-excellence/curriculum.md) (discipline).
> **Status:** Draft for pilot batch review — v0.1.

---

## 🎯 Learning Outcomes

After completing this path, an automation engineer will:

- Write automated tests that verify user workflows end-to-end — not just unit checks
- Apply test design patterns (page objects, parameterized tests, fixtures) that survive code changes
- Automate API testing alongside E2E — the full coverage picture
- Integrate tests into CI/CD pipelines — automated, not manual
- Report test results effectively — clear pass/fail, flaky detection, accessibility metrics
- Mentor manual testers on automation — the career path they wish they'd had

---

## 📚 Table of Contents

### 🔵 Manual Tester Track (Phases 1-3)

- [Phase 1: Automation Mindset](#phase-1-automation-mindset-beginner)
  - 1. Testing Mindset Shift
  - 2. Code Literacy Fundamentals
  - 3. Debugging Mindset

- [Phase 2: Playwright Fundamentals](#phase-2-playwright-fundamentals-intermediate)
  - 4. Playwright Core Concepts
  - 5. Locator Strategies
  - 6. Basic Interactions & Actions
  - 7. Assertions & Expect

- [Phase 3: Test Design & Maintenance](#phase-3-test-design-and-maintenance-intermediate)
  - 8. Test Organization
  - 9. Page Object Model
  - 10. Test Parameterization
  - 11. Test Maintenance Patterns
  - 12. Debugging & Troubleshooting

### 🟡 Automation Engineer Track (Phases 4-6)

- [Phase 4: API Automation](#phase-4-api-automation-advanced)
  - 13. API Testing Fundamentals
  - 14. Authentication & Sessions
  - 15. Data Setup & Teardown
  - 16. Advanced Assertions

- [Phase 5: CI/CD Integration](#phase-5-cicd-integration-advanced)
  - 17. CI Pipeline Foundations
  - 18. Parallel Execution
  - 19. Artifacts & Reporting

- [Phase 6: Quality & Maturity](#phase-6-quality-and-maturity-leadership-track)
  - 20. Test Reporting & Metrics
  - 21. Performance & Accessibility
  - 22. Mentoring & Leadership

---

## Prerequisites (complete before Phase 1)

Before Phase 1, make sure you have:

- **Access to a test codebase** where you can create a PR. If you're between projects, your tech lead should provide a sandbox repo.
- **A GitHub account** with push access to the test repo.
- **A code editor installed** (VS Code recommended).
- **Node.js 18+ installed** locally (`node --version` to verify).
- **Basic command-line comfort** (`cd`, `ls`, `git status` don't scare you).
- **Completed dev-excellence Phase 1-2** OR have 6+ months of manual testing experience. This path teaches automation, not testing fundamentals.

---

## 🔵 Phase 1 — Automation Mindset (Beginner)

**Goal:** Shift from "I verify behavior manually" to "I verify behavior through code."

### 1. Testing Mindset Shift

**Learn:**

- **Manual vs. Automated Testing — The Paradigm Shift:** Manual testing is exploratory; automated testing is deterministic. A manual tester asks "what happens if I do this?" An automation engineer asks "how do I verify this happens every time I run the test?"
- **WhatAutomates Well vs. What Doesn't:** High-value automations — regression suites, smoke tests, critical user journeys. Low-value automations — one-off exploratory tests, UI that changes weekly. The ROI test: "will I run this 10+ times?"
- **The Automation Pyramid:** Unit tests (fast, brittle) → Integration tests (medium speed, medium value) → E2E tests (slow, highest confidence). Automate the pyramid; don't skip levels.

**Mini-task:**
Pick 3 manual test cases you're running this week. For each, ask: (1) "will I run this 10+ times?" (2) "is the underlying UI stable?" (3) "does it take >1 minute to execute manually?" Open a doc PR that explains which 3 you'd automate and why. Tag `docs(automation-1)`.

**Self-check:**
- [ ] I can explain why some tests are better suited for automation than others
- [ ] I can identify the "ROI" factors for automating a test case
- [ ] I understand the automation pyramid and where E2E fits

---

### 2. Code Literacy Fundamentals

**Learn:**

- **JavaScript/TypeScript for Testers:** You don't need to be a developer. You need to read test code, modify selectors, and understand test failure messages. Key concepts: variables, functions (`function name() {}`), objects (`{ key: value }`), arrays (`[item1, item2]`), and control flow (`if/else`, `for` loops).
- **Reading Error Messages:** Playwright errors tell you exactly what's wrong — "element not found," "timeout waiting for," "assertion failed." The skill is reading the error, not guessing.
- **Test Structure Basics:** `test()` blocks, `describe()` suites, `beforeEach()` setup. Copy the pattern; modify the specifics.

**Mini-task:**
Create a playground file in your test repo. Write these 5 snippets, run them, verify they work: (1) a simple `console.log`, (2) a function that adds two numbers, (3) an array with `.map()`, (4) a conditional `if/else`, (5) a basic test with Playwright's `test()`. Commit as `test(literacy): <your-name>-playground`. This is just the basics — you don't need to memorize; you need to recognize.

**Self-check:**
- [ ] I can read basic JavaScript/TypeScript without panicking
- [ ] I understand what `test()`, `describe()`, and `beforeEach()` do in a test file
- [ ] I can run a Playwright test locally and interpret the output

---

### 3. Debugging Mindset

**Learn:**

- **Debugging vs. Guessing:** The manual tester re-runs to see if it's flaky. The automation engineer reads the error, checks the selector, reproduces locally. Debugging is a systematic skill; guessing is a time-waster.
- **The Debug Flow:** (1) Read the error message — it tells you exactly what failed. (2) Check the timeline — Playwright records video/network on failure. (3) Verify the locator — is the element still there? (4) Isolate the test — run just the failing test to reproduce. (5) Fix and verify.
- **Console Logging for Tests:** `console.log()` in your test to trace execution. Playwright's `page.on()` events to trace network. The skill is knowing where to look.

**Mini-task:**
Take a failing Playwright test (yours or a teammate's). Debug it systematically: (1) read the error, (2) check Playwright trace viewer, (3) verify the locator, (4) isolate the test, (5) fix. Document your process in a comment on the fix PR. Commit with `test(debug): <test-name>-fix`.

**Self-check:**
- [ ] I can read a Playwright error message without confusion
- [ ] I know how to use Playwright's trace viewer to debug
- [ ] I can systematically debug a test instead of guessing

---

## 🔵 Phase 2 — Playwright Fundamentals (Intermediate)

**Goal:** Write your first automated tests. Go from "I understand the concept" to "I can write code that verifies behavior."

### 4. Playwright Core Concepts

**Learn:**

- **Why Playwright:** The CoE standard. Works across browsers (Chromium, Firefox, WebKit), auto-waits for elements, built-in parallelism, great API. Replaces Cypress/Selenium as the standard.
- **Playwright Test Architecture:** `test()` blocks, `playwright.config.ts`, projects (browser configurations), fixtures (test setup). The config drives the behavior; the test drives the assertions.
- **Running Tests:** `npx playwright test`, `npx playwright test --grep "<pattern>"`, `npx playwright test --trace on` for debugging. The CLI is your friend.

**Mini-task:**
Install Playwright in your test repo (`npm init playwright@latest`), configure it with one project (your browser), and run the default example test. Modify the test to verify something on your staging URL (e.g., "the homepage loads," "the title contains X"). Commit as `test(playwright-init): <your-name>`.

**Self-check:**
- [ ] I can install and configure Playwright in a new project
- [ ] I understand the `playwright.config.ts` structure
- [ ] I can run tests with different CLI flags (`--grep`, `--trace`)

---

### 5. Locator Strategies

**Learn:**

- **Locator Priority:** (1) Test IDs (`data-testid`) — most stable. (2) Role + accessible name (`getByRole('button', { name: 'Submit' })`) — semantic. (3) Text (`getByText('Submit')`) — fragile. (4) CSS/XPath — last resort.
- **Why Locators Matter:** Manual testers "see" the button. Automation engineers "locate" the button. If the UI changes, the test breaks. Stable locators survive small UI changes.
- **Playwright-Specific Locators:** `page.getByLabel()`, `page.getByPlaceholder()`, `page.getByRole()`, `page.getByTestId()`. These map to accessible patterns, not CSS selectors.

**Mini-task:**
Pick 5 elements on your staging app (buttons, inputs, links). Write a Playwright test that locates each element using: (1) `getByRole` for interactive elements, (2) `getByLabel` for form fields, (3) `getByTestId` (if available) for hard-to-locate elements. Commit with `test(locators): <your-name>-strategy`. Tag the PR with `refactor(automation-2)`.

**Self-check:**
- [ ] I can prioritize locators from most stable to least stable
- [ ] I can use Playwright's `getBy*` locators correctly
- [ ] I understand why test IDs improve test stability

---

### 6. Basic Interactions & Actions

**Learn:**

- **Playwright Actions:** `click()`, `fill()`, `type()`, `selectOption()`, `check()`, `uncheck()`, `hover()`. These auto-wait — Playwright waits for the element to be actionable before acting.
- **Actionability Checks:** Playwright checks: visible, stable, enabled, receving events. If any fails, the test fails with a clear error. No more "element not ready" flaky tests.
- **Page vs. Component Interactions:** `page.click()` for page-level interactions; `await component.click()` for component-level. Know what you're interacting with.

**Mini-task:**
Write a Playwright test that completes a user journey on your staging app: (1) navigate to the page, (2) fill a form, (3) submit, (4) verify the success state. Use at least 3 different interaction types. Commit as `test(journey): <your-name>-<journey-name>`.

**Self-check:**
- [ ] I can use the basic Playwright actions correctly
- [ ] I understand auto-waiting and actionability checks
- [ ] I can complete a multi-step user journey in code

---

### 7. Assertions & Expect

**Learn:**

- **Playwright's `expect()`:** The assertion library. `expect(locator).toBeVisible()`, `expect(locator).toHaveText()`, `expect(page).toHaveURL()`. Chained matchers for every occasion.
- **Soft Assertions vs. Hard Assertions:** Hard — the test stops on the first failure. Soft (`expect.soft()`) — continues even if it fails, then reports all failures at the end. Use soft for comprehensive reporting.
- **Custom Matchers:** `expect.extend()` to add project-specific matchers. The CoE standardizes on a few custom matchers — learn the standard ones first.

**Mini-task:**
Enhance your journey test (from Topic 6) with 5 assertions: (1) element visibility (`toBeVisible()`), (2) text content (`toHaveText()`), (3) URL (`toHaveURL()`), (4) form values (`toHaveValue()`), (5) class/state (`toHaveClass()`). Commit as `test(assertions): <your-name>-journey-enhanced`.

**Self-check:**
- [ ] I can use at least 5 different Playwright matchers
- [ ] I understand the difference between hard and soft assertions
- [ ] I know when to use which assertion type

---

## 🔵 Phase 3 — Test Design & Maintenance (Intermediate)

**Goal:** Write tests that survive code changes. Go from "I can write a test" to "my tests don't break every sprint."

### 8. Test Organization

**Learn:**

- **Test File Structure:** One test file per feature or user journey. Tests should be independent — no ordering dependencies. Use `test.describe()` to group related tests.
- **Naming Conventions:** `test.describe('Feature', () => { test('should do X', ...) })`. Name tests like sentences: "should login with valid credentials." The test name IS the documentation.
- **Tagging for Filtering:** Use `test.skip()`, `test.only()`, and `@tag` annotations. Run subsets: `npx playwright test --grep @smoke`. Vital for CI.

**Mini-task:**
Re-organize your existing tests (from Topics 4-7) into a logical `test.describe()` structure: group by feature, not by test number. Add at least one `@smoke` and `@regression` tag to each. Commit as `refactor(test-org): <your-name>-structure`.

**Self-check:**
- [ ] I can structure tests using `test.describe()`
- [ ] I understand test independence and why ordering matters
- [ ] I can filter tests using tags in CI

---

### 9. Page Object Model

**Learn:**

- **The POM Pattern:** Pages = objects; elements = properties; actions = methods. `LoginPage.username = 'input'` (property), `LoginPage.submit()` (method). The test reads like English.
- **Why POM Matters:** If the login page changes, you change ONE file (LoginPage), not EVERY test. The test describes intent; the page object describes implementation.
- **CoE Standard:** Every CoE test file should use the Page Object Model. No `page.locator('button').click()` in test files; that's what the page object is for.

**Mini-task:**
Create a Page Object for a page in your staging app. Move at least 3 locators into the page object as properties, and 2 actions as methods. Refactor an existing test to use the page object. Commit as `refactor(pom): <your-name>-<page-name>`.

**Self-check:**
- [ ] I can create a Page Object with properties and methods
- [ ] I understand why POM reduces maintenance
- [ ] I can refactor a test to use POM

---

### 10. Test Parameterization

**Learn:**

- **Data-Driven Testing:** Same test, different data. Instead of writing "test should login with user A" and "test should login with user B," write one test and pass `[userA, userB]` as data. Playwright supports `test.each()`.
- **Fixtures for Data Setup:** Use Playwright fixtures to inject test data. No more `beforeEach()` that sets up the same data in every test. Use `test.step()` for test isolation.
- **Environment-Specific Configs:** Dev, staging, production — different URLs, different credentials. Use `playwright.config.ts` projects and environment variables.

**Mini-task:**
Parameterize one of your existing tests with 3 different data sets. Convert a hard-coded credential to use an environment variable. Commit as `test(parameterized): <your-name>-<test-name>`.

**Self-check:**
- [ ] I can write a data-driven test using `test.each()`
- [ ] I understand Playwright fixtures for data setup
- [ ] I can configure environment-specific URLs in config

---

### 11. Test Maintenance Patterns

**Learn:**

- **What Makes Tests Brittle:** Selecting by CSS selector, testing implementation details (not behavior), hard-codedWaits (`sleep()` instead of auto-wait), test interdependencies. Fix these and tests survive.
- **The 5 Maintenance Rules:** (1) Prefer semantic locators (roles, labels). (2) Test behavior, not implementation. (3) Use `waitFor()` for dynamic content (not `sleep()`). (4) Independent tests — no shared state. (5) Name tests like documentation.
- **Flaky Test Management:** Retry once locally; if it fails twice, it's not flaky — it's broken. Track flaky tests separately (`--retries`).

**Mini-task:**
Audit your existing tests for brittle patterns. Identify 3 tests that use CSS selectors, bad sleep patterns, or test interdependencies. Refactor each to follow the 5 rules. Commit with `refactor(maintenance): <your-name>-<test-names>`.

**Self-check:**
- [ ] I can identify 5 common brittle test patterns
- [ ] I can fix a test to make it maintainable
- [ ] I understand Playwright's retry and timeout handling

---

### 12. Debugging & Troubleshooting

**Learn:**

- **Playwright Trace Viewer:** `npx playwright show-report` — see every action, every network request, every console log. The best debugging tool in testing.
- **Video/Screenshot On Failure:** Configure in `playwright.config.ts`: `trace: 'on-first-retry'`, `video: 'on-last-retry'`. You'll thank yourself when a test fails at 2am.
- **Network Interception:** `page.route()`, `page.unroute()`. Intercept API calls to mock responses without a backend. The key to testing edge cases: 500 errors, Slow responses, Empty states.

**Mini-task:**
Configure your `playwright.config.ts` to capture trace, video, and screenshot on test failure. Re-run a failing test with the new configuration. Use the trace viewer to identify the root cause. Document your findings in a comment. Commit as `test(config): <your-name>-debugging-config`.

**Self-check:**
- [ ] I can use Playwright trace viewer to debug
- [ ] I can configure video/screenshot capture on failure
- [ ] I understand network interception for mocking

---

## 🟡 Phase 4 — API Automation (Advanced)

**Goal:** Automate API testing alongside E2E. Full coverage includes both layers.

### 13. API Testing Fundamentals

**Learn:**

- **Playwright vs. REST Client:** Use Playwright's built-in `request` API for API tests. Same authentication, same config, unified reporting. No separate REST client needed.
- **HTTP Methods in Playwright:** `request.get()`, `request.post()`, `request.put()`, `request.patch()`, `request.delete()`. All verbs supported.
- **Response Verification:** `expect(response).toBeOK()`, `expect(response).toHaveBody()`, `expect(response).toHaveHeader()`. API assertions are simpler than UI — status codes, headers, body.

**Mini-task:**
Write an API test that hits an endpoint on your staging API: (1) GET to fetch data, (2) POST to create a record, (3) verify the response status and body. Use Playwright's `request` API. Commit as `test(api): <your-name>-<endpoint-name>`.

**Self-check:**
- [ ] I can use Playwright's request API for API testing
- [ ] I can verify HTTP status codes and response bodies
- [ ] I understand the difference between E2E and API testing

---

### 14. Authentication & Sessions

**Learn:**

- **Session Management in Tests:** Login once, reuse the session. Playwright's `storageState` — authenticate in one test, save state, use it in others. No re-login in every test.
- **OAuth & Token Handling:** Extract tokens from UI login, use in API headers. Handle refresh tokens for long-running test suites.
- **Shared Setup Fixtures:** Use Playwright fixtures for authenticated state. `test.beforeEach()` that checks for stored auth; skips login if valid.

**Mini-task:**
Implement session management for your test suite: authenticate once, save the state, reuse across tests. Refactor at least 3 existing tests to use the shared authentication state. Commit as `refactor(auth): <your-name>-session-management`.

**Self-check:**
- [ ] I can implement session state reuse with Playwright
- [ ] I can handle OAuth tokens in tests
- [ ] I understand fixture-based authentication

---

### 15. Data Setup & Teardown

**Learn:**

- **Test Data Lifecycle:** Setup → Test → Teardown. Create data before the test, clean it up after. Playwright `test.afterEach()` for teardown.
- **API vs. UI for Setup:** Create test data via API (faster) or via UI (more realistic). Use API for data setup; use UI for the critical path.
- **Fixtures for Data:** Use `test.step()` to isolate data setup from test assertions. Clear, traceable, debuggable.

**Mini-task:**
Implement full setup/teardown for an API test: (1) POST to create test data, (2) run the test, (3) DELETE to clean up. Use `test.step()` for clarity. Commit as `test(data-lifecycle): <your-name>-<resource-name>`.

**Self-check:**
- [ ] I can implement test data setup via API
- [ ] I understand the setup → test → teardown lifecycle
- [ ] I can use test.step() for clear test isolation

---

### 16. Advanced Assertions

**Learn:**

- **Schema Validation:** `expect(response).toHaveSchema()`. Validate API response structures against expected schemas. For CoE API standardization, see [REST API Best Practices](../../general/rest-api-best-practices.md).
- **Partial Matching:** `toContain()`, `toMatchObject()`. Don't assert every field; assert what matters. Over-specification = brittleness.
- **Error Case Testing:** Negative assertions. `toHaveStatus(401)`, `toHaveErrorBody()`. Test the error paths — they're as important as success paths.

**Mini-task:**
Write an API test suite that covers both positive and negative cases: (1) success scenarios (200/201), (2) auth failures (401), (3) validation failures (400), (4) not found (404). Use partial matching where appropriate. Commit as `test(api-complete): <your-name>-<endpoint-name>`.

**Self-check:**
- [ ] I can validate API response schemas
- [ ] I can test both positive and negative API scenarios
- [ ] I understand when to use partial vs. exact matching

---

## 🟡 Phase 5 — CI/CD Integration (Advanced)

**Goal:** Tests in CI, not on your laptop. Automated execution, clear reporting.

### 17. CI Pipeline Foundations

**Learn:**

- **GitHub Actions for Playwright:** The CoE standard. `npx playwright test` runs in CI. Use official `playwright` action or custom ` Runs-on` with `npm install` + `npx playwright install`.
- **Secrets Management:** Never commit credentials. Use GitHub secrets, inject via `${{ secrets }}`. Test against staging only; never credentials in prod.
- **Conditional Execution:** Run full suite on PR, smoke on push. Use matrix strategies for parallel execution.

**Mini-task:**
Set up a GitHub Actions workflow that runs your Playwright tests on PR. Include: (1) checkout, (2) install, (3) install browsers, (4) run tests, (5) upload artifacts. Commit as `ci(workflow): <your-name>-playwright-tests`.

**Self-check:**
- [ ] I can create a GitHub Actions workflow for Playwright
- [ ] I understand secrets management in CI
- [ ] I can configure conditional test execution

---

### 18. Parallel Execution

**Learn:**

- **Why Parallel:** 10 tests in series = 10 minutes. 10 tests in parallel = 1 minute. Playwright has it built-in with `workers`.
- **Configuring Workers:** `workers: process.env.CI ? 4 : 1` — parallel in CI, serial locally for debugging. The CoE standard configuration.
- **Shard Strategy:** Split the full suite across multiple CI jobs (`--shard`). For large suites, this is essential for <5 minute feedback loops.

**Mini-task:**
Configure your `playwright.config.ts` for parallel execution: set `workers: process.env.CI ? 4 : 1`. Measure the time difference before/after. Document the results in your PR. Commit as `ci(parallel): <your-name>-execution-config`.

**Self-check:**
- [ ] I can configure Playwright workers
- [ ] I understand when to use sharding
- [ ] I can measure and report parallel execution gains

---

### 19. Artifacts & Reporting

**Learn:**

- **Test Reports:** Playwright HTML report (`npx playwright show-report`). Upload as CI artifact. The CoE standard reporter.
- **Tracing:** Upload Playwright traces to GitHub Actions artifacts on failure. `npx playwright show-report` extracts the trace from the artifact.
- **Custom Reporting:** Add custom metadata to test reports using `test.info().annotations`. Track environment, build, and test data for post-mortem analysis.

**Mini-task:**
Configure your CI workflow to upload test reports and traces: (1) HTML report as artifact, (2) trace viewer on failure. Update the README with instructions on downloading and viewing reports. Commit as `ci(reports): <your-name>-artifact-config`.

**Self-check:**
- [ ] I can upload test reports to CI artifacts
- [ ] I can configure trace viewing for failures
- [ ] I understand how to use test metadata

---

## 🟡 Phase 6 — Quality & Maturity (Leadership Track)

**Goal:** Go from "I write tests" to "our automation practice is mature." Leadership track.

### 20. Test Reporting & Metrics

**Learn:**

- **Flaky Test Metrics:** Track flaky tests over time. Target: <1% flaky rate. The CoE standard: investigate anything that flakes >3 times.
- **Test Coverage Metrics:** What % of features have automated tests? What % of critical paths are covered? Use tags to segment: `@critical`, `@smoke`, `@regression`.
- **Reporting Cadence:** Daily build reports, weekly trend analysis. Who monitors? Who acts on flakiness?

**Mini-task:**
Create a test reporting dashboard: (1) generate a test report for your last run, (2) calculate the flaky rate, (3) segment by tags (`@critical`, `@smoke`, `@regression`), (4) propose a monitoring cadence. Document in your PR.

**Self-check:**
- [ ] I can calculate and report flaky test metrics
- [ ] I can segment tests by critical/smoke/regression tags
- [ ] I understand the CoE's flaky test standard

---

### 21. Performance & Accessibility

**Learn:**

- **Performance Testing with Playwright:** `playwright test --project=performance` — measure page load, time to interactive. Integrate with CI thresholds.
- **Accessibility Testing:** Playwright's `axe` integration. `await expect(page).toHaveNoViolations()`. Automated accessibility testing right alongside functional tests.
- **CoE Standards:** The CoE requires accessibility testing. It's not optional. If you're automating, you're testing a11y too.

**Mini-task:**
Add performance and accessibility testing to your config: (1) add `playwright test --project=perf` that measures page load, (2) add axe-core to verify no accessibility violations. Create at least one performance test and one a11y test. Commit as `test(a11y-perf): <your-name>-additional-checks`.

**Self-check:**
- [ ] I can add performance testing to Playwright
- [ ] I can use axe-core for accessibility testing
- [ ] I understand why a11y testing is mandatory

---

### 22. Mentoring & Leadership

**Learn:**

- **The Automation Career Path:** What manual testers need to become automation engineers. The curriculum you're reading. Being the mentor you wish you'd had.
- **Code Review for Tests:** Just like code review for features. Test readability, locator stability, assertion coverage. Apply the same rigor.
- **Building an Automation Team:** Hiring, onboarding, standards. The leadership work beyond Just Writing Tests.

**Mini-task:**
Document your automation journey: (1) what you learned at each phase, (2) what you'd do differently as a mentor, (3) a one-page "getting started" guide for the next manual tester following this path. Commit as `docs(mentorship): <your-name>-automation-journey`.

**Self-check:**
- [ ] I can articulate the automation career path
- [ ] I can code-review a test suite
- [ ] I can mentor a manual tester on automation

---

## Document control

| Field | Value |
|---|---|
| Document | Automation Engineer Learning Path |
| Version | 0.1 (draft — 6 phases, 22 topics) |
| Owner | CoE QA Working Group |
| Review Cycle | Quarterly |
| Status | Draft for pilot batch review |
| Related | [README.md](./README.md), [roadmap-gap-analysis.md](./roadmap-gap-analysis.md), [REST API Best Practices](../../general/rest-api-best-practices.md), [Dev Excellence Curriculum](../dev-excellence/curriculum.md) |

---

**Maintained by:** Techversant CoE
**Last Updated:** June 2026