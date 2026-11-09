# 06. Authentication and Authorization

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Authentication checks who is calling the API. Authorization checks what they may do. Mistakes here expose client
data, so this whole stage is Red Zone work: write the code by hand, and have a senior engineer review it. Back to the
[roadmap](./README.md).

## Password storage

Passwords are never stored, only a slow, salted hash of them. If the database leaks, the hashes are hard to reverse.

**What to learn:**

- ASP.NET Core Identity's `PasswordHasher`, which uses Password-Based Key Derivation Function 2
  (PBKDF2) with a salt, or Argon2id through a library, and why fast hashes such as SHA-256 are
  unsafe
- Re-hashing a password at sign-in when the hasher reports that its settings have changed
- Returning the same error for an unknown email and a wrong password

**Resources:**

- [Hash passwords](https://learn.microsoft.com/en-us/aspnet/core/security/data-protection/consumer-apis/password-hashing),
  Microsoft Learn
- [Password and credential storage](../../../../security/audit/security-audit-reference.md#64-password-and-credential-storage),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## JWT bearer authentication

A JSON Web Token (JWT) is a signed token that carries the user's ID. ASP.NET Core's JWT bearer handler checks it on
each request and turns it into a signed-in user.

**What to learn:**

- Issuing tokens at sign-in with a key from configuration, an expiry time, and the user's ID as the subject, because
  usernames and emails can change
- `AddJwtBearer` with token validation settings for the issuer, audience, lifetime, signing key and allowed
  algorithms, and how the handler renames standard claims
- Reading RealWorld's `Authorization: Token <token>` header in the `OnMessageReceived` event, because the handler
  expects `Bearer`
- Writing the 401 body with `errors.token` in the `OnChallenge` event, because the handler's own 401 has no body,
  and a JSON 403 in the `OnForbidden` event if you use policies
- A signing key of at least 256 bits, and a short `ClockSkew`, because the default accepts tokens 5 minutes past
  their expiry

**Resources:**

- [Configure JWT bearer authentication](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/configure-jwt-bearer-authentication),
  Microsoft Learn
- [Tokens: JWT, OAuth 2.0 and OIDC](../../../../security/audit/security-audit-reference.md#94-tokens--jwt-oauth-20-oidc),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Cookie sign-in for single-page apps

For a Techversant front end, the default is a session in an `HttpOnly` cookie, so no token is ever readable by
browser scripts.

**What to learn:**

- Cookie authentication, which returns 401 and 403 for API endpoints in ASP.NET Core 10 instead of redirecting
- Cross-site request forgery (CSRF) protection with ASP.NET Core's antiforgery support, and the cookie's `Secure`,
  `HttpOnly` and `SameSite` settings
- When to use cookies and when to use tokens, such as for mobile apps and other servers

**Resources:**

- [Cookie authentication](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/cookie) and
  [antiforgery](https://learn.microsoft.com/en-us/aspnet/core/security/anti-request-forgery), Microsoft Learn
- [Session management](../../../../security/audit/security-audit-reference.md#93-session-management), in the
  Techversant security audit reference

**Level:** Advanced · Core

## Authorization rules

Authorization policies decide who may call an endpoint. Object-level rules decide whether this user may act on this
exact record.

**What to learn:**

- `RequireAuthorization` on route groups, policies, and `AllowAnonymous` for endpoints that work signed in or out
- Why an `AllowAnonymous` endpoint accepts a bad token by default, and returning 401 when a token is sent but fails,
  while still allowing requests with no token
- Object-level checks in the service or with resource-based authorization, such as "only the author may delete this
  article", returning `errors.article` or `errors.comment` `forbidden`
- Returning 403 when a signed-in user may not act, and 401 when nobody is signed in

**Resources:**

- [Resource-based authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/resourcebased),
  Microsoft Learn
- [Object-level access](../../../../security/audit/security-audit-reference.md#32-object-level-access-and-idor), in
  the Techversant security audit reference

**Level:** Practitioner · Core

## Rate limiting sign-in

Without a limit, an attacker can try thousands of passwords a minute. Rate limiting slows them down.

**What to learn:**

- ASP.NET Core's rate limiting middleware, with a partitioned limiter, setting the rejection status to 429, because
  the default is 503, and writing a JSON body in `OnRejected`
- Limiting sign-in by IP address in the middleware, and by email in the sign-in service, for example with a counter
  in the cache, because the middleware runs before the body is read. Combined, one attacker cannot lock out every
  user.
- Keeping counts in a shared store, such as Redis, when there is more than one server, because the built-in
  limiters count in memory
- Returning a `Retry-After` header, and reading the real client IP behind a proxy with the forwarded headers
  middleware, trusting only your own proxy

**Resources:**

- [Rate limiting middleware](https://learn.microsoft.com/en-us/aspnet/core/performance/rate-limit), Microsoft Learn
- [Rate limiting and quotas](../../../../security/audit/security-audit-reference.md#83-rate-limiting-and-quotas), in
  the Techversant security audit reference

**Level:** Practitioner · Core

## Project: Add Sign-In and Permissions

**Brief:** Add sign-up, sign-in and the current user endpoints with JWTs, then follow, favourite and the personal
feed. Switch creating, updating and deleting articles and comments to the signed-in user, with rules for who may
change them. Write all of this code by hand, and have a senior engineer review it before it merges.

**Size:** 4–5 days

**Verification**, checked by a reviewer:

- [ ] Passwords are hashed with Identity's password hasher or Argon2, no log line contains a password or token, and
  no response contains a password. The user endpoints return the token as the contract requires.
- [ ] Sign-in returns the same error for an unknown email and a wrong password
- [ ] The API accepts `Authorization: Token <token>`, and tokens are signed with a key from configuration, checked
  for issuer, audience, algorithm and lifetime, and expire after a configured time
- [ ] Error bodies match the tests: `errors.token` `is missing` for 401, `errors.credentials` `invalid` for a
  failed sign-in, and `errors.article` or `errors.comment` `forbidden` for 403
- [ ] A username or email that is already taken returns 409 with `errors.username` or `errors.email` set to
  `has already been taken`, and deleting a missing comment returns 404 with `errors.comment` `not found`
- [ ] Only an article's author may update or delete it, and only a comment's author may delete it
- [ ] Sign-in and sign-up are rate limited, the limit returns 429, and a full test run still passes with the limits
  on
- [ ] All 13 RealWorld API test files pass
- [ ] A senior engineer has reviewed the authentication setup, sign-in, token and authorization code, and the review
  is linked in the pull request

Previous: [05. Validation and Error Handling](./05-validation-and-error-handling.md) · Next:
[07. Background Jobs and Caching](./07-background-jobs-and-caching.md)
