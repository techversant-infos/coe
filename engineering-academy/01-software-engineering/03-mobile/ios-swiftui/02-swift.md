# 02. Swift

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-18 · **Next review:** 2027-02-18

Swift is the language of every Apple platform. It is safe by design: the compiler catches missing values, unhandled
errors and data shared unsafely between tasks before the app runs. Back to the [roadmap](./README.md).

## Swift basics

Swift code is short to write but strict about types. Getting comfortable with its value types is the first step.

**What to learn:**

- Constants with `let` and variables with `var`, type inference, and the basic types
- Structs compared with classes: structs are copied, classes are shared, and most app data should be structs
- Enums with associated values, `switch` that must handle every case, protocols, extensions and closures

**Resources:**
[The Swift Programming Language](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/),
Swift documentation

**Level:** Practitioner · Core

## Optionals

A Swift value can never be missing unless its type says so. An optional, such as `String?`, holds either a value or
`nil`.

**What to learn:**

- Unwrapping with `if let`, `guard let` and `??`, and optional chaining with `?.`
- Why force unwrapping with `!` crashes the app when the value is `nil`, and when it is acceptable
- Modelling API fields that can be `null`, such as a profile's `bio`, as optionals

**Resources:**
[Optionals](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/thebasics/#Optionals), The
Swift Programming Language

**Level:** Practitioner · Core

## Error handling

Functions that can fail are marked `throws`, and the caller must handle the error. The compiler checks that nothing
is forgotten.

**What to learn:**

- Throwing, `do`/`catch` and `try`, and defining your own error types as enums
- Typed throws, such as `throws(APIError)`, so callers know exactly which errors to expect
- Turning network and decoding failures into errors the interface can explain to the user

**Resources:**
[Error handling](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/errorhandling/), The
Swift Programming Language

**Level:** Practitioner · Core

## Swift concurrency

Network calls take time, and the interface must keep responding while they run. Swift's concurrency features run
that work safely, and Swift 6 checks for data races when the code compiles.

**What to learn:**

- `async` and `await`, `Task`, and cancelling a task when the user leaves a screen
- Actors and the main actor: new Xcode app projects run code on the main actor by default, and slow work moves off it
  on purpose
- `Sendable`, and reading the compiler's data-race errors instead of silencing them

**Resources:**

- [Concurrency](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/), The
  Swift Programming Language
- [Swift 6 migration guide](https://www.swift.org/migration/documentation/migrationguide/), Swift documentation

**Level:** Practitioner · Core

## Codable and JSON

API responses arrive as JSON (JavaScript Object Notation). The `Codable` protocol turns JSON into typed Swift values
and back.

**What to learn:**

- `Codable` structs, `JSONDecoder` and `JSONEncoder`, with the default key strategy, because RealWorld keys are already
  camelCase, such as `createdAt`
- Decoding ISO 8601 dates with fractional seconds, such as `2026-11-18T09:25:38.683Z`, with a custom date strategy,
  because the built-in `.iso8601` strategy rejects the fractional part; and the RealWorld wrappers such as
  `{"article": {...}}`
- Reading decoding errors, which say exactly which field did not match

**Resources:**
[Encoding and decoding custom types](https://developer.apple.com/documentation/foundation/encoding-and-decoding-custom-types),
Apple

**Level:** Practitioner · Core

## Packages, testing and formatting

Swift Package Manager adds libraries to a project and builds your own packages. Tests and a formatter keep the code
reliable and consistent, so reviews can focus on what the code does.

**What to learn:**

- Adding a package in Xcode, creating your own with `swift package init --type library`, and checking a package's
  maintenance and licence before you add it
- Unit tests with Swift Testing: `@Test`, `#expect` and `#require`
- Replacing the network in tests with a `URLProtocol` subclass that returns prepared responses
- `swift format`, included with Xcode, and a linter such as SwiftLint, run before every commit

**Resources:**

- [Swift Package Manager](https://www.swift.org/documentation/package-manager/), Swift documentation
- [Swift Testing](https://developer.apple.com/documentation/testing), Apple
- [Formatters and linters](../../../00-engineering-foundations/03-clean-code.md#formatters-and-linters), in
  Engineering Foundations

**Level:** Practitioner · Core

## Project: Write a Typed API Client

**Brief:** Write a small Swift package that calls the RealWorld API: list articles, get one article by slug, and list
tags. Base the types on the API specification, `specs/api/openapi.yml` in the RealWorld repository. You use this
package in every later stage, so keep it free of any SwiftUI code.

**Size:** 2 days

**Verification**, checked by a reviewer:

- [ ] The package builds in Swift 6 language mode with no warnings, and uses `!` only where the pull request explains
  why
- [ ] The types for articles, profiles and tags match the API specification, with optionals for fields that can be
  `null`
- [ ] Every function is `async`, checks the status code, and throws a typed error when the call fails
- [ ] Every request has a timeout, and a timeout produces the same typed error as a network failure
- [ ] Swift Testing tests cover a successful call and a failed call for each function, with the network replaced by a
  `URLProtocol` stub
- [ ] `swift format` makes no changes, and the linter reports no warnings
- [ ] The README explains how to add the package and run the tests

Previous: [01. iOS Platform and Design](./01-ios-platform-and-design.md) · Next:
[03. SwiftUI Fundamentals](./03-swiftui-fundamentals.md)
