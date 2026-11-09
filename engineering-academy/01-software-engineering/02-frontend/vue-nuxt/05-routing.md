# 05. Routing

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Routing decides which page to show for each URL. Good URLs can be bookmarked, shared and opened in a new tab, and
the browser's back button works as people expect. Back to the [roadmap](./README.md).

## Client-side routing

In a single-page app, the router changes the page without a full reload. Vue Router is Vue's official router.

**What to learn:**

- Defining routes, and linking between them with `RouterLink` instead of plain `a` tags
- Navigating from code with `router.push`, for example after a form is saved
- Showing a "not found" page for unknown URLs with a catch-all route
- File-based routing in Vue Router 5, where files in a folder become routes, as Nuxt does in stage 08

**Resources:** [Vue Router guide](https://router.vuejs.org/guide/)

**Level:** Practitioner · Core

## URL parameters and query strings

Part of the URL often identifies what to show, such as an article's slug in `/article/:slug`, or filters it, such
as `?page=2`.

**What to learn:**

- Reading route parameters with `useRoute`, and reacting when they change on the same page
- Keeping filters and page numbers in the query string, so the URL describes the page
- Updating the query string without losing the other parameters
- Working out the active feed tab and page from `route.query` yourself, because the router's active class ignores
  the query

**Resources:**
[Dynamic route matching](https://router.vuejs.org/guide/essentials/dynamic-matching.html), Vue Router documentation

**Level:** Practitioner · Core

## Layouts and nested routes

Most pages share a header and footer. Nested routes let a shared layout stay on screen while the content inside it
changes.

**What to learn:**

- A layout route with a `RouterView` for child pages
- Nested routes, such as a profile page with "My Articles" and "Favorited Articles" tabs
- Moving focus to the new content after navigation, for screen reader users

**Resources:**
[Nested routes](https://router.vuejs.org/guide/essentials/nested-routes.html), Vue Router documentation

**Level:** Practitioner · Core

## Navigation guards

Some pages are only for signed-in users. A navigation guard sends other visitors to the sign-in page.

**What to learn:**

- A global `beforeEach` guard and route `meta` fields, to redirect signed-out users from pages such as the editor
  and settings, and a check of `to.query.feed` for the personal feed, which shares the home page's path
- Why a guard in the browser is only for convenience: the API must check every request itself

**Resources:**

- [Navigation guards](https://router.vuejs.org/guide/advanced/navigation-guards.html), Vue Router documentation
- [Authorization](../../../../security/audit/security-audit-reference.md#31-authorization), in the Techversant
  security audit reference

**Level:** Practitioner · Core

## Lazy-loaded routes

Lazy loading loads the code for a page only when someone opens it, so the first page loads faster.

**What to learn:**

- Loading route components with dynamic imports
- Checking the build output to see which files each page loads

**Resources:**
[Lazy loading routes](https://router.vuejs.org/guide/advanced/lazy-loading.html), Vue Router documentation

**Level:** Advanced · Optional

## Project: Add Every Page and Route

**Brief:** Add the routing for every RealWorld page, using the route table in `specs/e2e/SELECTORS.md`: home, tag
feeds, sign-in, sign-up, editor, settings, profile, favourites and article. Pages can show placeholder content where
the forms come in stage 06.

**Size:** 2 days

**Verification**, checked by a reviewer:

- [ ] Every route in the selector contract opens the right page, including `/tag/:tag` and `?page=N`
- [ ] Opening any of these URLs directly in a new tab shows the same page as navigating to it
- [ ] The browser's back and forward buttons move between pages as expected
- [ ] The header and footer come from one shared layout, and the active link has the `active` class
- [ ] Signed-out visitors to `/editor`, `/settings` and `/?feed=following` are sent to `/login`
- [ ] An unknown URL shows a "not found" page

Previous: [04. State and Data Flow](./04-state-and-data-flow.md) · Next:
[06. Forms and Validation](./06-forms-and-validation.md)
