# 07. Background Jobs and Caching

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Slow work, such as sending email or calling another system, should not make users wait. Queues move it to the
background, and caching avoids doing the same expensive work twice. Back to the [roadmap](./README.md).

## Queues with BullMQ

BullMQ keeps jobs in Redis until a worker process runs them. Workers run separately from the API, so slow jobs never
hold up requests.

**What to learn:**

- Adding jobs to a queue from the API, and running a worker in its own process
- Retries with back-off, timeouts, and what happens to a job that keeps failing
- Writing jobs that are safe to run twice, because a job can run more than once

**Resources:**

- [BullMQ guide](https://docs.bullmq.io/guide/introduction)
- [Messaging and jobs](../../../../standards/nodejs/nodejs-typescript-best-practices.md#messaging--jobs), in the
  Techversant Node.js and TypeScript best practices

**Level:** Practitioner · Core

## Events and email

When something happens, such as a new follower, the API records it and a job sends the email. If the job is queued
in the same request that changes the data, one can succeed while the other fails.

**What to learn:**

- Sending email from a worker with a library such as Nodemailer, and testing it locally with a tool such as Mailpit
- The outbox pattern: saving the event in the same database transaction as the change, and queuing it from there
- Keeping personal data out of job data where you can, by passing IDs instead

**Resources:**

- [Nodemailer](https://nodemailer.com/)
- [Messaging and jobs](../../../../standards/nodejs/nodejs-typescript-best-practices.md#messaging--jobs), in the
  Techversant Node.js and TypeScript best practices

**Level:** Practitioner · Core

## Scheduled jobs

Some work runs on a timetable, such as a nightly clean-up. BullMQ's job schedulers add a job on a fixed schedule,
and only one copy runs even when several workers are running.

**What to learn:**

- Creating a job scheduler with `upsertJobScheduler` and a cron pattern
- Why scheduling with `setInterval` in the API process breaks when you run more than one copy

**Resources:** [Job schedulers](https://docs.bullmq.io/guide/job-schedulers), BullMQ documentation

**Level:** Practitioner · Core

## Caching with Redis

A cache keeps the result of slow work for a while. The hard part is removing it when the data changes.

**What to learn:**

- Reading and writing cached values with a time to live, and choosing keys
- Removing cached values when the data changes, and the risks of serving stale data
- Never caching one user's data where another user can read it

**Resources:**

- [Redis documentation](https://redis.io/docs/latest/develop/)
- [Performance](../../../../standards/nodejs/nodejs-typescript-best-practices.md#performance), in the Techversant
  Node.js and TypeScript best practices

**Level:** Practitioner · Core

## Queue dashboards

A dashboard shows waiting, active and failed jobs, and lets you retry a failed one.

**What to learn:**

- Running a dashboard such as Bull Board, and protecting it in production

**Resources:** [Bull Board](https://github.com/felixmosh/bull-board)

**Level:** Advanced · Optional

## Project: Add Notifications and Caching

**Brief:** Email users when someone follows them, through a queued job. Cache the tag list and clear it when articles
change. Schedule a nightly job that deletes tags no article uses.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Following a user queues a job, and the email arrives in Mailpit when the worker runs
- [ ] The job has retries with back-off and a timeout, a job that keeps failing is kept for inspection, and running
  it twice sends one email
- [ ] The job data holds IDs, not email addresses or other personal data
- [ ] `GET /api/tags` is served from the cache, and creating, updating or deleting an article, or the nightly
  clean-up, updates the list straight away
- [ ] The nightly clean-up runs from a BullMQ job scheduler, not from a timer in the API process
- [ ] Tests check what was queued, without a real Redis server or email
- [ ] All 13 RealWorld API test files still pass

Previous: [06. Authentication and Authorization](./06-authentication-and-authorization.md) · Next:
[08. Testing](./08-testing.md)
