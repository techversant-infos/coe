# 06. Authentication and Authorization

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Authentication checks who is calling the API. Authorization checks what they may do. Mistakes here expose client
data, so this whole stage is Red Zone work: write the code by hand, and have a senior engineer review it. Back to the
[roadmap](./README.md).

## Password storage

Passwords are never stored, only a slow, salted hash of them. If the database leaks, the hashes are hard to reverse.

**What to learn:**

- Hashing with Laravel's `Hash` facade, and why bcrypt or Argon2id are used instead of fast hashes such as SHA-256
- Checking a password with `Hash::check`, and rehashing when the settings change
- Returning the same error for an unknown email and a wrong password

**Resources:**

- [Hashing](https://laravel.com/docs/13.x/hashing), Laravel documentation
- [Password and credential storage](../../../../security/audit/security-audit-reference.md#64-password-and-credential-storage),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## API tokens with Sanctum

Laravel Sanctum issues API tokens and checks them on each request. It stores only a hash of each token, so a
database leak does not reveal working tokens.

**What to learn:**

- Issuing a token at sign-up and sign-in, and protecting routes with the `auth:sanctum` middleware
- Reading the signed-in user on protected routes with `$request->user()`
- Token expiry, revoking tokens on sign-out, and pruning expired tokens
- Accepting RealWorld's `Authorization: Token <token>` header instead of the standard `Bearer` scheme, for example
  with `Sanctum::getAccessTokenFromRequestUsing()` in a service provider
- Routes that work signed in or out, such as the article list: no `auth:sanctum` middleware, and the user read
  with `$request->user('sanctum')`

**Resources:**

- [Sanctum](https://laravel.com/docs/13.x/sanctum), Laravel documentation
- [Tokens: JWT, OAuth 2.0 and OIDC](../../../../security/audit/security-audit-reference.md#94-tokens--jwt-oauth-20-oidc),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Cookie sign-in for single-page apps

For a Techversant front end on the same site, Sanctum's cookie-based sign-in is the default: Laravel owns the
session, and no token is ever stored in the browser.

**What to learn:**

- How Sanctum's single-page app sign-in uses session cookies and CSRF protection
- Setting stateful domains, the session cookie's `Secure`, `HttpOnly` and `SameSite` attributes, and CORS with
  credentials
- When to use cookies and when to use tokens, such as for mobile apps and other servers

**Resources:**

- [SPA authentication](https://laravel.com/docs/13.x/sanctum#spa-authentication), Laravel documentation
- [Session management](../../../../security/audit/security-audit-reference.md#93-session-management) and
  [CSRF](../../../../security/audit/security-audit-reference.md#35-cross-site-request-forgery-csrf), in the
  Techversant security audit reference

**Level:** Advanced · Core

## Policies and gates

Authorization rules belong in one place, not scattered through controllers. A policy holds the rules for one model,
such as "only the author may delete an article".

**What to learn:**

- Writing policies, and checking them with `Gate::authorize`, the `can` middleware or the `#[Authorize]` attribute
- Object-level checks: always confirming the user may act on this exact record, not only on records of this type
- Returning 403 when a signed-in user may not act, and 401 when nobody is signed in

**Resources:**

- [Authorization](https://laravel.com/docs/13.x/authorization), Laravel documentation
- [Authorization](../../../../security/audit/security-audit-reference.md#31-authorization) and
  [object-level access](../../../../security/audit/security-audit-reference.md#32-object-level-access-and-idor), in
  the Techversant security audit reference

**Level:** Practitioner · Core

## Rate limiting sign-in

Without a limit, an attacker can try thousands of passwords a minute. Rate limiting slows them down.

**What to learn:**

- Defining rate limiters for sign-in and sign-up, with limits set in configuration
- Limiting sign-in by email and IP address together, so one attacker cannot lock out every user
- Returning 429 with a `Retry-After` header

**Resources:**

- [Rate limiting](https://laravel.com/docs/13.x/routing#rate-limiting), Laravel documentation
- [Rate limiting and quotas](../../../../security/audit/security-audit-reference.md#83-rate-limiting-and-quotas), in
  the Techversant security audit reference

**Level:** Practitioner · Core

## Project: Add Sign-In and Permissions

**Brief:** Add sign-up, sign-in and the current user endpoints with Sanctum tokens, then follow, favourite and the
personal feed. Switch creating, updating and deleting articles and comments to the signed-in user, with rules for
who may change them. Write all of this code by hand, and have a senior engineer review it before it merges.

**Size:** 4–5 days

**Verification**, checked by a reviewer:

- [ ] Passwords are hashed with bcrypt or Argon2id, and no response or log line ever contains a password or token
- [ ] Sign-in returns the same error for an unknown email and a wrong password
- [ ] The API accepts `Authorization: Token <token>`, the database stores only hashes of tokens, and tokens expire
  after a configured time
- [ ] Error bodies match the tests: `errors.token` `is missing` for 401, `errors.credentials` `invalid` for a
  failed sign-in, and `errors.article` or `errors.comment` `forbidden` for 403
- [ ] Only an article's author may update or delete it, and only a comment's author may delete it, through policies
- [ ] Sign-in and sign-up are rate limited, the limit returns 429, and a full test run still passes with the limits
  on
- [ ] All 13 RealWorld API test files pass
- [ ] A senior engineer has reviewed the sign-in, token and policy code, and the review is linked in the pull request

Previous: [05. Validation and Error Handling](./05-validation-and-error-handling.md) · Next:
[07. Background Jobs and Caching](./07-background-jobs-and-caching.md)
