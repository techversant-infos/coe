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

## Resource routes and controllers

Laravel can create every route for a resource from one line, and a matching controller with one method for each.

**What to learn:**

- `Route::apiResource`, and limiting it to the routes you need
- Route model binding, including binding by a column such as `slug`
- Endpoints that do not fit a resource, such as `POST /api/articles/{slug}/favorite`

**Resources:**
[Resource controllers](https://laravel.com/docs/13.x/controllers#resource-controllers), Laravel documentation

**Level:** Practitioner · Core

## API resources

An API resource turns a model into exactly the JSON the contract promises, so the database structure never leaks
into the response.

**What to learn:**

- Writing `JsonResource` and resource collection classes
- Wrapping a response in a key, such as `{"article": {...}}`, and naming fields the way the contract does
- Including a field only when it applies, such as `following` for a signed-in user

**Resources:** [Eloquent API resources](https://laravel.com/docs/13.x/eloquent-resources), Laravel documentation

**Level:** Practitioner · Core

## Status codes and headers

The status code tells the client what happened before it reads the body. The right code lets a front end react
correctly without guessing.

**What to learn:**

- 200, 201 with the new resource, and 204 with no body
- 401 for "who are you?", 403 for "you may not", 404, 409 and 422
- Headers such as `Content-Type` and `Location`

**Resources:**
[HTTP status codes](../../../../standards/general/rest-api-best-practices.md#6-http-status-codes-descriptive), in the
Techversant REST API best practices

**Level:** Practitioner · Core

## Filtering and pagination

Lists can grow without limit. Filters and pagination keep responses small and fast.

**What to learn:**

- Filtering by query parameters, such as `?tag=php&author=jane`
- Limit and offset pagination, with a safe maximum page size
- Returning the total count, as the RealWorld contract does with `articlesCount`

**Resources:**
[Filtering, sorting and pagination](../../../../standards/general/rest-api-best-practices.md#8-filtering-sorting--pagination),
in the Techversant REST API best practices

**Level:** Practitioner · Core

## API documentation with OpenAPI

An OpenAPI file describes every endpoint in a format that tools can read, so clients can generate code and test
against it.

**What to learn:**

- Reading an OpenAPI file, such as RealWorld's `openapi.yml`
- Generating documentation from Laravel code, for example with the Scramble package

**Resources:** [OpenAPI specification](https://spec.openapis.org/oas/latest.html)

**Level:** Advanced · Optional

## Project: Shape Every Endpoint

**Brief:** Add a route, controller method and API resource for every endpoint in the RealWorld `openapi.yml`. Return
sample data that matches the specification exactly; stage 04 replaces it with the database.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] `route:list --path=api` shows every method and path in `openapi.yml`, and no others, with
  `GET /api/articles/feed` registered before `GET /api/articles/{article}`
- [ ] Every response, including lists, has the exact keys, nesting and types in the specification
- [ ] Article routes use the slug, not an ID
- [ ] Sign-up, creating an article and adding a comment return 201, and every other endpoint returns the status
  the specification gives
- [ ] `GET /api/articles` reads `tag`, `author`, `favorited`, `limit` and `offset`, and caps `limit` at a safe
  maximum
- [ ] Controllers contain no response formatting; API resources do it

Previous: [02. The Framework](./02-the-framework.md) · Next:
[04. Databases and Data Access](./04-databases-and-data-access.md)
