# 03. HTTP and REST APIs

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

An API is a contract: front ends, mobile apps and other systems rely on its URLs, fields and status codes staying
the same. This stage covers designing endpoints well and returning exactly the shape the contract promises. Back to
the [roadmap](./README.md).

## REST API design

REST APIs model the system as resources, such as articles and comments, and use HTTP methods to act on them.
Techversant has one standard for how its APIs look.

**What to learn:**

- Resource URLs, nesting, and when an action endpoint is the right choice
- Which HTTP methods are safe and idempotent, and what that means for retries
- JSON field naming, dates in ISO 8601, and the difference between a `null` field and a missing one

**Resources:**
[REST API best practices](../../../../standards/general/rest-api-best-practices.md), Techversant

**Level:** Practitioner · Core

## Request and response DTOs

Data transfer objects (DTOs) hold exactly what a request or response carries. Returning entities directly leaks the
database structure and can expose fields such as password hashes.

**What to learn:**

- Java records as request and response DTOs, and mapping entities to them in one place
- Wrapping a response in a key, such as `{"article": {...}}`, and reading wrapped request bodies
- How Jackson 3, the JSON library in Spring Boot 4, names fields and writes dates and `null` values. Jackson 3
  moved to the `tools.jackson` packages, while its annotations stay in `com.fasterxml.jackson.annotation`.
- Keeping `null` fields in responses, such as `"bio": null`, because the contract returns them: do not set
  `default-property-inclusion` to `non_null`

**Resources:**
[JSON](https://docs.spring.io/spring-boot/reference/features/json.html), Spring Boot documentation

**Level:** Practitioner · Core

## Path matching and parameters

Spring matches each request to the most specific mapping. Knowing the rules prevents surprises, such as a fixed path
being read as a parameter.

**What to learn:**

- How a fixed path such as `/api/articles/feed` wins over a pattern such as `/api/articles/{slug}`
- Required and optional query parameters, and their default values
- Spring's handling of trailing slashes, which it does not match by default

**Resources:**
[Request mapping](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller/ann-requestmapping.html),
Spring Framework documentation

**Level:** Practitioner · Core

## Status codes and headers

The status code tells the client what happened before it reads the body. The right code lets a front end react
correctly without guessing.

**What to learn:**

- 200, 201 with the new resource, and 204 with no body
- 401 for "who are you?", 403 for "you may not", 404, 409 and 422
- Setting status codes and headers with `ResponseEntity` or `@ResponseStatus`

**Resources:**
[HTTP status codes](../../../../standards/general/rest-api-best-practices.md#6-http-status-codes-descriptive), in the
Techversant REST API best practices

**Level:** Practitioner · Core

## Filtering and pagination

Lists can grow without limit. Filters and pagination keep responses small and fast.

**What to learn:**

- Filtering by query parameters, such as `?tag=java&author=jane`
- Limit and offset pagination, with a safe maximum page size. Spring Data's `Pageable` works in pages, so the
  contract's `offset` needs its own handling.
- Returning the total count, as the RealWorld contract does with `articlesCount`

**Resources:**
[Filtering, sorting and pagination](../../../../standards/general/rest-api-best-practices.md#8-filtering-sorting--pagination),
in the Techversant REST API best practices

**Level:** Practitioner · Core

## API documentation with OpenAPI

An OpenAPI file describes every endpoint in a format that tools can read. Spring projects can generate one from their
controllers.

**What to learn:**

- Reading an OpenAPI file, such as RealWorld's `openapi.yml`
- Generating documentation with springdoc-openapi

**Resources:** [springdoc-openapi](https://springdoc.org/)

**Level:** Advanced · Optional

## Project: Shape Every Endpoint

**Brief:** Add a controller method and DTOs for every endpoint in the RealWorld `openapi.yml`. Return sample data that
matches the specification exactly; stage 04 replaces it with the database.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Every method and path in `openapi.yml` has a mapping, and there are no others under `/api`
- [ ] `GET /api/articles/feed` reaches the feed method, not the method for a single article
- [ ] Every response, including lists, has the exact keys, nesting and types in the specification
- [ ] Article paths use the slug, not an ID
- [ ] Sign-up, creating an article and adding a comment return 201, and every other endpoint returns the status the
  specification gives
- [ ] `GET /api/articles` reads `tag`, `author`, `favorited`, `limit` and `offset`, and caps `limit` at a safe
  maximum
- [ ] Controllers return DTOs only, never entities or maps

Previous: [02. The Framework](./02-the-framework.md) · Next:
[04. Databases and Data Access](./04-databases-and-data-access.md)
