# 07. Working with APIs

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Almost every screen in a client project shows data from an API, or sends data to one. This stage covers loading
data well, handling every error the API returns, and keeping the sign-in token safe. Back to the
[roadmap](./README.md).

## Fetching data and loading states

Every request can be slow, fail or return nothing. The user should always see which of these happened.

**What to learn:**

- Showing loading, success, empty and error states for every request
- Cancelling a request when the user leaves the page, with `AbortController`
- Why fetching inside `useEffect` gets complicated, and which tools solve it

**Resources:** [Fetching data with effects](https://react.dev/reference/react/useEffect#fetching-data-with-effects),
React documentation

**Level:** Practitioner · Core

## Server state with TanStack Query

Data from the server is not like other state: it can go out of date and must be fetched again. TanStack Query caches
it, refreshes it, and tracks loading and errors for you.

**What to learn:**

- Queries with `useQuery`, and choosing query keys, such as `['articles', { tag, page }]`
- Mutations with `useMutation`, and refreshing related queries after a change
- Optimistic updates, such as showing a favourite straight away and undoing it if the request fails

**Resources:**

- [TanStack Query overview](https://tanstack.com/query/latest/docs/framework/react/overview)
- [Optimistic updates](https://tanstack.com/query/latest/docs/framework/react/guides/optimistic-updates)

**Level:** Practitioner · Core

## Handling API errors

APIs return errors in an agreed format, so the front end can show the right message. Techversant APIs follow one
standard error format; the RealWorld API uses its own, with a list of messages under each key.

**What to learn:**

- Telling apart validation errors (422), conflicts such as an email already in use (409), authentication errors
  (401), permission errors (403), missing items (404) and server errors (5xx)
- Showing field errors next to the field, and general errors in one place
- Treating a 401 at sign-in as a form error (wrong email or password), and a 401 elsewhere as a session that is no
  longer valid
- Telling a rejected session (4xx) apart from a server that is down (5xx or no response): sign out for the first,
  and keep the user signed in and offer to retry for the second

**Resources:**
[Error response format](../../../../standards/general/rest-api-best-practices.md#52-error-response-format), in the
Techversant REST API best practices

**Level:** Practitioner · Core

## Rendering user content safely

Article bodies are written in Markdown by users, so the HTML made from them can carry a cross-site scripting
(XSS) attack. The RealWorld tests try several.

**What to learn:**

- Turning Markdown into HTML with a library such as marked, and cleaning it with DOMPurify before
  `dangerouslySetInnerHTML`
- Why React escapes text by default, so only HTML you insert yourself is a risk
- Never inserting HTML that has not been cleaned, even from your own API

**Resources:**
[Cross-site scripting and output encoding](../../../../security/audit/security-audit-reference.md#73-cross-site-scripting-and-output-encoding),
in the Techversant security audit reference

**Level:** Practitioner · Core

## Tokens in the browser

After sign-in, the API gives the app a token to send with every request. Where you keep it decides who else can read
it. This is Red Zone work: write it by hand, and have a senior engineer review it.

> **Practice only:** the RealWorld test contract stores the token in `localStorage` under the `jwtToken` key. Follow
> it in this stage so the tests can run, and move it to an httpOnly cookie in stage 08. See the
> [practice app](../practice-app.md#practice-only-parts-of-the-contract) page.

**What to learn:**

- Sending the token with each request, as the API expects; RealWorld uses `Authorization: Token <jwt>`
- Why `localStorage` is readable by any script on the page, including a script injected through cross-site
  scripting (XSS)
- Why Techversant's default for client work is an httpOnly cookie, set by the back end, often Laravel Sanctum
- Clearing every trace of the token and the user's data on sign-out

**Resources:**

- [Tokens: JWT, OAuth 2.0 and OIDC](../../../../security/audit/security-audit-reference.md#94-tokens--jwt-oauth-20-oidc)
  and [Session management](../../../../security/audit/security-audit-reference.md#93-session-management), in the
  Techversant security audit reference
- [Red Zone](../../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the Techversant AI
  Era Coding Guidelines

**Level:** Practitioner · Core

## CORS

Browsers block a page from reading responses from another origin unless the API allows it. Cross-Origin Resource
Sharing (CORS) is how the API says which origins it allows.

**What to learn:**

- What an origin is, and why `localhost:5173` calling `localhost:3000` is a cross-origin request
- Preflight requests, and why credentials need extra settings on both sides
- Why the fix belongs in the API's settings, never in turning off browser security

**Resources:**

- [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS), MDN
- [CORS](../../../../security/audit/security-audit-reference.md#43-cors), in the Techversant security audit
  reference

**Level:** Practitioner · Core

## Project: Connect to the API and Sign In

**Brief:** Make the whole app work against the RealWorld API: sign-up, sign-in and sign-out, writing and
editing articles, comments, following and favourites. Load and change data with TanStack Query. Write the sign-in
and token code by hand, and have a senior engineer review it.

**Size:** 4–5 days

**Verification**, checked by a reviewer:

- [ ] Every page loads its data with TanStack Query, and shows loading, empty and error states
- [ ] Favouriting, following, commenting and deleting update the page without a full reload, and roll back when the
  request fails
- [ ] Sign-in stores the token as the contract requires, sends it as `Authorization: Token <jwt>`, and sign-out
  removes it and clears cached user data
- [ ] When the app starts and loading the current user returns a 4xx error, it clears the token and shows the
  signed-out pages. On a 5xx error or no response, it keeps the token and shows a "Connecting" message, as
  `user-fetch-errors.spec.ts` expects.
- [ ] The app exposes `window.__conduit_debug__`, as `specs/e2e/helpers/debug.ts` describes, in development and
  test builds only
- [ ] The edit and delete buttons appear only on the signed-in user's own articles and comments
- [ ] Sign-in and sign-up go to `/`, the editor and settings save, Update Settings goes to `/profile/:username`, and the
  settings form opens with the user's current values
- [ ] A failed form submit stays on the form and shows `.error-messages`: a 400 or 401 shows the API's errors without
  signing the user out, and a network failure shows "Unable to connect"
- [ ] A 404, a 500 or a network failure on an article or profile still renders `.article-page` or `.profile-page`, with
  an error message
- [ ] Reloading `/settings` while signed in stays on `/settings`, because the guard waits for the current user to
  load before it redirects
- [ ] The empty Your Feed says "Your feed is empty", and the article body renders Markdown that is cleaned before
  it reaches the page, so the RealWorld XSS tests pass
- [ ] A senior engineer has reviewed the sign-in and token code, and the review is linked in the pull request
- [ ] The RealWorld end-to-end tests run in `spa` mode against the public demo API, and the pull request records
  how many ran, passed, failed and were skipped

Previous: [06. Forms and Validation](./06-forms-and-validation.md) · Next:
[08. Rendering and the Meta-Framework](./08-rendering-and-the-meta-framework.md)
