# 09. Security and Performance

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

A working API is not finished until it is safe and fast under real use. This stage covers the security checks every
Techversant API passes, and finding and fixing what makes a Java service slow. Back to the [roadmap](./README.md).

## Input handling and injection

Every request is untrusted. Data transfer objects (DTOs), limits and safe queries keep bad input from doing harm.

**What to learn:**

- Accepting only the fields a DTO lists, so a request cannot set fields such as an article's author
- Passing values to queries only as parameters, in Jakarta Persistence Query Language (JPQL) and
  SQL alike
- Limits on request size, list sizes and string lengths, and treating stored URLs, such as profile images, as
  untrusted input

**Resources:**
[SQL and data store injection](../../../../security/audit/security-audit-reference.md#72-sql-and-data-store-injection),
in the Techversant security audit reference

**Level:** Practitioner · Core

## CORS and security headers

Browsers let a front end on another origin call your API only if the API allows it, through cross-origin resource
sharing (CORS). Security headers protect API
responses, too.

**What to learn:**

- A `CorsConfigurationSource` with an allow-list of origins, never allowing every origin with credentials
- The security headers Spring Security adds, and the ones the Techversant audit requires on API and error responses

**Resources:**

- [CORS](https://docs.spring.io/spring-security/reference/servlet/integrations/cors.html) and
  [security headers](https://docs.spring.io/spring-security/reference/servlet/exploits/headers.html), Spring
  Security documentation
- [Security headers](../../../../security/audit/security-audit-reference.md#42-security-headers), in the Techversant
  security audit reference

**Level:** Practitioner · Core

## The security audit checklist

Every Techversant pull request is checked against the security audit checklist. Learn it well enough to check your
own work before review.

**What to learn:**

- The checklist's sections, and which ones apply to an API
- Checking dependencies with OWASP (Open Worldwide Application Security Project) Dependency-Check or a similar scanner,
  and acting on what it finds
- Exposing only the Actuator endpoints you need, and protecting them

**Resources:** [Security audit checklist](../../../../security/audit/security-audit-checklist.md), Techversant

**Level:** Practitioner · Core

## Query performance and indexes

Slow APIs are usually slow databases. An index on the right column can turn a query from seconds into milliseconds.

**What to learn:**

- Finding slow queries, and reading `EXPLAIN ANALYZE` output
- Adding indexes in Flyway migrations for the columns you filter, join and sort on, such as foreign keys and
  `created_at`. PostgreSQL does not index foreign keys for you.
- The connection pool, HikariCP, and why a pool that is too large or too small slows everything down

**Resources:**
[Data access](https://docs.spring.io/spring-boot/reference/data/sql.html), Spring Boot documentation

**Level:** Advanced · Core

## JVM performance and load testing

The Java virtual machine (JVM) needs memory settings that fit its container, and a load test shows how the service
behaves before real traffic does.

**What to learn:**

- Heap size in containers, garbage collection basics, and reading memory and thread metrics from Actuator
- Turning on virtual threads, and what they change for a service that waits on the database
- Load testing with a tool such as k6, and reading response time percentiles against a target

**Resources:**

- [Virtual threads](https://docs.spring.io/spring-boot/reference/features/spring-application.html#features.spring-application.virtual-threads),
  Spring Boot documentation
- [k6 documentation](https://grafana.com/docs/k6/latest/)

**Level:** Advanced · Core

## Native images

GraalVM native images start in milliseconds and use less memory, at the cost of longer builds and some limits on
what the code can do.

**What to learn:**

- Building a native image with Spring Boot, and the limits it puts on reflection

**Resources:**
[GraalVM native images](https://docs.spring.io/spring-boot/reference/packaging/native-image/index.html), Spring Boot
documentation

**Level:** Advanced · Optional

## Project: Harden and Speed Up the API

**Brief:** Check your API against the Techversant security audit checklist and fix what you find. Then load test the
article list and feed, find the slowest parts, and make them faster.

**Size:** 3 days

**Verification**, checked by a reviewer:

- [ ] The security audit checklist is filled in for the API, with every applicable item passed or fixed
- [ ] The dependency scanner reports no known high or critical vulnerabilities
- [ ] A test shows that a request cannot change an article's author
- [ ] CORS allows only the configured front-end origins, and API and error responses carry the required headers
- [ ] Only the health, info and metrics Actuator endpoints are exposed, and the metrics endpoint is not public
- [ ] The pull request shows `EXPLAIN ANALYZE` output before and after for the article list and feed, on a seed of
  about 100,000 articles, with the indexes added
- [ ] A k6 load test of `GET /api/articles` meets the target agreed with your reviewer, and the script and results
  are in the repository

Previous: [08. Testing](./08-testing.md) · Next: [10. Deployment and Operations](./10-deployment-and-operations.md)
