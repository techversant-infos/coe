# 04. Databases and Data Access

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Most of what an API does is read and write data. A good data model and efficient queries keep the API correct and
fast as the data grows. Back to the [roadmap](./README.md).

## Models and migrations

Models describe the tables, and migrations change the database to match. Everyone on the team, and every
environment, gets the same schema by running them.

**What to learn:**

- Fields, `Meta` options, a custom user model set up at the start of the project, and indexes
- `makemigrations` and `migrate`, reading the generated migration, and never changing one that has already run
  elsewhere
- Why migrations that run on a production database are Red Zone work: written by hand, safe to run while the app is
  live, and reviewed by a senior engineer

**Resources:**

- [Models](https://docs.djangoproject.com/en/6.1/topics/db/models/) and
  [migrations](https://docs.djangoproject.com/en/6.1/topics/migrations/), Django documentation
- [Red Zone](../../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only),
  in the Techversant AI Era Coding Guidelines

**Level:** Practitioner · Core

## Relationships and queries

The RealWorld data has many relationships: authors, followers, favourites, tags and comments. The ORM queries them
through querysets.

**What to learn:**

- `ForeignKey`, `ManyToManyField`, and relationships to the same model, such as users following users
- Querysets: filtering across relationships, such as articles favourited by a user, and ordering
- Annotations with `Count` and `Exists`, for values such as `favoritesCount` and `favorited`

**Resources:**
[Making queries](https://docs.djangoproject.com/en/6.1/topics/db/queries/), Django documentation

**Level:** Practitioner · Core

## Efficient queries

The most common Django performance bug is the N+1 query: one query for a list, then one more for every item.

**What to learn:**

- `select_related` for single related objects, and `prefetch_related` for lists
- Fetch modes, added in Django 6.1: `FETCH_PEERS` turns many N+1 cases into two queries, and `RAISE` makes missed
  loading fail in tests
- Counting the queries a request runs, for example with `django-debug-toolbar`, or the `django_assert_num_queries`
  fixture in tests

**Resources:**
[Database access optimization](https://docs.djangoproject.com/en/6.1/topics/db/optimization/), Django
documentation

**Level:** Practitioner · Core

## Data integrity and transactions

The database should refuse bad data even when the code has a bug. Transactions make several changes succeed or fail
together.

**What to learn:**

- `UniqueConstraint`, such as one favourite per user and article, and the right `on_delete` rule, including the
  database-level options added in Django 6.1
- Wrapping related changes in `transaction.atomic`
- Catching `IntegrityError` from a unique constraint, instead of checking first and racing another request

**Resources:**
[Database transactions](https://docs.djangoproject.com/en/6.1/topics/db/transactions/), Django documentation

**Level:** Practitioner · Core

## Factories and seed data

Factories create realistic test records in one line. A seed command fills a database with sample data for
development.

**What to learn:**

- Writing factories with factory_boy
- A management command that seeds a development database with users, articles, tags and comments

**Resources:**

- [factory_boy](https://factoryboy.readthedocs.io/en/stable/)
- [Writing custom management commands](https://docs.djangoproject.com/en/6.1/howto/custom-management-commands/),
  Django documentation

**Level:** Practitioner · Core

## Raw SQL

Some queries are clearer or faster in SQL than in the ORM, such as reports.

**What to learn:**

- `raw()` and database cursors, always passing values as parameters, never by joining strings
- Reading a query plan with `QuerySet.explain()`

**Resources:**

- [Performing raw SQL queries](https://docs.djangoproject.com/en/6.1/topics/db/sql/), Django documentation
- [SQL and data store injection](../../../../security/audit/security-audit-reference.md#72-sql-and-data-store-injection),
  in the Techversant security audit reference

**Level:** Advanced · Optional

## Project: Store the Data

**Brief:** Design the RealWorld models, and replace the stage 03 sample data with real queries for the endpoints that
do not need sign-in: listing articles, getting one article, comments, tags and profiles. Use your stage 01 slug
library, backed by the database.

**Size:** 3–4 days

**Verification**, checked by a reviewer:

- [ ] The project uses a custom user model, and migrations create users, articles, tags, comments, favourites and
  follows, with foreign keys and unique constraints
- [ ] `GET /api/articles` filters by `tag`, `author` and `favorited`, pages with `limit` and `offset`, and returns
  the newest first with the right `articlesCount`
- [ ] Article slugs come from the stage 01 library, and two articles with the same title get different slugs
- [ ] A test with `django_assert_num_queries` shows that listing 20 articles runs the same number of queries as
  listing 2
- [ ] A seed command fills a development database with enough data to try every filter
- [ ] The responses still match the specification exactly

Previous: [03. HTTP and REST APIs](./03-http-and-rest-apis.md) · Next:
[05. Validation and Error Handling](./05-validation-and-error-handling.md)
