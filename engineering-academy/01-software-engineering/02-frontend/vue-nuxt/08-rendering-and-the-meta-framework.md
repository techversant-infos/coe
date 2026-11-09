# 08. Rendering and the Meta-Framework

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Vue shows the interface; a meta-framework adds file-based routing, server rendering, data loading and a production
server around it. Nuxt is the meta-framework for Vue. This stage covers Nuxt 4. Back to the [roadmap](./README.md).

## Pages, layouts and the app directory

In Nuxt 4, your code lives in the `app` directory. Files in `app/pages` become routes, and layouts wrap them.

**What to learn:**

- Pages and dynamic routes, such as `app/pages/article/[slug].vue`, and linking with `NuxtLink`
- Layouts in `app/layouts`, and `error.vue` for errors and missing pages
- Auto-imports: which components, composables and utilities Nuxt imports for you, and where they come from

**Resources:**
[Pages directory](https://nuxt.com/docs/4.x/guide/directory-structure/app/pages), Nuxt documentation

**Level:** Advanced · Core

## Server rendering and hydration

Nuxt renders each page on the server and sends finished HTML. The browser then hydrates it: Vue attaches to the HTML
and makes it interactive.

**What to learn:**

- What hydration is, and the mismatches caused when the server and browser render differently, such as with dates
  or `localStorage`
- Running browser-only code in `onMounted` or inside `<ClientOnly>`
- Why module-level state, such as a `ref` declared outside a composable, is shared by every user on the server,
  and keeping per-user state in `useState` or Pinia
- Runtime config: private values stay on the server, and only `public` values reach the browser

**Resources:**
[Server-side rendering](https://vuejs.org/guide/scaling-up/ssr.html), Vue documentation

**Level:** Advanced · Core

## Data fetching with useFetch

`useFetch` and `useAsyncData` load data on the server and pass it to the browser with the page, so the browser does
not fetch it again.

**What to learn:**

- `useFetch` and `useAsyncData`, their keys, and the `status`, `error` and `refresh` values they return
- Why calling `$fetch` directly in a component's setup fetches twice, once on the server and once in the browser,
  and why to keep it for event handlers
- Refetching when a route parameter or query value changes
- Calling your own server routes with `useFetch` or `useRequestFetch()` during server rendering, so the session
  cookie is sent
- Updating the page after a change with `refresh` or `refreshNuxtData`, and clearing user data on sign-out with
  `clearNuxtData`

**Resources:**
[Data fetching](https://nuxt.com/docs/4.x/getting-started/data-fetching), Nuxt documentation

**Level:** Advanced · Core

## Server routes

Files in `server/api` become API endpoints that run on the Nuxt server. They let the app call the RealWorld API from
the server, where the token can stay out of the browser. Anyone can call a server route directly, not only through
your pages.

**What to learn:**

- Writing a server route with `defineEventHandler`, and calling the RealWorld API from it
- Validating the body with the same Zod schema as the browser, for example with `readValidatedBody`
- Checking who the user is inside every server route that reads or changes their data

**Resources:** [Server directory](https://nuxt.com/docs/4.x/guide/directory-structure/server), Nuxt documentation

**Level:** Advanced · Core

## Route middleware and authentication

Route middleware runs before a page is shown, on the server and in the browser, which suits redirecting signed-out
users. It is not the place for full authorization checks. This is Red Zone work: write it by hand, and have a senior
engineer review it.

**What to learn:**

- Keeping the token in an httpOnly cookie set by a server route, or in a sealed (encrypted) session cookie with a
  module such as nuxt-auth-utils, and sending it to the API only from server code
- Redirecting signed-out users in route middleware, and checking the session again in server routes
- Loading the signed-in user once on the server, into `useState` or with nuxt-auth-utils' `useUserSession`, so the
  header and middleware see the same user on the server and in the browser. Keep the token in the session's
  server-only data, never in the user data the browser receives.
- Setting the cookie's `Secure`, `SameSite` and `Path` attributes, and protecting server routes that change data from
  cross-site request forgery (CSRF)
- On client projects with a Laravel back end, using Laravel Sanctum's cookie-based sessions, where Laravel owns the
  session

**Resources:**

- [Middleware directory](https://nuxt.com/docs/4.x/guide/directory-structure/app/middleware), Nuxt documentation
- [nuxt-auth-utils](https://github.com/atinux/nuxt-auth-utils), Nuxt module on GitHub
- [Session management](../../../../security/audit/security-audit-reference.md#93-session-management) and
  [CSRF](../../../../security/audit/security-audit-reference.md#35-cross-site-request-forgery-csrf), in the
  Techversant security audit reference

**Level:** Advanced · Core

## Rendering modes

Nuxt can render a page on every request, build it once at build time, cache it for a while, or render it only in the
browser. Route rules set the mode for each route.

**What to learn:**

- `routeRules` for prerendering, for caching with stale-while-revalidate (serve the cached page, then rebuild it in
  the background), and for turning off server rendering for a route
- Which pages are the same for every visitor. In RealWorld almost every page shows the signed-in user, so cache
  only shared data, such as tags, and never cache a page that uses a CSP nonce.
- Checking the build log and `.output/public` for prerendered routes, and the response headers for cached ones

**Resources:** [Rendering modes](https://nuxt.com/docs/4.x/guide/concepts/rendering), Nuxt documentation

**Level:** Advanced · Core

## Project: Move the App to Nuxt

**Brief:** Move your RealWorld front end to Nuxt 4. Render every page on the server, load page data with `useFetch`
or `useAsyncData`, send the forms through server routes, and move the token from `localStorage` into an httpOnly
cookie. Write the sign-in, cookie, middleware and server route session code by hand, and have a senior engineer
review it.

**Size:** 5 days

**Verification**, checked by a reviewer:

- [ ] Every route in the selector contract works, and opening any page directly shows content without waiting for
  browser JavaScript
- [ ] The browser console shows no hydration mismatch warnings, and browser-only code runs in `onMounted` or
  `<ClientOnly>`
- [ ] Page data loads on the server with `useFetch` or `useAsyncData`, and the browser does not repeat any of those
  requests on the first page load
- [ ] Every request that needs the token, including favourite, follow, comment and delete, goes through a server
  route that checks the session, and every form's server route validates its input with the same Zod schema as
  the browser
- [ ] No composable keeps user data in module-level state, and the header shows the same user on the server and in
  the browser
- [ ] The token is in an httpOnly, `Secure`, `SameSite` cookie or a sealed session, and no browser script can read it
- [ ] Route middleware redirects signed-out users from `/editor`, `/settings` and `/?feed=following`, and server
  routes check the session again before loading their data
- [ ] No route rule caches or prerenders a page that shows the signed-in user or their data
- [ ] A senior engineer has reviewed the sign-in, cookie, middleware and server route session code, and the review is
  linked in the pull request
- [ ] The `jwtToken` key and the debug interface are gone, because `ssr` mode does not use them
- [ ] The RealWorld end-to-end tests run with `TEST_MODE=ssr` against the public demo API, and the pull request records
  how many ran, passed, failed and were skipped. Every skipped test is one the suite marks as SPA-only (single-page app
  only).

Previous: [07. Working with APIs](./07-working-with-apis.md) · Next: [09. Testing](./09-testing.md)
