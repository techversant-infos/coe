# 09. Testing

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Tests let you change a front end without fear of breaking it. A good mix has many fast component tests, some tests
against a mocked API, and a few end-to-end tests that drive a real browser. Back to the [roadmap](./README.md).

## Component tests

Component tests render one component, act on it the way a user would, and check what appears on screen. Vitest runs
the tests, and Vue Testing Library renders components and finds elements.

**What to learn:**

- Rendering a component and finding elements by role, label or text, as a user would
- Simulating clicks and typing with `user-event`, and waiting for changes with `findBy` queries
- Testing behaviour, not implementation details such as the names of refs
- Testing components that use Nuxt composables with `@nuxt/test-utils`, its `nuxt` test environment and
  `mountSuspended`

**Resources:**

- [Vitest guide](https://vitest.dev/guide/)
- [Vue Testing Library](https://testing-library.com/docs/vue-testing-library/intro/)
- [Testing](https://nuxt.com/docs/4.x/getting-started/testing), Nuxt documentation
- [Test levels](../../../00-engineering-foundations/07-testing-and-refactoring.md#test-levels), in Engineering
  Foundations

**Level:** Practitioner · Core

## Mocking APIs with MSW

Mock Service Worker (MSW) answers network requests with responses you define. Tests can then show what the page does
when the API is slow, fails or returns nothing, without a real back end.

**What to learn:**

- Writing request handlers for the endpoints a component or server route calls
- Overriding a handler in one test to return an error, such as a 422 or a 500
- Running MSW in Node to test your API client, composables and server route code. Whole pages that Nuxt renders on
  the server are tested with Playwright instead.

**Resources:** [MSW documentation](https://mswjs.io/docs/)

**Level:** Practitioner · Core

## End-to-end tests with Playwright

End-to-end tests open the app in a real browser and go through whole flows, such as signing up and writing an
article. They are slower, so keep them for the flows that matter most.

**What to learn:**

- Writing tests with locators such as `getByRole` and `getByLabel`, which wait for elements automatically
- Setting up test data through the API instead of the user interface, so tests are fast and independent
- Reading the trace viewer to find out why a test failed
- Running the RealWorld suite alongside your own tests

**Resources:**

- [Playwright: getting started](https://playwright.dev/docs/intro)
- [Writing locators](https://playwright.dev/docs/locators), Playwright documentation

**Level:** Advanced · Core

## Accessibility testing

Automated checks find many accessibility problems, such as missing labels and low contrast, on every test run. They
cannot find them all, so a short manual keyboard check is still needed.

**What to learn:**

- Running axe in Playwright tests with `@axe-core/playwright`
- Choosing which pages and states to check, such as forms with errors showing
- What automated checks miss, and a short manual check with the keyboard and a screen reader

**Resources:** [Accessibility testing](https://playwright.dev/docs/accessibility-testing), Playwright documentation

**Level:** Advanced · Core

## Project: Pass the Full Test Suite

**Brief:** Add your own tests to the Nuxt app and get the RealWorld end-to-end suite passing. Cover the cases the
suite skips in `ssr` mode, such as API errors, with your own tests.

**Size:** 4 days

**Verification**, checked by a reviewer:

- [ ] Component tests cover the article preview, the feed tabs, pagination and every form, including validation
  errors
- [ ] MSW tests show how the API client and server routes handle 401, 404, 409, 422 and 500 responses
- [ ] Playwright tests show the page for an unknown article slug, and what happens with an invalid session cookie,
  set with `context.addCookies`
- [ ] At least three of your own Playwright tests cover sign-up, writing an article and favouriting, with test data
  set up through the API
- [ ] axe checks in Playwright report no serious or critical issues on the home, article, editor and sign-in pages
- [ ] The RealWorld suite runs with `TEST_MODE=ssr` against the public demo API with no failures, and every skipped
  test is one the suite marks as SPA-only (single-page app only)
- [ ] All tests run in continuous integration on every pull request, and a failing test blocks the merge

Previous: [08. Rendering and the Meta-Framework](./08-rendering-and-the-meta-framework.md) · Next:
[10. Performance and Production](./10-performance-and-production.md)
