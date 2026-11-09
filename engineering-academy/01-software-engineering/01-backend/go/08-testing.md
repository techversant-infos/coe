# 08. Testing

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Tests let you change an API without fear of breaking the clients that depend on it. Go has testing built in: the
`testing` package and `go test` cover unit tests, handler tests, benchmarks and fuzzing. Back to the
[roadmap](./README.md).

## Unit tests

Unit tests check services and other business code on their own, quickly and without a database.

**What to learn:**

- The `testing` package, table-driven tests and subtests with `t.Run`, and naming tests by the behaviour they check
- Fakes that satisfy a small interface, instead of a mocking library, and when a mock is still useful
- Testing the failure cases as carefully as the success cases

**Resources:**

- [Package testing](https://pkg.go.dev/testing), Go documentation
- [Table-driven tests](https://go.dev/wiki/TableDrivenTests), Go wiki

**Level:** Practitioner · Core

## Handler tests

Handler tests send requests to your handlers and check the responses, including the status, the JSON body and the
middleware.

**What to learn:**

- `httptest.NewRecorder` for one handler, and `httptest.NewServer` for the whole router with its middleware
- Testing secured endpoints, with and without a valid token
- Checking 401, 403, 404, 409 and 422 responses and their bodies

**Resources:** [Package httptest](https://pkg.go.dev/net/http/httptest), Go documentation

**Level:** Practitioner · Core

## Integration tests with Testcontainers

Fakes cannot show that your queries, migrations and jobs work. Testcontainers starts real PostgreSQL and Redis servers
in containers for the test run.

**What to learn:**

- testcontainers-go and its PostgreSQL and Redis modules, started once in `TestMain`
- Running goose migrations before the tests, and keeping tests independent of each other
- Using the same database engine and version as production

**Resources:** [PostgreSQL module](https://golang.testcontainers.org/modules/postgres/), Testcontainers for Go

**Level:** Practitioner · Core

## Contract tests and static analysis

Your own tests check what you thought of. The RealWorld API tests check the contract, and static analysis checks the
whole codebase.

**What to learn:**

- Running the RealWorld Hurl tests in continuous integration against a fresh database
- Running every test with `go test -race`, and reading a coverage profile to find untested behaviour
- Running golangci-lint in the build, with no new problems allowed

**Resources:**

- [Running the API tests](../practice-app.md#running-the-api-tests), on the back-end practice app page
- [Test levels](../../../00-engineering-foundations/07-testing-and-refactoring.md#test-levels), in Engineering
  Foundations

**Level:** Practitioner · Core

## Fuzz testing

Fuzz testing feeds a function many generated inputs and reports any that make it fail. Go runs fuzz tests with
`go test`.

**What to learn:**

- Writing a fuzz test for the slug library or the JSON request decoding, and adding failing inputs to the test data

**Resources:** [Getting started with fuzzing](https://go.dev/doc/tutorial/fuzz), go.dev

**Level:** Advanced · Optional

## Project: Pass the Full Test Suite

**Brief:** Keep every RealWorld API test passing, add your own unit, handler and integration tests, and run
everything in continuous integration on each pull request.

**Size:** 3–4 days

**Verification**, checked by a reviewer:

- [ ] All 13 RealWorld Hurl files pass against a fresh database in continuous integration, and the pull request
  shows the result
- [ ] Services have unit tests, covering success and each error they return
- [ ] Every endpoint has handler tests for success and for each error status it can return
- [ ] Integration tests run against PostgreSQL and Redis started by Testcontainers
- [ ] Authorization tests show that users cannot change other users' articles and comments
- [ ] Every test passes with `go test -race`, the coverage report is in the pull request, and every gap in the
  services is explained
- [ ] Continuous integration runs `gofmt`, golangci-lint, the tests and the Hurl tests on every pull request, and a
  failure blocks the merge

Previous: [07. Background Jobs and Caching](./07-background-jobs-and-caching.md) · Next:
[09. Security and Performance](./09-security-and-performance.md)
