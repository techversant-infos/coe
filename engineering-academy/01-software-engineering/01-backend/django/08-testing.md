# 08. Testing

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Tests let you change an API without fear of breaking the clients that depend on it. Django and DRF have tools for
testing a whole request against a real database, and pytest keeps the tests short. Back to the
[roadmap](./README.md).

## API tests with pytest

An API test sends a request to your app and checks the response and the database, without a browser or a running
server.

**What to learn:**

- pytest and pytest-django, fixtures, the `django_db` mark and the `db` fixture
- DRF's `APIClient`, signing in with `force_authenticate`, and checking the status and JSON body
- Testing the failure cases as carefully as the success cases: 401, 403, 404, 409 and 422

**Resources:**

- [pytest-django](https://pytest-django.readthedocs.io/en/latest/)
- [Testing](https://www.django-rest-framework.org/api-guide/testing/), DRF documentation

**Level:** Practitioner · Core

## Test data and the database

Each test needs a known starting state. pytest-django gives each test a clean database, and factories create exactly
the records a test needs.

**What to learn:**

- Using factory_boy in tests, and keeping each test independent of the others
- Running tests against PostgreSQL, the same engine as production, not SQLite
- The `django_assert_num_queries` fixture, to keep N+1 queries from coming back

**Resources:** [Testing tools](https://docs.djangoproject.com/en/6.1/topics/testing/tools/), Django documentation

**Level:** Practitioner · Core

## Mocks and external services

Tests should not send real email or call real external services.

**What to learn:**

- Django's in-memory email backend in tests, and Celery's eager mode or mocking `delay`
- The `django_capture_on_commit_callbacks` fixture, because test transactions never commit, so `on_commit`
  callbacks do not run on their own
- `unittest.mock` for calls to other services, and failing the test if an unexpected call is made
- The risk of mocking code you own

**Resources:**
[unittest.mock](https://docs.python.org/3/library/unittest.mock.html), Python documentation

**Level:** Practitioner · Core

## Contract tests and type checks

Your own tests check what you thought of. The RealWorld API tests check the contract, and the type checker checks
every file.

**What to learn:**

- Running the RealWorld Hurl tests in continuous integration against a fresh database
- mypy with the django-stubs and djangorestframework-stubs plugins
- Measuring coverage with coverage.py, and reading it to find untested behaviour

**Resources:**

- [Running the API tests](../practice-app.md#running-the-api-tests), on the back-end practice app page
- [django-stubs](https://github.com/typeddjango/django-stubs)
- [Test levels](../../../00-engineering-foundations/07-testing-and-refactoring.md#test-levels), in Engineering
  Foundations

**Level:** Practitioner · Core

## Mutation testing

Mutation testing changes your code in small ways and checks that a test fails each time. It shows which tests would
miss a real bug.

**What to learn:**

- Running mutmut on a critical module, such as the permission classes, and reading the results

**Resources:** [mutmut](https://mutmut.readthedocs.io/en/latest/)

**Level:** Advanced · Optional

## Project: Pass the Full Test Suite

**Brief:** Keep every RealWorld API test passing, add your own tests for every endpoint, and run everything in
continuous integration on each pull request.

**Size:** 3–4 days

**Verification**, checked by a reviewer:

- [ ] All 13 RealWorld Hurl files pass against a fresh database in continuous integration, and the pull request
  shows the result
- [ ] Every endpoint has tests for success and for each error status it can return, run against PostgreSQL
- [ ] Permission tests show that users cannot change other users' articles and comments
- [ ] Query count tests cover the article list and feed
- [ ] The coverage report is in the pull request, and every gap is explained
- [ ] mypy with the Django plugins reports no errors
- [ ] Continuous integration runs Ruff, mypy, the tests and the Hurl tests on every pull request, and a failure
  blocks the merge

Previous: [07. Background Jobs and Caching](./07-background-jobs-and-caching.md) · Next:
[09. Security and Performance](./09-security-and-performance.md)
