# 01. Language Fundamentals

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Laravel is PHP, and modern PHP is a typed, object-oriented language. Solid PHP makes every Laravel feature easier
to understand, and Techversant projects require PHP 8.3 or later. Back to the [roadmap](./README.md).

## Modern PHP syntax and types

Modern PHP catches many mistakes early when you declare types. Techversant code turns on strict types in every file.

**What to learn:**

- `declare(strict_types=1);`, and typing parameters, return values and properties
- Nullable and union types, `match` expressions, named arguments and the nullsafe operator (`?->`)
- Enums for fixed sets of values, and `readonly` properties and classes for values that must not change

**Resources:**

- [Language reference](https://www.php.net/manual/en/langref.php), PHP manual
- [PHP coding standards](../../../../standards/php/php-coding-standards.md), Techversant

**Level:** Practitioner · Core

## Object-oriented PHP

Laravel is built from classes. You read and write them every day: controllers, models, jobs and services.

**What to learn:**

- Classes, constructors with promoted properties, and visibility
- Interfaces and abstract classes, and when to use each
- Traits, and why Laravel uses them for shared behaviour such as `HasFactory`
- Static methods and late static binding, which Laravel facades and Eloquent rely on

**Resources:** [Classes and objects](https://www.php.net/manual/en/language.oop5.php), PHP manual

**Level:** Practitioner · Core

## Errors and exceptions

PHP reports problems by throwing exceptions. Handling them in the right place keeps errors clear for users and useful
for developers.

**What to learn:**

- Throwing and catching exceptions, and `finally`
- Writing your own exception classes for problems in your domain
- Letting unexpected exceptions reach the framework, instead of hiding them

**Resources:**

- [The Exception class](https://www.php.net/manual/en/class.exception.php) and
  [predefined exceptions](https://www.php.net/manual/en/reserved.exceptions.php), PHP manual
- [Error handling and logging](../../../../standards/php/php-coding-standards.md#7-error-handling--logging), in the
  Techversant PHP coding standards

**Level:** Practitioner · Core

## Composer and autoloading

Composer installs libraries and loads your classes automatically from their namespace, following the PSR-4 standard.

**What to learn:**

- `composer.json`, installing and updating packages, and why `composer.lock` is committed
- PSR-4 autoloading: how a namespace maps to a folder
- Version constraints such as `^13.0`, and checking packages for known security issues with `composer audit`

**Resources:**

- [Composer basic usage](https://getcomposer.org/doc/01-basic-usage.md)
- [Dependency management](../../../../standards/php/php-best-practices.md#3-dependency-management), in the Techversant
  PHP best practices

**Level:** Practitioner · Core

## Code style and static analysis

A shared code style keeps reviews about behaviour, not formatting. Static analysis reads your code without running it
and finds type errors and likely bugs.

**What to learn:**

- PSR-12 code style, checked by PHP_CodeSniffer or Laravel Pint with the `psr12` preset
- PHPStan, its levels, and why Techversant requires level 8 or higher
- Running both in the editor and before every commit

**Resources:**

- [Formatting and style](../../../../standards/php/php-coding-standards.md#4-formatting--style) and
  [Testing and quality assurance](../../../../standards/php/php-coding-standards.md#9-testing--quality-assurance), in
  the Techversant PHP coding standards
- [PHPStan: getting started](https://phpstan.org/user-guide/getting-started)

**Level:** Practitioner · Core

## Project: Write a Slug Library in Plain PHP

**Brief:** Before you use Laravel, write a small Composer package in plain PHP that turns an article title into a URL
slug, such as `How to Train Your Dragon` into `how-to-train-your-dragon`, and makes it unique when a slug is already
taken. Your RealWorld API uses the same rules in later stages.

**Size:** 2 days

**Verification**, checked by a reviewer:

- [ ] The package loads through Composer's PSR-4 autoloading, and `composer.lock` is committed
- [ ] Every file declares strict types, and every parameter, property and return value has a type
- [ ] Titles with accents, punctuation and repeated spaces give lower-case, hyphen-separated ASCII slugs, and a title
  of only symbols throws a clear exception
- [ ] A taken slug gets a suffix, such as `-2`, through an interface that a later stage can back with the database
- [ ] PHPUnit or Pest tests cover each of these cases
- [ ] PHP_CodeSniffer or Pint reports no PSR-12 issues, and PHPStan level 8 reports no errors
- [ ] The README explains how to install, test and use the package

Next: [02. The Framework](./02-the-framework.md)
