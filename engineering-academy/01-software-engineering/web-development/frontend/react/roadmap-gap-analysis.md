# React Roadmap Gap Analysis (Internal Review Document)

> **Audience:** CoE Web Working Group, tech leads, and reviewers not a reader-facing document.
> **Purpose:** Show how the [React Learning Path](./intermediate.md) maps to the full React ecosystem defined by the community [React Developer Roadmap](https://github.com/adam-golab/react-developer-roadmap) (see [roadmap.png](./roadmap.png)). Used during pilot review to challenge scope decisions, not during onboarding.

---

## How to read this document

- ** covered** the path explicitly teaches this and assesses it
- ** partial** the path touches this but doesn't go deep; a sibling document or a future phase covers the rest
- ** not covered (with reason)** the path deliberately skips this; the reason is given so a reviewer can challenge the call

A reviewer should walk this table top-to-bottom in roughly 10 minutes, then ask: *for any row, is the depth enough for our pilot batch?* and *for any row, is the reason still valid in 2026?*

---

## Gap analysis: our path vs. the full React ecosystem

| Roadmap branch | Status | Where / Why |
|---|---|---|
| **HTML / CSS basics** | | [intermediate.md Prerequisites](./intermediate.md#prerequisites-complete-before-week-1) minimum bar is semantic HTML, Flexbox, Grid, responsive design |
| **JS Basics (ES6+)** | | [Phase 1](./intermediate.md#phase-1-javascript-typescript-refresh) modules, async/await, destructuring, optional chaining, nullish coalescing |
| **General Dev Skills** (Git, HTTP, terminal, algorithms, design patterns) | partial | Git + HTTP in prerequisites; terminal/algorithms/design patterns **deliberately omitted** out of scope for a learning path |
| **Core React** (JSX, components, hooks, context) | | [Phase 2](./intermediate.md#phase-2-react-core-jsx-components-and-props) (JSX/Components), [Phase 3](./intermediate.md#phase-3-state-events-and-conditional-rendering) (State/Events), [Phase 4](./intermediate.md#phase-4-effects-refs-and-the-component-lifecycle) (Effects/Refs) the strongest section of the path |
| **Build Tools** (npm, pnpm, Vite, Webpack) | | [Phase 1](./intermediate.md#phase-1-javascript-typescript-refresh) (pnpm) + [Phase 8](./intermediate.md#phase-8-production-patterns-and-project-structure) (Vite build) we standardize on **Vite** for new projects |
| **Task Runners** (gulp, npm scripts) | | npm scripts only gulp is legacy. Not in scope. |
| **Styling** (Tailwind, CSS Modules, CSS-in-JS) | | Tailwind + shadcn/ui in [Phase 8](./intermediate.md#phase-8-production-patterns-and-project-structure); CSS Modules allowed only if a project already uses them |
| **State Management** (Context, useReducer, Redux, MobX, Zustand) | | Context + useReducer in [Phase 6](./intermediate.md#phase-6-composition-patterns-and-custom-hooks); "when to reach for RKT or Zustand" rule in [Phase 8](./intermediate.md#phase-8-production-patterns-and-project-structure) |
| **Type Checkers** (PropTypes, TypeScript, Flow) | | TypeScript in prerequisites + [Phase 1](./intermediate.md#phase-1-javascript-typescript-refresh) Flow is dead, PropTypes is legacy |
| **Form Helpers** (RHF, Formik, Final Form, Redux Form) | | [Phase 5](./intermediate.md#phase-5-forms-validation-and-api-integration) RHF + Zod is the modern default |
| **Routing** (React Router, Reach Router, etc.) | | [Phase 8](./intermediate.md#phase-8-production-patterns-and-project-structure) React Router v6+ for pure-React SPAs; explicit "skip if Next.js" rule |
| **API Clients** (fetch, axios, TanStack Query) | | [Phase 4](./intermediate.md#phase-4-effects-refs-and-the-component-lifecycle) (fetch) + [Phase 5](./intermediate.md#phase-5-forms-validation-and-api-integration) (TanStack Query teaser) |
| **GraphQL** (Apollo, Relay, urql) | | **Deliberately omitted** we standardize on **REST + Laravel** per the [REST API Best Practices](../../../../../general/rest-api-best-practices.md) CoE standard. Revisit only if a product requires it. |
| **Utility Libraries** (Lodash, date-fns, clsx, RxJS) | | [Phase 8](./intermediate.md#phase-8-production-patterns-and-project-structure) team defaults: `clsx`, `date-fns`, native `fetch` |
| **Testing** (Jest, Vitest, RTL, MSW, Cypress, Playwright) | | [Phase 7](./intermediate.md#phase-7-testing-react-components) Vitest + RTL + MSW + Playwright is the modern stack |
| **Internationalization** (React Intl, i18next) | partial | [Phase 8](./intermediate.md#phase-8-production-patterns-and-project-structure) explicit "out of scope, see CoE i18n policy" pointer. i18n policy itself is a TODO. |
| **Server-Side Rendering** (Next.js, After.js) | | Explicit cross-link to the [Next.js Learning Path](../nextjs/intermediate.md) best possible handling: it's a sibling path, not duplicated |
| **Static Site Generators** (Gatsby, Astro) | | Out of scope for a Laravel-frontend team. Astro is worth watching; revisit if marketing sites become a recurring need. |
| **Backend Integration** (Laravel API, Rails, etc.) | | **The whole path is built on this assumption.** Architecture call at the top of [intermediate.md](./intermediate.md) sets the rule. |
| **Mobile** (React Native, Cordova) | | Out of scope today. **Future sibling path candidate.** |
| **Desktop** (Electron, Tauri) | | Out of scope. |
| **Virtual Reality** (React 360) | | **Dead project** ignore. |
| **Web Security** (XSS, CSRF, CSP) | | [Phase 8](./intermediate.md#phase-8-production-patterns-and-project-structure) `dangerouslySetInnerHTML` rule, Sanctum/CSRF cross-link to Next.js Phase 7, client-Zod rule |
| **PWA / Service Workers** | partial | [Phase 8](./intermediate.md#phase-8-production-patterns-and-project-structure) explicit "out of scope, see CoE PWA guide" pointer. PWA guide itself is a TODO. |
| **Performance / Web Vitals** | | [Phase 8](./intermediate.md#phase-8-production-patterns-and-project-structure) Profiler, bundle visualizer, and Core Web Vitals (LCP, INP, CLS) named with target thresholds |
| **Accessibility** | | [Phase 8](./intermediate.md#phase-8-production-patterns-and-project-structure) + the rubric's a11y row |
| **Design systems / tokens** | | [Phase 8](./intermediate.md#phase-8-production-patterns-and-project-structure) design tokens via Tailwind theme extension or CSS custom properties |
| **Build & deploy** (CI/CD, env, Docker, hosting) | | Deferred to the Next.js path. Acceptable for Vite-React because it's mostly `vite build` + static host. |

---

## What we deliberately skipped (and why)

These roadmap items show up in the full React Developer Roadmap but are **out of scope for our team** in 2026. Listing them so a reviewer can challenge the decision:

- **jQuery, Moment.js, lodash (for new code)** superseded by native JS / `date-fns` / `clsx`
- **Flow** Meta has wound it down; TypeScript won
- **MobX, Redux (vanilla)** Zustand and Redux Toolkit are the modern replacements; we teach Context + useReducer first
- **Enzyme** React Testing Library replaced it
- **Cypress** for E2E Playwright is our standard per the Next.js path
- **GraphQL / Apollo / Relay** we standardize on REST per the CoE API standard
- **React 360, Proton Native, Cordova** dead or dying
- **Webpack, Rollup, Parcel (for app code)** Vite is the new default; we don't need to teach the alternatives
- **Class components** React 19, 100% hooks
- **PropTypes** TypeScript is the type system
- **CSS-in-JS (styled-components, Emotion)** Tailwind is our standard
- **Gatsby** Next.js is the SSR/SSG default; we don't need a second framework

---

## Reviewer questions

When reviewing this gap analysis, ask:

1. For every ** partial** row: *is the depth enough for our pilot batch, or does it block Week-1 delivery?*
2. For every ** not covered** row: *is the reason still valid in 2026?* Especially:
 - GraphQL has a new product appeared that needs it?
 - i18n has a new product appeared that ships with multiple locales?
 - PWAs has a new product appeared that needs offline / install-to-homescreen?
3. For every ** covered** row: *is the depth right, or are we teaching too much / too little?*

---

## Document control

| Field | Value |
|---|---|
| Document | React Roadmap Gap Analysis |
| Version | 0.1 (extracted from React folder README, made reviewer-only) |
| Owner | CoE Web Working Group |
| Review Cycle | Quarterly |
| Status | Internal review document |
| Related | [intermediate.md](./intermediate.md), [roadmap.png](./roadmap.png), [Next.js Learning Path](../nextjs/intermediate.md) |
