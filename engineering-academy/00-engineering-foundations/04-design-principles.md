# 04. Design Principles

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Working code is the start. Well-designed code is easy to test, change and reuse, because each part has one job and
depends on as little as possible. Back to the [roadmap](./README.md).

## SOLID

SOLID is five principles for object-oriented design. They help you notice code that will be hard to change.

**What to learn:**

- Single responsibility: a class has one reason to change
- Open-closed: add behaviour by adding code, not by editing working code
- Liskov substitution: a subtype must work wherever its parent type is expected, without surprising the caller
- Interface segregation: small, focused interfaces instead of one large one
- Dependency inversion: depend on abstractions, not on concrete details such as a specific database

**Resources:**

- *Clean Architecture*, Robert C. Martin, the part on design principles
- [SOLID](https://en.wikipedia.org/wiki/SOLID), for a short overview with links to each principle

**In your stack:** the principles apply beyond classes. In a front end, a component with one responsibility is
easier to reuse. In mobile, a view model that does one job is easier to test.

**Level:** Practitioner · Core

## Separation of concerns

Keep different kinds of work in different places: presentation, business rules and data access. A change to one
should not ripple into the others.

**What to learn:**

- Layers such as controller, service and repository, and what belongs in each
- Spotting a "fat" controller or component that does everything
- Keeping business rules free of framework and database details

**Resources:** *Clean Architecture*, Robert C. Martin

**In your stack:** in a back end, controllers handle HTTP, services hold rules and repositories talk to the
database. In a front end, separate data fetching from display. In mobile, follow the platform's recommended
architecture, such as a view model between the view and the data.

**Level:** Practitioner · Core

## Dependency injection

Instead of a class creating the things it needs, they are passed in. You can then swap a real database for a test
double, or one email provider for another.

**What to learn:**

- Passing dependencies through the constructor
- Using your framework's dependency injection container where it has one
- Replacing a dependency with a stub or fake in a unit test

**Resources:**

- [Inversion of control containers and the dependency injection pattern](https://martinfowler.com/articles/injection.html),
  Martin Fowler

**In your stack:** for example NestJS providers, Laravel's service container, Spring, or Hilt on Android. In
React, pass dependencies as props or through context.

**Level:** Practitioner · Core

## Composition over inheritance

Inheritance ties a class tightly to its parent. Building behaviour from small parts that work together is usually
more flexible.

**What to learn:**

- "Is-a" and "has-a": use inheritance only when a subtype really is a kind of its parent in every way
- Building behaviour by combining small objects or functions
- Recognizing deep inheritance trees as a warning sign

**Resources:**

- *Design Patterns*, Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides, which first set out the principle
  "favour object composition over class inheritance"

**In your stack:** React and modern mobile UI frameworks such as Jetpack Compose and SwiftUI build screens by
composing small components, not by inheriting from them.

**Level:** Practitioner · Core

## Configuration and feature flags

Settings that change between environments, and features that are not ready yet, should not be hard-coded. Keep them
in configuration and behind flags.

**What to learn:**

- Reading settings from environment variables or configuration files, never hard-coding them
- Keeping secrets out of the repository
- Merging unfinished work behind a feature flag instead of keeping a long-lived branch

**Resources:**

- [Core principles](../../standards/git/git-workflow.md#️-core-principles), in the Techversant Git workflow, on
  feature flags
- [The Twelve-Factor App: config](https://12factor.net/config)

**Level:** Practitioner · Core

## Project: Extract a Service and Inject Its Dependencies

**Brief:** Find the place in the practice app where a controller, route handler or component does too much, such
as validating, applying rules and querying the database in one function. Move the business rules into a service,
pass its data access in as a dependency, and unit test the service with a stub in place of the database.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] The controller or handler now only deals with requests and responses, and calls the service
- [ ] The service receives its data access through the constructor or the framework's injection, and does not
  create it
- [ ] At least three unit tests cover the service, using a stub or fake for data access, and run without a database
- [ ] One hard-coded setting is moved to configuration
- [ ] The PR description names the principle behind each change, such as single responsibility or dependency
  inversion
- [ ] The API tests pass before and after, with the same results

Previous: [03. Clean Code](./03-clean-code.md) · Next: [05. Design Thinking](./05-design-thinking.md)
