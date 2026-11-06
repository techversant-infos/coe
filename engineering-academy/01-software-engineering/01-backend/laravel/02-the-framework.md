# 02. The Framework

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Laravel gives you a structure, a set of tools and a way of doing common jobs, so every Techversant Laravel project
feels familiar. This stage covers how a request travels through Laravel 13 and where your code fits. Back to the
[roadmap](./README.md).

## Project structure and Artisan

Every Laravel project has the same folders, so you can find your way around any of them. Artisan, the command-line
tool, creates files and runs tasks.

**What to learn:**

- Creating a project, and what lives in `app`, `bootstrap`, `config`, `database`, `routes` and `tests`
- Creating classes with `make:` commands, and listing routes with `route:list`
- Where Techversant projects put services and other code that is not a controller or model

**Resources:**

- [Directory structure](https://laravel.com/docs/13.x/structure) and
  [Artisan console](https://laravel.com/docs/13.x/artisan), Laravel documentation
- [Project structure](../../../../standards/php/php-coding-standards.md#2-project-structure), in the Techversant PHP
  coding standards

**Level:** Practitioner · Core

## Request lifecycle and the service container

A request enters through `public/index.php`, passes through middleware, reaches your route, and returns a response.
The service container builds your classes and passes in what they need.

**What to learn:**

- The order a request follows, and where `bootstrap/app.php` configures routing, middleware and exceptions
- Dependency injection through constructors, and binding an interface to a class in a service provider
- Facades, and when to inject a dependency instead

**Resources:**

- [Request lifecycle](https://laravel.com/docs/13.x/lifecycle) and
  [Service container](https://laravel.com/docs/13.x/container), Laravel documentation

**Level:** Practitioner · Core

## Routing and controllers

Routes map a method and URL to the code that handles it. Controllers group the handlers for one resource.

**What to learn:**

- Turning on API routes with `php artisan install:api`, which creates `routes/api.php` under the `/api` prefix
- Route parameters, named routes and route groups
- Controllers with one job each, and keeping business logic out of them

**Resources:**

- [Routing](https://laravel.com/docs/13.x/routing) and [Controllers](https://laravel.com/docs/13.x/controllers),
  Laravel documentation

**Level:** Practitioner · Core

## Middleware

Middleware runs before or after the code for a route, such as adding a request ID to every log line or checking the
sign-in token.

**What to learn:**

- Writing middleware, and adding it to one route, a group or every request
- Middleware order, and the middleware Laravel adds to API routes
- Declaring middleware on a controller with the `#[Middleware]` attribute, added in Laravel 13

**Resources:** [Middleware](https://laravel.com/docs/13.x/middleware), Laravel documentation

**Level:** Practitioner · Core

## Configuration and environments

Settings that change between your machine, staging and production live in environment variables, never in code.

**What to learn:**

- The `.env` file, `config` files, and reading settings with `config()`, not `env()`, outside config files
- Why `.env` is never committed, and what goes in `.env.example`
- Caching configuration in production, and why `env()` then stops working outside config files

**Resources:**

- [Configuration](https://laravel.com/docs/13.x/configuration), Laravel documentation
- [Environment configuration](../../../../standards/php/php-best-practices.md#4-environment-configuration), in the
  Techversant PHP best practices

**Level:** Practitioner · Core

## Laravel AI SDK

Laravel 13 includes a first-party AI SDK for text generation, agents and embeddings. Learn it when a project adds AI
features.

**What to learn:**

- Calling a model through the SDK, and keeping API keys in configuration
- Techversant's rules for AI features in client applications

**Resources:**

- [Laravel 13 release notes](https://laravel.com/docs/13.x/releases), Laravel documentation
- [LLM application security](../../../../security/audit/security-audit-reference.md#142-llm-application-security),
  in the Techversant security audit reference

**Level:** Advanced · Optional

## Project: Start the API

**Brief:** Create a Laravel 13 project for your RealWorld API, turn on API routes, and add the first endpoint,
`GET /api/tags`, returning `{"tags": []}` for now.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] The project runs on PHP 8.3 or later, with API routes turned on and served under `/api`
- [ ] `GET /api/tags` returns status 200 and `{"tags": []}`
- [ ] An unknown path under `/api` returns a JSON 404, not an HTML page
- [ ] A middleware adds a request ID to every response header and log line, and has a test
- [ ] `.env` is not committed, `.env.example` lists every setting, and code reads settings through `config()`
- [ ] Pint or PHP_CodeSniffer and PHPStan level 8 run with no errors
- [ ] The README explains how to install, run and test the project

Previous: [01. Language Fundamentals](./01-language-fundamentals.md) · Next:
[03. HTTP and REST APIs](./03-http-and-rest-apis.md)
