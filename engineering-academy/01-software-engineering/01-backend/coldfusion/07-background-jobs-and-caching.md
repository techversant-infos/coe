# 07. Background Jobs and Caching

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-20 · **Next review:** 2027-05-20

Slow work, such as sending email, should not make a user wait. Some work belongs at a set time, and a cache keeps
answers that are expensive to build. Each needs care, because a job can run twice and a cache can go stale. Back to the
[roadmap](./README.md).

## Scheduled tasks

Scheduled tasks run work at set times, such as a nightly report or a clean-up of expired tokens.

**What to learn:**

- The ColdBox scheduler: tasks in `config/Scheduler.cfc`, their frequency, and what happens when one fails
- `<cfschedule>` and tasks set up in the engine's administrator, which you find in older applications
- Running a task on only one server when the application runs on several

**Resources:**

- [Scheduled tasks](https://coldbox.ortusbooks.com/digging-deeper/scheduled-tasks), ColdBox documentation
- [cfschedule](https://docs.lucee.org/reference/tags/schedule.html), Lucee documentation

**Level:** Practitioner · Core

## Background jobs and idempotency

A background job runs outside the request, so the user gets a fast response. Jobs can fail and run again, so each
one must be safe to repeat: idempotent.

**What to learn:**

- Running work in the background with ColdBox's async features, and queues with the cbq module and a provider
  that runs jobs in the background, such as the database provider
- Retries, timeouts, and recording failed jobs, which cbq does only when failed-job logging is turned on
- Making a job idempotent with a unique key, so running it twice sends one email
- Passing IDs to a job, not email addresses or other personal data

**Resources:**

- [Async programming](https://coldbox.ortusbooks.com/digging-deeper/promises-async-programming), ColdBox
  documentation
- [cbq](https://cbq.ortusbooks.com/) and [Failed jobs](https://cbq.ortusbooks.com/jobs/failed-jobs), Ortus
  documentation

**Level:** Advanced · Core

## Sending email

Email leaves your system for good, so test it against a local mail catcher that never delivers, and keep the sending
code in one place.

**What to learn:**

- `cfmail` in script and tags, and the cbmailservices module for ColdBox
- A local mail catcher, such as Mailpit, for development and tests
- Plain-text and HTML parts, and keeping personal data out of logs

**Resources:**

- [cfmail](https://docs.lucee.org/reference/tags/mail.html), Lucee documentation
- [cbmailservices](https://coldbox-mailservices.ortusbooks.com/), Ortus documentation
- [Mailpit](https://mailpit.axllent.org/)

**Level:** Practitioner · Core

## Caching with CacheBox

A cache keeps a result so the next request does not rebuild it. The hard part is knowing when the cached result is
out of date.

**What to learn:**

- CacheBox: getting a cache, `getOrSet()`, and timeouts
- Cache keys that include everything the result depends on, such as the user or the filters
- Clearing a cached result when the data behind it changes
- Why the `application` scope is not a cache, and why a cache shared by several servers needs an external store

**Resources:**
[CacheBox overview](https://cachebox.ortusbooks.com/getting-started/overview), Ortus documentation

**Level:** Practitioner · Core

## Locking and shared state

Many requests run at the same time. Two of them can change the same data at once, such as a double favourite, or
read a shared scope while another request is writing it.

**What to learn:**

- Which scopes are shared between requests: `application`, `server` and `session`
- `<cflock>` and `lock` in script, named and scope locks, and keeping locked code short
- Letting the database prevent duplicates with a unique constraint, instead of a lock, when several servers run
  the application

**Resources:** [cflock](https://docs.lucee.org/reference/tags/lock.html), Lucee documentation

**Level:** Advanced · Core

## Project: Add Notifications, Caching and a Nightly Report

**Brief:** Email users when someone follows them, through a background job. Cache the tag list and clear it when
articles change. Schedule a nightly task that removes expired tokens and writes a short report of new articles.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Following a user sends an email through a background job, and the email arrives in Mailpit
- [ ] The job has retries and a timeout, a failed job is recorded, and running it twice sends one email
- [ ] Favouriting the same article twice at the same moment stores one favourite
- [ ] The job receives IDs, not email addresses or other personal data
- [ ] `GET /api/tags` is served from the cache, and creating, updating or deleting an article updates the list
  straight away
- [ ] The scheduler runs the nightly task, the task is safe to run twice, and its failures are logged
- [ ] Tests check what was queued, sent and cached, without sending real email
- [ ] All 13 RealWorld API test files still pass

Previous: [06. Authentication and Authorization](./06-authentication-and-authorization.md) · Next:
[08. Testing](./08-testing.md)
