# 07. Background Jobs and Caching

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Slow work, such as sending email or calling another system, should not make users wait. Queues move it to the
background, and caching avoids doing the same expensive work twice. Back to the [roadmap](./README.md).

## Queues and jobs

A job is a class that does one piece of work. A queue holds jobs until a worker process runs them.

**What to learn:**

- Creating jobs, dispatching them, and running a worker with `queue:work`
- Choosing a queue driver: database for small projects, Redis for larger ones
- Retries, back-off and timeouts, including the `#[Tries]`, `#[Backoff]` and `#[Timeout]` attributes added in
  Laravel 13
- Failed jobs, and writing jobs that are safe to run twice

**Resources:** [Queues](https://laravel.com/docs/13.x/queues), Laravel documentation

**Level:** Practitioner · Core

## Events, notifications and mail

Events announce that something happened, such as a new follower. Listeners and notifications react to them, often
through the queue.

**What to learn:**

- Events and listeners, and queuing a listener
- Notifications that send email, and testing email locally with a tool such as Mailpit
- Keeping personal data out of job payloads where you can, by passing IDs instead

**Resources:**

- [Events](https://laravel.com/docs/13.x/events) and [Notifications](https://laravel.com/docs/13.x/notifications),
  Laravel documentation

**Level:** Practitioner · Core

## Task scheduling

The scheduler runs commands on a timetable, such as pruning expired tokens every night, from one cron entry.

**What to learn:**

- Defining scheduled tasks in `routes/console.php`, such as `sanctum:prune-expired --hours=24` every day, and
  listing them with `schedule:list`
- Stopping overlapping runs, and running a task on one server only

**Resources:** [Task scheduling](https://laravel.com/docs/13.x/scheduling), Laravel documentation

**Level:** Practitioner · Core

## Caching

A cache keeps the result of slow work for a while. The hard part is removing it when the data changes.

**What to learn:**

- The `Cache` facade, `remember`, and choosing how long values live
- Removing cached values when the data changes, and the risks of serving stale data
- Never caching one user's data where another user can read it

**Resources:**

- [Cache](https://laravel.com/docs/13.x/cache), Laravel documentation
- [Performance and scalability](../../../../standards/php/php-best-practices.md#7-performance--scalability), in the
  Techversant PHP best practices

**Level:** Practitioner · Core

## Horizon

Horizon is a dashboard and configuration tool for Redis queues: throughput, failures and worker counts in one place.

**What to learn:**

- Installing Horizon, and protecting its dashboard in production
- Configuring workers per queue

**Resources:** [Horizon](https://laravel.com/docs/13.x/horizon), Laravel documentation

**Level:** Advanced · Optional

## Project: Add Notifications and Caching

**Brief:** Email users when someone follows them, through a queued notification. Cache the tag list and clear it when
articles change. Schedule a nightly task that prunes expired tokens.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Following a user queues a notification, and the email arrives in Mailpit when a worker runs
- [ ] The job has retries and a timeout, a failed job appears in the failed jobs table, and running it twice sends
  one email
- [ ] The job payload holds IDs, not email addresses or other personal data
- [ ] `GET /api/tags` is served from the cache, and creating, updating or deleting an article updates the list
  straight away
- [ ] `schedule:list` shows `sanctum:prune-expired` running every day
- [ ] Feature tests use `Queue::fake()` and `Notification::fake()` to check what was dispatched and sent
- [ ] All 13 RealWorld API test files still pass

Previous: [06. Authentication and Authorization](./06-authentication-and-authorization.md) · Next:
[08. Testing](./08-testing.md)
