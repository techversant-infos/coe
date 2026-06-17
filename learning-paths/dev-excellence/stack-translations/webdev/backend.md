# Backend Stack Translation — Developer Excellence Curriculum

> **Audience:** Developers working on a **backend** codebase (any server-side language or framework).
> **Purpose:** Companion to the universal [Developer Excellence Curriculum](../../curriculum.md). Each of the 20 topics below says: *what does this topic mean in a backend codebase, and what does the mini-task look like in your stack?*
> **Read alongside:** [curriculum.md](../../curriculum.md) (the universal master) + your team's stack-specific code-review checklist + the [REST API Best Practices](../../../../general/rest-api-best-practices.md) CoE standard.
> **Status:** Draft for pilot-batch review — v0.1.

---

## How to use this document

1. **For every topic in the master curriculum**, the section below has:
   - **Concept in this stack** — 2-3 lines on what the universal principle looks like in a backend codebase
   - **Mini-task variant** — the master's mini-task, rewritten for the backend context
   - **Topic-specific video** — one or two well-known videos that teach *exactly* this concept (not a channel — a specific video)
2. **Use the master's code-review focus questions** as-is — they're universal.
3. **Use the master's self-check** as-is — it's stack-agnostic by design.

The master says "controller with more than 20 lines." This document says "the entry point of the request — the route handler, controller, or resolver — whichever your framework uses, *that* file is the controller. Apply the same rule."

---

## Topic 1 — Clean Code Fundamentals

**Concept in this stack:** Naming conventions in a backend codebase are about the *domain*, not the framework. A `User` is a real concept; a `UserDTO` is the *transport* concept; a `UserEntity` is the *persistence* concept. Three different layers, three different names. The same user can be represented three times in three different files — and that's fine, because each representation is for a different audience.

Functions hold business operations (`calculateInvoiceTotal`, `reserveInventory`). Classes are domain nouns (`Invoice`, `Order`, `InventoryItem`). Constants are domain values (`MAX_LOGIN_ATTEMPTS`, `ORDER_GRACE_PERIOD_DAYS`).

**Mini-task variant:**
Pick a recent PR of yours. Re-read the diff with the focus question: *can a new backend dev understand this without context?* Rename any unclear names. Extract any function that does two things. Open a follow-up PR tagged `refactor(clean-code-1): <your-name>`.

**Topic-specific video:**
- [Clean Code — Uncle Bob / Functions (excerpt, 8 minutes)](https://www.youtube.com/watch?v=2X9NnJ4aIu0) — the canonical video on function size and naming.

---

## Topic 2 — Control Flow & Logic Clarity

**Concept in this stack:** The "deeply nested if-else" pattern in a backend codebase is a request handler with three levels of business-rule nesting. The fix is the same: early returns + guard clauses. But there's a backend-specific twist: business rules often have *many* valid paths (different user roles, different order states, different feature flags). The discipline is to extract the *happy path* and the *early guards* first, and let the special cases live below as named branches.

**Mini-task variant:**
Take the most deeply nested request handler in your current codebase. Refactor it using early returns + guard clauses. Commit `refactor(control-flow-2): <handler-name>`.

**Topic-specific video:**
- [Guard Clauses and the Happy Path — CodeAesthetic (4 minutes)](https://www.youtube.com/watch?v=EumXakNps08) — the canonical short video on this pattern.

---

## Topic 3 — DRY vs. WET

**Concept in this stack:** Backend has a strong temptation to over-abstract — the "base controller" that every controller extends, the "common service" that does five things, the "shared utility" that's been growing for two years. The rule of three still applies, and it's especially important in backend code: a wrong abstraction at the service layer is *expensive* to undo because every consumer inherits it.

A *good* abstraction in the backend has a single, clear domain responsibility. A *bad* abstraction is one where you'd have to scroll to the call site to know what it does.

**Mini-task variant:**
Find a piece of code in your backend that you suspect is *over-abstracted* — a helper with only one or two callers, with a signature that's harder to read than inlining. Inline it back. Commit `refactor(clean-code-3): inline-over-abstraction`. If the abstraction has three callers with genuinely shared semantics, write an ADR (Topic 9) explaining why you're keeping it.

**Topic-specific video:**
- [The Wrong Abstraction — Sandi Metz (excerpt, 5 minutes)](https://www.youtube.com/watch?v=LfPkgM2vXxw) — short, on-topic, the "wrong abstraction is worse than duplication" framing.

---

## Topic 4 — Basic Error Handling

**Concept in this stack:** Backend has two error surfaces: the *user* (a friendly "We couldn't save your changes" — the API's response) and the *developer* (a structured log line with the request id, the operation, the cause). The boundary between them is the same as the master: fail fast at the cause, surface user-friendly text, log the developer context.

In a backend codebase, "fail fast" often means: validate at the boundary, then *commit nothing* until the operation has succeeded. Or: don't half-write to the database — wrap the operation in a transaction.

**Mini-task variant:**
Pick one error path in your service. Verify it: (1) fails fast at the cause, (2) returns a user-friendly error response (per the [REST API Best Practices](../../../../general/rest-api-best-practices.md) error envelope), (3) logs enough context for the on-call engineer, (4) does NOT log any PII, token, or secret. Fix any of the four that are missing. Commit `refactor(clean-code-4): error-handling`.

**Topic-specific video:**
- [Structured Logging in Production — Honeypot (15 minutes)](https://www.youtube.com/watch?v=r-Tx5V3y3DY) — the canonical intro to structured logs (which is what your on-call engineer actually reads).

---

## Topic 5 — SOLID Principles (Core)

**Concept in this stack:** SOLID in the backend maps to *service design*. S = one service, one bounded responsibility (a `BillingService` doesn't also do shipping). O = extend by interface, not by editing the implementation. L = substitutable implementations (any `PaymentGateway` can be swapped without changing `OrderProcessor`). I = small interfaces (`Chargeable`, `Refundable`, `Reportable` instead of one giant `PaymentService`). D = inject the dependency as a constructor parameter; the consumer doesn't construct it.

**Mini-task variant:**
Pick the *worst-designed* service in your codebase. Apply the SOLID principles to it, *one refactor per principle*, in five separate PRs. Title each `refactor(solid-N): <principle>`.

**Topic-specific video:**
- [SOLID Principles in 100 Seconds — Fireship (2 minutes)](https://www.youtube.com/watch?v=5WHK6jFybWc) — quick refresher.
- [The Single Responsibility Principle — Uncle Bob (10 minutes)](https://www.youtube.com/watch?v=0vFkYpplApA) — the canonical video on SRP.

---

## Topic 6 — Separation of Concerns (SoC)

**Concept in this stack:** A backend service should not also be the HTTP handler, the business-logic container, the database access layer, and the email sender. The cure: keep the *transport* concern at the boundary (controller, route handler), the *business* concern in a service, the *persistence* concern in a repository, and the *side effects* (email, queue, log) in a dedicated dispatcher.

The "thin controller" rule: a route handler should orchestrate (parse the request, call the service, format the response). If your route handler is more than ~20 lines, it's probably doing more than one concern.

**Mini-task variant:**
Find a route handler in your codebase with more than 20 lines. Extract the business logic into a service. The route handler should become a thin orchestrator. Commit `refactor(soc): <route-name>-to-thin`.

**Topic-specific video:**
- [Layered Architecture in 100 Seconds — Fireship (2 minutes)](https://www.youtube.com/watch?v=T6NfllUt9XU) — short, on the controller / service / repository split.

---

## Topic 7 — Dependency Injection & Inversion of Control

**Concept in this stack:** In a backend codebase, dependencies are usually the *database*, the *cache*, the *message queue*, the *external API client*, the *clock* (`Date.now()`), and the *logger*. The pattern: pass them in via the constructor (or a DI container), don't `new` them inside the service.

A "composition root" is the one place in the app where everything is wired together. Don't sprinkle `new` calls across the codebase. The test: if you can replace a dependency with a mock without editing the consuming class, the DI is right.

**Mini-task variant:**
Find a service in your codebase that constructs its own dependencies. Inject them via the constructor (or register them in your DI container). Write one unit test that uses a mock dependency. Commit `refactor(di): inject-<dependency>`.

**Topic-specific video:**
- [What is Dependency Injection? — Web Dev Simplified (8 minutes)](https://www.youtube.com/watch?v=RsEZAX4-kdI) — the canonical intro, framework-agnostic.

---

## Topic 8 — Reusability & Extensibility

**Concept in this stack:** Composition over inheritance — backend code rarely has a strong inheritance problem, but the *subclass explosion* is a real smell (a `GoldUser extends User`, a `PlatinumUser extends User`, a `BetaUser extends User` — all with copy-pasted overrides). The fix: a `User` with a `Tier` value object, and a service that dispatches on tier.

Config-driven behavior: a feature flag, a config value, or a database lookup is data. Don't add a new subclass for every new variation.

**Mini-task variant:**
Find a class hierarchy in your codebase with 3+ subclasses that share 80% of their code. Refactor one of them to composition. If the *only* difference is a config value, replace the subclass with a config flag. Commit `refactor(reuse): composition-over-inheritance`.

**Topic-specific video:**
- [Composition Over Inheritance — Fun Fun Function (8 minutes)](https://www.youtube.com/watch?v=wfF3W5KnfXA) — the canonical video on this pattern.

---

## Topic 9 — Design Thinking for Engineering

**Concept in this stack:** The "user" in a backend codebase is more than the end user — it's the *caller* of the service (another service, a script, the frontend), the *operator* (the on-call engineer), and the *auditor* (security, compliance). Change scenarios: "If we add a new tenant, what changes?" "If we move the database, what changes?" "If we add a new payment provider, what changes?" Variability points are the *config*, the *DI bindings*, and the *external API clients*. The stable part is the *domain logic*.

**Mini-task variant:**
Take your current ticket. Write 3 change scenarios in the form "if X, then Y" before writing any code. Open an ADR (use the master's Phase 7 format). Ask your reviewer: do these scenarios match the design, or does the design need to change? Commit `docs(design): change-scenarios-<ticket-id>`.

**Topic-specific video:**
- [Domain Modeling — Eric Evans (excerpt, 8 minutes)](https://www.youtube.com/watch?v=pU2OB9DHIu4) — the canonical video on the change-scenarios approach.

---

## Topic 10 — Trade-off Analysis

**Concept in this stack:** The classic backend trade-offs: consistency vs. availability (CAP), read-your-writes vs. eventual consistency, sync vs. async (queue now, or return immediately), denormalization vs. joins, microservices vs. monolith. None of these have a "right" answer; they have informed trade-offs.

The right discipline: write down the trade-off, defend it for 2 minutes, change it when the measurement says so. The master's 4-row trade-off table applies directly.

**Mini-task variant:**
Take the design decision in Topic 9's ADR. Add a "Trade-offs" section that names what you gave up. Push the PR; ask your reviewer to challenge any trade-off they think is wrong. If you can't defend it, change the design.

**Topic-specific video:**
- [CAP Theorem in 100 Seconds — Fireship (2 minutes)](https://www.youtube.com/watch?v=f1S6hIBJ3Wk) — quick refresher on the consistency / availability trade-off.

---

## Topic 11 — Domain Modeling Basics

**Concept in this stack:** In a backend codebase, the *model* is the domain entity (`Order`, `User`, `Invoice`). An *entity* has identity and is mutable (`Order #1234` is the same order even when its total changes). A *value object* has no identity and is defined by its values (`Address(street, city, zip)` — two addresses with the same fields are equal).

The "anemic model" in backend code: a class that's just getters and setters, with the business rules in a separate service. The fix: move the rules onto the model.

**Mini-task variant:**
Find a class in your backend that's anemic (just getters/setters, business rules in services). Move one business rule from the service onto the model. Commit `refactor(ddd): move-rule-onto-model`.

**Topic-specific video:**
- [Anemic Domain Model — Khalil Stemmler (15 minutes)](https://www.youtube.com/watch?v=lkIFFw4tfcc) — the canonical video on the smell + the fix.

---

## Topic 12 — RESTful API Design Principles

**Concept in this stack:** A backend dev *designs* the API (or consumes an external one). The relevant discipline: be predictable, use the right HTTP methods and status codes, support idempotency for retried POSTs, paginate and filter consistently, and version deliberately. The master cites the [REST API Best Practices](../../../../general/rest-api-best-practices.md) CoE standard — that's the source of truth for our internal APIs.

**Mini-task variant:**
Pick one API endpoint you own. Review it for the five points in the master (predictability, methods/status codes, idempotency, pagination/filtering/sort, versioning). Open a doc PR (`docs(api-review): <endpoint>`) that lists each gap. Coordinate with consumers before changing the contract.

**Topic-specific video:**
- [REST API Design Best Practices — Hussein Nasser (15 minutes)](https://www.youtube.com/watch?v=rp1eH4jK1vE) — quick, applies the master's REST standards.

---

## Topic 13 — Validation & Boundary Protection

**Concept in this stack:** The "boundary" in a backend codebase is *every input from outside* (HTTP request, message-queue payload, scheduled-job argument, file upload). The server is the last line of defense. Validate at the boundary: the request handler / route handler validates the input, the service assumes validated input, the repository assumes a known entity.

Re-validate on the server; never trust the client. Use parameterized queries for any database access — never concatenate. The master links to your language's standards doc for the specifics.

**Mini-task variant:**
Pick one route handler in your codebase. Audit the inputs: are they all validated? Is the validation at the boundary? Is the same schema shared with the client? Open a doc PR (`docs(validation-audit): <endpoint>`) listing the gaps.

**Topic-specific video:**
- [Input Validation in Web APIs — Hussein Nasser (12 minutes)](https://www.youtube.com/watch?v=Ap8m3YDDHPA) — covers the boundary pattern, framework-agnostic.

---

## Topic 14 — Performance Awareness

**Concept in this stack:** The backend "N+1" is a loop that fetches related data one-by-one. The "caching basics" map to your cache layer (Redis, Memcached, or in-process). The "measure-first" rule applies to your profiler (whatever the stack uses) and to the APM (Application Performance Monitoring) — Vercel Analytics, New Relic, Datadog, Prometheus, or whichever the team uses.

**Mini-task variant:**
Find one N+1 query in your codebase. Eager-load it. Compare the query count before and after. Commit `perf(n+1): <module>` with the before/after numbers in the PR description.

**Topic-specific video:**
- [N+1 Query Problem — Hussein Nasser (8 minutes)](https://www.youtube.com/watch?v=fA7Ah8RBKRo) — the canonical short video on the smell + the fix.

---

## Topic 15 — Testing Fundamentals

**Concept in this stack:** Backend has three layers of tests: *unit* (a function, a service), *integration* (a service with a real database, a real queue), and *E2E* (the full HTTP stack with a real server). The pyramid still applies: many unit, some integration, few E2E. The "what NOT to test" is the framework's routing — trust the framework to route a request; test the *behavior* your service adds.

**Mini-task variant:**
Write one unit test for a function you wrote in the last week. The test name should be a sentence. The body should be arrange/act/assert. Commit `test: <function-name>`.

**Topic-specific video:**
- [Test Pyramid — Google Testing Blog (8 minutes, talk excerpt)](https://www.youtube.com/watch?v=f6PGJJrHHf8) — the canonical intro to the unit / integration / E2E split.

---

## Topic 16 — Writing Testable Code

**Concept in this stack:** A testable service takes its dependencies via the constructor (or DI), doesn't reach for `Date.now()` or `Math.random()` inside the service body, and doesn't read environment variables directly (inject the config). The "inject the clock" pattern: pass a `Clock` interface (or a `time.Now()` function) instead of calling `Date.now()`. Hidden dependencies: the global state, the static `Logger`, the static `HttpClient`.

**Mini-task variant:**
Find a service in your codebase that uses `Date.now()` or a static logger. Inject the dependency. Write a unit test with a fixed time and a mock logger. Commit `refactor(testable): inject-<dependency>`.

**Topic-specific video:**
- [Unit Testing Best Practices — Web Dev Simplified (10 minutes)](https://www.youtube.com/watch?v=HYrXogv7xkk) — the canonical intro, framework-agnostic.

---

## Topic 17 — Refactoring Techniques

**Concept in this stack:** Backend refactors have their own decision rules: refactor a *service* (extract a method, rename, split into two services) when the names are right but the body is wrong; refactor a *type* (split a giant type, add a value object) when the same type is used in three places; rewrite a *module* (throw out the file and start over) when the architecture doesn't fit the new requirement.

The Fowler smell catalog still applies: long method, large class, long parameter list, primitive obsession. The "names vs. bodies" test: if the names are right, refactor; if the names are wrong, rewrite.

**Mini-task variant:**
Take a code smell from your backend codebase. Refactor it in a single PR. The PR should be small enough to read in 10 minutes. The tests should be green before and after. Commit `refactor: <smell>`.

**Topic-specific video:**
- [Refactoring: Improving the Design of Existing Code — Martin Fowler (excerpt, 10 minutes)](https://www.youtube.com/watch?v=_T6diCXMpL4) — the canonical intro to the catalog.

---

## Topic 18 — Effective Code Review Practices

**Concept in this stack:** A code review on a backend PR is about *intent* (does this match the design?), *correctness* (does the data flow work?), *readability* (will the next backend dev understand it?), and *security* (input validation, parameterized queries, auth checks). Defer to the formatter. Be objective, not subjective.

The "questions not commands" rule applies especially to design decisions: "Could this be an interface?" is better than "Make this an interface."

**Mini-task variant:**
Review 5 PRs in the next week. For each PR, write at least one question (not a command) and at least one specific praise. After the week, reflect: did the tone work? What would you do differently?

**Topic-specific video:**
- [Code Review Best Practices — Google Engineering Practices (15 minutes)](https://www.youtube.com/watch?v=zlQzl2NHkhk) — the de-facto reference.

---

## Topic 19 — Code Review Checklist (Standardized)

**Concept in this stack:** The master's 9-point checklist applies, with backend-specific rows: **Database access** (parameterized queries, no N+1, proper indexing), **API contract** (the [REST API Best Practices](../../../../general/rest-api-best-practices.md) standards), **Auth/AuthZ** (the right user is doing the right action — see the [Security Audit Checklist](../../../../audit/security-audit-checklist.md)). Use your framework's static analysis tool (PHPStan, ESLint, etc.) in CI to catch the easy stuff automatically.

**Mini-task variant:**
Pick 3 of your open PRs. Self-review them against the 9-point master checklist + the database / API / auth rows. Open follow-up PRs for any gap. Reflect: which points did you consistently miss?

**Topic-specific video:**
- [OWASP Top 10 — Dave Kennedy / various (varies)](https://www.youtube.com/watch?v=rWHx4vKoh7g) — quick, on the security rows.

---

## Topic 20 — Engineering Ethics & Ownership

**Concept in this stack:** A backend dev owns the *data integrity* and the *security boundary*. The principle: code is read more often than written, but a misnamed column or a missing auth check is a production incident, not just bad code. The same ownership principle: name the technical debt you create (e.g. "this query will need an index in v2"), and flag the debt you inherit.

**Mini-task variant:**
Find the oldest open TODO in your backend codebase. Read it. Is it still relevant? If yes, file a ticket and link it; if no, close it. Commit `chore: review-todo-<module>`.

**Topic-specific video:**
- [Technical Debt Is Not a Bug — A Philosophy of Software (15 minutes)](https://www.youtube.com/watch?v=pqeJzpTMFRA) — short, on the "debt is a deliberate trade-off" framing.

---

## Phase 7 — Senior Developer Mindset (Lead Track)

**Concept in this stack:** A backend lead owns the *architecture* (service boundaries, data model, deployment topology, observability) and the *mentoring* (helping junior devs design better services). The ADRs a backend lead writes tend to be about: service decomposition, data-model migrations, API version strategies, and observability choices. The Phase 7 reading list applies; the artifacts (3 ADRs, 1 architecture note, 1 backward-compat plan, 1 risk analysis, 1 mentoring reflection) are the same.

**Mini-task variant:**
Write one ADR for a real backend architecture decision in your codebase. Use the master's Phase 7 format. Pair with a tech lead for review.

**Topic-specific video:**
- [How to Write a Good ADR — Michael Nygard / various (varies)](https://www.youtube.com/watch?v=kS1pZQLzJy0) — short, on the format and what to include.

---

## Document control

| Field | Value |
|---|---|
| Document | Backend Stack Translation — Developer Excellence Curriculum |
| Version | 0.1 (initial — 20 topic translations + Phase 7) |
| Owner | CoE Web Working Group (with cross-team review from Mobile + Backend) |
| Review Cycle | Quarterly |
| Status | Draft for pilot-batch review |
| Related | [curriculum.md](../../curriculum.md), [frontend.md](./frontend.md), [mobile stacks](../mobile/stacks.md), [REST API Best Practices](../../../../general/rest-api-best-practices.md), [Security Audit Checklist](../../../../audit/security-audit-checklist.md) |
