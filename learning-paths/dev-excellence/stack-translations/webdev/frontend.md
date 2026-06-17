# Frontend Stack Translation — Developer Excellence Curriculum

> **Audience:** Developers working on a **web frontend** codebase.
> **Purpose:** Companion to the universal [Developer Excellence Curriculum](../../curriculum.md). For each of the 20 topics: *what changes in your stack, and what does the mini-task look like?*
> **Read alongside:** [curriculum.md](../../curriculum.md) (the universal master) + your team's stack-specific code-review checklist.
> **Status:** Draft for pilot-batch review — v0.3.

---

## How to use this document

For each topic in the master curriculum, the section below has three short lines:

- **What changes in this stack** — the diff from the master, *not* a restatement of the topic. If you read the master, this is the only new information you need.
- **Mini-task variant** — the master's mini-task, rewritten for the frontend context.
- **Watch** — one verified YouTube link (provided by your tech lead) on this exact topic. If the link is missing, search YouTube for the topic and pick a video under 15 minutes from a known channel.

---

## Topic 1 — Clean Code Fundamentals

**What changes in this stack:** Naming is about *UI vocabulary* and *lifecycle*, not just code vocabulary. A `<ProductCard>` is a real concept the user sees; `ProductListItem` is more specific. The name should match the concept the user and the team would recognize. Components are nouns; variables hold UI state; methods are event handlers and lifecycle hooks.

**Mini-task variant:**
Pick a recent component you wrote. Re-read it: *can a new frontend dev understand this without context?* Rename any unclear names. Extract any component doing two visual jobs. Open a follow-up PR tagged `refactor(clean-code-1): <your-name>`.

**Watch:** Search YouTube for "clean code functions Uncle Bob" — pick a video under 10 min.

---

## Topic 2 — Control Flow & Logic Clarity

**What changes in this stack:** Deeply nested control flow shows up as nested conditional rendering, complex reducer switches, and event-handler chains. Fix: derived values, early returns in handlers, replace nested ternaries with a small lookup or component switch. A render function with 4 levels of `{cond1 ? cond2 ? ...}` is the frontend equivalent of a 4-level nested if.

**Mini-task variant:**
Find the most deeply nested render function or reducer. Refactor it using a derived value and a component switch. Commit `refactor(control-flow-2): <component-name>`.

**Watch:** Search YouTube for "guard clauses early return" — pick a video under 10 min.

---

## Topic 3 — DRY vs. WET

**What changes in this stack:** Frontend has a strong over-abstraction temptation — the "shared component" that takes 12 props and has 8 conditional branches is the classic smell. Rule of three still applies. A *good* frontend abstraction has a single visual identity (`<Button>`, `<Input>`, `<Modal>`). A *bad* one is where you'd have to look at the call site to know what it looks like.

**Mini-task variant:**
Find a shared component in your codebase with 3+ consumers that has noticeably different shapes. Inline it back into the 3 call sites. Commit `refactor(clean-code-3): inline-over-abstraction`.

**Watch:** Search YouTube for "wrong abstraction Sandi Metz" — pick the talk excerpt.

---

## Topic 4 — Basic Error Handling

**What changes in this stack:** Two error surfaces — the *user* (a friendly "We couldn't load that" message) and the *developer* (a console log with context). "Fail fast" often means: don't optimistically update if the underlying call will fail; don't render a half-loaded screen — show the error UI or the loading UI, not a jumble. Use the framework's error-boundary pattern to keep the boundary clean.

**Mini-task variant:**
Pick one error path in your UI. Verify it: (1) fails fast at the cause, (2) shows a user-friendly message, (3) logs enough context for the on-call engineer, (4) does NOT log PII, tokens, or secrets. Fix any of the four that are missing. Commit `refactor(clean-code-4): error-handling`.

**Watch:** Search YouTube for "react error boundaries" — pick a 5–10 min video.

---

## Topic 5 — SOLID Principles (Core)

**What changes in this stack:** SOLID maps to *component design*, not class design. S = one component, one job. O = extend by composition or by adding a prop, not by editing. L = polymorphic components that can be swapped. I = small prop interfaces — split a 12-prop component. D = inject dependencies as props or context, don't `import` them inside the component body.

**Mini-task variant:**
Pick the *worst-designed* component in your codebase (too many props, too many responsibilities, or too much internal state). Apply the SOLID principles, *one refactor per principle*, in five separate PRs. Title each `refactor(solid-N): <principle>`.

**Watch:** Search YouTube for "SOLID principles explained" — pick a video under 10 min.

---

## Topic 6 — Separation of Concerns (SoC)

**What changes in this stack:** A component should not also be the data fetcher, the business-logic container, and the layout. Cure: keep the visual concern in the component, the data concern in a hook or data layer, the business logic in a service module. The "thin component" is the frontend equivalent of the "thin controller" — orchestrates, doesn't decide. A component over ~50 lines is doing more than one concern.

**Mini-task variant:**
Find a component with more than 50 lines. Extract the data-fetching into a hook (or data layer) and the business logic into a service module. The component should become a thin orchestrator. Commit `refactor(soc): <component-name>-to-thin`.

**Watch:** Search YouTube for "container presentational pattern" — pick a 5–10 min video.

---

## Topic 7 — Dependency Injection & IoC

**What changes in this stack:** UI dependencies are usually the *data source* (a fetch client, a state store), the *logger*, the *clock* (`Date.now()`), and the *router*. Pass them in; don't `import` them inside the component body. Frameworks have idioms: prop drilling (small trees), context (deeper), state-management library. The principle is unchanged.

**Mini-task variant:**
Find a component that imports and calls a data source directly. Inject the data source as a prop (or via context / a hook). Write a unit test that uses a mock data source. Commit `refactor(di): inject-<dependency>`.

**Watch:** Search YouTube for "dependency injection frontend" — pick a 10–15 min video.

---

## Topic 8 — Reusability & Extensibility

**What changes in this stack:** Composition over inheritance — frontend doesn't have a strong inheritance problem, but *prop explosion* is real (a `<Button>` that takes 20 props and tries to be every button). Fix: split the button into a `<Button>` (visual identity), a `<ButtonGroup>`, a `<LinkButton>`; let composition do the rest. Config-driven behavior is data — don't add a new prop for a behavior that's actually a configuration choice.

**Mini-task variant:**
Find a component in your codebase with 10+ props, several of which are flags (`isLoading`, `isDisabled`, `isError`, `isSuccess`). Refactor: extract the *visual identity* into a base component, compose the variants with a small wrapper. Commit `refactor(reuse): composition-over-props`.

**Watch:** Search YouTube for "composition over inheritance" — pick a video under 15 min.

---

## Topic 9 — Design Thinking for Engineering

**What changes in this stack:** The "user" is more than the end user — it's the developer who will *use* the component (`<UserCard>` consumer) and the designer who will *theme* it. Change scenarios: "If we add a dark mode, what changes?" "If we add a new locale, what changes?" "If the API adds a new field, what changes?" Variability points = props and design tokens. Stable part = visual identity.

**Mini-task variant:**
Take your current ticket. Write 3 change scenarios in the form "if X, then Y" before writing any code. Open an ADR (use the master's Phase 7 format). Ask your reviewer: do these scenarios match the design, or does the design need to change? Commit `docs(design): change-scenarios-<ticket-id>`.

**Watch:** Search YouTube for "design thinking software engineering" — pick a 5–10 min video.

---

## Topic 10 — Trade-off Analysis

**What changes in this stack:** Classic frontend trade-offs: render-everything-on-the-server vs. render-on-the-client; bundle size vs. feature richness; build-time optimization vs. runtime flexibility; custom design system vs. off-the-shelf. None of these have a "right" answer; they have informed trade-offs. Write it down, defend for 2 minutes, change when measurement says so.

**Mini-task variant:**
Take the design decision in Topic 9's ADR. Add a "Trade-offs" section that names what you gave up. Push the PR; ask your reviewer to challenge any trade-off they think is wrong. If you can't defend it, change the design.

**Watch:** Search YouTube for "trade-off analysis engineering" — pick a 10–15 min video.

---

## Topic 11 — Domain Modeling Basics

**What changes in this stack:** In a UI codebase, the "model" is the type (or the language's equivalent). Entity = has identity, is mutable (`User { id, name, email }` — same user even when name changes). Value object = no identity, defined by values (`Address { street, city, zip }`). The anemic model: a type that's just fields, with all the business logic in a separate utility. Fix: put the rules on the type (or a thin class wrapping it).

**Mini-task variant:**
Find a type in your codebase that's anemic (just fields, business rules in utilities). Move one business rule from the utility onto the type. Commit `refactor(ddd): move-rule-onto-model`.

**Watch:** Search YouTube for "value objects typescript" — pick a 10–15 min video.

---

## Topic 12 — RESTful API Design Principles

**What changes in this stack:** A frontend dev *consumes* the API, not designs it. The discipline: be a *good* consumer. Know HTTP methods and status codes (so you don't write a `try/catch` that swallows a 4xx differently from a 5xx). Know idempotency (so a retried POST doesn't double-create). Use the API's filter and sort conventions (the master cites the CoE standard).

**Mini-task variant:**
Pick one API your UI calls. Review it for the five points in the master. Open a doc PR (`docs(api-review): <endpoint>`) listing each gap. Coordinate with the API owner before changing the consumer.

**Watch:** Search YouTube for "REST API design best practices" — pick a 10–15 min video.

---

## Topic 13 — Validation & Boundary Protection

**What changes in this stack:** The "boundary" in the frontend is *every input from the user* (form fields, URL params, file uploads, drag-and-drop). The server is the last line of defense, but the client is the *first* — and a good first line catches most of the bad input before a round trip. Validate at the boundary: a form handler validates the form, a route loader validates URL params, a file upload handler validates the file. Re-validate on the server; never trust the client.

**Mini-task variant:**
Pick one form or input handler. Audit: is the validation at the boundary? Is the same schema shared with the server? Open a doc PR (`docs(validation-audit): <form>`) listing the gaps.

**Watch:** Search YouTube for "form validation client server" — pick a 10–15 min video.

---

## Topic 14 — Performance Awareness

**What changes in this stack:** The frontend "N+1" is a *re-render* — a list of 100 items that re-renders because one item changed. Fix: memoization, virtualization (only render what's on screen), stable references (don't create a new object identity on every render). "Caching basics" map to client-side caching (data layer / state management). "Measure-first" applies to the framework's profiler.

**Mini-task variant:**
Find one re-render in your codebase that's measurably slow. Use the framework's profiler to confirm. Apply the fix (memoization / virtualization / stable references). Commit `perf(re-render): <component-name>` with the before/after numbers in the PR description.

**Watch:** Search YouTube for "react performance slow renders" — pick a 10–15 min video.

---

## Topic 15 — Testing Fundamentals

**What changes in this stack:** Frontend has *unit* (a function, a hook), *component* (a component with a mock data source), and *E2E* (a real browser, real user flow). The pyramid still applies: many unit, some component, few E2E. The "what NOT to test" is the framework's rendering — trust the framework to render a `<div>`; test the *behavior* your component adds.

**Mini-task variant:**
Write one component test for a component you wrote in the last week. The test name should be a sentence. The body should be arrange/act/assert. Commit `test: <component-name>`.

**Watch:** Search YouTube for "testing javascript Kent C Dodds" — pick a 5–10 min video.

---

## Topic 16 — Writing Testable Code

**What changes in this stack:** A testable component takes its dependencies as props (or via context), uses the framework's testing utilities (`render`, `screen`, `fireEvent`), and doesn't reach for `Date.now()` or `Math.random()` inside the render body. The "inject the clock" pattern: pass a `clock` or `useFakeTimers` setup. Hidden dependencies: `new Date()`, `localStorage`, the global `fetch`.

**Mini-task variant:**
Find a component in your codebase that uses `Date.now()` or a global fetch directly. Inject the dependency (or wrap it in a hook). Write a component test with a fixed time / a mock fetch. Commit `refactor(testable): inject-<dependency>`.

**Watch:** Search YouTube for "mocking strategies frontend tests" — pick a 10–15 min video.

---

## Topic 17 — Refactoring Techniques

**What changes in this stack:** Frontend refactor decision rules: refactor a *component* (extract sub-components, rename, split props) when names are right but body is wrong; refactor a *type* (split a giant type, add a value object) when the same type is used in three places; rewrite a *screen* when the architecture doesn't fit. The Fowler smell catalog still applies: long method, large class, long parameter list, primitive obsession. In the frontend, "long parameter list" is often "long prop list" — same smell, same fix.

**Mini-task variant:**
Take a code smell from your frontend codebase. Refactor it in a single PR. The PR should be small enough to read in 10 minutes. The tests should be green before and after. Commit `refactor: <smell>`.

**Watch:** Search YouTube for "refactoring UI components" — pick a 10–15 min video.

---

## Topic 18 — Effective Code Review Practices

**What changes in this stack:** A UI PR review is about *intent* (matches the design?), *correctness* (data flow works?), *readability* (next frontend dev understands?), and *accessibility* (keyboard, screen reader, color contrast, motion preferences, focus management). Defer to the formatter. Be objective, not subjective. "Questions not commands" applies especially to UI — the design is often a judgment call: "Could this be a `<dialog>`?" is better than "Use a `<dialog>`."

**Mini-task variant:**
Review 5 PRs in the next week. For each PR, write at least one question (not a command) and at least one specific praise. After the week, reflect: did the tone work? What would you do differently?

**Watch:** Search YouTube for "code review best practices Google" — pick a 10–15 min video.

---

## Topic 19 — Code Review Checklist (Standardized)

**What changes in this stack:** The master's 9-point checklist applies, with one frontend-specific row to add: **Accessibility** (keyboard, screen reader, color contrast, motion preferences, focus management). Use the framework's a11y testing tool (axe-core, eslint-plugin-jsx-a11y, or the framework's built-in lint rules) in CI to catch the easy stuff automatically.

**Mini-task variant:**
Pick 3 of your open PRs. Self-review them against the 9-point master checklist + the accessibility row. Open follow-up PRs for any gap. Reflect: which points did you consistently miss?

**Watch:** Search YouTube for "accessibility frontend developers" — pick a 10–15 min video.

---

## Topic 20 — Engineering Ethics & Ownership

**What changes in this stack:** A frontend dev owns the *user's experience*. Code is read more often than written, but UI code is *used* more often than either. A confusing button is a slow product, not just bad code. Same ownership principle: name the technical debt you create ("this prop will need to become a slot in v2"), flag the debt you inherit.

**Mini-task variant:**
Find the oldest open TODO in your frontend codebase. Read it. Is it still relevant? If yes, file a ticket and link it; if no, close it. Commit `chore: review-todo-<module>`.

**Watch:** Search YouTube for "ethics of software engineering" — pick a 10–15 min video.

---

## Phase 7 — Senior Developer Mindset (Lead Track)

**What changes in this stack:** A frontend lead owns the *architecture* (component library, state management, build pipeline, design tokens) and the *mentoring* (helping junior devs write better components). The ADRs a frontend lead writes tend to be about: component-library design choices, state-management migrations, server-rendering decisions, and bundle-size budgets. The Phase 7 reading list applies; the artifacts (3 ADRs, 1 architecture note, 1 backward-compat plan, 1 risk analysis, 1 mentoring reflection) are the same.

**Mini-task variant:**
Write one ADR for a real frontend architecture decision in your codebase. Use the master's Phase 7 format. Pair with a tech lead for review.

**Watch:** Search YouTube for "how to write ADR Michael Nygard" — pick a 10–15 min video.

---

## Document control

| Field | Value |
|---|---|
| Document | Frontend Stack Translation — Developer Excellence Curriculum |
| Version | 0.3 (rewrote per-topic structure to 'What changes + Mini-task + Watch'; replaced unverified YouTube links with search hints) |
| Owner | CoE Web Working Group (with cross-team review from Mobile + Backend) |
| Review Cycle | Quarterly |
| Status | Draft for pilot-batch review |
| Related | [curriculum.md](../../curriculum.md), [backend.md](./backend.md), [mobile stacks](../mobile/stacks.md) |
