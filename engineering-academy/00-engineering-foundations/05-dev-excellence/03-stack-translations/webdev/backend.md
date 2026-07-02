# Backend Stack Translation Developer Excellence Curriculum

> **Audience:** Developers working on a **backend** codebase.
> **Purpose:** Companion to the universal [Developer Excellence Curriculum](../../01-curriculum.md). For each of the 20 topics: *what changes in your stack, and what does the mini-task look like?*
> **Read alongside:** [01-curriculum.md](../../01-curriculum.md) (the universal master) + your team's stack-specific code-review checklist + the [REST API Best Practices](../../../../../general/rest-api-best-practices.md) CoE standard.
> **Status:** Draft for pilot-batch review v0.3.

---

## How to use this document

For each topic in the master curriculum, the section below has three short lines:

- **What changes in this stack** the diff from the master, *not* a restatement of the topic. If you read the master, this is the only new information you need.
- **Mini-task variant** the master's mini-task, rewritten for the backend context.
- **Watch** one verified YouTube link (provided by your tech lead) on this exact topic. If the link is missing, search YouTube for the topic and pick a video under 15 minutes from a known channel.

---

## Topic 1 Clean Code Fundamentals

**What changes in this stack:** A backend codebase has three layers of names domain (`User`), transport (`UserDTO`), and persistence (`UserEntity`). The same user can be represented three times in three files. That's not duplication; each name is for a different audience (business logic, API contract, database).

**Mini-task variant:**
Pick a recent PR of yours. Re-read the diff: *can a new backend dev understand this without context?* Rename any unclear names. Extract any function that does two things. Open a follow-up PR tagged `refactor(clean-code-1): <your-name>`.

**Watch:** [What is clean code? - Uncle Bob](https://www.youtube.com/watch?v=F9owUy1g_YE)

---

## Topic 2 Control Flow & Logic Clarity

**What changes in this stack:** Backend code has request handlers with three levels of business-rule nesting (different user roles, order states, feature flags). The discipline: extract the *happy path* and *early guards* first, let the special cases live below as named branches.

**Mini-task variant:**
Take the most deeply nested request handler in your current codebase. Refactor it using early returns + guard clauses. Commit `refactor(control-flow-2): <handler-name>`.

**Watch:** [Guard Clauses Make Your Code 10x Cleaner](https://www.youtube.com/watch?v=Jf0NdoqRMiw)

---

## Topic 3 DRY vs. WET

**What changes in this stack:** Backend has a strong over-abstraction temptation (the "base controller" or "common service" that does five things). A wrong abstraction at the service layer is *expensive* to undo because every consumer inherits it. The rule of three still applies, and it's especially important in backend code.

**Mini-task variant:**
Find a piece of backend code you suspect is *over-abstracted* a helper with only one or two callers, with a signature that's harder to read than inlining. Inline it back. Commit `refactor(clean-code-3): inline-over-abstraction`.

**Watch:** Search YouTube for "wrong abstraction Sandi Metz" pick the talk excerpt.

---

## Topic 4 Basic Error Handling

**What changes in this stack:** Two error surfaces the *user* (a friendly API response) and the *developer* (a structured log line with request id, operation, cause). Backend-specific: "fail fast" often means wrap the operation in a transaction so you never half-write to the database. Distinguish offline from server errors in the log (different on-call actions).

**Mini-task variant:**
Pick one error path in your service. Verify it: (1) fails fast at the cause, (2) returns a user-friendly error response per the [REST API Best Practices](../../../../../general/rest-api-best-practices.md) error envelope, (3) logs enough context for the on-call engineer, (4) does NOT log PII, tokens, or secrets. Fix any of the four that are missing. Commit `refactor(clean-code-4): error-handling`.

**Watch:** Search YouTube for "structured logging backend production" pick a 1015 min video.

---

## Topic 5 SOLID Principles (Core)

**What changes in this stack:** SOLID maps to *service design*. S = one service, one bounded responsibility. O = extend by interface, not by editing. L = substitutable implementations. I = small interfaces (split a 12-method interface). D = inject dependencies via constructor, don't `new` them inside the service.

**Mini-task variant:**
Pick the *worst-designed* service in your codebase. Apply the SOLID principles, *one refactor per principle*, in five separate PRs. Title each `refactor(solid-N): <principle>`.

**Watch:** [SOLID Principles: Do You Really Understand Them?](https://www.youtube.com/watch?v=kF7rQmSRlq0)

---

## Topic 6 Separation of Concerns (SoC)

**What changes in this stack:** A service should not also be the HTTP handler, the business-logic container, the database access layer, and the email sender. Cure: keep transport at the boundary (route handler), business in a service, persistence in a repository, side effects (email, queue, log) in a dedicated dispatcher. A route handler over ~20 lines is doing more than one concern.

**Mini-task variant:**
Find a route handler in your codebase with more than 20 lines. Extract the business logic into a service. The route handler should become a thin orchestrator. Commit `refactor(soc): <route-name>-to-thin`.

**Watch:** [Separation of Concerns](https://www.youtube.com/watch?v=VtF6aebWe58)

---

## Topic 7 Dependency Injection & IoC

**What changes in this stack:** Backend dependencies are usually the *database*, *cache*, *message queue*, *external API client*, *clock* (`Date.now()`), and *logger*. Pass them in via constructor (or DI container). Composition root = the one place in the app where everything is wired. Don't sprinkle `new` across the codebase.

**Mini-task variant:**
Find a service that constructs its own dependencies. Inject them via constructor (or register them in your DI container). Write one unit test that uses a mock dependency. Commit `refactor(di): inject-<dependency>`.

**Watch:** [Dependency Injection in a Nutshell](https://www.youtube.com/watch?v=yunF2PgJlHU)

---

## Topic 8 Reusability & Extensibility

**What changes in this stack:** Backend's subclass explosion (GoldUser, PlatinumUser, BetaUser, all copy-pasted) is the same problem as the frontend's prop explosion. The fix: a `User` with a `Tier` value object, and a service that dispatches on tier. Config-driven behavior is data don't add a new subclass for every variation.

**Mini-task variant:**
Find a class hierarchy in your codebase with 3+ subclasses that share 80% of their code. Refactor one of them to composition. If the *only* difference is a config value, replace the subclass with a config flag. Commit `refactor(reuse): composition-over-inheritance`.

**Watch:** [Composition Over Inheritance](https://www.youtube.com/watch?v=EqHX7DAL0Jk)

---

## Topic 9 Design Thinking for Engineering

**What changes in this stack:** The "user" in a backend codebase is more than the end user it's the *caller* of the service (another service, a script, the frontend), the *operator* (the on-call engineer), and the *auditor* (security, compliance). Change scenarios: "If we add a new tenant, what changes?" "If we move the database, what changes?" "If we add a new payment provider, what changes?" Variability points = config, DI bindings, external API clients. Stable part = domain logic.

**Mini-task variant:**
Take your current ticket. Write 3 change scenarios in the form "if X, then Y" before writing any code. Open an ADR (use the master's Phase 7 format). Ask your reviewer: do these scenarios match the design, or does the design need to change? Commit `docs(design): change-scenarios-<ticket-id>`.

**Watch:** Search YouTube for "domain modeling change scenarios" pick a 1020 min video.

---

## Topic 10 Trade-off Analysis

**What changes in this stack:** Classic backend trade-offs: consistency vs. availability (CAP), read-your-writes vs. eventual consistency, sync vs. async (queue now, or return immediately), denormalization vs. joins, microservices vs. monolith. None of these have a "right" answer; they have informed trade-offs. Write down the trade-off, defend it for 2 minutes, change it when the measurement says so.

**Mini-task variant:**
Take the design decision in Topic 9's ADR. Add a "Trade-offs" section that names what you gave up. Push the PR; ask your reviewer to challenge any trade-off they think is wrong. If you can't defend it, change the design.

**Watch:** [CAP Theorem Explained](https://www.youtube.com/watch?v=BHqjEjzAicA)

---

## Topic 11 Domain Modeling Basics

**What changes in this stack:** In a backend codebase, the *model* is the domain entity (`Order`, `User`, `Invoice`). Entity = has identity, is mutable. Value object = no identity, defined by values (`Address(street, city, zip)`). The anemic model: a class that's just getters/setters, with business rules in a separate service. Fix: move the rules onto the model.

**Mini-task variant:**
Find a class in your backend that's anemic (just getters/setters, business rules in services). Move one business rule from the service onto the model. Commit `refactor(ddd): move-rule-onto-model`.

**Watch:** Search YouTube for "anemic domain model" pick a 1015 min video.

---

## Topic 12 RESTful API Design Principles

**What changes in this stack:** A backend dev *designs* the API (or consumes an external one). The discipline: be predictable, use the right HTTP methods and status codes, support idempotency for retried POSTs, paginate and filter consistently, version deliberately. The master cites the [REST API Best Practices](../../../../../general/rest-api-best-practices.md) that's the source of truth for our internal APIs.

**Mini-task variant:**
Pick one API endpoint you own. Review it for the five points in the master (predictability, methods/status codes, idempotency, pagination/filtering/sort, versioning). Open a doc PR (`docs(api-review): <endpoint>`) that lists each gap. Coordinate with consumers before changing the contract.

**Watch:** Search YouTube for "REST API design best practices" pick a 1015 min video.

---

## Topic 13 Validation & Boundary Protection

**What changes in this stack:** The "boundary" is *every input from outside* (HTTP request, message-queue payload, scheduled-job argument, file upload). The server is the last line of defense. Validate at the boundary: the request handler validates, the service assumes validated input, the repository assumes a known entity. Use parameterized queries never concatenate.

**Mini-task variant:**
Pick one route handler. Audit the inputs: are they all validated? Is the validation at the boundary? Is the same schema shared with the client? Open a doc PR (`docs(validation-audit): <endpoint>`) listing the gaps.

**Watch:** Search YouTube for "input validation web API security" pick a 1015 min video.

---

## Topic 14 Performance Awareness

**What changes in this stack:** The backend "N+1" is a loop that fetches related data one-by-one. "Caching basics" map to your cache layer. "Measure-first" applies to your profiler and APM (Datadog, New Relic, Prometheus, or whichever the team uses). For backend, the *fix* for an N+1 is almost always an eager-load or a join but the *diagnosis* requires measuring.

**Mini-task variant:**
Find one N+1 query in your codebase. Eager-load it. Compare the query count before and after. Commit `perf(n+1): <module>` with the before/after numbers in the PR description.

**Watch:** [N+1 Query Problem Explained](https://www.youtube.com/shorts/3w2g50NojVQ)

---

## Topic 15 Testing Fundamentals

**What changes in this stack:** Backend has *unit* (a function, a service), *integration* (a service with a real database, real queue), and *E2E* (the full HTTP stack with a real server). The pyramid still applies: many unit, some integration, few E2E. The "what NOT to test" is the framework's routing trust the framework; test the *behavior* your service adds.

**Mini-task variant:**
Write one unit test for a function you wrote in the last week. The test name should be a sentence. The body should be arrange/act/assert. Commit `test: <function-name>`.

**Watch:** [Test Pyramid](https://www.youtube.com/watch?v=Re4anDcHSwA)

---

## Topic 16 Writing Testable Code

**What changes in this stack:** A testable service takes its dependencies via constructor (or DI), doesn't reach for `Date.now()` or `Math.random()` inside the service body, and doesn't read environment variables directly (inject the config). The "inject the clock" pattern: pass a `Clock` interface or `time.Now()` function instead of calling `Date.now()`.

**Mini-task variant:**
Find a service that uses `Date.now()` or a static logger. Inject the dependency. Write a unit test with a fixed time and a mock logger. Commit `refactor(testable): inject-<dependency>`.

**Watch:** Search YouTube for "writing testable code dependency injection" pick a 1015 min video.

---

## Topic 17 Refactoring Techniques

**What changes in this stack:** Backend refactor decision rules refactor a *service* (extract method, rename, split into two) when names are right but body is wrong; refactor a *type* (split, add a value object) when the same type is used in three places; rewrite a *module* when architecture doesn't fit. Fowler smell catalog applies: long method, large class, long parameter list, primitive obsession. "Names vs. bodies" test: if names are right, refactor; if names are wrong, rewrite.

**Mini-task variant:**
Take a code smell from your backend codebase. Refactor it in a single PR. The PR should be small enough to read in 10 minutes. The tests should be green before and after. Commit `refactor: <smell>`.

**Watch:** Search YouTube for "refactoring Martin Fowler catalog" pick a 1015 min video.

---

## Topic 18 Effective Code Review Practices

**What changes in this stack:** A backend code review is about *intent* (matches design?), *correctness* (data flow works?), *readability* (next dev understands?), and *security* (input validation, parameterized queries, auth checks). Defer to the formatter. Be objective, not subjective. "Questions not commands" applies especially to design: "Could this be an interface?" is better than "Make this an interface."

**Mini-task variant:**
Review 5 PRs in the next week. For each PR, write at least one question (not a command) and at least one specific praise. After the week, reflect: did the tone work? What would you do differently?

**Watch:** [Code Review Best Practices](https://www.youtube.com/watch?v=1Ge__2Yx_XQ)

---

## Topic 19 Code Review Checklist (Standardized)

**What changes in this stack:** The master's 9-point checklist applies, with backend-specific rows: **Database access** (parameterized queries, no N+1, proper indexing), **API contract** (the [REST API Best Practices](../../../../../general/rest-api-best-practices.md) standards), **Auth/AuthZ** (the right user is doing the right action see the [Security Audit Checklist](../../../../../audit/security-audit-checklist.md)). Use your framework's static analysis tool (PHPStan, ESLint, etc.) in CI to catch the easy stuff automatically.

**Mini-task variant:**
Pick 3 of your open PRs. Self-review them against the 9-point master checklist + the database / API / auth rows. Open follow-up PRs for any gap. Reflect: which points did you consistently miss?

**Watch:** [OWASP Top 10 Overview](https://www.youtube.com/watch?v=Jzr0Jdnq_EI)

---

## Topic 20 Engineering Ethics & Ownership

**What changes in this stack:** A backend dev owns the *data integrity* and the *security boundary*. Code is read more often than written, but a misnamed column or a missing auth check is a production incident, not just bad code. Same ownership principle: name the technical debt you create ("this query will need an index in v2"), flag the debt you inherit.

**Mini-task variant:**
Find the oldest open TODO in your backend codebase. Read it. Is it still relevant? If yes, file a ticket and link it; if no, close it. Commit `chore: review-todo-<module>`.

**Watch:** Search YouTube for "technical debt management" pick a 1015 min video.

---

## Phase 7 Senior Developer Mindset (Lead Track)

**What changes in this stack:** A backend lead owns the *architecture* (service boundaries, data model, deployment topology, observability) and the *mentoring* (helping junior devs design better services). The ADRs a backend lead writes tend to be about: service decomposition, data-model migrations, API version strategies, and observability choices. The Phase 7 reading list applies; the artifacts (3 ADRs, 1 architecture note, 1 backward-compat plan, 1 risk analysis, 1 mentoring reflection) are the same.

**Mini-task variant:**
Write one ADR for a real backend architecture decision in your codebase. Use the master's Phase 7 format. Pair with a tech lead for review.

**Watch:** Search YouTube for "how to write ADR Michael Nygard" pick a 1015 min video.

---

## Document control

| Field | Value |
|---|---|
| Document | Backend Stack Translation Developer Excellence Curriculum |
| Version | 0.3 (rewrote per-topic structure to 'What changes + Mini-task + Watch'; 11 of 21 YouTube links verified by tech lead topics 1, 2, 5, 6, 7, 8, 10, 14, 15, 18, 19; the rest remain search hints pending verification) |
| Owner | CoE Web Working Group (with cross-team review from Mobile + Backend) |
| Review Cycle | Quarterly |
| Status | Draft for pilot-batch review |
| Related | [01-curriculum.md](../../01-curriculum.md), [frontend.md](./frontend.md), [mobile stacks](../mobile/stacks.md), [REST API Best Practices](../../../../../general/rest-api-best-practices.md), [Security Audit Checklist](../../../../../audit/security-audit-checklist.md) |
