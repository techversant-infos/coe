# 09. Security and Performance

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

A working API is not finished until it is safe and fast under real use. This stage covers the security checks every
Techversant API passes, and finding and fixing what makes it slow. Back to the [roadmap](./README.md).

## Django's security settings

Django protects against many attacks by default, and its deployment check lists the settings still to turn on.

**What to learn:**

- Running `manage.py check --deploy`, and fixing what it reports
- HTTPS settings such as `SECURE_SSL_REDIRECT`, `SECURE_HSTS_SECONDS` and secure cookies, and `SECURE_PROXY_SSL_HEADER`
  behind a load balancer
- Keeping read-only fields, such as an article's author, out of what a serializer accepts

**Resources:**

- [Deployment checklist](https://docs.djangoproject.com/en/6.1/howto/deployment/checklist/) and
  [security in Django](https://docs.djangoproject.com/en/6.1/topics/security/), Django documentation

**Level:** Practitioner · Core

## CORS and security headers

Browsers only let a front end on another origin call your API if the API allows it. Security headers protect API
responses, too.

**What to learn:**

- django-cors-headers with an allow-list of origins, never allowing every origin with credentials
- The security headers the Techversant audit requires on API and error responses, and Django's built-in Content
  Security Policy support for any HTML pages, such as the admin site

**Resources:**

- [django-cors-headers](https://github.com/adamchainz/django-cors-headers)
- [Security headers](../../../../security/audit/security-audit-reference.md#42-security-headers) and
  [CORS](../../../../security/audit/security-audit-reference.md#43-cors), in the Techversant security audit reference

**Level:** Practitioner · Core

## The security audit checklist

Every Techversant pull request is checked against the security audit checklist. Learn it well enough to check your
own work before review.

**What to learn:**

- The checklist's sections, and which ones apply to an API
- Checking dependencies with `pip-audit`, and acting on what it finds

**Resources:**

- [Security audit checklist](../../../../security/audit/security-audit-checklist.md), Techversant
- [SQL and data store injection](../../../../security/audit/security-audit-reference.md#72-sql-and-data-store-injection),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Query performance and indexes

Slow APIs are usually slow databases. An index on the right column can turn a query from seconds into milliseconds.

**What to learn:**

- Finding slow queries, and reading plans with `QuerySet.explain(analyze=True)` on PostgreSQL
- Adding indexes for the columns you filter, join and sort on, such as the follows and favourites tables and
  `created_at`
- Selecting only the columns you need with `only()` and `values()`, and paging large result sets

**Resources:**
[Database access optimization](https://docs.djangoproject.com/en/6.1/topics/db/optimization/), Django
documentation

**Level:** Advanced · Core

## Load testing

A load test sends many requests at once, to find how the API behaves before real traffic does.

**What to learn:**

- Writing a simple load test with a tool such as k6 or Locust, and reading response time percentiles
- Setting a target, such as a 95th percentile under 300 milliseconds, and testing against a production-like setup
- Choosing the number of Gunicorn workers, and what happens when they are all busy

**Resources:** [k6](https://grafana.com/docs/k6/latest/) and [Locust](https://docs.locust.io/en/stable/) documentation

**Level:** Advanced · Core

## Async views and ASGI

Django can run under ASGI (Asynchronous Server Gateway Interface) and serve async views, which helps when a view waits
on many slow services. It also changes how database access must be written.

**What to learn:**

- When async views help, and `sync_to_async` for calling the ORM from async code

**Resources:**
[Asynchronous support](https://docs.djangoproject.com/en/6.1/topics/async/), Django documentation

**Level:** Advanced · Optional

## Project: Harden and Speed Up the API

**Brief:** Check your API against the Techversant security audit checklist and Django's deployment check, and fix
what you find. Then load test the article list and feed, find the slowest queries, and make them faster.

**Size:** 3 days

**Verification**, checked by a reviewer:

- [ ] The security audit checklist is filled in for the API, with every applicable item passed or fixed
- [ ] `manage.py check --deploy` with production settings reports no warnings, and `pip-audit` reports no known
  vulnerabilities
- [ ] A test shows that a request cannot change an article's author
- [ ] CORS allows only the configured front-end origins, and API and error responses carry the required headers
- [ ] The pull request shows `EXPLAIN ANALYZE` output before and after for the article list and feed, on a seed of
  about 100,000 articles, with the indexes added
- [ ] A load test of `GET /api/articles` meets the target agreed with your reviewer, and the script and results are
  in the repository

Previous: [08. Testing](./08-testing.md) · Next: [10. Deployment and Operations](./10-deployment-and-operations.md)
