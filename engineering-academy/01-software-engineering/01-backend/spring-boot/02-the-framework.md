# 02. The Framework

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Spring Boot sets up a Spring application with sensible defaults, so you write business code instead of
configuration. This stage covers how Spring Boot 4 starts an application, handles a request and wires your classes
together. Back to the [roadmap](./README.md).

## Starters and auto-configuration

Starters bring in a set of libraries, and auto-configuration sets them up based on what is on the classpath and in
your settings.

**What to learn:**

- Creating a project with Spring Initializr, and what each starter adds, such as `spring-boot-starter-webmvc`
- How auto-configuration decides what to set up, and how to see its decisions
- Running the application, and Spring Boot's supported releases

**Resources:**

- [Spring Initializr](https://start.spring.io/)
- [Auto-configuration](https://docs.spring.io/spring-boot/reference/using/auto-configuration.html), Spring Boot
  documentation

**Level:** Practitioner · Core

## Dependency injection and beans

Spring creates your classes as beans and passes each one the beans it needs. Code depends on interfaces, which makes
it easier to test and change.

**What to learn:**

- `@Component`, `@Service` and `@Repository`, and constructor injection
- `@Configuration` classes and `@Bean` methods for objects you do not write yourself
- Bean scopes, and why beans should not hold request data in fields

**Resources:**
[Dependency injection](https://docs.spring.io/spring-framework/reference/core/beans/dependencies/factory-collaborators.html),
Spring Framework documentation

**Level:** Practitioner · Core

## Controllers

A controller maps HTTP requests to methods. Spring turns JSON request bodies into Java objects and return values into
JSON.

**What to learn:**

- `@RestController`, `@GetMapping` and the other mapping annotations, and `@PathVariable` and `@RequestParam`
- A common `/api` prefix for every controller
- Keeping controllers thin, with business logic in services

**Resources:**
[Annotated controllers](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller.html), Spring
Framework documentation

**Level:** Practitioner · Core

## Filters and the request cycle

A request passes through servlet filters, then Spring's dispatcher, then your controller. Filters are where request
IDs, logging context and security checks go.

**What to learn:**

- Writing a filter, such as one that adds a request ID to every response and to the logging context, called the
  Mapped Diagnostic Context (MDC)
- The order filters run in, and where Spring Security's filters sit
- Interceptors, and when to use one instead of a filter

**Resources:** [Filters](https://docs.spring.io/spring-framework/reference/web/webmvc/filters.html), Spring Framework
documentation

**Level:** Practitioner · Core

## Configuration and profiles

Settings that change between your machine, staging and production come from environment variables and profile files,
never from code.

**What to learn:**

- `application.yml`, environment variables, and how Spring Boot decides which value wins
- Typed settings with `@ConfigurationProperties`, validated at start-up, so the app refuses to start with a bad
  value
- Profiles for local and test settings, and keeping secrets out of the repository

**Resources:**
[Externalized configuration](https://docs.spring.io/spring-boot/reference/features/external-config.html), Spring Boot
documentation

**Level:** Practitioner · Core

## Spring AI

Spring AI adds a common way to call language models, run tools and work with embeddings. Learn it when a project adds
AI features.

**What to learn:**

- Calling a model with Spring AI's client, with API keys in configuration
- Techversant's rules for AI features in client applications

**Resources:**

- [Spring AI](https://docs.spring.io/spring-ai/reference/)
- [LLM application security](../../../../security/audit/security-audit-reference.md#142-llm-application-security),
  in the Techversant security audit reference

**Level:** Advanced · Optional

## Project: Start the API

**Brief:** Create a Spring Boot 4 project for your RealWorld API, and add the first endpoint, `GET /api/tags`,
returning `{"tags": []}` for now.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] The project builds with the Maven wrapper on Java 25 and a supported Spring Boot 4 release, and serves its
  endpoints under `/api`
- [ ] `GET /api/tags` returns status 200 and `{"tags": []}`
- [ ] An unknown path under `/api` returns a JSON 404, not an HTML error page
- [ ] A filter adds a request ID to every response header and log line, and has a test
- [ ] Settings are bound to validated `@ConfigurationProperties` classes, and no secret is in the repository
- [ ] The formatter, Checkstyle, and SpotBugs or Error Prone run in the build with no errors
- [ ] The README explains how to build, run and test the project

Previous: [01. Language Fundamentals](./01-language-fundamentals.md) · Next:
[03. HTTP and REST APIs](./03-http-and-rest-apis.md)
