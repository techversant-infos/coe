# 07. Working with APIs

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-18 · **Next review:** 2027-05-18

An iPhone app is usually the front end for an API, used over networks that are slow, change between Wi-Fi and mobile
data, or disappear. This stage connects the whole app to the API, safely. Back to the [roadmap](./README.md).

## Changing data

Reading data is half the job. Writing articles, comments, follows and favourites changes data on the server, and
every screen must stay in step.

**What to learn:**

- Sending changes through the repository with `URLSession`, then updating the affected models
- Optimistic updates, such as showing a favourite straight away and undoing it if the request fails
- Preventing double submits when the user taps twice

**Resources:** [URLSession](https://developer.apple.com/documentation/foundation/urlsession), Apple

**Level:** Practitioner · Core

## Handling API errors

The API returns errors in a fixed shape, and each kind of error needs a different response in the app.

**What to learn:**

- Decoding RealWorld's error body, `{"errors": {"field": ["message"]}}`, into a typed error and showing it on the form
- What 401, 403, 404, 409, 422 and 5xx responses mean, and what the user should see for each, following the
  [practice app](../practice-app.md#behaviour-rules) rules
- Never signing the user out because of a 401, 409 or 422 on a form

**Resources:** [HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status), MDN
Web Docs

**Level:** Practitioner · Core

## Poor and missing networks

Mobile users lose the connection in lifts, trains and basements. The app must say what is happening and recover
when the network returns.

**What to learn:**

- Timeouts on every request, so a screen never spins forever, and automatic retries for GET requests only; the user
  retries a failed write, so an article or comment is never created twice
- `NWPathMonitor`, and why it reports whether a network path exists, not whether the API can be reached
- Clear "Unable to connect" and "Connecting" states, with a retry button, and reloading when the network returns

**Resources:** [NWPathMonitor](https://developer.apple.com/documentation/network/nwpathmonitor), Apple

**Level:** Practitioner · Core

## Tokens on the device

After sign-in, the API gives the app a token to send with every request. On an iPhone, the token belongs in the
Keychain. This is Red Zone work: write it by hand, and have a senior engineer review it.

**What to learn:**

- Storing, reading and deleting the token with Keychain Services, through a small wrapper you write and test
- Why `UserDefaults` and plain files are not safe for tokens
- Choosing an accessibility option such as `kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly`, which never moves the
  token to another device: a backup restores it only to the same iPhone
- Keychain items can survive the app being deleted; Apple does not document this, so handle both cases: detect a
  fresh install with a flag in `UserDefaults` and delete any old token
- Sending the token as `Authorization: Token <jwt>`, replacing it with the one `PUT /user` returns, and clearing it
  and every cached piece of user data on sign-out

**Resources:**

- [Keychain services](https://developer.apple.com/documentation/security/keychain-services), Apple
- [Restricting keychain item accessibility](https://developer.apple.com/documentation/security/restricting-keychain-item-accessibility),
  Apple
- [Tokens: JWT, OAuth 2.0 and OIDC](../../../../security/audit/security-audit-reference.md#94-tokens--jwt-oauth-20-oidc),
  in the Techversant security audit reference
- [Red Zone](../../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the Techversant AI
  Era Coding Guidelines

**Level:** Practitioner · Core

## Rendering user content safely

Article bodies and comments are written by other users. Showing them must never let one user run code or open
harmful links on another user's phone.

**What to learn:**

- Rendering Markdown as native text, never as HTML in a web view: `AttributedString(markdown:)` handles inline
  styles and links, and headings and lists need a maintained library your lead approves
- SwiftUI sends link taps to the `openURL` environment action; replace it with an `OpenURLAction` that opens only
  `http` and `https` addresses and discards every other link
- Deciding whether images in article bodies load at all, because each one is fetched from the reader's phone, and
  showing comments as plain text

**Resources:**

- [OpenURLAction](https://developer.apple.com/documentation/swiftui/openurlaction), SwiftUI documentation
- [Cross-site scripting and output encoding](../../../../security/audit/security-audit-reference.md#73-cross-site-scripting-and-output-encoding),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Configuration and environments

The app needs the API address, and different builds may point at different servers. Anything built into the app can
be read by anyone who downloads it.

**What to learn:**

- Build configuration files (`.xcconfig`) that set values per configuration, passed into `Info.plist` and read with
  `Bundle.main`; `//` starts a comment in these files, so write an address as
  `https:/$()/api.example.com`
- Why those values, and anything else in the app bundle, can be read from the app file; secrets stay on a server
- Separate settings for development and production builds, which stage 10 turns into schemes

**Resources:**
[Adding a build configuration file to your project](https://developer.apple.com/documentation/xcode/adding-a-build-configuration-file-to-your-project),
Apple

**Level:** Practitioner · Core

## Project: Connect to the API and Sign In

**Brief:** Make the whole app work against the RealWorld API: sign-up, sign-in and sign-out, writing and editing
articles, comments, following and favourites. Follow every rule on the [practice app](../practice-app.md) page.
Write the Red Zone code listed on that page by hand, and have a senior engineer review it.

**Size:** 4–5 days

**Verification**, checked by a reviewer:

- [ ] Every screen loads its data through the repository layer, and shows loading, empty and error states
- [ ] Favouriting, following, commenting and deleting update the screen at once and roll back when the request fails
- [ ] The token is stored only in the Keychain, with a this-device-only accessibility option, sent as
  `Authorization: Token <jwt>`, and removed with all cached user data on sign-out
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
- [ ] Article bodies render Markdown as native text, and a test shows that `tel:`, `javascript:` and custom-scheme
  links do nothing
- [ ] A fresh install removes any token left in the Keychain by an earlier install
- [ ] The API address comes from configuration, no secret is built into the app, and the temporary signed-in switch
  from stage 05 is gone
- [ ] A senior engineer has reviewed the Red Zone code: sign-up, sign-in and sign-out, Keychain storage, adding the
  token to requests, the startup check, 401 handling, the signed-in screen checks, and the email and password change in
  Settings; the review is linked in the pull request

Previous: [06. Forms and Input](./06-forms-and-input.md) · Next: [08. Device Features](./08-device-features.md)
