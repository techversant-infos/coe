# Developer Excellence Curriculum â€” Gap Analysis (Internal Review Document)

> **Audience:** CoE Web Working Group, Mobile leads, Backend leads, and curriculum reviewers â€” not a reader-facing document.
> **Purpose:** Show how the [Developer Excellence Curriculum](./curriculum.md) maps to the wider developer-discipline landscape (clean code, design, testing, review, lead-track) and the related CoE standards. Used during pilot review to challenge scope decisions, not during onboarding.

---

## Gap analysis: our curriculum vs. the full developer-discipline landscape

The developer-discipline landscape is large. The major branches a 2026 Techversant team needs to think about are: **clean code**, **design principles**, **design thinking**, **API & architecture**, **testing**, **code review**, **ethics & ownership**, and **lead-track**.

Legend: âœ… covered in depth Â· âš ï¸ covered lightly Â· âŒ not covered (reason in third column)

| Topic / branch | Status | Where / Why |
|---|---|---|
| **Clean Code Fundamentals** (naming, function size, magic numbers, formatting) | âœ… | [Phase 1, Topic 1](./curriculum.md#1-clean-code-fundamentals) â€” full topic with mini-task |
| **Control Flow & Logic Clarity** (nesting, early returns, guard clauses) | âœ… | [Phase 1, Topic 2](./curriculum.md#2-control-flow-logic-clarity) â€” full topic with the "deepest-nested function" mini-task |
| **DRY vs. WET** (Rule of Three, over-abstraction) | âœ… | [Phase 1, Topic 3](./curriculum.md#3-dry-vs-wet) â€” full topic; explicitly covers "wrong abstraction is worse than duplication" |
| **Basic Error Handling** (exceptions vs. return codes, fail-fast, logging) | âœ… | [Phase 1, Topic 4](./curriculum.md#4-basic-error-handling) â€” full topic; pairs with the [REST API Best Practices](../../general/rest-api-best-practices.md) error envelope |
| **SOLID Principles** (all five, with one evolving example) | âœ… | [Phase 2, Topic 5](./curriculum.md#5-solid-principles-core) â€” full topic; "one evolving codebase" format per [how-to-teach.md](./how-to-teach.md) |
| **Separation of Concerns** (controllers/services/repositories) | âœ… | [Phase 2, Topic 6](./curriculum.md#6-separation-of-concerns-soc) â€” full topic; stack-specific guidance for Laravel, Next.js, iOS, Android |
| **Dependency Injection & IoC** (constructor injection, composition root) | âœ… | [Phase 2, Topic 7](./curriculum.md#7-dependency-injection-inversion-of-control) â€” full topic; includes the three-step refactor |
| **Reusability & Extensibility** (composition over inheritance, feature flags) | âœ… | [Phase 2, Topic 8](./curriculum.md#8-reusability-extensibility) â€” full topic |
| **Design Thinking for Engineering** (change scenarios, variability points) | âœ… | [Phase 3, Topic 9](./curriculum.md#9-design-thinking-for-engineering) â€” full topic; the ADR-format mini-task feeds into Phase 7 |
| **Trade-off Analysis** (readability vs. performance, the "no perfect solution" mindset) | âœ… | [Phase 3, Topic 10](./curriculum.md#10-trade-off-analysis) â€” full topic; the 4-row trade-off table is a reusable artifact |
| **Domain Modeling Basics** (entities vs. value objects, anemic models, ubiquitous language) | âœ… | [Phase 3, Topic 11](./curriculum.md#11-domain-modeling-basics) â€” full topic; the minimum DDD vocabulary |
| **RESTful API Design Principles** (resources, HTTP methods, idempotency, versioning) | âœ… | [Phase 4, Topic 12](./curriculum.md#12-restful-api-design-principles) â€” full topic; pairs with the [REST API Best Practices](../../general/rest-api-best-practices.md) CoE standard |
| **Validation & Boundary Protection** (input validation, trust boundaries, sanitization) | âœ… | [Phase 4, Topic 13](./curriculum.md#13-validation-boundary-protection) â€” full topic; cross-references the [PHP](../../php/php-coding-standards.md) and [Node.js](../../nodejs/nodejs-typescript-best-practices.md) standards for parameterized queries |
| **Performance Awareness** (N+1, caching basics, measure-first) | âœ… | [Phase 4, Topic 14](./curriculum.md#14-performance-awareness) â€” full topic; pairs with the [Next.js path Phase 4](../../01-software-engineering/web-development/frontend/nextjs/intermediate.md#phase-4-server-components-vs-client-components) for the caching model |
| **Testing Fundamentals** (unit/integration/E2E, what NOT to test) | âœ… | [Phase 5, Topic 15](./curriculum.md#15-testing-fundamentals) â€” full topic |
| **Writing Testable Code** (pure functions, mocking vs. stubbing, hidden dependencies) | âœ… | [Phase 5, Topic 16](./curriculum.md#16-writing-testable-code) â€” full topic; the "inject the clock" pattern is the canonical example |
| **Refactoring Techniques** (safe refactoring, Rule of Three, refactor vs. rewrite) | âœ… | [Phase 5, Topic 17](./curriculum.md#17-refactoring-techniques) â€” full topic; the "names vs. bodies" decision rule is a reusable artifact |
| **Effective Code Review Practices** (objective vs. subjective, questions vs. commands) | âœ… | [Phase 6, Topic 18](./curriculum.md#18-effective-code-review-practices) â€” full topic; the "5 PRs in a week" mini-task |
| **Code Review Checklist (Standardized)** (the 9-point Techversant checklist) | âœ… | [Phase 6, Topic 19](./curriculum.md#19-code-review-checklist-standardized) â€” full topic; cross-references the stack-specific checklists |
| **Engineering Ethics & Ownership** (next-developer principle, debt awareness, accountability) | âœ… | [Phase 6, Topic 20](./curriculum.md#20-engineering-ethics-ownership) â€” full topic; the "oldest open TODO" mini-task |
| **Senior Developer Mindset** (ADRs, scale, backward compat, mentoring) | âœ… | [Phase 7](./curriculum.md#phase-7-senior-developer-mindset-optional-lead-track) â€” full phase; self-paced + pair with tech lead; portfolio outcome |
| **Concurrency & Threading** | âš ï¸ partial | Touched implicitly in Phase 4 Topic 14 (performance) and Phase 5 Topic 16 (testability), but no dedicated topic. **Defer to a stack-specific path or a v0.2 add-on if a team needs it.** |
| **Security as a discipline** (threat modeling, OWASP, secure-by-default) | âš ï¸ partial | The security *row* in the [Topic 19 checklist](./curriculum.md#19-code-review-checklist-standardized) is the entry point. Full coverage lives in the [Security Audit Checklist](../../audit/security-audit-checklist.md) and the [Auth/AuthZ topics in the stack paths](../../01-software-engineering/web-development/frontend/nextjs/intermediate.md#phase-7-authentication-and-authorization). The curriculum *cites* security but does not *teach* it as a stand-alone topic. |
| **Observability & Monitoring** (structured logging, metrics, tracing) | âš ï¸ partial | Touched in [Phase 1, Topic 4](./curriculum.md#4-basic-error-handling) (logging basics) and [Phase 4, Topic 14](./curriculum.md#14-performance-awareness) (measure-first). Full coverage lives in the [Node.js standards](../../nodejs/nodejs-typescript-best-practices.md) and the [Next.js path Phase 10](../../01-software-engineering/web-development/frontend/nextjs/intermediate.md#phase-10-production-readiness). |
| **DDD Strategic Patterns** (bounded contexts, context mapping, aggregates) | âš ï¸ partial | [Phase 3, Topic 11](./curriculum.md#11-domain-modeling-basics) covers *tactical* patterns (entity vs. value object) but not *strategic* (bounded contexts). **Defer to a v0.2 add-on or a dedicated DDD deep-dive.** |
| **Refactoring Catalog (Fowler's full list)** | âš ï¸ partial | [Phase 5, Topic 17](./curriculum.md#17-refactoring-techniques) names the smells and gives the decision rule. The full Fowler catalog is the recommended reading; not in the curriculum itself. |
| **Architecture Patterns** (microservices, event-driven, CQRS) | âŒ | **Deliberately omitted** â€” these are *architecture* topics, not *developer-discipline* topics. They belong in the lead-track reading (Phase 7) and in a future architecture curriculum. |
| **Specific frameworks / language idioms** (UI framework hooks, backend framework patterns, mobile framework APIs) | âœ… | The master curriculum is tech-agnostic on purpose. Stack-specific translations live in the [stack-translations/](./stack-translations/) subfolder: [webdev/frontend](./stack-translations/webdev/frontend.md), [webdev/backend](./stack-translations/webdev/backend.md), [mobile/stacks](./stack-translations/mobile/stacks.md). Each topic in the master has a corresponding translation + stack-specific mini-task variant in those docs. |
| **Team-process topics** (standups, retros, planning) | âŒ | **Deliberately omitted** â€” these are *process* topics, not *developer-discipline* topics. Pair with a future process / agile curriculum if the team needs it. |
| **Soft skills** (public speaking, conflict resolution) | âŒ | **Deliberately omitted** â€” out of scope for a developer-discipline curriculum. Pair with a future soft-skills curriculum. |
| **Vendor / cloud-specific content** (AWS, Azure, Vercel, Netlify) | âŒ | **Deliberately omitted** â€” covered in the stack-specific paths where they're used (e.g. [Vercel in Next.js path Phase 10](../../01-software-engineering/web-development/frontend/nextjs/intermediate.md#phase-10-production-readiness)). |

---

## What we deliberately skipped (and why)

The âŒ rows in the table above capture each decision in one line. This section expands the rationale for the trickier ones â€” the cases a reviewer is most likely to push back on. If the table's third column is enough, skip this section.

- **Architecture patterns** (microservices, event-driven, CQRS, serverless) â€” these are *architecture* topics, not developer-discipline topics. The risk of including them is that the curriculum becomes a 200-page book instead of a 6-week run. Pair with a future architecture curriculum.
- **Specific frameworks / language idioms** â€” the curriculum is *tech-agnostic on purpose*. A PHP developer and a React developer should both finish the curriculum with the same vocabulary (SOLID, DRY, idempotency, ADR). Framework-specific content lives in the [tech-specific paths](../../01-software-engineering/web-development/frontend/react/intermediate.md), which layer *on top* of this curriculum.
- **Team-process topics** (standups, retros, sprint planning) â€” these belong in a *process* curriculum, not a *developer-discipline* curriculum. The two often get conflated; the curriculum's stance is to keep them separate.
- **Soft skills** (public speaking, conflict resolution, time management) â€” out of scope. These are real skills; they're not developer-discipline skills. Pair with a future soft-skills curriculum.
- **Full DDD strategic patterns** (bounded contexts, context mapping, aggregates) â€” covered at the *tactical* level (entity vs. value object, ubiquitous language) in [Topic 11](./curriculum.md#11-domain-modeling-basics). The strategic level is a separate discipline; a developer who has finished Topic 11 is *ready* to read a DDD book, not *done* with DDD.
- **Refactoring Catalog (Fowler's full 70+ smells)** â€” the curriculum names the *categories* and gives the *decision rule*. The full catalog is a recommended-reading item, not a topic.
- **Concurrency & threading** â€” *highly* stack-specific (JavaScript's event loop is not Java's threads is not Swift's actors). The right place is in the tech-specific paths where the language forces a specific model. Adding it to the cross-cutting curriculum would force a choice that doesn't apply to half the developers.
- **Observability & monitoring as a stand-alone topic** â€” touched in [Topic 4](./curriculum.md#4-basic-error-handling) and [Topic 14](./curriculum.md#14-performance-awareness). Full coverage lives in the stack-specific paths and in the [REST API Best Practices](../../general/rest-api-best-practices.md). The right level of detail depends on the stack.
- **Security as a stand-alone topic** â€” the curriculum's stance is that it doesn't *teach* security; it *cites* security. The security row in [Topic 19's checklist](./curriculum.md#19-code-review-checklist-standardized) is the entry point; the [Security Audit Checklist](../../audit/security-audit-checklist.md) is the depth; the [Auth/AuthZ phases in the stack paths](../../01-software-engineering/web-development/frontend/nextjs/intermediate.md#phase-7-authentication-and-authorization) are the implementation. Splitting the discipline into a separate topic would risk the "we taught security in the curriculum" trap.

---

## Gaps that should probably be closed before full-team rollout

Six small, targeted additions to a future v0.2 or v0.3:

1. **Concurrency & threading** â€” one or two paragraphs in [Topic 14](./curriculum.md#14-performance-awareness) covering the "what is a thread / event loop / actor" mental model. Defer to v0.2 if a team needs it.
2. **Observability & monitoring one-pager** â€” a one-paragraph pointer in [Topic 4](./curriculum.md#4-basic-error-handling) linking to the [Node.js standards](../../nodejs/nodejs-typescript-best-practices.md) and [Next.js Phase 10](../../01-software-engineering/web-development/frontend/nextjs/intermediate.md#phase-10-production-readiness). Topic 4's "what to log" mini-task covers most of the basics.
3. **Security one-pager** â€” a "when you see a security issue in code review, here's the escalation path" one-liner in [Topic 19](./curriculum.md#19-code-review-checklist-standardized). Links to the [Security Audit Checklist](../../audit/security-audit-checklist.md) and the [AI Era Coding Guidelines](../../general/ai-era-coding-guidelines.md) Red Zone.
4. **DDD strategic patterns pointer** â€” a one-line "if the codebase is large enough to have bounded contexts, see the team's DDD reading list" in [Topic 11](./curriculum.md#11-domain-modeling-basics). Defer to v0.2.
5. **Architecture patterns pointer** â€” a one-line "for microservices / event-driven / CQRS, see Phase 7's reading list" in [Phase 7](./curriculum.md#phase-7-senior-developer-mindset-optional-lead-track). Already implicit; could be made explicit.
6. **Refactoring Catalog reference** â€” a one-line "for the full smell catalog, see Fowler's *Refactoring* (recommended reading)" in [Topic 17](./curriculum.md#17-refactoring-techniques). Already implicit; could be made explicit.

---

## Document control

| Field | Value |
|---|---|
| Document | Developer Excellence Curriculum â€” Gap Analysis |
| Version | 0.4 (v0.3 trimmed the "What we deliberately skipped" expansion to one-liners, dropped the generic "Reviewer questions" section; ~25 lines trimmed) |
| Owner | CoE Web Working Group (with cross-team review from Mobile + Backend) |
| Review Cycle | Quarterly |
| Status | Internal review document |
| Related | [curriculum.md](./curriculum.md), [README.md](./README.md), [how-to-teach.md](./how-to-teach.md), [stack-translations/](./stack-translations/), [React Learning Path](../../01-software-engineering/web-development/frontend/react/intermediate.md), [Next.js Learning Path](../../01-software-engineering/web-development/frontend/nextjs/intermediate.md), [REST API Best Practices](../../general/rest-api-best-practices.md), [Security Audit Checklist](../../audit/security-audit-checklist.md) |
