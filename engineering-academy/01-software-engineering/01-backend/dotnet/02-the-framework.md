# 02. The Framework

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

ASP.NET Core is the web framework of .NET. This stage covers how an ASP.NET Core 10 app starts, handles a request and
wires your classes together. Back to the [roadmap](./README.md).

## Minimal APIs and controllers

ASP.NET Core offers two ways to write endpoints. Minimal APIs map a route to a method; controllers group endpoints in
classes.

**What to learn:**

- Minimal APIs with `MapGet` and `MapPost`, route groups with `MapGroup`, and returning `TypedResults`
- Controllers with `[ApiController]`, and how to work in a project that already uses them
- Keeping endpoints thin, with business rules in services

**Resources:**
[Minimal APIs overview](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/overview), Microsoft
Learn

**Level:** Practitioner · Core

## Dependency injection

ASP.NET Core creates your services and passes each one the services it needs. Code depends on interfaces, which
makes it easier to test and change.

**What to learn:**

- Registering services as singleton, scoped or transient, and what each lifetime means for a request
- Constructor injection, and the bug where a singleton keeps hold of a scoped service, such as the database context

**Resources:**
[Dependency injection](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection), Microsoft
Learn

**Level:** Practitioner · Core

## Middleware and the request pipeline

Every request passes through a pipeline of middleware before it reaches an endpoint. The order of the pipeline
decides what runs first.

**What to learn:**

- The order of the built-in middleware, such as exception handling, authentication and authorization
- Writing your own middleware, such as one that adds a request ID to every response and to the logging scope
- Testing a middleware

**Resources:**
[Write custom middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/write), Microsoft
Learn

**Level:** Practitioner · Core

## Routing

Routing matches a request's method and path to an endpoint.

**What to learn:**

- Route templates, parameters and constraints, such as `/api/articles/{slug}`
- Why a literal segment beats a parameter, so `GET /api/articles/feed` never reaches the single-article endpoint
- ASP.NET Core's empty 404 and 405 responses, and replacing them with JSON

**Resources:**
[Routing](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/routing), Microsoft Learn

**Level:** Practitioner · Core

## Configuration and options

Settings come from `appsettings.json`, environment variables and, on your machine, user secrets. The options pattern
binds them to typed classes.

**What to learn:**

- Configuration sources and their order, and keeping secrets out of `appsettings.json`
- Binding settings to options classes, validating them, and checking them at start-up with `ValidateOnStart`
- Environments, such as Development and Production

**Resources:**
[Options pattern](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/configuration/options), Microsoft Learn

**Level:** Practitioner · Core

## AI features with Microsoft.Extensions.AI

Microsoft.Extensions.AI gives .NET one way to call language models from different providers. Learn it when a project
adds AI features.

**What to learn:**

- Calling a model through `IChatClient`, with API keys in configuration
- Techversant's rules for AI features in client applications

**Resources:**

- [Microsoft.Extensions.AI](https://learn.microsoft.com/en-us/dotnet/ai/microsoft-extensions-ai), Microsoft Learn
- [LLM application security](../../../../security/audit/security-audit-reference.md#142-llm-application-security),
  in the Techversant security audit reference

**Level:** Advanced · Optional

## Project: Start the API

**Brief:** Create an ASP.NET Core 10 project for your RealWorld API, and add the first endpoint, `GET /api/tags`,
returning `{"tags": []}` for now.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] The project builds on .NET 10 with the software development kit (SDK) pinned in `global.json`, and serves its
  endpoints under `/api`
- [ ] `GET /api/tags` returns status 200 and `{"tags": []}`
- [ ] An unknown path under `/api` returns a JSON 404, and a wrong method returns a JSON 405, not an empty body
- [ ] A middleware adds a request ID to every response header and log line, and has a test
- [ ] Settings are bound to options classes validated at start-up, and no secret is in the repository
- [ ] The build treats warnings as errors, and `dotnet format --verify-no-changes` passes
- [ ] The README explains how to build, run and test the project

Previous: [01. Language Fundamentals](./01-language-fundamentals.md) · Next:
[03. HTTP and REST APIs](./03-http-and-rest-apis.md)
