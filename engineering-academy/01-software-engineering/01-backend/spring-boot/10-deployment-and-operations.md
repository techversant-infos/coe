# 10. Deployment and Operations

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

An API is finished when it runs reliably where clients can reach it, and the team knows when something goes wrong.
This stage covers building, deploying and running a Spring Boot service in production. Back to the
[roadmap](./README.md).

## Production configuration

Production needs different settings from your machine, and secrets from a safe store.

**What to learn:**

- A production profile, and settings from environment variables or a secrets manager, never from the image or the
  repository
- Keeping the JSON Web Token (JWT) signing key and database passwords secret, and rotating them
- Turning off anything meant only for development, such as detailed error pages

**Resources:**

- [Externalized configuration](https://docs.spring.io/spring-boot/reference/features/external-config.html), Spring
  Boot documentation
- [Keys and secrets management](../../../../security/audit/security-audit-reference.md#63-keys-and-secrets-management),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Container images

A container image packages the service and its Java runtime, so it runs the same way in every environment.

**What to learn:**

- Building an image with Cloud Native Buildpacks through the Spring Boot Maven plugin, or with a Dockerfile
- A Java runtime image instead of the full Java Development Kit (JDK), memory settings that fit the container, and a
  user that is not root
- Layered images, so a code change does not rebuild the layers that hold the libraries

**Resources:**

- [Container images](https://docs.spring.io/spring-boot/reference/packaging/container-images/index.html), Spring
  Boot documentation
- [Containers and orchestration](../../../../security/audit/security-audit-reference.md#45-containers-and-orchestration),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## CI/CD pipelines

A pipeline checks, builds and deploys every change the same way, so releases are routine.

**What to learn:**

- Running the formatter check, static analysis and tests on every pull request
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

- Running Flyway as its own deploy step, or deciding carefully when the application may run it at start-up
- Changes that are safe while the app is live, such as adding a nullable column, and splitting a risky change into
  steps: add, backfill, switch, then remove
- Backups and a rollback plan before every production migration

**Resources:**

- [Database initialization](https://docs.spring.io/spring-boot/how-to/data-initialization.html), Spring Boot
  documentation
- [Red Zone](../../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the Techversant AI
  Era Coding Guidelines

**Level:** Advanced · Core

## Graceful shutdown

When a new version is deployed, the old one gets a signal to stop. Spring Boot shuts down gracefully by default:
it stops taking new requests and lets open ones finish.

**What to learn:**

- Graceful shutdown, and setting how long it may take
- Stopping message listeners and scheduled tasks cleanly
- Starting the process directly with an exec-form entry point, so the stop signal reaches Java

**Resources:**
[Graceful shutdown](https://docs.spring.io/spring-boot/reference/web/graceful-shutdown.html), Spring Boot
documentation

**Level:** Practitioner · Core

## Health checks and monitoring

The team should know the API is down before clients tell them. Health checks, logs, metrics and traces make that
possible.

**What to learn:**

- Actuator's liveness and readiness health groups, on by default in Spring Boot 4, and adding the database check
  to readiness only, with `management.endpoint.health.group.readiness.include`
- Metrics with Micrometer, traces with OpenTelemetry, and logs to standard output as JSON
- Alerts for error rates, slow responses and a growing queue

**Resources:**

- [Actuator](https://docs.spring.io/spring-boot/reference/actuator/index.html), Spring Boot documentation
- [Alerting and detection](../../../../security/audit/security-audit-reference.md#114-alerting-and-detection), in the
  Techversant security audit reference

**Level:** Advanced · Core

## Project: Make It Production-Ready

**Brief:** Package your RealWorld API as a container image, and build a pipeline that checks, builds and deploys it
to a test environment. Write a production migration plan for one schema change, and have a senior engineer review
it.

**Size:** 4 days

**Verification**, checked by a reviewer:

- [ ] The image uses a Java runtime, not the full JDK, runs as a user that is not root, and starts Java directly
- [ ] No secrets are in the image or repository, and the service reads them from the environment
- [ ] The pipeline runs the formatter check, static analysis, the tests and the RealWorld Hurl tests, then builds,
  scans and deploys the image
- [ ] The readiness check fails when the database is unreachable, and the liveness check stays healthy
- [ ] On a stop signal, a request in progress finishes before the process exits
- [ ] Logs reach standard output as JSON, with no passwords, tokens or personal data
- [ ] A migration plan for adding a required column to articles shows each step, the backup and the rollback, and a
  senior engineer has reviewed it
- [ ] A RealWorld front end works against the deployed API

Previous: [09. Security and Performance](./09-security-and-performance.md) · Back to the
[roadmap](./README.md#capstone) for the capstone
