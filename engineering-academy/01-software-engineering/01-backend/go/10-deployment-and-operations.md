# 10. Deployment and Operations

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

An API is finished when it runs reliably where clients can reach it, and the team knows when something goes wrong.
This stage covers building, deploying and running a Go service in production. Back to the [roadmap](./README.md).

## Production configuration

Production needs different settings from your machine, and secrets from a safe store.

**What to learn:**

- Settings from environment variables or a secrets manager, never from the image or the repository
- Keeping the JSON Web Token (JWT) signing key and database passwords secret, and rotating them
- Turning off anything meant only for development, such as debug endpoints

**Resources:**
[Keys and secrets management](../../../../security/audit/security-audit-reference.md#63-keys-and-secrets-management),
in the Techversant security audit reference

**Level:** Practitioner · Core

## Container images

Go builds a single binary, so a Go image can hold little more than the program itself.

**What to learn:**

- A multi-stage Dockerfile that builds a static binary with `CGO_ENABLED=0`
- A small base image, such as distroless static, that includes certificates and runs as a user that is not root
- Starting the binary directly with an exec-form entry point, so stop signals reach it

**Resources:**

- [Go language guide](https://docs.docker.com/guides/golang/), Docker documentation
- [Distroless images](https://github.com/GoogleContainerTools/distroless)
- [Containers and orchestration](../../../../security/audit/security-audit-reference.md#45-containers-and-orchestration),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## CI/CD pipelines

A pipeline checks, builds and deploys every change the same way, so releases are routine.

**What to learn:**

- Running `gofmt`, golangci-lint, `govulncheck` and the tests on every pull request
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

- Running goose as its own deploy step, not from every copy of the server as it starts
- Changes that are safe while the app is live, such as adding a nullable column, and splitting a risky change into
  steps: add, backfill, switch, then remove
- Backups and a rollback plan before every production migration

**Resources:**

- [goose](https://pressly.github.io/goose/)
- [Red Zone](../../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the Techversant AI
  Era Coding Guidelines

**Level:** Advanced · Core

## Graceful shutdown

When a new version is deployed, the old one gets a signal to stop. Go does not shut down gracefully on its own: you
write the code that stops taking new requests and lets open ones finish.

**What to learn:**

- Catching the stop signal with `signal.NotifyContext`, and calling `server.Shutdown` with a time limit
- Treating `http.ErrServerClosed` as normal, and waiting for `Shutdown` to return before the program exits
- Stopping the River client so running jobs finish, then closing the database pool
- Failing the readiness check first, so the load balancer stops sending new requests

**Resources:** [Package os/signal](https://pkg.go.dev/os/signal), Go documentation

**Level:** Practitioner · Core

## Health checks and monitoring

The team should know the API is down before clients tell them. Health checks, logs, metrics and traces make that
possible.

**What to learn:**

- Separate liveness and readiness endpoints, with readiness checking the database
- Metrics and traces with OpenTelemetry or the Prometheus client, and logs to standard output as JSON
- Alerts for error rates, slow responses and a growing job queue

**Resources:**

- [OpenTelemetry for Go](https://opentelemetry.io/docs/languages/go/)
- [Alerting and detection](../../../../security/audit/security-audit-reference.md#114-alerting-and-detection), in the
  Techversant security audit reference

**Level:** Advanced · Core

## Project: Make It Production-Ready

**Brief:** Package your RealWorld API as a container image, and build a pipeline that checks, builds and deploys it
to a test environment. Write a production migration plan for one schema change, and have a senior engineer review
it.

**Size:** 4 days

**Verification**, checked by a reviewer:

- [ ] The image holds a static binary on a small base image, runs as a user that is not root, and starts the binary
  directly
- [ ] No secrets are in the image or repository, and the service reads them from the environment
- [ ] The pipeline runs `gofmt`, golangci-lint, `govulncheck`, the tests and the RealWorld Hurl tests, then builds,
  scans and deploys the image
- [ ] The readiness check fails when the database is unreachable, and the liveness check stays healthy
- [ ] On a stop signal, a request in progress and a running job both finish before the process exits
- [ ] Logs reach standard output as JSON, with no passwords, tokens or personal data
- [ ] A migration plan for adding a required column to articles shows each step, the backup and the rollback, and a
  senior engineer has reviewed it
- [ ] A RealWorld front end works against the deployed API

Previous: [09. Security and Performance](./09-security-and-performance.md) · Back to the
[roadmap](./README.md#capstone) for the capstone
