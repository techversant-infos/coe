# 08. Testing

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Tests let you change an API without fear of breaking the clients that depend on it. Techversant Node.js services
use many fast unit tests, fewer integration tests against a real database, and a small number of end-to-end tests.
Back to the [roadmap](./README.md).

## Unit tests with Vitest

Unit tests check services and other business code on their own, with in-memory fakes in place of the database and
other systems.

**What to learn:**

- Writing tests with Vitest, and naming them by the behaviour they check
- Passing in fakes for repositories, the clock and ID generators, so tests are fast and repeatable
- Testing the failure cases as carefully as the success cases

**Resources:**

- [Vitest guide](https://vitest.dev/guide/)
- [Testing](../../../../standards/nodejs/nodejs-typescript-style-guide.md#14-testing), in the Techversant Node.js and
  TypeScript style guide

**Level:** Practitioner · Core

## HTTP tests

HTTP tests send a request to the app and check the response. Fastify's `inject` runs a request without opening a
port, and Supertest does the same for a running server.

**What to learn:**

- Building the app in a function, so each test can create its own instance
- Checking the status, the JSON body and the headers, including 401, 403, 404, 409 and 422 responses
- Signing in once per test, through the API or with a test token

**Resources:**

- [Testing](https://fastify.dev/docs/latest/Guides/Testing/), Fastify documentation
- [Supertest](https://github.com/forwardemail/supertest)

**Level:** Practitioner · Core

## Integration tests with a real database

Mocks cannot show that your queries and migrations work. Integration tests run against a real database in a
container, created fresh for the test run.

**What to learn:**

- Starting a database for tests with Testcontainers, and running migrations before the tests
- Keeping tests independent, for example with a clean database or a transaction per test
- Running the same database engine and version as production

**Resources:**

- [Testcontainers for Node.js](https://node.testcontainers.org/)
- [Testing strategy](../../../../standards/nodejs/nodejs-typescript-best-practices.md#testing-strategy), in the
  Techversant Node.js and TypeScript best practices

**Level:** Practitioner · Core

## Contract tests and type checks

Your own tests check what you thought of. The RealWorld API tests check the contract, and the type checker checks
every file.

**What to learn:**

- Running the RealWorld Hurl tests in continuous integration against a fresh database
- Running `tsc --noEmit`, or your project's type check, as its own step
- Measuring code coverage with Vitest, and reading it to find untested behaviour

**Resources:**

- [Running the API tests](../practice-app.md#running-the-api-tests), on the back-end practice app page
- [Test levels](../../../00-engineering-foundations/07-testing-and-refactoring.md#test-levels), in Engineering
  Foundations

**Level:** Practitioner · Core

## Mutation testing

Mutation testing changes your code in small ways and checks that a test fails each time. It shows which tests would
miss a real bug.

**What to learn:**

- Running Stryker on a critical module, such as the authorization checks, and reading the score

**Resources:** [StrykerJS](https://stryker-mutator.io/docs/stryker-js/introduction/)

**Level:** Advanced · Optional

## Project: Pass the Full Test Suite

**Brief:** Keep every RealWorld API test passing, add your own unit, HTTP and integration tests, and run everything in
continuous integration on each pull request.

**Size:** 3–4 days

**Verification**, checked by a reviewer:

- [ ] All 13 RealWorld Hurl files pass against a fresh database in continuous integration, and the pull request
  shows the result
- [ ] Services have unit tests with in-memory fakes, covering success and each error they can raise
- [ ] Every endpoint has HTTP tests for success and for each error status it can return
- [ ] Integration tests run the repositories against a real database started by Testcontainers
- [ ] Authorization tests show that users cannot change other users' articles and comments
- [ ] The coverage report is in the pull request, and every gap in the services is explained
- [ ] Continuous integration runs the type check, ESLint, the tests and the Hurl tests on every pull request, and a
  failure blocks the merge

Previous: [07. Background Jobs and Caching](./07-background-jobs-and-caching.md) · Next:
[09. Security and Performance](./09-security-and-performance.md)
