# 01. Language Fundamentals

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

ASP.NET Core is written in C#, and modern C# is short, safe and expressive. Solid C# makes every later stage easier.
Projects use the current long-term support (LTS) release, .NET 10, with C# 14. Back to the [roadmap](./README.md).

## Modern C# features

Recent C# releases added features that remove most boilerplate code. ASP.NET Core code uses them everywhere.

**What to learn:**

- Records, pattern matching, primary constructors and collection expressions
- Nullable reference types, and why projects turn their warnings into errors
- Language Integrated Query (LINQ) for filtering, sorting and shaping collections

**Resources:**

- [A tour of C#](https://learn.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/), Microsoft Learn
- [Nullable reference types](https://learn.microsoft.com/en-us/dotnet/csharp/nullable-references), Microsoft Learn

**Level:** Practitioner · Core

## Types and object-oriented design

ASP.NET Core applications are built from classes, records and interfaces. Small types with clear jobs are easier to
test and to change.

**What to learn:**

- Classes, records and structs, and when to use each
- Interfaces and immutability, and preferring composition to inheritance
- Generics, such as `List<Article>`

**Resources:** [The C# type system](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/types/), Microsoft
Learn

**Level:** Practitioner · Core

## Exceptions

.NET reports problems by throwing exceptions. Handling them in the right place keeps errors clear for users and
useful for developers.

**What to learn:**

- Throwing and catching exceptions, and never catching one only to ignore it
- Writing your own exception classes for problems in your domain
- `using` and `IDisposable`, so resources are released even when an exception is thrown

**Resources:**
[Best practices for exceptions](https://learn.microsoft.com/en-us/dotnet/standard/exceptions/best-practices-for-exceptions),
Microsoft Learn

**Level:** Practitioner · Core

## Async and await

An API spends most of its time waiting for the database and other services. `async` and `await` free the thread while
it waits, so the server can handle many requests at once.

**What to learn:**

- `Task`, `async` and `await`, and keeping code asynchronous all the way down
- Passing a `CancellationToken` to every call, so work stops when the request ends
- Why `.Result` and `.Wait()` block threads and can stall a busy server

**Resources:**
[Asynchronous programming](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/), Microsoft
Learn

**Level:** Practitioner · Core

## The .NET CLI and NuGet

The .NET command-line interface (CLI), the `dotnet` command, creates, builds, tests and publishes projects. NuGet
supplies the libraries.

**What to learn:**

- `dotnet new`, `build`, `test` and `run`, the `.csproj` file, and pinning the software development kit (SDK)
  version with `global.json`
- Adding NuGet packages, and keeping versions in one place with central package management
- NuGet's security audit, which warns about packages with known vulnerabilities when you restore

**Resources:**

- [.NET CLI](https://learn.microsoft.com/en-us/dotnet/core/tools/), Microsoft Learn
- [Dependency hygiene](../../../../security/audit/security-audit-reference.md#51-dependency-hygiene), in the
  Techversant security audit reference

**Level:** Practitioner · Core

## Code style and static analysis

A shared code style keeps reviews about behaviour, not formatting. The .NET analyzers find likely bugs while you type.

**What to learn:**

- An `.editorconfig` file, and formatting with `dotnet format`
- The built-in .NET analyzers, and treating warnings as errors in the build

**Resources:**

- [Code analysis in .NET](https://learn.microsoft.com/en-us/dotnet/fundamentals/code-analysis/overview), Microsoft
  Learn
- [Formatters and linters](../../../00-engineering-foundations/03-clean-code.md#formatters-and-linters), in
  Engineering Foundations

**Level:** Practitioner · Core

## Parallel programming

Some work can run on several threads at once, such as processing a large file. Shared data then needs care.

**What to learn:**

- `Task.WhenAll`, `Parallel.ForEachAsync` and channels, and why mutable shared objects cause bugs

**Resources:**
[Parallel programming](https://learn.microsoft.com/en-us/dotnet/standard/parallel-programming/), Microsoft Learn

**Level:** Advanced · Optional

## Project: Write a Slug Library in C\#

**Brief:** Before you use ASP.NET Core, write a small C# library that turns an article title into a URL slug, such as
`How to Train Your Dragon` into `how-to-train-your-dragon`, and makes it unique when a slug is already taken. Your
RealWorld API uses the same rules in later stages.

**Size:** 2 days

**Verification**, checked by a reviewer:

- [ ] The library and its test project build on .NET 10, with the SDK pinned in `global.json`
- [ ] Nullable reference types are on, and the build treats warnings as errors
- [ ] Titles with accents, punctuation and repeated spaces give lower-case, hyphen-separated ASCII slugs, and a title
  of only symbols throws a clear exception
- [ ] A taken slug gets a suffix, such as `-2`, through an asynchronous interface that a later stage can back with
  the database
- [ ] xUnit tests cover each of these cases
- [ ] `dotnet format --verify-no-changes` passes
- [ ] The README explains how to build, test and use the library

Next: [02. The Framework](./02-the-framework.md)
