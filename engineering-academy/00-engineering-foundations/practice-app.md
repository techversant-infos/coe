# Practice App: RealWorld

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

All the projects in the [Engineering Foundations roadmap](./README.md) use the same open-source app. You work in a
stack close to your own, and the app's test suites check every change the same way for everyone.

## The App

RealWorld, also called Conduit, is a Medium-style blogging app. Users sign up, follow authors, write articles, add
tags, comment and favourite articles. The project publishes one API specification, and the community has built many
front ends and back ends against it. Any front end works with any back end.

Checked against the repository on 6 November 2026.

| Detail | Value |
|--------|-------|
| Repository | [realworld-apps/realworld](https://github.com/realworld-apps/realworld) |
| Licence | MIT, in the repository's `LICENSE` file |
| API specification | `specs/api/openapi.yml` |
| API tests | Hurl tests in `specs/api/hurl`, run with `specs/api/run-api-tests-hurl.sh` |
| End-to-end tests | Playwright tests in `specs/e2e`, including authentication, articles, comments and an XSS security test |
| Documentation | [docs.realworld.show](https://docs.realworld.show/) |
| Implementations | Listed on [codebase.show](https://codebase.show/projects/realworld), filtered by language and framework |

## Choosing Your Stack

Pick the implementation closest to the work you do, and check its licence before you start.

| You work on | Pick |
|-------------|------|
| Back end (Node.js, PHP, Java, .NET, Python and others) | A back end in your language, plus any working front end to try it in a browser |
| Web front end (React, Angular, Vue and others) | A front end in your framework, plus any working back end |
| Mobile | A back end in the language closest to your mobile work, such as Kotlin or Swift. Few RealWorld mobile apps are maintained, so most projects happen on the back end, and the **In your stack** notes on each topic show how it applies to mobile code. |
| Test automation | The back end or front end your team's products are closest to. Your test skills carry over to every project. |

Use the app for practice only. Do not deploy it with real users' data, and do not copy its code into client work.

## Setting It Up

1. Create a repository for your practice work, as agreed with your lead, and push the implementation you chose to
   it. You need your own repository so you can open pull requests and get them reviewed.
2. Follow the implementation's README to run it locally.
3. Clone the [RealWorld repository](https://github.com/realworld-apps/realworld) next to it, install
   [Hurl](https://hurl.dev/), and run the API tests against your back end:

   ```bash
   cd realworld/specs/api
   HOST=http://localhost:3000/api ./run-api-tests-hurl.sh
   ```

   Change the port to match your back end.
4. Record which tests pass. This is your baseline: after every project, the same tests must still pass.
5. If you work on a front end, run the end-to-end tests in `specs/e2e` as well, following the instructions in the
   RealWorld repository.

## The Feature You Build

From stage 05 onwards, you add one feature to the app: **article bookmarks**. A signed-in reader can bookmark an
article to read later, see a list of their bookmarks and remove one. Bookmarks are private to each reader.

The feature is small enough to build in a week, but touches every layer: the data model, an API, validation,
authorization, tests and, for front-end engineers, the user interface.

## How the Projects Use It

| Stage | Project |
|-------|---------|
| 01 | [Ship your first change](./01-git-and-pull-requests.md#project-ship-your-first-change) |
| 02 | [Explore and test with an AI assistant](./02-working-with-ai-tools.md#project-explore-and-test-with-an-ai-assistant) |
| 03 | [Clean up one module](./03-clean-code.md#project-clean-up-one-module) |
| 04 | [Extract a service and inject its dependencies](./04-design-principles.md#project-extract-a-service-and-inject-its-dependencies) |
| 05 | [Design article bookmarks](./05-design-thinking.md#project-design-article-bookmarks) |
| 06 | [Build the bookmarks API](./06-apis-and-boundaries.md#project-build-the-bookmarks-api) |
| 07 | [Test the feature and refactor one smell](./07-testing-and-refactoring.md#project-test-the-feature-and-refactor-one-smell) |
| 08 | [Security-review your feature](./08-secure-engineering.md#project-security-review-your-feature) |
| 09 | [Review three pull requests](./09-code-review.md#project-review-three-pull-requests) |
| 10 | [Hand over your feature](./10-communication-and-ownership.md#project-hand-over-your-feature) |
