# 03. Clean Code

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Much review friction, and many bugs, come from code that is hard to read rather than code that is wrong. Clean code
lets another developer understand your work without asking you. Back to the [roadmap](./README.md).

## Naming

A good name says what something holds or does, so the reader does not have to work it out.

**What to learn:**

- Variables as nouns without abbreviations or type prefixes: `customerName`, not `custNm` or `strCustName`
- Functions as verbs with one intent: `calculateTotal`, not `processStuff`
- Named constants instead of magic numbers: `MAX_LOGIN_ATTEMPTS`, not `5`

**Resources:**

- Techversant style guides: [Node.js and TypeScript](../../standards/nodejs/nodejs-typescript-style-guide.md),
  [PHP](../../standards/php/php-coding-standards.md) and
  [ColdFusion](../../standards/coldfusion/coldfusion-style-guide.md)
- *Clean Code*, Robert C. Martin, the chapter on meaningful names

**In your stack:** in React or Vue, name components after what they show (`ArticleList`) and event handlers after
the event (`handleSubmit`). In mobile code, follow the platform's conventions, such as Kotlin and Swift naming
guidelines.

**Level:** Foundation · Core

## Small functions

A function that does one thing is easy to name, test and change. A function that does three things hides bugs
between them.

**What to learn:**

- One function, one job: if you need "and" to describe it, split it
- Keeping functions short enough to read without scrolling
- Few parameters; group related ones into an object

**Resources:** *Clean Code*, Robert C. Martin, the chapter on functions

**In your stack:** in a back end, keep controllers thin and move logic into services. In a front end, split large
components into smaller ones. In mobile, keep view code free of business logic.

**Level:** Foundation · Core

## Control flow

Deep nesting makes the reader track many conditions at once. Flat code with early exits is easier to follow and
change.

**What to learn:**

- Guard clauses: handle the exceptional case first and return early
- Keeping the main path at the lowest indentation level
- Treating three levels of nesting as a sign to refactor

**Resources:**

- [Replace nested conditional with guard clauses](https://refactoring.com/catalog/replaceNestedConditionalWithGuardClauses.html),
  in Martin Fowler's refactoring catalog

**Level:** Foundation · Core

## Duplication

Repeated code means a fix must be made in several places. But merging code that only looks alike creates the wrong
abstraction, which is harder to undo than duplication.

**What to learn:**

- Don't Repeat Yourself (DRY): every piece of knowledge should have one clear home
- The rule of three: tolerate a second copy, and extract on the third, once you can see what really is shared
- Spotting the wrong abstraction: a shared helper full of flags and special cases for each caller

**Resources:**

- [The wrong abstraction](https://sandimetz.com/blog/2016/1/20/the-wrong-abstraction), Sandi Metz
- *The Pragmatic Programmer*, Andrew Hunt and David Thomas, on DRY

**Level:** Foundation · Core

## Error handling and logging

Good error handling makes failures quick to find and fix. Users see a helpful message; developers see enough
context to debug, and never a secret.

**What to learn:**

- Failing fast, close to the cause, instead of letting bad data travel through the system
- Separating expected failures, such as invalid input, from exceptional ones, such as a lost database connection
- Logging the operation, an identifier and the time, and never passwords, tokens or personal data

**Resources:**

- [What must be logged](../../security/audit/security-audit-reference.md#111-what-must-be-logged) and
  [what must never be logged](../../security/audit/security-audit-reference.md#112-what-must-never-be-logged), in the
  Techversant security audit reference
- [Error response format](../../standards/general/rest-api-best-practices.md#52-error-response-format), in the
  Techversant REST API standard

**In your stack:** in a front end, show a clear message and keep the user's input when a request fails. In mobile,
handle lost connections without crashing. In a back end, return the standard error response and log the details
on the server.

**Level:** Foundation · Core

## Formatters and linters

Formatting arguments waste review time. Let tools enforce formatting and catch common mistakes, so reviews focus on
what the code does.

**What to learn:**

- Running the project's formatter on save, and its linter before every commit
- Fixing lint warnings instead of hiding them
- Keeping `.editorconfig` and tool settings in the repository

**Resources:**

- [Core principles](../../standards/git/git-workflow.md#️-core-principles), in the Techversant Git workflow, on
  `.editorconfig`
- [Node.js and TypeScript style guide](../../standards/nodejs/nodejs-typescript-style-guide.md), Techversant

**In your stack:** for example Prettier and ESLint for JavaScript and TypeScript, PHP-CS-Fixer or Pint for PHP,
ktlint for Kotlin and SwiftLint for Swift.

**Level:** Foundation · Core

## Project: Clean Up One Module

**Brief:** Choose one module of the practice app that is hard to read, agreed with your reviewer. Clean it up
without changing what it does: rename, split functions, flatten nesting, remove real duplication and improve error
handling.

**Size:** 2 days

**Verification**, checked by a reviewer:

- [ ] The formatter and linter run with no errors on the changed files
- [ ] Every renamed variable and function says what it holds or does, with no abbreviations or type prefixes
- [ ] No function in the module is nested more than two levels deep, or does more than one job
- [ ] Magic numbers and strings are replaced with named constants
- [ ] At least one error path fails fast and logs useful context, with no secrets or personal data in the log
- [ ] The PR description lists each change and why, and notes any duplication you chose to keep
- [ ] The API tests pass before and after, with the same results

Previous: [02. Working with AI Tools](./02-working-with-ai-tools.md) · Next:
[04. Design Principles](./04-design-principles.md)
