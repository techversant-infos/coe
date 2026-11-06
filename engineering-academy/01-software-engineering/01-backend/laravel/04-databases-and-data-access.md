# 04. Databases and Data Access

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Most of what an API does is read and write data. A good data model and efficient queries keep the API correct and
fast as the data grows. Back to the [roadmap](./README.md).

## Migrations

Migrations are versioned files that change the database structure. Everyone on the team, and every environment, gets
the same schema by running them.

**What to learn:**

- Creating tables, columns, indexes and foreign keys in a migration
- Running and rolling back migrations, and never changing a migration that has already run elsewhere
- Why migrations that run on a production database are Red Zone work: written by hand, safe to run while the app is
  live, and reviewed by a senior engineer

**Resources:**

- [Migrations](https://laravel.com/docs/13.x/migrations), Laravel documentation
- [Red Zone](../../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the Techversant AI
  Era Coding Guidelines

**Level:** Practitioner · Core

## Eloquent models and relationships

Eloquent maps each table to a model class, and relationships connect them, such as an article that belongs to a user
and has many comments.

**What to learn:**

- Models, `$fillable`, casts, and naming that follows Laravel's conventions
- One-to-many, many-to-many with a pivot table, and relationships to the same table, such as users following users
- Querying relationships, such as articles favourited by a user

**Resources:**

- [Eloquent](https://laravel.com/docs/13.x/eloquent) and
  [Eloquent relationships](https://laravel.com/docs/13.x/eloquent-relationships), Laravel documentation

**Level:** Practitioner · Core

## Efficient queries

The most common Laravel performance bug is the N+1 query: one query for a list, then one more for every item.

**What to learn:**

- Eager loading with `with()` and counting with `withCount()` and `withExists()`
- Turning on `Model::preventLazyLoading()` outside production, so N+1 queries fail early
- Reading the queries a request runs, for example with Laravel Telescope or the query log

**Resources:**
[Eager loading](https://laravel.com/docs/13.x/eloquent-relationships#eager-loading), Laravel documentation

**Level:** Practitioner · Core

## Data integrity and transactions

The database should refuse bad data even when the code has a bug. Transactions make several changes succeed or fail
together.

**What to learn:**

- Unique constraints, such as one favourite per user and article, and foreign keys with the right delete rule
- Timestamps with fractions of a second, with `$table->timestamps(precision: 6)` and a matching `$dateFormat`, when
  changes in the same second must be told apart
- Wrapping related changes in `DB::transaction()`
- Why a unique constraint beats checking in code first, when two requests arrive at once

**Resources:**

- [Database transactions](https://laravel.com/docs/13.x/database#database-transactions), Laravel documentation
- [Database and data integrity](../../../../standards/php/php-best-practices.md#6-database--data-integrity), in the
  Techversant PHP best practices

**Level:** Practitioner · Core

## Factories and seeders

Factories create realistic test records in one line. Seeders fill a database with sample data for development.

**What to learn:**

- Writing factories with states, such as a published article
- Seeding a development database with users, articles, tags and comments
- Keeping seeders out of production unless the data is reference data

**Resources:**

- [Eloquent factories](https://laravel.com/docs/13.x/eloquent-factories) and
  [Seeding](https://laravel.com/docs/13.x/seeding), Laravel documentation

**Level:** Practitioner · Core

## Query builder and raw SQL

Some queries are clearer or faster in the query builder or SQL than in Eloquent, such as reports.

**What to learn:**

- The query builder, and always passing values as bindings, never by joining strings
- Reading a query plan with `EXPLAIN`

**Resources:**

- [Query builder](https://laravel.com/docs/13.x/queries), Laravel documentation
- [SQL and data store injection](../../../../security/audit/security-audit-reference.md#72-sql-and-data-store-injection),
  in the Techversant security audit reference

**Level:** Advanced · Optional

## Project: Store the Data

**Brief:** Design the RealWorld schema, build the Eloquent models, and replace the stage 03 sample data with real
queries for the endpoints that do not need sign-in: listing articles, getting one article, comments, tags and
profiles. Use your stage 01 slug library, backed by the database.

**Size:** 3–4 days

**Verification**, checked by a reviewer:

- [ ] Migrations create users, articles, tags, comments, favourites and follows, with foreign keys and unique
  constraints, and roll back cleanly
- [ ] `GET /api/articles` filters by `tag`, `author` and `favorited`, pages with `limit` and `offset`, and returns
  the newest first with the right `articlesCount`
- [ ] Article slugs come from the stage 01 library, and two articles with the same title get different slugs
- [ ] `Model::preventLazyLoading()` is on outside production, and listing 20 articles runs the same number of queries
  as listing 2
- [ ] A seeder fills a development database with enough data to try every filter
- [ ] Timestamps are stored with fractions of a second
- [ ] The responses still match the specification exactly

Previous: [03. HTTP and REST APIs](./03-http-and-rest-apis.md) · Next:
[05. Validation and Error Handling](./05-validation-and-error-handling.md)
