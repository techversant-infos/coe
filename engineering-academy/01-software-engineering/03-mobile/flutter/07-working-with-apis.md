# 07. Working with APIs

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-12 · **Next review:** 2027-02-12

A mobile app is usually the front end for an API, used over networks that are slow, change between Wi-Fi and mobile
data, or disappear. This stage connects the whole app to the API, safely. Back to the [roadmap](./README.md).

## Changing data

Reading data is half the job. Writing articles, comments, follows and favourites changes data on the server, and
every screen must stay in step.

**What to learn:**

- Sending changes through the repository, then invalidating the affected cached data
- Optimistic updates, such as showing a favourite straight away and undoing it if the request fails
- Preventing double submits when the user taps twice

**Resources:** [Optimistic state](https://docs.flutter.dev/app-architecture/design-patterns/optimistic-state),
Flutter documentation

**Level:** Practitioner · Core

## Handling API errors

The API returns errors in a fixed shape, and each kind of error needs a different response in the app.

**What to learn:**

- Reading RealWorld's error body, `{"errors": {"field": ["message"]}}`, into a typed error and showing it on the form
- What 401, 403, 404, 409, 422 and 5xx responses mean, and what the user should see for each, following the
  [practice app](../practice-app.md#behaviour-rules) rules
- Never signing the user out because of a 401, 409 or 422 on a form

**Resources:** [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status), MDN Web
Docs

**Level:** Practitioner · Core

## Poor and missing networks

Mobile users lose the connection in lifts, trains and basements. The app must say what is happening and recover
when the network returns.

**What to learn:**

- Timeouts on every request, so a screen never spins forever, and automatic retries for GET requests only; the user
  retries a failed write, so an article or comment is never created twice
- `connectivity_plus`, and why it reports the type of connection, not whether the API can be reached
- Clear "Unable to connect" and "Connecting" states, with a retry button, and reloading when the network returns

**Resources:** [connectivity_plus](https://pub.dev/packages/connectivity_plus), pub.dev

**Level:** Practitioner · Core

## Tokens on the device

After sign-in, the API gives the app a token to send with every request. On a phone, the token belongs in the
platform's secure storage. This is Red Zone work: write it by hand, and have a senior engineer review it.

**What to learn:**

- Storing the token with `flutter_secure_storage`, which uses the Keychain on iOS and keys held in the Android
  Keystore on Android
- Why `shared_preferences` and plain files are not safe for tokens
- Turning off Android Auto Backup for the secure storage files, as the package's README explains, because restored
  files cannot be decrypted on a new device
- iOS Keychain items survive the app being deleted, so detect a fresh install with a flag in normal storage and delete
  any old token; choose a Keychain accessibility option that keeps the token on this device only
- Sending the token as `Authorization: Token <jwt>`, replacing it with the one `PUT /user` returns, and clearing it
  and every cached piece of user data on sign-out

**Resources:**

- [flutter_secure_storage](https://pub.dev/packages/flutter_secure_storage), pub.dev
- [Tokens: JWT, OAuth 2.0 and OIDC](../../../../security/audit/security-audit-reference.md#94-tokens--jwt-oauth-20-oidc),
  in the Techversant security audit reference
- [Red Zone](../../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the Techversant AI
  Era Coding Guidelines

**Level:** Practitioner · Core

## Rendering user content safely

Article bodies and comments are written by other users. Showing them must never let one user run code or open
harmful links on another user's phone.

**What to learn:**

- Rendering Markdown as Flutter widgets with `flutter_markdown_plus`, the maintained successor of the discontinued
  `flutter_markdown`
- Its links do nothing until you handle `onTapLink`; open only `http` and `https` addresses there, with
  `url_launcher`
- Deciding whether images in article bodies load at all, because each one is fetched from the reader's phone, and
  showing comments as plain text

**Resources:**

- [flutter_markdown_plus](https://pub.dev/packages/flutter_markdown_plus), pub.dev
- [Cross-site scripting and output encoding](../../../../security/audit/security-audit-reference.md#73-cross-site-scripting-and-output-encoding),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Configuration and environments

The app needs the API address, and different builds may point at different servers. Anything built into the app can
be read by anyone who downloads it.

**What to learn:**

- Passing settings with `--dart-define-from-file`, and reading them with `String.fromEnvironment`
- Why those values, and anything else in the app, can be read from the app file, even with obfuscation; secrets stay
  on a server
- Separate settings for development and production builds, which stage 10 turns into flavours

**Resources:** [Obfuscating Dart code](https://docs.flutter.dev/deployment/obfuscate), Flutter documentation

**Level:** Practitioner · Core

## Project: Connect to the API and Sign In

**Brief:** Make the whole app work against the RealWorld API: sign-up, sign-in and sign-out, writing and editing
articles, comments, following and favourites. Follow every rule on the [practice app](../practice-app.md) page.
Write the sign-in and token code by hand, and have a senior engineer review it.

**Size:** 4–5 days

**Verification**, checked by a reviewer:

- [ ] Every screen loads its data through the repository layer, and shows loading, empty and error states
- [ ] Favouriting, following, commenting and deleting update the screen at once and roll back when the request fails
- [ ] The token is stored only with `flutter_secure_storage`, sent as `Authorization: Token <jwt>`, and removed with
  all cached user data on sign-out
- [ ] When the app starts, a 401 or 403 for the current user signs the app out; any other response, or no response,
  keeps the token and shows "Connecting" with a retry
- [ ] A 401 on a request other than a form submit signs the user out on the same screen and says the session ended
- [ ] A failed form submit stays on the form with the API's errors, and a 401, 409 or 422 never signs the user out; a
  network failure shows "Unable to connect"
- [ ] A 404, a 500 or a network failure on an article or profile still shows the screen, with an error and a retry
- [ ] Settings sends `password` only when the user typed a new one, and the token is replaced with the one `PUT /user`
  returns
- [ ] Edit and delete buttons appear only on the signed-in user's own articles and comments
- [ ] The empty Your Feed says "Your feed is empty"
- [ ] Article bodies render Markdown as widgets, and a test shows that `tel:`, `javascript:` and custom-scheme links do
  nothing
- [ ] A fresh install removes any token left in the Keychain by an earlier install
- [ ] The API address comes from configuration, no secret is built into the app, and the temporary signed-in switch
  from stage 05 is gone
- [ ] A senior engineer has reviewed the sign-in and token code, and the review is linked in the pull request

Previous: [06. Forms and Input](./06-forms-and-input.md) · Next: [08. Device Features](./08-device-features.md)
