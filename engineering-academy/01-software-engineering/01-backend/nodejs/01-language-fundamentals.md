# 01. Language Fundamentals

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Techversant writes Node.js services in TypeScript, with strict compiler settings. Solid TypeScript and a clear
picture of how Node.js runs your code make every later stage easier. Projects use the current Node.js long-term
support (LTS) release. Back to the [roadmap](./README.md).

## TypeScript for the server

TypeScript adds types to JavaScript, so the compiler catches mistakes before the code runs. Techversant projects turn
on its strictest checks.

**What to learn:**

- Types, interfaces, union types and narrowing, and avoiding `any`
- The compiler settings Techversant requires, such as `strict`, `noUncheckedIndexedAccess` and
  `exactOptionalPropertyTypes`
- Typed errors: error classes with a `code`, never thrown strings

**Resources:**

- [TypeScript handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
- [Language and compiler settings](../../../../standards/nodejs/nodejs-typescript-style-guide.md#3-language--compiler-settings)
  and [error handling](../../../../standards/nodejs/nodejs-typescript-style-guide.md#7-error-handling), in the
  Techversant Node.js and TypeScript style guide

**Level:** Practitioner · Core

## The Node.js runtime and the event loop

Node.js runs your JavaScript on one main thread. The event loop lets it serve many requests at once by working on
others while one waits for the database or the network.

**What to learn:**

- What the event loop does, and why one slow, CPU-heavy function delays every request
- The difference between waiting work, such as a database call, and blocking work, such as hashing a large file
- Node.js release lines, and why projects use an LTS release

**Resources:**

- [The Node.js event loop](https://nodejs.org/en/learn/asynchronous-work/event-loop-timers-and-nexttick) and
  [Don't block the event loop](https://nodejs.org/en/learn/asynchronous-work/dont-block-the-event-loop), Node.js
  documentation

**Level:** Practitioner · Core

## Asynchronous code

Almost everything a back end does waits on something. Promises and `async`/`await` keep that code readable, and
mistakes here cause bugs that are hard to find.

**What to learn:**

- `async` and `await`, and handling rejected promises with `try`/`catch`
- Floating promises: why every promise must be awaited or handled, and the lint rule that catches them
- Running work in parallel with `Promise.all` and `Promise.allSettled`, with a limit on how many run at once

**Resources:**

- [Asynchronous JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Async_JS), MDN
- [Async and concurrency](../../../../standards/nodejs/nodejs-typescript-style-guide.md#9-async--concurrency), in the
  Techversant Node.js and TypeScript style guide

**Level:** Practitioner · Core

## Modules and packages

Node.js projects use ES modules and install packages with npm. The lock file makes every install the same.

**What to learn:**

- ES modules with `import` and `export`, and the `NodeNext` module setting Techversant uses
- `package.json` scripts, installing with `npm ci`, and why `package-lock.json` is committed
- Checking packages for known security issues with `npm audit`

**Resources:**

- [Modules: ECMAScript modules](https://nodejs.org/api/esm.html), Node.js documentation
- [Modules and imports](../../../../standards/nodejs/nodejs-typescript-style-guide.md#6-modules--imports), in the
  Techversant Node.js and TypeScript style guide

**Level:** Practitioner · Core

## Linting and formatting

A linter catches likely bugs, such as a forgotten `await`, and a formatter keeps the style consistent, so reviews can
focus on behaviour.

**What to learn:**

- ESLint with type-aware TypeScript rules, and Prettier
- Running both, and the type check, in the editor and before every commit

**Resources:**

- [Code formatting and linting](../../../../standards/nodejs/nodejs-typescript-style-guide.md#4-code-formatting--linting),
  in the Techversant Node.js and TypeScript style guide
- [typescript-eslint](https://typescript-eslint.io/getting-started/)

**Level:** Practitioner · Core

## Running TypeScript directly

Recent Node.js releases can run TypeScript files directly by removing the types, without a separate build step. It
suits scripts and development; most services still compile for production.

**What to learn:**

- What type stripping does not support: enums, namespaces and parameter properties, which the
  `erasableSyntaxOnly` setting rejects
- Imports with `.ts` extensions and `import type` for type-only imports, and how this differs from compiled
  `NodeNext` code, which imports `.js` files
- Why a separate type check is still needed, and why `tsconfig` `paths` are ignored

**Resources:** [TypeScript in Node.js](https://nodejs.org/en/learn/typescript/run-natively), Node.js documentation

**Level:** Advanced · Optional

## Project: Write a Slug Library in TypeScript

**Brief:** Write a small TypeScript package that turns an article title into a URL slug, such as
`How to Train Your Dragon` into `how-to-train-your-dragon`, and makes it unique when a slug is already taken. Your
RealWorld API uses the same rules in later stages.

**Size:** 2 days

**Verification**, checked by a reviewer:

- [ ] The package builds with the compiler settings in the Techversant style guide, with no `any` types
- [ ] Titles with accents, punctuation and repeated spaces give lower-case, hyphen-separated ASCII slugs, and a title
  of only symbols throws a typed error
- [ ] A taken slug gets a suffix, such as `-2`, through an interface that a later stage can back with the database
- [ ] Vitest tests cover each of these cases
- [ ] ESLint, with the floating promises rule on, and Prettier report no errors
- [ ] `package-lock.json` is committed, and the README explains how to install, test and use the package

Next: [02. The Framework](./02-the-framework.md)
