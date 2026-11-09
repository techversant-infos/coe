# 01. Language Fundamentals

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Go is a small language with a large standard library, and Go teams build most of a service with the standard library
alone. Solid Go makes every later stage easier. Projects use the current release, Go 1.27; each Go release gets
security fixes until two newer releases are out. Back to the [roadmap](./README.md).

## Go basics

Go has few features, and each one is used everywhere. Learn them well before you build a server.

**What to learn:**

- Types, structs, methods and pointers, and when a method needs a pointer receiver
- Slices and maps, and the zero value of every type, including why a `nil` slice and an empty slice look different
  in JSON
- Packages, exported names that start with a capital letter, and how to lay out a small project

**Resources:**

- [A Tour of Go](https://go.dev/tour/), go.dev
- [Effective Go](https://go.dev/doc/effective_go), go.dev

**Level:** Practitioner · Core

## Interfaces and composition

Go has no classes or inheritance. Small interfaces and struct embedding do the same jobs, and make code easy to test.

**What to learn:**

- Interfaces that a type satisfies by having the methods, with no "implements" keyword, and keeping interfaces
  small
- Accepting interfaces and returning concrete types, so callers can pass a fake in tests
- Embedding one struct in another, and why it is not inheritance

**Resources:** [Effective Go](https://go.dev/doc/effective_go), go.dev

**Level:** Practitioner · Core

## Errors as values

Go functions return errors as ordinary values, and the caller decides what to do. Checking every error is what keeps
Go services reliable.

**What to learn:**

- Returning an `error` and checking it at every call, never ignoring it with `_`
- Wrapping errors with `%w`, and checking them with `errors.Is` and `errors.As`
- Your own error values and types for problems in your domain, and why `panic` is only for programmer mistakes

**Resources:**

- [Working with errors](https://go.dev/blog/go1.13-errors), the Go blog
- [Package errors](https://pkg.go.dev/errors), Go documentation

**Level:** Practitioner · Core

## Modules and tooling

The `go` command builds, tests and manages dependencies, with no extra build tool.

**What to learn:**

- The `go.mod` and `go.sum` files, adding a module such as `golang.org/x/text`, and `go mod tidy`
- Pinning tools written in Go, such as goose and `govulncheck`, with `tool` lines in `go.mod`. Install sqlc as a
  pinned release binary or run its Docker image, because building it needs a C compiler.
- Checking dependencies for known security issues with `govulncheck`

**Resources:**

- [Managing dependencies](https://go.dev/doc/modules/managing-dependencies), go.dev
- [Dependency hygiene](../../../../security/audit/security-audit-reference.md#51-dependency-hygiene), in the
  Techversant security audit reference

**Level:** Practitioner · Core

## Code style and static analysis

Every Go project uses the same formatting, so reviews are about behaviour. Linters find likely bugs without running
the code.

**What to learn:**

- Formatting with `gofmt`, and finding likely bugs with `go vet`
- Running golangci-lint with linters such as staticcheck, errcheck and gosec, in the editor and in the build

**Resources:**

- [golangci-lint](https://golangci-lint.run/)
- [Formatters and linters](../../../00-engineering-foundations/03-clean-code.md#formatters-and-linters), in
  Engineering Foundations

**Level:** Practitioner · Core

## Goroutines, channels and context

A Go server runs each request in its own goroutine, so every Go developer works with concurrency from the first day.

**What to learn:**

- Goroutines and channels, `sync.WaitGroup` and `sync.Mutex`, and why shared data needs protecting
- The `context` package: passing a context as the first argument, and stopping work when it is cancelled
- Finding data races with the race detector, `go test -race`

**Resources:**

- [Pipelines and cancellation](https://go.dev/blog/pipelines), the Go blog
- [Data race detector](https://go.dev/doc/articles/race_detector), go.dev

**Level:** Practitioner · Core

## Generics

Generics let one function or type work with many types, such as a helper that splits any list into pages.

**What to learn:**

- Type parameters and constraints, and when a plain interface is clearer

**Resources:** [Getting started with generics](https://go.dev/doc/tutorial/generics), go.dev

**Level:** Advanced · Optional

## Project: Write a Slug Library in Go

**Brief:** Before you build a server, write a small Go package that turns an article title into a URL slug, such as
`How to Train Your Dragon` into `how-to-train-your-dragon`, and makes it unique when a slug is already taken. Your
RealWorld API uses the same rules in later stages.

**Size:** 2 days

**Verification**, checked by a reviewer:

- [ ] The module builds and its tests pass on Go 1.27 with `go test ./...`
- [ ] Titles with accents, punctuation and repeated spaces give lower-case, hyphen-separated ASCII slugs, and a title
  of only symbols returns an error that callers can check with `errors.Is`
- [ ] A taken slug gets a suffix, such as `-2`, through an interface that takes a context, so a later stage can back
  it with the database
- [ ] Table-driven tests cover each of these cases, and `go test -race` passes
- [ ] `gofmt`, `go vet` and golangci-lint report no problems
- [ ] The README explains how to build, test and use the package

Next: [02. The Framework](./02-the-framework.md)
