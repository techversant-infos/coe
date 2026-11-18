# 07. Working with APIs

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-12 · **Next review:** 2027-02-12

A mobile app is usually the front end for an API, used over networks that are slow, change between Wi-Fi and
mobile data, or disappear. This stage connects the whole app to the API, safely. Back to the
[roadmap](./README.md).

## Changing data

Reading data is half the job. Writing articles, comments, follows and favourites changes data on the server, and the
screen must stay in step.

**What to learn:**

- TanStack Query mutations, and refreshing the affected queries after a change
- Optimistic updates, such as showing a favourite straight away and undoing it if the request fails
- Preventing double submits when the user taps twice

**Resources:**
[Optimistic updates](https://tanstack.com/query/latest/docs/framework/react/guides/optimistic-updates), TanStack
Query documentation

**Level:** Practitioner · Core

## Handling API errors

The API returns errors in a fixed shape, and each kind of error needs a different response in the app.

**What to learn:**

- Reading RealWorld's error body, `{"errors": {"field": ["message"]}}`, and showing it on the form
- What 401, 403, 404, 409, 422 and 5xx responses mean, and what the user should see for each, following the
  [practice app](../practice-app.md#behaviour-rules) rules
- Never signing the user out because of a 401, 409 or 422 on a form
- Route error boundaries, so a crash in one screen shows a message and a retry instead of a blank screen

**Resources:**

- [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status), MDN Web Docs
- [Error handling](https://docs.expo.dev/router/error-handling/), Expo Router documentation

**Level:** Practitioner · Core

## Poor and missing networks

Mobile users lose the connection in lifts, trains and basements. The app must say what is happening and recover
when the network returns.

**What to learn:**

- Detecting the connection state, and connecting it to TanStack Query's online manager
- Offline, TanStack Query pauses queries and mutations instead of failing them; show "Unable to connect" when a
  query is paused, and decide whether form submits fail at once
- Timeouts and limited retries, so a request never leaves a screen spinning forever
- Clear "Unable to connect" and "Connecting" states, with a retry button

**Resources:**

- [React Native support](https://tanstack.com/query/latest/docs/framework/react/react-native) and
  [Network mode](https://tanstack.com/query/latest/docs/framework/react/guides/network-mode), TanStack Query
  documentation

**Level:** Practitioner · Core

## Tokens on the device

After sign-in, the API gives the app a token to send with every request. On a phone, the token belongs in the
platform's secure storage. This is Red Zone work: write it by hand, and have a senior engineer review it.

**What to learn:**

- Storing the token with `expo-secure-store`, which uses the Keychain on iOS and storage encrypted with the Android
  Keystore on Android
- Why AsyncStorage and plain files are not safe for tokens
- iOS Keychain items survive the app being deleted, so detect a fresh install with a flag in normal storage and
  delete any old token; choose an accessibility setting such as `WHEN_UNLOCKED_THIS_DEVICE_ONLY` so the token does
  not move to a new device through a backup
- Sending the token as `Authorization: Token <jwt>`, replacing it with the one `PUT /user` returns, and clearing it
  and every cached user query on sign-out
- Keeping the token out of the query cache: the API's user object contains it

**Resources:**

- [SecureStore](https://docs.expo.dev/versions/latest/sdk/securestore/), Expo documentation
- [Tokens: JWT, OAuth 2.0 and OIDC](../../../../security/audit/security-audit-reference.md#94-tokens--jwt-oauth-20-oidc),
  in the Techversant security audit reference
- [Red Zone](../../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the Techversant AI
  Era Coding Guidelines

**Level:** Practitioner · Core

## Rendering user content safely

Article bodies and comments are written by other users. Showing them must never let one user run code or open
harmful links on another user's phone.

**What to learn:**

- Rendering Markdown as native components with a library such as `react-native-marked`, instead of loading HTML into
  a web view
- `react-native-marked` opens every link with the system by default, so pass a custom renderer for links and
  images that opens only `http` and `https` addresses, in an in-app browser
- Deciding whether images in article bodies load at all, because each one is fetched from the reader's phone
- Never passing user text to a web view that can run JavaScript
- Showing plain text for comments, so markup appears as text

**Resources:**
[Cross-site scripting and output encoding](../../../../security/audit/security-audit-reference.md#73-cross-site-scripting-and-output-encoding),
in the Techversant security audit reference

**Level:** Practitioner · Core

## Configuration and environments

The app needs the API address, and different builds may point at different servers. Anything built into the app can
be read by anyone who downloads it.

**What to learn:**

- Environment variables starting with `EXPO_PUBLIC_`, which are built into the app as plain text
- Never putting a secret, such as a private API key, in the app; secrets stay on a server
- Separate settings for development, preview and production builds

**Resources:** [Environment variables](https://docs.expo.dev/guides/environment-variables/), Expo documentation

**Level:** Practitioner · Core

## Project: Connect to the API and Sign In

**Brief:** Make the whole app work against the RealWorld API: sign-up, sign-in and sign-out, writing and editing
articles, comments, following and favourites. Follow every rule on the [practice app](../practice-app.md) page.
Write the sign-in and token code by hand, and have a senior engineer review it.

**Size:** 4–5 days

**Verification**, checked by a reviewer:

- [ ] Every screen loads its data with TanStack Query, and shows loading, empty and error states
- [ ] Favouriting, following, commenting and deleting update the screen at once and roll back when the request fails
- [ ] The token is stored only with `expo-secure-store`, sent as `Authorization: Token <jwt>`, and removed with all
  cached user data on sign-out
- [ ] When the app starts, a 401 or 403 for the current user signs the app out; any other response, or no response,
  keeps the token and shows "Connecting" with a retry
- [ ] A 401 on a request other than a form submit signs the user out on the same screen and says the session ended
- [ ] A failed form submit stays on the form with the API's errors, and a 401, 409 or 422 never signs the user out;
  a network failure shows "Unable to connect"
- [ ] A 404, a 500 or a network failure on an article or profile still shows the screen, with an error and a retry
- [ ] Edit and delete buttons appear only on the signed-in user's own articles and comments
- [ ] The empty Your Feed says "Your feed is empty"
- [ ] Article bodies render Markdown as native components, and a test shows that `tel:`, `javascript:` and
  custom-scheme links do nothing
- [ ] A fresh install removes any token left in the Keychain by an earlier install
- [ ] The temporary signed-in switch from stage 05 is gone
- [ ] The API address comes from configuration, and no secret is built into the app
- [ ] A senior engineer has reviewed the sign-in and token code, and the review is linked in the pull request

Previous: [06. Forms and Input](./06-forms-and-input.md) · Next: [08. Device Features](./08-device-features.md)
