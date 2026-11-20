# 06. Authentication and Authorization

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-20 · **Next review:** 2027-05-20

Authentication checks who a user is. Authorization checks what they may do. Both are Red Zone work at Techversant:
write the code by hand, never with AI tools, and have a senior engineer review it before it merges. Back to the
[roadmap](./README.md).

## Password storage

A stored password must be useless to an attacker who copies the database. That means a slow, salted hash, never
plain text and never a fast hash such as SHA-256.

**What to learn:**

- bcrypt and Argon2id, and why a slow hash protects passwords
- Hashing that works on both engines, such as the BCrypt module from ForgeBox. Lucee has no bcrypt function built
  in. Adobe introduced `PasswordHashGenerate()` and `PasswordHashVerify()` in ColdFusion 2025 Update 8 and
  deprecated `GenerateBCryptHash()` and `VerifyBCryptHash()` in the same update
- Comparing a password only through the hash library's verify function

**Resources:**

- [Password and credential storage](../../../../security/audit/security-audit-reference.md#64-password-and-credential-storage),
  in the Techversant security audit reference
- [BCrypt module](https://github.com/coldbox-modules/bcrypt), ColdBox modules
- [Hash and verify passwords](https://guides.adobe.com/coldfusion/en/docs/introduction-to-coldfusion/__references__/hash-and-verify-passwords-in-coldfusion.html),
  Adobe ColdFusion documentation
- [Deprecated features](https://guides.adobe.com/coldfusion/en/docs/introduction-to-coldfusion/deprecated-features.html),
  Adobe ColdFusion documentation
- [Password storage cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html),
  OWASP (Open Worldwide Application Security Project)

**Level:** Advanced · Core

## API tokens

After sign-in, the client sends a token with every request. RealWorld expects `Authorization: Token <token>`; client
projects use `Authorization: Bearer <token>`.

**What to learn:**

- Creating a long random token with a secure random generator, such as `generateSecretKey("AES", 256)`, never
  `createUUID()` or `rand()`; storing only a hash of it; and giving it an expiry
- Reading the token in one place, such as an interceptor, and loading the signed-in user for the request
- Returning 401 when the token is missing, wrong or expired, and the same answer for each
- JSON Web Tokens (JWT) with cbsecurity's JWT services, and why a signed token is hard to revoke before it expires;
  cbsecurity's JWT services read `Bearer` tokens by default; this project uses an opaque token with RealWorld's
  `Token` prefix, so the token check is your own code

**Resources:**

- [Tokens: JWT, OAuth 2.0 and OIDC](../../../../security/audit/security-audit-reference.md#94-tokens--jwt-oauth-20-oidc),
  in the Techversant security audit reference
- [JWT services](https://coldbox-security.ortusbooks.com/jwt/jwt-services), cbsecurity documentation

**Level:** Advanced · Core

## Rules and permissions with cbsecurity

cbsecurity is ColdBox's security module. It protects routes and handlers with rules, and gives your code one place
to ask who the user is and what they may do.

**What to learn:**

- Security rules and `secured` annotations on handlers and actions, and a custom validator that checks your own
  token and returns the RealWorld 401 body
- The cbsecurity model: checking the signed-in user and their permissions in code
- 401 for a user who is not signed in, and 403 for a signed-in user who is not allowed
- Object-level checks: loading the article and confirming that the user is its author, on every change

**Resources:**

- [Overview](https://coldbox-security.ortusbooks.com/getting-started/overview),
  [Security rules](https://coldbox-security.ortusbooks.com/usage/security-rules) and
  [cbsecurity model](https://coldbox-security.ortusbooks.com/usage/cbsecurity-model), cbsecurity documentation
- [Authorization](../../../../security/audit/security-audit-reference.md#31-authorization) and
  [object-level access](../../../../security/audit/security-audit-reference.md#32-object-level-access-and-idor), in the
  Techversant security audit reference

**Level:** Advanced · Core

## Sessions and cookies

Most older CFML (ColdFusion Markup Language) applications sign users in with sessions and cookies, not tokens. You need
to maintain that code safely.

**What to learn:**

- Session management in `Application.cfc`, the `session` scope, and `this.sessionManagement = false` for an API
  that uses tokens
- Starting a new session after sign-in with `sessionRotate()`, and ending it fully at sign-out with
  `sessionInvalidate()`
- Cookie flags: `HttpOnly`, `Secure` and `SameSite`, and cross-site request forgery (CSRF) protection for forms
  with `csrfGenerateToken()` and `csrfVerifyToken()`

**Resources:**

- [Session management](../../../../security/audit/security-audit-reference.md#93-session-management) and
  [Cross-site request forgery](../../../../security/audit/security-audit-reference.md#35-cross-site-request-forgery-csrf),
  in the Techversant security audit reference

**Level:** Advanced · Optional

## Rate limiting sign-in

Without a limit, an attacker can try thousands of passwords a minute. Rate limiting slows them down.

**What to learn:**

- Limiting sign-in and sign-up attempts by IP address and by account, with the count in a shared cache
- Returning 429 with a `Retry-After` header
- Setting limits that a full RealWorld test run still passes

**Resources:**
[Rate limiting and quotas](../../../../security/audit/security-audit-reference.md#83-rate-limiting-and-quotas), in
the Techversant security audit reference

**Level:** Advanced · Core

## Project: Add Sign-In and Permissions

**Brief:** Add sign-up, sign-in and the current user endpoints with tokens, then follow, favourite and the personal
feed. Switch creating, updating and deleting articles and comments to the signed-in user, with rules for who may
change them. Write all of this code by hand, and have a senior engineer review it before it merges.

**Size:** 4–5 days

**Verification**, checked by a reviewer:

- [ ] Passwords are hashed with bcrypt or Argon2id, no log line contains a password or token, and no response
  contains a password or a stored token hash. `GET` and `PUT /api/user` return the token from the request header
- [ ] Sign-in returns the same error for an unknown email and a wrong password
- [ ] The API accepts `Authorization: Token <token>`, the database stores only hashes of tokens, and tokens expire
  after a configured time
- [ ] Error bodies match the tests: `errors.token` `is missing` for 401, `errors.credentials` `invalid` for a failed
  sign-in, and `errors.article` or `errors.comment` `forbidden` for 403
- [ ] A username or email that is already taken returns 409 with `errors.username` or `errors.email` set to
  `has already been taken`, and deleting a missing comment returns 404 with `errors.comment` `not found`
- [ ] Only an article's author may update or delete it, and only a comment's author may delete it, checked on the
  loaded record
- [ ] Sign-in and sign-up are rate limited, the limit returns 429, and a full test run still passes with the limits on
- [ ] All 13 RealWorld API test files pass
- [ ] A senior engineer has reviewed the sign-in, token and permission code, and the review is linked in the pull
  request

Previous: [05. Validation and Error Handling](./05-validation-and-error-handling.md) · Next:
[07. Background Jobs and Caching](./07-background-jobs-and-caching.md)
