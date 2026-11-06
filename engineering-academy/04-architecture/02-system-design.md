# 02. System Design

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

System design turns requirements and quality attributes into a structure: which parts the system has, how they
talk, and how it grows. Back to the [roadmap](./README.md).

## Requirements and capacity estimates

Before choosing a design, know how big the problem is. A rough estimate of users, requests and data tells you
whether one server is enough or whether you need to plan for scale.

**What to learn:**

- Turning business numbers (monthly users, peak events) into requests per second, storage and bandwidth
- Separating read traffic from write traffic, because they usually scale differently
- Writing estimates down with their assumptions, so they can be checked later

**Resources:**

- [Back-of-the-envelope estimation](https://github.com/donnemartin/system-design-primer#back-of-the-envelope-calculations),
  in the System Design Primer

**Level:** Practitioner · Core

## Monoliths and microservices

The biggest structural choice is how many deployable parts the system has. A well-structured monolith is the right
start for most client projects; microservices pay off only when teams and scale need independent releases.

**What to learn:**

- Monolith, modular monolith and microservices, and what each costs to build and run
- Drawing module boundaries around business capabilities, so a later split is possible
- The signs that a split is justified: team size, release conflicts, very different scaling needs

**Resources:**

- [Monolith first](https://martinfowler.com/bliki/MonolithFirst.html), Martin Fowler
- [Microservices](https://martinfowler.com/articles/microservices.html), James Lewis and Martin Fowler
- [Microservice architecture patterns](https://microservices.io/patterns/), Chris Richardson

**Level:** Advanced · Core

## Caching

Caching keeps a copy of data closer to where it is needed, so the system does less work. It is the cheapest way to
handle read-heavy traffic, and the easiest way to show users stale data.

**What to learn:**

- Where to cache: the browser, a content delivery network (CDN), the application and the database
- Cache-aside and expiry, and how to invalidate a cached item when the data changes
- What must never be cached, such as one user's private data in a shared cache

**Resources:**

- [Cache-aside pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/cache-aside), Azure
  Architecture Center
- [HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching), MDN

**Level:** Practitioner · Core

## Scaling

When one server is not enough, you add capacity. Doing that safely depends on design choices made much earlier.

**What to learn:**

- Vertical and horizontal scaling, and why stateless application servers make horizontal scaling easy
- Load balancing, and keeping sessions and files out of the application server
- Read replicas and partitioning for the database, and their limits

**Resources:**

- [The Twelve-Factor App](https://12factor.net/), especially the processes and backing services factors
- [Performance efficiency pillar](https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/),
  Azure Well-Architected Framework

**Level:** Practitioner · Core

## Background jobs and queues

Some work should not happen while the user waits: sending emails, resizing images, calling slow systems. Moving it
to background jobs keeps the system fast and lets it absorb peaks.

**What to learn:**

- Queues, workers and scheduled jobs, and when each fits
- Making jobs safe to run twice, because queues can deliver a message more than once
- Watching queue length, so you notice when workers fall behind

**Resources:**

- [Queue-based load leveling pattern](https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling),
  Azure Architecture Center

**Level:** Practitioner · Core

## Project: Design for Ten Times the Users

**Brief:** Lantern expects 50,000 monthly active users, with viral peaks of about 20 times the average. Estimate the
load, find where the current app will break first, and design the structure that will carry it.

**Size:** 3–4 days

**Verification**, checked by an architect or lead:

- [ ] A capacity estimate converts the brief's numbers into peak requests per second, split into reads and writes,
  with every assumption written down
- [ ] A load test of the running app, using a tool such as [k6](https://grafana.com/docs/k6/latest/), shows the
  request rate at which response times or errors first exceed the scenario from stage 01, with the numbers
- [ ] The first bottleneck is named, with evidence from the test, such as a slow query or a saturated CPU
- [ ] An ADR chooses between a monolith, a modular monolith and services for the next year, with at least two
  options compared
- [ ] A caching design states what is cached, where, for how long and how it is invalidated, and what is never
  cached
- [ ] Notification sending is designed as background work, and the design says what happens when a job runs twice
- [ ] An updated container diagram shows the new design

Previous: [01. Architecture Basics](./01-architecture-basics.md) · Next:
[03. API and Integration Architecture](./03-api-and-integration-architecture.md)
