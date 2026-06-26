**Version:** 0.3 (draft)
**Issued by:** Techversant Center of Excellence (CoE)
**Effective Date:** June 2026
**Audience:** Web Dev Team â€” backend/PHP/Laravel-leaning engineers who need to build production React frontends
**Length:** 8 phases over 6 weeks (~5 hours/week, pair-friendly)
**Status:** Draft for Pilot Batch
**Prerequisite for:** [Next.js Learning Path](../nextjs/intermediate.md) â€” finish this first
**Contributors:** Compiled by CoE Web Working Group, reviewed by Web team leads

# React Learning Path â€” For the Web Dev Team
*From PHP/Laravel backend to confident React frontend engineer.*

This is the **foundation track**. If your team's goal is Next.js (see [../nextjs/intermediate.md](../nextjs/intermediate.md)), this path comes first. It covers React 19.x, JSX, components, state, effects, custom hooks, forms, API integration, testing, and production patterns â€” all written for backend engineers who read JavaScript but haven't built a frontend professionally.

> **Architecture call (read first):** React is a **UI library**, not a full framework. You will use it as the view layer for our Laravel API. This path assumes you will **not** do full-stack React with direct DB access â€” that's a Next.js (or Laravel Inertia) concern.

---

## ðŸŽ¯ Learning Outcomes

By the end of this 6-week plan, every developer on the team should be able to:

1. Read and write JSX confidently â€” components, props, state, conditional rendering, lists.
2. Use hooks (`useState`, `useEffect`, `useContext`, `useReducer`) correctly and explain when each one runs.
3. Write custom hooks that encapsulate reusable logic.
4. Build a form with controlled inputs, client-side validation, and proper error display.
5. Fetch data from a Laravel API, handle loading/error states, and render it in a list.
6. Apply component composition patterns: lifting state, render props, compound components.
7. Test components with React Testing Library, mock API calls with MSW.
8. Ship a feature that passes a code review against our [Node.js TypeScript Code Review Checklist](../../../../nodejs/nodejs-typescript-code-review-checklist.md).

> **Realistic scope:** ~30 hours is enough to build a working React frontend and contribute to supervised tickets. The confidence that comes from building things on the job â€” in code review, on real tickets, pair programming â€” is the rest of the journey.

### Team-Level Metrics of Success

Beyond individual outcomes, we measure whether the path moved the team's velocity:

- **% of frontend tickets completed without senior blocking** â€” track per quarter, target a meaningful rise from baseline
- **PR review turnaround** on frontend PRs â€” should drop as pattern-recognition grows
- **Defect rate** on the first 30 days after a feature merges â€” should stay flat or fall
- **Onboarding time** for a new hire to ship their first React PR â€” target: 2 weeks

Re-baseline these at the end of the path. If they're not moving, the path needs a revision, not a louder announcement.

---

## ðŸ“š Table of Contents
- [Prerequisites (complete before Week 1)](#prerequisites-complete-before-week-1)
- [Suggested 6-Week Plan](#suggested-6-week-plan)
- [Phase 1 â€” JavaScript + TypeScript Refresh](#phase-1--javascript--typescript-refresh)
- [Phase 2 â€” React Core: JSX, Components, and Props](#phase-2--react-core-jsx-components-and-props)
- [Phase 3 â€” State, Events, and Conditional Rendering](#phase-3--state-events-and-conditional-rendering)
- [Phase 4 â€” Effects, Refs, and the Component Lifecycle](#phase-4--effects-refs-and-the-component-lifecycle)
- [Phase 5 â€” Forms, Validation, and API Integration](#phase-5--forms-validation-and-api-integration)
- [Phase 6 â€” Composition Patterns and Custom Hooks](#phase-6--composition-patterns-and-custom-hooks)
- [Phase 7 â€” Testing React Components](#phase-7--testing-react-components)
- [Phase 8 â€” Production Patterns and Project Structure](#phase-8--production-patterns-and-project-structure)
- [Recommended Courses](#recommended-courses)
- [Channels, Podcasts & Newsletters](#channels-podcasts--newsletters)
- [Tutorial & Reference Links](#tutorial--reference-links)
- [Certifications](#certifications)
- [How to Use This Path](#how-to-use-this-path)
- [Document Control](#document-control)

---

## Prerequisites (complete before Week 1)

The path assumes you have these technical basics. If not, spend 1â€“2 days topping up before starting:

| Skill | Minimum bar | Refresher resource |
|---|---|---|
| **JavaScript / ES6+** | `async/await`, modules, destructuring, `map/filter/reduce`, `fetch` API | javascript.info |
| **TypeScript basics** | `interface`, `type`, generics â€” enough to read Zod schemas and type props | [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html) |
| **Git & PR workflow** | Branch, PR, rebase, resolve conflicts | [git/Techversant_Git_Workflow.md](../../../../git/Techversant_Git_Workflow.md) |
| **Node.js & npm/pnpm** | Install, run `npm run dev`, read `.env` | nodejs.dev/learn/getting-started |
| **HTML & CSS** | Semantic HTML, Flexbox, Grid, responsive design | web.dev â€” Learn CSS |
| **API basics** | HTTP methods/status codes, JSON, auth headers/cookies | MDN â€” HTTP overview |

**Bonus but not required:** touched React before, used `useState` or `useEffect`, read a tutorial. The path assumes zero React fluency.

---

## Suggested 6-Week Plan

| Week | Focus | Output / Definition of Done |
|---|---|---|
| 1 | JS/TS refresh + React core | Working component tree: header, product card, product list |
| 2 | State, events, conditional rendering | Product listing with search/filter, loading and empty states |
| 3 | Effects, refs, lifecycle | Product listing wired to a Laravel API, with debounced search |
| 4 | Forms, validation, API integration | Customer add/edit form with React Hook Form + Zod, posts to Laravel |
| 5 | Composition patterns + custom hooks | Refactored feature using custom hooks, render props, compound components |
| 6 | Testing + production patterns | Vitest + RTL tests, MSW mocks, a11y check, production build reviewed |

> **Buffer:** treat Weeks 5â€“6 as flexible. If the team is behind, fold testing into a follow-up sprint. The point is the **6 weekly deliverables**, not hitting 6 weeks exactly.

> **Working agreement:** the deliverable at the end of each week is what gets reviewed on Friday. Pair on the harder phases (3, 4, 5). Open a PR for the deliverable even if it's small â€” it builds the habit.

### Weekly PR Assessment Rubric

Each week's deliverable PR is reviewed on this rubric. Score 0â€“2 per row (0 = missing, 1 = partial, 2 = solid). Aim for 12/14+ before moving on. The goal isn't perfection â€” it's catching the same gap three weeks in a row.

| Dimension | What good looks like |
|---|---|
| **Code correctness** | Feature works end-to-end against the mock or real Laravel API |
| **Type safety** | No `any` unless justified; typed props, state, and responses |
| **Component structure** | Small, single-purpose components; clear prop boundaries |
| **State placement** | State lives at the right level â€” not too high, not too low |
| **Effect hygiene** | `useEffect` has correct dependencies; no infinite loops; cleanup where needed |
| **Error handling** | API errors surfaced to the user; no swallowed exceptions; CoE error envelope used |
| **Accessibility basics** | Semantic HTML, keyboard reachable, labelled form inputs, color contrast not broken |
| **AI-assisted disclosure** | PR description declares what was AI-generated; no AI code in Red Zone areas (auth, payment, prod DB) |

---

## Phase 1 â€” JavaScript + TypeScript Refresh

**Why this phase exists:** the team is comfortable with JavaScript at a basic level, but React and our stack assume fluency with modern syntax and types. One week of refresh prevents a month of small stumbles later.

**Learn:**
- **JavaScript / ES6+**
  - Modules (`import` / `export`)
  - `async` / `await` and Promises
  - Destructuring, spread / rest
  - `map`, `filter`, `reduce`
  - **Optional chaining** (`?.`) and **nullish coalescing** (`??`) â€” used everywhere in React props
  - `fetch` API
  - `npm` and `pnpm`
- **TypeScript basics**
  - Interfaces, types, generics
  - Typing API responses
  - `tsconfig.json` essentials (`strict`, `noImplicitAny`)

**Mini task:**
Build a small script or page that calls a Laravel API with `fetch()`, types the response, and renders a list of items. The point is **typing the wire format**, not building UI.

**Self-check:**
- [ ] I can `await` a `fetch` and narrow the response to a typed shape.
- [ ] I can explain why we never trust the API response to be the shape we asked for.
- [ ] I can run `pnpm dev` on a colleague's project without breaking it.
- [ ] I can read `user?.profile?.name ?? 'Anonymous'` and explain both operators.

---

## Phase 2 â€” React Core: JSX, Components, and Props

**Why this phase exists:** React is the foundation everything else builds on. Get the mental model right â€” components are functions that return UI â€” before adding state and effects.

**Learn:**
- JSX syntax and rules (one root element, camelCase attributes, expressions in `{}`)
- Components as functions: function components, arrow components
- Props: reading, destructuring, default values, type annotations
- **Component composition:** children prop, slots, wrapper patterns
- **Lists and keys:** mapping arrays to elements, why keys matter, what makes a good key
- **Conditional rendering:** ternary, `&&`, early return, null for "hide"

**Source of truth:** the **official React docs at [react.dev/learn](https://react.dev/learn)**. React is currently in the 19.x line â€” always read the current docs, not a 2022 blog post.

**Key mental model:**
> "A component is a function. Props are its arguments. JSX is the return value. That's it."

**Mini task:**
Build a **product card + product list**:
- `<ProductCard />` â€” receives a product object via props, renders name, price, image placeholder, "Add to Cart" button
- `<ProductList />` â€” receives an array of products, maps to `<ProductCard />`
- `<App />` â€” holds the product data, renders `<ProductList />`
- Use TypeScript interfaces for the product shape

**Self-check:**
- [ ] I can explain why JSX looks like HTML but isn't HTML.
- [ ] I can explain what a `key` is for and what makes a good one.
- [ ] I can compose components using `children` instead of prop drilling.

---

## Phase 3 â€” State, Events, and Conditional Rendering

**Why this phase exists:** static UI is useful, but most apps need to respond to the user. This phase introduces state â€” the mechanism React uses to remember things between renders.

**Learn:**
- `useState` â€” the state primitive
- `useReducer` â€” when state logic gets complex (next-action reducer, form reducer)
- **State updates are asynchronous and batched** â€” don't read state immediately after setting it
- **Lifting state up** â€” when siblings need to share state, move it to their nearest common parent
- **Controlled components** â€” form inputs whose value is driven by React state
- Events: `onClick`, `onChange`, `onSubmit`, `onKeyDown`
- **Conditional rendering patterns:** ternary, `&&`, early return, map-to-null for filtered lists
- **`useContext`** â€” the API for shared state without prop drilling (we'll use it properly in Phase 6)

**Mini task:**
Extend the product list from Phase 2 into a **product listing page**:
- **Search** â€” filter products by name as the user types (state: `searchQuery`)
- **Category filter** â€” filter by category (state: `selectedCategory`)
- **"Contact seller" form** â€” controlled inputs for name, email, message (state: form fields)
- **Loading and empty states** â€” conditional rendering based on data availability
- Use a local mock JSON file â€” no API yet

**Self-check:**
- [ ] I can explain the difference between a **controlled** and an **uncontrolled** input.
- [ ] I can lift state up when two siblings need to share it.
- [ ] I can explain why setting state in a loop doesn't do what I expect.

---

## Phase 4 â€” Effects, Refs, and the Component Lifecycle

**Why this phase exists:** most real apps need to talk to the outside world â€” fetch data, subscribe to events, measure DOM nodes. `useEffect` is React's escape hatch for side effects. `useRef` gives you a persistent value that survives re-renders without triggering them.

**Learn:**
- `useEffect` â€” what it does, when it runs, how the dependency array controls it
- **Effect dependency arrays:** `[]` (once on mount), `[dep]` (when dep changes), no array (every render) â€” and the consequences of each
- **Cleanup functions** â€” returning a function from `useEffect` to undo what you did
- **Common effect patterns:** fetch on mount, subscribe to events, sync with external state
- **Effect anti-patterns:** infinite loops, stale closures, fetching in the wrong place
- `useRef` â€” persisting a value across renders without re-triggering render, accessing DOM nodes
- **`useCallback` and `useMemo`** â€” when to use them, when they don't matter (the React 19 Compiler reduces the need for manual memoization â€” see Phase 8)

**React 19 improvements worth knowing:**
- **`use()` hook** â€” read resources (Promises, Context) inside render, without `useEffect`. Cleaner than the old `useState + useEffect` pattern for simple async data.
- **Better async transitions** â€” `useTransition` and `useDeferredValue` mark state updates as non-urgent, keeping the UI responsive while a heavy update runs.
- **Improved error reporting** â€” error boundaries now give you better error info in dev.

**Mental model for effects:**
> "Use `useEffect` when you need to synchronize React with something outside of React. If it's a one-time setup, clean it up. If it reacts to a change, list the dependency."

> **"Effect vs. event handler" rule of thumb:** If the side effect is caused by the **user** (button click, form submit), put it in the **event handler** â€” not in `useEffect`. If it's caused by the component **mounting** or **state changing**, use `useEffect`. In real apps, you'll often use a data library (TanStack Query) instead of `useEffect` for fetching â€” we'll cover that in the Next.js path.

**Mini task:**
Wire the product listing to a **real Laravel API**:
- Fetch products from `/api/products` in a `useEffect` on mount
- Handle loading state (show a spinner), error state (show the CoE error envelope), and success state
- Add **debounced search** â€” wait 300ms after the user stops typing before fetching (use `setTimeout` in a `useEffect` cleanup)
- Add a **click-outside ref** on the search input that closes a dropdown
- **Stretch:** refactor the initial fetch to use the `use()` hook instead of `useState` + `useEffect` and compare the code

**Self-check:**
- [ ] I can explain what a "stale closure" is and how cleanup functions prevent it.
- [ ] I can choose between `useEffect` for data fetching vs. fetching in an event handler.
- [ ] I can explain when `useCallback` actually helps performance and when it's premature optimization.
- [ ] I can name one thing the React 19 `use()` hook does that the older `useState + useEffect` pattern doesn't.

---

## Phase 5 â€” Forms, Validation, and API Integration

**Why this phase exists:** every product we ship is, eventually, a form. Forms are where the most bugs live. Get the form story right once and you stop re-learning it per project.

**Learn:**
- **Form handling patterns:** controlled inputs vs. `FormData` vs. uncontrolled with refs
- **React Hook Form** â€” register inputs, handle submission, show errors, reset â€” with minimal re-renders
- **Zod** for schema validation (matches our Node.js standard) â€” infer TypeScript types from schemas
- **API integration patterns:** where to fetch, where to mutate, how to handle errors
- **Optimistic updates** â€” update the UI before the server confirms; roll back on error
- **Toast notifications** for success/error feedback
- *(Forward-looking)* React 19's `useActionState` and **Server Actions** are the natural extension of the React Hook Form + Zod pattern when you move to Next.js â€” covered in the [Next.js Learning Path](../nextjs/intermediate.md#phase-6--forms-validation-and-mutations). For pure React (Vite, CRA, etc.), stick with React Hook Form.

**Standard pattern (use this for new work):**

```
User fills form (React Hook Form + Zod)
        â”‚  submit
        â–¼
validate with Zod
        â”‚  valid?
        â–¼
POST to Laravel API
        â”‚  200?
        â–¼
update local state (optimistic or on success)
        â”‚  error?
        â–¼
show error in CoE standard error envelope
```

**Mini task:**
Build a **customer add/edit form**:
- React Hook Form + Zod schema (name required, email must be valid, phone optional)
- "Add Customer" button â†’ POST to a Laravel endpoint (mock or real)
- Inline field errors (red text below the field)
- Toast notification on success
- List of customers rendered below the form (adds the new customer optimistically)

**Self-check:**
- [ ] I can explain why we validate on the client *and* on the server.
- [ ] I can return a Zod error tree to the UI and render it field-by-field.
- [ ] I can explain the difference between optimistic update and waiting for the server.

---

## Phase 6 â€” Composition Patterns and Custom Hooks

**Why this phase exists:** once you can build a component, the next skill is building a **system** of components that compose well. Custom hooks let you extract and share logic without sharing state.

**Learn:**
- **Component composition deep dive:**
  - **Specialization:** generic component + specific variants via props
  - **Compound components:** `<Select><SelectTrigger /><SelectContent /></Select>` â€” components that share implicit state
  - **Render props:** passing a function as a child to control rendering
  - **Higher-Order Components (HOCs):** wrapping a component to add behavior (know them, prefer hooks)
- **Custom hooks:** extracting logic into a reusable function prefixed with `use`
  - `useFetch(url)` â€” fetch + loading + error + data
  - `useLocalStorage(key, initial)` â€” persist state to localStorage
  - `useDebounce(value, delay)` â€” delay a value change
  - `useAuth()` â€” wrap the Laravel auth check
- **Context API:** `createContext`, `useContext`, `Provider` â€” for data that's needed deeply without prop drilling
  - When to use it: theme, auth user, language
  - When not to use it: frequently changing data (use state + props instead)

**Mini task:**
Take the customer feature from Phase 5 and refactor it:
1. Extract the customer list fetch into a `useCustomers()` custom hook
2. Extract the form into a `<CustomerForm />` that accepts an optional `customer` prop (for edit mode)
3. Wrap the app in an `AuthContext` that provides the current user
4. Use a `<ProtectedRoute>` compound component to gate the customer page

**Self-check:**
- [ ] I can explain when to extract logic into a custom hook vs. keeping it in the component.
- [ ] I can explain the difference between composition, render props, and HOCs.
- [ ] I can describe a scenario where Context is the right tool and one where it's the wrong tool.

---

## Phase 7 â€” Testing React Components

**Why this phase exists:** we have a Node.js testing standard ([Node.js TypeScript Best Practices](../../../../nodejs/nodejs-typescript-best-practices.md)) â€” the React path extends it.

**Learn:**
- **Vitest** â€” unit test runner (or Jest if a project predates it)
- **React Testing Library (RTL)** â€” test components the way users interact with them
  - Query by role, label, text â€” **not** by class name or internal state
  - `render`, `fireEvent`, `screen`, `within`
- **MSW (Mock Service Worker)** â€” intercept API calls at the network level, return fake data
  - Same handlers run in Vitest (Node) and the browser â€” one definition, both environments
- **Testing patterns:**
  - Render a component, find elements, interact, assert the result
  - Test behavior, not implementation
  - Mock at the API boundary (`services/`), not inside components

**Minimum expectation per developer:**
> Every developer should know how to test **a form, a data-fetching component, an API error state, and at least one user interaction flow**.

**Mini task:**
- RTL test for `<ProductList />` â€” renders products, filters when search input changes, shows loading state
- RTL test for `<CustomerForm />` â€” renders, submits empty form, shows validation errors
- MSW handler returning a fake Laravel response for the customer list
- One test for the `useCustomers()` custom hook (no component needed)
- *Stretch:* a pure unit test for a `useReducer` reducer (no React, no RTL â€” just `expect(reducer(state, action)).toEqual(newState)`)

**Self-check:**
- [ ] I can test a component without knowing its internal state variable names.
- [ ] I can mock a Laravel API response with MSW and assert the UI renders the right state.
- [ ] I can test a custom hook without rendering a component.

---

## Phase 8 â€” Production Patterns and Project Structure

**Why this phase exists:** "works on my machine" is not shipped. Production React has different constraints: bundle size, accessibility, error boundaries, and a folder structure that scales beyond one developer.

**Learn:**
- **Styling:** **Tailwind CSS** is the team default (per the [Next.js path Phase 8](../nextjs/intermediate.md#phase-8--ui-system-and-frontend-architecture)). For pure-React SPAs, set up Tailwind on day one. **shadcn/ui** for primitives â€” same "owned by us" framing as the Next.js path. If a project already uses CSS Modules, follow the existing convention.
- **Routing (pure-React only):** if you're building a Vite-React SPA â€” not a Next.js app â€” add **React Router v6+**. Pattern: `<BrowserRouter>` â†’ `<Routes>` â†’ `<Route path="â€¦" element={â€¦} />`. Skip this if the app is going inside Next.js (file-based routing handles it).
- **State management at scale:** Context + `useReducer` cover 90% of state. Reach for **Redux Toolkit** only when (a) many components need the same data, (b) you need time-travel debugging or middleware (sagas, polling), or (c) the team already standardized on it. **Zustand** is the lighter alternative â€” pick one if Context is painful, not before. Don't reach for state-management libraries "just in case."
- **Design tokens:** colors, spacing, type scale â€” never hardcode hex values. Use CSS custom properties or a Tailwind theme extension.
- **Web security basics:** render untrusted user input as text (`{user.bio}` in JSX, never `dangerouslySetInnerHTML`), and rely on Laravel Sanctum for CSRF (covered in the [Next.js path Phase 7](../nextjs/intermediate.md#phase-7--authentication-and-authorization)). If the app is browser-only and consumes a public API, validate inputs on the client with Zod and on the server.
- **Core Web Vitals (LCP, INP, CLS):** recognize them in Lighthouse. LCP = largest contentful paint (target < 2.5s). INP = interaction to next paint (target < 200ms). CLS = cumulative layout shift (target < 0.1). All three are why we lazy-load, `next/image`-style sizing, and avoid layout-thrashing animations.
- **Utility libraries (team default):** `clsx` for class composition, `date-fns` for dates, native `fetch` over axios. Don't add lodash, moment, or rxjs to a new project.
- **PWAs / offline:** out of scope for this path. If a product needs install-to-homescreen or offline support, see the CoE PWA guide (TODO).
- **i18n:** out of scope for this path. If the product supports multiple languages, see the CoE i18n policy (TODO).
- **Folder structure for a React project:**
  ```
  src/
    components/       â† shared, generic UI (Button, Input, Modal)
    features/         â† vertical slices: customers/, products/
      customers/
        components/
        hooks/
        api.ts        â† API calls for this feature
        schemas.ts    â† Zod schemas
    hooks/            â† cross-feature custom hooks
    lib/              â† framework glue (fetch client, env, utils)
    services/         â† API clients (Laravel SDK wrappers)
    types/            â† shared TypeScript types
    App.tsx
    main.tsx
  ```
- **`React.memo`, `useMemo`, `useCallback`** â€” when they help, when they don't
- **React 19 Compiler (auto-memoization):** the experimental/stable compiler can automatically memoize components and hooks, reducing the need for `useMemo` and `useCallback` boilerplate. **Don't add manual memoization "just in case"** â€” measure first with the Profiler, then optimize. The Compiler is an opt-in config; ask a tech lead before enabling in a production project.
- **Code splitting and lazy loading** â€” `React.lazy` + `Suspense` for route-level splitting
- **Error boundaries** â€” catching render errors without crashing the whole app
- **Accessibility basics** â€” semantic HTML, ARIA when needed, keyboard navigation, focus management, color contrast
- **Accessibility linting** â€” `eslint-plugin-jsx-a11y` catches missing alt text, broken ARIA, label/input mismatches, and other a11y mistakes at lint time. Add it to the project from day one.
- **Bundle analysis** â€” `vite-bundle-visualizer` (or `rollup-plugin-visualizer`) gives you a treemap of what's in your JS bundle. Run it on every release; the first time you do, you'll find a surprise.
- **Performance awareness** â€” why re-renders happen, the React DevTools Profiler, avoiding unnecessary re-renders
- **Build process** â€” `vite build` outputs, what's in `dist/`

**Mini task:**
Take the customer feature and prepare it for production review:
1. Organize files into the `features/` structure above
2. Add an error boundary around the customer page
3. Lazy-load the customer form (`React.lazy` + `Suspense`)
4. Run the React DevTools Profiler â€” identify and fix one unnecessary re-render
5. Run an accessibility check (axe DevTools or Lighthouse) â€” fix the top issue
6. Run `vite build` â€” review the bundle size
7. Run `vite-bundle-visualizer` â€” note the three largest chunks and decide if any are worth lazy-loading
8. Add `eslint-plugin-jsx-a11y` and fix the warnings it surfaces

**Self-check:**
- [ ] I can explain why a component re-rendered and how to prevent it.
- [ ] I can describe the folder structure and where a new feature would go.
- [ ] I can run a Lighthouse audit and explain its top 3 findings.
- [ ] I can read a bundle treemap and identify a candidate for code splitting.
- [ ] I can name the three Core Web Vitals and roughly what targets they should hit.
- [ ] I can explain when I'd reach for Context, Redux Toolkit, or Zustand â€” and when none of them.

---

## Recommended Courses

**Reading order:** official sources first â€” they are the most current. Treat third-party content as supplements.

> **Using AI to accelerate:** tools like Cursor, Claude Code, or Copilot pair well with these resources â€” paste a doc section and ask for a summary, ask an LLM to explain a concept in your own terms, or have it scaffold the exercise at the end of a doc chapter. This is the **collaborate** tier of the CoE AI delegation model ([AI Era Coding Guidelines](../../../../general/ai-era-coding-guidelines.md)). Keep auth, payments, and prod DB migrations manual.

| Level | Course | Why | Cost |
|---|---|---|---|
| **Primary â€” React** | [react.dev/learn](https://react.dev/learn) â€” official React docs (Quick Start, Thinking in React, Managing State) | Official, current, project-based, maintained by the React team | Free |
| **Supplement â€” interactive** | [Scrimba: Learn React](https://scrimba.com/learn/learnreact) â€” video + embedded editor, pause-and-edit | Best for visual / kinesthetic learners; type along without setting up a project | Free (Scrimba account) |
| **Supplement â€” full video build** | *Modern React Full Course 2026* â€” ByteGrad or freeCodeCamp on YouTube (search for the latest) | Single sitting, full build from zero to deploy; pick a 2025/2026 release | Free |
| Deep dive | *The Road to React* â€” Robin Wieruch (free online) | Written for developers, concise, covers hooks well | Free |
| TypeScript + React | *Total TypeScript* â€” Matt Pocock | Best-in-class for the TypeScript + React typing patterns we use | Paid |

> **CoE rule:** Course work is a starting point. Real learning happens in the **weekly deliverable** and in code review on a real codebase.

---

## Channels, Podcasts & Newsletters

Curated, low-noise, high-signal. Subscribe to 2â€“3 â€” more than that and you'll stop reading them.

**YouTube channels**
- [React](https://www.youtube.com/@react) â€” official React channel
- [Lee Robinson](https://www.youtube.com/@leerob) â€” Vercel VP, practical React + Next.js patterns
- [Jack Herrington](https://www.youtube.com/@jherr) â€” React, RSC, advanced patterns
- [Web Dev Simplified](https://www.youtube.com/@WebDevSimplified) â€” fundamentals refresher
- [Theo â€“ t3.gg](https://www.youtube.com/@t3dotgg) â€” opinionated, fast-moving, useful counterpoints

**Podcasts**
- *Syntax.fm* â€” weekly, broad web dev with regular React episodes
- *JS Party* â€” panel format, good for "what's the consensus on X"
- *React Round Up* â€” narrower, React-heavy

**Newsletters**
- [Bytes](https://bytes.dev/) â€” daily, sharp JavaScript news
- [React Status](https://react.statuscode.com/) â€” React ecosystem
- [TLDR Web Dev](https://tldr.tech/webdev) â€” broad, 5-minute read

**Blogs to follow**
- [React Blog](https://react.dev/blog) â€” official releases and deep dives
- [Dan Abramov's blog](https://overreacted.io/) â€” long-form React deep dives

---

## Tutorial & Reference Links

Bookmark these; you'll return to them often.

**Official**
- [React Docs (learn)](https://react.dev/learn)
- [React Docs (reference)](https://react.dev/reference/react)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [Zod Docs](https://zod.dev/)
- [React Hook Form Docs](https://react-hook-form.com/)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [MSW Docs](https://mswjs.io/)
- [Vitest Docs](https://vitest.dev/)
- [React Testing Library Docs](https://testing-library.com/react)

**Curated tutorials**
- [Scrimba: Learn React](https://scrimba.com/learn/learnreact) â€” interactive, pause-and-edit
- [Patterns.dev](https://www.patterns.dev/) â€” modern web app patterns (free book)
- [The Road to React](https://www.roadtoreact.com/) â€” Robin Wieruch, written for developers

**Recipes & cookbooks**
- [React Examples repo](https://github.com/facebook/react/tree/main/docs/src/components/examples) â€” official examples
- [useHooks](https://usehooks.com/) â€” collection of curated React hooks with explanations

---

## Certifications

There is **no first-party React certification** from Meta or the React team. Adjacent certifications:

| Certification | Issuer | Why it matters | Cost |
|---|---|---|---|
| **Meta Front-End Developer Professional Certificate** | Coursera / Meta | Covers React fundamentals, JS, CSS â€” useful if Phase 2 feels shaky | Paid |
| **freeCodeCamp: Front End Development Libraries Certification** | freeCodeCamp | Covers React, Redux, and frontend tooling; self-paced, project-based | Free |
| **Vercel Front-End Developer Certification** (when available) | Vercel | First-party, focused on the React + Next.js stack we use | Paid |

> **CoE stance:** Certifications are a **floor**, not a ceiling. A working weekly deliverable + code review history on `dev` is worth more than any certificate. Use certs to round out gaps, not to substitute for building.

---

## How to Use This Path

**This is v0.1 Draft for Pilot Batch.** Run it with 3â€“5 developers first. Collect feedback after Week 3 and revise before rolling out to the full team.

1. **Complete the Prerequisites** (above) before Week 1. If you can't, talk to a tech lead.
2. **Start on Monday.** Pick a phase. Work in pairs where the path says to pair.
3. **Deliver on Friday.** The weekly deliverable is what gets reviewed. It can be small.
4. **Open a PR for every deliverable.** Even tiny ones. The habit is the point.
5. **Use AI carefully.** Per [CoE AI guidelines](../../../../general/ai-era-coding-guidelines.md), AI can *explain concepts*, *scaffold tests* (Phase 7 especially), and *review* code â€” but **auth and DB migration code is Red Zone, manual only.** Tag AI-assisted commits `[ai-assisted: <tool>]`.
6. **Track progress.** Use a shared Notion/Kanban or a simple spreadsheet: one row per developer, one column per phase, check off self-checks as you go. Review in the team meeting each Friday.
7. **Then move to Next.js.** This path feeds directly into [../nextjs/intermediate.md](../nextjs/intermediate.md). Once you've completed this path, the Next.js path will feel like a natural extension â€” not a completely different world.
8. **Feedback loop.** After Week 3 of the pilot, open a feedback PR against this doc with: what was too hard, what was skipped, what was missing, what should be cut. Revise for the full-team rollout.
9. **Update this doc.** Broken link? Better course? Found a gap? PR it. This is a living document.
10. **Cross-link with our existing standards:**
    - Code review: [nodejs-typescript-code-review-checklist.md](../../../../nodejs/nodejs-typescript-code-review-checklist.md)
    - API design: [rest-api-best-practices.md](../../../../general/rest-api-best-practices.md)
    - AI policy: [ai-era-coding-guidelines.md](../../../../general/ai-era-coding-guidelines.md)
    - Git workflow: [git/Techversant_Git_Workflow.md](../../../../git/Techversant_Git_Workflow.md)

---

## Document Control

| Field | Value |
|---|---|
| Document | React Learning Path â€” For the Web Dev Team |
| Version | 0.3 (roadmap gap closure: Tailwind/shadcn call, React Router, state-mgmt rule, design tokens, security basics, Core Web Vitals, utility-lib defaults, PWA/i18n pointers) |
| Owner | CoE Web Working Group |
| Review Cycle | Quarterly |
| Status | Draft â€” pilot batch |
| Supersedes | v0.2 |
| Related | [Next.js Learning Path](../nextjs/intermediate.md), [Node.js TypeScript Best Practices](../../../../nodejs/nodejs-typescript-best-practices.md), [REST API Best Practices](../../../../general/rest-api-best-practices.md), [AI Era Coding Guidelines](../../../../general/ai-era-coding-guidelines.md) |

---

**Maintained by:** Techversant CoE
**Last Updated:** June 2026
