# 08. Testing

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-20 · **Next review:** 2027-05-20

Tests let you change code without fear, including old code that nobody fully understands. TestBox is the testing
framework for CFML (ColdFusion Markup Language). Back to the [roadmap](./README.md).

## Unit tests with TestBox

Unit tests check one function or component on its own, quickly.

**What to learn:**

- TestBox specs: `describe()`, `it()` and `expect()`, and `beforeEach()` for setting up each test
- Testing models and services by giving them fake dependencies
- Running tests from the browser runner and with `box testbox run`

**Resources:**

- [Behaviour-driven development (BDD) primer](https://testbox.ortusbooks.com/getting-started/testbox-bdd-primer) and
  [Running tests](https://testbox.ortusbooks.com/getting-started/running-tests), TestBox documentation
- [Test levels](../../../00-engineering-foundations/07-testing-and-refactoring.md#test-levels), in Engineering
  Foundations

**Level:** Practitioner · Core

## Integration tests for ColdBox

Integration tests send a request through the whole framework, from the router to the response, without a browser.

**What to learn:**

- Test bundles that extend ColdBox's `BaseTestCase`, and running a route with `get()`, `post()` and `put()`
- Checking the status code, headers and JSON body of a response
- Running each test inside a transaction, or resetting the data, so tests pass in any order

**Resources:**

- [Testing quick start](https://coldbox.ortusbooks.com/testing/testing-quick-start) and
  [HTTP testing methods](https://coldbox.ortusbooks.com/the-basics/testing-quick-start/integration-testing/http-testing-methods),
  ColdBox documentation

**Level:** Practitioner · Core

## Mocks and test doubles

A mock stands in for something slow or outside your control, such as email or another API, so tests are fast and
repeatable.

**What to learn:**

- MockBox: creating mocks and stubs, and checking that a method was called
- Replacing the mail service and the job queue in tests
- Mocking only what you do not own, and testing the rest for real

**Resources:** [MockBox](https://testbox.ortusbooks.com/mocking/mockbox), TestBox documentation

**Level:** Practitioner · Core

## Contract tests and coverage

The RealWorld Hurl tests check your API against the contract from the outside. Coverage shows which lines your own
tests never run.

**What to learn:**

- Running the 13 Hurl files against a fresh database, locally and in continuous integration
- Code coverage with TestBox, which needs FusionReactor, a separately licensed monitoring tool, and reading the
  report for untested branches
- Checking formatting with cfformat on every pull request

**Resources:**

- [Hurl](https://hurl.dev/)
- [Code coverage](https://testbox.ortusbooks.com/digging-deeper/code-coverage), TestBox documentation
- [commandbox-cfformat](https://www.forgebox.io/view/commandbox-cfformat), ForgeBox

**Level:** Advanced · Core

## Characterising older code

Before you change old code without tests, write tests that record what it does today, right or wrong. They tell you
when your change alters behaviour you did not mean to touch.

**What to learn:**

- Characterisation tests: recording the current output for a set of inputs, then refactoring
- Finding a seam, a place where you can test a piece without running the whole page
- Testing a page by its HTTP response when nothing smaller is possible

**Resources:**

- [Characterization tests](../../../07-consulting/coldfusion/04-maintaining-legacy-applications.md#characterization-tests),
  in the Senior ColdFusion Consultant roadmap
- [ColdFusion best practices](../../../../standards/coldfusion/coldfusion-best-practices.md), Techversant:
  the testing section

**Level:** Advanced · Core

## Project: Pass the Full Test Suite

**Brief:** Get every RealWorld API test passing, add your own TestBox tests for every endpoint, and run everything in
continuous integration on each pull request. Then take over the older archive page below, which queries the article
database directly. Use a separate local practice folder outside the API checkout, web root and build context. Give it
its own `Application.cfc` and a datasource that points to a disposable copy of the schema with synthetic records.
Keep both versions of `archive.cfm` out of the API repository and its deployment image.

Match the table and column names to your local schema. Write characterisation tests before adding the optional
`tag` filter. Fix the injection and encoding problems while preserving the output for valid input.

```cfm
<!--- archive.cfm: lists the articles for one month --->
<cfparam name="url.month" default="#dateFormat(now(), 'yyyy-mm')#">
<cfquery name="qArticles">
  SELECT a.slug, a.title, a.created_at, u.username
  FROM articles a
  JOIN users u ON u.id = a.author_id
  WHERE to_char(a.created_at, 'YYYY-MM') = '#url.month#'
  ORDER BY a.created_at DESC
</cfquery>
<cfoutput>
  <h1>Articles for #url.month#</h1>
  <cfif qArticles.recordCount EQ 0>
    <p>No articles this month.</p>
  </cfif>
  <ul>
    <cfloop query="qArticles">
      <li><a href="/articles/#slug#">#title#</a> by #username# on #dateFormat(created_at, "d mmm yyyy")#</li>
    </cfloop>
  </ul>
</cfoutput>
```

**Size:** 3–4 days

**Verification**, checked by a reviewer:

- [ ] All 13 RealWorld Hurl files pass against a fresh database in continuous integration, and the pull request
  shows the result
- [ ] Every endpoint has integration tests for success and for each error case it can return
- [ ] Permission tests show that users cannot change other users' articles and comments
- [ ] Every public function in handlers and models has at least one test, and, where the project has a
  FusionReactor licence, line coverage is at least 80%
- [ ] `cfformat check` reports no issues
- [ ] Continuous integration runs the format check, the TestBox tests and the Hurl tests on every pull
  request, and a failure blocks the merge
- [ ] Characterisation tests, written before any change, record the archive page's output for a month with
  articles and a month with none, and still pass after the change
- [ ] `?tag=` limits the archive to that tag, and the page works as before without it
- [ ] The month and tag are checked and bound as parameters, every value on the page is encoded, and the pull
  request lists each problem found and how it was fixed
- [ ] The archive runs only in the isolated local setup. The pull request records the test results without adding
  either version of `archive.cfm` to the API repository.

Previous: [07. Background Jobs and Caching](./07-background-jobs-and-caching.md) · Next:
[09. Security and Performance](./09-security-and-performance.md)
