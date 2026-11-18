# 02. Dart

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-12 · **Next review:** 2027-02-12

Flutter apps are written in Dart, a typed language from Google with sound null safety. Solid Dart skills make every
later stage easier, and the type system catches many mistakes before the app runs. Back to the
[roadmap](./README.md).

## Dart basics

Dart looks familiar if you know Java, C#, TypeScript or JavaScript, with a few ideas of its own.

**What to learn:**

- Variables with `var`, `final` and `const`, and why Flutter code uses `final` and `const` wherever it can
- Functions, named and optional parameters, and classes with constructors
- Collections: `List`, `Map` and `Set`, and methods such as `map`, `where` and `firstWhere`

**Resources:** [Introduction to Dart](https://dart.dev/language), Dart documentation

**Level:** Practitioner · Core

## Null safety

In Dart, a variable cannot hold `null` unless its type says so. The compiler checks this, so a whole class of crashes
cannot happen.

**What to learn:**

- Nullable types such as `String?`, and the operators `?.`, `??` and `!`
- Why `!` should be rare: it turns a compile-time check back into a possible crash
- Fields from the API that can be `null`, such as a profile's `bio` and `image`

**Resources:** [Sound null safety](https://dart.dev/null-safety), Dart documentation

**Level:** Practitioner · Core

## Asynchronous Dart

Calls to an API take time, and on mobile they often fail. `Future`, `async` and `await` let the app keep working
while it waits.

**What to learn:**

- `Future`, writing `async` functions with `await`, and `Stream` for values that arrive over time
- Handling errors with `try`/`catch`, including network failures and timeouts
- Calling an API with the `http` package, and checking the status code before reading the body

**Resources:**

- [Asynchronous programming](https://dart.dev/libraries/async/async-await), Dart documentation
- [Fetch data from the internet](https://docs.flutter.dev/cookbook/networking/fetch-data), Flutter documentation

**Level:** Practitioner · Core

## Modern Dart features

Recent versions of Dart added records, patterns and sealed classes. They make data and error handling shorter and
safer.

**What to learn:**

- Records for returning more than one value, and pattern matching with `switch` expressions
- Sealed classes for results that are either a success or a known kind of error, checked by the compiler
- Turning JSON into typed classes by hand, or with `json_serializable`

**Resources:**

- [Patterns](https://dart.dev/language/patterns), Dart documentation
- [JSON and serialisation](https://docs.flutter.dev/data-and-backend/serialization/json), Flutter documentation

**Level:** Practitioner · Core

## Packages, analysis and formatting

Dart projects add packages from pub.dev in `pubspec.yaml`. The analyser and formatter keep code consistent, so
reviews can focus on what the code does.

**What to learn:**

- `pubspec.yaml`, adding packages with `flutter pub add`, and why the `pubspec.lock` file is committed for apps
- Creating your own package with `dart create --template=package`, and using it from an app with a `path` dependency
- Checking a package's score, maintenance and platform support on pub.dev before you add it
- Unit tests with `package:test`, replacing the HTTP client with `MockClient` from `package:http/testing.dart`
- `dart analyze` with lint rules such as `flutter_lints`, and `dart format` before every commit

**Resources:**

- [Using packages](https://docs.flutter.dev/packages-and-plugins/using-packages), Flutter documentation
- [Customising static analysis](https://dart.dev/tools/analysis), Dart documentation
- [Formatters and linters](../../../00-engineering-foundations/03-clean-code.md#formatters-and-linters), in
  Engineering Foundations

**Level:** Practitioner · Core

## Project: Write a Typed API Client

**Brief:** Write a small Dart package that calls the RealWorld API: list articles, get one article by slug, and list
tags. Base the classes on the API specification, `specs/api/openapi.yml` in the RealWorld repository. You use this
package in every later stage, so keep it free of any Flutter code.

**Size:** 2 days

**Verification**, checked by a reviewer:

- [ ] The package has no analyser warnings, and uses `!` only where the pull request explains why
- [ ] The classes for articles, profiles and tags match the API specification, including fields that can be `null`
- [ ] Every function checks the status code, and returns or throws a typed error when the call fails
- [ ] Every request has a timeout, and a timeout produces the same typed error as a network failure
- [ ] Unit tests cover a successful call and a failed call for each function, with the HTTP client replaced by a test
  double
- [ ] `dart format` and `dart analyze` run with no changes and no warnings
- [ ] The README explains how to install and test

Previous: [01. Mobile Platforms and Design](./01-mobile-platforms-and-design.md) · Next:
[03. Flutter Fundamentals](./03-flutter-fundamentals.md)
