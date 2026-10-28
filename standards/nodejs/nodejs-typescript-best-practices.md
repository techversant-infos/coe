**Version:** 1.0
**Issued by:** Techversant Center of Excellence (CoE)
**Effective Date:** November 2025
**Contributors:** Compiled by CoE Node.js Working Group

# Node.js TypeScript Best Practices: The Ultimate Survival Guide
*How to build services that are boring to operate (in the best way).*

## 📚 Table of Contents
- [Intro: Why Bother?](#intro-why-bother)
- [Architecture & Boundaries](#architecture--boundaries)
- [Configuration & Secrets](#configuration--secrets)
- [Validation & DTOs](#validation--dtos)
- [Error Handling](#error-handling)
- [Logging & Observability](#logging--observability)
- [HTTP APIs](#http-apis)
- [Data Layer](#data-layer)
- [Messaging & Jobs](#messaging--jobs)
- [Security](#security)
- [Performance](#performance)
- [Testing Strategy](#testing-strategy)
- [Environment Management](#environment-management)
- [Deployment & CI/CD](#deployment--cicd)
- [Quick Wins](#quick-wins)
- [Conclusion](#conclusion)

## Intro: Why Bother?
Great services are built for **change** and **failure**. Design for clarity, testability, and operability. Future-you will thank you.

## Architecture & Boundaries
- Prefer **hexagonal architecture**: Ports (interfaces) and Adapters (implementations).
- Keep controllers thin; business rules live in services and domain models.
- Inject dependencies (repo, cache, clock, uuid) for testability.
- Split monorepos with workspaces (pnpm/npm) and **per-service ownership**.

## Configuration & Secrets
- Configuration as code via `@fastify/env` or `envalid` + Zod schema.
- Keep `.env.example` up to date. Use **Azure Key Vault/AWS SM** in cloud.
- Feature flags for risky changes. No environment branching inside domain code.

## Validation & DTOs
- Validate at edges with **Zod** and infer types:
```ts
const CreateUser = z.object({ email: z.string().email(), name: z.string().min(1) });
type CreateUser = z.infer<typeof CreateUser>;
```
- Map DTOs ↔ domain; avoid leaking persistence types to API.

## Error Handling
- Domain errors are explicit. Convert to transport errors at edges.
- Add an **error id** to responses; log stack traces server-side only.
- Never expose internal messages or stack traces to clients.

## Logging & Observability
- Use **Pino** with serializers; include requestId and userId.
- Adopt **OpenTelemetry**: traces for requests, spans for DB/cache/HTTP.
- Emit RED/USE metrics and domain KPIs; build dashboards and SLOs.

## HTTP APIs
- Idempotency for POST where clients might retry.
- Pagination and filtering; consistent error shape:
```json
{ "error": { "id": "abc123", "code": "NOT_FOUND", "message": "..." } }
```
- Document with **OpenAPI**; keep examples real and testable.

## Data Layer
- Pick a mature tool (Prisma/TypeORM/Drizzle). Use **migrations**.
- Enforce **unique** and **foreign key** constraints; soft delete with care.
- For reads, consider **CQRS** (separate read models) when complexity grows.

## Messaging & Jobs
- Use queues (BullMQ/RabbitMQ/SQS) for background work.
- Ensure **at-least-once** handling, idempotency keys, and dead-letter queues.
- Use **outbox pattern** for reliable event publication from DB transactions.

## Security
- Adopt **OWASP ASVS** practices; threat model critical flows.
- Secure headers (helmet), CORS allow-list, rate limits, and input size limits.
- Store passwords with **bcrypt/argon2**; rotate tokens/keys regularly.
- Sign and verify JWTs with audience/issuer; short-lived access tokens; refresh flow.

## Performance
- Use **Redis** for cache and rate limits; invalidate precisely.
- Stream large downloads; gzip/br compression; ETags and conditional GETs.
- Avoid hot loops/blocking work; push CPU-heavy tasks to workers.

## Testing Strategy
- Unit: Pure functions/services with in-memory fakes.
- Integration: Real DB (ephemeral container) + HTTP; migrate up before tests.
- E2E: Happy path + critical failures; run in CI nightly or per-PR if cheap.
- Contract tests for external services where feasible.

## Environment Management
- Twelve-Factor alignment: env-config, disposability, stateless processes.
- Health endpoints: `/healthz` (liveness), `/readyz` (readiness).
- Blue/green or canary deploys with automatic rollbacks and feature flags.

## Deployment & CI/CD
- Pipeline: lint → typecheck → test → build → docker → security scan → deploy.
- Minimal images (distroless/alpine), run as **non-root**, drop Linux caps.
- SBOM generation (CycloneDX) and image signing (cosign).

## Quick Wins
- Add `pino-http` with requestId middleware.
- Add Zod validation for every public endpoint.
- Introduce a global error handler and never leak stack traces.
- Add `AbortController` + timeouts for all outbound HTTP calls.
- Enforce `eslint-plugin-security` and dependency scanning.

## Conclusion
Build **clear**, **observable**, and **secure** services. Optimize for change, and make failure cheap to detect and recover from. Ship with confidence.


## 📖 Reference Document

For a more detailed explanation and extended best practices, refer to the official CoE document:

👉 [**Node.js Best Practices — Detailed Reference (Google Docs)**](https://docs.google.com/document/d/1sXKJd0gX5ejmOo1BVAVbJNuGf2cZyVJv/edit?usp=sharing&ouid=110772354547577566076&rtpof=true&sd=true)

This document expands upon the topics covered here with additional architecture patterns, coding standards, and DevSecOps recommendations.

