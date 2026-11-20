# 04. Databases and Data Access

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-20 · **Next review:** 2027-05-20

Almost every API reads and writes a database, and most ColdFusion Markup Language (CFML) performance and security
problems start in a query. This stage uses PostgreSQL, plain SQL with bound parameters, and the qb query builder, with
migrations to keep every copy of the database the same. Back to the [roadmap](./README.md).

## SQL foundations

You read and write SQL every day, whatever library sits on top. Knowing what the database does with it is the basis
of everything else in this stage.

**What to learn:**

- `SELECT` with `WHERE`, `JOIN`, `GROUP BY`, `ORDER BY`, `LIMIT` and `OFFSET`
- `INSERT`, `UPDATE` and `DELETE`, and checking how many rows changed
- Primary keys, foreign keys, unique constraints and indexes, and how they shape a schema

**Resources:**
[PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html), PostgreSQL documentation

**Level:** Practitioner · Core

## Datasources and bound parameters

A datasource holds the connection details for a database, outside your code. Every value you send to the database
goes as a bound parameter, never joined into the SQL string.

**What to learn:**

- Defining one datasource with values from environment variables, in the template's `.cfconfig.json` or in
  `Application.cfc`, and replacing the template's MySQL datasource with PostgreSQL
- `queryExecute()` with named parameters and a `cfsqltype` for each, and the `<cfqueryparam>` tag in older code
- Why `"WHERE slug = '#url.slug#'"` is an SQL injection hole, and finding it in code you inherit
- Values that cannot be parameters, such as a column to sort by, checked against a list of allowed values

**Resources:**

- [queryExecute()](https://docs.lucee.org/reference/functions/queryexecute.html), Lucee documentation
- [cfqueryparam](https://helpx.adobe.com/coldfusion/cfml-reference/coldfusion-tags/tags-p-q/cfqueryparam.html), Adobe
  ColdFusion documentation
- [Database query practices](../../../../standards/coldfusion/coldfusion-style-guide.md#6-database-query-practices),
  in the Techversant ColdFusion style guide
- [SQL and data store injection](../../../../security/audit/security-audit-reference.md#72-sql-and-data-store-injection),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Migrations

Migrations are versioned scripts that change the schema, so every developer, test run and server has the same
database.

**What to learn:**

- Installing `commandbox-migrations`, and creating, running and rolling back migrations with `migrate` commands
- Writing a migration's `up` and `down` with the schema builder
- Never editing a migration that has already run on a shared database: add a new one instead

**Resources:** [CFMigrations](https://cfmigrations.ortusbooks.com/), Ortus documentation

**Level:** Practitioner · Core

## Query builder

qb builds SQL from CFML code and binds every value for you. It keeps queries readable and works the same on
PostgreSQL, MySQL and SQL Server.

**What to learn:**

- Selects, joins, `where` clauses and ordering with qb
- Inserts, updates and deletes, and reading the SQL that qb produces
- Writing plain SQL with `queryExecute()` when a query is clearer that way

**Resources:**
[qb documentation](https://qb.ortusbooks.com/) and
[qb: selects](https://qb.ortusbooks.com/query-builder/building-queries/selects), Ortus documentation

**Level:** Practitioner · Core

## Data integrity and transactions

A transaction makes several changes succeed or fail together. Constraints stop bad data even when the code has a
bug.

**What to learn:**

- `transaction { }` in script and `<cftransaction>` in tags, and rolling back on an error
- Letting a unique constraint reject a duplicate, and turning the database error into a clear API error
- Timestamps with milliseconds: CFML dates hold milliseconds, so store `timestamptz(3)`, run the server in UTC (the Java
  system property `user.timezone` set to `UTC` in `server.json`), and return the value the database stored, such as from
  `RETURNING`

**Resources:**
[cftransaction](https://docs.lucee.org/reference/tags/transaction.html), Lucee documentation

**Level:** Practitioner · Core

## Efficient queries

A list page that runs one query per row gets slower with every row. This is the N+1 problem, and it is the most
common performance bug in data access.

**What to learn:**

- Spotting N+1 queries, and loading the tags, authors and counts for a whole page in a few queries
- Selecting only the columns you need, and paging every list
- Reading the plan for a query with `EXPLAIN`

**Resources:**

- [Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html), PostgreSQL documentation
- [ColdFusion code review checklist](../../../../standards/coldfusion/coldfusion-code-review-checklist.md), Techversant:
  the database interaction section

**Level:** Advanced · Core

## Quick ORM

Quick is an object-relational mapper (ORM) for ColdBox, built on qb. It maps each table to a component with
relationships, like Eloquent in Laravel. Some projects use it; others prefer qb or plain SQL.

**What to learn:**

- Entities, relationships and eager loading
- When an ORM helps, and when it hides slow queries

**Resources:** [Quick](https://quick.ortusbooks.com/), Ortus documentation

**Level:** Advanced · Optional

## Project: Store the Data

**Brief:** Design the RealWorld schema in PostgreSQL, write the migrations, and replace the stage 03 sample data with
real queries for the endpoints that do not need sign-in: listing articles, getting one article, comments, tags and
profiles. Make article slugs unique.

**Size:** 3–4 days

**Verification**, checked by a reviewer:

- [ ] Migrations create users, articles, tags, comments, favourites and follows, with foreign keys and unique
  constraints, and roll back cleanly
- [ ] Every query binds its values through qb, `queryExecute()` parameters or `<cfqueryparam>`, and the datasource
  settings come from environment variables
- [ ] `GET /api/articles` filters by `tag`, `author` and `favorited`, pages with `limit` and `offset`, and returns
  the newest first with the right `articlesCount`
- [ ] Two articles with the same title get different slugs, and a unique constraint backs this up
- [ ] Listing 20 articles runs the same number of queries as listing 2
- [ ] A seed script fills a development database with enough data to try every filter
- [ ] Timestamps are stored with milliseconds in UTC, an empty `bio` or `image` returns `null`, and the responses
  still match the specification exactly

Previous: [03. HTTP and REST APIs](./03-http-and-rest-apis.md) · Next:
[05. Validation and Error Handling](./05-validation-and-error-handling.md)
