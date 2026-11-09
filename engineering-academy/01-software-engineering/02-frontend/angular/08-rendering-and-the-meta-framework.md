# 08. Rendering and the Meta-Framework

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-09 · **Next review:** 2027-02-09

In React and Vue, a separate meta-framework adds server rendering. Angular builds it in: the Angular command-line
interface (CLI) and `@angular/ssr` render pages on a Node.js server, prerender them at build time, or leave them to the
browser. This stage covers server rendering in Angular 22. Back to the [roadmap](./README.md).

## Server-side rendering

With server-side rendering (SSR), a Node.js server runs your Angular app for each request and sends finished HTML.
The server is an Express app in `server.ts`, which you can extend.

**What to learn:**

- Adding SSR with the Angular CLI, and what `server.ts` and the server app configuration do
- Code that only works in the browser, such as `localStorage` and `window`, and running it in `afterNextRender`
- Reading the incoming request with the `REQUEST` token, a Web API `Request` that is null in the browser and during
  prerendering, and reading cookies with `headers.get('cookie')`

**Resources:** [Server-side rendering](https://angular.dev/guide/ssr), Angular documentation

**Level:** Advanced · Core

## Hydration

After the server sends HTML, the browser hydrates it: Angular attaches to the existing page instead of rebuilding
it. Incremental hydration, the default in Angular 22, hydrates parts of the page only when they are needed.

**What to learn:**

- Hydration, and the errors caused when the server and browser render different markup
- `@defer` blocks with hydration triggers, such as `hydrate on viewport`
- Checking hydration in Angular DevTools

**Resources:**
[Incremental hydration](https://angular.dev/guide/incremental-hydration), Angular documentation

**Level:** Advanced · Core

## Data on the server

Data the server loads should reach the browser with the page, so the browser does not fetch it again.

**What to learn:**

- The HTTP transfer cache, which passes server responses to the browser, and why it skips requests with an
  `Authorization` header. Leave that setting off: the `/user` response contains the token, which would end up in the
  page.
- `HTTP_TRANSFER_CACHE_ORIGIN_MAP`, when the server calls the API at a different address from the browser
- `resource` and `rxResource` with an `id`, so their server results are reused in the browser. `httpResource` uses the
  HTTP transfer cache instead.
- Calling the RealWorld API from the server with the user's token, without sending the token to the browser

**Resources:** [HTTP transfer cache](https://angular.dev/guide/ssr#caching-data-when-using-httpclient), Angular
documentation

**Level:** Advanced · Core

## Caching personalized responses

Server-rendered HTML can contain the signed-in user's name or private data. Treat cache behavior as part of the
authorization boundary: a response generated for one user must never be served to another user by a browser cache,
reverse proxy or CDN.

**What to learn:**

- Classifying rendered pages and API responses as public or personalized before enabling caching
- Applying `Cache-Control: no-store` to personalized HTML and authenticated API or proxy responses, and checking that
  deployment infrastructure respects it
- Keeping authenticated responses out of shared or application-managed caches unless a reviewed design proves the
  cache is correctly isolated by user and tenant
- Testing the same route with two separate sessions after warming any configured cache

**Resources:** [OWASP Web Cache Security](https://cheatsheetseries.owasp.org/cheatsheets/Web_Cache_Security_Cheat_Sheet.html)
and [HTTP Security Response Headers](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html).

**Level:** Advanced · Core

## Render modes

Each route can be rendered on every request, prerendered at build time, or rendered only in the browser. Server
route configuration sets the mode for each route.

**What to learn:**

- Server routes with `RenderMode.Server`, `RenderMode.Prerender` and `RenderMode.Client`
- Which pages are the same for every visitor. In RealWorld almost every page shows the signed-in user in the header, so
  most pages must render on request, and a prerendered page cannot carry a per-request Content Security Policy (CSP)
  nonce.
- Checking the build output to see how each route is rendered

**Resources:**
[Rendering strategies](https://angular.dev/guide/routing/rendering-strategies), Angular documentation

**Level:** Advanced · Core

## Authentication on the server

With SSR, the token can live in an httpOnly cookie that only the server reads. This is Red Zone work: write it by
hand, and have a senior engineer review it.

**What to learn:**

- Express endpoints in `server.ts` for sign-in, sign-up and sign-out that call the RealWorld API, set the token in an
  httpOnly cookie, and remove `token` from every response they send to the browser
- An `/api` proxy route in `server.ts`, registered before the Angular handler, that forwards the browser's calls to the
  RealWorld API with `Authorization: Token <jwt>` from the cookie, so buttons such as favourite and follow work after
  hydration
- An interceptor that, on the server, reads the cookie from the request and sends the token to the RealWorld API
  directly
- Guards that redirect signed-out users, and the server checking the session again before loading their data
- Passing the signed-in user, without the token, to the browser in `TransferState`, so the browser's first render and
  its guards match the server
- Setting the cookie's `Secure`, `SameSite` and `Path` attributes, and protecting requests that change data from
  cross-site request forgery (CSRF). The `XSRF-TOKEN` cookie and `X-XSRF-TOKEN` header are only a sketch, not a complete
  security design: agree the approach with a senior engineer and follow the security audit reference and OWASP CSRF
  guidance. Cover how protection is established before sign-in, sign-in and sign-up requests, session changes, and
  every state-changing request; do not copy a naive double-submit design.
- On client projects with a Laravel back end, using Laravel Sanctum's cookie-based sessions, where Laravel owns the
  session

**Resources:**

- [Security](https://angular.dev/best-practices/security), Angular documentation, which covers CSRF protection in the
  HTTP client
- [Cross-Site Request Forgery Prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html),
  OWASP
- [Session management](../../../../security/audit/security-audit-reference.md#93-session-management) and
  [CSRF](../../../../security/audit/security-audit-reference.md#35-cross-site-request-forgery-csrf), in the
  Techversant security audit reference

**Level:** Advanced · Core

## Analog

Analog is a meta-framework for Angular with file-based routing and API routes, similar to Nuxt and Next.js. Some
projects use it.

**What to learn:**

- How Analog's file-based routes and API routes compare with the Angular CLI's SSR

**Resources:** [Analog](https://analogjs.org/)

**Level:** Advanced · Optional

## Project: Render the App on the Server

**Brief:** Add server-side rendering to your RealWorld front end. Render every page on the server, prerender what can
be shared, and move the token from `localStorage` into an httpOnly cookie handled by the SSR server. Write the sign-in,
cookie, proxy, interceptor and guard code by hand, and have a senior engineer review it.

**Size:** 5 days

**Verification**, checked by a reviewer:

- [ ] Every route in the selector contract works, and opening any page directly shows content without waiting for
  browser JavaScript
- [ ] The browser console shows no hydration errors, and browser-only code runs only in the browser
- [ ] For a signed-out visitor, articles and tags the server loaded are not fetched again by the browser on the first
  page load
- [ ] Every request that needs the token, including favourite, follow, comment and delete, goes through the `/api` proxy
  on the SSR server, which adds the token from the cookie and checks the XSRF header on changes, and every sign-in and
  sign-up endpoint validates its input with the same Zod schema as the browser
- [ ] A senior engineer reviews and records the CSRF design, including pre-authentication, sign-in, sign-up and
  session changes; tests show that requests without valid protection are rejected
- [ ] The token is in an httpOnly, `Secure`, `SameSite` cookie, and no browser script can read it: no response from the
  SSR server and no transfer state in the page contains it
- [ ] Personalized SSR pages and authenticated API or proxy responses use `Cache-Control: no-store`; after warming
  the route as one user, a second session never receives the first user's content
- [ ] Reloading `/settings` while signed in shows the settings page with the signed-in header and no redirect, because
  the browser receives the user in `TransferState`
- [ ] Guards redirect signed-out users from `/editor`, `/settings` and `/?feed=following`, and the server checks the
  session again before loading their data
- [ ] No route prerenders a page that shows the signed-in user or their data
- [ ] A senior engineer has reviewed the sign-in, cookie, proxy, interceptor and guard code, and the review is linked in
  the
  pull request
- [ ] The `jwtToken` key and the debug interface are gone, because `ssr` mode does not use them
- [ ] The RealWorld end-to-end tests run with `TEST_MODE=ssr` against the public demo API, and the pull request
  records how many ran, passed, failed and were skipped. Every skipped test is one the suite marks as SPA-only
  (single-page app only).

Previous: [07. Working with APIs](./07-working-with-apis.md) · Next: [09. Testing](./09-testing.md)
