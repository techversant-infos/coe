# 08. Testing

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Tests let you change an API without fear of breaking the clients that depend on it. ASP.NET Core can run the whole
app in memory for tests, and Testcontainers gives those tests a real database. Back to the [roadmap](./README.md).

## Unit tests

Unit tests check services and other business code on their own, quickly and without a database.

**What to learn:**

- xUnit facts (single tests) and theories (one test run with several inputs), and naming tests by the behaviour they
  check
- Test doubles with a library such as NSubstitute, and when a hand-written fake is clearer
- Testing the failure cases as carefully as the success cases

**Resources:** [xUnit.net](https://xunit.net/)

**Level:** Practitioner · Core

## Endpoint tests with WebApplicationFactory

`WebApplicationFactory` starts your whole app in memory, so tests send real HTTP requests through the middleware,
authentication and endpoints.

**What to learn:**

- Creating a test client from `WebApplicationFactory`, and replacing services for a test
- Testing secured endpoints, with and without a valid token
- Checking 401, 403, 404, 409 and 422 responses and their bodies

**Resources:**
[Integration tests](https://learn.microsoft.com/en-us/aspnet/core/test/integration-tests), Microsoft Learn

**Level:** Practitioner · Core

## Database tests with Testcontainers

Test doubles cannot show that your queries and migrations work, and the in-memory provider of Entity Framework Core (EF
Core) behaves differently from PostgreSQL. Testcontainers starts a real PostgreSQL server in a container for the test
run.

**What to learn:**

- Testcontainers for .NET and its PostgreSQL module, shared across the tests in a class or collection
- Applying migrations before the tests, and resetting data between tests, for example with Respawn, using its PostgreSQL
  adapter and leaving out the migrations history table and Hangfire's schema
- Using the same database engine and version as production

**Resources:** [PostgreSQL module](https://dotnet.testcontainers.org/modules/postgres/), Testcontainers for .NET

**Level:** Practitioner · Core

## Contract tests and static analysis

Your own tests check what you thought of. The RealWorld API tests check the contract, and static analysis checks the
whole codebase.

**What to learn:**

- Running the RealWorld Hurl tests in continuous integration against a fresh database
- Collecting code coverage, and reading it to find untested behaviour
- Building with the .NET analyzers and warnings as errors, with no new warnings allowed

**Resources:**

- [Running the API tests](../practice-app.md#running-the-api-tests), on the back-end practice app page
- [Test levels](../../../00-engineering-foundations/07-testing-and-refactoring.md#test-levels), in Engineering
  Foundations

**Level:** Practitioner · Core

## Mutation testing

Mutation testing changes your code in small ways and checks that a test fails each time. It shows which tests would
miss a real bug.

**What to learn:**

- Running Stryker.NET on a critical project, such as the authorization rules, and reading the report

**Resources:** [Stryker.NET](https://stryker-mutator.io/docs/stryker-net/introduction/)

**Level:** Advanced · Optional

## Project: Pass the Full Test Suite

**Brief:** Keep every RealWorld API test passing, add your own unit, endpoint and database tests, and run everything in
continuous integration on each pull request.

**Size:** 3–4 days

**Verification**, checked by a reviewer:

- [ ] All 13 RealWorld Hurl files pass against a fresh database in continuous integration, and the pull request
  shows the result
- [ ] Services have unit tests, covering success and each exception they can throw
- [ ] Every endpoint has endpoint tests for success and for each error status it can return
- [ ] Database tests run against PostgreSQL started by Testcontainers, not the in-memory provider
- [ ] Authorization tests show that users cannot change other users' articles and comments
- [ ] The coverage report is in the pull request, and every gap in the services is explained
- [ ] Continuous integration runs `dotnet format --verify-no-changes`, the build with warnings as errors, the tests
  and the Hurl tests on every pull request, and a failure blocks the merge

Previous: [07. Background Jobs and Caching](./07-background-jobs-and-caching.md) · Next:
[09. Security and Performance](./09-security-and-performance.md)
