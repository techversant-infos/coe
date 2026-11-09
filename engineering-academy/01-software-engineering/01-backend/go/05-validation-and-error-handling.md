# 05. Validation and Error Handling

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

An API must check every request, because anyone can send anything to it. When something goes wrong, the client needs
a clear, predictable error, and the team needs a log entry that explains it. Back to the [roadmap](./README.md).

## Validating requests

Every request body is decoded into a request struct and checked before your code uses it.

**What to learn:**

- Validating structs with a library such as go-playground/validator, with rules such as `required`, `email` and `max`,
  or with plain checks in a `Validate` method
- Reporting field names from the `json` tags, such as `email` rather than `Email`, with messages that match the
  contract, such as `can't be blank`, and putting the contract's message first when several rules fail on one field
- Telling a missing field from an explicit `null` in partial updates, for example with a small generic type that
  records whether the field was sent: `PUT /api/user` rejects `"email": null`, saves `"image": null` and leaves
  missing fields unchanged. Use the type as a value field, not a pointer, because `encoding/json` passes `null` to
  `UnmarshalJSON` only for value fields.
- The password rules the tests check: shorter than 8 characters returns 422, and 64 characters is accepted

**Resources:**

- [validator](https://pkg.go.dev/github.com/go-playground/validator/v10)
- [Input validation](../../../../security/audit/security-audit-reference.md#71-input-validation), in the Techversant
  security audit reference

**Level:** Practitioner · Core

## Error response format

Clients handle errors in code, so every error must have the same shape. In Go you write that shape yourself, in one
place.

**What to learn:**

- One function that writes every error response, used by every handler and middleware
- Returning 422 for invalid input, as `{"errors": {"<field>": ["<message>"]}}`
- The Techversant standard error format for client projects, and how it differs from RealWorld's

**Resources:**

- [Error response format](../../../../standards/general/rest-api-best-practices.md#52-error-response-format), in the
  Techversant REST API best practices
- [Practice-only parts of the contract](../practice-app.md#practice-only-parts-of-the-contract), on the back-end
  practice app page

**Level:** Practitioner · Core

## Domain errors

Business code should say what went wrong in business terms, such as "article not found", and leave HTTP details to
the edge of the app.

**What to learn:**

- Error values and types for your domain, such as `ErrNotFound`, returned by services and turned into status codes in
  one place with `errors.Is` and `errors.As`
- A handler type that returns an error, so handlers do not each write their own error responses
- Never sending internal error text or stack traces to clients

**Resources:**
[Error handling](../../../../security/audit/security-audit-reference.md#121-error-handling), in the Techversant
security audit reference

**Level:** Practitioner · Core

## Logging with slog

Logs tell you what happened when a user reports a problem. Useful logs have context; safe logs leave out secrets
and personal data.

**What to learn:**

- The standard library's `log/slog` package, its JSON handler and log levels
- Adding the request ID and user ID to every line, for example with a logger stored in the request context
- What must never be logged: passwords, tokens and personal data, and hiding them with the `LogValuer` interface

**Resources:**

- [Package log/slog](https://pkg.go.dev/log/slog), Go documentation
- [What must never be logged](../../../../security/audit/security-audit-reference.md#112-what-must-never-be-logged),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Project: Validate Every Request

**Brief:** Add validation for every endpoint that takes input: sign-up, sign-in, updating the user, creating and
updating articles, and adding comments. Return errors in the RealWorld format. Sign-up and sign-in stop after
validation until stage 06, and new articles and comments belong to, and `PUT /api/user` updates, a seeded user.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Every request body is decoded into a request struct and validated, and handlers use only validated data
- [ ] Invalid input returns 422 with `{"errors": {"<field>": ["<message>"]}}`. Your own tests use the field names
  and messages from `specs/api/hurl/errors_auth.hurl` and `errors_articles.hurl`; the Hurl files themselves run
  from stage 06, because they sign up first.
- [ ] Updates follow the tests: an article updated without `tagList` keeps its tags, `"tagList": []` removes
  them and `"tagList": null` returns 422; `PUT /api/user` rejects `null` for `email` and `username` and a
  password under 8 characters, saves `"image": null` and keeps fields that were not sent
- [ ] A missing article or profile returns 404 with `errors.<name>` set to `not found`, and no response anywhere
  shows internal error text
- [ ] Updating an article in the same second as creating it changes `updatedAt`
- [ ] Log lines are JSON with the request ID, and a test shows that a password in a request is never logged
- [ ] Tests cover each error case

Previous: [04. Databases and Data Access](./04-databases-and-data-access.md) · Next:
[06. Authentication and Authorization](./06-authentication-and-authorization.md)
