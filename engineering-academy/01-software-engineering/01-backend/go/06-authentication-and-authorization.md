# 06. Authentication and Authorization

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Authentication checks who is calling the API. Authorization checks what they may do. Mistakes here expose client
data, so this whole stage is Red Zone work: write the code by hand, and have a senior engineer review it. Back to the
[roadmap](./README.md).

## Password storage

Passwords are never stored, only a slow, salted hash of them. If the database leaks, the hashes are hard to reverse.

**What to learn:**

- Hashing with Argon2id or bcrypt from `golang.org/x/crypto`, and why fast hashes such as SHA-256 are unsafe
- Argon2id returns only the raw hash: generate the salt with `crypto/rand`, store the salt and settings with the
  hash, and compare with `crypto/subtle.ConstantTimeCompare`. bcrypt does this for you, but rejects passwords over
  72 bytes.
- Returning the same error for an unknown email and a wrong password, and still hashing when the email is unknown,
  so the response time does not reveal which emails exist

**Resources:**

- [Package argon2](https://pkg.go.dev/golang.org/x/crypto/argon2), Go documentation
- [Password and credential storage](../../../../security/audit/security-audit-reference.md#64-password-and-credential-storage),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## JSON Web Tokens

A signed JSON Web Token (JWT) proves who the user is on each request, without a database lookup.

**What to learn:**

- Signing tokens with golang-jwt at sign-in, with a key from configuration, an expiry time, and the user's ID as the
  subject, because usernames and emails can change
- Parsing with `jwt.WithValidMethods` and `jwt.WithExpirationRequired`, so a token cannot choose its own algorithm
  or skip the expiry check
- A middleware that reads RealWorld's `Authorization: Token <token>` header, puts the user ID in the request context,
  and returns 401 with `errors.token` when the token is missing or invalid

**Resources:**

- [golang-jwt](https://pkg.go.dev/github.com/golang-jwt/jwt/v5)
- [Tokens: JWT, OAuth 2.0 and OIDC](../../../../security/audit/security-audit-reference.md#94-tokens--jwt-oauth-20-oidc),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Cookie sign-in for single-page apps

For a Techversant front end, the default is a session in an `HttpOnly` cookie, so no token is ever readable by
browser scripts.

**What to learn:**

- Sessions with a library such as scs, stored in Redis when there is more than one server
- Cross-site request forgery (CSRF) protection with the standard library's `http.CrossOriginProtection`, and the
  cookie's `Secure`, `HttpOnly` and `SameSite` attributes
- When to use cookies and when to use tokens, such as for mobile apps and other servers

**Resources:**

- [scs](https://github.com/alexedwards/scs) and
  [CrossOriginProtection](https://pkg.go.dev/net/http#CrossOriginProtection)
- [Session management](../../../../security/audit/security-audit-reference.md#93-session-management), in the
  Techversant security audit reference

**Level:** Advanced · Core

## Authorization rules

Middleware decides who may call an endpoint. Object-level rules decide whether this user may act on this exact
record.

**What to learn:**

- Two middleware functions: one that requires a user, and one for endpoints that work signed in or out, such as the
  article list, where a missing token is allowed but a bad one is rejected
- Object-level checks in the service, such as "only the author may delete this article", returning a domain error
  that becomes `errors.article` or `errors.comment` `forbidden`
- Returning 403 when a signed-in user may not act, and 401 when nobody is signed in

**Resources:**
[Object-level access](../../../../security/audit/security-audit-reference.md#32-object-level-access-and-idor), in the
Techversant security audit reference

**Level:** Practitioner · Core

## Rate limiting sign-in

Without a limit, an attacker can try thousands of passwords a minute. Rate limiting slows them down.

**What to learn:**

- Rate limiting in memory with `golang.org/x/time/rate` on one server, and in Redis, for example with redis_rate,
  when there are several. In memory, keep one limiter per key in a map guarded by a mutex, and remove idle entries
  so memory does not grow without limit.
- Limiting sign-in by email and IP address together, so one attacker cannot lock out every user
- Returning 429 with a `Retry-After` header, and reading the real client IP behind a proxy, trusting forwarded
  headers only from your own proxy

**Resources:**

- [redis_rate](https://github.com/go-redis/redis_rate)
- [Rate limiting and quotas](../../../../security/audit/security-audit-reference.md#83-rate-limiting-and-quotas), in
  the Techversant security audit reference

**Level:** Practitioner · Core

## Project: Add Sign-In and Permissions

**Brief:** Add sign-up, sign-in and the current user endpoints with JWTs, then follow, favourite and the personal
feed. Switch creating, updating and deleting articles and comments to the signed-in user, with rules for who may
change them. Write all of this code by hand, and have a senior engineer review it before it merges.

**Size:** 4–5 days

**Verification**, checked by a reviewer:

- [ ] Passwords are hashed with Argon2id or bcrypt, no log line contains a password or token, and no response
  contains a password. The user endpoints return the token as the contract requires.
- [ ] Sign-in returns the same error for an unknown email and a wrong password
- [ ] The API accepts `Authorization: Token <token>`, and tokens are signed with a key from configuration, checked
  against the expected signing method, and expire after a configured time
- [ ] Error bodies match the tests: `errors.token` `is missing` for 401, `errors.credentials` `invalid` for a
  failed sign-in, and `errors.article` or `errors.comment` `forbidden` for 403
- [ ] A username or email that is already taken returns 409 with `errors.username` or `errors.email` set to
  `has already been taken`, and deleting a missing comment returns 404 with `errors.comment` `not found`
- [ ] Only an article's author may update or delete it, and only a comment's author may delete it
- [ ] Sign-in and sign-up are rate limited, the limit returns 429, and a full test run still passes with the limits
  on
- [ ] All 13 RealWorld API test files pass
- [ ] A senior engineer has reviewed the sign-in, token, middleware and authorization code, and the review is
  linked in the pull request

Previous: [05. Validation and Error Handling](./05-validation-and-error-handling.md) · Next:
[07. Background Jobs and Caching](./07-background-jobs-and-caching.md)
