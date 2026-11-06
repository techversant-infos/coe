# 07. Background Jobs and Caching

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Slow work, such as sending email or calling another system, should not make users wait. A message broker moves it to
the background, and caching avoids doing the same expensive work twice. Back to the [roadmap](./README.md).

## Messages with RabbitMQ

Spring's `@Async` runs work on another thread, but the work is lost if the app stops. For work that must not be
lost, send a message to a broker such as RabbitMQ, and let a listener process it.

**What to learn:**

- Sending messages with `RabbitTemplate` from Spring AMQP (Advanced Message Queuing Protocol), and receiving them with
  `@RabbitListener`
- Retries with back-off, and a dead-letter queue for messages that keep failing
- Writing listeners that are safe to run twice, because a message can arrive more than once

**Resources:** [AMQP](https://docs.spring.io/spring-boot/reference/messaging/amqp.html), Spring Boot documentation

**Level:** Practitioner · Core

## Events and email

If a message is sent before the database change commits, a listener can act on data that was never saved.
Transaction-bound events solve this.

**What to learn:**

- Publishing application events, and `@TransactionalEventListener` with the after-commit phase
- The outbox pattern, for when a message must never be lost even if the broker is down
- Sending email with Spring's mail support, and testing it locally with a tool such as Mailpit
- Passing IDs in messages, not personal data

**Resources:**
[Transaction-bound events](https://docs.spring.io/spring-framework/reference/data-access/transaction/event.html),
Spring Framework documentation

**Level:** Practitioner · Core

## Scheduled tasks

Some work runs on a timetable, such as a nightly clean-up. When the app runs on more than one server, only one copy
of a task should run.

**What to learn:**

- `@Scheduled` with a cron expression, and turning scheduling on
- A lock, for example with ShedLock, so only one server runs each task

**Resources:**

- [Task execution and scheduling](https://docs.spring.io/spring-boot/reference/features/task-execution-and-scheduling.html),
  Spring Boot documentation
- [ShedLock](https://github.com/lukas-krecan/ShedLock)

**Level:** Practitioner · Core

## Caching

A cache keeps the result of slow work for a while. The hard part is removing it when the data changes.

**What to learn:**

- Spring's cache abstraction with `@Cacheable` and `@CacheEvict`, backed by Redis
- Removing cached values when the data changes, and the risks of serving stale data
- Never caching one user's data where another user can read it
- A JSON serializer for the Redis cache, and why calling a `@Cacheable` method from the same class skips the cache

**Resources:** [Caching](https://docs.spring.io/spring-boot/reference/io/caching.html), Spring Boot documentation

**Level:** Practitioner · Core

## Background job libraries

Some projects use a job library, such as JobRunr, which stores jobs in the database and comes with a dashboard.

**What to learn:**

- How a database-backed job library compares with a message broker

**Resources:** [JobRunr](https://www.jobrunr.io/en/documentation/)

**Level:** Advanced · Optional

## Project: Add Notifications and Caching

**Brief:** Email users when someone follows them, through a RabbitMQ message sent after the change commits. Cache the
tag list and clear it when articles change. Schedule a nightly task that deletes tags no article uses.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Following a user sends a message after the transaction commits, and the email arrives in Mailpit when the
  listener runs
- [ ] The listener retries with back-off, a message that keeps failing goes to a dead-letter queue, and receiving it
  twice sends one email
- [ ] Messages hold IDs, not email addresses or other personal data
- [ ] `GET /api/tags` is served from the cache, and creating, updating or deleting an article, or the nightly
  clean-up, updates the list straight away
- [ ] The nightly clean-up holds a lock, so only one server runs it
- [ ] Tests check what was sent, with RabbitMQ started by Testcontainers or a test double
- [ ] All 13 RealWorld API test files still pass

Previous: [06. Authentication and Authorization](./06-authentication-and-authorization.md) · Next:
[08. Testing](./08-testing.md)
