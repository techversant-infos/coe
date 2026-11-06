# 05. Validation and Error Handling

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

An API must check every request, because anyone can send anything to it. When something goes wrong, the client needs
a clear, predictable error, and the team needs a log entry that explains it. Back to the [roadmap](./README.md).

## Validating requests with Zod

Your route schemas from stage 03 already reject bad input. This topic covers making the rules complete and the
messages useful.

**What to learn:**

- Rules for required fields, lengths, email addresses and lists, such as each item in `article.tagList`
- Validating nested input, such as `article.title`, and refusing unknown fields where it matters
- Why every value from outside, including headers and query strings, must be validated

**Resources:**

- [Zod documentation](https://zod.dev/)
- [Input validation](../../../../security/audit/security-audit-reference.md#71-input-validation), in the Techversant
  security audit reference

**Level:** Practitioner · Core

## Error response format

Clients handle errors in code, so every error must have the same shape. Fastify answers validation failures with
status 400 and its own JSON, which matches neither RealWorld nor Techversant, so you change it.

**What to learn:**

- A central error handler with `setErrorHandler` that turns every error into the contract's format
- Turning a Zod issue path, such as `["user", "username"]`, into `errors.username`, and replacing Zod's default
  messages with the contract's, such as `can't be blank`
- Returning 422 for invalid input, and 409 for a username or email that is already taken, as RealWorld does
- The Techversant standard error format for client projects, and how it differs from RealWorld's

**Resources:**

- [Error response format](../../../../standards/general/rest-api-best-practices.md#52-error-response-format) and
  [validation error examples](../../../../standards/general/rest-api-best-practices.md#7-validation-error-examples), in
  the Techversant REST API best practices
- [Practice-only parts of the contract](../practice-app.md#practice-only-parts-of-the-contract), on the back-end
  practice app page

**Level:** Practitioner · Core

## Domain errors

Business code should say what went wrong in business terms, such as "article not found", and leave HTTP details to
the edge of the app.

**What to learn:**

- Typed error classes, such as `NotFoundError` and `ForbiddenError`, thrown by services
- Mapping each error class to a status code and body in one place
- Never sending stack traces or internal messages to clients, and adding an error ID that matches the log line

**Resources:**

- [Errors](https://fastify.dev/docs/latest/Reference/Errors/), Fastify documentation
- [Error handling](../../../../standards/nodejs/nodejs-typescript-best-practices.md#error-handling), in the
  Techversant Node.js and TypeScript best practices

**Level:** Practitioner · Core

## Logging with Pino

Logs tell you what happened when a user reports a problem. Useful logs have context; safe logs leave out secrets and
personal data.

**What to learn:**

- Pino log levels, child loggers, and adding the request ID and user ID to every line
- Pino's `redact` option, to remove fields such as passwords and tokens from every log line
- What must never be logged: passwords, tokens and personal data

**Resources:**

- [Logging](https://fastify.dev/docs/latest/Reference/Logging/), Fastify documentation
- [Logging](../../../../standards/nodejs/nodejs-typescript-style-guide.md#8-logging), in the Techversant Node.js and
  TypeScript style guide, and
  [what must never be logged](../../../../security/audit/security-audit-reference.md#112-what-must-never-be-logged)

**Level:** Practitioner · Core

## Project: Validate Every Request

**Brief:** Complete the validation for every endpoint that takes input: sign-up, sign-in, updating the user, creating
and updating articles, and adding comments. Return errors in the RealWorld format. Sign-up and sign-in stop after
validation until stage 06, and new articles and comments belong to a seeded user.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Every endpoint that takes input validates it with a Zod schema, and handlers use only validated data
- [ ] Invalid input returns 422 with `{"errors": {"<field>": ["<message>"]}}`. Your own tests use the field names
  and messages from `specs/api/hurl/errors_auth.hurl` and `errors_articles.hurl`; the Hurl files themselves run
  from stage 06, because they sign up first.
- [ ] A missing article or profile returns 404 with `errors.<name>` set to `not found`, and no response anywhere
  shows a stack trace
- [ ] Updating an article in the same second as creating it changes `updatedAt`
- [ ] Services throw typed domain errors, and one error handler maps them to responses
- [ ] Log lines are JSON with the request ID, and a test shows that a password in a request is never logged
- [ ] Tests cover each error case

Previous: [04. Databases and Data Access](./04-databases-and-data-access.md) · Next:
[06. Authentication and Authorization](./06-authentication-and-authorization.md)
