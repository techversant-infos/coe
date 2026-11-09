# 09. Security and Performance

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

A working API is not finished until it is safe and fast under real use. This stage covers the security checks every
Techversant API passes, and finding and fixing what makes a .NET service slow. Back to the [roadmap](./README.md).

## Input handling and injection

Every request is untrusted. Data transfer objects (DTOs), limits and safe queries keep bad input from doing harm.

**What to learn:**

- Binding requests to DTOs, never to entities, so a request cannot set fields such as an article's author
- Lowering the request body limit of Kestrel, ASP.NET Core's built-in web server, which is about 30 MB by default, and
  limiting list sizes and string lengths
- Passing values to queries only as parameters, and treating stored URLs, such as profile images, as untrusted input

**Resources:**

- [Kestrel limits](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel/options), Microsoft
  Learn
- [SQL and data store injection](../../../../security/audit/security-audit-reference.md#72-sql-and-data-store-injection),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## CORS and security headers

Browsers let a front end on another origin call your API only if the API allows it, through cross-origin resource
sharing (CORS). Security headers protect API responses, too.

**What to learn:**

- A CORS policy with an allow-list of origins, never allowing every origin with credentials
- A middleware that adds the security headers the Techversant audit requires, on API and error responses alike, and
  HTTP Strict Transport Security (HSTS)

**Resources:**

- [Enable CORS](https://learn.microsoft.com/en-us/aspnet/core/security/cors), Microsoft Learn
- [Security headers](../../../../security/audit/security-audit-reference.md#42-security-headers), in the Techversant
  security audit reference

**Level:** Practitioner · Core

## The security audit checklist

Every Techversant pull request is checked against the security audit checklist. Learn it well enough to check your
own work before review.

**What to learn:**

- The checklist's sections, and which ones apply to an API
- NuGet's security audit, including packages your packages depend on, and acting on what it finds
- Protecting the Hangfire dashboard and keeping detailed health check output private

**Resources:**

- [Security audit checklist](../../../../security/audit/security-audit-checklist.md), Techversant
- [Auditing packages](https://learn.microsoft.com/en-us/nuget/concepts/auditing-packages), Microsoft Learn

**Level:** Practitioner · Core

## Query performance and indexes

Slow APIs are usually slow databases. An index on the right column can turn a query from seconds into milliseconds.

**What to learn:**

- Finding slow queries, and reading `EXPLAIN ANALYZE` output for the SQL that Entity Framework Core (EF Core)
  writes
- Adding indexes in migrations for the columns you filter, join and sort on, such as foreign keys and `created_at`.
  EF Core adds indexes for foreign keys by convention, but check every filter and sort.
- The connection pool, and why a pool that is too large or too small slows everything down

**Resources:** [Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html), PostgreSQL documentation

**Level:** Advanced · Core

## Profiling and load testing

.NET's diagnostic tools show where a service spends its time and memory, and a load test shows how it behaves before
real traffic does.

**What to learn:**

- `dotnet-counters` and `dotnet-trace`, and spotting thread pool starvation, where blocking calls leave no threads free
  for new requests
- Measuring code with BenchmarkDotNet
- Load testing with a tool such as k6, and reading response time percentiles against a target

**Resources:**

- [.NET diagnostics](https://learn.microsoft.com/en-us/dotnet/core/diagnostics/), Microsoft Learn
- [k6 documentation](https://grafana.com/docs/k6/latest/)

**Level:** Advanced · Core

## Native AOT

Native ahead-of-time (AOT) compilation builds an app that starts faster and uses less memory, with limits on what the
code can do.

**What to learn:**

- Publishing an ASP.NET Core app with native AOT, and the features it does not support

**Resources:**
[Native AOT](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/native-aot), Microsoft Learn

**Level:** Advanced · Optional

## Project: Harden and Speed Up the API

**Brief:** Check your API against the Techversant security audit checklist and fix what you find. Then load test the
article list and feed, find the slowest parts, and make them faster.

**Size:** 3 days

**Verification**, checked by a reviewer:

- [ ] The security audit checklist is filled in for the API, with every applicable item passed or fixed
- [ ] NuGet's audit reports no known high or critical vulnerabilities, including in dependencies of dependencies
- [ ] A test shows that a request cannot change an article's author, and a body over the size limit returns 413
- [ ] CORS allows only the configured front-end origins, and API and error responses carry the required headers
- [ ] The Hangfire dashboard needs sign-in, and health checks show no internal details publicly
- [ ] The pull request shows `EXPLAIN ANALYZE` output before and after for the article list and feed, on a seed of
  about 100,000 articles, with the indexes added
- [ ] A k6 load test of `GET /api/articles` meets the target agreed with your reviewer, and the script and results
  are in the repository

Previous: [08. Testing](./08-testing.md) · Next: [10. Deployment and Operations](./10-deployment-and-operations.md)
