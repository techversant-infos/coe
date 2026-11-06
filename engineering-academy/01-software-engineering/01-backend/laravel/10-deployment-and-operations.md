# 10. Deployment and Operations

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

An API is finished when it runs reliably where clients can reach it, and the team knows when something goes wrong.
This stage covers building, deploying and running a Laravel app in production. Back to the [roadmap](./README.md).

## Production configuration

Production needs different settings from your machine: debugging off, caches on, and secrets from a safe store.

**What to learn:**

- `APP_ENV=production` and `APP_DEBUG=false`, and why debug mode in production leaks secrets
- Caching configuration, routes, events and views with `php artisan optimize` when the container starts or at
  deploy, not while building the image, which has no production settings
- Keeping secrets, such as `APP_KEY` and database passwords, in the environment or a secrets manager, never in the
  image or the repository

**Resources:**

- [Deployment](https://laravel.com/docs/13.x/deployment), Laravel documentation
- [Keys and secrets management](../../../../security/audit/security-audit-reference.md#63-keys-and-secrets-management),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Docker images

A Docker image packages the app and its PHP runtime, so it runs the same way in every environment.

**What to learn:**

- Building a small image with PHP-FPM and a web server, or an image built for Laravel
- Pinning the PHP version, turning on OPcache, and running as a user that is not root
- Using one image for the web server, the queue worker and the scheduler, with a different command for each

**Resources:**

- [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/), Docker documentation
- [Tooling and PHP runtime](../../../../standards/php/php-coding-standards.md#11-tooling--php-runtime), in the
  Techversant PHP coding standards

**Level:** Practitioner · Core

## CI/CD pipelines

A pipeline checks, builds and deploys every change the same way, so releases are routine.

**What to learn:**

- Running the code style check, static analysis and tests on every pull request
- Building and tagging the image once, and promoting the same image through each environment
- Techversant's branch and promotion rules for product teams

**Resources:**

- [DevOps, CI/CD and deployment standards](../../../../standards/php/php-best-practices.md#9-devops-cicd--deployment-standards),
  in the Techversant PHP best practices
- [Git workflow](../../../../standards/git/git-workflow.md), Techversant

**Level:** Practitioner · Core

## Production database migrations

Changing a live database can lock tables or break the running version of the app. This is Red Zone work: write it
by hand, and have a senior engineer review it.

**What to learn:**

- Changes that are safe while the app is live, such as adding a nullable column, and changes that are not
- Splitting a risky change into steps, such as add, backfill, switch, then remove
- Backups and a rollback plan before every production migration

**Resources:**

- [Migrations](https://laravel.com/docs/13.x/migrations), Laravel documentation
- [Red Zone](../../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the Techversant AI
  Era Coding Guidelines

**Level:** Advanced · Core

## Workers and the scheduler in production

Queue workers and the scheduler are long-running processes. They need supervising, and restarting when new code is
deployed.

**What to learn:**

- Running workers under a process manager or as their own containers
- Restarting workers on deploy with `queue:restart`, so they load the new code
- Running `schedule:run` every minute, or `schedule:work` in a container

**Resources:** [Queues in production](https://laravel.com/docs/13.x/queues#supervisor-configuration), Laravel
documentation

**Level:** Practitioner · Core

## Health checks and monitoring

The team should know the API is down before clients tell them. Health checks, logs and error tracking make that
possible.

**What to learn:**

- Laravel's built-in `/up` health route, which only shows that the app starts, and adding a listener for the
  `DiagnosingHealth` event that checks the database
- Sending logs to standard output as JSON, and errors to the monitoring tool your project uses
- Alerts for error rates, slow responses and a growing queue

**Resources:**

- [Logging](https://laravel.com/docs/13.x/logging) and [Pulse](https://laravel.com/docs/13.x/pulse), Laravel
  documentation
- [Alerting and detection](../../../../security/audit/security-audit-reference.md#114-alerting-and-detection), in the
  Techversant security audit reference

**Level:** Advanced · Core

## Project: Make It Production-Ready

**Brief:** Package your RealWorld API as a Docker image, run it with a queue worker and the scheduler, and build a
pipeline that checks, builds and deploys it to a test environment. Write a production migration plan for one schema
change, and have a senior engineer review it.

**Size:** 4 days

**Verification**, checked by a reviewer:

- [ ] One Docker image runs the web server, the queue worker and the scheduler, as a user that is not root, with
  OPcache on
- [ ] The running container has `APP_DEBUG=false` and configuration cached at start-up, with no secrets in the
  image or repository
- [ ] The pipeline runs the code style check, Larastan, the feature tests and the RealWorld Hurl tests, then builds
  and deploys the image
- [ ] `/up` reports healthy, and fails when the database is unreachable
- [ ] Logs reach standard output as JSON, with no passwords, tokens or personal data
- [ ] A migration plan for adding a required column to `articles` shows each step, the backup and the rollback, and a
  senior engineer has reviewed it
- [ ] A RealWorld front end works against the deployed API

Previous: [09. Security and Performance](./09-security-and-performance.md) · Back to the
[roadmap](./README.md#capstone) for the capstone
