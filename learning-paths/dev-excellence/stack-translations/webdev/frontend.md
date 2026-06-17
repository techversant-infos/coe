# Frontend Stack Translation — Developer Excellence Curriculum

> **Audience:** Developers working on a **web frontend** codebase (any UI framework).
> **Purpose:** Companion to the universal [Developer Excellence Curriculum](../../curriculum.md). Each of the 20 topics below says: *what does this topic mean in a frontend codebase, and what does the mini-task look like in your stack?*
> **Read alongside:** [curriculum.md](../../curriculum.md) (the universal master) + your team's stack-specific code-review checklist.
> **Status:** Draft for pilot-batch review — v0.1.

---

## How to use this document

1. **For every topic in the master curriculum**, the section below has:
   - **Concept in this stack** — 2-3 lines on what the universal principle looks like in a frontend codebase
   - **Mini-task variant** — the master's mini-task, rewritten for the frontend context
   - **Topic-specific video** — one or two well-known videos that teach *exactly* this concept (not a channel — a specific video)
2. **Use the master's code-review focus questions** as-is — they're universal.
3. **Use the master's self-check** as-is — it's stack-agnostic by design.

The master says "controller with more than 20 lines." This document says "the file that owns the request lifecycle on the client, the same thing on a UI server, or the view-model that orchestrates the screen — whichever your framework uses, *that* file is the controller. Apply the same rule."

---

## Topic 1 — Clean Code Fundamentals

**Concept in this stack:** Naming conventions in a frontend codebase are about *UI vocabulary*, not just code vocabulary. A `<ProductCard>` is a real concept the user sees; a `ProductListItem` is a more specific concept. The name should match the concept the user and the team would recognize.

Variables hold UI state (`isOpen`, `selectedTabId`, `searchQuery`) and derived values (`displayedProducts = filter(products, query)`). Methods are event handlers and lifecycle hooks. Components are nouns that match the design system.

**Mini-task variant:**
Pick a recent component you wrote. Re-read it with the focus question: *can a new frontend dev understand this without context?* Rename any unclear names. Extract any component that's doing two visual jobs. Open a follow-up PR tagged `refactor(clean-code-1): <your-name>`.

**Topic-specific video:**
- [Web Development In 2026 — A Practical Guide (Fireship)](https://www.youtube.com/watch?v=EuGDFjM3kq0) — short, opinionated, names the current frontend vocabulary in 11 minutes.

---

## Topic 2 — Control Flow & Logic Clarity

**Concept in this stack:** The "deeply nested if-else" pattern shows up in frontend code as deeply nested conditional rendering, complex reducer switch statements, and event-handler chains. The fix is the same: extract a derived value, use early returns in handlers, and replace nested ternaries with a small lookup or component switch.

Watch for: a render function with 4 levels of `{cond1 ? cond2 ? ... : ... : ...}` is the frontend equivalent of a 4-level nested if. It's harder to read, not easier.

**Mini-task variant:**
Find the most deeply nested render function or reducer in your current codebase. Refactor it using a derived value (a `const` computed at the top) and a component switch (small sub-components per case). Commit `refactor(control-flow-2): <component-name>`.

**Topic-specific video:**
- [The Flaw of If-Else Chains — Code Aesthetic (3 minutes)](https://www.youtube.com/watch?v=EumXakNps08) — short and on-topic for the early-return pattern.

---

## Topic 3 — DRY vs. WET

**Concept in this stack:** Frontend has a strong temptation to over-abstract. The "shared component" that takes 12 props and has 8 conditional branches is the classic smell. The rule of three still applies: copy once (acceptable), copy twice (acceptable), copy three times (extract).

A *good* abstraction in the frontend has a clear, single visual identity (`<Button>`, `<Input>`, `<Modal>`). A *bad* abstraction is one where you'd have to look at the call site to know what it looks like.

**Mini-task variant:**
Find a shared component in your codebase with 3+ consumers that has noticeably different shapes. Inline it back into the 3 call sites. Commit `refactor(clean-code-3): inline-over-abstraction`. If the component has a *visual* identity that genuinely is shared, write an ADR (Topic 9) explaining why you're keeping it.

**Topic-specific video:**
- [The "Aha" Moment When You Get DRY — Theo (3 minutes)](https://www.youtube.com/watch?v=l5RT-McT1nE) — opinionated take on the rule of three in UI code.

---

## Topic 4 — Basic Error Handling

**Concept in this stack:** Frontend has two error surfaces: the *developer* (a failed fetch throws; a console.error tells you why) and the *user* (a friendly "We couldn't load that. Please try again."). The boundary between them is the same as in the master: fail fast at the cause, surface user-friendly text, log the developer context.

In a UI codebase, "fail fast" often means: don't optimistically update if the underlying call will fail. Or: don't render a half-loaded screen — show the error UI or the loading UI, not a jumble.

**Mini-task variant:**
Pick one error path in your UI. Verify it: (1) fails fast at the cause (a request fails → the user sees an error, not stale data), (2) shows a user-friendly error message, (3) logs enough context for the on-call engineer, (4) does NOT log any PII, token, or secret. Fix any of the four that are missing. Commit `refactor(clean-code-4): error-handling`.

**Topic-specific video:**
- [Why Every Frontend Dev Should Learn Error Boundaries — Jack Herrington (8 minutes)](https://www.youtube.com/watch?v=ubyTsvjB14k) — covers the boundary pattern in client-rendered UI.

---

## Topic 5 — SOLID Principles (Core)

**Concept in this stack:** SOLID in the frontend maps to component design, not class design. S = one component, one job (a `<UserProfile>` doesn't also do `<CommentList>`). O = extend by composition or by adding a prop, not by editing the component. L = polymorphic components that can be swapped (a `<Button>` that can be `<Link>` styled as a button). I = small prop interfaces — if a component takes 12 props, split it. D = inject dependencies as props or context, not by importing them inside the component body.

**Mini-task variant:**
Pick the *worst-designed* component in your codebase (the one with too many props, too many responsibilities, or too much internal state). Apply the SOLID principles to it, *one refactor per principle*, in five separate PRs. Title each `refactor(solid-N): <principle>`.

**Topic-specific video:**
- [SOLID Principles in 100 Seconds — Fireship (2 minutes)](https://www.youtube.com/watch?v=5WHK6jFybWc) — quick refresher, not framework-specific.
- [Component Design Patterns — Jack Herrington (15 minutes)](https://www.youtube.com/watch?v=Yx-SXV4NQS4) — applies SOLID thinking to React components.

---

## Topic 6 — Separation of Concerns (SoC)

**Concept in this stack:** A frontend component should not also be the data fetcher, the business-logic container, and the layout. The cure: keep the visual concern in the component, the data concern in a hook or data layer, and the business logic in a service module.

The "thin component" is the frontend equivalent of the "thin controller": the component orchestrates, the data layer fetches, the service module decides. If your component is more than ~50 lines, it's probably doing more than one concern.

**Mini-task variant:**
Find a component in your codebase with more than 50 lines. Extract the data-fetching into a hook (or data layer) and the business logic into a service module. The component should become a thin orchestrator. Commit `refactor(soc): <component-name>-to-thin`.

**Topic-specific video:**
- [Container / Presentational Pattern — Web Dev Simplified (10 minutes)](https://www.youtube.com/watch?v=OEu8OW0F4_Q) — the canonical video on splitting data from view.

---

## Topic 7 — Dependency Injection & Inversion of Control

**Concept in this stack:** In a UI codebase, dependencies are usually the *data source* (a fetch client, a state store), the *logger*, the *clock* (`Date.now()`), and the *router*. The pattern is the same: pass them in, don't `import` them inside the component body.

Frameworks have idioms for this: prop drilling (small trees), context (deeper trees), or a dedicated state-management library. The principle is unchanged: the consumer doesn't construct the dependency.

**Mini-task variant:**
Find a component that imports and calls a data source directly. Inject the data source as a prop (or via context / a hook). Write a unit test that uses a mock data source. Commit `refactor(di): inject-<dependency>`.

**Topic-specific video:**
- [Dependency Injection in React — Leigh Halliday (12 minutes)](https://www.youtube.com/watch?v=fF6LEV3vua4) — practical, framework-aware.

---

## Topic 8 — Reusability & Extensibility

**Concept in this stack:** Composition over inheritance — frontend doesn't have a strong inheritance problem, but it has a *prop explosion* problem (a `<Button>` that takes 20 props and tries to be every button). The fix: split the button into a `<Button>` (the visual identity), a `<ButtonGroup>`, a `<LinkButton>`, and let composition do the rest.

Config-driven behavior: a feature flag, a config value, or a design-token lookup is data. Don't add a new prop to a component for a behavior that's actually a configuration choice.

**Mini-task variant:**
Find a component in your codebase with 10+ props, several of which are really flags (`isLoading`, `isDisabled`, `isError`, `isSuccess`). Refactor: extract the *visual identity* into a base component, compose the variants with a small wrapper. Commit `refactor(reuse): composition-over-props`.

**Topic-specific video:**
- [Composition vs Configuration — Matt Pocock (15 minutes)](https://www.youtube.com/watch?v=wfogZfDOWd0) — TypeScript-aware, applies to UI code in any framework.

---

## Topic 9 — Design Thinking for Engineering

**Concept in this stack:** The "user" in a frontend codebase is more than the end user — it's the developer who will *use* the component (`<UserCard>` consumer) and the designer who will *theme* it. Change scenarios in the frontend: "If we add a dark mode, what changes?" "If we add a new locale, what changes?" "If the API adds a new field, what changes?" Variability points are the props and the design tokens; the stable part is the visual identity.

**Mini-task variant:**
Take your current ticket. Write 3 change scenarios in the form "if X, then Y" before writing any code. Open an ADR (use the master's Phase 7 format). Ask your reviewer: do these scenarios match the design, or does the design need to change? Commit `docs(design): change-scenarios-<ticket-id>`.

**Topic-specific video:**
- [Design Thinking in 5 Minutes — Sprout (5 minutes)](https://www.youtube.com/watch?v=4u_K8L0e2sc) — quick, framework-agnostic.

---

## Topic 10 — Trade-off Analysis

**Concept in this stack:** The classic frontend trade-offs: render-everything-on-the-server (faster first paint, less interactivity) vs. render-on-the-client (slower first paint, more interactivity); bundle size vs. feature richness; build-time optimization vs. runtime flexibility; a custom design system vs. an off-the-shelf one. None of these have a "right" answer; they have informed trade-offs.

The right discipline: write down the trade-off, defend it for 2 minutes, change it when the measurement says so.

**Mini-task variant:**
Take the design decision in Topic 9's ADR. Add a "Trade-offs" section that names what you gave up. Push the PR; ask your reviewer to challenge any trade-off they think is wrong. If you can't defend it, change the design.

**Topic-specific video:**
- [Trade-off Analysis for Engineers — Hussein Nasser (12 minutes)](https://www.youtube.com/watch?v=zS0l3knxQsU) — backend-leaning but the trade-off thinking applies to frontend too.

---

## Topic 11 — Domain Modeling Basics

**Concept in this stack:** In a UI codebase, the "model" is the TypeScript type (or the equivalent in your language). An *entity* has identity and is mutable (`User { id, name, email }` — same user even when name changes). A *value object* has no identity and is defined by its values (`Address { street, city, zip }` — two addresses with the same fields are equal).

The "anemic model" in the frontend: a type that's just fields, with all the business logic in a separate utility file. The fix: put the rules on the type (or a thin class wrapping it).

**Mini-task variant:**
Find a type in your codebase that's anemic (just fields, business rules in utilities). Move one business rule from the utility onto the type. Commit `refactor(ddd): move-rule-onto-model`.

**Topic-specific video:**
- [Value Objects in TypeScript — Khalil Stemmler (18 minutes)](https://www.youtube.com/watch?v=9MOGZ5Fiqs0) — practical, framework-agnostic.

---

## Topic 12 — RESTful API Design Principles

**Concept in this stack:** A frontend dev consumes the API, not designs it. The relevant discipline is: be a *good* consumer. Know the HTTP methods and status codes (so you don't write a `try/catch` that swallows a 4xx differently from a 5xx). Know idempotency (so a retried POST doesn't double-create). Use the API's filter and sort conventions (the master cites the CoE standard).

**Mini-task variant:**
Pick one API your UI calls. Review it for the five points in the master (predictability, methods/status codes, idempotency, pagination/filtering/sort, versioning). Open a doc PR (`docs(api-review): <endpoint>`) that lists each gap. Coordinate with the API owner before changing the consumer.

**Topic-specific video:**
- [REST API Design Best Practices — Hussein Nasser (15 minutes)](https://www.youtube.com/watch?v=rp1eH4jK1vE) — quick, the master's REST standards applied.

---

## Topic 13 — Validation & Boundary Protection

**Concept in this stack:** The "boundary" in the frontend is *every input from the user* (form fields, URL params, file uploads, drag-and-drop). The server is the last line of defense, but the client is the *first* — and a good first line catches most of the bad input before a round trip.

Validate at the boundary: a form handler validates the form, a route loader validates URL params, a file upload handler validates the file. Re-validate on the server; never trust the client.

**Mini-task variant:**
Pick one form or input handler in your codebase. Audit: is the validation at the boundary? Is the same schema shared with the server? Open a doc PR (`docs(validation-audit): <form>`) listing the gaps.

**Topic-specific video:**
- [Form Validation Done Right — Jack Herrington (20 minutes)](https://www.youtube.com/watch?v=6a2E9dB3YkA) — covers client + server validation, framework-aware.

---

## Topic 14 — Performance Awareness

**Concept in this stack:** The frontend "N+1" is the *re-render* — a list of 100 items that re-renders because one item changed. The fix: memoization, virtualization (only render what's on screen), and stable references (don't create a new object identity on every render). The "caching basics" map to client-side caching (the data layer / state management) and the "measure-first" rule applies to the browser's profiler.

**Mini-task variant:**
Find one re-render in your codebase that's measurably slow. Use the framework's profiler to confirm. Apply the fix (memoization / virtualization / stable references). Commit `perf(re-render): <component-name>` with the before/after numbers in the PR description.

**Topic-specific video:**
- [React Performance: 7 Steps to Fix Slow Renders — Jack Herrington (15 minutes)](https://www.youtube.com/watch?v=4iTJ7TpgDx0) — pragmatic, framework-aware, applies the measure-first rule.

---

## Topic 15 — Testing Fundamentals

**Concept in this stack:** Frontend has three layers of tests: *unit* (a function, a hook), *component* (a component with a mock data source), and *E2E* (a real browser, real user flow). The pyramid still applies: many unit, some component, few E2E. The "what NOT to test" is the framework's rendering — trust the framework to render a `<div>`; test the *behavior* your component adds.

**Mini-task variant:**
Write one component test for a component you wrote in the last week. The test name should be a sentence. The body should be arrange/act/assert. Commit `test: <component-name>`.

**Topic-specific video:**
- [Testing JavaScript — Kent C. Dodds (course preview, 10 minutes)](https://www.youtube.com/watch?v=cRbD9dSpA60) — the canonical intro to the unit/component/E2E split.

---

## Topic 16 — Writing Testable Code

**Concept in this stack:** A testable component takes its dependencies as props (or via context), uses the framework's testing utilities (render, screen, fireEvent), and doesn't reach for `Date.now()` or `Math.random()` inside the render body. The "inject the clock" pattern applies: pass a `clock` or a `useFakeTimers` setup. Hidden dependencies are the same: `new Date()`, `localStorage`, the global `fetch`.

**Mini-task variant:**
Find a component in your codebase that uses `Date.now()` or a global fetch directly. Inject the dependency (or wrap it in a hook). Write a component test with a fixed time / a mock fetch. Commit `refactor(testable): inject-<dependency>`.

**Topic-specific video:**
- [Mocking Strategies for Frontend Tests — Web Dev Simplified (12 minutes)](https://www.youtube.com/watch?v=3ZPIYjrBkhg) — covers stubs vs. mocks in component tests.

---

## Topic 17 — Refactoring Techniques

**Concept in this stack:** Frontend refactors have their own decision rules: refactor a *component* (extract sub-components, rename, split props) when the names are right but the body is wrong; refactor a *type* (split a giant type, add a value object) when the same type is used in three places; rewrite a *screen* (throw out the file and start over) when the architecture doesn't fit the new requirement.

The Fowler smell catalog still applies: long method, large class, long parameter list, primitive obsession. In the frontend, "long parameter list" is often "long prop list" — same smell, same fix.

**Mini-task variant:**
Take a code smell from your frontend codebase. Refactor it in a single PR. The PR should be small enough to read in 10 minutes. The tests should be green before and after. Commit `refactor: <smell>`.

**Topic-specific video:**
- [Refactoring UI Components — Jack Herrington (15 minutes)](https://www.youtube.com/watch?v=3sLSi9T5eQo) — applies the Fowler catalog to UI code.

---

## Topic 18 — Effective Code Review Practices

**Concept in this stack:** A code review on a UI PR is about *intent* (does this match the design?), *correctness* (does the data flow work?), *readability* (will the next frontend dev understand it?), and *accessibility* (does this work for keyboard / screen reader / reduced motion users?). Defer to the formatter. Be objective, not subjective.

The "questions not commands" rule applies especially to UI PRs — the design is often a judgment call, and "Could this be a `<dialog>` instead of a custom modal?" is better than "Use a `<dialog>`."

**Mini-task variant:**
Review 5 PRs in the next week. For each PR, write at least one question (not a command) and at least one specific praise. After the week, reflect: did the tone work? What would you do differently?

**Topic-specific video:**
- [Code Review Best Practices — Google Engineering Practices (15 minutes)](https://www.youtube.com/watch?v=zlQzl2NHkhk) — the de-facto reference, framework-agnostic.

---

## Topic 19 — Code Review Checklist (Standardized)

**Concept in this stack:** The master's 9-point checklist applies, with one frontend-specific row to add: **Accessibility** (keyboard, screen reader, color contrast, motion preferences, focus management). Use your framework's a11y testing tool (axe-core, eslint-plugin-jsx-a11y, or the framework's built-in lint rules) in CI to catch the easy stuff automatically.

**Mini-task variant:**
Pick 3 of your open PRs. Self-review them against the 9-point master checklist + the accessibility row. Open follow-up PRs for any gap. Reflect: which points did you consistently miss?

**Topic-specific video:**
- [Accessibility for Frontend Developers — Marcy Sutton (20 minutes)](https://www.youtube.com/watch?v=ckD6lxoYGN8) — practical, framework-agnostic.

---

## Topic 20 — Engineering Ethics & Ownership

**Concept in this stack:** A frontend dev owns the *user's experience*. The principle: code is read more often than written, but UI code is *used* more often than either. A confusing button is a slow product, not just bad code. The same ownership principle: name the technical debt you create (e.g. "this prop will need to become a slot in v2"), and flag the debt you inherit.

**Mini-task variant:**
Find the oldest open TODO in your frontend codebase. Read it. Is it still relevant? If yes, file a ticket and link it; if no, close it. Commit `chore: review-todo-<module>`.

**Topic-specific video:**
- [The Ethics of Software Engineering — CodeAesthetic (12 minutes)](https://www.youtube.com/watch?v=BOfrJzgI7V0) — short, on-topic, framework-agnostic.

---

## Phase 7 — Senior Developer Mindset (Lead Track)

**Concept in this stack:** A frontend lead owns the *architecture* (component library, state management, build pipeline, design tokens) and the *mentoring* (helping junior devs write better components). The ADRs a frontend lead writes tend to be about: component-library design choices, state-management migrations, server-rendering decisions, and bundle-size budgets. The Phase 7 reading list applies; the artifacts (3 ADRs, 1 architecture note, 1 backward-compat plan, 1 risk analysis, 1 mentoring reflection) are the same.

**Mini-task variant:**
Write one ADR for a real frontend architecture decision in your codebase. Use the master's Phase 7 format. Pair with a tech lead for review.

**Topic-specific video:**
- [How to Write a Good Frontend ADR — Lee McGovern / various (varies)](https://www.youtube.com/watch?v=kS1pZQLzJy0) — short, on the format and what to include.

---

## Document control

| Field | Value |
|---|---|
| Document | Frontend Stack Translation — Developer Excellence Curriculum |
| Version | 0.1 (initial — 20 topic translations + Phase 7) |
| Owner | CoE Web Working Group (with cross-team review from Mobile + Backend) |
| Review Cycle | Quarterly |
| Status | Draft for pilot-batch review |
| Related | [curriculum.md](../../curriculum.md), [backend.md](./backend.md), [mobile stacks](../mobile/stacks.md) |
