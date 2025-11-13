**Version:** 1.0
**Issued by:** Techversant Center of Excellence (CoE)
**Effective Date:** November 2025
**Contributors:** Compiled by CoE Node.js Working Group

# Node.js TypeScript Style Guide (Techversant CoE)

## 📚 Table of Contents
- [1. Purpose](#1-purpose)
- [2. Project Layout](#2-project-layout)
- [3. Language & Compiler Settings](#3-language--compiler-settings)
- [4. Code Formatting & Linting](#4-code-formatting--linting)
- [5. Naming & Conventions](#5-naming--conventions)
- [6. Modules & Imports](#6-modules--imports)
- [7. Error Handling](#7-error-handling)
- [8. Logging](#8-logging)
- [9. Async & Concurrency](#9-async--concurrency)
- [10. API Design](#10-api-design)
- [11. Data Access](#11-data-access)
- [12. Security](#12-security)
- [13. Performance](#13-performance)
- [14. Testing](#14-testing)
- [15. Git & CI/CD](#15-git--cicd)
- [16. Documentation](#16-documentation)

## 1. Purpose
This guide defines how we structure, format, and write **Node.js TypeScript** code so teams can collaborate effectively across products and services.

> 💡 Consistency reduces friction and accelerates delivery.

## 2. Project Layout
```
/src
  /api            # controllers/route handlers
  /modules        # business modules (domain + services)
  /infra          # db, queues, cache, external clients
  /shared         # cross-cutting utils, types
  /config         # configuration schema & loaders
  /app.ts         # app bootstrap
/tests
/scripts
/docker
```
- **Hexagonal/Layered** separation: controllers → services → repositories/adapters.
- Keep domain logic framework-agnostic; frameworks live at edges (HTTP, DB, queues).

## 3. Language & Compiler Settings
- Target **ES2022+**, `"module": "NodeNext"`, `"moduleResolution": "NodeNext"`.
- `"strict": true`, `"noImplicitAny": true`, `"exactOptionalPropertyTypes": true`.
- `"forceConsistentCasingInFileNames": true`, `"noUncheckedIndexedAccess": true`.
- Emit source maps in non-prod; inline in unit tests.
- Prefer **path aliases** via `tsconfig.paths.json`:
```json
{
  "compilerOptions": { "baseUrl": ".", "paths": { "@/*": ["src/*"] } }
}
```

## 4. Code Formatting & Linting
- **Prettier** for formatting; **ESLint** for rules (`@typescript-eslint/*`).
- Do not fight Prettier; avoid manual line breaks unless improving clarity.
- Example ESLint essentials: `no-floating-promises`, `no-misused-promises`, `eqeqeq`, `import/order`, `@typescript-eslint/consistent-type-definitions` (prefer `type` over `interface` for data shapes).

## 5. Naming & Conventions
- Files: `kebab-case.ts`. Classes: `PascalCase`. Variables/functions: `camelCase`.
- DTOs end with `Dto`, entities with `Entity`, repositories with `Repo`.
- Booleans start with `is/has/can/should`. Enums are singular: `enum Role { Admin }`.
- Prefer **type-first** design: define `type`/`zod` schemas for inputs/outputs.

## 6. Modules & Imports
- Use **ES modules**. Absolute imports via `@/…` paths.
- Group imports: stdlib, third-party, internal. No deep relative `../../..` chains.
- Avoid default exports for domain logic; prefer named exports for tree-shaking.

## 7. Error Handling
- Never `throw` raw strings. Create **typed errors**:
```ts
export class DomainError extends Error { readonly code = "DOMAIN_ERROR"; }
export class NotFoundError extends DomainError { readonly code = "NOT_FOUND"; }
```
- In HTTP, map errors to status codes in a centralized middleware.
- Attach a **request id** and **error id** to logs and responses.

## 8. Logging
- Use **Pino** (JSON, structured). Child loggers per module/request.
- Include fields: `requestId`, `userId`, `traceId`. Mask secrets (tokens, passwords).
- Log levels: `fatal` | `error` | `warn` | `info` | `debug` | `trace`. Default `info`.

## 9. Async & Concurrency
- Use `async/await`; avoid raw `.then()` chains.
- Do not forget `await` for promises (enable `no-floating-promises`).
- Use **AbortController** for cancellable HTTP/DB calls.
- For parallelism, use `Promise.allSettled` with **bounded concurrency** (p-queue).

## 10. API Design
- REST: nouns + plural resources; use standard verbs and status codes.
- Request validation at edges with **Zod/Yup**; produce typed `req.body` via inference.
- Pagination: `?page` + `?pageSize` or cursor-based; always return `total` or `nextCursor`.
- Versioning: prefix routes (`/v1`), never break old clients without deprecation plan.

## 11. Data Access
- Pick one ORM/Query builder per service: **Prisma**, **TypeORM**, or **Drizzle**.
- Repositories hide persistence details and expose *domain* vocabulary.
- Use **transactions** for multi-step writes; enforce **idempotency** where relevant.
- For Mongo, define strict schemas (Zod/Mongoose) and **indexes** in code.

## 12. Security
- **12.1 Input/Output**: Validate all inputs, encode outputs for HTML contexts in SSR.
- **12.2 Auth**: JWT for stateless APIs; rotate keys; short expiries; refresh flows.
- **12.3 Secrets**: No secrets in code. Use env providers (Azure Key Vault, AWS SM).
- **12.4 HTTP**: Enable CORS with explicit allow-lists; set security headers (helmet).
- **12.5 Data**: Use parameterized queries; hash passwords with **bcrypt/argon2**.
- **12.6 Files**: Validate uploads (extension/MIME/size), store outside web-root/CDN.
- **12.7 OWASP**: Adhere to OWASP ASVS & Top 10; run dependency checks (npm audit, Snyk).

## 13. Performance
- Use **caching** (HTTP cache headers, Redis with TTLs). Cache-by-key, not globals.
- Avoid N+1 DB queries; batch with `IN` or data loader patterns.
- Stream large responses; prefer NDJSON or pagination over massive payloads.
- Measure with APM (OpenTelemetry) and business KPIs; set SLOs and budgets.

## 14. Testing
- Pyramid: **70% unit**, **20% integration**, **10% E2E**.
- Frameworks: Vitest/Jest for unit; Supertest for HTTP; Playwright/Cypress for E2E.
- Isolate time/uuid/random via DI; seed test data consistently; parallelize safely.

## 15. Git & CI/CD
- Branch naming: `feat/`, `fix/`, `chore/`, `docs/`, `refactor/`.
- Conventional commits; enforce PR templates and required checks.
- CI steps: install → typecheck → lint → unit → integration → build → image scan → deploy.
- Use **feature flags**; keep trunk deployable; practice blue/green or canary releases.

## 16. Documentation
- `README.md` per service with run instructions and env vars table.
- ADRs for architectural decisions. Auto-generate API docs (OpenAPI/Swagger).
- Include **operability runbooks**: health checks, dashboards, alerts, SLOs.
