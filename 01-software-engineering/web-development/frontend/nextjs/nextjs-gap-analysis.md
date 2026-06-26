# Next.js â€” Gap Analysis (Internal Review Document)

> **Audience:** CoE Web Working Group, tech leads, and reviewers â€” not a reader-facing document.
> **Purpose:** Show how the [Next.js Learning Path](./intermediate.md) maps to the wider Next.js ecosystem (App Router, Server Components, Server Actions, deployment surfaces, ecosystem libraries) and to the visual map in [nextjs-learning-path.png](./nextjs-learning-path.png). Used during pilot review to challenge scope decisions, not during onboarding.

---

## How to read this document

- **âœ… covered** â€” the path explicitly teaches this and assesses it
- **âš ï¸ partial** â€” the path touches this but doesn't go deep; a sibling document or a future phase covers the rest
- **âŒ not covered (with reason)** â€” the path deliberately skips this; the reason is given so a reviewer can challenge the call

A reviewer should walk this table top-to-bottom in roughly 10 minutes, then ask: *for any âš ï¸ row, is the depth enough for our pilot batch?* and *for any âŒ row, is the reason still valid in 2026?*

---

## Gap analysis: our path vs. the full Next.js ecosystem

The Next.js ecosystem is smaller and more focused than the React one. The major branches a 2026 Next.js team needs to think about are: **routing (App Router)**, **rendering (Server vs. Client Components)**, **data (fetch, Server Actions, route handlers)**, **auth**, **styling/UI**, **testing**, **deployment/infra**, **performance**, **security**, and **ecosystem integrations** (CMS, analytics, payments, etc.).

| Next.js branch / topic | Status | Where / Why |
|---|---|---|
| **JS / TS basics** | âœ… | [Phase 1](./intermediate.md#phase-1--javascript--typescript-refresh) â€” modules, async/await, destructuring, fetch, `tsconfig` essentials |
| **React fundamentals** (JSX, components, hooks) | âœ… | [Phase 2](./intermediate.md#phase-2--react-fundamentals) â€” quick refresher for backend engineers; deeper coverage in the [React path Phase 2â€“6](../react/intermediate.md) |
| **App Router** (file-based routing, layouts, loading, error, not-found) | âœ… | [Phase 3](./intermediate.md#phase-3--nextjs-basics-with-the-app-router) â€” pages, layouts, special files, dynamic routes, route groups, metadata |
| **Server Components vs. Client Components** | âœ… | [Phase 4](./intermediate.md#phase-4--server-components-vs-client-components) â€” boundary, serialization rules, when not to use `"use client"`, mental model |
| **Caching & revalidation** (`fetch` cache, `revalidatePath`, `revalidateTag`, dynamic flags) | âœ… | [Phase 4](./intermediate.md#phase-4--server-components-vs-client-components) + [Phase 10](./intermediate.md#phase-10--production-readiness) â€” when to use `force-cache`, `no-store`, tagged revalidation |
| **Partial Prerendering (PPR)** | âš ï¸ partial | [Phase 4](./intermediate.md#phase-4--server-components-vs-client-components) â€” explicitly demoted to "advanced, come back to this after Week 8." The right call for a pilot batch. |
| **Data fetching (Server Components)** | âœ… | [Phase 5](./intermediate.md#phase-5--data-fetching-apis-and-backend-integration) â€” `fetch` in Server Components, error/loading states, `NEXT_PUBLIC_*` env handling |
| **Data fetching (Client)** | âœ… | [Phase 5](./intermediate.md#phase-5--data-fetching-apis-and-backend-integration) â€” TanStack Query standardized for client refetch / mutation / sharing |
| **Route handlers** (`app/api/.../route.ts`) | âœ… | [Phase 5](./intermediate.md#phase-5--data-fetching-apis-and-backend-integration) â€” for webhooks, callbacks, and proxying sensitive calls to Laravel |
| **Server Actions / React Server Functions** | âœ… | [Phase 6](./intermediate.md#phase-6--forms-validation-and-mutations) â€” explicitly called out as the modern mutation pattern; includes the "two names, one thing" note |
| **Forms + validation** (RHF, Zod) | âœ… | [Phase 6](./intermediate.md#phase-6--forms-validation-and-mutations) â€” RHF + Zod client-side, re-validate in Server Action, CoE error envelope |
| **Optimistic UI** | âœ… | [Phase 6](./intermediate.md#phase-6--forms-validation-and-mutations) â€” `useOptimistic` and the standard pattern |
| **File upload** (multipart, presigned URLs) | âœ… | [Phase 6](./intermediate.md#phase-6--forms-validation-and-mutations) â€” basic coverage; presigned URLs to S3/DO Spaces |
| **Authentication & Authorization** (Sanctum, middleware, RBAC) | âœ… | [Phase 7](./intermediate.md#phase-7--authentication-and-authorization) â€” Sanctum cookies, `middleware.ts`, `cookies()` from `next/headers`, three-place check |
| **Auth.js (NextAuth)** | âš ï¸ partial | [Recommended Courses](./intermediate.md#recommended-courses) â€” noted as "only needed if a project is not Laravel-backed." Correctly out of scope. |
| **Styling â€” Tailwind CSS** | âœ… | [Phase 3](./intermediate.md#phase-3--nextjs-basics-with-the-app-router) + [Phase 8](./intermediate.md#phase-8--ui-system-and-frontend-architecture) â€” our default; CSS Modules allowed only if a project predates Tailwind |
| **shadcn/ui** | âœ… | [Phase 8](./intermediate.md#phase-8--ui-system-and-frontend-architecture) â€” "owned by us" framing, copy-paste into `components/` |
| **Design tokens** | âœ… | [Phase 8](./intermediate.md#phase-8--ui-system-and-frontend-architecture) â€” "don't hardcode hex values" |
| **Folder structure** (route groups, `features/`, `components/`) | âœ… | [Phase 8](./intermediate.md#phase-8--ui-system-and-frontend-architecture) â€” the full tree with the `app/(auth)/` + `app/(protected)/` route group pattern |
| **Testing â€” Vitest + RTL** | âœ… | [Phase 9](./intermediate.md#phase-9--testing) â€” unit + component tests, MSW for API mocking |
| **Testing â€” Playwright E2E** | âœ… | [Phase 9](./intermediate.md#phase-9--testing) â€” auth flow, protected page, E2E for the critical user journey |
| **Testing â€” Server Actions directly** | âœ… | [Phase 9](./intermediate.md#phase-9--testing) â€” "a Server Action is just a function â€” import it in a Vitest test, call it, assert" |
| **Deployment â€” Vercel** | âœ… | [Phase 10](./intermediate.md#phase-10--production-readiness) â€” default target for new projects |
| **Deployment â€” self-hosted Node / Docker** | âœ… | [Phase 10](./intermediate.md#phase-10--production-readiness) â€” `output: 'standalone'`, image size, env |
| **Structured logging (Pino + requestId)** | âœ… | [Phase 10](./intermediate.md#phase-10--production-readiness) â€” per the Node.js standard |
| **Observability (Vercel Analytics, OpenTelemetry)** | âœ… | [Phase 10](./intermediate.md#phase-10--production-readiness) â€” Vercel Analytics + Speed Insights for Vercel; OTel via `instrumentation.ts` for self-hosted |
| **Error boundaries** (`error.tsx`, `global-error.tsx`) | âœ… | [Phase 3](./intermediate.md#phase-3--nextjs-basics-with-the-app-router) + [Phase 10](./intermediate.md#phase-10--production-readiness) |
| **Image / font optimization** (`next/image`, `next/font`) | âœ… | [Phase 10](./intermediate.md#phase-10--production-readiness) |
| **Accessibility** (a11y + axe-core in Playwright) | âœ… | [Phase 10](./intermediate.md#phase-10--production-readiness) + the rubric's a11y row |
| **SEO** (metadata, sitemap, robots, OG) | âœ… | [Phase 3](./intermediate.md#phase-3--nextjs-basics-with-the-app-router) + [Phase 10](./intermediate.md#phase-10--production-readiness) |
| **Security headers** (CSP, HSTS, X-Frame-Options, Referrer-Policy) | âœ… | [Phase 10](./intermediate.md#phase-10--production-readiness) â€” apply via `next.config.js` `headers()` function, not middleware |
| **Rate limiting** | âš ï¸ partial | [Phase 10](./intermediate.md#phase-10--production-readiness) â€” "typically at the Laravel API layer." Correct â€” we don't want to reinvent this in Next.js. |
| **CI/CD** (lint â†’ typecheck â†’ test â†’ build â†’ preview â†’ promote) | âœ… | [Phase 10](./intermediate.md#phase-10--production-readiness) + the GitHub Actions mini task |
| **GraphQL / Apollo / tRPC** | âŒ | **Deliberately omitted** â€” we standardize on **REST + Laravel** per the [REST API Best Practices](../../../../general/rest-api-best-practices.md) CoE standard. Revisit only if a product requires it. |
| **CMS / headless content** (Sanity, Contentful, Payload) | âŒ | Out of scope â€” our products are Laravel-backed, not content-driven. Revisit if a marketing site needs it. |
| **E-commerce** (Shopify, Stripe Checkout, Medusa) | âŒ | Out of scope. Payment + checkout is Red Zone. |
| **Real-time / WebSockets** (Pusher, Ably, `socket.io`, Next.js `after()`) | âŒ | Out of scope. **GAP to add: a one-liner in Phase 5** â€” "If a product needs real-time, escalate to a tech lead. `after()` for post-response work, Pusher/Ably for fan-out. Don't roll your own." |
| **i18n** (next-intl, next-i18next) | âŒ | **GAP.** Several Laravel-backed products ship with multiple locales. The [React path](../react/roadmap-gap-analysis.md) flagged this too. Add a pointer: "If the product supports multiple languages, see the CoE i18n policy (TODO)." |
| **PWA / offline** | âŒ | **GAP.** Same as React path â€” out of scope unless a product needs it. |
| **React 19 Compiler (auto-memoization)** | âŒ | **GAP.** The React path flagged this. The Next.js path should mention it too â€” the Compiler is opt-in for Next.js apps and "don't add manual memoization 'just in case'" still applies. |
| **Middleware edge cases** (geofencing, A/B routing, bot detection) | âŒ | Out of scope for a learning path. The path covers middleware as a proxy/gate in [Phase 7](./intermediate.md#phase-7--authentication-and-authorization); advanced middleware patterns (geofencing, A/B, bot detection) are not taught. |
| **i18n routing** (`/[locale]/...` route group) | âŒ | Out of scope. Pairs with the i18n policy gap above. |
| **Edge runtime vs. Node runtime** | âš ï¸ partial | [Phase 4](./intermediate.md#phase-4--server-components-vs-client-components) â€” not explicitly named, but the server/client guidance implicitly keeps us on the Node runtime. Worth a one-liner: "Stay on the Node runtime unless you have a specific edge case." |
| **ISR / on-demand revalidation** | âœ… | [Phase 5](./intermediate.md#phase-5--data-fetching-apis-and-backend-integration) + [Phase 10](./intermediate.md#phase-10--production-readiness) â€” `revalidatePath`, `revalidateTag` are the on-demand revalidation primitives |
| **Streaming with `<Suspense>` and `loading.tsx`** | âœ… | [Phase 3](./intermediate.md#phase-3--nextjs-basics-with-the-app-router) â€” "Streaming with `<Suspense>`" sub-section. Route-level `loading.tsx` vs. component-level `<Suspense>`, granular vs. coarse, request waterfalls, pair-with-caching note. |
| **`use cache` directive (Cache Components â€” React 19 / Next.js 15+/16 standard)** | âœ… | [Phase 5](./intermediate.md#phase-5--data-fetching-apis-and-backend-integration) â€” "Cache Components (the new model)" sub-section. The "cached by default â†’ opt-in" shift, when to use `"use cache"`, why the old default caused subtle bugs. |
| **Turbopack** (default bundler in Next.js 15+) | âŒ | **GAP.** New in Next.js 15. Worth a one-liner: "Turbopack is the default bundler in Next.js 15+. Don't add Webpack config unless you have a specific reason." |
| **App Router â†’ Pages Router migration** | âŒ | Out of scope â€” we don't migrate legacy Pages Router apps. New projects are App Router only. |
| **International SEO** (`hreflang`, locale-specific sitemaps) | âŒ | Out of scope. Pairs with the i18n policy gap above. |

---

## What we deliberately skipped (and why)

These Next.js ecosystem items don't appear in the path. Listing them so a reviewer can challenge the decision:

- **Pages Router** â€” App Router is our default. We don't teach the Pages Router at all; new code goes into `app/`.
- **GraphQL / tRPC** â€” REST + Laravel is our standard. GraphQL would mean a separate Laravel GraphQL layer; tRPC would mean coupling Next.js to the backend type system. Both break the architecture call.
- **CMS integrations** (Sanity, Contentful, Payload) â€” our content lives in Laravel, not in a third-party CMS.
- **Payments / checkout** â€” Red Zone. Auth/payment/prod DB work is never fully delegated to AI and always needs two-layer review. A Next.js path that taught Stripe would teach a pattern our security model doesn't support.
- **Real-time / WebSockets** â€” not a current need. Would be a future phase if a product requires it.
- **i18n routing** â€” out of scope until the CoE i18n policy exists. Pair with the React path's i18n gap.
- **PWA / offline** â€” out of scope unless a product explicitly needs it.
- **Custom Webpack config** â€” Turbopack is the new default. We don't teach the old one.
- **NextAuth / Auth.js** â€” only relevant for non-Laravel apps. Our auth lives in Laravel Sanctum.
- **Class components / `getServerSideProps` / `getStaticProps`** â€” Next.js App Router moves us to Server Components, Server Actions, and `fetch` caching. We don't teach the pre-App-Router mental model.
- **CSS-in-JS** (styled-components, Emotion) â€” Tailwind is our standard.
- **Storybook for component documentation** â€” **GAP.** Once we have a `shadcn/ui`-based component library, Storybook becomes valuable. Not in scope for the pilot; revisit when the first team reaches Phase 8 for the second time.
- **End-to-end type safety with tRPC / Zodios** â€” we standardize on REST + Zod for boundary validation. tRPC's value is type-safety across the network, which REST + Zod already gives us at the SDK boundary.

---

## Gaps that should probably be closed before full-team rollout

These are the items the gap analysis surfaced as **missing but worth adding** â€” small, targeted additions to a future v0.6:

1. **i18n** â€” one-line pointer in Phase 5 or 8, with a TODO for the CoE i18n policy
2. **React 19 Compiler note** â€” same wording as the [React path](../react/intermediate.md#phase-8--production-patterns-and-project-structure): opt-in, "don't add manual memoization 'just in case'"
3. **âœ… `use cache` directive / Cache Components** â€” closed in v0.6 (Phase 5 sub-section "Cache Components (the new model)"). Streaming also added in v0.6 as a Phase 3 sub-section.
4. **Turbopack** â€” one-line "Next.js 15+ updates" pointer in Phase 10
5. **Real-time** â€” one-line "escalate to a tech lead; don't roll your own" pointer in Phase 5
6. **Edge runtime vs. Node runtime** â€” one-line "stay on Node unless you have a specific edge case" in Phase 4
7. **Storybook** â€” defer; mention only when the second team reaches Phase 8

---

## Reviewer questions

When reviewing this gap analysis, ask:

1. For every **âš ï¸ partial** row: *is the depth enough for our pilot batch, or does it block Week-1 delivery?*
2. For every **âŒ not covered** row: *is the reason still valid in 2026?* Especially:
   - GraphQL / tRPC â€” has a new product appeared that needs end-to-end type safety?
   - i18n â€” has a new product appeared that ships with multiple locales?
   - Real-time â€” has a new product appeared that needs WebSockets / fan-out?
   - PWAs â€” has a new product appeared that needs offline / install-to-homescreen?
3. For every **âœ… covered** row: *is the depth right, or are we teaching too much / too little?*
4. **Pre-full-team rollout:** the items in "Gaps that should probably be closed" â€” can we land the open ones in v0.7 before the full-team rollout, or are they OK to defer to v0.8?

---

## Document control

| Field | Value |
|---|---|
| Document | Next.js â€” Gap Analysis |
| Version | 0.2 (Streaming row added; `use cache` row moved from âŒ GAP to âœ… Phase 5; "Gaps to close" item 3 closed) |
| Owner | CoE Web Working Group |
| Review Cycle | Quarterly |
| Status | Internal review document |
| Related | [intermediate.md](./intermediate.md), [nextjs-learning-path.png](./nextjs-learning-path.png), [React Learning Path](../react/intermediate.md) |
