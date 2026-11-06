# Practice App: A RealWorld Front End

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Every front-end path in the academy builds the same app: a front end for **RealWorld**, an open-source
Medium-style blogging app also called Conduit. You build it stage by stage in your framework, and RealWorld's own
tests check it the same way for everyone.

## Why This App

- **It is a real app.** Sign-up, sign-in, articles, comments, tags, profiles, following, favourites and pagination
  cover most of what client front ends do.
- **The contract is fixed.** One API specification and one set of page templates mean you spend your time on
  front-end skills, not on deciding what to build.
- **It is tested for you.** A shared Playwright suite checks every page, form and flow, including a basic
  cross-site scripting test.
- **It pairs with any back end.** Every RealWorld back end follows the same API, including one you build in a
  [back-end path](../01-backend/README.md).

## Key Details

| Detail | Value |
|--------|-------|
| Repository | [realworld-apps/realworld](https://github.com/realworld-apps/realworld), MIT licence |
| Front-end specification | [Templates, styles, routing and tests](https://docs.realworld.show/specifications/frontend/templates/) on the RealWorld documentation site |
| Shared stylesheet | `assets/theme/styles.css` in the repository. It does not include fonts or icons; the templates page shows how to load them. |
| End-to-end tests | Playwright tests in `specs/e2e`, with a base configuration in `specs/e2e/playwright.base.ts` |
| Test contract | `specs/e2e/SELECTORS.md`: the routes, form field names, CSS classes, button text, token storage key and debug interface the tests rely on |
| API for day-to-day work | The official back end, [nitro-prisma-zod-realworld-example-app](https://github.com/realworld-apps/nitro-prisma-zod-realworld-example-app), run on your machine. It serves `http://localhost:3000/api` and starts with no data. |
| API for the end-to-end suite | The public demo API, `https://api.realworld.show/api`. It has the seeded accounts the suite expects, such as `johndoe`. Signed-in users see only their own content and the demo accounts' content. |

## Setting Up

1. Create a repository for your practice work, as agreed with your lead, and give your reviewer write access.
2. Clone the [RealWorld repository](https://github.com/realworld-apps/realworld) next to it. You need the
   stylesheet, the templates and the tests from it.
3. Run the official back end locally, following its README, for day-to-day work. It uses port 3000. Vite apps use
   port 5173 by default; run Next.js on another port, for example `next dev -p 3001`.
4. Read `specs/e2e/SELECTORS.md` before you write any markup. Every route, field name and class it lists must exist
   in your app, or the tests cannot find your pages.
5. Override the stylesheet's colour variables, such as `--brand`, `--text-muted` and `--text-light`, so text has a
   contrast of at least 4.5:1. The default colours fail the axe contrast check, and the tests do not depend on them.

## Running the End-to-End Tests

The tests read their settings from environment variables:

| Variable | What it does |
|----------|--------------|
| `TEST_MODE` | `spa` (the default) for an app that calls the API from the browser; `ssr` for an app that renders on a server and calls the API from there |
| `API_BASE` | The API address the tests use for setup. Leave it unset, so it uses the public demo API |

Extend the base configuration in `specs/e2e/playwright.base.ts`, setting `baseURL` and `webServer` to your
development server, as the RealWorld [front-end tests page](https://docs.realworld.show/specifications/frontend/tests/)
describes.

Run the suite with your app pointed at the public demo API. The suite does not fully pass against a fresh local back
end: some tests need the demo's seeded accounts and articles, and two spec files mock the demo API's address
directly. Sign up only with generated test data, never real names or email addresses.

In `ssr` mode the suite skips the tests marked SPA-only, because they read the token in the browser or intercept
browser calls to the API. Those skips are expected. Any other skipped test needs a reason.

When you report results, show the number of tests that ran, passed, failed and were skipped. A skipped test is not a
pass.

## Practice-Only Parts of the Contract

Two parts of the RealWorld test contract exist only so the shared tests can work. They are fine in your practice
app, and must never appear in client work:

- **The token in `localStorage`.** The contract stores the sign-in token under the `jwtToken` key, where any script
  on the page can read it. Techversant's default for client work is an httpOnly cookie set by the back end. You move
  to a cookie in stage 08.
- **The debug interface.** The contract exposes `window.__conduit_debug__`, including a function that returns the
  token. Remove it when you move to a cookie, because `ssr` mode does not use it. The production checks confirm it
  is gone.

Use the app for practice only. Do not deploy it with real users' data, and do not copy its code into client work.

## Paths That Use It

- [React and Next.js](./react-nextjs/README.md)
