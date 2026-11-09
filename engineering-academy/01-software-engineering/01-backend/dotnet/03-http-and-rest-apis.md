# 03. HTTP and REST APIs

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

An API is a contract: front ends, mobile apps and other systems rely on its URLs, fields and status codes staying
the same. This stage covers designing endpoints well and returning exactly the shape the contract promises. Back to
the [roadmap](./README.md).

## REST API design

Good APIs are predictable. Once a client knows how one endpoint works, it can guess how the others work.

**What to learn:**

- Resources and URLs, such as `/api/articles/{slug}/comments`, and which HTTP method does what
- Plural nouns, nesting only one level deep, and never putting verbs in URLs
- Versioning an API, and keeping changes backwards compatible

**Resources:**
[REST API best practices](../../../../standards/general/rest-api-best-practices.md), Techversant

**Level:** Practitioner · Core

## Request and response DTOs

Data transfer objects (DTOs) hold exactly what a request or response carries. Returning entities directly leaks the
database structure and can expose fields such as password hashes.

**What to learn:**

- C# records as request and response DTOs, and mapping entities to them in one place
- Wrapping a response in a key, such as `{"article": {...}}`, and reading wrapped request bodies
- How System.Text.Json names fields in camel case, writes dates and `null` values, and why an empty list must be
  `[]`, not `null`
- Keeping `null` fields in responses, such as `"bio": null`, because the contract returns them, and never ignoring
  `null` values globally
- A separate summary DTO for article lists, because list items leave out `body` entirely

**Resources:**
[System.Text.Json overview](https://learn.microsoft.com/en-us/dotnet/standard/serialization/system-text-json/overview),
Microsoft Learn

**Level:** Practitioner · Core

## Route and query parameters

Endpoints read values from the route and the query string, and must cope when they are missing or wrong.

**What to learn:**

- Binding route and query values to method parameters, with defaults for optional values
- Route constraints, and what happens when a value cannot be converted, such as `limit=abc`
- Trailing slashes and case: how ASP.NET Core matches paths

**Resources:**
[Route constraints](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/routing#route-constraints), Microsoft
Learn

**Level:** Practitioner · Core

## Status codes and headers

Status codes tell clients what happened without reading the body. The wrong code breaks client error handling.

**What to learn:**

- 200, 201 and 204 for success, 401 and 403 for sign-in and permission errors, 404, 409 and 422 for client errors
- `TypedResults` such as `Created`, `NoContent` and `NotFound`
- Headers such as `Location` and `Content-Type`

**Resources:**
[HTTP status codes](../../../../standards/general/rest-api-best-practices.md#6-http-status-codes-descriptive), in the
Techversant REST API best practices

**Level:** Practitioner · Core

## Filtering and pagination

Lists can grow without limit, so every list endpoint needs paging and a sensible maximum.

**What to learn:**

- Limit and offset paging, as RealWorld uses, and cursor paging for very large lists
- Filtering with query parameters, such as `?tag=dotnet&author=jake`
- Returning the total count, such as `articlesCount`, with each page

**Resources:**
[Filtering, sorting and pagination](../../../../standards/general/rest-api-best-practices.md#8-filtering-sorting--pagination),
in the Techversant REST API best practices

**Level:** Practitioner · Core

## API documentation with OpenAPI

ASP.NET Core can generate an OpenAPI document from your endpoints, so the documentation cannot drift from the code.

**What to learn:**

- The built-in OpenAPI support, which writes OpenAPI 3.1 by default in ASP.NET Core 10, and comparing its output with
  RealWorld's `openapi.yml`

**Resources:**
[OpenAPI support](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/openapi/overview), Microsoft Learn

**Level:** Advanced · Optional

## Project: Shape Every Endpoint

**Brief:** Add an endpoint, with request and response DTOs, for every method and path in the RealWorld
`openapi.yml`. Return sample data that matches
the specification exactly; stage 04 replaces it with the database.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Every method and path in `openapi.yml` has an endpoint, and there are no others under `/api`
- [ ] `GET /api/articles/feed` reaches the feed endpoint, not the endpoint for a single article
- [ ] Every response, including lists, has the exact keys, nesting and types in the specification, with `[]` for
  empty lists and `null` where the specification allows it
- [ ] Article paths use the slug, not an ID
- [ ] Sign-up, creating an article and adding a comment return 201, and every other endpoint returns the status the
  specification gives
- [ ] `GET /api/articles` reads `tag`, `author`, `favorited`, `limit` and `offset`, and caps `limit` at a safe
  maximum
- [ ] Endpoints return DTOs only, never entities or anonymous objects

Previous: [02. The Framework](./02-the-framework.md) · Next:
[04. Databases and Data Access](./04-databases-and-data-access.md)
