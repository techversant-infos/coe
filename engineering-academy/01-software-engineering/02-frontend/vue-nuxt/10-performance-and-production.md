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

- Finding large packages in the bundle with `nuxt analyze`
- Loading heavy components only when needed, with the `Lazy` prefix, and delaying their hydration until they are
  visible
- Choosing small packages, and importing only the parts you use

**Resources:** [nuxt analyze](https://nuxt.com/docs/4.x/api/commands/analyze), Nuxt documentation

**Level:** Advanced · Core

## Images and fonts

Images are often the largest files on a page, and late-loading fonts make text jump. Nuxt modules handle both.

**What to learn:**

- `NuxtImg` from Nuxt Image: sizes, lazy loading, and setting width and height to prevent layout shift
- Loading fonts with Nuxt Fonts, so they are served with the app and do not shift the layout
- Loading the page's main image early with `NuxtImg`'s `preload` prop or `fetchpriority="high"`, to improve LCP

**Resources:** [Nuxt Image](https://image.nuxt.com/) and [Nuxt Fonts](https://fonts.nuxt.com/) documentation

**Level:** Advanced · Core

## Security headers

Security headers tell the browser to block whole classes of attack. A Content Security Policy (CSP) lists the only
places scripts may load from, which limits the damage of a cross-site scripting bug.

**What to learn:**

- The headers Techversant requires, such as `Content-Security-Policy`, `Strict-Transport-Security` and
  `X-Content-Type-Options`
- Setting them with the Nuxt Security module, with a strict CSP that uses nonces for pages rendered on request and
  hashes for prerendered pages, instead of `unsafe-inline`
- Checking the headers on the deployed site, including error pages, not only in local development

**Resources:**

- [Security headers](../../../../security/audit/security-audit-reference.md#42-security-headers) and
  [Cross-site scripting and output encoding](../../../../security/audit/security-audit-reference.md#73-cross-site-scripting-and-output-encoding),
  in the Techversant security audit reference
- [Strict CSP](https://nuxt-security.vercel.app/advanced/strict-csp), Nuxt Security documentation

**Level:** Advanced · Core

## Error monitoring and logging

When a page breaks for a user, you need to know before they report it. Error monitoring collects errors from browsers
and servers, with enough detail to fix them.

**What to learn:**

- Catching errors with `error.vue` and `NuxtErrorBoundary`, and showing a friendly message
- Sending errors to the monitoring tool your project uses, with the page, release and browser
- Never sending tokens, passwords or personal data in error reports and logs

**Resources:**

- [Error handling](https://nuxt.com/docs/4.x/getting-started/error-handling), Nuxt documentation
- [What must never be logged](../../../../security/audit/security-audit-reference.md#112-what-must-never-be-logged),
  in the Techversant security audit reference

**Level:** Advanced · Core

## Deployment

A production build runs differently from the development server. It must be built, configured and run the same way
every time.

**What to learn:**

- Building with `nuxt build`, running the server from `.output`, and packaging it in a Docker image
- Runtime config set from environment variables, which ones reach the browser (`NUXT_PUBLIC_`), and keeping secrets
  out of them. Only keys declared in `runtimeConfig` can be set from `NUXT_` variables, so one Docker image can
  serve every environment.
- Watching Nuxt's security advisories, running `npm audit` in continuous integration, and upgrading promptly
- Removing practice-only and debug code from production builds

**Resources:** [Deployment](https://nuxt.com/docs/4.x/getting-started/deployment), Nuxt documentation

**Level:** Advanced · Core

## Project: Make It Production-Ready

**Brief:** Prepare your Nuxt RealWorld front end for production: meet the Core Web Vitals targets, add security
headers, set up error reporting, and run it from a Docker image. Have a senior engineer review the security headers.

**Size:** 4 days

**Verification**, checked by a reviewer:

- [ ] Lighthouse on the production build, with mobile settings, shows LCP of 2.5 seconds or less and CLS of 0.1 or
  less on the home and article pages, and Total Blocking Time is recorded as the lab stand-in for INP
- [ ] The `nuxt analyze` report is in the pull request, and no page loads a package it does not use
- [ ] The app's own images use `NuxtImg` with sizes set. User avatars, which can come from any address, use a plain
  `img` with width and height set. Fonts load through Nuxt Fonts.
- [ ] The running Docker container sends every header the security audit reference requires, on normal and error
  pages, with a CSP that has no `unsafe-eval` and no `unsafe-inline` for scripts
- [ ] The pull request explains which pages use nonces and which use hashes
- [ ] A senior engineer has reviewed the security headers, and the review is linked in the pull request
- [ ] Errors show a friendly page and reach the error log, with no token or personal data in them
- [ ] The app runs from a Docker image built in continuous integration, with configuration from environment
  variables only
- [ ] A search of the production build finds no `__conduit_debug__` and no `jwtToken`
- [ ] `npm audit` runs in continuous integration, and the app uses a Nuxt release with no known high or critical
  advisories

Previous: [09. Testing](./09-testing.md) · Back to the [roadmap](./README.md#capstone) for the capstone
