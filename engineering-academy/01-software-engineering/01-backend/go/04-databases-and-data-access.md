# 04. Databases and Data Access

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Most of what an API does is read and write data. A good data model and efficient queries keep the API correct and fast
as the data grows. This path writes SQL for PostgreSQL with pgx and sqlc, and uses goose for migrations. Back to the
[roadmap](./README.md).

## Migrations with goose

goose applies versioned SQL migrations in order, so every environment gets the same schema.

**What to learn:**

- Writing migrations as numbered SQL files with an up and a down part, and how goose records which have run
- Running goose from the command line, and pinning its version in `go.mod`
- Why migrations that run on a production database are Red Zone work: written by hand, safe to run while the app is
  live, and reviewed by a senior engineer

**Resources:**

- [goose](https://pressly.github.io/goose/)
- [Red Zone](../../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the Techversant AI
  Era Coding Guidelines

**Level:** Practitioner · Core

## PostgreSQL with pgx

pgx is the PostgreSQL driver most Go services use. Its pool shares a fixed number of connections between requests.

**What to learn:**

- Opening a `pgxpool` pool at start-up, and passing the request context to every query
- Reading rows into structs, closing them, and handling `NULL` columns
- Timestamps with sub-second precision, so `updatedAt` changes even when an update comes in the same second

**Resources:** [pgxpool](https://pkg.go.dev/github.com/jackc/pgx/v5/pgxpool), pgx documentation

**Level:** Practitioner · Core

## Type-safe queries with sqlc

sqlc reads the SQL you write and generates Go functions and structs for it, so a wrong column name fails at build
time, not in production.

**What to learn:**

- Writing queries in `.sql` files, generating code with sqlc, and committing the generated code
- Queries with filters that may or may not be present, such as tag, author and favourited, for example with
  `sqlc.narg('tag')` and `(sqlc.narg('tag')::text IS NULL OR ...)`
- Passing values only as query parameters, never joining them into SQL strings

**Resources:**

- [sqlc documentation](https://docs.sqlc.dev/en/latest/)
- [SQL and data store injection](../../../../security/audit/security-audit-reference.md#72-sql-and-data-store-injection),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Efficient queries

The most common performance bug is the N+1 query: one query for a list, then one more for every item. In Go it often
hides in a loop that calls the database.

**What to learn:**

- Loading related data, such as authors and tags, with joins or one query for the whole page, for example with
  `WHERE id = ANY($1)`
- Keeping `tagList` in a stable order, such as the order given, because the RealWorld API tests check tags by
  position
- Aggregating tags with `COALESCE(array_agg(...) FILTER (WHERE ... IS NOT NULL), '{}')`, so an article with no
  tags gets `[]` rather than `null`
- Counting the queries a request runs in tests, for example with a pgx query tracer

**Resources:** [pgx](https://pkg.go.dev/github.com/jackc/pgx/v5), pgx documentation

**Level:** Practitioner · Core

## Data integrity and transactions

The database should refuse bad data even when the code has a bug. Transactions make several changes succeed or fail
together.

**What to learn:**

- Foreign keys, unique constraints and `NOT NULL`, and recognising a unique violation from its PostgreSQL error code
- Transactions with `pool.Begin`, a deferred `Rollback`, and `Commit`, and keeping them short
- Setting `updated_at` in every update query

**Resources:**
[Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html), PostgreSQL documentation

**Level:** Practitioner · Core

## ORMs such as GORM

Some Go projects use an object-relational mapper (ORM), such as GORM. Learn to work in one when a project already
does.

**What to learn:**

- How GORM maps structs to tables, its trade-offs against writing SQL, and why its automatic migration must never
  run on a production database

**Resources:** [GORM guides](https://gorm.io/docs/)

**Level:** Practitioner · Optional

## Project: Store the Data

**Brief:** Design the RealWorld schema in goose migrations, write the queries for sqlc, and replace the stage 03
sample data with real queries for the endpoints that do not need sign-in: listing articles, getting one article,
comments, tags and profiles. Use your stage 01 slug library, backed by the database.

**Size:** 3–4 days

**Verification**, checked by a reviewer:

- [ ] goose migrations create users, articles, tags, comments, favourites and follows, with foreign keys and unique
  constraints, and they run up and down cleanly
- [ ] `GET /api/articles` filters by `tag`, `author` and `favorited`, pages with `limit` and `offset`, and returns
  the newest first with the right `articlesCount`
- [ ] Article slugs come from the stage 01 library, and two articles with the same title get different slugs
- [ ] Every query takes the request context, and a test shows that listing 20 articles runs the same number of
  queries as listing 2
- [ ] A seed command fills a development database with enough data to try every filter
- [ ] The responses still match the specification exactly

Previous: [03. HTTP and REST APIs](./03-http-and-rest-apis.md) · Next:
[05. Validation and Error Handling](./05-validation-and-error-handling.md)
