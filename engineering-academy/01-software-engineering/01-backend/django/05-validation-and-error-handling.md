# 05. Validation and Error Handling

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

An API must check every request, because anyone can send anything to it. When something goes wrong, the client needs
a clear, predictable error, and the team needs a log entry that explains it. Back to the [roadmap](./README.md).

## Validation with serializers

Serializers validate incoming data before your code uses it, so views only ever work with valid data.

**What to learn:**

- Field options such as `required`, `max_length` and `allow_blank`, and `EmailField`
- Validating nested input, such as `article.title` and each item in `article.tagList`
- Field and object validation methods, and using only `serializer.validated_data`, never the raw request data

**Resources:**

- [Validators](https://www.django-rest-framework.org/api-guide/validators/), DRF documentation
- [Input validation](../../../../security/audit/security-audit-reference.md#71-input-validation), in the Techversant
  security audit reference

**Level:** Practitioner · Core

## Error response format

Clients handle errors in code, so every error must have the same shape. DRF answers validation failures with status
400 and its own JSON, which matches neither RealWorld nor Techversant, so you change it.

**What to learn:**

- A custom exception handler, set in `REST_FRAMEWORK["EXCEPTION_HANDLER"]`, that turns every error into the
  contract's format
- Mapping errors with the `unique` code, from `exc.get_codes()`, to 409, and validating the inner `user` or
  `article` object, so field errors are not nested under it
- Returning 422 for other invalid input, and replacing DRF's default messages with the contract's, such as
  `can't be blank`
- The Techversant standard error format for client projects, and how it differs from RealWorld's

**Resources:**

- [Exceptions](https://www.django-rest-framework.org/api-guide/exceptions/), DRF documentation
- [Error response format](../../../../standards/general/rest-api-best-practices.md#52-error-response-format), in the
  Techversant REST API best practices
- [Practice-only parts of the contract](../practice-app.md#practice-only-parts-of-the-contract), on the back-end
  practice app page

**Level:** Practitioner · Core

## Domain errors

Business code should say what went wrong in business terms, such as "article not found", and leave HTTP details to
the edge of the app.

**What to learn:**

- Your own exception classes, raised by services, and mapped to status codes in the exception handler
- Turning `Http404` and `DoesNotExist` into the contract's 404 body
- Never sending stack traces or internal messages to clients

**Resources:**
[Error handling](../../../../security/audit/security-audit-reference.md#121-error-handling), in the Techversant
security audit reference

**Level:** Practitioner · Core

## Logging

Logs tell you what happened when a user reports a problem. Useful logs have context; safe logs leave out secrets
and personal data.

**What to learn:**

- Django's `LOGGING` setting, loggers and levels, and adding the request ID and user ID to every line
- Writing logs as JSON, for example with structlog, so log tools can search them
- What must never be logged: passwords, tokens and personal data

**Resources:**

- [Logging](https://docs.djangoproject.com/en/6.1/topics/logging/), Django documentation
- [What must never be logged](../../../../security/audit/security-audit-reference.md#112-what-must-never-be-logged),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Project: Validate Every Request

**Brief:** Add validation for every endpoint that takes input: sign-up, sign-in, updating the user, creating and
updating articles, and adding comments. Return errors in the RealWorld format. Sign-up and sign-in stop after
validation until stage 06, and new articles and comments belong to a seeded user.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Every endpoint that takes input validates it with a serializer, and views use only validated data
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
