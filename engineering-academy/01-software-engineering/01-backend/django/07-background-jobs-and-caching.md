# 07. Background Jobs and Caching

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Slow work, such as sending email or calling another system, should not make users wait. Task queues move it to the
background, and caching avoids doing the same expensive work twice. Back to the [roadmap](./README.md).

## Tasks with Celery

Celery runs tasks in worker processes, using a broker such as Redis to hold them until a worker is free. Most Django
client projects that need background work use it.

**What to learn:**

- Setting up Celery with Django, defining tasks, and running a worker
- Retries with back-off, time limits, and what happens to a task that keeps failing
- Queuing a task only after the database change is saved, with `transaction.on_commit`
- Writing tasks that are safe to run twice, and passing IDs, not model objects or personal data

**Resources:**
[First steps with Django](https://docs.celeryq.dev/en/stable/django/first-steps-with-django.html), Celery
documentation

**Level:** Practitioner · Core

## Email

Django sends email through a backend you choose in settings. In development, a local tool catches every message so
nothing reaches real people.

**What to learn:**

- Sending email from a task with `send_mail`, and templates for the message
- Testing email locally with a tool such as Mailpit, and checking `mail.outbox` in tests

**Resources:** [Sending email](https://docs.djangoproject.com/en/6.1/topics/email/), Django documentation

**Level:** Practitioner · Core

## Scheduled tasks

Some work runs on a timetable, such as a nightly clean-up. Celery beat adds tasks to the queue on a schedule.

**What to learn:**

- Defining a schedule with Celery beat, and running exactly one beat process
- Why a cron job on each web server breaks when you run more than one copy

**Resources:** [Periodic tasks](https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html), Celery
documentation

**Level:** Practitioner · Core

## Caching

A cache keeps the result of slow work for a while. The hard part is removing it when the data changes.

**What to learn:**

- Django's cache framework with the built-in Redis backend, and `cache.get_or_set`
- Removing cached values when the data changes, and the risks of serving stale data
- Never caching one user's data where another user can read it

**Resources:** [Django's cache framework](https://docs.djangoproject.com/en/6.1/topics/cache/), Django documentation

**Level:** Practitioner · Core

## Django's Tasks framework

Django 6.0 added a built-in way to define background tasks. Django defines and queues them; a separate worker
backend runs them.

**What to learn:**

- Defining a task with the `@task` decorator, and choosing a backend that has a worker
- How it compares with Celery for small projects

**Resources:** [Tasks framework](https://docs.djangoproject.com/en/6.1/topics/tasks/), Django documentation

**Level:** Advanced · Optional

## Project: Add Notifications and Caching

**Brief:** Email users when someone follows them, through a Celery task. Cache the tag list and clear it when
articles change. Schedule a nightly task that deletes tags no article uses, and expired tokens.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Following a user queues a task after the change is saved, and the email arrives in Mailpit when a worker runs
- [ ] The task has retries with back-off and a time limit, and running it twice sends one email
- [ ] The task arguments are IDs, not email addresses or other personal data
- [ ] `GET /api/tags` is served from the cache, and creating, updating or deleting an article, or the nightly
  clean-up, updates the list straight away
- [ ] Celery beat runs the nightly clean-up, and only one beat process runs
- [ ] Tests check what was queued and sent, without a real broker or email server
- [ ] All 13 RealWorld API test files still pass

Previous: [06. Authentication and Authorization](./06-authentication-and-authorization.md) · Next:
[08. Testing](./08-testing.md)
