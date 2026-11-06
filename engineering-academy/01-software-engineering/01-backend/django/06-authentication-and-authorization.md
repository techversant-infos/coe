# 06. Authentication and Authorization

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Authentication checks who is calling the API. Authorization checks what they may do. Mistakes here expose client
data, so this whole stage is Red Zone work: write the code by hand, and have a senior engineer review it. Back to the
[roadmap](./README.md).

## Password storage

Django never stores passwords, only a slow, salted hash of them. If the database leaks, the hashes are hard to
reverse.

**What to learn:**

- Django's password hashers, and putting Argon2 first in `PASSWORD_HASHERS`
- `set_password` and `check_password`, and Django's password validators
- Returning the same error for an unknown email and a wrong password

**Resources:**

- [Password management](https://docs.djangoproject.com/en/6.1/topics/auth/passwords/), Django documentation
- [Password and credential storage](../../../../security/audit/security-audit-reference.md#64-password-and-credential-storage),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## API tokens

The API issues a token at sign-in and checks it on each request. DRF's built-in tokens are stored as plain text and
never expire, so this path uses django-rest-knox, which stores only a hash of each token and lets tokens expire.

**What to learn:**

- Issuing a token at sign-up and sign-in, and checking it with knox's authentication class
- The `Authorization: Token <token>` header, which knox and RealWorld both use
- Listing knox's authentication class first in `DEFAULT_AUTHENTICATION_CLASSES`, because DRF uses the first class
  to decide between 401 and 403
- Token expiry, deleting tokens on sign-out, and why a stolen token stays valid until it expires
- Turning DRF's authentication errors into 401 with `errors.token`, and letting routes that work signed in or out,
  such as the article list, accept a missing token but reject a bad one

**Resources:**

- [django-rest-knox](https://django-commons.org/django-rest-knox/)
- [Authentication](https://www.django-rest-framework.org/api-guide/authentication/), DRF documentation
- [Tokens: JWT, OAuth 2.0 and OIDC](../../../../security/audit/security-audit-reference.md#94-tokens--jwt-oauth-20-oidc),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Cookie sign-in for single-page apps

For a Techversant front end on the same site, the default is Django's session cookie, so no token is ever readable
by browser scripts.

**What to learn:**

- DRF's `SessionAuthentication`, and why it requires a cross-site request forgery (CSRF)
  token on every change
- Session cookie settings: `SESSION_COOKIE_SECURE`, `SESSION_COOKIE_HTTPONLY` and `SESSION_COOKIE_SAMESITE`, and
  CSRF trusted origins
- When to use cookies and when to use tokens, such as for mobile apps and other servers

**Resources:**

- [How to use sessions](https://docs.djangoproject.com/en/6.1/topics/http/sessions/) and
  [CSRF protection](https://docs.djangoproject.com/en/6.1/ref/csrf/), Django documentation
- [Session management](../../../../security/audit/security-audit-reference.md#93-session-management),
  in the Techversant security audit reference

**Level:** Advanced · Core

## Permission classes

Authorization rules belong in permission classes, not scattered through views. A permission class can check the
request, and the exact object it acts on.

**What to learn:**

- `IsAuthenticated` and `IsAuthenticatedOrReadOnly`, and writing your own class with `has_object_permission`
- Object-level checks: always confirming the user may act on this exact record, such as "only the author may delete
  this article"
- Returning 403 when a signed-in user may not act, and 401 when nobody is signed in

**Resources:**

- [Permissions](https://www.django-rest-framework.org/api-guide/permissions/), DRF documentation
- [Authorization](../../../../security/audit/security-audit-reference.md#31-authorization) and
  [object-level access](../../../../security/audit/security-audit-reference.md#32-object-level-access-and-idor), in
  the Techversant security audit reference

**Level:** Practitioner · Core

## Rate limiting sign-in

Without a limit, an attacker can try thousands of passwords a minute. Rate limiting slows them down.

**What to learn:**

- DRF throttling with `ScopedRateThrottle`, and rates set in settings
- A custom throttle that limits sign-in by email and IP address together, so one attacker cannot lock out every user
- Returning 429 with a `Retry-After` header

**Resources:**

- [Throttling](https://www.django-rest-framework.org/api-guide/throttling/), DRF documentation
- [Rate limiting and quotas](../../../../security/audit/security-audit-reference.md#83-rate-limiting-and-quotas),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Project: Add Sign-In and Permissions

**Brief:** Add sign-up, sign-in and the current user endpoints with knox tokens, then follow, favourite and the
personal feed. Switch creating, updating and deleting articles and comments to the signed-in user, with rules for
who may change them. Write all of this code by hand, and have a senior engineer review it before it merges.

**Size:** 4–5 days

**Verification**, checked by a reviewer:

- [ ] Passwords are hashed with Argon2, no log line contains a password or token, and no response contains a
  password or a stored token hash. `GET` and `PUT /api/user` return the token from the request header.
- [ ] Sign-in returns the same error for an unknown email and a wrong password
- [ ] The API accepts `Authorization: Token <token>`, the database stores only hashes of tokens, and tokens expire
  after a configured time
- [ ] Error bodies match the tests: `errors.token` `is missing` for 401, `errors.credentials` `invalid` for a
  failed sign-in, and `errors.article` or `errors.comment` `forbidden` for 403
- [ ] A username or email that is already taken returns 409 with `errors.username` or `errors.email` set to
  `has already been taken`, and deleting a missing comment returns 404 with `errors.comment` `not found`
- [ ] Only an article's author may update or delete it, and only a comment's author may delete it, through permission
  classes
- [ ] Sign-in and sign-up are rate limited, the limit returns 429, and a full test run still passes with the limits
  on
- [ ] All 13 RealWorld API test files pass
- [ ] A senior engineer has reviewed the sign-in, token and permission code, and the review is linked in the pull
  request

Previous: [05. Validation and Error Handling](./05-validation-and-error-handling.md) · Next:
[07. Background Jobs and Caching](./07-background-jobs-and-caching.md)
