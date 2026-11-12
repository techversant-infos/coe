# 02. JavaScript and TypeScript

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-11 · **Next review:** 2027-02-11

React Native apps are written in JavaScript, and Techversant writes them in TypeScript. Solid language skills make
every later stage easier, and types catch many mistakes before the app runs. Back to the [roadmap](./README.md).

## Modern JavaScript

Most React Native code uses a small set of modern JavaScript features again and again.

**What to learn:**

- `const` and `let`, arrow functions, and template literals
- Destructuring, the spread operator, and optional chaining (`?.`)
- Array methods such as `map`, `filter` and `find`, which return new arrays instead of changing the old one

**Resources:**
[JavaScript guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide), MDN

**Level:** Practitioner · Core

## Asynchronous JavaScript

Calls to an API take time, and on mobile they often fail. Promises and `async`/`await` let the app keep working
while it waits.

**What to learn:**

- Promises, and writing `async` functions with `await`
- Handling errors with `try`/`catch`, including network failures and timeouts
- Calling an API with `fetch`, and checking the response status before reading the body

**Resources:**

- [Asynchronous JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Async_JS), MDN
- [Networking](https://reactnative.dev/docs/network), React Native documentation

**Level:** Practitioner · Core

## TypeScript essentials

TypeScript adds types to JavaScript. The editor warns you when you pass the wrong data, and the code documents what
each function expects.

**What to learn:**

- Typing variables, function parameters and return values, and objects with `type` and `interface`
- Union types, narrowing, and avoiding `any`
- Strict mode, which Techversant projects turn on, and how Expo projects set up TypeScript

**Resources:**

- [TypeScript handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [Using TypeScript](https://docs.expo.dev/guides/typescript/), Expo documentation
- [Node.js and TypeScript style guide](../../../../standards/nodejs/nodejs-typescript-style-guide.md), Techversant

**Level:** Practitioner · Core

## Packages and tools

Mobile projects install packages with npm, like web projects, but some packages include native code for iOS and
Android. Those need a new build of the app, not only a reload.

**What to learn:**

- `package.json`, installing packages, and why the lock file is committed
- Installing packages with `npx expo install`, which picks versions that match your Expo software development kit (SDK)
  version
- The difference between a package that is only JavaScript and one that includes native code

**Resources:** [Expo workflow overview](https://docs.expo.dev/workflow/overview/), Expo documentation

**Level:** Practitioner · Core

## Linting and formatting

A linter catches likely bugs, and a formatter keeps the code style consistent, so reviews can focus on what the code
does.

**What to learn:**

- Running ESLint and Prettier in the editor and before every commit
- Expo's ESLint configuration, including the rules of hooks

**Resources:**

- [Formatters and linters](../../../00-engineering-foundations/03-clean-code.md#formatters-and-linters), in
  Engineering Foundations
- [Using ESLint and Prettier](https://docs.expo.dev/guides/using-eslint/), Expo documentation

**Level:** Practitioner · Core

## Project: Write a Typed API Client

**Brief:** Write a small TypeScript module that calls the RealWorld API: list articles, get one article by slug, and
list tags. Base the types on the API specification, `specs/api/openapi.yml` in the RealWorld repository. You use this
module in every later stage, so keep it free of any React Native code.

**Size:** 2 days

**Verification**, checked by a reviewer:

- [ ] The module builds with TypeScript strict mode and has no `any` types
- [ ] The types for articles, profiles and tags match the API specification
- [ ] Every function checks the response status, and returns or throws a typed error when the call fails
- [ ] Every request has a timeout, and a timeout produces the same typed error as a network failure
- [ ] Unit tests cover a successful call and a failed call for each function, with `fetch` replaced by a test double
- [ ] ESLint and Prettier run with no errors
- [ ] The lock file is committed, and the README explains how to install and test

Previous: [01. Mobile Platforms and Design](./01-mobile-platforms-and-design.md) · Next:
[03. React Native Fundamentals](./03-react-native-fundamentals.md)
