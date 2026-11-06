# 10. Deployment and Operations

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

An API is finished when it runs reliably where clients can reach it, and the team knows when something goes wrong.
This stage covers building, deploying and running a Node.js service in production. Back to the
[roadmap](./README.md).

## Production configuration

Production needs different settings from your machine, and secrets from a safe store.

**What to learn:**

- `NODE_ENV=production`, and what changes when it is set
- Keeping secrets, such as the JWT secret and database passwords, in the environment or a secrets manager, never in
  the image or the repository
- Rotating secrets, such as the JWT signing key, without signing everyone out at once

**Resources:**

- [Keys and secrets management](../../../../security/audit/security-audit-reference.md#63-keys-and-secrets-management),
  in the Techversant security audit reference
- [Environment management](../../../../standards/nodejs/nodejs-typescript-best-practices.md#environment-management),
  in the Techversant Node.js and TypeScript best practices

**Level:** Practitioner · Core

## Docker images

A Docker image packages the service and its Node.js runtime, so it runs the same way in every environment.

**What to learn:**

- A multi-stage build: compile in one stage, and copy only the output and production packages into a small final
  image
- Installing with `npm ci --omit=dev`, pinning the Node.js version, and running as a user that is not root
- Copying the generated Prisma Client into the final image, because Prisma 7 generates it into your source tree
- Starting Node directly with an exec-form `CMD`, such as `CMD ["node", "dist/server.js"]`, so stop signals reach
  it
- Using one image for the API and the worker, with a different command for each

**Resources:**

- [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/), Docker documentation
- [Deployment and CI/CD](../../../../standards/nodejs/nodejs-typescript-best-practices.md#deployment--cicd), in the
  Techversant Node.js and TypeScript best practices

**Level:** Practitioner · Core

## CI/CD pipelines

A pipeline checks, builds and deploys every change the same way, so releases are routine.

**What to learn:**

- The Techversant pipeline order: install, type check, lint, test, build, image, security scan, deploy
- Building and tagging the image once, and promoting the same image through each environment
- Generating a software bill of materials (SBOM) for the image

**Resources:**

- [Git and CI/CD](../../../../standards/nodejs/nodejs-typescript-style-guide.md#15-git--cicd), in the Techversant
  Node.js and TypeScript style guide
- [Git workflow](../../../../standards/git/git-workflow.md), Techversant

**Level:** Practitioner · Core

## Production database migrations

Changing a live database can lock tables or break the running version of the app. This is Red Zone work: write it
by hand, and have a senior engineer review it.

**What to learn:**

- Running `prisma migrate deploy` as its own deploy step, not when each copy of the service starts, from the build
  stage or a separate migration image, because the Prisma CLI is not in the production image
- Changes that are safe while the app is live, such as adding a nullable column, and splitting a risky change into
  steps: add, backfill, switch, then remove
- Backups and a rollback plan before every production migration

**Resources:**

- [Deploying database changes](https://www.prisma.io/docs/orm/prisma-client/deployment/deploy-database-changes-with-prisma-migrate),
  Prisma documentation
- [Red Zone](../../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the Techversant AI
  Era Coding Guidelines

**Level:** Advanced · Core

## Graceful shutdown

When a new version is deployed, the old one gets a signal to stop. A graceful shutdown finishes the work in progress
instead of dropping it.

**What to learn:**

- Handling `SIGTERM`: stop taking new requests, finish open ones with `fastify.close()`, then exit
- Closing the worker so the current job finishes, and closing database and Redis connections
- A time limit, so a stuck request cannot stop the shutdown forever

**Resources:** [Server](https://fastify.dev/docs/latest/Reference/Server/), Fastify documentation

**Level:** Practitioner · Core

## Health checks and monitoring

The team should know the API is down before clients tell them. Health checks, logs and traces make that possible.

**What to learn:**

- `/healthz` for "the process is alive" and `/readyz` for "it can serve traffic", which checks the database
- Logs to standard output as JSON, and traces with OpenTelemetry
- Alerts for error rates, slow responses and a growing queue

**Resources:**

- [Logging and observability](../../../../standards/nodejs/nodejs-typescript-best-practices.md#logging--observability),
  in the Techversant Node.js and TypeScript best practices
- [OpenTelemetry for JavaScript](https://opentelemetry.io/docs/languages/js/)

**Level:** Advanced · Core

## Project: Make It Production-Ready

**Brief:** Package your RealWorld API as a Docker image, run it with its worker, and build a pipeline that checks,
builds and deploys it to a test environment. Write a production migration plan for one schema change, and have a
senior engineer review it.

**Size:** 4 days

**Verification**, checked by a reviewer:

- [ ] A multi-stage Docker image runs the API and the worker, as a user that is not root, with no development
  packages
- [ ] No secrets are in the image or repository, and the service reads them from the environment
- [ ] The pipeline runs the type check, ESLint, the tests and the RealWorld Hurl tests, then builds, scans and
  deploys the image
- [ ] `/readyz` fails when the database is unreachable, and `/healthz` stays healthy
- [ ] On `SIGTERM`, a request in progress finishes, and the process exits within the time limit
- [ ] Logs reach standard output as JSON, with no passwords, tokens or personal data
- [ ] A migration plan for adding a required column to articles shows each step, the backup and the rollback, and a
  senior engineer has reviewed it
- [ ] A RealWorld front end works against the deployed API

Previous: [09. Security and Performance](./09-security-and-performance.md) · Back to the
[roadmap](./README.md#capstone) for the capstone
