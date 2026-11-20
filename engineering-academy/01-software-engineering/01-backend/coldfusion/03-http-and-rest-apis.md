# 03. HTTP and REST APIs

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-20 · **Next review:** 2027-05-20

A REST API is a contract. Front ends, mobile apps and other teams build against it, so every name, status code and
response shape matters. CFML (ColdFusion Markup Language) adds one more job: making sure the JSON it produces has the
exact keys and types the contract asks for. Back to the [roadmap](./README.md).

## REST API design

Good APIs are predictable. Techversant's REST API standard sets the rules for naming, responses and errors on client
projects.

**What to learn:**

- Resources as plural nouns, and HTTP methods for actions: `GET`, `POST`, `PUT`, `PATCH` and `DELETE`
- Which methods are safe, and which are idempotent, meaning repeating the request has the same effect
- Where the RealWorld contract differs from Techversant's rules, listed on the [practice app](../practice-app.md) page

**Resources:**
[REST API best practices](../../../../standards/general/rest-api-best-practices.md), Techversant

**Level:** Practitioner · Core

## Resource routes

ColdBox can register all the routes for a resource in one line, and you add the extra routes the contract needs.

**What to learn:**

- `resources()` in `config/Router.cfc`, which handler action each route calls, and setting `parameterName` to
  `slug`, because the default is `:id`
- Route parameters such as `:slug`, and the order of routes: `/api/articles/feed` must come before
  `/api/articles/:slug`, or the router reads `feed` as a slug
- Restricting each action to its HTTP methods, so a wrong method returns 405

**Resources:**

- [Resourceful routes](https://coldbox.ortusbooks.com/the-basics/routing/routing-dsl/resourceful-routes) and
  [HTTP method security](https://coldbox.ortusbooks.com/the-basics/event-handlers/http-method-security), ColdBox
  documentation

**Level:** Practitioner · Core

## JSON in CFML

CFML turns structs and arrays into JSON with `serializeJSON()`, and ColdBox does it for you in `RestHandler`. The
engines make choices you must check, or the response will not match the contract.

**What to learn:**

- Key case: Adobe ColdFusion turns struct keys into upper case unless `Application.cfc` sets
  `this.serialization.preserveCaseForStructKey = true`, and Lucee does the same for keys written with dot notation,
  such as `user.email = ...`. Set the option, write keys in quotes, such as `{"email": user.email}`, and check the JSON
- Types: make sure booleans, numbers and empty arrays come out as JSON types, not strings such as `"true"`
- Null: without null support, a database `NULL` reaches CFML as an empty string, so `bio` would come out as `""`
  instead of `null`. Turn on full null support with `this.nullSupport = true` on Lucee and
  `this.enableNullSupport = true` on Adobe ColdFusion, and test the JSON on both engines
- Dates: `serializeJSON()` does not write ISO 8601, so format each date yourself in UTC with `dateTimeFormat()`,
  such as `2026-11-20T09:30:00.000Z`
- Building the response shape in one place for each resource, so every endpoint returns an article the same way

**Resources:**

- [serializeJSON()](https://docs.lucee.org/reference/functions/serializejson.html) and
  [Preserving struct key case](https://docs.lucee.org/recipes/structs-preserve-key-case.html) and
  [Null support](https://docs.lucee.org/recipes/null-support.html), Lucee documentation
- [serializeJSON()](https://helpx.adobe.com/coldfusion/cfml-reference/coldfusion-functions/functions-s/serializejson.html),
  Adobe ColdFusion documentation
- [Rendering data](https://coldbox.ortusbooks.com/the-basics/event-handlers/rendering-data), ColdBox documentation

**Level:** Practitioner · Core

## Status codes and headers

The status code tells the client what happened before it reads the body. Headers carry details such as the content
type and where a new resource lives.

**What to learn:**

- 200, 201, 204, 400, 401, 403, 404, 409, 422 and 500, and choosing between them
- Setting the status and headers through `event.getResponse()`, and returning JSON for every `/api` path even when
  the request has no `Accept` header
- `Content-Type: application/json`, and the `Location` header for a new resource

**Resources:**

- [HTTP status codes](../../../../standards/general/rest-api-best-practices.md#6-http-status-codes-descriptive), in the
  Techversant REST API best practices
- [RestHandler](https://coldbox.ortusbooks.com/digging-deeper/rest-handler), ColdBox documentation

**Level:** Practitioner · Core

## Filtering and pagination

List endpoints must stay fast and usable as data grows. Clients filter and page through results with query
parameters.

**What to learn:**

- Reading query parameters such as `tag`, `author`, `limit` and `offset` through the request context
- Offset pagination, a safe maximum for `limit`, and returning the total count
- Checking every parameter's type and range before you use it

**Resources:**
[Filtering, sorting and pagination](../../../../standards/general/rest-api-best-practices.md#8-filtering-sorting--pagination),
in the Techversant REST API best practices

**Level:** Practitioner · Core

## Browser clients and AJAX

Many CFML applications serve their own pages and call the server from the browser with AJAX (asynchronous JavaScript and
XML) requests. You need to read and maintain that code as well as write APIs.

**What to learn:**

- Calling an API with the browser's Fetch API, sending JSON and handling error responses
- Reading and maintaining jQuery `$.ajax()` calls in older pages, and not adding jQuery to new code
- Encoding values before they go into HTML, and sending forms with a cross-site request forgery (CSRF) token

**Resources:**

- [Using the Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch), MDN Web Docs
- [Cross-site scripting and output encoding](../../../../security/audit/security-audit-reference.md#73-cross-site-scripting-and-output-encoding),
  in the Techversant security audit reference

**Level:** Practitioner · Optional

## API documentation with OpenAPI

An OpenAPI document describes every endpoint, so front-end teams can build against the API before it is finished.

**What to learn:**

- Reading an OpenAPI file, such as RealWorld's `openapi.yml`
- Generating documentation from your handlers with the cbswagger module

**Resources:**

- [OpenAPI specification](https://spec.openapis.org/oas/latest.html)
- [cbswagger](https://www.forgebox.io/view/cbswagger), ForgeBox

**Level:** Advanced · Optional

## Project: Shape Every Endpoint

**Brief:** Add a route and handler action for every endpoint in the RealWorld `openapi.yml`. Return sample data that
matches the specification exactly; stage 04 replaces it with the database.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] The router registers every method and path in `openapi.yml`, and no others, with `GET /api/articles/feed`
  registered before `GET /api/articles/:slug`
- [ ] Every response, including lists, has the exact keys, key case, nesting and types in the specification, with `null`
  for an empty `bio` or `image` and ISO 8601 dates, checked on the raw JSON
- [ ] Article routes use the slug, not an ID
- [ ] Sign-up, creating an article and adding a comment return 201, and every other endpoint returns the status the
  specification gives
- [ ] `GET /api/articles` reads `tag`, `author`, `favorited`, `limit` and `offset`, and caps `limit` at a safe
  maximum
- [ ] Each resource has one function that builds its response shape, and handlers do no other formatting

Previous: [02. The Framework](./02-the-framework.md) · Next:
[04. Databases and Data Access](./04-databases-and-data-access.md)
