# 08. Testing

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Tests let you change an API without fear of breaking the clients that depend on it. Laravel has tools for testing a
whole request against a real database, and the tests run fast. Back to the [roadmap](./README.md).

## Feature tests

A feature test sends a request to your app and checks the response, the database and anything sent, without a
browser or a running server.

**What to learn:**

- Writing tests with Pest or PHPUnit, and making requests with `getJson`, `postJson` and `actingAs`
- Checking the status, the JSON shape with `assertJsonPath` and `assertJsonStructure`, and the database
- Testing the failure cases as carefully as the success cases: 401, 403, 404, 409 and 422

**Resources:**

- [HTTP tests](https://laravel.com/docs/13.x/http-tests), Laravel documentation
- [Pest documentation](https://pestphp.com/docs/installation)

**Level:** Practitioner · Core

## Database testing

Each test needs a known starting state. Laravel resets the database between tests, and factories create exactly the
records a test needs.

**What to learn:**

- The `RefreshDatabase` trait, and running tests against the same database engine as production
- Creating records with factories, and keeping each test independent of the others

**Resources:** [Database testing](https://laravel.com/docs/13.x/database-testing), Laravel documentation

**Level:** Practitioner · Core

## Fakes and mocks

Tests should not send real email or call real external services. Laravel's fakes record what would have happened, so
you can check it.

**What to learn:**

- `Queue::fake()`, `Mail::fake()`, `Notification::fake()` and `Event::fake()`
- `Http::fake()` for calls to other services, and failing the test if an unexpected call is made
- When a fake is better than a mock, and the risk of mocking code you own

**Resources:** [Mocking](https://laravel.com/docs/13.x/mocking), Laravel documentation

**Level:** Practitioner · Core

## Contract tests and static analysis

Your own tests check what you thought of. The RealWorld API tests check the contract, and static analysis checks the
types across the whole codebase.

**What to learn:**

- Running the RealWorld Hurl tests in continuous integration against a fresh database
- Larastan, the PHPStan extension that understands Laravel, at level 8 or higher
- Code coverage, and Techversant's minimum of 80%

**Resources:**

- [Running the API tests](../practice-app.md#running-the-api-tests), on the back-end practice app page
- [Testing and quality assurance](../../../../standards/php/php-best-practices.md#11-testing--quality-assurance), in the
  Techversant PHP best practices
- [Test levels](../../../00-engineering-foundations/07-testing-and-refactoring.md#test-levels), in Engineering
  Foundations

**Level:** Practitioner · Core

## Mutation testing

Mutation testing changes your code in small ways and checks that a test fails each time. It shows which tests would
miss a real bug.

**What to learn:**

- Running Infection on a critical module, such as the policies, and reading the score

**Resources:** [Infection](https://infection.github.io/guide/)

**Level:** Advanced · Optional

## Project: Pass the Full Test Suite

**Brief:** Get every RealWorld API test passing, add your own feature tests for every endpoint, and run everything in
continuous integration on each pull request.

**Size:** 3–4 days

**Verification**, checked by a reviewer:

- [ ] All 13 RealWorld Hurl files pass against a fresh database in continuous integration, and the pull request
  shows the result
- [ ] Every endpoint has feature tests for success and for each error case it can return
- [ ] Policy tests show that users cannot change other users' articles and comments
- [ ] Line coverage is at least 80%
- [ ] Larastan at level 8 reports no errors, with no new entries in an ignore list or baseline
- [ ] Continuous integration runs the code style check, Larastan, the feature tests and the Hurl tests on every
  pull request, and a failure blocks the merge

Previous: [07. Background Jobs and Caching](./07-background-jobs-and-caching.md) · Next:
[09. Security and Performance](./09-security-and-performance.md)
