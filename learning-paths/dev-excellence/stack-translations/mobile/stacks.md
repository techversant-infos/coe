# Mobile Stack Translation — Developer Excellence Curriculum

> **Audience:** Developers working on a **mobile** codebase (any platform-native or cross-platform framework).
> **Purpose:** Companion to the universal [Developer Excellence Curriculum](../../curriculum.md). Each of the 20 topics below says: *what does this topic mean in a mobile codebase, and what does the mini-task look like in your stack?*
> **Read alongside:** [curriculum.md](../../curriculum.md) (the universal master) + your team's stack-specific code-review checklist.
> **Status:** Draft for pilot-batch review — v0.1.

---

## How to use this document

1. **For every topic in the master curriculum**, the section below has:
   - **Concept in this stack** — 2-3 lines on what the universal principle looks like in a mobile codebase
   - **Mini-task variant** — the master's mini-task, rewritten for the mobile context
   - **Topic-specific video** — one or two well-known videos that teach *exactly* this concept (not a channel — a specific video)
2. **Use the master's code-review focus questions** as-is — they're universal.
3. **Use the master's self-check** as-is — it's stack-agnostic by design.

The master says "controller with more than 20 lines." This document says "the entry point of the screen — the view controller, the screen / composable that owns the lifecycle, the presenter, or the view-model — whichever your framework uses, *that* file is the controller. Apply the same rule."

---

## Topic 1 — Clean Code Fundamentals

**Concept in this stack:** Naming conventions in a mobile codebase are about *UI vocabulary* and *lifecycle*. A `<ProductCard>` (or `ProductCardView`, depending on the platform) is a real concept the user sees. A `ProductListItemViewModel` is a more specific concept that the team recognizes. The name should match the concept.

Variables hold UI state (`isOpen`, `selectedTabId`, `searchQuery`) and derived values (`displayedProducts = filter(products, query)`). Methods are event handlers, lifecycle hooks, and navigation actions. Types / classes are nouns that match the design system or the screen.

**Mini-task variant:**
Pick a recent screen or view-model you wrote. Re-read it with the focus question: *can a new mobile dev understand this without context?* Rename any unclear names. Extract any function that does two things. Open a follow-up PR tagged `refactor(clean-code-1): <your-name>`.

**Topic-specific video:**
- [Clean Code in Mobile — Caolan McMahon (15 minutes)](https://www.youtube.com/watch?v=RR_dQ4sZjLA) — short, applies the universal principles to a mobile codebase.

---

## Topic 2 — Control Flow & Logic Clarity

**Concept in this stack:** The "deeply nested if-else" pattern in a mobile codebase is a view-model with three levels of business-rule nesting, or a deep navigation chain. The fix is the same: early returns + guard clauses. The mobile-specific twist: lifecycle methods (viewDidLoad, onCreate, onAppear) are *also* control flow, and a deep lifecycle method is a smell. Extract the lifecycle setup into private methods that each do one thing.

**Mini-task variant:**
Take the most deeply nested view-model or lifecycle method in your current codebase. Refactor it using early returns + guard clauses. Commit `refactor(control-flow-2): <view-model-or-screen-name>`.

**Topic-specific video:**
- [Refactoring Deeply Nested Code — Fun Fun Function (8 minutes)](https://www.youtube.com/watch?v=EumXakNps08) — short, the early-return pattern in practice.

---

## Topic 3 — DRY vs. WET

**Concept in this stack:** Mobile has a strong temptation to over-abstract — the "shared screen" that takes 12 props and has 8 conditional branches; the "common view-model" that does five things. The rule of three still applies: copy once (acceptable), copy twice (acceptable), copy three times (extract).

A *good* abstraction in the mobile codebase has a single, clear visual identity (a button, an input, a card). A *bad* abstraction is one where you'd have to look at the call site to know what it looks like.

**Mini-task variant:**
Find a shared view or view-model in your codebase with 3+ consumers that has noticeably different shapes. Inline it back into the 3 call sites. Commit `refactor(clean-code-3): inline-over-abstraction`. If the abstraction has a *visual* identity that genuinely is shared, write an ADR (Topic 9) explaining why you're keeping it.

**Topic-specific video:**
- [Don't DRY Too Early — Fun Fun Function (6 minutes)](https://www.youtube.com/watch?v=H0S6jAMCOEo) — short, on the rule of three in mobile code.

---

## Topic 4 — Basic Error Handling

**Concept in this stack:** Mobile has two error surfaces: the *user* (a friendly "We couldn't load that. Please try again." — the UI's error state) and the *developer* (a structured log line with the operation, the cause, the device context). The boundary between them is the same as the master: fail fast at the cause, surface user-friendly text, log the developer context.

In a mobile codebase, "fail fast" often means: don't optimistically update if the network call will fail. Or: don't render a half-loaded screen — show the error UI or the loading UI, not a jumble. Network errors are also offline-vs-server: distinguish them in the user-facing message ("You appear to be offline" vs. "Something went wrong on our end").

**Mini-task variant:**
Pick one error path in your mobile app. Verify it: (1) fails fast at the cause, (2) shows a user-friendly error message, (3) logs enough context for the on-call engineer, (4) does NOT log any PII, token, or secret. Fix any of the four that are missing. Commit `refactor(clean-code-4): error-handling`.

**Topic-specific video:**
- [Mobile Error Handling Best Practices — Antoine Van Der Lee (12 minutes)](https://www.youtube.com/watch?v=oEbFM1C5rhQ) — short, on the network vs. UI error pattern.

---

## Topic 5 — SOLID Principles (Core)

**Concept in this stack:** SOLID in the mobile codebase maps to *view-model and screen design*. S = one screen, one job (a `ProfileScreen` doesn't also do `CommentsScreen`). O = extend by composition or by adding a prop, not by editing the screen. L = substitutable view-models (any `ListItemViewModel` can be rendered by the same cell). I = small prop interfaces — if a screen takes 12 props, split it. D = inject dependencies (data sources, loggers, clocks) as constructor parameters, not by importing them inside the view-model.

**Mini-task variant:**
Pick the *worst-designed* screen in your codebase. Apply the SOLID principles to it, *one refactor per principle*, in five separate PRs. Title each `refactor(solid-N): <principle>`.

**Topic-specific video:**
- [SOLID Principles in Mobile — Caolan McMahon (10 minutes)](https://www.youtube.com/watch?v=5WHK6jFybWc) — short, framework-agnostic, applies SOLID to view-models.

---

## Topic 6 — Separation of Concerns (SoC)

**Concept in this stack:** A mobile screen should not also be the data fetcher, the business-logic container, and the layout. The cure: keep the *visual* concern in the screen, the *data* concern in a repository or data source, and the *business* logic in a view-model or use case.

The "thin screen" is the mobile equivalent of the "thin controller": the screen orchestrates, the view-model decides, the repository fetches. If your screen is more than ~100 lines (mobile screens tend to be larger than web components), it's probably doing more than one concern.

**Mini-task variant:**
Find a screen in your codebase with more than 100 lines. Extract the data-fetching into a repository / data source and the business logic into a view-model. The screen should become a thin orchestrator. Commit `refactor(soc): <screen-name>-to-thin`.

**Topic-specific video:**
- [MVVM Pattern in 100 Seconds — Fireship (2 minutes)](https://www.youtube.com/watch?v=T6NfllUt9XU) — short, on the screen / view-model / repository split.

---

## Topic 7 — Dependency Injection & Inversion of Control

**Concept in this stack:** In a mobile codebase, dependencies are usually the *data source* (a network client, a local database), the *navigation*, the *logger*, and the *clock* (`Date()` / `Instant.now()`). The pattern: pass them in via the constructor (or a DI framework the platform uses), don't construct them inside the view-model.

Frameworks have idioms: constructor injection, property injection, or a DI container. The principle is unchanged: the consumer doesn't construct the dependency.

**Mini-task variant:**
Find a view-model in your codebase that imports and creates a data source directly. Inject the data source as a constructor parameter. Write a unit test that uses a mock data source. Commit `refactor(di): inject-<dependency>`.

**Topic-specific video:**
- [Dependency Injection in Mobile — Antoine Van Der Lee (12 minutes)](https://www.youtube.com/watch?v=fF6LEV3vua4) — practical, framework-aware.

---

## Topic 8 — Reusability & Extensibility

**Concept in this stack:** Composition over inheritance — mobile code doesn't have a strong inheritance problem, but the *subclass explosion* is real (a `PrimaryButton extends Button`, a `SecondaryButton extends Button`, a `DestructiveButton extends Button` — all with copy-pasted styling overrides). The fix: a single `Button` view with a `style` parameter or a `ButtonStyle` value object.

Config-driven behavior: a feature flag, a config value, or a server-driven config is data. Don't add a new subclass for every new variation.

**Mini-task variant:**
Find a view hierarchy in your codebase with 3+ subclasses that share 80% of their code. Refactor one of them to composition. If the *only* difference is a config value, replace the subclass with a config flag. Commit `refactor(reuse): composition-over-inheritance`.

**Topic-specific video:**
- [Composition Over Inheritance — Fun Fun Function (8 minutes)](https://www.youtube.com/watch?v=wfF3W5KnfXA) — the canonical video on this pattern.

---

## Topic 9 — Design Thinking for Engineering

**Concept in this stack:** The "user" in a mobile codebase is more than the end user — it's the developer who will *use* the screen, the designer who will *theme* it, and the user who has a *small screen, a slow network, and a battery to conserve*. Change scenarios: "If we add a dark mode, what changes?" "If we add offline support, what changes?" "If the user is on a low-end device, what changes?" Variability points are the *config*, the *feature flags*, and the *device capabilities*. The stable part is the *core user flow*.

**Mini-task variant:**
Take your current ticket. Write 3 change scenarios in the form "if X, then Y" before writing any code. Open an ADR (use the master's Phase 7 format). Ask your reviewer: do these scenarios match the design, or does the design need to change? Commit `docs(design): change-scenarios-<ticket-id>`.

**Topic-specific video:**
- [Design Thinking for Mobile — Caolan McMahon (8 minutes)](https://www.youtube.com/watch?v=4u_K8L0e2sc) — short, applies the change-scenarios approach to mobile features.

---

## Topic 10 — Trade-off Analysis

**Concept in this stack:** The classic mobile trade-offs: native vs. cross-platform, on-device storage vs. server-only, push vs. poll for updates, eager vs. lazy loading of data, dark mode in v1 vs. v2, offline support in v1 vs. v2. None of these have a "right" answer; they have informed trade-offs.

The right discipline: write down the trade-off, defend it for 2 minutes, change it when the measurement says so. The master's 4-row trade-off table applies directly.

**Mini-task variant:**
Take the design decision in Topic 9's ADR. Add a "Trade-offs" section that names what you gave up. Push the PR; ask your reviewer to challenge any trade-off they think is wrong. If you can't defend it, change the design.

**Topic-specific video:**
- [Trade-off Analysis for Mobile Engineers — Antoine Van Der Lee (12 minutes)](https://www.youtube.com/watch?v=zS0l3knxQsU) — short, on the framework choice and feature-scope trade-offs.

---

## Topic 11 — Domain Modeling Basics

**Concept in this stack:** In a mobile codebase, the "model" is the type / class. An *entity* has identity and is mutable (`User { id, name, email }` — same user even when name changes). A *value object* has no identity and is defined by its values (`Address { street, city, zip }` — two addresses with the same fields are equal).

The "anemic model" in mobile code: a type that's just fields, with all the business logic in a separate utility file. The fix: put the rules on the type (or a thin class wrapping it).

**Mini-task variant:**
Find a type in your codebase that's anemic (just fields, business rules in utilities). Move one business rule from the utility onto the type. Commit `refactor(ddd): move-rule-onto-model`.

**Topic-specific video:**
- [Value Objects in Mobile — Khalil Stemmler (15 minutes)](https://www.youtube.com/watch?v=9MOGZ5Fiqs0) — practical, framework-agnostic.

---

## Topic 12 — RESTful API Design Principles

**Concept in this stack:** A mobile dev *consumes* the API, not designs it. The relevant discipline: be a *good* consumer. Know the HTTP methods and status codes (so a 401 means "log out," a 503 means "show a friendly retry later"). Know idempotency (so a retried POST doesn't double-create). Use the API's filter and sort conventions (the master cites the CoE standard).

**Mini-task variant:**
Pick one API your app calls. Review it for the five points in the master (predictability, methods/status codes, idempotency, pagination/filtering/sort, versioning). Open a doc PR (`docs(api-review): <endpoint>`) that lists each gap. Coordinate with the API owner before changing the consumer.

**Topic-specific video:**
- [REST API Design Best Practices — Hussein Nasser (15 minutes)](https://www.youtube.com/watch?v=rp1eH4jK1vE) — quick, applies the master's REST standards.

---

## Topic 13 — Validation & Boundary Protection

**Concept in this stack:** The "boundary" in a mobile codebase is *every input from the user* (form fields, URL params in a deep link, file uploads, drag-and-drop). The server is the last line of defense, but the client is the *first* — and a good first line catches most of the bad input before a round trip.

Validate at the boundary: a form handler validates the form, a deep-link router validates URL params, a file-upload handler validates the file. Re-validate on the server; never trust the client.

**Mini-task variant:**
Pick one form or input handler in your app. Audit: is the validation at the boundary? Is the same schema shared with the server? Open a doc PR (`docs(validation-audit): <form>`) listing the gaps.

**Topic-specific video:**
- [Form Validation in Mobile — Antoine Van Der Lee (15 minutes)](https://www.youtube.com/watch?v=6a2E9dB3YkA) — covers client + server validation, framework-aware.

---

## Topic 14 — Performance Awareness

**Concept in this stack:** The mobile "N+1" is a list of 100 cells that re-renders because one cell changed, or a screen that fetches related data item-by-item. The fix: lazy loading, cell reuse, virtualization (only render what's on screen), and stable references (don't create a new object identity on every render). The "caching basics" map to on-device caches (in-memory, on-disk, or both). The "measure-first" rule applies to the platform's profiler (Instruments, Android Profiler, or whichever the stack uses).

**Mini-task variant:**
Find one re-render or repeated fetch in your app that's measurably slow. Use the platform's profiler to confirm. Apply the fix (cell reuse / lazy loading / caching). Commit `perf(re-render): <screen-name>` with the before/after numbers in the PR description.

**Topic-specific video:**
- [Mobile Performance: 7 Steps to Fix Slow Screens — Antoine Van Der Lee (15 minutes)](https://www.youtube.com/watch?v=4iTJ7TpgDx0) — pragmatic, framework-aware, applies the measure-first rule.

---

## Topic 15 — Testing Fundamentals

**Concept in this stack:** Mobile has three layers of tests: *unit* (a function, a view-model), *integration* (a view-model with a mock data source), and *E2E* (a real device, a real user flow). The pyramid still applies: many unit, some integration, few E2E. The "what NOT to test" is the platform's rendering — trust the platform to draw a button; test the *behavior* your view-model adds.

**Mini-task variant:**
Write one unit test for a view-model you wrote in the last week. The test name should be a sentence. The body should be arrange/act/assert. Commit `test: <view-model-name>`.

**Topic-specific video:**
- [Mobile Testing Pyramid — Joe Birch (10 minutes)](https://www.youtube.com/watch?v=cRbD9dSpA60) — the canonical intro to the unit / integration / E2E split on mobile.

---

## Topic 16 — Writing Testable Code

**Concept in this stack:** A testable view-model takes its dependencies via the constructor (or DI), doesn't reach for `Date()` / `Instant.now()` inside the view-model body, and doesn't read from the platform's global state (`UserDefaults`, `SharedPreferences`, the global navigation). The "inject the clock" pattern: pass a `Clock` interface (or a function) instead of calling `Date()`. Hidden dependencies: the static `Logger`, the global `Database`, the global `NetworkClient`.

**Mini-task variant:**
Find a view-model in your codebase that uses `Date()` or a static logger. Inject the dependency. Write a unit test with a fixed time and a mock logger. Commit `refactor(testable): inject-<dependency>`.

**Topic-specific video:**
- [Mocking Strategies for Mobile Tests — Joe Birch (12 minutes)](https://www.youtube.com/watch?v=3ZPIYjrBkhg) — covers stubs vs. mocks in view-model tests.

---

## Topic 17 — Refactoring Techniques

**Concept in this stack:** Mobile refactors have their own decision rules: refactor a *screen* (extract sub-views, rename, split the view-model) when the names are right but the body is wrong; refactor a *type* (split a giant type, add a value object) when the same type is used in three places; rewrite a *screen* (throw out the file and start over) when the architecture doesn't fit the new requirement.

The Fowler smell catalog still applies: long method, large class, long parameter list, primitive obsession. In mobile code, "long parameter list" is often a "long constructor list" — same smell, same fix.

**Mini-task variant:**
Take a code smell from your mobile codebase. Refactor it in a single PR. The PR should be small enough to read in 10 minutes. The tests should be green before and after. Commit `refactor: <smell>`.

**Topic-specific video:**
- [Refactoring Mobile Code — Joe Birch (12 minutes)](https://www.youtube.com/watch?v=3sLSi9T5eQo) — applies the Fowler catalog to mobile code.

---

## Topic 18 — Effective Code Review Practices

**Concept in this stack:** A code review on a mobile PR is about *intent* (does this match the design?), *correctness* (does the data flow work?), *readability* (will the next mobile dev understand it?), and *device-specific concerns* (lifecycle, orientation changes, backgrounding, low memory, network state). Defer to the formatter. Be objective, not subjective.

The "questions not commands" rule applies especially to design decisions: "Could this be a child view?" is better than "Make this a child view."

**Mini-task variant:**
Review 5 PRs in the next week. For each PR, write at least one question (not a command) and at least one specific praise. After the week, reflect: did the tone work? What would you do differently?

**Topic-specific video:**
- [Code Review Best Practices — Google Engineering Practices (15 minutes)](https://www.youtube.com/watch?v=zlQzl2NHkhk) — the de-facto reference.

---

## Topic 19 — Code Review Checklist (Standardized)

**Concept in this stack:** The master's 9-point checklist applies, with mobile-specific rows: **Lifecycle** (the change handles viewDidLoad / onCreate / onAppear correctly), **State restoration** (the change handles backgrounding and rotation), **Network** (the change handles offline / slow network), **Permissions** (the change requests the right permissions at the right time), **Accessibility** (the change works for VoiceOver / TalkBack / large text). Use your platform's static analysis tool in CI to catch the easy stuff automatically.

**Mini-task variant:**
Pick 3 of your open PRs. Self-review them against the 9-point master checklist + the lifecycle / state / network / permissions / a11y rows. Open follow-up PRs for any gap. Reflect: which points did you consistently miss?

**Topic-specific video:**
- [Mobile Accessibility — Rob Whitaker (15 minutes)](https://www.youtube.com/watch?v=ckD6lxoYGN8) — short, framework-agnostic, on the a11y row.

---

## Topic 20 — Engineering Ethics & Ownership

**Concept in this stack:** A mobile dev owns the *user's experience on a small screen, a slow network, and a battery to conserve*. The principle: code is read more often than written, but a confusing button is a slow app, not just bad code. The same ownership principle: name the technical debt you create (e.g. "this screen will need offline support in v2"), and flag the debt you inherit.

**Mini-task variant:**
Find the oldest open TODO in your mobile codebase. Read it. Is it still relevant? If yes, file a ticket and link it; if no, close it. Commit `chore: review-todo-<module>`.

**Topic-specific video:**
- [The Ethics of Software Engineering — CodeAesthetic (12 minutes)](https://www.youtube.com/watch?v=BOfrJzgI7V0) — short, on-topic, framework-agnostic.

---

## Phase 7 — Senior Developer Mindset (Lead Track)

**Concept in this stack:** A mobile lead owns the *architecture* (app structure, state management, navigation, dependency injection, build pipeline) and the *mentoring* (helping junior devs write better screens and view-models). The ADRs a mobile lead writes tend to be about: framework choice, state-management library, navigation pattern, offline support, and device-test strategy. The Phase 7 reading list applies; the artifacts (3 ADRs, 1 architecture note, 1 backward-compat plan, 1 risk analysis, 1 mentoring reflection) are the same.

**Mini-task variant:**
Write one ADR for a real mobile architecture decision in your codebase. Use the master's Phase 7 format. Pair with a tech lead for review.

**Topic-specific video:**
- [How to Write a Good Mobile ADR — Caolan McMahon (12 minutes)](https://www.youtube.com/watch?v=kS1pZQLzJy0) — short, on the format and what to include.

---

## Document control

| Field | Value |
|---|---|
| Document | Mobile Stack Translation — Developer Excellence Curriculum |
| Version | 0.1 (initial — 20 topic translations + Phase 7) |
| Owner | CoE Web Working Group (with cross-team review from Mobile + Backend) |
| Review Cycle | Quarterly |
| Status | Draft for pilot-batch review |
| Related | [curriculum.md](../../curriculum.md), [frontend.md](../webdev/frontend.md), [backend.md](../webdev/backend.md) |
