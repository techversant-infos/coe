# Manual Tester to Automation Engineer

> **Audience:** Manual testers with little or no automation experience.
> **Length:** 8-10 weeks, around 5 hours/week.
> **Goal:** Become productive writing and maintaining Playwright automation with support from a senior reviewer.

---

## Learning Outcomes

By the end of this path, the learner should be able to:

1. Read and modify basic JavaScript used in automation tests.
2. Use Git to create a branch, commit changes, and open a PR.
3. Inspect HTML, CSS, DOM structure, and browser behavior using DevTools.
4. Write Playwright tests using stable locators, actions, assertions, and traces.
5. Automate a complete user journey without relying on brittle selectors or fixed sleeps.
6. Create basic API checks with Playwright's request API.
7. Explain what should be automated, what should stay manual, and why.
8. Complete a capstone automation PR with mentor review.

---

## Suggested 10-Week Plan

| Week | Focus | Output / Definition of Done |
|---|---|---|
| 0 | Automation mindset | Convert 5 manual test cases into automation candidates with ROI notes |
| 1 | JavaScript fundamentals | Can edit variables, functions, objects, arrays, conditionals, and async code |
| 2 | Git + developer workflow | Opens a small automation PR using the Techversant Git workflow |
| 3 | HTML, CSS, DOM, DevTools | Locates elements reliably and explains why a locator is stable or brittle |
| 4 | Playwright fundamentals | Creates and runs a basic Playwright test locally |
| 5 | Locators, actions, assertions | Automates a complete happy-path user journey |
| 6 | Debugging and traces | Fixes a failing test using Playwright trace viewer and error output |
| 7 | Page Objects and fixtures | Refactors one journey into a maintainable Page Object structure |
| 8 | API testing basics | Adds one API setup/assertion flow using Playwright request API |
| 9 | Capstone | Opens a reviewed automation PR with UI + API coverage and README notes |

---

## Phase 0 - Automation Mindset

**Goal:** Learn what to automate before learning how to automate.

**Learn:**

- Automation ROI
- Regression vs exploratory testing
- Test pyramid and test trophy
- What should stay manual
- Cost of flaky tests
- Risk-based automation

**Mini-task:** Pick 5 manual test cases from the current project. Mark each as automate now, automate later, or keep manual. Explain the risk, run frequency, stability, and maintenance cost.

**Topic resource:** [Test Automation Pyramid - Google Testing Blog](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)

---

## Phase 1 - Programming Fundamentals

**Goal:** Build enough JavaScript confidence to read and edit automation code.

**Learn:**

- Variables and constants
- Functions
- Objects and arrays
- Conditions and loops
- Modules and imports
- `async` / `await`
- Error messages and stack traces

**Mini-task:** Create a small JavaScript playground with 5 snippets: function, array map, object lookup, conditional branch, and async function.

**Topic resource:** [MDN - JavaScript First Steps](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps)

---

## Phase 2 - Git and Developer Workflow

**Goal:** Work like an engineer, not only a tester running scripts locally.

**Learn:**

- Branching
- Commits
- Pull requests
- Review comments
- Rebase/conflict basics
- Test evidence in PRs

**Mini-task:** Open a PR that adds one small test or test fixture and includes setup, verification, and screenshots/traces where useful.

**Internal standard:** [Git Workflow](../../../00-engineering-foundations/git-workflow.md)

---

## Phase 3 - HTML, CSS, DOM, and DevTools

**Goal:** Understand what Playwright sees when it locates an element.

**Learn:**

- HTML elements and attributes
- Form labels and accessible names
- CSS selectors and why they are often brittle
- DOM inspection
- Network tab basics
- Console errors

**Mini-task:** Inspect a real page and document stable locators for 10 elements using role, label, placeholder, text, and test id where appropriate.

**Topic resource:** [Playwright Docs - Locators](https://playwright.dev/docs/locators)

---

## Phase 4 - Playwright Fundamentals

**Goal:** Write and run your first meaningful Playwright tests.

**Learn:**

- `test()` and `expect()`
- `playwright.config.ts`
- Browser projects
- Running by file, title, or tag
- Auto-waiting and actionability

**Mini-task:** Create a smoke test that opens the staging app, verifies the page loaded, and checks one meaningful user-visible state.

**Topic resource:** [Playwright Docs - Getting Started](https://playwright.dev/docs/intro)

---

## Phase 5 - User Journey Automation

**Goal:** Automate a real workflow using stable selectors and clear assertions.

**Learn:**

- `getByRole`, `getByLabel`, `getByTestId`
- `click`, `fill`, `selectOption`, `check`
- `toBeVisible`, `toHaveText`, `toHaveURL`
- Avoiding fixed waits

**Mini-task:** Automate one complete journey: login, perform an action, verify success, and clean up if needed.

**Topic resource:** [Playwright Docs - Assertions](https://playwright.dev/docs/test-assertions)

---

## Phase 6 - Debugging and Trace Viewer

**Goal:** Debug automation failures systematically.

**Learn:**

- Reading Playwright errors
- Trace viewer
- Screenshots and videos
- Console and network inspection
- Isolating one failing test

**Mini-task:** Break one test intentionally, use trace viewer to diagnose it, then fix it and document the debugging steps in the PR.

**Topic resource:** [Playwright Docs - Trace Viewer](https://playwright.dev/docs/trace-viewer)

---

## Phase 7 - Framework Basics

**Goal:** Make tests maintainable enough for a team.

**Learn:**

- Page Object Model
- Fixtures
- Test data helpers
- Tags: smoke, regression, critical
- Test naming

**Mini-task:** Refactor the capstone journey into a Page Object and fixture-backed setup.

**Topic resource:** [Playwright Docs - Page Object Models](https://playwright.dev/docs/pom)

---

## Phase 8 - API Testing Basics

**Goal:** Learn when API tests are better than UI tests.

**Learn:**

- Playwright request API
- Status code assertions
- Response body assertions
- Setup and teardown via API
- Positive and negative scenarios

**Mini-task:** Add one API test for the same feature covered by the UI test. Use API setup when it makes the UI test simpler and more reliable.

**Topic resource:** [Playwright Docs - API Testing](https://playwright.dev/docs/api-testing)

---

## Phase 9 - Capstone Project

**Goal:** Prove readiness for supervised automation work.

**Capstone:** Automate one real project workflow with:

- one UI journey test,
- one API assertion or setup step,
- stable locators,
- Page Object or fixture structure,
- trace/debug configuration,
- PR notes explaining what was automated and why.

## Readiness Checklist

- [ ] I can explain why this test is worth automating.
- [ ] I can run the test locally.
- [ ] I can debug a failure using trace viewer.
- [ ] I can avoid fixed sleeps and brittle selectors.
- [ ] I can open a reviewable automation PR.
- [ ] I can explain the test code I wrote.

---

## Related Paths

- [Automation Strategy](../../strategy/automation-strategy.md)
- [Automation Engineer to Senior Automation Engineer](./senior-automation.md)
- [AI Assisted Testing](../../../06-ai-engineering/ai-assisted-testing/README.md)
