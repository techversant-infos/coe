# 02. Full-Stack Delivery

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

FDEs deliver whole features, from the database to the screen. Back to the [roadmap](./README.md).

## TypeScript

The main language used in this roadmap's projects: one strictly typed language for the UI, the API and
background jobs.

**What to learn:**

- `strict` mode, types for API inputs and outputs, `null` handling
- Modules, async code and error handling
- Reading type errors instead of silencing them

**Resources:**

- [Node.js and TypeScript Best Practices](../../standards/nodejs/nodejs-typescript-best-practices.md)
- [TypeScript documentation](https://www.typescriptlang.org/docs/)

**Level:** Practitioner · Core

## Python

Python is the second language in this roadmap.
Most AI and data tools support it first, and many client teams build in it.

**What to learn:**

- Virtual environments and installing packages
- Reading and changing client scripts
- Data scripts and notebooks for quick analysis
- The Python SDKs of the AI providers you use

**Resources:** [The Python Tutorial](https://docs.python.org/3/tutorial/)

**Level:** Practitioner · Core

## React and Next.js

Most client-facing work needs a UI: an internal tool, a review screen for AI output, a dashboard.

**What to learn:**

- Components, state, forms and data fetching
- Server and client rendering in Next.js
- Accessible, usable screens for non-technical users

**Resources:**

- [React learning path](../01-software-engineering/01-web-development/01-frontend/01-react/README.md)
- [Next.js learning path](../01-software-engineering/01-web-development/01-frontend/02-nextjs/README.md)
- [React documentation](https://react.dev/learn)

**Level:** Practitioner · Core

## Node.js APIs

APIs connect the UI, the AI features and the client's systems.

**What to learn:**

- Express or a similar framework in TypeScript
- Input validation, error responses and structured logs
- Background jobs and scheduled tasks

**Resources:**

- [Backend path](../01-software-engineering/01-web-development/02-backend/README.md)
- [Node.js and TypeScript Style Guide](../../standards/nodejs/nodejs-typescript-style-guide.md)
- [Node.js documentation](https://nodejs.org/en/learn)

**Level:** Practitioner · Core

## API design

Client systems will call your API, sometimes for years after you leave. A clear, stable API is part of a good
handover.

**What to learn:**

- Resource naming, status codes and error formats
- Pagination, filtering and versioning
- Changing an API without breaking existing callers

**Resources:** [REST API Best Practices](../../standards/general/rest-api-best-practices.md)

**Level:** Practitioner · Core

## PostgreSQL and migrations

A common choice for new builds, and the database used in this roadmap's projects. With the pgvector extension
it can also hold the vector search behind AI features.

**What to learn:**

- Tables, indexes, constraints and transactions
- Writing and testing migrations; rolling them back
- Production database migrations are Red Zone: write them by hand, without AI generation, and have a senior
  engineer review them

**Resources:**

- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
- [AI Era Coding Guidelines: Red Zone](../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only)

**Level:** Practitioner · Core

## Automated testing

Tests are how you prove to the client, and to yourself, that the change works and keeps working.

**What to learn:**

- Unit, integration and end-to-end tests, and when each is worth it
- Tests that fail when the code is wrong
- Tests for code you inherited, before you change it

**Resources:**

- [Developer Excellence Curriculum](../00-engineering-foundations/05-dev-excellence/01-curriculum.md)
- [Vitest guide](https://vitest.dev/guide/), [Playwright documentation](https://playwright.dev/docs/intro)

**Level:** Practitioner · Core

## Code review

On an engagement you review your own agent's output, your colleagues' work and sometimes the client's code.

**What to learn:**

- Finding material issues first: correctness, security, data handling
- Reviewing AI-written changes as carefully as human ones
- Writing review comments people can act on

**Resources:** [Node.js and TypeScript Code Review Checklist](../../standards/nodejs/nodejs-typescript-code-review-checklist.md)

**Level:** Practitioner · Core

## Data structures and algorithms

Enough to choose a sensible approach, spot slow code and pass technical interviews.

**What to learn:**

- Arrays, maps, sets, trees and queues, and when to use each
- Big-O reasoning for loops and queries
- Sorting, searching and recursion

**Resources:** [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)

**Level:** Practitioner · Optional

## System design

Choosing an architecture that fits the client's size, budget and team, not the most impressive one.

**What to learn:**

- Monolith or services, synchronous or queued, cache or not
- Designing for failure: timeouts, retries, idempotency
- Explaining a design and its trade-offs to the client

**Resources:**

- [Architecture](../04-architecture/README.md) (planned academy path)
- [The System Design Primer](https://github.com/donnemartin/system-design-primer)

**Level:** Advanced · Core

## Project: Build a Service Request Tracker

**Brief:** Build a small full-stack application: a Next.js UI, a Node.js API in TypeScript and a PostgreSQL
database. Users create, list, filter (by status and assignee) and close requests. Keep it: later projects build on it.

**Size:** 4–6 days

**Verification**, checked by a reviewer:

- [ ] The API follows the [REST API Best Practices](../../standards/general/rest-api-best-practices.md): malformed
  JSON returns `400`, invalid fields return `422`, and both use the standard's error format
- [ ] Every database change is a migration that applies and rolls back cleanly on an empty database
- [ ] Unit tests cover the business rules, integration tests run against a real test database, and one Playwright test
  creates and closes a request
- [ ] Breaking a business rule on purpose makes at least one test fail
- [ ] A reviewer works through the [code review checklist](../../standards/nodejs/nodejs-typescript-code-review-checklist.md)
  and no material issue is left open
- [ ] A one-page design note explains the architecture and one trade-off you made, and why
- [ ] A new engineer runs the application locally from the README without asking you anything

Previous: [01. Engineering Foundations](./01-engineering-foundations.md) · Next: [03. Data](./03-data.md)
