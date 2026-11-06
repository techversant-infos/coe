# 09. Security and Performance

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

A working API is not finished until it is safe and fast under real use. This stage covers the security checks every
Techversant API passes, and finding and fixing what makes it slow. Back to the [roadmap](./README.md).

## Mass assignment and injection

Laravel protects against the most common attacks when you use it as intended. Most security bugs come from working
around those protections.

**What to learn:**

- Mass assignment: listing `$fillable` fields, so a request cannot set fields such as `author_id`
- Passing values as bindings in raw queries, never joining them into SQL strings
- Treating stored URLs, such as profile images, as untrusted input

**Resources:**

- [Mass assignment](https://laravel.com/docs/13.x/eloquent#mass-assignment), Laravel documentation
- [SQL and data store injection](../../../../security/audit/security-audit-reference.md#72-sql-and-data-store-injection),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## CORS and security headers

Browsers only let a front end on another origin call your API if the API allows it. Security headers protect API
responses, too.

**What to learn:**

- Publishing `config/cors.php` with `php artisan config:publish cors`, and setting allowed origins, methods and
  credentials there, never allowing every origin with credentials
- The security headers the Techversant audit requires on API and error responses

**Resources:**

- [CORS](https://laravel.com/docs/13.x/routing#cors), Laravel documentation
- [Security headers](../../../../security/audit/security-audit-reference.md#42-security-headers) and
  [CORS](../../../../security/audit/security-audit-reference.md#43-cors), in the Techversant security audit reference

**Level:** Practitioner · Core

## The security audit checklist

Every Techversant pull request is checked against the security audit checklist. Learn it well enough to check your
own work before review.

**What to learn:**

- The checklist's sections, and which ones apply to an API
- Checking dependencies with `composer audit`, and acting on what it finds

**Resources:**

- [Security audit checklist](../../../../security/audit/security-audit-checklist.md), Techversant
- [Advanced security practices](../../../../standards/php/php-best-practices.md#5-advanced-security-practices), in the
  Techversant PHP best practices

**Level:** Practitioner · Core

## Query performance and indexes

Slow APIs are usually slow databases. An index on the right column can turn a query from seconds into milliseconds.

**What to learn:**

- Finding slow queries, and reading `EXPLAIN` output
- Adding indexes for the columns you filter, join and sort on, such as `slug` and `created_at`
- Selecting only the columns you need, and paging large result sets

**Resources:** [Database: getting started](https://laravel.com/docs/13.x/database), Laravel documentation

**Level:** Advanced · Core

## Load testing

A load test sends many requests at once, to find how the API behaves before real traffic does.

**What to learn:**

- Writing a simple load test with a tool such as k6, and reading response time percentiles
- Setting a target, such as a 95th percentile under 300 milliseconds, and testing against a production-like setup

**Resources:** [k6 documentation](https://grafana.com/docs/k6/latest/)

**Level:** Advanced · Core

## Octane

Laravel Octane keeps the app in memory between requests, which can make it much faster. It also changes how state
behaves, so code must be written for it.

**What to learn:**

- How Octane differs from PHP-FPM, and the state leaks to avoid

**Resources:** [Octane](https://laravel.com/docs/13.x/octane), Laravel documentation

**Level:** Advanced · Optional

## Project: Harden and Speed Up the API

**Brief:** Check your API against the Techversant security audit checklist and fix what you find. Then load test the
article list and feed, find the slowest queries, and make them faster.

**Size:** 3 days

**Verification**, checked by a reviewer:

- [ ] The security audit checklist is filled in for the API, with every applicable item passed or fixed
- [ ] `composer audit` reports no known vulnerabilities
- [ ] Every model lists `$fillable`, and a test shows that a request cannot change an article's author
- [ ] CORS allows only the configured front-end origins, and API and error responses carry the required headers
- [ ] The pull request shows `EXPLAIN` output before and after for the article list and feed, with the indexes added
- [ ] A k6 load test of `GET /api/articles` meets the target agreed with your reviewer, and the script and results
  are in the repository

Previous: [08. Testing](./08-testing.md) · Next: [10. Deployment and Operations](./10-deployment-and-operations.md)
