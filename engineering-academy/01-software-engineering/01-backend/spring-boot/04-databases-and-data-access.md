# 04. Databases and Data Access

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Most of what an API does is read and write data. A good data model and efficient queries keep the API correct and fast
as the data grows. This path uses Spring Data JPA (Jakarta Persistence) with Hibernate, and Flyway for migrations. Back
to the [roadmap](./README.md).

## Migrations with Flyway

Flyway applies versioned SQL migrations in order, so every environment gets the same schema. Hibernate should never
change the schema for you outside a throwaway local database.

**What to learn:**

- Adding Flyway with `spring-boot-starter-flyway` and `flyway-database-postgresql`. In Spring Boot 4,
  `flyway-core` on its own does not run your migrations.
- Writing migrations as numbered SQL files, and how Flyway records which have run
- Turning off Hibernate's automatic schema changes, and checking the mapping against the schema instead
- Why migrations that run on a production database are Red Zone work: written by hand, safe to run while the app is
  live, and reviewed by a senior engineer

**Resources:**

- [Database initialization](https://docs.spring.io/spring-boot/how-to/data-initialization.html), Spring Boot
  documentation
- [Red Zone](../../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the Techversant AI
  Era Coding Guidelines

**Level:** Practitioner · Core

## Entities and relationships

JPA entities map classes to tables, and relationships connect them, such as an article that belongs to a user and
has many comments.

**What to learn:**

- `@Entity`, IDs, columns and `Instant` for timestamps
- `@ManyToOne`, `@OneToMany` and `@ManyToMany` with a join table, and relationships to the same entity, such as
  users following users
- Keeping `tagList` in a stable order, such as the order given, because a `Set` relationship has no order
- Lazy loading, and why relationships should be lazy by default

**Resources:**
[Hibernate ORM user guide](https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html)

**Level:** Practitioner · Core

## Repositories and queries

Spring Data JPA writes the repository code for you. You declare an interface, and Spring builds queries from method
names or from the Jakarta Persistence Query Language (JPQL) you write.

**What to learn:**

- Repository interfaces, derived query methods, and `@Query` with named parameters
- Specifications or query methods for filters that may or may not be present, such as tag, author and favourited
- Projections that load only the fields a response needs

**Resources:** [Spring Data JPA](https://docs.spring.io/spring-data/jpa/reference/), Spring Data documentation

**Level:** Practitioner · Core

## Efficient queries

The most common JPA performance bug is the N+1 query: one query for a list, then one more for every item.

**What to learn:**

- Fetch joins and `@EntityGraph`, to load related data in the same query
- Why paging over a fetch-joined collection makes Hibernate page in memory, and paging the article IDs first or
  using `hibernate.default_batch_fetch_size` instead
- Setting `spring.jpa.open-in-view` to `false`, so lazy loading cannot quietly run queries while the response is
  written
- Logging the SQL a request runs during development, and counting queries in tests

**Resources:**
[Data access](https://docs.spring.io/spring-boot/reference/data/sql.html), Spring Boot documentation

**Level:** Practitioner · Core

## Data integrity and transactions

The database should refuse bad data even when the code has a bug. Transactions make several changes succeed or fail
together.

**What to learn:**

- Unique constraints, such as one favourite per user and article, and foreign keys with the right delete rule
- `@Transactional` on service methods, read-only transactions, and why calling a transactional method from the same
  class skips the transaction
- Handling `DataIntegrityViolationException` from a unique constraint, instead of checking first and racing another
  request

**Resources:**
[Transaction management](https://docs.spring.io/spring-framework/reference/data-access/transaction.html), Spring
Framework documentation

**Level:** Practitioner · Core

## SQL with JdbcClient

Some queries are clearer or faster in SQL than in JPA, such as reports.

**What to learn:**

- `JdbcClient` with named parameters, never joining values into SQL strings
- Reading a query plan with `EXPLAIN`

**Resources:**

- [JdbcClient](https://docs.spring.io/spring-framework/reference/data-access/jdbc/core.html#jdbc-JdbcClient), Spring
  Framework documentation
- [SQL and data store injection](../../../../security/audit/security-audit-reference.md#72-sql-and-data-store-injection),
  in the Techversant security audit reference

**Level:** Advanced · Optional

## Project: Store the Data

**Brief:** Design the RealWorld schema in Flyway migrations, build the entities and repositories, and replace the
stage 03 sample data with real queries for the endpoints that do not need sign-in: listing articles, getting one
article, comments, tags and profiles. Use your stage 01 slug library, backed by the database.

**Size:** 3–4 days

**Verification**, checked by a reviewer:

- [ ] Flyway migrations create users, articles, tags, comments, favourites and follows, with foreign keys and unique
  constraints, and Hibernate's schema validation passes
- [ ] `GET /api/articles` filters by `tag`, `author` and `favorited`, pages with `limit` and `offset`, and returns
  the newest first with the right `articlesCount`
- [ ] Article slugs come from the stage 01 library, and two articles with the same title get different slugs
- [ ] `spring.jpa.open-in-view` is `false`, and a test shows that listing 20 articles runs the same number of
  queries as listing 2
- [ ] A seed script or profile fills a development database with enough data to try every filter
- [ ] The responses still match the specification exactly

Previous: [03. HTTP and REST APIs](./03-http-and-rest-apis.md) · Next:
[05. Validation and Error Handling](./05-validation-and-error-handling.md)
