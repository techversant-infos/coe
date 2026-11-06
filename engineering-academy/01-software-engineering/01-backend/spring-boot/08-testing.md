# 08. Testing

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Tests let you change an API without fear of breaking the clients that depend on it. Spring Boot has test support for
every layer, from a single class to the whole application against real services in containers. Back to the
[roadmap](./README.md).

## Unit tests

Unit tests check services and other business code on their own, quickly and without Spring.

**What to learn:**

- JUnit, AssertJ assertions, and naming tests by the behaviour they check
- Test doubles with Mockito, and when a hand-written fake is clearer
- Testing the failure cases as carefully as the success cases

**Resources:** [JUnit user guide](https://docs.junit.org/current/user-guide/)

**Level:** Practitioner · Core

## Web layer tests

Web layer tests send requests to your controllers and check the responses, including the status, the JSON body and
the security rules.

**What to learn:**

- `@WebMvcTest` with `MockMvc`, or `RestTestClient` for a running application, and the test starters for each
  module, such as `spring-boot-starter-webmvc-test`
- `@MockitoBean`, which replaces `@MockBean`, removed in Spring Boot 4
- Testing secured endpoints, with and without a signed-in user
- Checking 401, 403, 404, 409 and 422 responses and their bodies

**Resources:**
[Testing Spring Boot applications](https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html),
Spring Boot documentation

**Level:** Practitioner · Core

## Integration tests with Testcontainers

Mocks cannot show that your queries, migrations and messages work. Testcontainers starts real PostgreSQL, Redis and
RabbitMQ in containers for the test run.

**What to learn:**

- `@SpringBootTest` with Testcontainers, and `@ServiceConnection` to connect Spring to each container
- Running Flyway migrations before the tests, and keeping tests independent of each other
- Using the same database engine and version as production

**Resources:**
[Testcontainers](https://docs.spring.io/spring-boot/reference/testing/testcontainers.html), Spring Boot
documentation

**Level:** Practitioner · Core

## Contract tests and static analysis

Your own tests check what you thought of. The RealWorld API tests check the contract, and static analysis checks the
whole codebase.

**What to learn:**

- Running the RealWorld Hurl tests in continuous integration against a fresh database
- Measuring coverage with JaCoCo, and reading it to find untested behaviour
- Running SpotBugs or Error Prone in the build, with no new warnings allowed

**Resources:**

- [Running the API tests](../practice-app.md#running-the-api-tests), on the back-end practice app page
- [Test levels](../../../00-engineering-foundations/07-testing-and-refactoring.md#test-levels), in Engineering
  Foundations

**Level:** Practitioner · Core

## Mutation testing

Mutation testing changes your code in small ways and checks that a test fails each time. It shows which tests would
miss a real bug.

**What to learn:**

- Running PIT on a critical package, such as the authorization rules, and reading the report

**Resources:** [PIT](https://pitest.org/)

**Level:** Advanced · Optional

## Project: Pass the Full Test Suite

**Brief:** Keep every RealWorld API test passing, add your own unit, web layer and integration tests, and run
everything in continuous integration on each pull request.

**Size:** 3–4 days

**Verification**, checked by a reviewer:

- [ ] All 13 RealWorld Hurl files pass against a fresh database in continuous integration, and the pull request
  shows the result
- [ ] Services have unit tests, covering success and each exception they can throw
- [ ] Every endpoint has web layer tests for success and for each error status it can return
- [ ] Integration tests run against PostgreSQL, Redis and RabbitMQ started by Testcontainers
- [ ] Authorization tests show that users cannot change other users' articles and comments
- [ ] The JaCoCo report is in the pull request, and every gap in the services is explained
- [ ] Continuous integration runs the formatter check, static analysis, the tests and the Hurl tests on every pull
  request, and a failure blocks the merge

Previous: [07. Background Jobs and Caching](./07-background-jobs-and-caching.md) · Next:
[09. Security and Performance](./09-security-and-performance.md)
