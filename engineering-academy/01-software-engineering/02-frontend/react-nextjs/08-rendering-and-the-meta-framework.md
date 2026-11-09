# 08. Rendering and the Meta-Framework

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

React shows the interface; a meta-framework adds routing, server rendering, data loading and a production server
around it. React's documentation recommends starting new apps with a framework, and Next.js is the one Techversant
uses most. This stage covers Next.js 16 with the App Router. Back to the [roadmap](./README.md).

## App Router

In the App Router, folders in the `app` directory become routes. Special files, such as `page.tsx` and
`layout.tsx`, decide what each route shows.

**What to learn:**

- Pages, layouts, and dynamic segments such as `app/article/[slug]/page.tsx`
- `loading.tsx`, `error.tsx` and `not-found.tsx` for loading, error and missing pages
- Linking between pages, and reading route parameters and search parameters

**Resources:**
[Layouts and pages](https://nextjs.org/docs/app/getting-started/layouts-and-pages), Next.js documentation

**Level:** Advanced · Core

## Server and Client Components

In the App Router, components are Server Components unless you mark them otherwise. They run only on the server and
send no JavaScript for themselves to the browser. Client Components, marked with `'use client'`, run in the browser
and can use state, effects and event handlers.

**What to learn:**

- Which parts of a page need to be Client Components, and keeping them small
- Passing data from Server Components to Client Components as props
- Keeping secrets, such as API keys, in server-only code, so they never reach the browser

**Resources:**
[Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components), Next.js
documentation

**Level:** Advanced · Core

## Data fetching and caching

Server Components can fetch data directly with `async` and `await`. Next.js 16 can cache the results, so pages load
fast without calling the API on every request.

**What to learn:**

- Fetching data in a Server Component, and streaming slow parts of the page with `Suspense`
- The `'use cache'` directive, and setting how long a result stays fresh with `cacheLife`
- Tagging cached data with `cacheTag`, and refreshing it after a change with `updateTag` or `revalidateTag`
- Never caching data that belongs to one user where another user could see it

**Resources:**

- [Fetching data](https://nextjs.org/docs/app/getting-started/fetching-data), Next.js documentation
- [Caching](https://nextjs.org/docs/app/getting-started/caching), Next.js documentation

**Level:** Advanced · Core

## Server Actions

A Server Action is an `async` function marked with `'use server'` that a form or button calls to change data. It
runs on the server, so it can use secrets and cookies safely. Anyone can call it with a direct POST request, not only
through your page.

**What to learn:**

- Calling a Server Action from a form, with `useActionState` from stage 06
- Checking who the user is, and validating the input with the same Zod schema, inside every Server Action
- Refreshing cached data with `updateTag` and redirecting after the action succeeds

**Resources:** [Mutating data](https://nextjs.org/docs/app/getting-started/mutating-data), Next.js documentation

**Level:** Advanced · Core

## Proxy and authentication

From Next.js 16, Middleware is called Proxy and lives in a `proxy.ts` file. It runs before a request reaches a
route, which suits quick checks such as redirecting signed-out users. It is not the place for full authorization
checks. This is Red Zone work: write it by hand, and have a senior engineer review it.

**What to learn:**

- Keeping the token in an httpOnly cookie, set on the server after sign-in, and sending it to the API from server
  code
- Redirecting signed-out users in Proxy, and checking the session again where the data is loaded
- Setting the cookie's `Secure`, `SameSite` and `Path` attributes, and protecting form posts from cross-site request
  forgery (CSRF)
- On client projects with a Laravel back end, using Laravel Sanctum's cookie-based sessions, where Laravel owns the
  session

**Resources:**

- [Proxy](https://nextjs.org/docs/app/getting-started/proxy) and
  [Authentication](https://nextjs.org/docs/app/guides/authentication), Next.js documentation
- [Session management](../../../../security/audit/security-audit-reference.md#93-session-management) and
  [CSRF](../../../../security/audit/security-audit-reference.md#35-cross-site-request-forgery-csrf), in the
  Techversant security audit reference

**Level:** Advanced · Core

## Rendering strategies

Next.js can build a page once at build time, cache it and rebuild it later, or render it for every request. With
Cache Components, one page can mix all three: a fixed shell that loads straight away, with dynamic parts streamed in.

**What to learn:**

- Static, cached and request-time content, and what must wait for a request, such as reading cookies
- Partial Prerendering: a static shell with request-time parts inside `Suspense`. With Cache Components, a
  component that reads cookies outside `Suspense`, such as a header that shows the signed-in user, stops the build
  with an error.
- Checking the build output to see how each route is rendered

**Resources:** [Caching](https://nextjs.org/docs/app/getting-started/caching), Next.js documentation, which shows a
page that mixes static, cached and streamed parts

**Level:** Advanced · Core

## Project: Move the App to Next.js

**Brief:** Move your RealWorld front end to Next.js 16 with the App Router. Render the article, profile and home pages
with Server Components, use Server Actions for the forms, and move the token from `localStorage` into an httpOnly
cookie. Write the sign-in, cookie and Proxy code by hand, and have a senior engineer review it.

**Size:** 5 days

**Verification**, checked by a reviewer:

- [ ] Every route in the selector contract works, and opening any page directly shows content without waiting for
  browser JavaScript
- [ ] Client Components are used only where a page needs state or event handlers, and each one is marked
  `'use client'`
- [ ] Every form uses a Server Action that validates its input with the same Zod schema as the browser
- [ ] The token is in an httpOnly, `Secure`, `SameSite` cookie, and no browser script can read it
- [ ] Proxy redirects signed-out users from `/editor`, `/settings` and `/?feed=following`, and the server checks the
  session again before loading their data
- [ ] No page caches one user's data where another user can see it, such as the personal feed or settings
- [ ] A senior engineer has reviewed the sign-in, cookie and Proxy code, and the review is linked in the pull request
- [ ] The `jwtToken` key and the debug interface are gone, because `ssr` mode does not use them
- [ ] The RealWorld end-to-end tests run with `TEST_MODE=ssr` against the public demo API, and the pull request
  records how many ran, passed, failed and were skipped. Every skipped test is one the suite marks as SPA-only
  (single-page app only).

Previous: [07. Working with APIs](./07-working-with-apis.md) · Next: [09. Testing](./09-testing.md)
