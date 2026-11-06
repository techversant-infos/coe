# 03. API and Integration Architecture

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

APIs and integrations are the contracts between parts of a system and between systems. Once other teams and clients
depend on them, they are the hardest part to change. Back to the [roadmap](./README.md).

## API contracts and versioning

An API contract is a promise to every client that calls it. Design it deliberately, write it down before building,
and plan how it will change.

**What to learn:**

- Designing resources, methods, status codes and error responses to the Techversant standard
- Writing the contract first, as an OpenAPI file, and reviewing it before code
- Versioning rules: what counts as a breaking change, and how long an old version stays

**Resources:**

- [REST API Best Practices](../../standards/general/rest-api-best-practices.md), Techversant's API standard,
  including [versioning](../../standards/general/rest-api-best-practices.md#21-versioning-strategy-mandatory)
- [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)

**Level:** Advanced · Core

## Calls and messages

Parts of a system talk either by calling each other and waiting, or by sending messages and moving on. The choice
decides how failures spread.

**What to learn:**

- When a direct call fits, and when a message fits
- How one slow service can slow every service that calls it, and how messages stop that
- The cost of asynchronous designs: harder debugging and results that arrive later

**Resources:**

- [Asynchronous request-reply pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/async-request-reply),
  Azure Architecture Center

**Level:** Practitioner · Core

## Messaging and events

Events announce that something happened, such as "article published", so other parts can react without the
publisher knowing about them. They make systems easier to extend, and harder to follow.

**What to learn:**

- The difference between a command ("send this email") and an event ("article published")
- Designing event contents and documenting them, for example with AsyncAPI
- Delivery guarantees, duplicate messages and ordering, and how consumers cope with each

**Resources:**

- [What do you mean by "event-driven"?](https://martinfowler.com/articles/201701-event-driven.html), Martin Fowler
- [AsyncAPI documentation](https://www.asyncapi.com/docs)

**Level:** Advanced · Core

## Integration patterns

Client systems connect through APIs, webhooks, files, queues and batch jobs. The right pattern is the one both
sides can build, support and monitor.

**What to learn:**

- The common patterns and when each fits
- Retries, timeouts and idempotency keys, so a repeated request does no harm
- File and batch integrations, which many clients still depend on

**Resources:**

- [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/), Gregor Hohpe and Bobby Woolf
- [Idempotency for POST](../../standards/general/rest-api-best-practices.md#31-idempotency-for-post), in the
  Techversant API standard

**Level:** Practitioner · Core

## Backward compatibility

The mobile app in an old user's pocket will call your API for months after you change it. Every change must work for
the clients that have not updated yet.

**What to learn:**

- Additive changes that are safe, and changes that break existing clients
- Running two versions side by side, and retiring the old one with notice
- Contract tests that fail when a change breaks an existing client

**Resources:**

- [Versioning strategy](../../standards/general/rest-api-best-practices.md#21-versioning-strategy-mandatory), in the
  Techversant API standard
- [Parallel change](https://martinfowler.com/bliki/ParallelChange.html), Danilo Sato

**Level:** Advanced · Core

## Project: Design the Mobile and Notifications APIs

**Brief:** Lantern's mobile app will use the same API as the website, and users want notifications. Design the API
changes and the notification flow, without breaking the existing web front end.

**Size:** 3–4 days

**Verification**, checked by an architect or lead:

- [ ] An OpenAPI file describes every new or changed endpoint, and follows the Techversant REST standard for naming,
  errors and pagination
- [ ] The existing RealWorld API tests still pass against a back end that implements at least one new endpoint
- [ ] A versioning plan states which changes are additive, which would break clients, and how long an old version
  stays supported
- [ ] An event design lists each notification event, its contents, who publishes it and who consumes it
- [ ] The design states what happens when the email or push provider is down, and when the same event arrives twice
- [ ] An ADR records the choice between direct calls and messages for notifications, with at least two options
  compared
- [ ] A sequence diagram shows the path from "article published" to a push notification on a follower's phone

Previous: [02. System Design](./02-system-design.md) · Next: [04. Data Architecture](./04-data-architecture.md)
