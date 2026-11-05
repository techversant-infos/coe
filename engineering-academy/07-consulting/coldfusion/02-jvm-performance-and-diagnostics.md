# 02. JVM, Performance and Diagnostics

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

Every CFML engine runs on the Java Virtual Machine (JVM). Slow pages, crashes and memory problems are usually solved
by reading JVM and database evidence, not by guessing at settings. Back to the [roadmap](./README.md).

## Request lifecycle

Know what happens between the HTTP request and the response: the web server connector, `Application.cfc` events,
includes, custom tags and components.

**What to learn:**

- The order of `onApplicationStart`, `onSessionStart`, `onRequestStart`, `onRequest` and `onRequestEnd`
- How includes and custom tags change the execution path
- Adding a correlation ID so one request can be followed through the logs

**Resources:** [Deep expertise guide, section 1](./reference/coldfusion-deep-expertise-guide.md#1-trace-a-cfml-request-from-http-to-response)

**Level:** Practitioner · Core

## JVM memory and garbage collection

Most "ColdFusion is slow" reports end up being memory pressure or garbage collection pauses.

**What to learn:**

- Heap, metaspace (where the JVM keeps class definitions) and thread stacks, and what fills each
- Garbage collection basics and how to read GC logs
- Setting `-Xms` and `-Xmx` from evidence, and changing one setting at a time

**Resources:**

- [Deep expertise guide, section 2](./reference/coldfusion-deep-expertise-guide.md#2-explain-how-coldfusion-interacts-with-the-jvm)
- [Deep expertise guide, section 3](./reference/coldfusion-deep-expertise-guide.md#3-configure-and-tune-jvm-settings-for-coldfusion)

**Level:** Advanced · Core

## Thread dumps and heap dumps

Thread dumps show what every request is doing at one moment. Heap dumps show what is holding memory.

**What to learn:**

- Taking several thread dumps a few seconds apart and comparing them
- Spotting blocked threads, slow queries and calls to external services
- Taking a heap dump safely and finding what retains memory

**Resources:** [Deep expertise guide, section 7](./reference/coldfusion-deep-expertise-guide.md#7-use-built-in-diagnostics-and-debugging-tools)

**Level:** Advanced · Core

## Application monitoring

Monitoring tools show slow requests, slow queries and memory over time, which turns a vague complaint into evidence.

**What to learn:**

- FusionReactor, a commercial monitor used widely with CFML
- Adobe's free Performance Monitoring Toolset for ColdFusion, installed separately
- Slow request logging in the engine's administrator

**Resources:**

- [Deep expertise guide, section 7](./reference/coldfusion-deep-expertise-guide.md#7-use-built-in-diagnostics-and-debugging-tools)
- [FusionReactor](https://www.fusion-reactor.com/)

**Level:** Practitioner · Core

## Database access and connection pools

Database calls are the most common cause of slow CFML pages.

**What to learn:**

- Reading query plans and adding the right index
- Finding and removing N+1 queries, where a loop runs one query per row
- Sizing the connection pool and keeping transactions short

**Resources:** [Deep expertise guide, section 6](./reference/coldfusion-deep-expertise-guide.md#6-optimize-database-interactions-and-connection-pooling)

**Level:** Practitioner · Core

## Caching

The right cache removes repeated work; the wrong one serves stale or private data.

**What to learn:**

- Choosing the cache layer: query, object, page, HTTP or a shared cache such as Redis
- Cache keys, expiry and clearing the cache after a write
- Preventing many requests rebuilding the same cache entry at once

**Resources:** [Deep expertise guide, section 4](./reference/coldfusion-deep-expertise-guide.md#4-implement-advanced-caching-strategies)

**Level:** Practitioner · Core

## Load testing

A load test shows how the application behaves before real users find out, and proves whether a fix helped.

**What to learn:**

- Writing a repeatable test for the busiest user journeys
- Recording a baseline before you change anything
- Comparing response times and error rates before and after a change

**Resources:** [Apache JMeter](https://jmeter.apache.org/), [Grafana k6](https://grafana.com/docs/k6/latest/)

**Level:** Practitioner · Core

## Project: Find and Fix a Performance Problem

**Brief:** Load test the practice app, find its slowest user journey, and fix the cause. Prove the improvement with
numbers. Run the test on Lucee, or on a trial or licensed Adobe server: the free Developer edition is licensed for
development only and has usage limits, so its load results are not reliable.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] A load test script for at least three journeys is in the repository and runs with one command
- [ ] A baseline report shows response times (median and 95th percentile) and error rate
- [ ] Three thread dumps taken during the test, with a written explanation of what the busy threads were doing
- [ ] The cause of the slowest journey is identified with evidence: a query plan, a monitor trace or a thread dump
- [ ] After one change, the same test shows the improvement, and nothing else got worse
- [ ] A short note says why you changed that one thing and not a JVM setting, or why the JVM setting was right

Previous: [01. CFML and the Platform](./01-cfml-and-the-platform.md) · Next: [03. Security and Hardening](./03-security-and-hardening.md)
