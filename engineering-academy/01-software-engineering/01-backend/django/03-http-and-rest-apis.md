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

## Serializers

A serializer turns a model into exactly the JSON the contract promises, and checks incoming data. The database
structure never leaks into the response.

**What to learn:**

- `Serializer` and `ModelSerializer`, and choosing fields explicitly instead of `fields = "__all__"`
- Renaming fields to match the contract, such as `created_at` to `createdAt`, and nested serializers for the author
- Fields that depend on the signed-in user, such as `favorited`, through the serializer context

**Resources:** [Serializers](https://www.django-rest-framework.org/api-guide/serializers/), DRF documentation

**Level:** Practitioner · Core

## Views, viewsets and routers

DRF's generic views and viewsets give each resource its list, detail, create, update and delete actions with little
code. Routers create the URLs for them.

**What to learn:**

- Generic views and viewsets, and when a plain `APIView` is clearer
- `SimpleRouter(trailing_slash=False)`, so paths match the contract with no extra routes, and
  `lookup_field = "slug"`
- Extra actions, such as `POST /api/articles/{slug}/favorite`, with the `@action` decorator

**Resources:**
[Viewsets](https://www.django-rest-framework.org/api-guide/viewsets/) and
[routers](https://www.django-rest-framework.org/api-guide/routers/), DRF documentation

**Level:** Practitioner · Core

## Status codes and headers

The status code tells the client what happened before it reads the body. The right code lets a front end react
correctly without guessing.

**What to learn:**

- 200, 201 with the new resource, and 204 with no body
- 401 for "who are you?", 403 for "you may not", 404, 409 and 422
- Using the constants in `rest_framework.status`

**Resources:**
[HTTP status codes](../../../../standards/general/rest-api-best-practices.md#6-http-status-codes-descriptive), in the
Techversant REST API best practices

**Level:** Practitioner · Core

## Filtering and pagination

Lists can grow without limit. Filters and pagination keep responses small and fast.

**What to learn:**

- Filtering a queryset by query parameters, such as `?tag=python&author=jane`
- DRF's `LimitOffsetPagination`, with `PAGE_SIZE` set to 20, the contract's default, a safe maximum page size,
  and response keys changed to match the contract
- Returning the total count, as the RealWorld contract does with `articlesCount`

**Resources:**

- [Pagination](https://www.django-rest-framework.org/api-guide/pagination/), DRF documentation
- [Filtering, sorting and pagination](../../../../standards/general/rest-api-best-practices.md#8-filtering-sorting--pagination),
  in the Techversant REST API best practices

**Level:** Practitioner · Core

## API documentation with OpenAPI

An OpenAPI file describes every endpoint in a format that tools can read. DRF projects can generate one from their
views and serializers.

**What to learn:**

- Reading an OpenAPI file, such as RealWorld's `openapi.yml`
- Generating documentation with drf-spectacular

**Resources:** [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/)

**Level:** Advanced · Optional

## Project: Shape Every Endpoint

**Brief:** Add a view, serializer and URL for every endpoint in the RealWorld `openapi.yml`. Return sample data that
matches the specification exactly; stage 04 replaces it with the database.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Every method and path in `openapi.yml` has a URL, with no trailing slashes, and there are no others under `/api`
- [ ] `GET /api/articles/feed` reaches the feed view, not the view for a single article
- [ ] Every response, including lists, has the exact keys, nesting and types in the specification
- [ ] Article URLs use the slug, not an ID
- [ ] Sign-up, creating an article and adding a comment return 201, and every other endpoint returns the status the
  specification gives
- [ ] `GET /api/articles` reads `tag`, `author`, `favorited`, `limit` and `offset`, and caps `limit` at a safe
  maximum
- [ ] Serializers list their fields explicitly, and views contain no response formatting

Previous: [02. The Framework](./02-the-framework.md) · Next:
[04. Databases and Data Access](./04-databases-and-data-access.md)
