# 05. Validation and Error Handling

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

An API must check every request, because anyone can send anything to it. When something goes wrong, the client needs
a clear, predictable error, and the team needs a log entry that explains it. Back to the [roadmap](./README.md).

## Bean Validation

Jakarta Bean Validation checks request data transfer objects (DTOs) with annotations before your code uses them.

**What to learn:**

- `@Valid` on request bodies, and constraints such as `@NotBlank`, `@Email` and `@Size` on record components
- Validating nested objects, such as the `user` inside `{"user": {...}}`, and each item in `article.tagList`
- Custom messages, so they match the contract, such as `can't be blank`, and putting the contract's message first
  when several constraints fail on one field, for example by skipping length checks on blank values
- Telling a missing field from an explicit `null` in partial updates, for example with `Optional<String>` record
  components: `PUT /api/user` rejects `"email": null`, saves `"image": null` and leaves missing fields
  unchanged

**Resources:**

- [Validation](https://docs.spring.io/spring-boot/reference/io/validation.html), Spring Boot documentation
- [Input validation](../../../../security/audit/security-audit-reference.md#71-input-validation), in the Techversant
  security audit reference

**Level:** Practitioner · Core

## Error response format

Clients handle errors in code, so every error must have the same shape. By default, Spring answers validation failures
with status 400, and it can also return the standard problem details format. Neither matches the RealWorld or
Techversant format, so you replace them.

**What to learn:**

- A `@RestControllerAdvice` class that turns every error into the contract's format
- Returning 422 for invalid input, with field names taken from the inner object, such as `email` rather than
  `user.email`
- The Techversant standard error format for client projects, and how it differs from RealWorld's

**Resources:**

- [Error responses](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-ann-rest-exceptions.html),
  Spring Framework documentation
- [Error response format](../../../../standards/general/rest-api-best-practices.md#52-error-response-format), in the
  Techversant REST API best practices
- [Practice-only parts of the contract](../practice-app.md#practice-only-parts-of-the-contract), on the back-end
  practice app page

**Level:** Practitioner · Core

## Domain exceptions

Business code should say what went wrong in business terms, such as "article not found", and leave HTTP details to
the edge of the app.

**What to learn:**

- Your own exception classes, thrown by services and mapped to status codes in one `@RestControllerAdvice`
- Turning "not found" into the contract's 404 body
- Never sending stack traces or internal messages to clients

**Resources:**
[Error handling](../../../../security/audit/security-audit-reference.md#121-error-handling), in the Techversant
security audit reference

**Level:** Practitioner · Core

## Logging

Logs tell you what happened when a user reports a problem. Useful logs have context; safe logs leave out secrets
and personal data.

**What to learn:**

- SLF4J and Logback, log levels, and adding the request ID and user ID to every line through the Mapped Diagnostic
  Context (MDC)
- Spring Boot's built-in structured logging, which writes logs as JSON
- What must never be logged: passwords, tokens and personal data

**Resources:**

- [Logging](https://docs.spring.io/spring-boot/reference/features/logging.html), Spring Boot documentation
- [What must never be logged](../../../../security/audit/security-audit-reference.md#112-what-must-never-be-logged),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Project: Validate Every Request

**Brief:** Add validation for every endpoint that takes input: sign-up, sign-in, updating the user, creating and
updating articles, and adding comments. Return errors in the RealWorld format. Sign-up and sign-in stop after
validation until stage 06, and new articles and comments belong to, and `PUT /api/user` updates, a seeded user.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Every request body is a validated DTO, and controllers use only validated data
- [ ] Invalid input returns 422 with `{"errors": {"<field>": ["<message>"]}}`. Your own tests use the field names
  and messages from `specs/api/hurl/errors_auth.hurl` and `errors_articles.hurl`; the Hurl files themselves run
  from stage 06, because they sign up first.
- [ ] Updates follow the tests: an article updated without `tagList` keeps its tags, `"tagList": []` removes
  them and `"tagList": null` returns 422; `PUT /api/user` rejects `null` for `email` and `username` and a
  password under 8 characters, saves `"image": null` and keeps fields that were not sent
- [ ] A missing article or profile returns 404 with `errors.<name>` set to `not found`, and no response anywhere
  shows a stack trace
- [ ] Updating an article in the same second as creating it changes `updatedAt`
- [ ] Log lines are JSON with the request ID, and a test shows that a password in a request is never logged
- [ ] Tests cover each error case

Previous: [04. Databases and Data Access](./04-databases-and-data-access.md) · Next:
[06. Authentication and Authorization](./06-authentication-and-authorization.md)
