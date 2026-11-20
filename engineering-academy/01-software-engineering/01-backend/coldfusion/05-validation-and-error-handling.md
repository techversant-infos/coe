# 05. Validation and Error Handling

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-20 · **Next review:** 2027-05-20

Every request is untrusted until you check it. Clear validation errors help the people who build against your API,
and careful error handling keeps stack traces and secrets out of responses. Back to the [roadmap](./README.md).

## Validation with cbvalidation

The cbvalidation module checks input against a set of rules, called constraints, before your code uses it.

**What to learn:**

- Installing cbvalidation, and writing constraints such as `required`, `type`, `size` and `regex`, with custom
  messages such as `can't be blank`
- Validating the nested body, such as `rc.user` or `rc.article`, not the whole request collection
- Checking a taken username or email in the service, and turning a unique-constraint error into 409, not the
  `unique` constraint, which returns 422 and misses two sign-ups at the same moment
- Validating a request with `validateOrFail()`, and using only the validated values afterwards
- `RestHandler` answers a failed validation with 400 by default; RealWorld expects 422, so override
  `onValidationException()` in your base handler
- Telling a missing field apart from a field sent as `null` or as an empty string, for partial updates. Without
  null support, `structKeyExists()` treats a `null` field as missing, so turn null support on

**Resources:**

- [cbvalidation overview](https://coldbox-validation.ortusbooks.com/overview) and
  [Valid constraints](https://coldbox-validation.ortusbooks.com/overview/valid-constraints) and
  [Validating with failures](https://coldbox-validation.ortusbooks.com/overview/validating-constraints/validating-with-failures),
  Ortus documentation
- [Input validation](../../../../security/audit/security-audit-reference.md#71-input-validation), in the Techversant
  security audit reference

**Level:** Practitioner · Core

## Error response format

Clients need errors they can read and act on. One format across every endpoint means a client handles errors once.

**What to learn:**

- RealWorld's format: `{"errors": {"<field>": ["<message>"]}}`, with 422 for invalid input
- Techversant's standard error format for client projects, and why it differs
- Turning validation results into the format in one place, not in each handler

**Resources:**
[Error response format](../../../../standards/general/rest-api-best-practices.md#52-error-response-format) and
[validation error examples](../../../../standards/general/rest-api-best-practices.md#7-validation-error-examples), in
the Techversant REST API best practices

**Level:** Practitioner · Core

## Exception handling

CFML (ColdFusion Markup Language) reports problems by throwing exceptions. Handling them in the right place keeps errors
clear for users and useful for developers.

**What to learn:**

- `try`, `catch` and `finally` in script, `<cftry>` and `<cfcatch>` in tags, and throwing your own exception types
  with `throw()`
- How `RestHandler` turns exceptions into JSON responses, such as `EntityNotFound` into a 404
- Turning off the Robust Exception Information setting outside development, so responses never show a
  stack trace or SQL

**Resources:**

- [Handling errors](https://helpx.adobe.com/coldfusion/developing-applications/developing-cfml-applications/handling-errors.html),
  Adobe ColdFusion documentation
- [RestHandler](https://coldbox.ortusbooks.com/digging-deeper/rest-handler), ColdBox documentation
- [Error handling](../../../../standards/coldfusion/coldfusion-style-guide.md#9-error-handling), in the Techversant
  ColdFusion style guide

**Level:** Practitioner · Core

## Logging with LogBox

Logs are how you find out what happened in production. LogBox is ColdBox's logging library.

**What to learn:**

- Getting a logger, log levels, and appenders that write to the console or a file
- Writing JSON log lines that include the request ID
- What must never be logged: passwords, tokens and personal data

**Resources:**

- [Configuring LogBox](https://logbox.ortusbooks.com/configuration/configuring-logbox) and
  [Using a logger object](https://logbox.ortusbooks.com/usage/using-a-logger-object), Ortus documentation
- [What must never be logged](../../../../security/audit/security-audit-reference.md#112-what-must-never-be-logged),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Debugging a request across layers

When a response is wrong, the cause can be in the browser, the handler, the model or the database. Find which one
before you change any code.

**What to learn:**

- Reproducing a problem with an exact request, and following it through the logs with its request ID
- Checking the input, the SQL and the parameters, and the result at each layer
- The cbdebugger module for local development, and keeping it off everywhere else

**Resources:**

- [cbdebugger](https://www.forgebox.io/view/cbdebugger), ForgeBox
- [Debugging](https://learncfinaweek.com/course/index/section/Error_Handling_and_Debugging/item/Debugging.html),
  Learn CF in a Week

**Level:** Practitioner · Core

## Project: Validate Every Request

**Brief:** Add validation for every endpoint that takes input: sign-up, sign-in, updating the user, creating and
updating articles, and adding comments. Return errors in the RealWorld format. Until stage 06, sign-up and sign-in
stop after validation, new articles and comments belong to a seeded user, and `PUT /api/user` updates that user.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Every endpoint that takes input validates it with cbvalidation, and handlers use only validated data
- [ ] Invalid input returns 422 with `{"errors": {"<field>": ["<message>"]}}`. Your own tests use the field names
  and messages from `specs/api/hurl/errors_auth.hurl` and `errors_articles.hurl`; the Hurl files themselves run from
  stage 06, because they sign up first
- [ ] Updates follow the tests: an article updated without `tagList` keeps its tags, `"tagList": []` removes them
  and `"tagList": null` returns 422; `PUT /api/user` rejects `null` for `email`, `username` and `password` and a
  password under 8 characters, saves `"image": null` and keeps fields that were not sent
- [ ] A missing article or profile returns 404 with `errors.<name>` set to `not found`, and no response anywhere
  shows a stack trace, SQL or a file path
- [ ] Updating an article in the same second as creating it changes `updatedAt`
- [ ] Invalid requests without an `Accept` header still get JSON errors
- [ ] Log lines are JSON with the request ID, and a test shows that a password in a request is never logged
- [ ] Tests cover each error case

Previous: [04. Databases and Data Access](./04-databases-and-data-access.md) · Next:
[06. Authentication and Authorization](./06-authentication-and-authorization.md)
