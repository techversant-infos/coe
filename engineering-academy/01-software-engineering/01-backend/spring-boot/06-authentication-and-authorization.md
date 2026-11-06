# 06. Authentication and Authorization

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Authentication checks who is calling the API. Authorization checks what they may do. Mistakes here expose client
data, so this whole stage is Red Zone work: write the code by hand, and have a senior engineer review it. Back to the
[roadmap](./README.md).

## Password storage

Passwords are never stored, only a slow, salted hash of them. If the database leaks, the hashes are hard to reverse.

**What to learn:**

- Spring Security's `PasswordEncoder`, with Argon2 or bcrypt, and why fast hashes such as SHA-256 are unsafe
- The delegating encoder, which records the algorithm with each hash so it can change later
- Returning the same error for an unknown email and a wrong password

**Resources:**

- [Password storage](https://docs.spring.io/spring-security/reference/features/authentication/password-storage.html),
  Spring Security documentation
- [Password and credential storage](../../../../security/audit/security-audit-reference.md#64-password-and-credential-storage),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Spring Security and JSON Web Tokens

Spring Security runs as a chain of filters in front of your controllers. Its resource server support checks a
signed JSON Web Token (JWT) on each request.

**What to learn:**

- A `SecurityFilterChain` bean: which paths are open, which need a user, and turning off what a token API does not
  use: form sign-in, HTTP Basic, CSRF protection and server sessions. Cookie sign-in, below, keeps CSRF protection
  on.
- Signing tokens at sign-in with a `JwtEncoder`, and checking them with a `JwtDecoder` bean. With a shared secret,
  set the HS256 algorithm in the token header and use a key of at least 256 bits from configuration.
- An expiry time on every token, and the user's ID as the subject, because usernames and emails can change
- A custom `BearerTokenResolver` that reads RealWorld's `Authorization: Token <token>` header instead of `Bearer`
- An `AuthenticationEntryPoint` that returns 401 with `errors.token`, set for both missing and bad tokens, and an
  `AccessDeniedHandler` that returns a JSON 403
- Throwing a domain exception from the service for `errors.article` or `errors.comment` `forbidden`, and making
  sure a catch-all exception handler does not swallow Spring Security's own exceptions

**Resources:**

- [OAuth 2.0 resource server JWT](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/jwt.html),
  Spring Security documentation
- [Tokens: JWT, OAuth 2.0 and OIDC](../../../../security/audit/security-audit-reference.md#94-tokens--jwt-oauth-20-oidc),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Cookie sign-in for single-page apps

For a Techversant front end, the default is a session in an `HttpOnly` cookie, so no token is ever readable by
browser scripts.

**What to learn:**

- Session-based sign-in with Spring Security, and storing sessions in Redis with Spring Session when there is more
  than one server
- Cross-site request forgery (CSRF) protection for cookie-based requests, and the cookie's `Secure`, `HttpOnly` and
  `SameSite` attributes
- When to use cookies and when to use tokens, such as for mobile apps and other servers

**Resources:**

- [CSRF](https://docs.spring.io/spring-security/reference/servlet/exploits/csrf.html), Spring Security
  documentation
- [Session management](../../../../security/audit/security-audit-reference.md#93-session-management), in the
  Techversant security audit reference

**Level:** Advanced · Core

## Authorization rules

Path rules in the filter chain decide who may call an endpoint. Object-level rules decide whether this user may act
on this exact record.

**What to learn:**

- Path rules in `authorizeHttpRequests`, and method security with `@PreAuthorize`
- Rule order: `GET /api/articles/feed` needs a user, so its rule comes before the rule that opens
  `GET /api/articles/**`, and `/error` stays open so error responses keep their status
- Object-level checks in the service, such as "only the author may delete this article"
- Endpoints that work signed in or out, such as the article list, where a missing token is allowed but a bad one is
  rejected
- Returning 403 when a signed-in user may not act, and 401 when nobody is signed in

**Resources:**

- [Authorize HTTP requests](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html),
  Spring Security documentation
- [Object-level access](../../../../security/audit/security-audit-reference.md#32-object-level-access-and-idor), in
  the Techversant security audit reference

**Level:** Practitioner · Core

## Rate limiting sign-in

Without a limit, an attacker can try thousands of passwords a minute. Rate limiting slows them down.

**What to learn:**

- Rate limiting with a library such as Bucket4j, with limits set in configuration
- Limiting sign-in by email and IP address together, so one attacker cannot lock out every user
- Returning 429 with a `Retry-After` header
- Reading the real client IP behind a proxy with `server.forward-headers-strategy`, trusting only your own proxy

**Resources:**

- [Bucket4j](https://bucket4j.com/)
- [Rate limiting and quotas](../../../../security/audit/security-audit-reference.md#83-rate-limiting-and-quotas), in
  the Techversant security audit reference

**Level:** Practitioner · Core

## Project: Add Sign-In and Permissions

**Brief:** Add sign-up, sign-in and the current user endpoints with JWTs, then follow, favourite and the personal
feed. Switch creating, updating and deleting articles and comments to the signed-in user, with rules for who may
change them. Write all of this code by hand, and have a senior engineer review it before it merges.

**Size:** 4–5 days

**Verification**, checked by a reviewer:

- [ ] Passwords are hashed with Argon2 or bcrypt, no log line contains a password or token, and no response contains
  a password. The user endpoints return the token as the contract requires.
- [ ] Sign-in returns the same error for an unknown email and a wrong password
- [ ] The API accepts `Authorization: Token <token>`, and tokens are signed with a key from configuration and expire
  after a configured time
- [ ] Error bodies match the tests: `errors.token` `is missing` for 401, `errors.credentials` `invalid` for a
  failed sign-in, and `errors.article` or `errors.comment` `forbidden` for 403
- [ ] A username or email that is already taken returns 409 with `errors.username` or `errors.email` set to
  `has already been taken`, and deleting a missing comment returns 404 with `errors.comment` `not found`
- [ ] Only an article's author may update or delete it, and only a comment's author may delete it
- [ ] Sign-in and sign-up are rate limited, the limit returns 429, and a full test run still passes with the limits
  on
- [ ] All 13 RealWorld API test files pass
- [ ] A senior engineer has reviewed the security configuration, sign-in, token and authorization code, and the
  review is linked in the pull request

Previous: [05. Validation and Error Handling](./05-validation-and-error-handling.md) · Next:
[07. Background Jobs and Caching](./07-background-jobs-and-caching.md)
