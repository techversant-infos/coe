# 02. JavaScript and TypeScript

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

React is JavaScript, and Techversant writes it in TypeScript. Solid language skills make every later stage easier,
and types catch many mistakes before the code runs. Back to the [roadmap](./README.md).

## Modern JavaScript

Most React code uses a small set of modern JavaScript features again and again.

**What to learn:**

- `const` and `let`, arrow functions, and template literals
- Destructuring, the spread operator, and optional chaining (`?.`)
- Array methods such as `map`, `filter` and `find`, which return new arrays instead of changing the old one

**Resources:**
[JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide), MDN

**Level:** Practitioner · Core

## Asynchronous JavaScript

Calls to an API take time. Promises and `async`/`await` let the page keep working while it waits.

**What to learn:**

- Promises, and writing `async` functions with `await`
- Handling errors with `try`/`catch`, including network failures
- Calling an API with `fetch`, and checking the response status before reading the body

**Resources:**

- [Asynchronous JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Async_JS), MDN
- [Using the Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch), MDN

**Level:** Practitioner · Core

## TypeScript essentials

TypeScript adds types to JavaScript. The editor warns you when you pass the wrong data, and the code documents what
each function expects.

**What to learn:**

- Typing variables, function parameters and return values, and objects with `type` and `interface`
- Union types, narrowing, and avoiding `any`
- Strict mode, which Techversant projects turn on

**Resources:**

- [TypeScript handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [Node.js and TypeScript style guide](../../../../standards/nodejs/nodejs-typescript-style-guide.md), Techversant

**Level:** Practitioner · Core

## Packages and build tools

Front-end projects install packages with npm and bundle code with a build tool. Vite is a common choice for React
apps that do not use a framework such as Next.js.

**What to learn:**

- `package.json`, installing packages, and why the lock file is committed
- Running scripts such as `dev`, `build` and `test`
- Starting a React and TypeScript project with Vite, and adding Vitest to run unit tests

**Resources:**

- [Getting started with Vite](https://vite.dev/guide/) and [Vitest](https://vitest.dev/guide/)
- [About npm](https://docs.npmjs.com/about-npm)

**Level:** Practitioner · Core

## Linting and formatting

A linter catches likely bugs, and a formatter keeps the code style consistent, so reviews can focus on what the code
does.

**What to learn:**

- Running ESLint and Prettier in the editor and before every commit
- Lint rules for React, such as the rules of hooks

**Resources:**

- [Formatters and linters](../../../00-engineering-foundations/03-clean-code.md#formatters-and-linters), in
  Engineering Foundations
- [ESLint documentation](https://eslint.org/docs/latest/)

**Level:** Practitioner · Core

## Project: Write a Typed API Client

**Brief:** Write a small TypeScript module that calls the RealWorld API: list articles, get one article by slug, and
list tags. Base the types on the API specification, `specs/api/openapi.yml` in the RealWorld repository. You use this
module in every later stage.

**Size:** 2 days

**Verification**, checked by a reviewer:

- [ ] The project builds with TypeScript strict mode and has no `any` types
- [ ] The types for articles, profiles and tags match the API specification
- [ ] Every function checks the response status, and returns or throws a typed error when the call fails
- [ ] Vitest unit tests cover a successful call and a failed call for each function, with `fetch` replaced by a
  test double
- [ ] ESLint and Prettier run with no errors
- [ ] The lock file is committed, and the README explains how to install, test and build

Previous: [01. HTML, CSS and Accessibility](./01-html-css-and-accessibility.md) · Next:
[03. Framework Fundamentals](./03-framework-fundamentals.md)
