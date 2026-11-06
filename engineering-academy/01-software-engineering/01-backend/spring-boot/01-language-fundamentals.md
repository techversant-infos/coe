# 01. Language Fundamentals

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Spring Boot is Java, and modern Java is far shorter and clearer than the Java many people remember. Solid Java makes
every Spring feature easier to understand. Projects use the current long-term support (LTS) release, Java 25. Back to
the [roadmap](./README.md).

## Modern Java

Recent Java releases added features that remove most boilerplate code. Spring Boot code uses them everywhere.

**What to learn:**

- Records for data classes, and `var` for local variables
- Pattern matching with `instanceof` and `switch`, and sealed types
- Text blocks, the `Optional` type, and the Stream API for working with collections

**Resources:**

- [Learn Java](https://dev.java/learn/), dev.java
- [Records](https://dev.java/learn/records/), dev.java

**Level:** Practitioner · Core

## Object-oriented design in Java

Spring applications are built from classes and interfaces. Small classes with clear jobs are easier to test and to
change.

**What to learn:**

- Classes, interfaces and immutability, and preferring composition to inheritance
- Generics, such as `List<Article>`, and why raw types cause bugs
- `equals`, `hashCode` and `toString`, and why records give them to you

**Resources:** [Classes and objects](https://dev.java/learn/classes-objects/), dev.java

**Level:** Practitioner · Core

## Exceptions

Java reports problems by throwing exceptions. Handling them in the right place keeps errors clear for users and
useful for developers.

**What to learn:**

- Checked and unchecked exceptions, and why most application code uses unchecked ones
- Writing your own exception classes for problems in your domain
- `try`-with-resources, and never catching an exception only to ignore it

**Resources:** [Exceptions](https://dev.java/learn/exceptions/), dev.java

**Level:** Practitioner · Core

## Build tools and dependencies

Maven or Gradle builds the project, downloads its libraries and runs its tests. Most Spring Boot projects use Maven.

**What to learn:**

- The `pom.xml` file, dependencies and scopes, and the Maven wrapper (`mvnw`) that pins the Maven version
- The build lifecycle: compile, test, package and verify
- Checking dependencies for known security issues, for example with OWASP (Open Worldwide Application Security Project)
  Dependency-Check

**Resources:**

- [Maven in 5 minutes](https://maven.apache.org/guides/getting-started/maven-in-five-minutes.html), Apache Maven
- [Dependency hygiene](../../../../security/audit/security-audit-reference.md#51-dependency-hygiene), in the
  Techversant security audit reference

**Level:** Practitioner · Core

## Code style and static analysis

A shared code style keeps reviews about behaviour, not formatting. Static analysis finds likely bugs without running
the code.

**What to learn:**

- Formatting code automatically, for example with Spotless, and checking style with Checkstyle
- Finding likely bugs with SpotBugs or Error Prone, in the build and in the editor

**Resources:**

- [SpotBugs](https://spotbugs.github.io/)
- [Formatters and linters](../../../00-engineering-foundations/03-clean-code.md#formatters-and-linters), in
  Engineering Foundations

**Level:** Practitioner · Core

## Concurrency and virtual threads

Virtual threads let a Java server handle many waiting requests cheaply. Spring Boot can turn them on with one
setting.

**What to learn:**

- Threads, shared state, and why mutable shared objects cause bugs
- Virtual threads, and what they change for code that waits on databases and other services

**Resources:** [Virtual threads](https://dev.java/learn/new-features/virtual-threads/), dev.java

**Level:** Advanced · Optional

## Project: Write a Slug Library in Java

**Brief:** Before you use Spring, write a small Java library that turns an article title into a URL slug, such as
`How to Train Your Dragon` into `how-to-train-your-dragon`, and makes it unique when a slug is already taken. Your
RealWorld API uses the same rules in later stages.

**Size:** 2 days

**Verification**, checked by a reviewer:

- [ ] The library builds with the Maven wrapper on Java 25
- [ ] Titles with accents, punctuation and repeated spaces give lower-case, hyphen-separated ASCII slugs, and a title
  of only symbols throws a clear exception
- [ ] A taken slug gets a suffix, such as `-2`, through an interface that a later stage can back with the database
- [ ] JUnit tests cover each of these cases
- [ ] The formatter, Checkstyle, and SpotBugs or Error Prone run in the build with no errors
- [ ] The README explains how to build, test and use the library

Next: [02. The Framework](./02-the-framework.md)
