# 10. Deployment and Operations

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

An API is finished when it runs reliably where clients can reach it, and the team knows when something goes wrong.
This stage covers building, deploying and running an ASP.NET Core service in production. Back to the
[roadmap](./README.md).

## Production configuration

Production needs different settings from your machine, and secrets from a safe store.

**What to learn:**

- The Production environment, and settings from environment variables or a secrets manager, never from the image or
  the repository
- Keeping the JSON Web Token (JWT) signing key and database passwords secret, and rotating them
- Turning off anything meant only for development, such as the developer exception page
- Storing and encrypting ASP.NET Core's Data Protection keys, for example in Redis or the database, so cookies and
  antiforgery tokens survive restarts and work on every server

**Resources:**

- [Configuration](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/), Microsoft Learn
- [Keys and secrets management](../../../../security/audit/security-audit-reference.md#63-keys-and-secrets-management),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Container images

A container image packages the service and the .NET runtime, so it runs the same way in every environment.

**What to learn:**

- Building an image with `dotnet publish` and its container support, or with a Dockerfile
- The ASP.NET Core runtime image instead of the software development kit (SDK) image, Ubuntu Chiseled images,
  which hold only what the app needs to run, and the non-root `app` user and port
  8080 that .NET images use by default
- Starting the app directly with an exec-form entry point, so stop signals reach it

**Resources:**

- [Containerize an app with dotnet publish](https://learn.microsoft.com/en-us/dotnet/core/containers/sdk-publish),
  Microsoft Learn
- [Containers and orchestration](../../../../security/audit/security-audit-reference.md#45-containers-and-orchestration),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## CI/CD pipelines

A pipeline checks, builds and deploys every change the same way, so releases are routine.

**What to learn:**

- Running the format check, the build with warnings as errors, and the tests on every pull request
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

- Applying migrations as their own deploy step, with a migration bundle or a reviewed SQL script, never with
  `Database.Migrate()` from every copy of the app as it starts
- Changes that are safe while the app is live, such as adding a nullable column, and splitting a risky change into
  steps: add, backfill, switch, then remove
- Backups and a rollback plan before every production migration

**Resources:**

- [Applying migrations](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/applying), Microsoft
  Learn
- [Red Zone](../../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the Techversant AI
  Era Coding Guidelines

**Level:** Advanced · Core

## Graceful shutdown

When a new version is deployed, the old one gets a signal to stop. The .NET host handles it: Kestrel stops taking new
requests and lets open ones finish, up to a time limit.

**What to learn:**

- How the host shuts down, and setting the shutdown timeout
- Stopping background services through their cancellation token, and letting Hangfire finish or requeue running
  jobs
- Failing the readiness check first, so the load balancer stops sending new requests

**Resources:** [.NET Generic Host](https://learn.microsoft.com/en-us/dotnet/core/extensions/generic-host), Microsoft
Learn

**Level:** Practitioner · Core

## Health checks and monitoring

The team should know the API is down before clients tell them. Health checks, logs, metrics and traces make that
possible.

**What to learn:**

- Health check endpoints with tags, so liveness and readiness are separate, and readiness checks the database
- Metrics and traces with OpenTelemetry, and logs to standard output as JSON
- Alerts for error rates, slow responses and a growing job queue

**Resources:**

- [Health checks](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/health-checks), Microsoft Learn
- [Alerting and detection](../../../../security/audit/security-audit-reference.md#114-alerting-and-detection), in the
  Techversant security audit reference

**Level:** Advanced · Core

## Project: Make It Production-Ready

**Brief:** Package your RealWorld API as a container image, and build a pipeline that checks, builds and deploys it
to a test environment. Write a production migration plan for one schema change, and have a senior engineer review
it.

**Size:** 4 days

**Verification**, checked by a reviewer:

- [ ] The image uses the ASP.NET Core runtime, not the SDK, runs as a user that is not root, and starts the app
  directly
- [ ] No secrets are in the image or repository, and the service reads them from the environment
- [ ] The pipeline runs the format check, the build, the tests and the RealWorld Hurl tests, then builds, scans and
  deploys the image
- [ ] The readiness check fails when the database is unreachable, and the liveness check stays healthy
- [ ] On a stop signal, a request in progress finishes, and a running Hangfire job finishes or is requeued, before
  the process exits
- [ ] Logs reach standard output as JSON, with no passwords, tokens or personal data
- [ ] A migration plan for adding a required column to articles shows each step, the backup and the rollback, and a
  senior engineer has reviewed it
- [ ] A RealWorld front end works against the deployed API

Previous: [09. Security and Performance](./09-security-and-performance.md) · Back to the
[roadmap](./README.md#capstone) for the capstone
