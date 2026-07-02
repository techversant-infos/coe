# Automation Engineer to Senior Automation Engineer

> **Audience:** Automation engineers with 6+ months of automation experience.
> **Length:** 8-10 weeks, around 4-5 hours/week.
> **Goal:** Own automation quality across a project: framework design, API strategy, CI, reporting, flake control, accessibility, performance, AI-assisted workflows, and mentoring.
> **Level:** Advanced ? Expert
> **Next Level:** [Career Progression: QA Lead Path](../../../career-progression/04-lead-to-architect.md)

---

## Learning Outcomes

By the end of this path, the engineer should be able to:

1. Design an automation strategy instead of only writing scripts.
2. Improve a Playwright framework for maintainability and scale.
3. Decide when UI, API, component, or manual testing is the right layer.
4. Configure CI execution, reports, traces, sharding, and artifacts.
5. Track and reduce flaky tests.
6. Add accessibility and lightweight performance checks where useful.
7. Use AI to accelerate automation without delegating test judgment.
8. Mentor manual testers and junior automation engineers.

---

## Suggested 10-Week Plan

| Week | Focus | Output / Definition of Done |
|---|---|---|
| 1 | Automation design thinking | Automation strategy note for one project area |
| 2 | Framework architecture | Refactored Page Object/fixture structure with review notes |
| 3 | Advanced Playwright | Reliable auth, network control, trace/debug setup |
| 4 | API strategy | API test layer mapped to UI coverage gaps |
| 5 | CI/CD | Playwright workflow with artifacts and useful failure output |
| 6 | Flaky test control | Flake triage process and first cleanup PR |
| 7 | Accessibility | axe-based check for at least one critical page |
| 8 | Performance awareness | Lightweight timing or Web Vitals check for one critical journey |
| 9 | AI-assisted automation | Documented AI workflow for test generation/refactor/review |
| 10 | Mentoring capstone | Review another engineer's automation PR and improve the standard |

---

## Phase 1 - Automation Design Thinking

**Goal:** Decide what to automate and at which layer.

**Learn:**

- Risk-based automation
- Test pyramid vs test trophy
- UI vs API vs component tests
- Automation debt
- Cost of flaky tests
- Coverage that matters vs coverage theater

**Mini-task:** Pick one feature area and produce a one-page automation strategy: critical risks, tests to automate, tests to keep manual, layer choice, and maintenance risks.

**Topic resource:** [Google Testing Blog - Just Say No to More End-to-End Tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html)

---

## Phase 2 - Framework Architecture

**Goal:** Make the framework easy to maintain by the whole team.

**Learn:**

- Page Object boundaries
- Fixtures and test data builders
- Avoiding utility dumping grounds
- Test naming and tags
- Shared setup without hidden coupling

**Mini-task:** Refactor one messy test area into clear Page Objects, fixtures, and helpers. Add a short README explaining the pattern.

**Topic resource:** [Playwright Docs - Fixtures](https://playwright.dev/docs/test-fixtures)

---

## Phase 3 - Advanced Playwright

**Goal:** Use Playwright features that reduce flakiness and debugging time.

**Learn:**

- `storageState` auth reuse
- Network interception
- Traces, screenshots, videos
- Retries and timeouts
- Project configuration
- Parallel workers and isolation

**Mini-task:** Improve the framework configuration for trace/video/screenshot capture, reliable auth reuse, and local-vs-CI execution.

**Topic resource:** [Playwright Docs - Authentication](https://playwright.dev/docs/auth)

---

## Phase 4 - API Strategy

**Goal:** Use API automation to reduce slow and brittle UI coverage.

**Learn:**

- API tests as first-class tests
- API setup and teardown
- Contract expectations
- Positive and negative cases
- Mapping API coverage to UI journeys

**Mini-task:** Add an API test suite for one resource and update one UI test to use API setup instead of slow UI setup.

**Internal standard:** [REST API Best Practices](../../../../general/rest-api-best-practices.md)

---

## Phase 5 - CI/CD for Automation

**Goal:** Make automation useful in the delivery workflow.

**Learn:**

- GitHub Actions workflow design
- Browser install and caching basics
- Artifacts and reports
- Smoke vs regression split
- Secrets handling
- Failure triage from CI output

**Mini-task:** Create or improve a Playwright CI workflow that uploads reports/traces and runs the right suite for PRs.

**Topic resource:** [Playwright Docs - CI](https://playwright.dev/docs/ci)

---

## Phase 6 - Flaky Test Management

**Goal:** Treat flaky tests as automation debt, not background noise.

**Learn:**

- Flake categories: selector, timing, data, environment, product bug
- Retry policy
- Quarantine policy
- Flaky-rate tracking
- Ownership and SLA

**Mini-task:** Pick three flaky tests, classify root causes, fix at least one, and document what should happen to the others.

**Topic resource:** [Martin Fowler - Eradicating Non-Determinism in Tests](https://martinfowler.com/articles/nonDeterminism.html)

---

## Phase 7 - Accessibility Automation

**Goal:** Add useful automated accessibility coverage without pretending it replaces manual review.

**Learn:**

- axe-core basics
- WCAG issue categories
- Keyboard navigation smoke checks
- Labels and accessible names
- What automated a11y cannot catch

**Mini-task:** Add an axe-core accessibility test for one critical page and document any findings.

**Topic resource:** [Deque axe-core Playwright](https://github.com/dequelabs/axe-core-npm/tree/develop/packages/playwright)

---

## Phase 8 - Performance Awareness

**Goal:** Catch obvious performance regressions in critical journeys.

**Learn:**

- What to measure in automation
- Page load and user journey timings
- Lighthouse vs Playwright checks
- Thresholds and noise
- When performance testing needs a separate tool

**Mini-task:** Add a lightweight timing check for one critical journey. Document why the threshold is useful and what would happen on failure.

**Topic resource:** [web.dev - Core Web Vitals](https://web.dev/vitals/)

---

## Phase 9 - AI-Assisted Automation

**Goal:** Use AI to accelerate automation while keeping human ownership of test design.

**Learn:**

- Generate Playwright test drafts
- Convert manual test cases into automation candidates
- Refactor Page Objects
- Generate selector alternatives
- Explain trace failures
- Review automation PRs
- Avoid trusting AI for final test judgment

**Mini-task:** Use AI to draft or refactor one test, then manually review and improve it. In the PR, include what AI helped with and what you changed.

**Internal standard:** [AI Usage](../../../00-engineering-foundations/02-ai-usage.md)

---

## Phase 10 - Mentoring and Automation Leadership

**Goal:** Help others write better automation and improve team standards.

**Learn:**

- Reviewing automation PRs
- Coaching manual testers
- Writing framework docs
- Defining team standards
- Communicating automation health

**Capstone:** Review another engineer's automation PR, improve one framework standard, and publish a short guide for the team.

## Readiness Checklist

- [ ] I can explain what should and should not be automated.
- [ ] I can improve framework structure without over-abstraction.
- [ ] I can debug CI failures using artifacts and traces.
- [ ] I can reduce flaky tests systematically.
- [ ] I can add API, accessibility, and lightweight performance checks where they make sense.
- [ ] I can mentor another tester through an automation PR.

---

## Related Paths

- [Manual Tester to Automation Engineer](./01-manual-to-automation.md)
- [Automation Strategy](../../03-strategy/01-automation-strategy.md)
- [Developer Excellence Curriculum](../../../00-engineering-foundations/05-dev-excellence/01-curriculum.md)
- [AI Assisted Testing](../../../06-ai-engineering/02-ai-assisted-testing/README.md)
