# 04. Databases and Data Access

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Most of what an API does is read and write data. A good data model and efficient queries keep the API correct and
fast as the data grows. This path uses Prisma, one of the tools the Techversant standards name. Back to the
[roadmap](./README.md).

## Prisma schema and migrations

Prisma describes the database in one schema file. Prisma Migrate turns changes to that file into versioned SQL
migrations that every environment runs.

**What to learn:**

- Models, fields, relations and indexes in the Prisma schema
- Creating migrations in development, applying them elsewhere with `prisma migrate deploy`, and never changing a
  migration that has already run
- Prisma 7 set-up, which older tutorials miss: `prisma.config.ts`, a driver adapter such as `@prisma/adapter-pg`,
  the `prisma-client` generator with an `output` path, and running `prisma generate` and `prisma db seed` yourself
- Why migrations that run on a production database are Red Zone work: written by hand, safe to run while the app is
  live, and reviewed by a senior engineer

**Resources:**

- [Prisma schema](https://www.prisma.io/docs/orm/prisma-schema) and
  [Prisma Migrate](https://www.prisma.io/docs/orm/prisma-migrate), Prisma documentation
- [Red Zone](../../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the Techversant AI
  Era Coding Guidelines

**Level:** Practitioner · Core

## Relations and queries

The RealWorld data has many relations: authors, followers, favourites, tags and comments. Prisma Client queries them
with full types.

**What to learn:**

- One-to-many, many-to-many, and relations to the same model, such as users following users
- Filtering on relations, such as articles favourited by a user
- Choosing fields with `select` and `include`, and counting with `_count`

**Resources:**
[Relation queries](https://www.prisma.io/docs/orm/prisma-client/queries/relation-queries), Prisma documentation

**Level:** Practitioner · Core

## Efficient queries

The most common data access bug is the N+1 query: one query for a list, then one more for every item.

**What to learn:**

- Loading related data in the same query, instead of one query per item
- Logging the queries a request runs, and reading them during development
- Working out per-user fields, such as `favorited` and `following`, for a whole page of articles at once

**Resources:**

- [Query optimization](https://www.prisma.io/docs/orm/prisma-client/queries/query-optimization-performance), Prisma
  documentation
- [Performance](../../../../standards/nodejs/nodejs-typescript-style-guide.md#13-performance), in the Techversant
  Node.js and TypeScript style guide

**Level:** Practitioner · Core

## Data integrity and transactions

The database should refuse bad data even when the code has a bug. Transactions make several changes succeed or fail
together.

**What to learn:**

- Unique constraints, such as one favourite per user and article, and foreign keys with the right delete rule
- Handling a unique constraint error from Prisma, instead of checking first and racing another request
- Wrapping related changes in `$transaction`

**Resources:**

- [Transactions](https://www.prisma.io/docs/orm/prisma-client/queries/transactions), Prisma documentation
- [Data layer](../../../../standards/nodejs/nodejs-typescript-best-practices.md#data-layer), in the Techversant
  Node.js and TypeScript best practices

**Level:** Practitioner · Core

## Repositories

A repository hides the database behind an interface written in business terms, such as `findBySlug`. Business code
and tests then never depend on Prisma directly.

**What to learn:**

- Defining a repository interface in the module, and a Prisma implementation in `infra`
- Returning domain objects, not Prisma records, from the repository
- Using an in-memory implementation in unit tests

**Resources:**
[Data access](../../../../standards/nodejs/nodejs-typescript-style-guide.md#11-data-access), in the Techversant
Node.js and TypeScript style guide

**Level:** Practitioner · Core

## Raw SQL and other tools

Some queries are clearer in SQL, such as reports. Some projects use Drizzle instead of Prisma.

**What to learn:**

- Prisma's tagged template `$queryRaw`, which passes values safely, and why `$queryRawUnsafe` is dangerous
- How Drizzle differs from Prisma, if your project uses it

**Resources:**

- [Raw queries](https://www.prisma.io/docs/orm/prisma-client/using-raw-sql/raw-queries), Prisma documentation
- [SQL and data store injection](../../../../security/audit/security-audit-reference.md#72-sql-and-data-store-injection),
  in the Techversant security audit reference

**Level:** Advanced · Optional

## Project: Store the Data

**Brief:** Design the RealWorld schema in Prisma, build the repositories, and replace the stage 03 sample data with
real queries for the endpoints that do not need sign-in: listing articles, getting one article, comments, tags and
profiles. Use your stage 01 slug library, backed by the database.

**Size:** 3–4 days

**Verification**, checked by a reviewer:

- [ ] Migrations create users, articles, tags, comments, favourites and follows, with foreign keys and unique
  constraints
- [ ] `GET /api/articles` filters by `tag`, `author` and `favorited`, pages with `limit` and `offset`, and returns
  the newest first with the right `articlesCount`
- [ ] Article slugs come from the stage 01 library, and two articles with the same title get different slugs
- [ ] Listing 20 articles runs the same number of queries as listing 2
- [ ] Date columns keep Prisma's default millisecond precision, with no `@db.Timestamp(0)`
- [ ] Route handlers and services use repository interfaces, and only `infra` imports Prisma
- [ ] A seed script fills a development database with enough data to try every filter
- [ ] The responses still match the specification exactly

Previous: [03. HTTP and REST APIs](./03-http-and-rest-apis.md) · Next:
[05. Validation and Error Handling](./05-validation-and-error-handling.md)
