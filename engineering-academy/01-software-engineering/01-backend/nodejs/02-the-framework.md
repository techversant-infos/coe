# 02. The Framework

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Fastify gives a Node.js service its routing, request handling, validation and logging. This stage covers how a
request travels through Fastify and how Techversant lays out a service around it. Back to the
[roadmap](./README.md).

## Fastify basics

A Fastify server is built from routes and plugins. Each route has a method, a URL and a handler that returns the
response.

**What to learn:**

- Creating a server, adding routes, and returning JSON from a handler
- Route parameters and query strings, and route prefixes such as `/api`
- Starting and stopping the server cleanly, and testing a route with `inject` without opening a port

**Resources:** [Getting started](https://fastify.dev/docs/latest/Guides/Getting-Started/), Fastify documentation

**Level:** Practitioner · Core

## Plugins and encapsulation

Plugins add routes, hooks and shared objects, such as a database client. Encapsulation keeps what one plugin adds
from leaking into others unless you share it on purpose.

**What to learn:**

- Writing a plugin, and registering it with a prefix
- Decorators for shared objects, and `fastify-plugin` for sharing them with the whole app
- Plugin load order, and waiting for plugins to be ready

**Resources:** [Plugins guide](https://fastify.dev/docs/latest/Guides/Plugins-Guide/), Fastify documentation

**Level:** Practitioner · Core

## Project layout and boundaries

Techversant services keep business rules away from the framework. Route handlers stay thin, services hold the
rules, and adapters talk to databases and other systems.

**What to learn:**

- The Techversant layout: `api`, `modules`, `infra`, `shared` and `config` folders
- Ports and adapters: business code depends on an interface, such as an article repository, not on Prisma
- Passing dependencies in, such as the repository and the clock, so code is easy to test

**Resources:**

- [Project layout](../../../../standards/nodejs/nodejs-typescript-style-guide.md#2-project-layout), in the Techversant
  Node.js and TypeScript style guide
- [Architecture and boundaries](../../../../standards/nodejs/nodejs-typescript-best-practices.md#architecture--boundaries),
  in the Techversant Node.js and TypeScript best practices

**Level:** Practitioner · Core

## Hooks and the request lifecycle

A request passes through a series of hooks before and after the handler. Hooks are where you check tokens, add
context to logs and shape responses.

**What to learn:**

- The order of hooks, such as `onRequest`, `preHandler` and `onSend`
- Request IDs, and Fastify's built-in Pino logger with one child logger per request
- Adding a hook to one route, one plugin or the whole app

**Resources:**

- [Lifecycle](https://fastify.dev/docs/latest/Reference/Lifecycle/) and
  [Hooks](https://fastify.dev/docs/latest/Reference/Hooks/), Fastify documentation

**Level:** Practitioner · Core

## Configuration and environments

Settings that change between your machine, staging and production live in environment variables. Techversant
services validate them at start-up and refuse to start when one is missing.

**What to learn:**

- Reading configuration once, validating it with a Zod schema, and passing it in
- Why `.env` is never committed, and what goes in `.env.example`
- Keeping environment checks out of business code

**Resources:**
[Configuration and secrets](../../../../standards/nodejs/nodejs-typescript-best-practices.md#configuration--secrets),
in the Techversant Node.js and TypeScript best practices

**Level:** Practitioner · Core

## NestJS

NestJS is a larger framework with modules, dependency injection and decorators. Some client projects use it. Learn
it when your project does.

**What to learn:**

- Modules, controllers and providers, and how they map to the layout in this stage

**Resources:** [NestJS documentation](https://docs.nestjs.com/)

**Level:** Advanced · Optional

## Project: Start the API

**Brief:** Create a Fastify and TypeScript service for your RealWorld API, laid out the Techversant way, and add the
first endpoint, `GET /api/tags`, returning `{"tags": []}` for now.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] The service runs on the current Node.js LTS release, follows the Techversant project layout, and serves its
  routes under `/api`
- [ ] `GET /api/tags` returns status 200 and `{"tags": []}`
- [ ] An unknown path under `/api` returns a JSON 404
- [ ] Every response has a request ID header, and every log line is JSON with the same request ID
- [ ] Configuration is validated with Zod at start-up, and the service refuses to start when a required setting is
  missing
- [ ] `.env` is not committed, and `.env.example` lists every setting
- [ ] The type check, ESLint and an `inject` test for `GET /api/tags` pass
- [ ] The README explains how to install, run and test the service

Previous: [01. Language Fundamentals](./01-language-fundamentals.md) · Next:
[03. HTTP and REST APIs](./03-http-and-rest-apis.md)
