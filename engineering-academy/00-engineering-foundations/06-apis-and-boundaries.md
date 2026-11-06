# 06. APIs and Boundaries

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

APIs are where your code meets other code, other teams and the outside world. A consistent design makes them easy
to use, and checking every input at the boundary keeps bad data out. Back to the [roadmap](./README.md).

## REST API design

Techversant has one standard for REST APIs, so every project's API looks and behaves the same way.

**What to learn:**

- Naming resources as plural nouns, nesting at most two levels, and putting the version in the URL
- Using HTTP methods for what they mean, and knowing which ones are idempotent
- The standard success and error response formats, and the right status code for each case

**Resources:**

- [REST API Best Practices](../../standards/general/rest-api-best-practices.md), Techversant's API standard
- [HTTP semantics (RFC 9110)](https://www.rfc-editor.org/rfc/rfc9110.html), for the meaning of methods and status
  codes

**In your stack:** front-end and mobile developers call APIs more than they build them. Knowing the standard lets
you handle every error response the same way, and spot API problems early.

**Level:** Practitioner · Core

## Validation at boundaries

Every input from outside your code, such as a request body, a query string, a file or a message, can be wrong or
hostile. Check it where it enters, before it reaches your business rules.

**What to learn:**

- Validating type, format, length and range on the server, using an allow list of what is accepted
- Returning clear validation errors in the standard format, one per field
- Treating client-side validation as help for the user, never as protection

**Resources:**

- [Input validation](../../security/audit/security-audit-reference.md#71-input-validation), in the Techversant
  security audit reference
- [Validation error examples](../../standards/general/rest-api-best-practices.md#7-validation-error-examples), in the
  Techversant REST API standard

**In your stack:** use your framework's validation tools, such as Zod or class-validator in TypeScript, or Laravel
form requests. In front ends and mobile apps, validate for a better experience, and still expect the server to
reject bad input.

**Level:** Practitioner · Core

## Performance awareness

Most performance problems come from a few common mistakes. Measure before and after a change, instead of guessing.

**What to learn:**

- The N+1 query problem: one query for a list, then one more query for each item
- Pagination, so a list endpoint never returns everything at once
- Measuring with real numbers, such as query counts and response times, before and after a change

**Resources:**

- [Performance validation](../../standards/general/ai-era-coding-guidelines.md#63-performance-validation), in the
  Techversant AI Era Coding Guidelines
- [Pagination](../../standards/general/rest-api-best-practices.md#81-pagination), in the Techversant REST API
  standard

**In your stack:** in a back end, check the queries your ORM generates. In a front end, avoid re-rendering large
lists and fetching the same data twice. In mobile, load lists page by page and cache images.

**Level:** Practitioner · Core

## Caching basics

A cache keeps a copy of data so it does not have to be fetched or computed again. It speeds things up, and it can
serve out-of-date data if you are not careful.

**What to learn:**

- HTTP caching headers, and when a response can be cached
- Clearing a cached item when the underlying data changes
- Never caching one user's private data where another user could see it

**Resources:** [HTTP caching](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Caching), MDN

**Level:** Practitioner · Optional

## Project: Build the Bookmarks API

**Brief:** Build the article bookmarks endpoints from your stage 05 design. RealWorld's existing API has its own
style, so match it for compatibility, and note in your ADR where that differs from the Techversant REST standard.
Front-end engineers also add the bookmark button and the bookmarks list to the user interface.

**Size:** 3–4 days

**Verification**, checked by a reviewer:

- [ ] Endpoints exist to add a bookmark, remove one and list the signed-in reader's bookmarks
- [ ] The bookmarks list is paginated
- [ ] Every input is validated on the server, and invalid input returns a clear error with the right status code
- [ ] A reader can never see or change another reader's bookmarks
- [ ] The list endpoint runs a fixed number of queries whatever the number of bookmarks, shown with query counts for
  1 and 50 bookmarks
- [ ] The ADR notes each place where the endpoints follow RealWorld's style rather than the Techversant standard
- [ ] The existing API tests still pass

Previous: [05. Design Thinking](./05-design-thinking.md) · Next:
[07. Testing and Refactoring](./07-testing-and-refactoring.md)
