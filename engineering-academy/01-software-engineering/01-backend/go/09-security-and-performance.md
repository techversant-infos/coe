# 09. Security and Performance

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

A working API is not finished until it is safe and fast under real use. This stage covers the security checks every
Techversant API passes, and finding and fixing what makes a Go service slow. Back to the [roadmap](./README.md).

## Input handling and injection

Every request is untrusted. Request structs, limits and safe queries keep bad input from doing harm.

**What to learn:**

- Decoding into request structs that list only the fields a client may send, so a request cannot set fields such as
  an article's author
- Limiting the request body size with `http.MaxBytesReader`, and limiting list sizes and string lengths
- Passing values to queries only as parameters, and treating stored URLs, such as profile images, as untrusted input

**Resources:**
[SQL and data store injection](../../../../security/audit/security-audit-reference.md#72-sql-and-data-store-injection),
in the Techversant security audit reference

**Level:** Practitioner · Core

## CORS and security headers

Browsers let a front end on another origin call your API only if the API allows it, through cross-origin resource
sharing (CORS). Security headers protect API responses, too.

**What to learn:**

- CORS middleware, such as rs/cors, with an allow-list of origins, never allowing every origin with credentials
- A middleware that adds the security headers the Techversant audit requires, on API and error responses alike

**Resources:**

- [rs/cors](https://github.com/rs/cors)
- [Security headers](../../../../security/audit/security-audit-reference.md#42-security-headers), in the Techversant
  security audit reference

**Level:** Practitioner · Core

## The security audit checklist

Every Techversant pull request is checked against the security audit checklist. Learn it well enough to check your
own work before review.

**What to learn:**

- The checklist's sections, and which ones apply to an API
- Running `govulncheck`, which reports only known vulnerabilities in code your program calls, and gosec through
  golangci-lint
- Server timeouts against slow clients, and never exposing profiling endpoints publicly: `net/http/pprof`
  registers on `http.DefaultServeMux`, so serve the API from your own `ServeMux` and pprof on an internal-only port

**Resources:** [Security audit checklist](../../../../security/audit/security-audit-checklist.md), Techversant

**Level:** Practitioner · Core

## Query performance and indexes

Slow APIs are usually slow databases. An index on the right column can turn a query from seconds into milliseconds.

**What to learn:**

- Finding slow queries, and reading `EXPLAIN ANALYZE` output
- Adding indexes in migrations for the columns you filter, join and sort on, such as foreign keys and `created_at`.
  PostgreSQL does not index foreign keys for you.
- Creating indexes on a live table with `CREATE INDEX CONCURRENTLY`, in a goose migration marked
  `-- +goose NO TRANSACTION`
- Sizing the pgx connection pool, and why a pool that is too large or too small slows everything down

**Resources:** [Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html), PostgreSQL documentation

**Level:** Advanced · Core

## Profiling and load testing

Go's profiler shows where a service spends its time and memory, and a load test shows how it behaves before real
traffic does.

**What to learn:**

- CPU, memory and goroutine profiles with pprof, and benchmarks with `testing.B`
- Finding goroutine leaks, and why every goroutine needs a way to stop
- Load testing with a tool such as k6, and reading response time percentiles against a target

**Resources:**

- [Diagnostics](https://go.dev/doc/diagnostics), go.dev
- [k6 documentation](https://grafana.com/docs/k6/latest/)

**Level:** Advanced · Core

## The garbage collector

Go frees memory automatically. Two settings control how much memory it uses and how often it runs.

**What to learn:**

- How the garbage collector works, `GOGC`, and setting `GOMEMLIMIT` to about 90% of the container's memory limit.
  Since Go 1.25, `GOMAXPROCS` follows the container's CPU limit for you.

**Resources:** [Guide to the Go garbage collector](https://go.dev/doc/gc-guide), go.dev

**Level:** Advanced · Optional

## Project: Harden and Speed Up the API

**Brief:** Check your API against the Techversant security audit checklist and fix what you find. Then load test the
article list and feed, find the slowest parts, and make them faster.

**Size:** 3 days

**Verification**, checked by a reviewer:

- [ ] The security audit checklist is filled in for the API, with every applicable item passed or fixed
- [ ] `govulncheck` reports no vulnerabilities that your code calls
- [ ] A test shows that a request cannot change an article's author, and a body over the size limit returns 413
- [ ] CORS allows only the configured front-end origins, and API and error responses carry the required headers
- [ ] Profiling endpoints are not reachable from outside, and the server sets timeouts for slow clients
- [ ] The pull request shows `EXPLAIN ANALYZE` output before and after for the article list and feed, on a seed of
  about 100,000 articles, with the indexes added
- [ ] A k6 load test of `GET /api/articles` meets the target agreed with your reviewer, and the script and results
  are in the repository

Previous: [08. Testing](./08-testing.md) · Next: [10. Deployment and Operations](./10-deployment-and-operations.md)
