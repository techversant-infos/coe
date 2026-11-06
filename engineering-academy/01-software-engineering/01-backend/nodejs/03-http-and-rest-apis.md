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

- [REST API best practices](../../../../standards/general/rest-api-best-practices.md), Techversant
- [API design](../../../../standards/nodejs/nodejs-typescript-style-guide.md#10-api-design), in the Techversant
  Node.js and TypeScript style guide

**Level:** Practitioner · Core

## Route schemas with Zod

In Fastify, each route can declare schemas for its parameters, query string, body and responses. With a Zod type
provider, one Zod schema both validates the request and types the handler.

**What to learn:**

- Setting up `fastify-type-provider-zod`, and declaring `params`, `querystring` and `body` schemas
- Getting typed request data in the handler without casting
- Sharing schemas between routes, such as one `Article` schema for every response that returns an article

**Resources:**

- [Type providers](https://fastify.dev/docs/latest/Reference/Type-Providers/), Fastify documentation
- [Validation and DTOs](../../../../standards/nodejs/nodejs-typescript-best-practices.md#validation--dtos), in the
  Techversant Node.js and TypeScript best practices

**Level:** Practitioner · Core

## Response shapes

The response must match the contract exactly, whatever the database looks like. A response schema shapes the output
and drops any field it does not list, so internal fields never leak.

**What to learn:**

- Declaring a response schema for each status code
- Mapping database records to response objects in one place, such as `toArticleResponse`
- Wrapping responses in a key, such as `{"article": {...}}`, and naming fields the way the contract does

**Resources:**
[Validation and serialization](https://fastify.dev/docs/latest/Reference/Validation-and-Serialization/), Fastify
documentation

**Level:** Practitioner · Core

## Status codes and headers

The status code tells the client what happened before it reads the body. The right code lets a front end react
correctly without guessing.

**What to learn:**

- 200, 201 with the new resource, and 204 with no body
- 401 for "who are you?", 403 for "you may not", 404, 409 and 422
- Setting status codes and headers with `reply.code()` and `reply.header()`

**Resources:**
[HTTP status codes](../../../../standards/general/rest-api-best-practices.md#6-http-status-codes-descriptive), in the
Techversant REST API best practices

**Level:** Practitioner · Core

## Filtering and pagination

Lists can grow without limit. Filters and pagination keep responses small and fast.

**What to learn:**

- Filtering by query parameters, such as `?tag=node&author=jane`, with numbers parsed and checked by the schema
- Limit and offset pagination, with a safe maximum page size
- Returning the total count, as the RealWorld contract does with `articlesCount`

**Resources:**
[Filtering, sorting and pagination](../../../../standards/general/rest-api-best-practices.md#8-filtering-sorting--pagination),
in the Techversant REST API best practices

**Level:** Practitioner · Core

## API documentation with OpenAPI

An OpenAPI file describes every endpoint in a format that tools can read. Fastify can generate one from your route
schemas.

**What to learn:**

- Reading an OpenAPI file, such as RealWorld's `openapi.yml`
- Generating documentation with `@fastify/swagger`

**Resources:** [@fastify/swagger](https://github.com/fastify/fastify-swagger)

**Level:** Advanced · Optional

## Project: Shape Every Endpoint

**Brief:** Add a route with Zod schemas for every endpoint in the RealWorld `openapi.yml`. Return sample data that
matches the specification exactly; stage 04 replaces it with the database.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Every method and path in `openapi.yml` has a route, and there are no others under `/api`
- [ ] `GET /api/articles/feed` reaches the feed route, not the route for a single article
- [ ] Every route has a response schema, and every response has the exact keys, nesting and types in the
  specification
- [ ] Article routes use the slug, not an ID
- [ ] Sign-up, creating an article and adding a comment return 201, and every other endpoint returns the status the
  specification gives
- [ ] `GET /api/articles` reads `tag`, `author`, `favorited`, `limit` and `offset`, and caps `limit` at a safe
  maximum
- [ ] Handlers get typed request data from the schemas, with no type casts

Previous: [02. The Framework](./02-the-framework.md) · Next:
[04. Databases and Data Access](./04-databases-and-data-access.md)
