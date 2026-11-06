# 08. Secure Engineering

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Most security flaws come from a few common mistakes in everyday code. This stage covers how to avoid them, and when
to stop and ask for a security review. Back to the [roadmap](./README.md).

## Secrets

Passwords, API keys and tokens in code end up in the repository history, where anyone with access can find them.

**What to learn:**

- Keeping secrets in environment variables or a secrets manager, never in code or committed files
- Committing an example file with placeholder values instead of the real one
- What to do if you commit a secret: tell your lead, rotate it straight away, and do not just delete the line

**Resources:**

- [Keys and secrets management](../../security/audit/security-audit-reference.md#63-keys-and-secrets-management), in
  the Techversant security audit reference
- [Example secrets file](../../standards/git/secrets.env.example), in the Techversant Git standards

**In your stack:** front-end and mobile code ships to the user's device, so anything in it is public. Keep secret
keys on the server only.

**Level:** Foundation · Core

## Injection and output encoding

Injection happens when user input is treated as code, such as SQL or HTML. Parameterized queries and output
encoding stop it.

**What to learn:**

- Parameterized queries or a safe query builder, never strings built from user input
- Encoding output for where it appears, so user input shown in a page cannot run as script
- Why your framework's defaults help, and the functions that bypass them

**Resources:**

- [SQL and data store injection](../../security/audit/security-audit-reference.md#72-sql-and-data-store-injection)
  and [cross-site scripting](../../security/audit/security-audit-reference.md#73-cross-site-scripting-and-output-encoding),
  in the Techversant security audit reference

**In your stack:** in React, avoid `dangerouslySetInnerHTML`; in Vue, avoid `v-html` with user content. In mobile,
treat web views that show user content like a browser.

**Level:** Foundation · Core

## Authorization

Authentication checks who you are; authorization checks what you may do. Checking authorization on every request,
on the server, stops users reaching data that is not theirs.

**What to learn:**

- Checking permissions on the server for every request, not only hiding buttons in the user interface
- Checking access to each record, so changing an ID in the URL does not show someone else's data
- Authentication and authorization code is Red Zone work: written by hand and reviewed by a senior engineer

**Resources:**

- [Authorization](../../security/audit/security-audit-reference.md#31-authorization) and
  [object-level access](../../security/audit/security-audit-reference.md#32-object-level-access-and-idor), in the
  Techversant security audit reference
- [Red Zone](../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the Techversant AI Era
  Coding Guidelines

**Level:** Foundation · Core

## When to ask for a security review

Some changes need more than the everyday checklist. Knowing when to stop and ask is part of the job.

**What to learn:**

- The triggers: sign-in, permissions, sessions, encryption, personal or payment data, file uploads, webhooks and
  user-supplied URLs
- Escalating early, before you build, not after
- Writing a short note on what the change touches and what you are unsure about

**Resources:**

- [Does your change need more than this page?](../../security/audit/security-audit-checklist.md#does-your-change-need-more-than-this-page)
  and [stop and escalate](../../security/audit/security-audit-checklist.md#stop-and-escalate), in the Techversant
  security audit checklist

**Level:** Foundation · Core

## OWASP Top 10

The OWASP Top 10 lists the most critical web application security risks. The Techversant security checklist is
organized around the 2025 edition.

**What to learn:**

- The ten categories, starting with broken access control
- The Techversant minimum bar every pull request must meet
- Using the checklist on your own changes before you ask for review

**Resources:**

- [Security Audit Checklist](../../security/audit/security-audit-checklist.md), including the
  [minimum bar](../../security/audit/security-audit-checklist.md#minimum-bar)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/), OWASP Foundation

**Level:** Foundation · Core

## Project: Security-Review Your Feature

**Brief:** Review your bookmarks feature against the Techversant security checklist, fix what you find, and prove
the app still passes RealWorld's XSS security test.

**Size:** 1–2 days

**Verification**, checked by a senior engineer:

- [ ] The minimum bar items in the security checklist are each marked pass, fail or not applicable, with a reason
- [ ] No secret is in the repository or its history, and settings come from configuration
- [ ] Every query in the feature is parameterized or uses the framework's safe query builder
- [ ] A test proves that changing a bookmark or article ID cannot reach another reader's data
- [ ] RealWorld's `xss-security.spec.ts` end-to-end test passes against your back end and a front end
- [ ] A short note lists which parts of the feature, if any, would need a deeper security review, and why
- [ ] Any finding you could not fix is recorded as an issue with an owner

Previous: [07. Testing and Refactoring](./07-testing-and-refactoring.md) · Next:
[09. Code Review](./09-code-review.md)
