**Version:** 1.0
**Issued by:** Techversant Center of Excellence (CoE)
**Effective Date:** November 2025
**Contributors:** Compiled by CoE Node.js Working Group

# Node.js TypeScript Code Review Checklist

Focus on what can be verified in a **diff/PR**. Use this list during every review.

## 📁 1. Structure & Boundaries
- Clear separation of layers (API/controllers ↔ services ↔ repositories/adapters).
- No domain logic inside controllers or ORMs; services own business rules.
- Files are small and cohesive; no god modules.

## 🧩 2. Types & Contracts
- `tsconfig` is strict; no `any` leaks. Public APIs have explicit types.
- External interfaces (HTTP/queue) have validation (Zod/Yup) and inferred TS types.
- DTOs are immutable or treated as such; no mutation after validation.

## 🔗 3. Imports & Modules
- ES modules with ordered imports; no deep relative import pyramids.
- No circular dependencies (CI check with madge/depcruise).
- No unused exports; tree-shakeable modules where possible.

## 🧠 4. Code Quality
- Lint passes: `eslint`, `prettier`, `tsc --noEmit`.
- No `console.*` calls; use logger. No TODOs left in production code.
- Functions under ~50 lines; classes under ~300 lines unless justified.

## ⚠️ 5. Error Handling
- Uses typed errors; no raw `throw "msg"` or swallowed catches.
- Central error middleware maps to HTTP codes; includes error id/request id.
- Promise rejections are awaited/handled; `no-floating-promises` enforced.

## 📝 6. Logging & Observability
- Structured logging (Pino) with context fields; secrets masked.
- OpenTelemetry hooks present (traces, metrics); health endpoints implemented.
- Meaningful log levels; no sensitive payloads in logs.

## 🗄️ 7. Data & Transactions
- Parameterized queries; migration scripts reviewed.
- Transactions or outbox pattern for multi-entity writes/events.
- Indexes defined for frequent queries; N+1 patterns avoided.

## 🔒 8. Security
- Dependencies scanned; no known critical vulnerabilities.
- Auth flows verified; tokens have expiries, rotation, and audience checks.
- CORS, security headers, CSRF (where applicable) and rate limits configured.
- Input validation covers type/format/range; output encoding where relevant.

## 🚀 9. Performance & Resilience
- Bounded concurrency and backpressure for external calls.
- Retries with jitter, timeouts, circuit breakers for unstable deps.
- Caching used where appropriate with sane TTLs and invalidation strategy.

## 🧪 10. Testing
- Unit tests cover core logic; integration tests cover DB/HTTP happy-paths and errors.
- Tests are deterministic; no sleep/flaky network reliance.
- Coverage thresholds met (lines/branches > 80% for core modules).

## 🧰 11. DevEx & CI
- Dev scripts exist (`dev`, `test`, `lint`, `typecheck`, `build`).
- Dockerfile minimal and secure; multi-stage builds; non-root user.
- CI artifacts: coverage, lint reports, SBOM/image scan results.

## 🧾 12. Docs & Ops
- README updated; env var table clear with defaults and secrets guidance.
- OpenAPI/Swagger updated and versioned; migration notes included.
- Runbook updated: dashboards, alerts, SLOs, escalation.

---
✅ Apply this checklist to keep services clean, secure, observable, and maintainable.
