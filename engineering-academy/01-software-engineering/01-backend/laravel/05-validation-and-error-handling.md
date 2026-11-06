# 05. Validation and Error Handling

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

An API must check every request, because anyone can send anything to it. When something goes wrong, the client needs
a clear, predictable error, and the team needs a log entry that explains it. Back to the [roadmap](./README.md).

## Form requests and validation rules

A form request validates the input before the controller runs, so the controller only ever sees valid data.

**What to learn:**

- Creating form requests, and using built-in rules such as `required`, `email`, `max` and `unique`
- Validating nested input, such as `article.title` and each item in `article.tagList`
- Using only the validated data, with `$request->validated()`, never the raw input

**Resources:**

- [Validation](https://laravel.com/docs/13.x/validation), Laravel documentation
- [Input validation](../../../../security/audit/security-audit-reference.md#71-input-validation), in the Techversant
  security audit reference

**Level:** Practitioner · Core

## Error response format

Clients handle errors in code, so every error must have the same shape. Laravel's default error JSON does not match
RealWorld's or Techversant's, so you change it.

**What to learn:**

- Changing how validation errors are returned, so they match the contract
- Returning 409 for a username or email that is already taken, as RealWorld does, and 422 for other invalid input
- The Techversant standard error format for client projects, and how it differs from RealWorld's

**Resources:**

- [Error response format](../../../../standards/general/rest-api-best-practices.md#52-error-response-format) and
  [validation error examples](../../../../standards/general/rest-api-best-practices.md#7-validation-error-examples), in
  the Techversant REST API best practices
- [Practice-only parts of the contract](../practice-app.md#practice-only-parts-of-the-contract), on the back-end
  practice app page

**Level:** Practitioner · Core

## Exception handling

Exceptions that reach Laravel become responses. You decide how each kind is shown, and make sure no internal detail
reaches the client.

**What to learn:**

- Rendering exceptions as JSON in `bootstrap/app.php` with `withExceptions`, and with `shouldRenderJsonWhen` for
  every `/api` path, because some clients, including the RealWorld tests, send no `Accept` header
- Turning a missing model into a 404 in the contract's error format
- Why `APP_DEBUG` must be off in production, so stack traces never reach clients

**Resources:**

- [Error handling](https://laravel.com/docs/13.x/errors), Laravel documentation
- [Error handling](../../../../security/audit/security-audit-reference.md#121-error-handling), in the Techversant
  security audit reference

**Level:** Practitioner · Core

## Logging

Logs tell you what happened when a user reports a problem. Useful logs have context; safe logs leave out secrets
and personal data.

**What to learn:**

- Log channels and levels, and adding context such as the request ID and user ID
- Writing logs as JSON, so log tools can search them
- What must never be logged: passwords, tokens and personal data

**Resources:**

- [Logging](https://laravel.com/docs/13.x/logging), Laravel documentation
- [Logging, observability and monitoring](../../../../standards/php/php-best-practices.md#8-logging-observability--monitoring),
  in the Techversant PHP best practices, and
  [what must never be logged](../../../../security/audit/security-audit-reference.md#112-what-must-never-be-logged)

**Level:** Practitioner · Core

## Project: Validate Every Request

**Brief:** Add form requests for every endpoint that takes input: sign-up, sign-in, updating the user, creating and
updating articles, and adding comments. Return errors in the RealWorld format. Sign-up and sign-in stop after
validation until stage 06, and new articles and comments belong to a seeded user.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Every endpoint that takes input has a form request, and controllers use only validated data
- [ ] Invalid input returns 422 with `{"errors": {"<field>": ["<message>"]}}`, using the field names and messages in
  `specs/api/hurl/errors_auth.hurl` and `errors_articles.hurl`
- [ ] A username or email that is already taken returns 409
- [ ] A missing article, profile or comment returns 404 with `errors.<name>` set to `not found`, and no response
  anywhere shows a stack trace
- [ ] Invalid requests without an `Accept` header still get JSON errors, not a redirect
- [ ] Log lines are JSON with the request ID, and a test shows that a password in a request is never logged
- [ ] Feature tests cover each error case

Previous: [04. Databases and Data Access](./04-databases-and-data-access.md) · Next:
[06. Authentication and Authorization](./06-authentication-and-authorization.md)
