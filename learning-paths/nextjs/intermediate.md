**Version:** 0.3
**Issued by:** Techversant Center of Excellence (CoE)
**Effective Date:** June 2026
**Audience:** Web Dev Team — backend/PHP/Laravel-leaning engineers who need to ship modern Next.js frontends
**Length:** 10 phases over 8 weeks (~5 hours/week, pair-friendly)
**Contributors:** Compiled by CoE Web Working Group, reviewed by Web team leads

# Next.js Learning Path — For the Web Dev Team
*From PHP/Laravel backend to confident Next.js frontend engineer.*

This path is written for **our** team. The team is strong on the backend (PHP, Laravel, REST APIs) and on its way on the frontend. We are not starting from zero — we are starting from "I can read JavaScript, I've touched some React, and I want to ship a Next.js app against our Laravel APIs."

The path moves: **JS/TS refresh → React fundamentals → Next.js App Router → Server/Client model → API integration → Forms/Auth → UI system → Testing → Production**. Each phase ends with a small team-shaped deliverable that can be reviewed.

> **Architecture call (read first):** For our Laravel-based products, we run Next.js as a **frontend** that talks to a Laravel API. We are **not** doing full-stack Next.js with direct DB access for these products. This path reflects that.

---

## 🎯 Learning Outcomes

By the end of this 8-week plan, every developer on the team should be able to:

1. Read and write modern TypeScript and React without slowing the team down.
2. Scaffold a Next.js App Router project and explain its file-based routing.
3. Choose the right boundary between Server Components and Client Components in a code review.
4. Connect a Next.js app to a Laravel API — auth, errors, caching, env, the works.
5. Build validated forms with React Hook Form + Zod, submit via Server Actions, render errors in the CoE standard envelope.
6. Apply role-based access in middleware, server actions, and route handlers — server-side every time.
7. Ship a feature with unit, component, and E2E tests; pass Lighthouse and a basic accessibility audit.
8. Deploy to Vercel (or a self-hosted Node target) with logs, traces, env management, and a rollback plan.

### Team-Level Metrics of Success

Beyond individual outcomes, we measure whether the path actually moved the team's velocity:

- **% of new frontend tickets completed without senior blocking** — track per quarter, target a meaningful rise from baseline
- **PR review turnaround** on frontend PRs — should drop as the team's pattern-recognition grows
- **Defect rate** on the first 30 days after a feature merges — should stay flat or fall
- **Onboarding time** for a new hire to ship their first frontend PR — target: 2 weeks

Re-baseline these at the end of week 8. If they're not moving, the path needs a revision, not a louder announcement.

---

## 📚 Table of Contents
- [Suggested 8-Week Plan](#suggested-8-week-plan)
- [Phase 1 — JavaScript + TypeScript Refresh](#phase-1--javascript--typescript-refresh)
- [Phase 2 — React Fundamentals](#phase-2--react-fundamentals)
- [Phase 3 — Next.js Basics with the App Router](#phase-3--nextjs-basics-with-the-app-router)
- [Phase 4 — Server Components vs. Client Components](#phase-4--server-components-vs-client-components)
- [Phase 5 — Data Fetching, APIs, and Backend Integration](#phase-5--data-fetching-apis-and-backend-integration)
- [Phase 6 — Forms, Validation, and Mutations](#phase-6--forms-validation-and-mutations)
- [Phase 7 — Authentication and Authorization](#phase-7--authentication-and-authorization)
- [Phase 8 — UI System and Frontend Architecture](#phase-8--ui-system-and-frontend-architecture)
- [Phase 9 — Testing](#phase-9--testing)
- [Phase 10 — Production Readiness](#phase-10--production-readiness)
- [Recommended Courses](#recommended-courses)
- [Channels, Podcasts & Newsletters](#channels-podcasts--newsletters)
- [Tutorial & Reference Links](#tutorial--reference-links)
- [Certifications](#certifications)
- [Books (Optional Deep Dives)](#books-optional-deep-dives)
- [How to Use This Path](#how-to-use-this-path)
- [Document Control](#document-control)

---

## Suggested 8-Week Plan

| Week | Focus | Output / Definition of Done |
|---|---|---|
| 1 | JS/TS refresh | Consume a Laravel API with `fetch()` and render a typed list |
| 2 | React basics | Product listing page with search, filter, and form validation |
| 3 | Next.js routing & layouts | Admin dashboard shell with sidebar, top bar, nested + dynamic routes |
| 4 | Server/Client components | Hybrid product page — server data + client filter/search |
| 5 | Data fetching & API integration | Next.js frontend wired to an existing Laravel API with auth tokens |
| 6 | Forms & auth | Login + protected CRUD page against Laravel |
| 7 | UI architecture & testing | Reusable component library + tests for the CRUD page |
| 8 | Production project | Small admin panel MVP: deployed, monitored, rollback-ready |

> **Buffer:** treat Weeks 7–8 as flexible. If the team is behind, fold the production work into a follow-up sprint rather than rushing. The point of the path is the **8 weekly deliverables**, not hitting 8 weeks exactly.

> **Working agreement:** the deliverable at the end of each week is what gets reviewed on Friday. Pair on the harder phases (4, 5, 7). Open a PR for the deliverable even if it's small — it builds the habit.

---

## Phase 1 — JavaScript + TypeScript Refresh

**Why this phase exists:** the team is comfortable with JavaScript at a basic level, but Next.js and our stack assume fluency with modern syntax and types. One week of refresh prevents a month of small stumbles later.

**Learn:**
- **JavaScript / ES6+**
  - Modules (`import` / `export`)
  - `async` / `await` and Promises
  - Destructuring, spread / rest
  - `map`, `filter`, `reduce`
  - `fetch` API
  - `npm` and `pnpm`
- **TypeScript basics**
  - Interfaces, types, generics
  - Typing API responses
  - `tsconfig.json` essentials (`strict`, `noImplicitAny`)

**Mini task:**
Build a small page or script that calls a Laravel API with `fetch()`, types the response, and renders a list of items. The point is **typing the wire format**, not building UI.

**Self-check:**
- [ ] I can `await` a `fetch` and narrow the response to a typed shape.
- [ ] I can explain why we never trust the API response to be the shape we asked for.
- [ ] I can run `pnpm dev` on a colleague's project without breaking it.

---

## Phase 2 — React Fundamentals

**Why this phase exists:** Next.js is React. Trying to learn the App Router while learning React doubles the cognitive load. One week of React-first practice pays back ten times in Phases 3–4.

**Learn:**
- JSX and components
- Props and state
- Events and conditional rendering
- Lists and keys
- Forms (controlled inputs)
- Hooks: `useState`, `useEffect`
- Custom hooks
- Component composition

**Source of truth:** the **official React docs at [react.dev](https://react.dev/learn)**. React is currently in the 19.x line — always read the current docs, not a 2022 blog post.

**Mini task:**
Build a **product listing page** with:
- Search (filter by name)
- Category filter
- A "contact seller" form with client-side validation
- Loading and empty states

Use a local mock JSON file — no API yet. Get code reviewed before moving on.

**Self-check:**
- [ ] I can explain the difference between a controlled and an uncontrolled input.
- [ ] I can lift state up when two siblings need to share it.
- [ ] I can write a custom hook that wraps a `useEffect`.

---

## Phase 3 — Next.js Basics with the App Router

**Why this phase exists:** Next.js is **not** "React with routing bolted on." The App Router introduces file-based routing, layouts, server-rendering, and a new mental model. Get the model right before adding complexity.

**Learn:**
- Project structure (`app/`, `public/`, `next.config.*`)
- File-based routing:
  - `page.tsx` — a route
  - `layout.tsx` — shared chrome
  - `loading.tsx` — streaming fallback
  - `error.tsx` — error boundary
  - `not-found.tsx` — 404
- Nested routes and **route groups** `(group)`
- Dynamic routes: `[slug]`, `[...catchAll]`
- Metadata and SEO basics (`generateMetadata`, `metadata` export)
- Styling: **Tailwind CSS** (our standard) — or CSS Modules if a project predates Tailwind

**Primary course:** the **official Next.js Learn course** at [nextjs.org/learn](https://nextjs.org/learn). It builds a dashboard with login, protected pages, and CRUD — close to what we actually ship.

**Mini task:**
Build an **admin dashboard shell**:
- Sidebar with at least 3 sections
- Top bar with user avatar placeholder
- One section uses nested routes
- One section has a dynamic detail page (e.g. `/customers/[id]`)
- All four special files (`loading`, `error`, `not-found`, `layout`) in place

**Self-check:**
- [ ] I can add a new route by creating a single file.
- [ ] I can explain when `layout.tsx` re-renders vs. `page.tsx`.
- [ ] I can write `generateMetadata` for a dynamic route.

---

## Phase 4 — Server Components vs. Client Components

**Why this phase exists:** **this is the biggest mental shift for PHP developers.** In Laravel, "render a page" usually means SSR or a Blade view. In Next.js App Router, every component is a **Server Component** by default — it runs on the server, can read the DB / call an API directly, and ships **zero JavaScript** to the browser. Client Components are the **opt-in exception**, not the default.

**Learn:**
- Server Components (default)
- Client Components — and the `"use client"` directive
- When **not** to use a Client Component
- Passing props between server and client components (serialization rules)
- Avoiding unnecessary client-side JavaScript
- The "server island" pattern: keep data on the server, push only the interactive bit to the client
- **Partial Prerendering (PPR)** — pre-render the static shell, stream the dynamic parts (opt-in via `next.config.js` in current Next.js releases)
- **Caching & dynamic flags:** when to set `dynamic = 'force-dynamic'`, `revalidate = 0`, or `cache: 'no-store'` on a `fetch`

**Mental model to internalize:**
> "Start as a server component. Add `"use client"` only when you need state, effects, or browser APIs. Push the boundary as far toward the leaves of the tree as possible."

**Server Component gotchas (read these once, refer back often):**
- No hooks (`useState`, `useEffect`, `useContext`, etc.) — they run on the server, hooks run on the client.
- No browser APIs (`window`, `localStorage`, `document`) — the server has no browser.
- **Props are serialized** when crossing the server→client boundary. You can pass plain objects, arrays, dates, and primitives. You **cannot** pass functions, class instances, or non-serializable things. If a function must be passed, wrap it in a Server Action.
- Async is fine — Server Components can be `async function Page()`. Do all data fetching there.
- A Client Component cannot import a Server Component; a Server Component **can** render a Client Component. The boundary flows one way.
- Marking a component `"use client"` does **not** make it a Client Component in isolation — it makes the **subtree** below it client-side. Scope it tightly.

**Mini task:**
Build a **products page** where:
- Product data is fetched on the **server** (mocked is fine)
- The filter / search UI runs on the **client** as a small island
- The page ships the minimum possible JavaScript

**Extended exercise (pair on this):**
1. Open DevTools → Network → JS. Record the bundle size with the filter on the client.
2. Move the filter to the server (use a Server Action with `revalidatePath`). Compare bundle size and request waterfall.
3. Write a one-paragraph note in the PR: "Was client-only because of X. Could be server if we change Y."

**Self-check:**
- [ ] I can name three things that **force** a Client Component.
- [ ] I can name three things that **should not** be in a Client Component.
- [ ] I can draw the server / client boundary for any page in our admin panel.
- [ ] I can explain when I'd reach for `dynamic = 'force-dynamic'` vs. PPR vs. plain static rendering.

---

## Phase 5 — Data Fetching, APIs, and Backend Integration

**Why this phase exists:** this is where the path pays for itself for our team. We are **not** doing full-stack Next.js with direct DB access for Laravel-backed products. We are calling our own Laravel API from a Next.js frontend. Get this integration right and the rest of the app gets easier.

**Learn:**
- Server-side data fetching in Server Components (using `fetch`, `axios`, or an SDK)
- Client-side data fetching — **we standardize on TanStack Query** (formerly React Query). Use it for any data the client needs to refetch, mutate, or share across components. Avoid duplicating server cache in client state.
- Caching: Next.js `fetch` cache, `revalidatePath`, `revalidateTag`
- Loading and error states
- Environment variables: `NEXT_PUBLIC_*` for client-safe values, server-only for secrets
- **Route handlers** (`app/api/.../route.ts`) for webhooks, callbacks, and **proxying sensitive calls** to Laravel (so API keys never reach the browser)
- Calling **protected** Laravel APIs: token in `Authorization: Bearer …`, refresh on 401

**Decision rule — when to use which:**
| Need | Use |
|---|---|
| Data is needed for the first paint, no user interaction | **Server Component** + `fetch` + revalidation |
| Data changes often, needs to be refetched, paginated, infinite-scrolled, or shared between components | **Server Component for initial load + TanStack Query on the client** for subsequent updates |
| Browser-only data (localStorage, user media, geolocation) | Client Component + TanStack Query |
| Webhook, callback, or proxy that must hide the API key | **Route handler** |

**Architecture call:** for our Laravel products, treat the Laravel API as the source of truth. Next.js fetches from it; it does not own the data. This is the same separation we have in our mobile apps.

**Mini task:**
Connect the dashboard shell to an existing Laravel API:
- Fetch a list endpoint in a Server Component
- Add a `loading.tsx` and an `error.tsx`
- Add a `POST` via a route handler that proxies to Laravel (hides the API key)
- Read the API base URL from `NEXT_PUBLIC_API_URL`
- Add a TanStack Query hook for a "live" widget (e.g. unread notifications) that refetches every 30s

**Self-check:**
- [ ] I can explain where the auth token lives and how it gets to the Laravel API.
- [ ] I can choose between caching, revalidating, or no-store for a given fetch.
- [ ] I can return a Laravel error to the UI in our [standard error envelope](../../general/rest-api-best-practices.md).
- [ ] I can decide whether a feature needs Server Component data, TanStack Query, or a route handler.

---

## Phase 6 — Forms, Validation, and Mutations

**Why this phase exists:** every product we ship is, eventually, a form. Forms are where the most bugs live. Get the form story right once and you stop re-learning it per project.

**Learn:**
- Form handling (controlled vs. `FormData` / Server Actions)
- **React Hook Form** for client-side forms
- **Zod** for schema validation (matches our Node.js standard)
- **Server Actions / Server Functions** for mutations from Server Components
- Optimistic UI
- Error display in the CoE standard error envelope
- Toast notifications
- File upload basics (multipart, presigned URLs for S3 / Spaces)

**Standard pattern (use this for new work):**

```
Client form (React Hook Form + Zod)
        │  submit
        ▼
Server Action (re-validates with Zod on the server)
        │  calls
        ▼
Laravel API
        │  revalidatePath / revalidateTag
        ▼
UI re-renders
```

**Mini task:**
Build a **customer add / edit form** with:
- React Hook Form + Zod schema
- Server Action that re-validates and posts to Laravel
- Inline field errors
- Toast on success
- Optimistic update on the list

**Self-check:**
- [ ] I can explain why we re-validate on the server even when the client validates.
- [ ] I can return a Zod error tree to the UI and render it field-by-field.
- [ ] I can write a Server Action that revalidates only the affected list.

---

## Phase 7 — Authentication and Authorization

**Why this phase exists:** **auth is Red Zone in our CoE AI policy — manual code, two-layer review, never fully delegate.** This phase exists to make sure every team member can build an auth flow correctly, not to be clever.

**Learn:**
- Session vs. JWT — when to pick which
- Cookie-based auth (our Laravel Sanctum default)
- Protected routes (middleware + server-side checks in pages and actions)
- Next.js **middleware** (`middleware.ts`) as a proxy / gate
- Role-based access (admin / manager / viewer)
- Token refresh
- Logout and session invalidation
- Calling Laravel with the session cookie attached
- Reading the httpOnly cookie in Server Components / Server Actions via `cookies()` from `next/headers` (the **only** safe way to read it on the server)

**Architecture call:** for PHP/Laravel products, **Laravel owns the session**. Next.js is a client of the Laravel API. Do not roll your own JWT in Next.js; do not store tokens in `localStorage`. Use **httpOnly cookies** set by Laravel, forwarded by Next.js.

**Sanctum cookies vs. JWT — when to use which:**

| Aspect | Laravel Sanctum (cookies) — **our default** | JWT in `Authorization: Bearer` |
|---|---|---|
| Storage | httpOnly cookie, invisible to JS | Often `localStorage` (XSS risk) or memory (lost on refresh) |
| CSRF | Mitigated by Sanctum's CSRF cookie + `withCredentials` | Mitigated by short expiry + refresh tokens |
| Server-side revocation | Trivial — delete the session | Hard — JWTs are stateless; need a deny-list |
| Best for | First-party web apps on the same domain or a trusted subdomain | Mobile apps, third-party API consumers, cross-domain |
| Our default for | **Next.js frontends against Laravel** | Mobile apps, public APIs |

If you think you need JWT for a Next.js frontend, **escalate to a tech lead first**. The defaults are Sanctum cookies.

**Mini task:**
Add a **login + protected CRUD page** to the admin shell:
- Login form posts to Laravel (`/api/auth/login`)
- Laravel sets an httpOnly cookie
- Next.js `middleware.ts` blocks unauthenticated users from `/app/*`
- A Server Action reads the cookie via `cookies()` and re-checks the session before any mutation
- Logout clears the cookie via Laravel

**Self-check:**
- [ ] I can name the **three** places an auth check must run and why all three.
- [ ] I can read an httpOnly cookie in a Server Action via `cookies()` without exposing it to JS.
- [ ] I can revoke a session server-side.
- [ ] I can explain why we don't put the token in `localStorage`.

---

## Phase 8 — UI System and Frontend Architecture

**Why this phase exists:** once we have 2–3 Next.js projects, copy-pasting components stops working. We need a shared UI system and a folder structure we can copy into a new project.

**Learn:**
- **Tailwind CSS** (our standard)
- **shadcn/ui** — copy-paste components, **owned by us** (the CLI drops the source into our repo, not `node_modules`). Treat it like our own code: review, refactor, delete, customize. Don't upstream-block on it.
- Reusable component patterns: layout, form, table, dialog, toast
- Design tokens (colors, spacing, type scale) — don't hardcode hex values
- Folder structure for feature-based architecture
- **Route groups** `(group)` for separating auth and protected layouts cleanly

**Suggested structure (use as a starting point, adapt per project):**

```
app/
  (auth)/             ← public auth pages — login, forgot-password
    login/page.tsx
    layout.tsx        ← no sidebar, marketing chrome
  (protected)/        ← gated by middleware + a server check
    layout.tsx        ← sidebar + top bar
    customers/
      page.tsx
      [id]/page.tsx
    orders/page.tsx
  api/                ← route handlers only (webhooks, proxy)
components/           ← shared, generic UI primitives (Button, Input, Dialog)
features/             ← vertical slices: customers/, orders/, billing/
  customers/
    components/
    hooks/
    actions.ts        ← Server Actions
    schemas.ts        ← Zod schemas
    types.ts
lib/                  ← framework glue (axios client, env, utils)
services/             ← API clients (Laravel SDK wrappers)
types/                ← cross-feature types
hooks/                ← cross-feature React hooks
```

**Why route groups matter here:** `app/(protected)/` lets the protected layout own the auth check, so a Server Component in `(protected)/customers/page.tsx` can assume the session is valid and re-check it explicitly. `(auth)/` and `(protected)/` are **organizational only** — they don't appear in the URL.

**Mini task:**
- Move the existing dashboard shell into `app/(protected)/` with its own layout that calls the auth check.
- Move the login page into `app/(auth)/login/page.tsx` with a marketing layout.
- Pick the customer feature from earlier phases and refactor it into the `features/customers/` shape above.
- Add a `<DataTable>` component and reuse it for the customer list.

**Self-check:**
- [ ] I can explain the difference between `components/` and `features/`.
- [ ] I can add a new feature without touching unrelated folders.
- [ ] I can use `shadcn/ui` to add a new primitive without adding a runtime dependency.
- [ ] I can explain what a route group is and when it improves the project.

---

## Phase 9 — Testing

**Why this phase exists:** we have a Node.js testing standard ([Node.js TypeScript Best Practices](../../nodejs/nodejs-typescript-best-practices.md)) — the Next.js path extends it.

**Learn:**
- Unit testing with **Vitest** (or Jest if a project predates it)
- Component testing with **React Testing Library**
- **Playwright** for E2E
- **API mocking with MSW** (Mock Service Worker) for unit and component tests — same handlers run in Node and the browser, so one definition covers both
- **Testing Server Actions directly:** a Server Action is just a function — import it in a Vitest test, call it, assert. No Next.js runtime needed. Mock the Laravel SDK at the `services/` boundary.
- **Playwright route interception** for E2E — use sparingly; prefer hitting a real staging API
- Form validation testing (submit invalid data, assert inline errors)
- Auth flow testing (login, protected page redirect, expired session)

**Minimum expectation per developer:**
> Every developer should know how to test **forms, protected pages, API error states, and at least one critical user flow** for their feature.

**Mini task:**
- Vitest test for one Server Action (happy path + one Zod failure) — import the action, mock the SDK, call it
- Vitest + RTL test for the customer form, with **MSW** returning a fake Laravel response
- One Playwright E2E: login → create customer → see it in the list

**Self-check:**
- [ ] I can test a Server Action without spinning up Next.js.
- [ ] I can test a Client Component without testing implementation details.
- [ ] I can write a Playwright test that survives a CSS refactor.
- [ ] I can mock Laravel responses with MSW and assert the UI renders the right error state.

---

## Phase 10 — Production Readiness

**Why this phase exists:** "works on my machine" is not shipped. Production is a different problem — observability, env, security headers, and the ability to roll back in under 2 minutes.

**Learn:**
- Build process: `next build` outputs, what's in the `.next/` folder
- Deployment targets: **Vercel** (default for new projects), self-hosted Node, Docker
- For Docker, use `output: 'standalone'` in `next.config.js` so the image stays small
- Environment variables: `.env.local`, `.env.example`, secret manager for prod
- **Structured logging** (Pino per our Node.js standard) with `requestId` in every line
- **Observability:** enable **Vercel Analytics + Speed Insights** when on Vercel; for self-hosted, OpenTelemetry via `instrumentation.ts` exporting to your tracing backend
- **Error boundaries** — `error.tsx` and `global-error.tsx`
- Performance: **`next/image`** for all images (auto WebP/AVIF, lazy loading, responsive sizes), **`next/font`** for self-hosted fonts, dynamic imports, partial prerendering
- **Accessibility:** semantic HTML first, ARIA only when needed, keyboard nav, focus management, color contrast — test with axe-core in Playwright
- SEO: metadata, sitemap, robots, Open Graph
- **Caching strategy** — when to use `force-cache`, `no-store`, tagged revalidation
- **Security headers** — CSP, HSTS, X-Frame-Options, Referrer-Policy (see [REST API Best Practices](../../general/rest-api-best-practices.md))
- Rate limiting (typically at the Laravel API layer)
- **CI/CD** — lint → typecheck → test → build → preview → promote

**Mini task:**
Take the admin panel MVP and ship it to staging:
- Add a GitHub Actions workflow: lint + typecheck + test + build
- Add `instrumentation.ts` with Pino and OpenTelemetry (or Vercel Analytics on Vercel)
- Add `/api/health` route handler
- Add security headers in `next.config.js` (use a `headers()` function, not a middleware, so they're applied to every response)
- Set `output: 'standalone'` if you'll Dockerize
- Add a Playwright test that runs **axe-core** on the homepage and the protected dashboard
- Document the rollback steps in the project README

**Self-check:**
- [ ] I can find a request in production logs by `traceId`.
- [ ] I can roll back to the previous deploy in under 2 minutes.
- [ ] I can name the SLO for the app and the alert that fires when it's breached.
- [ ] I can run an a11y check and explain what its findings mean.

---

## Recommended Courses

Pick **one primary** source and treat the rest as references.

| Level | Course | Why | Cost |
|---|---|---|---|
| **Primary — React** | [react.dev/learn](https://react.dev/learn) — official React docs (Quick Start, Thinking in React, Managing State) | Official, current, project-based | Free |
| **Primary — Next.js** | [Next.js Learn course](https://nextjs.org/learn) — official Vercel tutorial | Builds a dashboard with login + CRUD, closest to what we ship | Free |
| Deep dive — Next.js | *Next.js & React — The Complete Guide* — Academind (Udemy) | Long-form, covers edge cases, good for first project | Paid |
| Server Components | *React Server Components Deep Dive* — Dan Abramov talks on YouTube | Mental model for Phase 4 | Free |
| TypeScript | *Total TypeScript* — Matt Pocock | Best-in-class for the kind of typing we do | Paid |
| Auth | [Auth.js (NextAuth) Crash Course](https://authjs.dev/) | Only needed if a project is not Laravel-backed | Free |

> **CoE rule:** Course work is a starting point. Real learning happens in the **weekly deliverable** and in code review on a real codebase.

---

## Channels, Podcasts & Newsletters

Curated, low-noise, high-signal. Subscribe to 2–3 — more than that and you'll stop reading them.

**YouTube channels**
- [Vercel](https://www.youtube.com/@VercelHQ) — official framework updates, deep dives
- [Lee Robinson](https://www.youtube.com/@leerob) — Vercel VP, practical Next.js patterns
- [Theo – t3.gg](https://www.youtube.com/@t3dotgg) — opinionated, fast-moving, useful counterpoints
- [Web Dev Simplified](https://www.youtube.com/@WebDevSimplified) — fundamentals refresher
- [Jack Herrington](https://www.youtube.com/@jherr) — React, RSC, advanced patterns

**Podcasts**
- *Syntax.fm* — weekly, broad web dev with regular Next.js episodes
- *JS Party* — panel format, good for "what's the consensus on X"
- *React Round Up* — narrower, React-heavy
- *Changelog* — open-source & infra, useful for the deploy/operate track

**Newsletters**
- [Next.js Weekly](https://nextjsweekly.com/) — curated Next.js news
- [Bytes](https://bytes.dev/) — daily, sharp JavaScript news
- [React Status](https://react.statuscode.com/) — React ecosystem
- [TLDR Web Dev](https://tldr.tech/webdev) — broad, 5-minute read

**Blogs to follow**
- [Next.js Blog](https://nextjs.org/blog) — release notes + engineering posts
- [Vercel Blog](https://vercel.com/blog) — RSC, edge, framework internals
- [Dan Abramov's blog](https://overreacted.io/) — long-form React deep dives

---

## Tutorial & Reference Links

Bookmark these; you'll return to them often.

**Official**
- [Next.js Docs (App Router)](https://nextjs.org/docs/app)
- [React Docs (learn)](https://react.dev/learn)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [Zod Docs](https://zod.dev/)
- [React Hook Form Docs](https://react-hook-form.com/)
- [shadcn/ui](https://ui.shadcn.com/)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Playwright Docs](https://playwright.dev/)

**Curated tutorials**
- [Next.js Learn (official tutorial)](https://nextjs.org/learn) — full guided build
- [Patterns.dev](https://www.patterns.dev/) — modern web app patterns (free book)

**Recipes & cookbooks**
- [Next.js Examples repo](https://github.com/vercel/next.js/tree/canary/examples) — 200+ official examples
- [Vercel templates](https://vercel.com/templates) — production-ready starters

---

## Certifications

There is **no first-party Next.js certification** from Vercel. Adjacent certifications that hold weight:

| Certification | Issuer | Why it matters | Cost |
|---|---|---|---|
| **Meta Front-End Developer Professional Certificate** | Coursera / Meta | Covers React fundamentals; useful if Phase 2 feels shaky | Paid |
| **Meta Back-End Developer Professional Certificate** | Coursera / Meta | Useful for the API side and the Laravel integration track | Paid |
| **AWS Certified Developer – Associate** | AWS | Matters once we self-host on AWS | Paid |
| **Vercel Solutions Architect** (where available) | Vercel | First-party, directly relevant | Paid |

> **CoE stance:** Certifications are a **floor**, not a ceiling. A working weekly deliverable + code review history on `dev` is worth more than any certificate. Use certs to round out gaps, not to substitute for building.

---

## Books (Optional Deep Dives)

For engineers who want depth beyond the docs.

- *Learning React* — Alex Banks & Eve Porcello (O'Reilly) — solid React fundamentals
- *Designing Web APIs* — Brenda Jin, Saurabh Sahni, Amir Shevat (O'Reilly) — for the API side
- *Web Performance in Action* — Jeremy Wagner — for the Lighthouse / Core Web Vitals work
- *Building Secure & Reliable Systems* — Google — for the production track (free online)
- *Refactoring* — Martin Fowler — for shaping our component library over time

---

## How to Use This Path

1. **Start on Monday.** Pick a phase. Work in pairs where the phase has a `*` in the 8-week plan.
2. **Deliver on Friday.** The weekly deliverable is what gets reviewed. It can be small.
3. **Open a PR for every deliverable.** Even tiny ones. The habit is the point.
4. **Use AI carefully.** Per [CoE AI guidelines](../../general/ai-era-coding-guidelines.md), AI can *explain concepts*, *scaffold tests* (Phase 9 especially), and *review* code — but **auth and DB migration code is Red Zone, manual only.** Tag AI-assisted commits `[ai-assisted: <tool>]`.
5. **Track progress.** Use a shared Notion/Kanban or a simple spreadsheet: one row per developer, one column per phase, check off self-checks as you go. Review in the team meeting each Friday.
6. **Update this doc.** Broken link? Better course? Found a gap? PR it. This is a living document.
7. **Cross-link with our existing standards:**
   - Code review: [nodejs-typescript-code-review-checklist.md](../../nodejs/nodejs-typescript-code-review-checklist.md)
   - API design: [rest-api-best-practices.md](../../general/rest-api-best-practices.md)
   - AI policy: [ai-era-coding-guidelines.md](../../general/ai-era-coding-guidelines.md)
   - Git workflow: [git/Techversant_Git_Workflow.md](../../git/Techversant_Git_Workflow.md)
8. **Starter template.** When the path is running, the first team to finish Phase 8 should publish a minimal **Laravel + Next.js + shadcn** starter repo and link it from this document. Until then, scaffold from `create-next-app`.

---

## Document Control

| Field | Value |
|---|---|
| Document | Next.js Learning Path — For the Web Dev Team |
| Version | 0.3 (review-pass: Phases 4/5/7/8/9/10 expanded) |
| Owner | CoE Web Working Group |
| Review Cycle | Quarterly |
| Status | Draft — first PR open |
| Supersedes | v0.2 |
| Related | [Node.js TypeScript Best Practices](../../nodejs/nodejs-typescript-best-practices.md), [REST API Best Practices](../../general/rest-api-best-practices.md), [AI Era Coding Guidelines](../../general/ai-era-coding-guidelines.md) |

---

**Maintained by:** Techversant CoE
**Last Updated:** June 2026
