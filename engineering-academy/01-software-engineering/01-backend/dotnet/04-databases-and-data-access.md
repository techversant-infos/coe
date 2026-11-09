# 04. Databases and Data Access

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Most of what an API does is read and write data. A good data model and efficient queries keep the API correct and fast
as the data grows. This path uses Entity Framework Core (EF Core) with PostgreSQL. Back to the [roadmap](./README.md).

## Migrations with EF Core

EF Core migrations record each change to the model as a versioned migration, so every environment gets the same
schema.

**What to learn:**

- Adding migrations with `dotnet ef migrations add`, and reading the SQL each one will run before you commit it
- Why `EnsureCreated` is only for throwaway databases
- Why migrations that run on a production database are Red Zone work: written by hand, safe to run while the app is
  live, and reviewed by a senior engineer

**Resources:**

- [Migrations overview](https://learn.microsoft.com/en-us/ef/core/managing-schemas/migrations/), Microsoft Learn
- [Red Zone](../../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the Techversant AI
  Era Coding Guidelines

**Level:** Practitioner · Core

## Entities and relationships

Entities map classes to tables, and relationships connect them, such as an article that belongs to a user and has
many comments.

**What to learn:**

- A `DbContext`, entities, and configuring them in code with the fluent API
- One-to-many and many-to-many relationships, and relationships to the same entity, such as users following users
- PostgreSQL with the Npgsql provider, and storing timestamps in UTC
- Keeping `tagList` in a stable order, such as sorting tags by name in the query or storing each tag's position on
  the join entity, because many-to-many relationships do not keep insertion order

**Resources:**
[Relationships](https://learn.microsoft.com/en-us/ef/core/modeling/relationships), Microsoft Learn

**Level:** Practitioner · Core

## Querying with LINQ

EF Core turns Language Integrated Query (LINQ) queries into SQL. Knowing which SQL it writes keeps queries correct and
fast.

**What to learn:**

- Building a query step by step for filters that may or may not be present, such as tag, author and favourited
- Projecting with `Select` into data transfer objects (DTOs), and `AsNoTracking` for read-only queries
- Raw SQL with `FromSql`, which turns values into parameters, and why joining values into SQL strings is unsafe

**Resources:**

- [Querying data](https://learn.microsoft.com/en-us/ef/core/querying/), Microsoft Learn
- [SQL and data store injection](../../../../security/audit/security-audit-reference.md#72-sql-and-data-store-injection),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Efficient queries

The most common performance bug is the N+1 query: one query for a list, then one more for every item.

**What to learn:**

- Loading related data with `Include` or with projections, and leaving lazy loading off
- Logging the SQL a request runs during development, and counting queries in tests, for example with an interceptor
- Split queries for large includes, and why paging needs a stable sort order

**Resources:**
[Efficient querying](https://learn.microsoft.com/en-us/ef/core/performance/efficient-querying), Microsoft Learn

**Level:** Practitioner · Core

## Data integrity and transactions

The database should refuse bad data even when the code has a bug. Transactions make several changes succeed or fail
together.

**What to learn:**

- Foreign keys, unique indexes and required columns, and recognising a unique violation when `SaveChanges` fails
- How `SaveChanges` wraps its changes in a transaction, and explicit transactions for more than one call
- Rounding timestamps to whole microseconds before saving, because PostgreSQL stores microseconds and .NET ticks are
  100 nanoseconds; otherwise the `createdAt` in the create response differs from later reads
- Setting `UpdatedAt` on every change, for example in a `SaveChanges` interceptor, so it changes even within the
  same second

**Resources:**
[Transactions](https://learn.microsoft.com/en-us/ef/core/saving/transactions), Microsoft Learn

**Level:** Practitioner · Core

## SQL with Dapper

Some queries are clearer or faster in plain SQL, such as reports. Dapper maps SQL results to objects with little
overhead.

**What to learn:**

- Running parameterised queries with Dapper, and reading a query plan with `EXPLAIN`

**Resources:** [Dapper](https://github.com/DapperLib/Dapper)

**Level:** Advanced · Optional

## Project: Store the Data

**Brief:** Design the RealWorld schema with EF Core entities and migrations, and replace the stage 03 sample data with
real queries for the endpoints that do not need sign-in: listing articles, getting one article, comments, tags and
profiles. Use your stage 01 slug library, backed by the database.

**Size:** 3–4 days

**Verification**, checked by a reviewer:

- [ ] Migrations create users, articles, tags, comments, favourites and follows, with foreign keys and unique
  indexes, and the reviewer has read the SQL they generate
- [ ] `GET /api/articles` filters by `tag`, `author` and `favorited`, pages with `limit` and `offset`, and returns
  the newest first with the right `articlesCount`
- [ ] Article slugs come from the stage 01 library, and two articles with the same title get different slugs
- [ ] Read queries use projections or `AsNoTracking`, and a test shows that listing 20 articles runs the same number
  of queries as listing 2
- [ ] A seed command fills a development database with enough data to try every filter
- [ ] The responses still match the specification exactly

Previous: [03. HTTP and REST APIs](./03-http-and-rest-apis.md) · Next:
[05. Validation and Error Handling](./05-validation-and-error-handling.md)
