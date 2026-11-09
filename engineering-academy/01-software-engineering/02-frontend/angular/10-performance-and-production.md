# 10. Performance and Production

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

A front end is finished when it is fast, secure and running where users can reach it. This stage covers measuring
speed, sending less code, protecting the page with security headers, and knowing when something breaks in
production. Back to the [roadmap](./README.md).

## Core Web Vitals

Core Web Vitals are Google's measures of how a page feels to use. A page passes when at least 75% of visits meet each
target.

**What to learn:**

- Largest Contentful Paint (LCP), 2.5 seconds or less: how fast the main content appears
- Interaction to Next Paint (INP), 200 milliseconds or less: how fast the page responds to a click or key press
- Cumulative Layout Shift (CLS), 0.1 or less: how much the page jumps around while loading
- Measuring with Lighthouse in the browser, and with real users through the `web-vitals` library

**Resources:**

- [Web Vitals](https://web.dev/articles/vitals), web.dev
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview), Chrome for Developers

**Level:** Advanced · Core

## Bundle size and code splitting

Every kilobyte of JavaScript must be downloaded and run before the page responds. Sending less code is often the
biggest speed gain.

**What to learn:**

- Size budgets in `angular.json`, which fail the build when a bundle grows too large
- Finding large packages with the build's stats output, and loading heavy parts of a page only when needed with
  `@defer`
- Choosing small packages, and importing only the parts you use

**Resources:** [Building Angular apps](https://angular.dev/tools/cli/build), Angular documentation

**Level:** Advanced · Core

## Images and fonts

Images are often the largest files on a page, and late-loading fonts make text jump. Angular has tools for both.

**What to learn:**

- `NgOptimizedImage`: sizes, lazy loading, and setting width and height to prevent layout shift
- Marking the page's main image with `priority`, to improve LCP
- How the production build inlines font stylesheets, and keeping font files small

**Resources:**
[Image optimization](https://angular.dev/guide/image-optimization), Angular documentation

**Level:** Advanced · Core

## Security headers

Security headers tell the browser to block whole classes of attack. A Content Security Policy (CSP) lists the only
places scripts may load from, which limits the damage of a cross-site scripting bug.

**What to learn:**

- The headers Techversant requires, such as `Content-Security-Policy`, `Strict-Transport-Security` and
  `X-Content-Type-Options`, set by the server-side rendering (SSR) server
- A strict CSP with a nonce, because Angular's automatic CSP (`autoCsp`) does not work with server-side rendering:
  `server.ts` creates a new nonce for each request, puts it in the CSP header and in the root element's `ngCspNonce`
  attribute, and Angular applies it to the inline styles it adds
- Angular's built-in sanitizing of values in templates, and why bypassing it is a security risk
- Checking the headers on the deployed site, including error pages, not only in local development

**Resources:**

- [Security headers](../../../../security/audit/security-audit-reference.md#42-security-headers) and
  [Cross-site scripting and output encoding](../../../../security/audit/security-audit-reference.md#73-cross-site-scripting-and-output-encoding),
  in the Techversant security audit reference
- [Security](https://angular.dev/best-practices/security), Angular documentation

**Level:** Advanced · Core

## Error monitoring and logging

When a page breaks for a user, you need to know before they report it. Error monitoring collects errors from browsers
and servers, with enough detail to fix them.

**What to learn:**

- A custom `ErrorHandler`, and showing a friendly message when a page fails
- `provideBrowserGlobalErrorListeners()`, which new projects include, so uncaught errors and rejected promises also
  reach the `ErrorHandler`
- Sending errors to the monitoring tool your project uses, with the page, release and browser
- Never sending tokens, passwords or personal data in error reports and logs

**Resources:**
[What must never be logged](../../../../security/audit/security-audit-reference.md#112-what-must-never-be-logged), in
the Techversant security audit reference

**Level:** Advanced · Core

## Deployment

A production build runs differently from the development server. It must be built, configured and run the same way
every time.

**What to learn:**

- Building with `ng build`, running the SSR server from the `dist` folder, and packaging it in a Docker image
- Why values in Angular's environment files are built into the bundle and readable by anyone, and keeping secrets
  on the server
- Listing the site's host names in `allowedHosts` in `angular.json`, so the SSR server answers requests for any other
  host with a 400 error instead of calling addresses an attacker chose
- Removing practice-only and debug code from production builds
- Watching Angular's security advisories, running `npm audit` in continuous integration, and upgrading promptly

**Resources:** [Deployment](https://angular.dev/tools/cli/deployment), Angular documentation

**Level:** Advanced · Core

## Project: Make It Production-Ready

**Brief:** Prepare your Angular RealWorld front end for production: meet the Core Web Vitals targets, add security
headers, set up error reporting, and run it from a Docker image. Have a senior engineer review the security headers.

**Size:** 4 days

**Verification**, checked by a reviewer:

- [ ] Lighthouse on the production build, with mobile settings, shows LCP of 2.5 seconds or less and CLS of 0.1 or
  less on the home and article pages, and Total Blocking Time is recorded as the lab stand-in for INP
- [ ] Size budgets are set in `angular.json`, the build passes them, and no page loads a package it does not use
- [ ] The app's own images use `NgOptimizedImage` with sizes set. User avatars, which can come from any address, use
  a plain `img` with width and height set.
- [ ] The running Docker container sends every header the security audit reference requires, on normal and error
  pages, with a CSP that has no `unsafe-eval` and no `unsafe-inline` for scripts
- [ ] The pull request explains how the CSP nonce is created for each request and how it reaches the page
- [ ] A senior engineer has reviewed the security headers, and the review is linked in the pull request
- [ ] Errors show a friendly page and reach the error log, with no token or personal data in them
- [ ] The app runs from a Docker image built in continuous integration, with secrets from environment variables on
  the server only
- [ ] The SSR server lists its host names in `allowedHosts`, and a request with an unknown `Host` header gets a 400
  response
- [ ] A search of the production build finds no `__conduit_debug__` and no `jwtToken`
- [ ] `npm audit` runs in continuous integration, and the app uses an Angular release with no known high or critical
  advisories

Previous: [09. Testing](./09-testing.md) · Back to the [roadmap](./README.md#capstone) for the capstone
