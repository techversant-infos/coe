# React Roadmap â€” Gap Analysis (Internal Review Document)

> **Audience:** CoE Web Working Group, tech leads, and reviewers â€” not a reader-facing document.
> **Purpose:** Show how the [React Learning Path](./intermediate.md) maps to the full React ecosystem defined by the community [React Developer Roadmap](https://github.com/adam-golab/react-developer-roadmap) (see [roadmap.png](./roadmap.png)). Used during pilot review to challenge scope decisions, not during onboarding.

---

## How to read this document

- **âœ… covered** â€” the path explicitly teaches this and assesses it
- **âš ï¸ partial** â€” the path touches this but doesn't go deep; a sibling document or a future phase covers the rest
- **âŒ not covered (with reason)** â€” the path deliberately skips this; the reason is given so a reviewer can challenge the call

A reviewer should walk this table top-to-bottom in roughly 10 minutes, then ask: *for any âš ï¸ row, is the depth enough for our pilot batch?* and *for any âŒ row, is the reason still valid in 2026?*

---

## Gap analysis: our path vs. the full React ecosystem

| Roadmap branch | Status | Where / Why |
|---|---|---|
| **HTML / CSS basics** | âœ… | [intermediate.md â€” Prerequisites](./intermediate.md#prerequisites-complete-before-week-1) â€” minimum bar is semantic HTML, Flexbox, Grid, responsive design |
| **JS Basics (ES6+)** | âœ… | [Phase 1](./intermediate.md#phase-1--javascript--typescript-refresh) â€” modules, async/await, destructuring, optional chaining, nullish coalescing |
| **General Dev Skills** (Git, HTTP, terminal, algorithms, design patterns) | âš ï¸ partial | Git + HTTP in prerequisites; terminal/algorithms/design patterns **deliberately omitted** â€” out of scope for a learning path |
| **Core React** (JSX, components, hooks, context) | âœ… | [Phase 2](./intermediate.md#phase-2--react-core-jsx-components-and-props) (JSX/Components), [Phase 3](./intermediate.md#phase-3--state-events-and-conditional-rendering) (State/Events), [Phase 4](./intermediate.md#phase-4--effects-refs-and-the-component-lifecycle) (Effects/Refs) â€” the strongest section of the path |
| **Build Tools** (npm, pnpm, Vite, Webpack) | âœ… | [Phase 1](./intermediate.md#phase-1--javascript--typescript-refresh) (pnpm) + [Phase 8](./intermediate.md#phase-8--production-patterns-and-project-structure) (Vite build) â€” we standardize on **Vite** for new projects |
| **Task Runners** (gulp, npm scripts) | âŒ | npm scripts only â€” gulp is legacy. Not in scope. |
| **Styling** (Tailwind, CSS Modules, CSS-in-JS) | âœ… | Tailwind + shadcn/ui in [Phase 8](./intermediate.md#phase-8--production-patterns-and-project-structure); CSS Modules allowed only if a project already uses them |
| **State Management** (Context, useReducer, Redux, MobX, Zustand) | âœ… | Context + useReducer in [Phase 6](./intermediate.md#phase-6--composition-patterns-and-custom-hooks); "when to reach for RKT or Zustand" rule in [Phase 8](./intermediate.md#phase-8--production-patterns-and-project-structure) |
| **Type Checkers** (PropTypes, TypeScript, Flow) | âœ… | TypeScript in prerequisites + [Phase 1](./intermediate.md#phase-1--javascript--typescript-refresh) â€” Flow is dead, PropTypes is legacy |
| **Form Helpers** (RHF, Formik, Final Form, Redux Form) | âœ… | [Phase 5](./intermediate.md#phase-5--forms-validation-and-api-integration) â€” RHF + Zod is the modern default |
| **Routing** (React Router, Reach Router, etc.) | âœ… | [Phase 8](./intermediate.md#phase-8--production-patterns-and-project-structure) â€” React Router v6+ for pure-React SPAs; explicit "skip if Next.js" rule |
| **API Clients** (fetch, axios, TanStack Query) | âœ… | [Phase 4](./intermediate.md#phase-4--effects-refs-and-the-component-lifecycle) (fetch) + [Phase 5](./intermediate.md#phase-5--forms-validation-and-api-integration) (TanStack Query teaser) |
| **GraphQL** (Apollo, Relay, urql) | âŒ | **Deliberately omitted** â€” we standardize on **REST + Laravel** per the [REST API Best Practices](../../../../general/rest-api-best-practices.md) CoE standard. Revisit only if a product requires it. |
| **Utility Libraries** (Lodash, date-fns, clsx, RxJS) | âœ… | [Phase 8](./intermediate.md#phase-8--production-patterns-and-project-structure) â€” team defaults: `clsx`, `date-fns`, native `fetch` |
| **Testing** (Jest, Vitest, RTL, MSW, Cypress, Playwright) | âœ… | [Phase 7](./intermediate.md#phase-7--testing-react-components) â€” Vitest + RTL + MSW + Playwright is the modern stack |
| **Internationalization** (React Intl, i18next) | âš ï¸ partial | [Phase 8](./intermediate.md#phase-8--production-patterns-and-project-structure) â€” explicit "out of scope, see CoE i18n policy" pointer. i18n policy itself is a TODO. |
| **Server-Side Rendering** (Next.js, After.js) | âœ… | Explicit cross-link to the [Next.js Learning Path](../nextjs/intermediate.md) â€” best possible handling: it's a sibling path, not duplicated |
| **Static Site Generators** (Gatsby, Astro) | âŒ | Out of scope for a Laravel-frontend team. Astro is worth watching; revisit if marketing sites become a recurring need. |
| **Backend Integration** (Laravel API, Rails, etc.) | âœ… | **The whole path is built on this assumption.** Architecture call at the top of [intermediate.md](./intermediate.md) sets the rule. |
| **Mobile** (React Native, Cordova) | âŒ | Out of scope today. **Future sibling path candidate.** |
| **Desktop** (Electron, Tauri) | âŒ | Out of scope. |
| **Virtual Reality** (React 360) | âŒ | **Dead project** â€” ignore. |
| **Web Security** (XSS, CSRF, CSP) | âœ… | [Phase 8](./intermediate.md#phase-8--production-patterns-and-project-structure) â€” `dangerouslySetInnerHTML` rule, Sanctum/CSRF cross-link to Next.js Phase 7, client-Zod rule |
| **PWA / Service Workers** | âš ï¸ partial | [Phase 8](./intermediate.md#phase-8--production-patterns-and-project-structure) â€” explicit "out of scope, see CoE PWA guide" pointer. PWA guide itself is a TODO. |
| **Performance / Web Vitals** | âœ… | [Phase 8](./intermediate.md#phase-8--production-patterns-and-project-structure) â€” Profiler, bundle visualizer, and Core Web Vitals (LCP, INP, CLS) named with target thresholds |
| **Accessibility** | âœ… | [Phase 8](./intermediate.md#phase-8--production-patterns-and-project-structure) + the rubric's a11y row |
| **Design systems / tokens** | âœ… | [Phase 8](./intermediate.md#phase-8--production-patterns-and-project-structure) â€” design tokens via Tailwind theme extension or CSS custom properties |
| **Build & deploy** (CI/CD, env, Docker, hosting) | âŒ | Deferred to the Next.js path. Acceptable for Vite-React because it's mostly `vite build` + static host. |

---

## What we deliberately skipped (and why)

These roadmap items show up in the full React Developer Roadmap but are **out of scope for our team** in 2026. Listing them so a reviewer can challenge the decision:

- **jQuery, Moment.js, lodash (for new code)** â€” superseded by native JS / `date-fns` / `clsx`
- **Flow** â€” Meta has wound it down; TypeScript won
- **MobX, Redux (vanilla)** â€” Zustand and Redux Toolkit are the modern replacements; we teach Context + useReducer first
- **Enzyme** â€” React Testing Library replaced it
- **Cypress** for E2E â€” Playwright is our standard per the Next.js path
- **GraphQL / Apollo / Relay** â€” we standardize on REST per the CoE API standard
- **React 360, Proton Native, Cordova** â€” dead or dying
- **Webpack, Rollup, Parcel (for app code)** â€” Vite is the new default; we don't need to teach the alternatives
- **Class components** â€” React 19, 100% hooks
- **PropTypes** â€” TypeScript is the type system
- **CSS-in-JS (styled-components, Emotion)** â€” Tailwind is our standard
- **Gatsby** â€” Next.js is the SSR/SSG default; we don't need a second framework

---

## Reviewer questions

When reviewing this gap analysis, ask:

1. For every **âš ï¸ partial** row: *is the depth enough for our pilot batch, or does it block Week-1 delivery?*
2. For every **âŒ not covered** row: *is the reason still valid in 2026?* Especially:
   - GraphQL â€” has a new product appeared that needs it?
   - i18n â€” has a new product appeared that ships with multiple locales?
   - PWAs â€” has a new product appeared that needs offline / install-to-homescreen?
3. For every **âœ… covered** row: *is the depth right, or are we teaching too much / too little?*

---

## Document control

| Field | Value |
|---|---|
| Document | React Roadmap â€” Gap Analysis |
| Version | 0.1 (extracted from React folder README, made reviewer-only) |
| Owner | CoE Web Working Group |
| Review Cycle | Quarterly |
| Status | Internal review document |
| Related | [intermediate.md](./intermediate.md), [roadmap.png](./roadmap.png), [Next.js Learning Path](../nextjs/intermediate.md) |
