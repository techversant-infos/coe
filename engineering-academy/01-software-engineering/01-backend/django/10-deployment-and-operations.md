# 10. Deployment and Operations

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

An API is finished when it runs reliably where clients can reach it, and the team knows when something goes wrong.
This stage covers building, deploying and running a Django app in production. Back to the [roadmap](./README.md).

## Production configuration

Production needs different settings from your machine, and secrets from a safe store.

**What to learn:**

- `DEBUG = False`, `ALLOWED_HOSTS`, and why debug mode in production leaks secrets
- Keeping secrets, such as `SECRET_KEY` and database passwords, in the environment or a secrets manager, never in
  the image or the repository
- Collecting static files for the admin site with `collectstatic`, served by WhiteNoise or the web server

**Resources:**

- [Deployment checklist](https://docs.djangoproject.com/en/6.1/howto/deployment/checklist/), Django documentation
- [Keys and secrets management](../../../../security/audit/security-audit-reference.md#63-keys-and-secrets-management),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Docker images and application servers

The development server is not for production. A Docker image runs the app under Gunicorn, the same way in every
environment.

**What to learn:**

- Running Django with Gunicorn, or for ASGI with Gunicorn and the `uvicorn-worker` package, or Uvicorn alone
- A small image: pinned Python version, packages installed from the lock file, and a user that is not root
- Starting the server with an exec-form `CMD`, so stop signals reach it, and one image for the web server, the
  Celery worker and beat, with a different command for each

**Resources:**

- [How to deploy with WSGI](https://docs.djangoproject.com/en/6.1/howto/deployment/wsgi/), Django documentation
- [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/), Docker documentation

**Level:** Practitioner · Core

## CI/CD pipelines

A pipeline checks, builds and deploys every change the same way, so releases are routine.

**What to learn:**

- Running Ruff, mypy and the tests on every pull request
- Building and tagging the image once, and promoting the same image through each environment
- Techversant's branch and promotion rules for product teams

**Resources:**

- [Git workflow](../../../../standards/git/git-workflow.md), Techversant
- [Build and CI/CD pipeline security](../../../../security/audit/security-audit-reference.md#52-build-and-cicd-pipeline-security),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Production database migrations

Changing a live database can lock tables or break the running version of the app. This is Red Zone work: write it
by hand, and have a senior engineer review it.

**What to learn:**

- Running `migrate` as its own deploy step, not when each copy of the app starts
- Changes that are safe while the app is live, such as adding a nullable column, and splitting a risky change into
  steps: add, backfill, switch, then remove
- Reading the SQL a migration will run with `sqlmigrate`, and a backup and rollback plan before every production
  migration

**Resources:**

- [Migrations](https://docs.djangoproject.com/en/6.1/topics/migrations/), Django documentation
- [Red Zone](../../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only),
  in the Techversant AI Era Coding Guidelines

**Level:** Advanced · Core

## Workers in production

Celery workers and beat are long-running processes. They need supervising, and restarting when new code is deployed.

**What to learn:**

- Running workers and one beat process as their own containers
- Stopping workers gracefully on deploy, so running tasks finish
- Watching queue length and failed tasks

**Resources:** [Workers guide](https://docs.celeryq.dev/en/stable/userguide/workers.html), Celery documentation

**Level:** Practitioner · Core

## Health checks and monitoring

The team should know the API is down before clients tell them. Health checks, logs and error tracking make that
possible.

**What to learn:**

- A health endpoint that checks the database and the broker, for example with django-health-check
- Sending logs to standard output as JSON, and errors to the monitoring tool your project uses
- Alerts for error rates, slow responses and a growing queue

**Resources:**

- [django-health-check](https://github.com/codingjoe/django-health-check)
- [Alerting and detection](../../../../security/audit/security-audit-reference.md#114-alerting-and-detection),
  in the Techversant security audit reference

**Level:** Advanced · Core

## Project: Make It Production-Ready

**Brief:** Package your RealWorld API as a Docker image, run it with Celery workers and beat, and build a pipeline
that checks, builds and deploys it to a test environment. Write a production migration plan for one schema change,
and have a senior engineer review it.

**Size:** 4 days

**Verification**, checked by a reviewer:

- [ ] One Docker image runs Gunicorn, the Celery worker and beat, as a user that is not root, started with an
  exec-form `CMD`
- [ ] The running container has `DEBUG = False` and a set `ALLOWED_HOSTS`, with no secrets in the image or
  repository
- [ ] The pipeline runs Ruff, mypy, the tests and the RealWorld Hurl tests, then builds and deploys the image
- [ ] The health endpoint fails when the database is unreachable
- [ ] Logs reach standard output as JSON, with no passwords, tokens or personal data
- [ ] A migration plan for adding a required column to articles shows each step, the SQL, the backup and the
  rollback, and a senior engineer has reviewed it
- [ ] A RealWorld front end works against the deployed API

Previous: [09. Security and Performance](./09-security-and-performance.md) · Back to the
[roadmap](./README.md#capstone) for the capstone
