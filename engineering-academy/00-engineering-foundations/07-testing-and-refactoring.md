# 07. Testing and Refactoring

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Tests prove that your change works and keeps working. With good tests in place, you can improve code safely through
refactoring. Back to the [roadmap](./README.md).

## Test levels

Different tests answer different questions. Unit tests are fast and pinpoint failures; end-to-end tests are slow
but prove the whole flow works.

**What to learn:**

- Unit, integration and end-to-end tests, and what each one is good for
- The test pyramid: many fast unit tests, fewer integration tests and a few end-to-end tests
- Choosing the cheapest test that would catch the bug you are worried about

**Resources:**

- [The practical test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html), Ham Vocke

**In your stack:** for example Jest or Vitest for JavaScript and TypeScript, PHPUnit or Pest for PHP, JUnit for
Kotlin and XCTest for Swift. RealWorld's Playwright suite is an example of end-to-end tests.

**Level:** Practitioner · Core

## Writing clear tests

A good test reads like a short specification: what is set up, what happens and what should be true. When it fails,
the name tells you what broke.

**What to learn:**

- Arrange, act, assert: set up, do one thing, check the result
- Naming tests after the behaviour, such as "returns 404 when the article does not exist"
- Proving a test can fail: break the code on purpose and watch the test go red

**Resources:**

- [Test ownership](../../standards/general/ai-era-coding-guidelines.md#61-test-ownership), in the Techversant AI Era
  Coding Guidelines, on why AI-written tests are placeholders until you verify them

**Level:** Practitioner · Core

## Testable code

Code is hard to test when it creates its own dependencies, reads the clock directly or hides logic in the user
interface. The design principles from stage 04 make code testable.

**What to learn:**

- Injecting dependencies so tests can replace them
- Keeping business rules in plain functions or classes, away from the framework
- Handling time, randomness and external calls through interfaces you can control in tests

**Resources:** *Working Effectively with Legacy Code*, Michael Feathers

**In your stack:** in a front end, test components through what the user sees, for example with Testing Library.
In mobile, keep logic in view models you can test without a device.

**Level:** Practitioner · Core

## Code smells

A code smell is a sign that a design problem may be hiding, such as a very long function, a class that knows too
much or the same change needed in many places.

**What to learn:**

- Common smells: long function, large class, long parameter list, duplicated code and feature envy
- Treating a smell as a reason to look closer, not proof of a problem
- Matching each smell to the refactoring that fixes it

**Resources:** *Refactoring*, Martin Fowler, the chapter on bad smells in code

**Level:** Practitioner · Core

## Safe refactoring

Refactoring changes the structure of code without changing what it does. Done in small steps with tests passing
after each one, it is safe.

**What to learn:**

- Taking small steps, such as extract function, rename and move, and running the tests after each
- Never mixing a refactoring with a behaviour change in the same commit
- Adding tests before you refactor code that has none

**Resources:**

- [Refactoring catalog](https://refactoring.com/catalog/), Martin Fowler

**Level:** Practitioner · Core

## Project: Test the Feature and Refactor One Smell

**Brief:** Write tests for your bookmarks feature at the right levels. Then find one code smell elsewhere in the
practice app and remove it with a named refactoring, in small steps.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Unit tests cover the bookmark rules, and integration tests cover the endpoints, including the error cases.
  Front-end engineers using a mock API test the bookmark button and list instead, including error responses
- [ ] Test names describe behaviour, and each test follows arrange, act, assert
- [ ] For one test, the PR description includes the failing output after you broke the code on purpose
- [ ] A test proves a reader cannot see another reader's bookmarks
- [ ] The PR names the smell as in chapter 3 of *Refactoring*, and the refactoring as in Fowler's catalog
- [ ] The refactoring is in separate commits from any behaviour change, and the tests pass after each commit
- [ ] The RealWorld API tests, and the end-to-end tests if you work on a front end, still pass

Previous: [06. APIs and Boundaries](./06-apis-and-boundaries.md) · Next:
[08. Secure Engineering](./08-secure-engineering.md)
