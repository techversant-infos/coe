# 07. Background Jobs and Caching

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Slow work, such as sending email or calling another system, should not make users wait. A job queue moves it to the
background, and caching avoids doing the same expensive work twice. This path uses Hangfire, which keeps its jobs in
the database. Back to the [roadmap](./README.md).

## Background services

A `BackgroundService` runs work inside the app for as long as the app is running. It suits work that may be lost on a
restart, such as refreshing a cache.

**What to learn:**

- `BackgroundService` and hosted services, and stopping cleanly when the app shuts down
- Creating a scope for each piece of work, because the database context is a scoped service
- Why work that must not be lost needs a job queue instead

**Resources:**
[Background tasks with hosted services](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/hosted-services),
Microsoft Learn

**Level:** Practitioner · Core

## Job queues with Hangfire

Hangfire stores each job in the database until a worker finishes it, and retries jobs that fail.

**What to learn:**

- Queuing jobs with Hangfire, storing them in PostgreSQL, and running the Hangfire server in the app or a separate
  worker
- Automatic retries, failed jobs, and the Hangfire dashboard, which must be protected
- Writing jobs that are safe to run twice, because a job can run more than once

**Resources:** [Hangfire documentation](https://docs.hangfire.io/en/latest/)

**Level:** Practitioner · Core

## Events and email

If a job is queued before the database change commits, a worker can act on data that was never saved.

**What to learn:**

- Queuing jobs only after `SaveChanges` succeeds, and the outbox pattern for when a job must never be lost
- Sending email with a library such as MailKit, and testing it locally with a tool such as Mailpit
- Passing IDs in jobs, not personal data

**Resources:** [MailKit](https://github.com/jstedfast/MailKit)

**Level:** Practitioner · Core

## Scheduled jobs

Some work runs on a timetable, such as a nightly clean-up. When the app runs on more than one server, only one copy
of a job should run.

**What to learn:**

- Hangfire's recurring jobs, with a cron schedule
- How Hangfire makes sure each scheduled run happens once, even with several servers

**Resources:**
[Recurrent tasks](https://docs.hangfire.io/en/latest/background-methods/performing-recurrent-tasks.html), Hangfire
documentation

**Level:** Practitioner · Core

## Caching

A cache keeps the result of slow work for a while. The hard part is removing it when the data changes.

**What to learn:**

- `HybridCache`, which keeps values in memory and in Redis, and protects against many requests rebuilding the same
  value at once
- Removing cached values when the data changes, with keys or tags, and the risks of serving stale data. Removal
  reaches the local memory and Redis but not other servers' memory, so keep the local expiry short, or turn off
  the local cache, for data that must update straight away.
- Never caching one user's data where another user can read it

**Resources:**
[HybridCache](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/hybrid), Microsoft Learn

**Level:** Practitioner · Core

## Message brokers

Some systems pass work between services through a message broker, such as RabbitMQ.

**What to learn:**

- Sending and receiving messages with RabbitMQ, and how a broker compares with a database-backed job queue

**Resources:** [RabbitMQ tutorial for .NET](https://www.rabbitmq.com/tutorials/tutorial-one-dotnet), RabbitMQ

**Level:** Advanced · Optional

## Project: Add Notifications and Caching

**Brief:** Email users when someone follows them, through a Hangfire job queued after the change is saved. Cache the
tag list and clear it when articles change. Schedule a nightly recurring job that deletes tags no article uses.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Following a user queues a job only after the change is saved, and the email arrives in Mailpit when the job
  runs
- [ ] A job that fails is retried, a job that keeps failing is kept as failed for inspection, and running a job
  twice sends one email
- [ ] Jobs hold IDs, not email addresses or other personal data
- [ ] `GET /api/tags` is served from the cache, and creating, updating or deleting an article, or the nightly
  clean-up, updates the list straight away
- [ ] The nightly clean-up is a recurring job that runs once per schedule, even with two servers running
- [ ] The Hangfire dashboard is not reachable without signing in
- [ ] Tests check that each job was queued, with a test double for the job client
- [ ] All 13 RealWorld API test files still pass

Previous: [06. Authentication and Authorization](./06-authentication-and-authorization.md) · Next:
[08. Testing](./08-testing.md)
