# 06. Authentication and Authorization

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Authentication checks who is calling the API. Authorization checks what they may do. Mistakes here expose client
data, so this whole stage is Red Zone work: write the code by hand, and have a senior engineer review it. Back to the
[roadmap](./README.md).

## Password storage

Passwords are never stored, only a slow, salted hash of them. If the database leaks, the hashes are hard to reverse.

**What to learn:**

- Hashing with Argon2id or bcrypt, for example with the `argon2` package, and why fast hashes such as SHA-256 are
  unsafe
- Hashing off the main thread, so sign-ins do not block other requests
- Returning the same error for an unknown email and a wrong password

**Resources:**
[Password and credential storage](../../../../security/audit/security-audit-reference.md#64-password-and-credential-storage),
in the Techversant security audit reference

**Level:** Practitioner · Core

## JSON Web Tokens

A JSON Web Token (JWT) is a signed token that carries the user's ID. The API checks the signature on each request
without a database lookup, so a token cannot be revoked early: keep its lifetime short.

**What to learn:**

- Signing and checking tokens with `@fastify/jwt`, with a secret from configuration and an expiry time
- Checking the issuer and audience, and never accepting unsigned tokens
- Accepting RealWorld's `Authorization: Token <token>` header instead of the standard `Bearer` scheme, with
  `@fastify/jwt`'s `extractToken` option
- Turning every `@fastify/jwt` error into 401 with `errors.token`: it reports a missing token as 400 by default
- Routes that work signed in or out, such as the article list: call `request.jwtVerify()` only when an
  `Authorization` header is present, so a missing token is allowed but a bad one is not

**Resources:**

- [@fastify/jwt](https://github.com/fastify/fastify-jwt)
- [Tokens: JWT, OAuth 2.0 and OIDC](../../../../security/audit/security-audit-reference.md#94-tokens--jwt-oauth-20-oidc),
  in the Techversant security audit reference
- [Security](../../../../standards/nodejs/nodejs-typescript-style-guide.md#12-security), in the Techversant Node.js
  and TypeScript style guide

**Level:** Practitioner · Core

## Cookie sign-in for single-page apps

For a Techversant front end, the default is a session in an `HttpOnly` cookie, so no token is ever readable by
browser scripts.

**What to learn:**

- Setting a session cookie with `@fastify/cookie`, with the `Secure`, `HttpOnly` and `SameSite` attributes
- Protecting cookie-based requests from cross-site request forgery (CSRF), for example with
  `@fastify/csrf-protection`
- When to use cookies and when to use tokens, such as for mobile apps and other servers

**Resources:**

- [Session management](../../../../security/audit/security-audit-reference.md#93-session-management) and
  [CSRF](../../../../security/audit/security-audit-reference.md#35-cross-site-request-forgery-csrf), in the
  Techversant security audit reference

**Level:** Advanced · Core

## Authorization checks

Authorization rules belong in the service layer, in one place per rule, not scattered through handlers.

**What to learn:**

- An `onRequest` hook that requires a signed-in user on protected routes, so a request with no token gets 401
  before its body is validated
- Object-level checks: always confirming the user may act on this exact record, such as "only the author may delete
  this article"
- Returning 403 when a signed-in user may not act, and 401 when nobody is signed in

**Resources:**

- [Authorization](../../../../security/audit/security-audit-reference.md#31-authorization) and
  [object-level access](../../../../security/audit/security-audit-reference.md#32-object-level-access-and-idor), in
  the Techversant security audit reference

**Level:** Practitioner · Core

## Rate limiting sign-in

Without a limit, an attacker can try thousands of passwords a minute. Rate limiting slows them down.

**What to learn:**

- `@fastify/rate-limit`, with limits for sign-in and sign-up set in configuration
- Limiting sign-in by email and IP address together, so one attacker cannot lock out every user. The limit runs
  before the body is read by default, so set `hook: 'preHandler'` on the sign-in route to use the email.
- Returning 429 with a `Retry-After` header

**Resources:**

- [@fastify/rate-limit](https://github.com/fastify/fastify-rate-limit)
- [Rate limiting and quotas](../../../../security/audit/security-audit-reference.md#83-rate-limiting-and-quotas), in
  the Techversant security audit reference

**Level:** Practitioner · Core

## Project: Add Sign-In and Permissions

**Brief:** Add sign-up, sign-in and the current user endpoints with JWTs, then follow, favourite and the personal
feed. Switch creating, updating and deleting articles and comments to the signed-in user, with rules for who may
change them. Write all of this code by hand, and have a senior engineer review it before it merges.

**Size:** 4–5 days

**Verification**, checked by a reviewer:

- [ ] Passwords are hashed with Argon2id or bcrypt, and no response or log line ever contains a password or token
- [ ] Sign-in returns the same error for an unknown email and a wrong password
- [ ] The API accepts `Authorization: Token <token>`, and tokens are signed with a secret from configuration and
  expire after a configured time
- [ ] Error bodies match the tests: `errors.token` `is missing` for 401, `errors.credentials` `invalid` for a
  failed sign-in, and `errors.article` or `errors.comment` `forbidden` for 403
- [ ] A username or email that is already taken returns 409 with `errors.username` or `errors.email` set to
  `has already been taken`, and deleting a missing comment returns 404 with `errors.comment` `not found`
- [ ] Only an article's author may update or delete it, and only a comment's author may delete it
- [ ] Sign-in and sign-up are rate limited, the limit returns 429, and a full test run still passes with the limits
  on
- [ ] All 13 RealWorld API test files pass
- [ ] A senior engineer has reviewed the sign-in, token and authorization code, and the review is linked in the pull
  request

Previous: [05. Validation and Error Handling](./05-validation-and-error-handling.md) · Next:
[07. Background Jobs and Caching](./07-background-jobs-and-caching.md)
