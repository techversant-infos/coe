# 09. Security and Performance

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

A working API is not finished until it is safe and fast under real use. This stage covers the security checks every
Techversant API passes, and finding and fixing what makes a Node.js service slow. Back to the
[roadmap](./README.md).

## Input limits and injection

Every request is untrusted. Limits stop oversized requests, and safe queries stop injection.

**What to learn:**

- Fastify's `bodyLimit`, and limits on list sizes and string lengths in your schemas
- Passing values to the database only as parameters, never by joining strings
- Never copying request data straight into a database update, so a request cannot set fields such as `authorId`
- Treating stored URLs, such as profile images, as untrusted input

**Resources:**

- [SQL and data store injection](../../../../security/audit/security-audit-reference.md#72-sql-and-data-store-injection)
  and [resource exhaustion and limits](../../../../security/audit/security-audit-reference.md#123-resource-exhaustion-and-limits),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## CORS and security headers

Browsers only let a front end on another origin call your API if the API allows it. Security headers protect API
responses, too.

**What to learn:**

- `@fastify/cors` with an allow-list of origins, never allowing every origin with credentials
- `@fastify/helmet`, and the security headers the Techversant audit requires on API and error responses

**Resources:**

- [@fastify/cors](https://github.com/fastify/fastify-cors) and
  [@fastify/helmet](https://github.com/fastify/fastify-helmet)
- [Security headers](../../../../security/audit/security-audit-reference.md#42-security-headers) and
  [CORS](../../../../security/audit/security-audit-reference.md#43-cors), in the Techversant security audit reference

**Level:** Practitioner · Core

## The security audit checklist

Every Techversant pull request is checked against the security audit checklist. Learn it well enough to check your
own work before review.

**What to learn:**

- The checklist's sections, and which ones apply to an API
- Checking dependencies with `npm audit`, and acting on what it finds

**Resources:**

- [Security audit checklist](../../../../security/audit/security-audit-checklist.md), Techversant
- [Security](../../../../standards/nodejs/nodejs-typescript-best-practices.md#security), in the Techversant Node.js
  and TypeScript best practices

**Level:** Practitioner · Core

## Query performance and indexes

Slow APIs are usually slow databases. An index on the right column can turn a query from seconds into milliseconds.

**What to learn:**

- Finding slow queries, and reading `EXPLAIN` output
- Adding indexes in the Prisma schema for the columns you filter, join and sort on, such as `authorId`, the join
  columns for favourites, follows and tags, and `createdAt`. PostgreSQL does not index foreign keys for you.
- Selecting only the fields you need, and paging large result sets

**Resources:** [Indexes](https://www.prisma.io/docs/orm/prisma-schema/data-model/indexes), Prisma documentation

**Level:** Advanced · Core

## The event loop under load

One slow, CPU-heavy function blocks every other request on the same process. Under load, this shows up as slow
responses everywhere.

**What to learn:**

- Measuring event loop delay with `perf_hooks.monitorEventLoopDelay`
- Moving CPU-heavy work, such as image processing, to worker threads or a queue
- Load testing with a tool such as k6, and reading response time percentiles against a target

**Resources:**

- [Don't block the event loop](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop), Node.js
  documentation
- [k6 documentation](https://grafana.com/docs/k6/latest/)

**Level:** Advanced · Core

## Profiling

A CPU profile shows which functions use the most time, so you fix the real cause instead of guessing.

**What to learn:**

- Recording a CPU profile with `node --cpu-prof`, and reading it in Chrome DevTools

**Resources:** [Profiling Node.js applications](https://nodejs.org/en/learn/getting-started/profiling), Node.js
documentation

**Level:** Advanced · Optional

## Project: Harden and Speed Up the API

**Brief:** Check your API against the Techversant security audit checklist and fix what you find. Then load test the
article list and feed, find the slowest parts, and make them faster.

**Size:** 3 days

**Verification**, checked by a reviewer:

- [ ] The security audit checklist is filled in for the API, with every applicable item passed or fixed
- [ ] `npm audit` reports no known high or critical vulnerabilities
- [ ] A test shows that a request cannot change an article's author, and an oversized body returns 413
- [ ] CORS allows only the configured front-end origins, and API and error responses carry the required headers
- [ ] The pull request shows `EXPLAIN ANALYZE` output before and after for the article list and feed, on a seed of
  about 100,000 articles, with the indexes added
- [ ] A k6 load test of `GET /api/articles` meets the target agreed with your reviewer, with event loop delay
  recorded, and the script and results are in the repository

Previous: [08. Testing](./08-testing.md) · Next: [10. Deployment and Operations](./10-deployment-and-operations.md)
