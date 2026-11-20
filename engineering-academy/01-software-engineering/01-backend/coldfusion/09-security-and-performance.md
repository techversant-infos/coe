# 09. Security and Performance

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-20 · **Next review:** 2027-05-20

A secure API protects client data; a fast one keeps users. Both need checking against real evidence, not assumptions.
CFML (ColdFusion Markup Language) adds its own checks: the engine's settings and administrator must be locked down as
well as the code. Back to the [roadmap](./README.md).

## Injection and output encoding

Injection lets an attacker run their own SQL or script through your code. In CFML, it usually comes from a value
placed straight into SQL or HTML.

**What to learn:**

- Finding unbound values in queries, binding `IN` lists with `list=true`, and checking `ORDER BY` columns against a
  list of allowed values
- Encoding output for its context: `encodeForHTML()`, `encodeForHTMLAttribute()`, `encodeForJavaScript()` and
  `encodeForURL()`
- Never passing user input to `evaluate()`, `<cfinclude>` paths or file functions

**Resources:**

- [SQL and data store injection](../../../../security/audit/security-audit-reference.md#72-sql-and-data-store-injection),
  in the Techversant security audit reference
- [Cross-site scripting and output encoding](../../../../security/audit/security-audit-reference.md#73-cross-site-scripting-and-output-encoding),
  in the Techversant security audit reference
- [Secure CFML coding](../../../07-consulting/coldfusion/03-security-and-hardening.md#secure-cfml-coding), in the
  Senior ColdFusion Consultant roadmap

**Level:** Advanced · Core

## Engine and server hardening

A CFML engine ships with an administrator, debugging output and settings meant for development. Each must be locked
down before the application faces the internet.

**What to learn:**

- Keeping the administrator off the public site, with a strong password
- Turning off debugging output and the Robust Exception Information setting in production
- Applying engine security updates, and checking the engine version against its support dates

**Resources:**

- [Lockdown guide](https://docs.lucee.org/guides/deploying-lucee-server-apps/lockdown-guide.html), Lucee documentation
- [ColdFusion 2025 lockdown guide](https://www.adobe.com/cc-shared/assets/pdf/products/coldfusion-family/coldfusion-2025-lockdown-guide-1-1.pdf),
  Adobe
- [Server lockdown](../../../07-consulting/coldfusion/03-security-and-hardening.md#server-lockdown), in the Senior
  ColdFusion Consultant roadmap
- [Application and server hardening](../../../../security/audit/security-audit-reference.md#41-application-and-server-hardening),
  in the Techversant security audit reference

**Level:** Advanced · Core

## CORS and security headers

Cross-origin resource sharing (CORS) decides which websites may call your API from a browser. Security headers tell
the browser to turn on its own protections.

**What to learn:**

- Allowing only the front-end origins you configure, never `*` with credentials
- Headers such as `Strict-Transport-Security`, `X-Content-Type-Options` and `Content-Security-Policy`
- Adding them in one place, such as an interceptor or the cors module

**Resources:**

- [Security headers](../../../../security/audit/security-audit-reference.md#42-security-headers) and
  [CORS](../../../../security/audit/security-audit-reference.md#43-cors), in the Techversant security audit reference
- [cors module](https://www.forgebox.io/view/cors), ForgeBox

**Level:** Advanced · Core

## The security and code review checklists

Techversant reviews every change against a security checklist, and ColdFusion code against its own review checklist.
Using them on your own code first makes reviews faster.

**What to learn:**

- Going through the security audit checklist and marking each item passed, fixed or not applicable
- The ColdFusion code review checklist: scopes, queries, security, errors and performance
- Checking packages for known security issues, and keeping `box.json` up to date

**Resources:**

- [Security audit checklist](../../../../security/audit/security-audit-checklist.md), Techversant
- [ColdFusion code review checklist](../../../../standards/coldfusion/coldfusion-code-review-checklist.md),
  Techversant

**Level:** Advanced · Core

## Query performance and indexes

Most slow endpoints are slow because of the database. Measure first, then add the index or change the query.

**What to learn:**

- `EXPLAIN ANALYZE` in PostgreSQL, and reading a plan for sequential scans and slow joins
- Choosing indexes for the filters and sort orders your API uses
- Separating database time, CFML time and network time before deciding what to fix

**Resources:**
[Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html), PostgreSQL documentation

**Level:** Advanced · Core

## File uploads

RealWorld has no uploads, but many client applications do, and an unchecked upload can let an attacker run their
own code on the server.

**What to learn:**

- Accepting only the file types you need, checked by content as well as name
- Saving uploads outside the web root, with a new name, and limiting their size
- The engine settings that block dangerous file extensions

**Resources:**
[File upload](../../../../security/audit/security-audit-reference.md#75-file-upload), in the Techversant security
audit reference

**Level:** Advanced · Optional

## Load testing

A load test shows how the API behaves with many users at once, before real users find out.

**What to learn:**

- Writing a k6 script for a list endpoint, and setting a target with your reviewer
- Watching the engine's memory, threads and database connections during the test

**Resources:**

- [k6 documentation](https://grafana.com/docs/k6/latest/), Grafana
- [Load testing](../../../07-consulting/coldfusion/02-jvm-performance-and-diagnostics.md#load-testing), in the Senior
  ColdFusion Consultant roadmap

**Level:** Advanced · Optional

## Project: Harden and Speed Up the API

**Brief:** Check your API against the Techversant security audit checklist and the ColdFusion code review checklist,
and fix what you find. Then load the article list and feed with about 100,000 articles, find the slowest queries,
and make them faster.

**Size:** 3 days

**Verification**, checked by a reviewer:

- [ ] The security audit checklist and the ColdFusion code review checklist are filled in for the API, with every
  applicable item passed or fixed
- [ ] No query contains an unbound value, and a test shows that a request cannot change an article's author
- [ ] CORS allows only the configured front-end origins, and API and error responses carry the required headers
- [ ] With production settings, the administrator is not reachable from the public address and an error response
  shows no stack trace
- [ ] The pull request shows `EXPLAIN ANALYZE` output before and after for the article list and feed, with the
  indexes added
- [ ] A k6 load test of `GET /api/articles` meets the target agreed with your reviewer, and the script and results
  are in the repository

Previous: [08. Testing](./08-testing.md) · Next: [10. Deployment and Operations](./10-deployment-and-operations.md)
