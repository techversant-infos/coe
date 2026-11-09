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

## JSON requests and responses

Go maps JSON to structs with field tags. Small details, such as a `nil` slice, decide whether a response matches the
contract.

**What to learn:**

- Request and response structs with `json` tags, and wrapper structs for bodies such as `{"article": {...}}`
- Why a `nil` slice becomes `null` in JSON, and always returning an empty list, such as `"tagList": []`
- Pointer fields for values that can be `null`, such as `"bio": null`
- Helpers that read and write JSON in one place, set the `Content-Type` header and turn a body that will not decode
  into a clear error

**Resources:** [Package encoding/json](https://pkg.go.dev/encoding/json), Go documentation

**Level:** Practitioner · Core

## Path and query parameters

Handlers read values from the path and the query string, and must cope when they are missing or wrong.

**What to learn:**

- Reading path values with `r.PathValue`, and query values with `r.URL.Query()`
- Converting text to numbers with `strconv`, with defaults for missing values and errors for bad ones
- Trailing slashes, and why `/api/articles/` and `/api/articles` are different patterns

**Resources:** [Routing enhancements](https://go.dev/blog/routing-enhancements), the Go blog

**Level:** Practitioner · Core

## Status codes and headers

Status codes tell clients what happened without reading the body. The wrong code breaks client error handling.

**What to learn:**

- 200, 201 and 204 for success, 401 and 403 for sign-in and permission errors, 404, 409 and 422 for client errors
- Setting headers, including `Content-Type`, before calling `w.WriteHeader`, because changes after `WriteHeader`
  or the first `Write` are ignored
- Headers such as `Location` and `Content-Type`

**Resources:**
[HTTP status codes](../../../../standards/general/rest-api-best-practices.md#6-http-status-codes-descriptive), in the
Techversant REST API best practices

**Level:** Practitioner · Core

## Filtering and pagination

Lists can grow without limit, so every list endpoint needs paging and a sensible maximum.

**What to learn:**

- Limit and offset paging, as RealWorld uses, and cursor paging for very large lists
- Filtering with query parameters, such as `?tag=go&author=jake`
- Returning the total count, such as `articlesCount`, with each page

**Resources:**
[Filtering, sorting and pagination](../../../../standards/general/rest-api-best-practices.md#8-filtering-sorting--pagination),
in the Techversant REST API best practices

**Level:** Practitioner · Core

## API documentation with OpenAPI

An OpenAPI file describes every endpoint. Tools can generate Go types and server interfaces from it, so the code
cannot drift from the contract.

**What to learn:**

- Generating request and response types from RealWorld's `openapi.yml` with oapi-codegen, and when hand-written
  types are clearer

**Resources:** [oapi-codegen](https://github.com/oapi-codegen/oapi-codegen)

**Level:** Advanced · Optional

## Project: Shape Every Endpoint

**Brief:** Add a route, a handler and request and response types for every endpoint in the RealWorld `openapi.yml`.
Return sample data that matches the specification exactly; stage 04 replaces it with the database.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Every method and path in `openapi.yml` has a route, and there are no others under `/api`
- [ ] `GET /api/articles/feed` reaches the feed handler, not the handler for a single article
- [ ] Every response, including lists, has the exact keys, nesting and types in the specification, with `[]` for
  empty lists and `null` where the specification allows it
- [ ] Article paths use the slug, not an ID
- [ ] Sign-up, creating an article and adding a comment return 201, and every other endpoint returns the status the
  specification gives
- [ ] `GET /api/articles` reads `tag`, `author`, `favorited`, `limit` and `offset`, rejects values that are not
  numbers, and caps `limit` at a safe maximum
- [ ] Handlers write response structs only, never database rows or maps

Previous: [02. The Framework](./02-the-framework.md) · Next:
[04. Databases and Data Access](./04-databases-and-data-access.md)
