# 02. The Framework

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Go teams rarely use one large framework. A Go API is built on the standard library's `net/http` package, with small
libraries added where they help, and together they do the framework's job on this path. This stage covers how a Go
server starts, routes a request and passes your dependencies to the code that needs them. Back to the
[roadmap](./README.md).

## HTTP servers and handlers

Everything that answers a request in Go is a handler. The server runs each request in its own goroutine.

**What to learn:**

- The `http.Handler` interface and `http.HandlerFunc`, and writing status codes, headers and bodies
- An `http.Server` with read-header, read, write and idle timeouts, and why `http.ListenAndServe` on its own has no
  timeouts and is not safe in production

**Resources:** [Package net/http](https://pkg.go.dev/net/http), Go documentation

**Level:** Practitioner · Core

## Routing

The standard library's router, `http.ServeMux`, matches methods and path wildcards, so most APIs need no router
library.

**What to learn:**

- Patterns such as `GET /api/articles/{slug}`, and reading the value with `r.PathValue("slug")`
- How the most specific pattern wins, so `GET /api/articles/feed` never reaches the single-article handler
- The router's plain-text 404 and 405 responses, which `ServeMux` has no setting for: wrap the router in a
  middleware that rewrites them as JSON, or use chi's `NotFound` and `MethodNotAllowed`. A catch-all `/api/`
  pattern turns every 405 into a 404.

**Resources:** [Routing enhancements](https://go.dev/blog/routing-enhancements), the Go blog

**Level:** Practitioner · Core

## Middleware

Middleware is a function that takes a handler and returns a handler that does more, such as logging every request.

**What to learn:**

- The `func(http.Handler) http.Handler` pattern, and the order in which middleware runs
- Middleware for request IDs, request logging and recovering from a panic with a JSON 500 response
- Testing a middleware with the `net/http/httptest` package

**Resources:**

- [Middleware](https://go-chi.io/#/pages/middleware), chi documentation; the same pattern works with the standard
  library
- [Package httptest](https://pkg.go.dev/net/http/httptest), Go documentation

**Level:** Practitioner · Core

## The request context

Every request carries a context. It is cancelled when the client goes away, and it carries request-scoped values,
such as the request ID.

**What to learn:**

- `r.Context()`, and passing it to every database and network call so work stops when the request ends
- Storing request-scoped values with a private key type, and keeping business data out of the context

**Resources:** [Package context](https://pkg.go.dev/context), Go documentation

**Level:** Practitioner · Core

## Configuration and dependencies

Settings come from the environment, and dependencies, such as the database pool and the logger, are passed to the
code that needs them instead of living in global variables.

**What to learn:**

- Reading environment variables into a config struct at start-up, and refusing to start when a setting is missing
- Passing dependencies through constructors or an application struct, which is dependency injection without a
  framework
- A small `main` that calls a `run` function returning an error, so start-up is testable

**Resources:** [Config](https://12factor.net/config), The Twelve-Factor App

**Level:** Practitioner · Core

## Routers and frameworks

Some projects use a router library, such as chi, or a framework, such as Echo or Gin. Learn to work in them when a
project already does.

**What to learn:**

- What chi adds to the standard library, such as route groups and ready-made middleware
- Why a chi handler is still an ordinary `http.Handler`, while Echo and Gin use their own handler types

**Resources:** [chi](https://go-chi.io/)

**Level:** Practitioner · Optional

## Project: Start the API

**Brief:** Create a Go module for your RealWorld API, and add the first endpoint, `GET /api/tags`, returning
`{"tags": []}` for now.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] The module builds on Go 1.27, serves its endpoints under `/api`, and the server sets read-header, read, write
  and idle timeouts
- [ ] `GET /api/tags` returns status 200 and `{"tags": []}`
- [ ] An unknown path under `/api` returns a JSON 404, and a wrong method returns a JSON 405, not plain text
- [ ] A middleware adds a request ID to every response header and log line, and has a test
- [ ] A panic in a handler returns a JSON 500 and is logged, and the server keeps running
- [ ] Settings come from environment variables checked at start-up, the server refuses to start without them, and
  no secret is in the repository
- [ ] `gofmt`, `go vet` and golangci-lint report no problems
- [ ] The README explains how to build, run and test the project

Previous: [01. Language Fundamentals](./01-language-fundamentals.md) · Next:
[03. HTTP and REST APIs](./03-http-and-rest-apis.md)
