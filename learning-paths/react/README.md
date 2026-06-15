# React Learning Path — Folder Index

This folder contains the team's React learning resources. Start with the path document, use the roadmap image as a visual reference, and use the gap analysis below to see where this path sits in the wider React ecosystem.

---

## 📂 What's in this folder

| File | Purpose | Read this when… |
|---|---|---|
| [**intermediate.md**](./intermediate.md) | The official team learning path — 8 phases over 6 weeks | You're starting the React track, planning the pilot, or running a code review against the rubric |
| [**roadmap.png**](./roadmap.png) | The community [React Developer Roadmap by adam-golab](https://github.com/adam-golab/react-developer-roadmap) (1542×2949) | You want a visual map of the wider React ecosystem and how our path fits into it |
| [**README.md**](./README.md) | This file — folder index, gap analysis, and "how this path relates to the rest of the CoE" | You're a tech lead, a new hire, or onboarding a new team to the path |

---

## 🚀 Where to start

1. **New to React on the team?** Open [intermediate.md](./intermediate.md) and read the **Architecture call** at the top — it sets the "React as a UI library for our Laravel API" frame for everything that follows.
2. **Planning a pilot batch?** Read the **Suggested 6-Week Plan** and the **Weekly PR Assessment Rubric** — those are the two operational artefacts the pilot will run on.
3. **Want the visual context?** Open [roadmap.png](./roadmap.png) for the full ecosystem map. The **gap analysis** below tells you which boxes in that map our path covers, which it skips, and why.
4. **Coming from the Next.js path?** Read [intermediate.md](./intermediate.md) — the React path is the **prerequisite foundation** for the [Next.js Learning Path](../nextjs/intermediate.md).

---

## 🗺 The roadmap at a glance

The image in this folder is the standard **React Developer Roadmap** (community-maintained, originally 2019, kept current by the author). It maps the full React ecosystem into 19 branches:

> Basics → General Dev Skills → Core React → Build Tools → Styling → State Management → Type Checkers → Form Helpers → Routing → API Clients → Utility Libraries → Testing → Internationalization → Server-Side Rendering → Static Site Generators → Backend Integration → Mobile → Desktop → Virtual Reality

It's a useful **completeness check**, not a curriculum. We deliberately don't cover every branch — see the gap analysis below.

---

## ✅ Gap analysis: our path vs. the full React ecosystem

This is the table a reviewer or tech lead walks through when deciding **what to add, what to skip, and what to defer to a sibling path**.

Legend: ✅ covered · ⚠️ partial · ❌ not covered (with reason)

| Roadmap branch | Status | Where / Why |
|---|---|---|
| **HTML / CSS basics** | ✅ | [intermediate.md — Prerequisites](./intermediate.md#prerequisites-complete-before-week-1) — minimum bar is semantic HTML, Flexbox, Grid, responsive design |
| **JS Basics (ES6+)** | ✅ | [Phase 1](./intermediate.md#phase-1--javascript--typescript-refresh) — modules, async/await, destructuring, optional chaining, nullish coalescing |
| **General Dev Skills** (Git, HTTP, terminal, algorithms, design patterns) | ⚠️ partial | Git + HTTP in prerequisites; terminal/algorithms/design patterns **deliberately omitted** — out of scope for a learning path |
| **Core React** (JSX, components, hooks, context) | ✅ | [Phases 2–6](./intermediate.md#phase-2--react-core-jsx-components-and-props) — strongest section |
| **Build Tools** (npm, pnpm, Vite, Webpack) | ✅ | [Phase 1](./intermediate.md#phase-1--javascript--typescript-refresh) (pnpm) + [Phase 8](./intermediate.md#phase-8--production-patterns-and-project-structure) (Vite build) — we standardize on **Vite** for new projects |
| **Task Runners** (gulp, npm scripts) | ❌ | npm scripts only — gulp is legacy. Not in scope. |
| **Styling** (Tailwind, CSS Modules, CSS-in-JS) | ⚠️ partial | Tailwind/shadcn-ui is the call in the **[Next.js path Phase 8](../nextjs/intermediate.md#phase-8--ui-system-and-frontend-architecture)**. The React path defers styling to that — acceptable because most of our React work today is inside a Next.js or Laravel-Inertia shell. **GAP to add: a one-liner in Phase 8 naming Tailwind as the default.** |
| **State Management** (Context, useReducer, Redux, MobX, Zustand) | ⚠️ partial | Context + useReducer in [Phase 6](./intermediate.md#phase-6--composition-patterns-and-custom-hooks). **GAP to add: a "When to reach for Redux Toolkit or Zustand" rule** — both are still used in production code we inherit. |
| **Type Checkers** (PropTypes, TypeScript, Flow) | ✅ | TypeScript in prerequisites + [Phase 1](./intermediate.md#phase-1--javascript--typescript-refresh) — Flow is dead, PropTypes is legacy |
| **Form Helpers** (RHF, Formik, Final Form, Redux Form) | ✅ | [Phase 5](./intermediate.md#phase-5--forms-validation-and-api-integration) — RHF + Zod is the modern default |
| **Routing** (React Router, Reach Router, etc.) | ❌ | **GAP.** Even a small Vite-React SPA usually needs React Router. Add a Phase-3-or-newer mini-section: "If you're building a pure-React app (not Next.js), use React Router v6+ for routing." |
| **API Clients** (fetch, axios, TanStack Query) | ✅ | [Phase 4](./intermediate.md#phase-4--effects-refs-and-the-component-lifecycle) (fetch) + [Phase 5](./intermediate.md#phase-5--forms-validation-and-api-integration) (TanStack Query teaser) |
| **GraphQL** (Apollo, Relay, urql) | ❌ | **Deliberately omitted** — we standardize on **REST + Laravel** per the [REST API Best Practices](../../general/rest-api-best-practices.md) CoE standard. Revisit only if a product requires it. |
| **Utility Libraries** (Lodash, date-fns, clsx, RxJS) | ⚠️ partial | Implicit (clsx is the shadcn convention). **GAP to add: a one-liner in Phase 8** — "We prefer `clsx` for class composition, `date-fns` for dates, native `fetch` over axios." |
| **Testing** (Jest, Vitest, RTL, MSW, Cypress, Playwright) | ✅ | [Phase 7](./intermediate.md#phase-7--testing-react-components) — Vitest + RTL + MSW + Playwright is the modern stack |
| **Internationalization** (React Intl, i18next) | ❌ | **GAP.** Several of our Laravel-backed products ship with multiple locales. Add a one-line pointer: "If the product supports multiple languages, see the [CoE i18n policy](#) (TODO: link when it exists)." |
| **Server-Side Rendering** (Next.js, After.js) | ✅ | Explicit cross-link to the [Next.js Learning Path](../nextjs/intermediate.md) — best possible handling: it's a sibling path, not duplicated |
| **Static Site Generators** (Gatsby, Astro) | ❌ | Out of scope for a Laravel-frontend team. Astro is worth watching; revisit if marketing sites become a recurring need. |
| **Backend Integration** (Laravel API, Rails, etc.) | ✅ | **The whole path is built on this assumption.** Architecture call at the top of [intermediate.md](./intermediate.md) sets the rule. |
| **Mobile** (React Native, Cordova) | ❌ | Out of scope today. **Future sibling path candidate.** |
| **Desktop** (Electron, Tauri) | ❌ | Out of scope. |
| **Virtual Reality** (React 360) | ❌ | **Dead project** — ignore. |
| **Web Security** (XSS, CSRF, CSP) | ❌ | **GAP.** Our React path doesn't mention security. The Next.js path covers CSRF/Sanctum in Phase 7, but pure-React against Laravel needs a pointer too. Add a "When you read user input → render it, use `textContent` not `innerHTML`" rule and a Sanctum/CSRF cross-link. |
| **PWA / Service Workers** | ❌ | **GAP to add: a one-liner** — "PWAs are out of scope for this path. If a product needs offline or install-to-homescreen, see the CoE PWA guide (TODO)." |
| **Performance / Web Vitals** | ⚠️ partial | [Phase 8](./intermediate.md#phase-8--production-patterns-and-project-structure) covers Profiler + bundle visualizer. **GAP to add: name the three Core Web Vitals (LCP, INP, CLS) explicitly** so developers can recognize them in Lighthouse. |
| **Accessibility** | ✅ | [Phase 8](./intermediate.md#phase-8--production-patterns-and-project-structure) + the rubric's a11y row |
| **Design systems / tokens** | ⚠️ partial | The folder structure in Phase 8 implies it. **GAP to add: a sentence on design tokens (colors, spacing, type scale)** — don't hardcode hex values. |
| **Build & deploy** (CI/CD, env, Docker, hosting) | ❌ | Deferred to the Next.js path. **Acceptable for Vite-React** because it's mostly `vite build` + static host (Vercel, Netlify, S3+CloudFront). Could add a one-liner: "For pure-React SPAs, `vite build` outputs to `dist/`. Deploy to Vercel/Netlify/S3+CloudFront." |

---

## 🔧 What we deliberately skipped (and why)

These roadmap items show up in the full React Developer Roadmap but are **out of scope for our team** in 2026. Listing them so a reviewer can challenge the decision:

- **jQuery, Moment.js, lodash (for new code)** — superseded by native JS / `date-fns` / `clsx`
- **Flow** — Meta has wound it down; TypeScript won
- **MobX, Redux (vanilla)** — Zustand and Redux Toolkit are the modern replacements; we teach Context + useReducer first
- **Enzyme** — React Testing Library replaced it
- **Cypress** for E2E — Playwright is our standard per the Next.js path
- **GraphQL / Apollo / Relay** — we standardize on REST per the CoE API standard
- **React 360, Proton Native, Cordova** — dead or dying
- **Webpack, Rollup, Parcel (for app code)** — Vite is the new default; we don't need to teach the alternatives
- **Class components** — React 19, 100% hooks
- **PropTypes** — TypeScript is the type system
- **CSS-in-JS (styled-components, Emotion)** — Tailwind is our standard
- **Gatsby** — Next.js is the SSR/SSG default; we don't need a second framework

---

## 🔗 Related paths in this repo

| Path | Audience | Length | Status |
|---|---|---|---|
| [**React** (this folder)](./intermediate.md) | Backend engineers new to React | 6 weeks, 8 phases | v0.2 pilot |
| [Next.js](../nextjs/intermediate.md) | Engineers who finished this path | 8 weeks, 10 phases | v0.5 pilot |

**Order of study:** React first → Next.js second. The Next.js path assumes the React fundamentals in this document.

---

## 🤖 AI delegation guidance (CoE standard)

When working through the React path with AI assistance:

- 🟢 **FULL DELEGATE:** scaffolding Vitest tests, generating Zod schemas from examples, formatting code, explaining a concept in your own words
- 🟡 **COLLABORATE:** writing components, designing the file structure, choosing between `useState` and `useReducer`
- 🟠 **HUMAN-LED:** designing the component API, picking the state-management pattern, code review
- 🔴 **NEVER DELEGATE:** auth code, session handling, anything touching tokens, production database work

For the full model, see [general/ai-era-coding-guidelines.md](../../general/ai-era-coding-guidelines.md).

---

## 📊 Document control

| Field | Value |
|---|---|
| Document | React Learning Path — Folder Index & Roadmap |
| Version | 0.1 |
| Owner | CoE Web Working Group |
| Review Cycle | Quarterly |
| Status | Draft — pilot batch |
| Related | [intermediate.md](./intermediate.md), [roadmap.png](./roadmap.png), [Next.js Learning Path](../nextjs/intermediate.md) |

---

**Maintained by:** Techversant CoE
**Last Updated:** June 2026
