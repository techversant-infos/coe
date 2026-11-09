# 07. Background Jobs and Caching

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Slow work, such as sending email or calling another system, should not make users wait. A job queue moves it to the
background, and caching avoids doing the same expensive work twice. This path uses River, a job queue that keeps its
jobs in PostgreSQL. Back to the [roadmap](./README.md).

## Job queues with River

Starting a goroutine with `go sendEmail()` is quick to write, but the work is lost if the server stops. A job queue
stores the work until a worker finishes it.

**What to learn:**

- Creating River's tables by exporting its SQL with `river migrate-get` into goose migrations
- River workers with typed job arguments, and queues with a set number of workers
- Retries with back-off, and what River does with a job that keeps failing
- Writing workers that are safe to run twice, because a job can run more than once

**Resources:**

- [River documentation](https://riverqueue.com/docs)
- [Job retries](https://riverqueue.com/docs/job-retries), River documentation

**Level:** Practitioner · Core

## Jobs and email

If a job is queued before the database change commits, a worker can act on data that was never saved. Because River
keeps jobs in PostgreSQL, a job can be inserted in the same transaction as the change.

**What to learn:**

- Inserting a job inside your transaction, so the job exists only if the change commits
- Sending email from a worker, and testing it locally with a tool such as Mailpit
- Passing IDs in jobs, not personal data

**Resources:**
[Transactional enqueueing](https://riverqueue.com/docs/transactional-enqueueing), River documentation

**Level:** Practitioner · Core

## Scheduled jobs

Some work runs on a timetable, such as a nightly clean-up. When the app runs on more than one server, only one copy
of a job should run.

**What to learn:**

- River's periodic jobs, with a schedule set in code
- How River elects one server as the leader, which alone queues periodic jobs

**Resources:** [Periodic jobs](https://riverqueue.com/docs/periodic-jobs), River documentation

**Level:** Practitioner · Core

## Caching with Redis

A cache keeps the result of slow work for a while. The hard part is removing it when the data changes.

**What to learn:**

- Reading and writing Redis with go-redis, with an expiry on every key, read and write timeouts set, and
  `ContextTimeoutEnabled` on so request deadlines apply
- Removing cached values when the data changes, and the risks of serving stale data
- Never caching one user's data where another user can read it

**Resources:** [Go client for Redis](https://redis.io/docs/latest/develop/clients/go/), Redis documentation

**Level:** Practitioner · Core

## Worker pools

Some work runs inside the process, such as calling several services at once. A worker pool keeps the number of
goroutines under control.

**What to learn:**

- Running a fixed number of goroutines that read from a channel, and stopping them when the context is cancelled
- Collecting the first error from a group of goroutines with the errgroup package

**Resources:** [Pipelines and cancellation](https://go.dev/blog/pipelines), the Go blog

**Level:** Advanced · Optional

## Project: Add Notifications and Caching

**Brief:** Email users when someone follows them, through a River job inserted in the same transaction as the follow.
Cache the tag list in Redis and clear it when articles change. Add a nightly periodic job that deletes tags no
article uses.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Following a user inserts a job in the same transaction, a follow that fails leaves no job, and the email
  arrives in Mailpit when the worker runs
- [ ] The worker retries with back-off, a job that keeps failing stops after a set number of attempts and is kept
  for inspection, and running a job twice sends one email
- [ ] Jobs hold IDs, not email addresses or other personal data
- [ ] `GET /api/tags` is served from the cache, and creating, updating or deleting an article, or the nightly
  clean-up, updates the list straight away
- [ ] The nightly clean-up is a River periodic job, so only one server queues it
- [ ] Tests check that each job was inserted, for example with River's test helpers
- [ ] All 13 RealWorld API test files still pass

Previous: [06. Authentication and Authorization](./06-authentication-and-authorization.md) · Next:
[08. Testing](./08-testing.md)
