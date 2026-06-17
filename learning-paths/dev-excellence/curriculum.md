# Developer Excellence Curriculum

> **Objective:** Build developers who write **clean, maintainable, testable, and scalable code** using industry best practices and standards — across web, mobile, and backend.

---

**Version:** 0.1
**Issued by:** Techversant Center of Excellence (CoE)
**Effective Date:** June 2026
**Audience:** All developers — web frontend, backend, mobile (iOS + Android). Tech-agnostic.
**Length:** 7 phases, 20 topics, 6–8 weeks (3–5 hours/week, pair-friendly)
**Status:** **Draft for cross-team review** — run with 3–5 developers from at least two teams first
**Contributors:** Compiled by CoE Web Working Group; pending cross-team review from Mobile + Backend leads
**Pre-requisite:** Comfortable shipping features in at least one of: React, Next.js, Laravel, Node.js, iOS, Android. The curriculum assumes you have something to *apply* the discipline to.

---

## 🎯 Learning Outcomes

After completing this curriculum, a developer will:

- Write code that **another developer can understand without context**
- Make design decisions consciously, with **documented trade-offs**
- Review pull requests with **objective criteria**, not personal taste
- Recognize code smells early and **refactor safely** before they compound
- Design APIs and systems with **users and change scenarios** in mind
- Mentor juniors using the same rubric the team uses for code review

### Team-Level Metrics of Success

- **PR cycle time** decreases for senior developers (because code lands cleaner on the first review)
- **Defect escape rate** decreases (because testable, refactored code is easier to verify)
- **Code-review comment quality** improves (objective questions, not "this is bad")
- **Tech-debt awareness** increases (developers flag the debt *they* create, not just inherit it)
- **Mentoring hours** become a tracked activity, not an undocumented one

We will measure these by tagging PRs with the topic number from this curriculum (e.g. `refactor/clean-code-1`) and reviewing them at Week 2 and Week 6.

---

## 📚 Table of Contents

- [Prerequisites (complete before Week 1)](#prerequisites-complete-before-week-1)
- [Suggested 6–8 Week Plan](#suggested-6-8-week-plan)
- [Phase 1 — Foundational Coding Discipline (Beginner)](#phase-1--foundational-coding-discipline-beginner)
  - [1. Clean Code Fundamentals](#1-clean-code-fundamentals)
  - [2. Control Flow & Logic Clarity](#2-control-flow--logic-clarity)
  - [3. DRY vs. WET](#3-dry-vs-wet)
  - [4. Basic Error Handling](#4-basic-error-handling)
- [Phase 2 — Core Design Principles (Intermediate)](#phase-2--core-design-principles-intermediate)
  - [5. SOLID Principles (Core)](#5-solid-principles-core)
  - [6. Separation of Concerns (SoC)](#6-separation-of-concerns-soc)
  - [7. Dependency Injection & Inversion of Control](#7-dependency-injection--inversion-of-control)
  - [8. Reusability & Extensibility](#8-reusability--extensibility)
- [Phase 3 — Design Thinking for Developers (Intermediate → Advanced)](#phase-3--design-thinking-for-developers-intermediate--advanced)
  - [9. Design Thinking for Engineering](#9-design-thinking-for-engineering)
  - [10. Trade-off Analysis](#10-trade-off-analysis)
  - [11. Domain Modeling Basics](#11-domain-modeling-basics)
- [Phase 4 — API & Architectural Thinking (Advanced)](#phase-4--api--architectural-thinking-advanced)
  - [12. RESTful API Design Principles](#12-restful-api-design-principles)
  - [13. Validation & Boundary Protection](#13-validation--boundary-protection)
  - [14. Performance Awareness](#14-performance-awareness)
- [Phase 5 — Testing & Quality Engineering (Advanced)](#phase-5--testing--quality-engineering-advanced)
  - [15. Testing Fundamentals](#15-testing-fundamentals)
  - [16. Writing Testable Code](#16-writing-testable-code)
  - [17. Refactoring Techniques](#17-refactoring-techniques)
- [Phase 6 — Code Review Excellence (Advanced)](#phase-6--code-review-excellence-advanced)
  - [18. Effective Code Review Practices](#18-effective-code-review-practices)
  - [19. Code Review Checklist (Standardized)](#19-code-review-checklist-standardized)
  - [20. Engineering Ethics & Ownership](#20-engineering-ethics--ownership)
- [Phase 7 — Senior Developer Mindset (Optional / Lead Track)](#phase-7--senior-developer-mindset-optional--lead-track)
- [How to Teach This Effectively](#how-to-teach-this-effectively)
- [Recommended Resources](#recommended-resources)
- [Document Control](#document-control)

---

## Prerequisites (complete before Week 1)

Before the first session, the developer should:

- **Have one production codebase they actively work on.** This curriculum teaches by evolving real code, not by abstract exercises. If the developer is between projects, run this with a sample codebase from the team's recent PRs.
- **Have completed a stack path** (React, Next.js, Laravel, or equivalent) OR be paired with a senior developer who can mentor. The curriculum *teaches* you to read and write good code; it does not teach you a language.
- **Have PR review experience** (even if reviewing seniors is the developer's only current experience). Topic 18 in Phase 6 assumes you can articulate a code review comment.
- **Have a code editor with a real linter + formatter installed.** The "formatting & consistency" topic in Phase 1 is the first session; if the developer's editor doesn't run Prettier/Black/equivalent on save, set that up before starting.

---

## Suggested 6–8 Week Plan

The curriculum is designed for **one topic per session, with a mini-task follow-up**. A full pilot run covers all 6 core phases in 6–8 weeks (one session per week, 1.5h session + 2–3h mini-task).

| Week | Phase | Topics | Format |
|---|---|---|---|
| 1 | Phase 1 | Topics 1, 2 | Session 1.5h + mini-task: clean up one open PR |
| 2 | Phase 1 | Topics 3, 4 | Session 1.5h + mini-task: apply DRY + error handling to one module |
| 3 | Phase 2 | Topics 5, 6 | Session 1.5h + mini-task: extract a service from a fat controller |
| 4 | Phase 2 | Topics 7, 8 | Session 1.5h + mini-task: inject a dependency into a hard-coupled class |
| 5 | Phase 3 | Topics 9, 10, 11 | Session 2h + mini-task: write an ADR for a design choice |
| 6 | Phase 4 | Topics 12, 13, 14 | Session 2h + mini-task: review an existing API for validation gaps |
| 7 | Phase 5 | Topics 15, 16, 17 | Session 2h + mini-task: add tests to a refactored module |
| 8 | Phase 6 | Topics 18, 19, 20 | Session 2h + mini-task: 5 code reviews using the standardized checklist |
| Optional | Phase 7 | Lead track | Async reading + mentoring hours; not a session |

Pair the developer with a senior who has **already run the curriculum** — the pair format is the single biggest predictor of pilot success.

### Phase 1 — Foundational Coding Discipline (Beginner)

**Goal:** Eliminate bad habits, improve readability, and create a shared coding baseline.

#### 1. Clean Code Fundamentals

**Why this topic exists:** Most bugs and most code-review friction come from code that's *hard to read*, not code that's *wrong*. This topic sets the floor for everything that follows.

**Learn:**
- Naming conventions:
  - Variables — nouns, no abbreviations, no type encoding (`customerName`, not `custNm` or `strCustName`)
  - Methods — verbs, single intent (`calculateTotal`, not `processStuff`)
  - Classes — nouns, single concept (`Invoice`, not `InvoiceProcessorHelper`)
- Meaningful vs. misleading names — `User[] activeUsers` is meaningful; `User[] list` is misleading (a list of what?)
- Function size & clarity — aim for one screen, one job. A function that does two things should be two functions.
- Avoiding magic numbers and magic strings — `MAX_LOGIN_ATTEMPTS = 5` is named; `if (attempts > 5)` is magic
- Code formatting & consistency — defer to the team's formatter (Prettier, Black, clang-format, SwiftLint). Don't argue formatting in PRs; argue intent.

**Code-review focus:**
- "Can I understand this code without context?"
- "Is the intent obvious?"
- "If I were new to this codebase, would I know what this variable holds?"

**Mini-task:**
Pick one open PR of yours. Re-read the diff with the focus question: *can I understand this code without context?* Rename any unclear names. Extract any function that does two things. Open a follow-up PR titled `refactor(clean-code-1): <your-name>` and ask your reviewer to apply the same three questions to your changes.

**Self-check:**
- [ ] I can name a variable without encoding its type
- [ ] I can write a function that does one thing in one screen
- [ ] I can replace every magic number in a function with a named constant

---

#### 2. Control Flow & Logic Clarity

**Why this topic exists:** Deeply nested conditionals are a leading indicator of bugs (each level of nesting multiplies the cognitive load). This topic gives the developer a default style that flattens the tree.

**Learn:**
- Avoiding deeply nested if-else — three levels of nesting is the alarm bell
- Early returns — flip the condition, return early, keep the happy path at the top indentation level
- Guard clauses — handle the exceptional case first (`if (user is null) return;`), keep the main path flat
- Happy-path-first coding — write the success case first, then add the error/edge-case branches as guards
- Why it matters:
  - Reduces cognitive load (the reader doesn't have to track state through 4 levels)
  - Easier debugging (errors live at the top, not buried)
  - Easier to add new branches (a new guard clause is local; a new level of nesting affects everything)

**Code-review focus:**
- "How many levels of nesting does this function have?"
- "Could the happy path be at the top indentation?"
- "Is each conditional a guard, or are some of them mid-flow logic?"

**Mini-task:**
Take the most deeply nested function in your current codebase (the one you've been avoiding). Refactor it using early returns + guard clauses. Commit the before/after in a single PR. Tag the reviewer and ask: *is the happy path at the top indentation now?*

**Self-check:**
- [ ] I can refactor a 4-level nested function to ≤2 levels using guard clauses
- [ ] I can name the *happy path* in any function I read
- [ ] I can write a new function with the success case at the top, edges as guards

---

#### 3. DRY vs. WET

**Why this topic exists:** "DRY" is one of the most over-applied principles in software. Repeated code is sometimes a smell, sometimes a sign of a premature abstraction. This topic teaches the developer to *recognize the difference*.

**Learn:**
- Don't Repeat Yourself (DRY) — the *intent*: every piece of knowledge has a single, authoritative representation
- When repetition is acceptable (WET — Write Everything Twice) — *three* times is the rule of thumb: copy once (acceptable), copy twice (acceptable), copy three times (extract)
- Over-abstraction dangers:
  - The wrong abstraction is **worse than duplication** — it makes the code harder to read, not easier
  - A premature abstraction guesses at the commonality; the guess is often wrong
  - Once the wrong abstraction is in place, every consumer inherits its mistakes
- The principle of "Rule of Three" — duplicate on the first two occurrences; extract on the third (or when the second copy needs to change differently from the first)

**Code-review focus:**
- "Is this abstraction adding clarity or complexity?"
- "Has this concept appeared three times, or only two?"
- "If I read the abstracted version, do I need to scroll back to the call site to understand it?"

**Mini-task:**
Find a piece of code in your codebase that you suspect is *over-abstracted* — a helper that has only one or two callers, with a signature that's harder to read than inlining. Inline it back. Commit and tag `refactor(clean-code-3): inline-over-abstraction`. If the helper has a third caller, write an ADR (Topic 9) explaining why you're keeping the abstraction.

**Self-check:**
- [ ] I can name a real abstraction in my codebase that *should* be inlined
- [ ] I can name a real duplication in my codebase that *should* be extracted (and the third occurrence proves it)
- [ ] I can explain "the wrong abstraction is worse than duplication" in 30 seconds

---

#### 4. Basic Error Handling

**Why this topic exists:** Bad error handling turns a 5-minute bug into a 5-day investigation. This topic gives the developer a default style for surfacing failures.

**Learn:**
- Exceptions vs. return codes:
  - **Exceptions** for *exceptional* conditions (network down, file missing, auth failed) — they unwind the call stack and force the caller to handle
  - **Return codes / Result types** for *expected* conditions (validation failed, user not found) — they're part of the API
  - Mix them only with a clear rule for which is which
- Fail-fast principle — detect the error as close to the cause as possible; don't let bad data flow through three layers before failing
- User-friendly vs. developer-friendly errors:
  - User sees: "We couldn't save your changes. Please try again." (or whatever your UX standard is)
  - Developer logs: `Failed to write invoice 12345: database connection timeout after 5s (requestId=...)` — with enough context to debug, never leaking internals to the user
- Logging basics — what to log:
  - **Always:** the operation that failed, a stable identifier (requestId, userId, resourceId), the time
  - **Never:** passwords, tokens, PII, full credit-card numbers
  - Use structured logging (the team's standard — see [REST API Best Practices](../../general/rest-api-best-practices.md))

**Code-review focus:**
- "If this fails in production at 2am, will the on-call engineer know what happened?"
- "Is the error surfaced at the right level — at the cause, or three layers down?"
- "Are we logging the *right* amount? (Not too much, not too little, never secrets)"

**Mini-task:**
Pick one error path in your current codebase. Verify it:
1. Fails fast at the cause (not after a chain of mutations)
2. Returns a user-friendly error message
3. Logs enough context for an on-call engineer to debug
4. Does NOT log any PII, token, or secret

Fix any of the four that are missing. Open a PR tagged `refactor(clean-code-4): error-handling`. If you find a secret being logged, treat that as a security issue and raise it separately — see the [Security Audit Checklist](../../audit/security-audit-checklist.md).

**Self-check:**
- [ ] I can choose between an exception and a return code based on whether the condition is *exceptional* or *expected*
- [ ] I can write a fail-fast error path that surfaces the cause at the right layer
- [ ] I can list three things I should *never* log

---

### Phase 2 — Core Design Principles (Intermediate)

**Goal:** Move from "working code" to "well-designed code."

#### 5. SOLID Principles (Core)

**Why this topic exists:** SOLID is the most-cited design vocabulary in our industry. Every developer on the team should know the names and the *why* — even when they don't strictly follow one of them. This is the topic that turns a senior reviewer's "this feels wrong" into "this violates LSP, here's why."

**Learn (using a single evolving example, not theory):**

> Pick a small but real example from your team's codebase — say, a `PaymentProcessor`. Build it once naively. Then evolve it through the five principles. Each principle is one refactor.

- **S — Single Responsibility Principle** — A class has *one* reason to change. If "save to DB" and "send email" are in the same class, that class has two reasons to change. (Refactor: split the `send` out.)
- **O — Open/Closed Principle** — Open to extension, closed to modification. Add a new payment type *without* editing `PaymentProcessor`. (Refactor: introduce a `PaymentMethod` interface, dispatch on type.)
- **L — Liskov Substitution Principle** — Subtypes must be substitutable for their base type. If `SquarePayment extends Payment` and calling `square.charge()` returns a different shape than `paypal.charge()`, you've violated LSP. (Refactor: tighten the contract — every `charge()` returns the same shape.)
- **I — Interface Segregation Principle** — Many small interfaces beat one big one. If a class implements 12 methods but only 3 are used, split the interface. (Refactor: split `PaymentService` into `Chargeable`, `Refundable`, `Reportable`.)
- **D — Dependency Inversion Principle** — High-level modules depend on *abstractions*, not concretions. `OrderProcessor` depends on `PaymentGateway` (interface), not `StripeGateway` (concrete). (Refactor: inject the gateway as a constructor parameter.)

**Outcome:**
- Easier feature changes (adding a payment type doesn't edit `PaymentProcessor`)
- Safer refactoring (the contract is explicit, so the breaking changes are visible)
- Better testability (mocked dependencies replace real ones — see Topic 7)

**Code-review focus:**
- "Does this class have one reason to change, or two?"
- "If I add a new variant tomorrow, do I edit this class or extend it?"
- "If I swap the implementation, does the consumer break?"

**Mini-task:**
Pick the *worst-designed* class in your codebase. Apply the five SOLID principles to it, *one refactor per principle*, in five separate PRs. Each PR is a teaching artifact: title it `refactor(solid-N): <principle-name>` and the PR description says which SOLID letter and what the "before" looked like. Use the evolving example from the session.

**Self-check:**
- [ ] I can name all five SOLID principles and give an example of each from my codebase
- [ ] I can spot a class with two responsibilities and split them
- [ ] I can inject a dependency instead of constructing it inside the class

---

#### 6. Separation of Concerns (SoC)

**Why this topic exists:** The "fat controller" is the most common architecture smell in web backends. The fix is layering: presentation knows about business logic, business logic knows about data, data knows about the database. Each layer has *one* concern.

**Learn:**
- Business logic vs. presentation — the same business rule ("an order can't be shipped if it's not paid") shouldn't live in the controller *and* the model. Pick one (the model / service layer) and let the controller call it.
- Controllers vs. services vs. repositories:
  - **Controller** — receives the request, calls the service, returns the response
  - **Service** — orchestrates the business rules
  - **Repository** — owns the data access
- Fat controller → thin controller — if your controller has more than ~20 lines of business logic, the logic belongs in a service
- Avoiding "God classes" — a class that knows about HTTP, database, business rules, and logging is a god class. The cure is layering.
- Stack-specific guidance:
  - **Laravel** — controllers, services, repositories, resources
  - **Next.js / React** — Server Actions / route handlers, services, data-access layer (the "thin server component" pattern)
  - **iOS** — view controllers, view models, services
  - **Android** — fragments / composables, view models, repositories

**Code-review focus:**
- "Is this controller doing business logic, or just orchestrating?"
- "Is this class doing one concern or three?"
- "If I had to swap the framework tomorrow, what would I have to change?"

**Mini-task:**
Find a controller in your codebase with more than 20 lines. Extract the business logic into a service. Update the controller to be a thin orchestrator. Commit `refactor(soc): <controller-name>-to-thin`.

**Self-check:**
- [ ] I can identify the three layers (controller, service, repository) in my codebase
- [ ] I can extract a service from a fat controller
- [ ] I can name a "god class" in my codebase and explain what concerns it's mixing

---

#### 7. Dependency Injection & Inversion of Control

**Why this topic exists:** Hard-coded dependencies make code untestable. Injected dependencies make code replaceable — for tests, for environments, for future implementations. This topic gives the developer the mechanical skill of injecting.

**Learn:**
- Hard dependencies vs. injected dependencies:
  - **Hard:** `const repo = new PostgresUserRepository();` — the class is married to Postgres
  - **Injected:** `constructor(private repo: UserRepository) {}` — the class knows the *interface*, not the implementation
- Constructor injection — pass the dependency in the constructor; the class never calls `new` for its own dependencies
- Why DI improves testing — in tests, pass a `MockUserRepository` that returns canned data; in production, pass the real one. The class is the same.
- Real-life refactoring example — start with a hard-coded dependency, then refactor in three steps:
  1. Extract the constructor of the dependency as a constructor parameter
  2. Define an interface (TypeScript, PHP interface, Swift protocol, Kotlin interface) for the dependency
  3. Register a binding (Laravel service container, Spring `Bean`, Swift composition root) so production code passes the real impl
- Composition root — the one place in the app where everything is wired together. *Don't* sprinkle `new` calls across the codebase.

**Code-review focus:**
- "Is this class easy to test?"
- "Can I replace this dependency with a mock?"
- "Where is the composition root for this module?"

**Mini-task:**
Find a class in your codebase that constructs its own dependencies. Inject them via the constructor. Write one unit test that passes a mock dependency. Commit `refactor(di): inject-<dependency-name>`.

**Self-check:**
- [ ] I can identify a class that hard-codes a dependency
- [ ] I can inject that dependency via the constructor
- [ ] I can write a unit test using a mock dependency

---

#### 8. Reusability & Extensibility

**Why this topic exists:** Reusability is *sometimes* a virtue, sometimes a trap. The developer needs to know when to extract and when to leave things alone. This topic gives the framework.

**Learn:**
- Composition over inheritance:
  - Inheritance creates *is-a* relationships (`Square is-a Rectangle` — and that's where the math breaks down)
  - Composition creates *has-a* relationships (`Square has-a Shape` — and the math stays correct)
  - Default to composition. Use inheritance only when the *is-a* relationship is genuinely correct AND the LSP (Topic 5) is satisfied
- Config-driven behavior:
  - Make the variation *data*, not code — feature flags, config values, database lookups
  - Resist the urge to add a subclass for every new variation; that's the inheritance tax
- Feature flags vs. conditionals:
  - **Feature flag** — toggle a feature on/off at runtime, for a cohort, for a region
  - **Conditional** — branch on a runtime value that's part of the input
  - Don't conflate: feature flags belong in a flag service, not in `if (user.role === 'admin')` scattered across the codebase

**Code-review focus:**
- "Is this new behavior a new class, or a new value of an existing one?"
- "Could this conditional be a config value instead of a hard-coded branch?"
- "Is this inheritance solving a real is-a problem, or papering over a missing config?"

**Mini-task:**
Find a class hierarchy in your codebase with 3+ subclasses that share 80% of their code. Refactor one of them to composition. If the *only* difference is a config value, replace the subclass with a config flag. Commit `refactor(reuse): composition-over-inheritance`.

**Self-check:**
- [ ] I can name a real case where composition is a better choice than inheritance in my codebase
- [ ] I can replace a hard-coded conditional with a config value
- [ ] I can use a feature flag instead of a scattered `if (user.role === ...)` check

---

### Phase 3 — Design Thinking for Developers (Intermediate → Advanced)

**Goal:** Teach developers to think before they code.

#### 9. Design Thinking for Engineering

**Why this topic exists:** Most engineering mistakes happen *before* the first line of code. The developer needs to spend time on the problem, not the syntax. This topic installs the habit.

**Learn:**
- Understand the problem, not just the ticket — the ticket says "add export-to-CSV"; the problem is "users need to take their data out of the system when they leave." The latter is what you design for.
- Who is the user? — internal user, external user, admin, support engineer, auditor. The "user" isn't always a customer.
- What can change in the future? — change scenarios: "If we add a new tenant, what breaks?" "If we move from Stripe to Adyen, what breaks?" "If the user uploads 10x more data, what breaks?"
- Identify variability points — the things that *will* change, separated from the things that *won't*. Build for the stable parts; isolate the variable parts.
- Practical exercise — rewrite requirements as "change scenarios":
  - "If [future change] happens, the system [should/should not] have to change."
  - This is the foundation of an Architecture Decision Record (Topic in Phase 7).

**Code-review focus:**
- "Did the author understand the problem, or just the ticket?"
- "Are the variability points called out, or hidden?"
- "Is the design robust to the change scenarios in the ADR?"

**Mini-task:**
Take your current ticket. Write 3 change scenarios (in the form "if X, then Y") *before* writing any code. Open an ADR (use the [template in Phase 7](#phase-7--senior-developer-mindset-optional--lead-track)) and ask your reviewer: "do these scenarios match the design, or does the design need to change?" Commit `docs(design): change-scenarios-<ticket-id>`.

**Self-check:**
- [ ] I can write 3 change scenarios for a ticket *before* writing code
- [ ] I can separate the stable parts of a design from the variable parts
- [ ] I can name the *user* of a feature, not just the requester

---

#### 10. Trade-off Analysis

**Why this topic exists:** There is no perfect solution. Every design decision is a trade-off. The senior developer makes the trade-off *consciously* and documents it. This topic installs the habit.

**Learn:**
- Readability vs. performance — a 3x faster function that's impossible to read is usually the wrong choice. Measure the performance first.
- Speed of delivery vs. long-term cost — the "we'll fix it later" tax. The later is real, the now is concrete. Pick consciously.
- Simplicity vs. flexibility — a flexible abstraction that's never used is over-engineering. A simple solution that breaks on the third variant is under-engineering. Look for the *third* variant (Topic 3, Rule of Three).
- Common trade-offs in our domain:
  | Trade-off | Lean toward | When to flip |
  |---|---|---|
  | Readability > cleverness | readability | in a 2% hot path measured by profiler |
  | Consistency > novelty | consistency | a measured business need |
  | Explicit > implicit | explicit | high-frequency code where the explicitness becomes noise |
  | Simple > flexible | simple | the third variant of a feature |
- The mindset — *"There is no perfect solution — only informed trade-offs."* The job of a senior developer is to make the trade-off, document it, and be able to defend it.

**Code-review focus:**
- "Is the trade-off conscious or accidental?"
- "If we picked readability over performance, did we measure first?"
- "Where is the ADR for this decision?"

**Mini-task:**
Take the design decision in Topic 9's ADR. Add a "Trade-offs" section that names what you gave up. Push the PR; ask your reviewer to challenge any trade-off they think is wrong. If you can't defend it, change the design.

**Self-check:**
- [ ] I can name a real trade-off in my current design — and what I gave up
- [ ] I can defend the trade-off in 2 minutes
- [ ] I can flip the trade-off when the third variant appears (or the performance number proves the cost)

---

#### 11. Domain Modeling Basics

**Why this topic exists:** Domain-Driven Design is its own discipline; this topic gives the developer the *minimum* vocabulary. Knowing "entity vs. value object" lets a developer read the codebase and follow the model.

**Learn:**
- Understanding domain language — the words in the code should match the words in the business. If the business says "order," the class is `Order`, not `OrderRequestDto`. (This is "ubiquitous language" in DDD.)
- Entities vs. value objects:
  - **Entity** — has identity, mutable over time (`Order #1234` is the same order even if its total changes)
  - **Value object** — has no identity, defined by its values (`Address(street, city, zip)` — two `Address` objects with the same values are equal)
- Avoid anemic models — a class that's just getters and setters, with the business rules in a separate service, has no behavior. Move the rules onto the model.
- Business rules belong in the domain, not controllers — a rule like "an order can't be shipped if it's not paid" belongs in `Order.ship()`, not in the controller. The controller orchestrates; the domain decides.

**Code-review focus:**
- "Is the class name in the business language, or in the framework language?"
- "Are there value objects hiding in this codebase (e.g. a tuple of three strings)?"
- "Is the model anemic — all data, no behavior?"

**Mini-task:**
Find a class in your codebase that's anemic (just getters/setters, business rules in services). Move one business rule from the service to the model. Commit `refactor(ddd): move-rule-onto-model`.

**Self-check:**
- [ ] I can name an entity and a value object from my codebase
- [ ] I can move a business rule from a service onto the model
- [ ] I can rename a class from the framework's vocabulary to the business's vocabulary

---

### Phase 4 — API & Architectural Thinking (Advanced)

**Goal:** Make developers system-aware.

#### 12. RESTful API Design Principles

**Why this topic exists:** The API is the *contract* with the world. Once it's published, changing it breaks consumers. This topic gives the developer the design vocabulary, paired with the [REST API Best Practices](../../general/rest-api-best-practices.md) CoE standard.

**Learn:**
- Resource-oriented URLs — `/orders/1234`, not `/getOrder?id=1234`. Nouns, not verbs.
- HTTP methods & status codes:
  - `GET` is safe + idempotent
  - `POST` is neither
  - `PUT` is idempotent (same request = same effect)
  - `PATCH` is for partial updates
  - `DELETE` is idempotent
  - Status codes: `200` OK, `201` Created, `204` No Content, `400` Bad Request, `401` Unauthorized, `403` Forbidden, `404` Not Found, `409` Conflict, `422` Unprocessable, `500` Server Error
- Idempotency — a `POST` that may be retried (payment, account creation) needs an idempotency key. The server recognizes the key and returns the same response.
- Pagination, filtering, sorting — the CoE standard is `_gt`, `_gte`, `_lt`, `_lte`, `_ne`, `_in`, `_between` for filtering; `sort=field` (asc) and `sort=-field` (desc)
- Versioning strategies:
  - **URL path** (`/api/v1/...`) — easy to read, easy to route
  - **Header** (`Accept: application/vnd.api+json;version=2`) — cleaner URLs, harder to test in a browser
  - **Subdomain** (`api.v2.example.com`) — different infra, harder to coordinate
  - Default to URL path for our internal APIs; revisit when a public API needs it

**Code-review focus:**
- "Is this API predictable? Can I guess the URL without reading the docs?"
- "Is it backward-compatible? Did a new field *break* any existing consumer?"
- "Are the right HTTP methods and status codes being used?"

**Mini-task:**
Pick one API in your codebase. Review it for the five points above. Open a doc PR (`docs(api-review): <endpoint>`) that lists each gap and proposes a fix. Coordinate with the API owner before changing the contract.

**Self-check:**
- [ ] I can name the right HTTP method and status code for a given operation
- [ ] I can explain idempotency in the context of a retry
- [ ] I can spot a URL that's a verb (anti-pattern) and refactor it to a resource

---

#### 13. Validation & Boundary Protection

**Why this topic exists:** Every input is untrusted. The server is the *last* line of defense. This topic gives the developer the default behavior for every input.

**Learn:**
- Input validation:
  - Validate at the **boundary** — controller, route handler, API endpoint
  - Use the same schema on client and server (Zod in TypeScript, Form Request in Laravel, etc.)
  - Re-validate on the server; never trust the client
- Defensive programming — assume the input is wrong; verify, then act
- Trust boundaries:
  - **Browser → server** — every parameter is user-controlled
  - **Server → service** — assume the service receives validated input (because the controller did the validation)
  - **Service → repository** — assume the repository receives a known entity
  - Don't re-validate at every layer; that's wasted work. Validate *at the boundary*.
- Data sanitization:
  - HTML escaping for any user content rendered in a browser
  - Parameterized queries for any database access (no string concatenation — see the [PHP standards](../../php/php-coding-standards.md) and the [Node.js standards](../../nodejs/nodejs-typescript-best-practices.md))
  - Output encoding at the rendering layer

**Code-review focus:**
- "Is this input validated *at the boundary*?"
- "Is the same schema used on client and server?"
- "Is the SQL parameterized? Are the strings escaped?"

**Mini-task:**
Pick one controller / route handler in your codebase. Audit the inputs: are they all validated? Is the validation at the boundary? Is the same schema shared with the client? Open a doc PR (`docs(validation-audit): <endpoint>`) listing the gaps.

**Self-check:**
- [ ] I can name the trust boundary for a given layer
- [ ] I can add server-side validation to an unvalidated input
- [ ] I can name one place in my codebase where the validation lives at the wrong layer

---

#### 14. Performance Awareness

**Why this topic exists:** Performance is a feature, but premature optimization is a trap. This topic gives the developer the *default discipline* (measure first) and the *common smells* (N+1, missing index, blocking IO).

**Learn:**
- N+1 problem:
  - In a loop, fetching related data one-by-one — `for user in users: user.profile = db.query(profile)` is N+1
  - The fix: eager-load with a join or a `with()` call. Profile before-and-after with the same query count.
- Caching basics:
  - Cache *expensive* operations, not cheap ones
  - Cache *invalidation* is the hard part — the answer is usually a TTL + a tag, not "cache forever"
  - Pair with [Phase 4 of the Next.js path](../nextjs/intermediate.md#phase-4-server-components-vs-client-components) for the Next.js caching model
- When optimization is premature:
  - The function is called 10x per request, and the profiler says it's 2% of total time
  - The fix: don't optimize. Write the readable version. Move on.
- Measuring before optimizing:
  - Use the team's standard tool (Blackfire, Xdebug + PHP, Chrome DevTools, Lighthouse, etc.)
  - The number on the screen, not the gut feeling, drives the decision

**Code-review focus:**
- "Did this change get measured, or is it a guess?"
- "Is this optimization in a hot path, or a cold one?"
- "Does the cache have an invalidation strategy, or is it 'set and forget'?"

**Mini-task:**
Find one N+1 query in your codebase. Eager-load it. Compare the query count before and after. Commit `perf(n+1): <module>` with the before/after numbers in the PR description.

**Self-check:**
- [ ] I can spot an N+1 query in a log
- [ ] I can name a cache invalidation strategy for a given cache
- [ ] I can defer optimization when the profile doesn't justify it

---

### Phase 5 — Testing & Quality Engineering (Advanced)

**Goal:** Confidence in change.

#### 15. Testing Fundamentals

**Why this topic exists:** Tests are how we *verify* the discipline from Phases 1–4 actually works. A refactor without tests is a rewrite in disguise. This topic installs the testing vocabulary.

**Learn:**
- Unit vs. integration vs. E2E:
  - **Unit** — tests one function/class in isolation; fast, no IO; thousands of these
  - **Integration** — tests multiple units together, often with a real DB; dozens of these
  - **E2E** — tests the full stack from the UI; slow, fragile; a handful of these for the critical path
  - The pyramid: many unit, some integration, few E2E
- What NOT to test:
  - The framework (don't test that React renders a `<div>`; trust it)
  - Trivial getters/setters
  - Pure delegation functions (the only thing they do is call something else)
- Test naming & structure:
  - `describe('OrderProcessor', () => { it('returns 0 when no items', ...) })` — name reads as a sentence
  - Arrange / Act / Assert — three clear sections
- Test readability:
  - One assertion per test, ideally
  - If you need 5 setup steps, the test is doing too much

**Code-review focus:**
- "Does this test actually verify the behavior, or just the syntax?"
- "Is the test name a sentence that describes the *behavior*, not the *implementation*?"
- "Is the test in the right layer? (Unit for unit, E2E for the user journey)"

**Mini-task:**
Write one unit test for a function you wrote in the last week. The test name should be a sentence. The body should be arrange/act/assert. Commit `test: <function-name>`.

**Self-check:**
- [ ] I can name the test pyramid layers and give a count for each
- [ ] I can name a function that doesn't need a test
- [ ] I can write a test name that describes the *behavior*, not the *implementation*

---

#### 16. Writing Testable Code

**Why this topic exists:** Some code is easy to test; some code is hard. The difference is usually *coupling*. This topic gives the developer the patterns that make code testable.

**Learn:**
- Pure functions — input → output, no side effects, no hidden state. The easiest to test.
- Mocking vs. stubbing:
  - **Stub** — returns canned data
  - **Mock** — verifies behavior (called with the right args, the right number of times)
  - Default to stubs. Mocks are for behavior the test cares about.
- Avoiding hidden dependencies:
  - Hidden: `new Date()`, `Math.random()`, `console.log`, global state, the filesystem
  - Visible: passed as a parameter, injected via the constructor, or wrapped in a function
  - If the test depends on `new Date()`, the test is *time-coupled* — and brittle
- Designing for testability:
  - Inject the clock (`Clock` interface, not `new Date()`)
  - Inject the random source (`Random` interface, not `Math.random()`)
  - Inject the logger (`Logger` interface, not `console.log`)

**Code-review focus:**
- "If I wanted to test this function at 3am on a Tuesday, what would I need to set up?"
- "Are the dependencies hidden, or visible?"
- "Could I swap `new Date()` for a `Clock` here?"

**Mini-task:**
Find a function in your codebase that uses `new Date()` or `Math.random()`. Inject the dependency. Write a unit test that uses a fixed value. Commit `refactor(testable): inject-<dependency>`.

**Self-check:**
- [ ] I can name a function that uses a hidden dependency
- [ ] I can inject that dependency and write a deterministic test
- [ ] I can explain the difference between a stub and a mock in 30 seconds

---

#### 17. Refactoring Techniques

**Why this topic exists:** Refactoring is a *discipline*, not a panic move. The developer needs a default process so a refactor stays safe.

**Learn:**
- Safe refactoring:
  - The tests pass *before* the refactor (and stay green *after*)
  - The behavior is unchanged — only the structure changes
  - One refactor at a time; don't combine three refactors with a feature
- Small, incremental changes:
  - If a refactor takes more than 200 lines of diff, it's probably a rewrite. Break it up.
  - The ideal refactor is a single PR that the reviewer can read in 10 minutes
- Refactor vs. rewrite decision-making:
  - **Refactor** when the architecture is right but the code is messy
  - **Rewrite** when the architecture is wrong and no amount of refactoring will fix it
  - The test: if the *names* of the classes/modules are right but the *bodies* are wrong, refactor. If the *names* are wrong, rewrite.
- Code smells recognition:
  - Long method, large class, long parameter list, divergent change, shotgun surgery, feature envy, data clumps, primitive obsession
  - The Martin Fowler catalog — keep a list, reference it

**Code-review focus:**
- "Is the refactor isolated from the feature change?"
- "Are the tests green before AND after?"
- "Is this a refactor or a rewrite disguised as one?"

**Mini-task:**
Take a code smell from your codebase (long method, large class, primitive obsession — pick one). Refactor it in a single PR. The PR should be small enough to read in 10 minutes. The tests should be green before and after. Commit `refactor: <smell>`.

**Self-check:**
- [ ] I can name three code smells from the Martin Fowler catalog
- [ ] I can do a refactor in a single PR with tests green before and after
- [ ] I can decide between refactor and rewrite by looking at the *names*

---

### Phase 6 — Code Review Excellence (Advanced)

**Goal:** Turn code review into a learning engine.

#### 18. Effective Code Review Practices

**Why this topic exists:** Code review is the most leveraged teaching moment in a developer's week. A bad review teaches nothing. A good review compounds.

**Learn:**
- What to review vs. what to ignore:
  - **Review** — intent, correctness, readability, the SOLID principles, test coverage, security
  - **Defer to the formatter** — indentation, quote style, line length. The team's formatter (Prettier, Black, etc.) is the source of truth; don't argue in PRs
- Objective vs. subjective feedback:
  - **Objective** — "this function is doing two things; the second should be a helper" (verifiable from the diff)
  - **Subjective** — "I would have written this differently" (a personal preference, not a review comment)
  - Default to objective. If you find yourself saying "I would have…", stop and ask: *is this a rule, or a preference?*
- Asking questions instead of giving commands:
  - "Could this be a value object?" (question) vs. "Make this a value object." (command)
  - The question invites the author to think; the command invites them to comply
- Review tone & psychology:
  - The author just shipped something; the review is a conversation, not a verdict
  - Praise the good parts first (a one-line "nice extraction" makes the critical comment land better)
  - Distinguish "must fix" (a defect) from "should consider" (an improvement) from "nit" (a preference)

**Code-review focus:**
- Is this comment objective or subjective?
- Did I ask a question, or give a command?
- Did I distinguish must-fix from should-consider from nit?

**Mini-task:**
Review 5 PRs in the next week using the four points above. For each PR, write at least one question (not a command) and at least one specific praise. After the week, reflect: did the tone work? Did the author push back? What would you do differently?

**Self-check:**
- [ ] I can name a comment I wrote that was subjective, and rewrite it as objective
- [ ] I can rewrite a command as a question
- [ ] I can distinguish must-fix from should-consider from nit in my own comments

---

#### 19. Code Review Checklist (Standardized)

**Why this topic exists:** A *team-level* checklist turns code review from "what does this reviewer care about" into "what does this team care about." This topic installs the team's checklist.

**Learn — the standardized Techversant checklist:**

For every PR, the reviewer checks:

- **Readability** — can a new joiner understand this without context?
- **Maintainability** — would the next person to touch this code thank the author?
- **SOLID adherence** — does each class have one responsibility? Are dependencies injected?
- **Error handling** — does the code fail fast at the cause? Are secrets never logged?
- **Security** — are inputs validated at the boundary? Is the SQL parameterized? Is the user the right user? (See the [Security Audit Checklist](../../audit/security-audit-checklist.md))
- **Test coverage** — is the new behavior tested? Are the tests at the right layer?
- **Performance** — was the change measured, or is it a guess?
- **Documentation** — if the public API changed, does the doc match?
- **AI disclosure** — if AI helped write this code, is the commit tagged `[ai-assisted]`?

The stack-specific checklists layer on top of this baseline:

- [Node.js checklist](../../nodejs/nodejs-typescript-code-review-checklist.md)
- [PHP / Laravel checklist](../../php/php-coding-standards.md)
- [CFML checklist](../../cf/coldfusion-code-review-checklist.md)

**How to use it:**

1. Reviewer runs the checklist top-to-bottom on every PR
2. The author is encouraged to *self-review* against the same checklist before requesting review
3. The team's "review-of-reviews" (sampled weekly) checks that the checklist is being applied, not just present

**Code-review focus:**
- The checklist itself — did the reviewer run it?

**Mini-task:**
Pick 3 of your open PRs. Self-review them against the 9-point checklist. Open follow-up PRs for any gap. Reflect: which points did you consistently miss? What does that say about your habits?

**Self-check:**
- [ ] I can name all 9 points of the standardized checklist
- [ ] I can self-review a PR against the checklist in 10 minutes
- [ ] I can name the stack-specific checklist for my stack

---

#### 20. Engineering Ethics & Ownership

**Why this topic exists:** Code is a *team artifact*. The decisions a developer makes — naming, testing, documenting, leaving debt — affect everyone who comes after. This topic installs the ethical frame.

**Learn:**
- Writing code for the next developer:
  - The next developer is often *you*, six months from now, with no context
  - The principle: code is read more often than it's written; optimize for the reader
- Documentation discipline:
  - The three places documentation lives — in the code (clear names, type annotations), in the commit (the diff is the design), and in the doc (the ADR, the API reference)
  - Pick the cheapest one that solves the problem; don't write a 50-page doc for what 5 lines of code can say
- Technical debt awareness:
  - Technical debt is *not* bad code; it's a *deliberate trade-off* that needs to be tracked
  - If you take on debt, leave a TODO with the date, the reason, and the plan
  - The team's "debt register" (a single doc) tracks the open items and their owners
- Accountability mindset:
  - When you ship a bug, you own the fix — not the on-call engineer
  - When you find debt you didn't create, you flag it — not just inherit it
  - When you take on a shortcut, you flag the shortcut — at commit time, not at code review time

**Code-review focus:**
- "If I were new to this codebase, would I know why this code is the way it is?"
- "Is the technical debt here tracked, or invisible?"
- "Does the commit message say what changed and why?"

**Mini-task:**
Find the oldest open TODO in your codebase. Read it. Is it still relevant? If yes, file a ticket and link it; if no, close it. Commit `chore: review-todo-<module>`.

**Self-check:**
- [ ] I can name a piece of technical debt I created and flag it
- [ ] I can write a commit message that says *what* and *why*, not just *what*
- [ ] I can pick the cheapest place to document a decision (code vs. commit vs. doc)

---

### Phase 7 — Senior Developer Mindset (Optional / Lead Track)

**Goal:** Create future tech leads. This phase is not a session; it's an async reading + mentoring track for developers who have finished Phases 1–6 and want to lead.

**Topics (self-paced + pair with a tech lead):**

- **Architectural Decision Records (ADRs)** — write 3 ADRs for real decisions in your codebase. Use the format from the [Techversant Git Workflow](../../git/Techversant_Git_Workflow.md). Pair with a tech lead for review.
- **Designing for scale** — read the team's architecture docs; identify one decision that limits scale and one that doesn't. Write a 1-page note.
- **Backward compatibility** — pick a public API in your codebase; document the contract; identify what would break a consumer. Propose a versioning strategy.
- **Risk-based decision making** — for a real upcoming decision, write down: the options, the risks, the mitigations, the reversibility. Discuss with a tech lead.
- **Mentoring juniors effectively** — pair with a junior for 4 weeks. Run one of the topics from this curriculum *with* them. Reflect on what worked and what didn't.

**Suggested reading:**

- *Designing Data-Intensive Applications* by Martin Kleppmann (the canonical book for the "designing for scale" topic)
- *Clean Architecture* by Robert C. Martin (the canonical book for the SOLID + layering topics in Phases 2 and 3)
- *Refactoring* by Martin Fowler (the canonical book for Phase 5, Topic 17)
- The team's [Techversant Git Workflow](../../git/Techversant_Git_Workflow.md) (for the ADR format and the "risk-based decision" framing)

**Outcome:** A developer who has finished Phase 7 has a portfolio — 3 ADRs, 1 architecture note, 1 backward-compat plan, 1 risk analysis, 1 mentoring reflection. They are *ready* to be a tech lead, not just "in line" for one.

---

## How to Teach This Effectively

> This section is for the *facilitator* — the senior developer or tech lead who runs the pilot batch. The topics above are the *content*. The format below is what makes the content land.

**✔ Use one simple codebase and evolve it step by step.**
Pick one codebase the team knows. Don't teach SOLID with five toy examples — teach SOLID by evolving *their* `PaymentProcessor`. Don't teach REST with a fresh project — review an existing API and refactor it.

**✔ Refactor live during sessions.**
The "before" is a real class in the repo. The "after" is the refactor in real time. The team sees the *decisions* — why the developer chose to extract a service *here*, not *there*. Pre-record the refactor only if the team is remote; live is always better.

**✔ Show before vs. after.**
Every topic has a "before" and an "after." The "before" is the smell. The "after" is the fix. The team's habit, after enough topics, is to *see the smell first* — to recognize the pattern in their own PRs.

**✔ Tie every concept to:**
- **Real production bugs** — "this exact pattern caused incident #2143 in production. Here's the postmortem."
- **Real code review comments** — "this exact comment is on PR #1827. The author pushed back; here's the resolution."
- **Real maintenance pain points** — "this exact abstraction slowed us down in the Q3 migration. Here's why."

**✔ Run in pairs.**
The pair format is the single biggest predictor of pilot success. A solo developer reads the topic; a pair *discusses* the topic. The discussion is where the discipline lands.

**✔ Time-box the topics.**
One session, one topic, one mini-task. Don't combine two topics. The mini-task is the *transfer* — if the developer can't apply it to a real PR, the session didn't land.

**✔ Review the mini-task.**
The mini-task is the assignment; the review is the feedback. The senior developer who runs the pilot also reviews the mini-task PRs. The review is the teaching moment, not the session.

**✔ Document the run.**
After the pilot, write 1 page: what worked, what didn't, what to change for v0.2. Feed it back into this curriculum via a PR.

---

## Recommended Resources

### Books (foundational)

- *Clean Code* by Robert C. Martin — the canonical book for Phases 1 and 6
- *Clean Architecture* by Robert C. Martin — the canonical book for Phases 2 and 3
- *Refactoring* by Martin Fowler — the canonical book for Phase 5
- *Designing Data-Intensive Applications* by Martin Kleppmann — for the Phase 7 "designing for scale" topic
- *The Pragmatic Programmer* by Andrew Hunt & David Thomas — the canonical book for the trade-off analysis mindset

### Online courses (one per phase)

- **Phase 1–2:** [ArjanCodes](https://www.youtube.com/@ArjanCodes) on YouTube (clean code + design principles in Python, but the patterns transfer)
- **Phase 3:** [Domain-Driven Design by Vladimir Khorikov](https://www.pluralsight.com/courses/domain-driven-design-fundamentals) (Pluralsight, paid)
- **Phase 4:** the [REST API Best Practices](../../general/rest-api-best-practices.md) CoE standard (no need for a course — read the doc)
- **Phase 5:** [Testing JavaScript by Kent C. Dodds](https://testingjavascript.com/) (paid, but the de-facto reference)
- **Phase 6:** [Code Review from the Book Club](https://google.github.io/eng-practices/review/) (Google's eng practices, public)

### CoE documents to pair with this curriculum

- [REST API Best Practices](../../general/rest-api-best-practices.md) — for Phase 4
- [AI Era Coding Guidelines](../../general/ai-era-coding-guidelines.md) — for Phase 6 (the two-layer review model)
- [Security Audit Checklist](../../audit/security-audit-checklist.md) — for the security row in the standardized checklist (Phase 6, Topic 19)
- [Techversant Git Workflow](../../git/Techversant_Git_Workflow.md) — for the ADR format (Phase 7)
- [Node.js Code Review Checklist](../../nodejs/nodejs-typescript-code-review-checklist.md) — stack-specific, for the Node.js team
- [PHP Coding Standards](../../php/php-coding-standards.md) — stack-specific, for the Laravel team

---

## Document Control

| Field | Value |
|---|---|
| Document | Developer Excellence Curriculum |
| Version | 0.1 (initial draft — 7 phases, 20 topics) |
| Owner | CoE Web Working Group (with cross-team review from Mobile + Backend) |
| Review Cycle | Quarterly |
| Status | Draft for cross-team review |
| Supersedes | — (initial version) |

---

**Maintained by:** Techversant CoE
**Last Updated:** June 2026
