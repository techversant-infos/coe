# Mobile Stack Translation Developer Excellence Curriculum

> **Audience:** Developers working on a **mobile** codebase.
> **Purpose:** Companion to the universal [Developer Excellence Curriculum](../../curriculum.md). For each of the 20 topics: *what changes in your stack, and what does the mini-task look like?*
> **Read alongside:** [curriculum.md](../../curriculum.md) (the universal master) + your team's stack-specific code-review checklist.
> **Status:** Draft for pilot-batch review v0.3.

---

## How to use this document

For each topic in the master curriculum, the section below has three short lines:

- **What changes in this stack** the diff from the master, *not* a restatement of the topic. If you read the master, this is the only new information you need.
- **Mini-task variant** the master's mini-task, rewritten for the mobile context.
- **Watch** one verified YouTube link (provided by your tech lead) on this exact topic. If the link is missing, search YouTube for the topic and pick a video under 15 minutes from a known channel.

---

## Topic 1 Clean Code Fundamentals

**What changes in this stack:** Naming is about *UI vocabulary* and *lifecycle*. A `ProductCardView` is a real concept the user sees. Variables hold UI state (`isOpen`, `selectedTabId`, `searchQuery`) and derived values. Methods are event handlers, lifecycle hooks, and navigation actions. Types/classes are nouns that match the design system or the screen.

**Mini-task variant:**
Pick a recent screen or view-model you wrote. Re-read it: *can a new mobile dev understand this without context?* Rename any unclear names. Extract any function doing two things. Open a follow-up PR tagged `refactor(clean-code-1): <your-name>`.

**Watch:** Search YouTube for "clean code functions Uncle Bob" pick a video under 10 min.

---

## Topic 2 Control Flow & Logic Clarity

**What changes in this stack:** Deeply nested control flow shows up as a view-model with three levels of business-rule nesting, or a deep navigation chain. Fix: early returns + guard clauses. Mobile-specific: lifecycle methods (`viewDidLoad`, `onCreate`, `onAppear`) are *also* control flow a deep lifecycle method is a smell. Extract lifecycle setup into private methods that each do one thing.

**Mini-task variant:**
Take the most deeply nested view-model or lifecycle method. Refactor using early returns + guard clauses. Commit `refactor(control-flow-2): <view-model-or-screen-name>`.

**Watch:** Search YouTube for "guard clauses early return" pick a video under 10 min.

---

## Topic 3 DRY vs. WET

**What changes in this stack:** Mobile's over-abstraction temptation is the "shared screen" that takes 12 props and has 8 conditional branches, or the "common view-model" that does five things. Rule of three still applies. A *good* mobile abstraction has a single visual identity (a button, an input, a card). A *bad* one is where you'd have to look at the call site to know what it looks like.

**Mini-task variant:**
Find a shared view or view-model in your codebase with 3+ consumers that has noticeably different shapes. Inline it back into the 3 call sites. Commit `refactor(clean-code-3): inline-over-abstraction`.

**Watch:** Search YouTube for "wrong abstraction Sandi Metz" pick the talk excerpt.

---

## Topic 4 Basic Error Handling

**What changes in this stack:** Two error surfaces the *user* (a friendly "We couldn't load that" message) and the *developer* (a structured log line with operation, cause, device context). "Fail fast" often means: don't optimistically update if the network call will fail; don't render a half-loaded screen. Mobile-specific: distinguish offline from server errors in the user-facing message ("You appear to be offline" vs. "Something went wrong on our end").

**Mini-task variant:**
Pick one error path in your app. Verify it: (1) fails fast at the cause, (2) shows a user-friendly message, (3) logs enough context for the on-call engineer, (4) does NOT log PII, tokens, or secrets. Fix any of the four that are missing. Commit `refactor(clean-code-4): error-handling`.

**Watch:** Search YouTube for "mobile error handling best practices" pick a 1015 min video.

---

## Topic 5 SOLID Principles (Core)

**What changes in this stack:** SOLID maps to *view-model and screen design*. S = one screen, one job. O = extend by composition or by adding a prop, not by editing. L = substitutable view-models (any `ListItemViewModel` rendered by the same cell). I = small prop interfaces split a 12-prop screen. D = inject dependencies as constructor parameters, don't `import` them inside the view-model.

**Mini-task variant:**
Pick the *worst-designed* screen in your codebase. Apply the SOLID principles, *one refactor per principle*, in five separate PRs. Title each `refactor(solid-N): <principle>`.

**Watch:** Search YouTube for "SOLID principles mobile" pick a video under 10 min.

---

## Topic 6 Separation of Concerns (SoC)

**What changes in this stack:** A screen should not also be the data fetcher, the business-logic container, and the layout. Cure: keep the *visual* concern in the screen, the *data* concern in a repository or data source, the *business* logic in a view-model or use case. The "thin screen" is the mobile equivalent of the "thin controller": orchestrates, doesn't decide. A screen over ~100 lines (mobile screens tend to be larger than web components) is doing more than one concern.

**Mini-task variant:**
Find a screen with more than 100 lines. Extract data-fetching into a repository / data source and business logic into a view-model. The screen should become a thin orchestrator. Commit `refactor(soc): <screen-name>-to-thin`.

**Watch:** Search YouTube for "MVVM pattern explained" pick a video under 10 min.

---

## Topic 7 Dependency Injection & IoC

**What changes in this stack:** Mobile dependencies are usually the *data source* (network client, local database), the *navigation*, the *logger*, and the *clock* (`Date()` / `Instant.now()`). Pass them in via constructor (or DI framework), don't construct them inside the view-model. Idioms: constructor injection, property injection, or a DI container. Principle unchanged.

**Mini-task variant:**
Find a view-model that imports and creates a data source directly. Inject the data source as a constructor parameter. Write a unit test that uses a mock data source. Commit `refactor(di): inject-<dependency>`.

**Watch:** Search YouTube for "dependency injection mobile" pick a 1015 min video.

---

## Topic 8 Reusability & Extensibility

**What changes in this stack:** Composition over inheritance mobile doesn't have a strong inheritance problem, but *subclass explosion* is real (PrimaryButton, SecondaryButton, DestructiveButton, all copy-pasted). Fix: a single `Button` with a `style` parameter or `ButtonStyle` value object. Config-driven behavior is data don't add a new subclass for every variation.

**Mini-task variant:**
Find a view hierarchy in your codebase with 3+ subclasses that share 80% of their code. Refactor one to composition. If the *only* difference is a config value, replace the subclass with a config flag. Commit `refactor(reuse): composition-over-inheritance`.

**Watch:** Search YouTube for "composition over inheritance" pick a video under 15 min.

---

## Topic 9 Design Thinking for Engineering

**What changes in this stack:** The "user" is more than the end user it's the developer who will *use* the screen, the designer who will *theme* it, and the user who has a *small screen, a slow network, and a battery to conserve*. Change scenarios: "If we add a dark mode, what changes?" "If we add offline support, what changes?" "If the user is on a low-end device, what changes?" Variability points = config, feature flags, device capabilities. Stable part = core user flow.

**Mini-task variant:**
Take your current ticket. Write 3 change scenarios in the form "if X, then Y" before writing any code. Open an ADR (use the master's Phase 7 format). Ask your reviewer: do these scenarios match the design, or does the design need to change? Commit `docs(design): change-scenarios-<ticket-id>`.

**Watch:** Search YouTube for "design thinking mobile engineering" pick a 510 min video.

---

## Topic 10 Trade-off Analysis

**What changes in this stack:** Classic mobile trade-offs: native vs. cross-platform, on-device storage vs. server-only, push vs. poll for updates, eager vs. lazy loading, dark mode in v1 vs. v2, offline support in v1 vs. v2. None of these have a "right" answer; they have informed trade-offs. Write it down, defend for 2 minutes, change when measurement says so.

**Mini-task variant:**
Take the design decision in Topic 9's ADR. Add a "Trade-offs" section that names what you gave up. Push the PR; ask your reviewer to challenge any trade-off they think is wrong. If you can't defend it, change the design.

**Watch:** Search YouTube for "trade-off analysis mobile" pick a 1015 min video.

---

## Topic 11 Domain Modeling Basics

**What changes in this stack:** The "model" is the type/class. Entity = has identity, is mutable (`User { id, name, email }`). Value object = no identity, defined by values (`Address { street, city, zip }`). Anemic model: a type that's just fields, with all the business logic in a separate utility. Fix: put the rules on the type (or a thin class wrapping it).

**Mini-task variant:**
Find a type in your codebase that's anemic (just fields, business rules in utilities). Move one business rule from the utility onto the type. Commit `refactor(ddd): move-rule-onto-model`.

**Watch:** Search YouTube for "value objects mobile" pick a 1015 min video.

---

## Topic 12 RESTful API Design Principles

**What changes in this stack:** A mobile dev *consumes* the API, not designs it. The discipline: be a *good* consumer. Know HTTP methods and status codes (a 401 means "log out," a 503 means "show a friendly retry later"). Know idempotency (so a retried POST doesn't double-create). Use the API's filter and sort conventions.

**Mini-task variant:**
Pick one API your app calls. Review it for the five points in the master. Open a doc PR (`docs(api-review): <endpoint>`) that lists each gap. Coordinate with the API owner before changing the consumer.

**Watch:** Search YouTube for "REST API design best practices" pick a 1015 min video.

---

## Topic 13 Validation & Boundary Protection

**What changes in this stack:** The "boundary" is *every input from the user* (form fields, URL params in a deep link, file uploads, drag-and-drop). The server is the last line of defense, but the client is the *first* a good first line catches most bad input before a round trip. Validate at the boundary: form handler validates the form, deep-link router validates URL params, file-upload handler validates the file. Re-validate on the server; never trust the client.

**Mini-task variant:**
Pick one form or input handler. Audit: is the validation at the boundary? Is the same schema shared with the server? Open a doc PR (`docs(validation-audit): <form>`) listing the gaps.

**Watch:** Search YouTube for "form validation mobile" pick a 1015 min video.

---

## Topic 14 Performance Awareness

**What changes in this stack:** The mobile "N+1" is a list of 100 cells that re-renders because one cell changed, or a screen that fetches related data item-by-item. Fix: lazy loading, cell reuse, virtualization (only render what's on screen), stable references. "Caching basics" map to on-device caches (in-memory, on-disk, or both). "Measure-first" applies to the platform's profiler (Instruments, Android Profiler, or whichever the stack uses).

**Mini-task variant:**
Find one re-render or repeated fetch that's measurably slow. Use the platform's profiler to confirm. Apply the fix (cell reuse / lazy loading / caching). Commit `perf(re-render): <screen-name>` with the before/after numbers in the PR description.

**Watch:** Search YouTube for "mobile performance optimization" pick a 1015 min video.

---

## Topic 15 Testing Fundamentals

**What changes in this stack:** Mobile has *unit* (a function, a view-model), *integration* (a view-model with a mock data source), and *E2E* (a real device, a real user flow). The pyramid still applies: many unit, some integration, few E2E. The "what NOT to test" is the platform's rendering trust the platform to draw a button; test the *behavior* your view-model adds.

**Mini-task variant:**
Write one unit test for a view-model you wrote in the last week. The test name should be a sentence. The body should be arrange/act/assert. Commit `test: <view-model-name>`.

**Watch:** Search YouTube for "mobile testing pyramid" pick a 510 min video.

---

## Topic 16 Writing Testable Code

**What changes in this stack:** A testable view-model takes its dependencies via constructor (or DI), doesn't reach for `Date()` / `Instant.now()` inside the view-model body, and doesn't read from the platform's global state (`UserDefaults`, `SharedPreferences`, global navigation). The "inject the clock" pattern: pass a `Clock` interface (or a function) instead of calling `Date()`. Hidden dependencies: static `Logger`, global `Database`, global `NetworkClient`.

**Mini-task variant:**
Find a view-model that uses `Date()` or a static logger. Inject the dependency. Write a unit test with a fixed time and a mock logger. Commit `refactor(testable): inject-<dependency>`.

**Watch:** Search YouTube for "mocking mobile tests" pick a 1015 min video.

---

## Topic 17 Refactoring Techniques

**What changes in this stack:** Mobile refactor decision rules: refactor a *screen* (extract sub-views, rename, split the view-model) when names are right but body is wrong; refactor a *type* (split a giant type, add a value object) when the same type is used in three places; rewrite a *screen* when architecture doesn't fit. Fowler smell catalog still applies: long method, large class, long parameter list, primitive obsession. In mobile code, "long parameter list" is often a "long constructor list" same smell, same fix.

**Mini-task variant:**
Take a code smell from your mobile codebase. Refactor it in a single PR. The PR should be small enough to read in 10 minutes. The tests should be green before and after. Commit `refactor: <smell>`.

**Watch:** Search YouTube for "refactoring mobile code" pick a 1015 min video.

---

## Topic 18 Effective Code Review Practices

**What changes in this stack:** A mobile PR review is about *intent* (matches design?), *correctness* (data flow works?), *readability* (next mobile dev understands?), and *device-specific concerns* (lifecycle, orientation changes, backgrounding, low memory, network state). Defer to the formatter. Be objective, not subjective. "Questions not commands" applies especially to design: "Could this be a child view?" is better than "Make this a child view."

**Mini-task variant:**
Review 5 PRs in the next week. For each PR, write at least one question (not a command) and at least one specific praise. After the week, reflect: did the tone work? What would you do differently?

**Watch:** Search YouTube for "code review best practices Google" pick a 1015 min video.

---

## Topic 19 Code Review Checklist (Standardized)

**What changes in this stack:** The master's 9-point checklist applies, with mobile-specific rows: **Lifecycle** (the change handles `viewDidLoad` / `onCreate` / `onAppear` correctly), **State restoration** (the change handles backgrounding and rotation), **Network** (the change handles offline / slow network), **Permissions** (the change requests the right permissions at the right time), **Accessibility** (the change works for VoiceOver / TalkBack / large text). Use the platform's static analysis tool in CI to catch the easy stuff automatically.

**Mini-task variant:**
Pick 3 of your open PRs. Self-review them against the 9-point master checklist + the lifecycle / state / network / permissions / a11y rows. Open follow-up PRs for any gap. Reflect: which points did you consistently miss?

**Watch:** Search YouTube for "mobile accessibility development" pick a 1015 min video.

---

## Topic 20 Engineering Ethics & Ownership

**What changes in this stack:** A mobile dev owns the *user's experience on a small screen, a slow network, and a battery to conserve*. Code is read more often than written, but a confusing button is a slow app, not just bad code. Same ownership principle: name the technical debt you create ("this screen will need offline support in v2"), flag the debt you inherit.

**Mini-task variant:**
Find the oldest open TODO in your mobile codebase. Read it. Is it still relevant? If yes, file a ticket and link it; if no, close it. Commit `chore: review-todo-<module>`.

**Watch:** Search YouTube for "ethics of software engineering" pick a 1015 min video.

---

## Phase 7 Senior Developer Mindset (Lead Track)

**What changes in this stack:** A mobile lead owns the *architecture* (app structure, state management, navigation, dependency injection, build pipeline) and the *mentoring* (helping junior devs write better screens and view-models). The ADRs a mobile lead writes tend to be about: framework choice, state-management library, navigation pattern, offline support, and device-test strategy. The Phase 7 reading list applies; the artifacts (3 ADRs, 1 architecture note, 1 backward-compat plan, 1 risk analysis, 1 mentoring reflection) are the same.

**Mini-task variant:**
Write one ADR for a real mobile architecture decision in your codebase. Use the master's Phase 7 format. Pair with a tech lead for review.

**Watch:** Search YouTube for "how to write ADR Michael Nygard" pick a 1015 min video.

---

## Document control

| Field | Value |
|---|---|
| Document | Mobile Stack Translation Developer Excellence Curriculum |
| Version | 0.3 (rewrote per-topic structure to 'What changes + Mini-task + Watch'; replaced unverified YouTube links with search hints) |
| Owner | CoE Web Working Group (with cross-team review from Mobile + Backend) |
| Review Cycle | Quarterly |
| Status | Draft for pilot-batch review |
| Related | [curriculum.md](../../curriculum.md), [frontend.md](../webdev/frontend.md), [backend.md](../webdev/backend.md) |
