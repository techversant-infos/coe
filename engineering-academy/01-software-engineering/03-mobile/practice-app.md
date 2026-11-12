# Practice App: A RealWorld Mobile Client

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-11 · **Next review:** 2027-02-11

Every mobile path in the academy builds the same app: a mobile client for **RealWorld**, an open-source Medium-style
blogging app also called Conduit. The web paths build the same app in the browser, so the API, the data and the
features are already familiar. Back to [Mobile](./README.md).

## Why This App

- **It is a real app.** Sign-up, sign-in, feeds, articles, comments, profiles, following and favourites cover most
  of what client mobile apps do.
- **The API is fixed.** One API specification means you spend your time on mobile skills, not on deciding what to
  build.
- **It pairs with any back end.** Every RealWorld back end follows the same API, including one you build in a
  [back-end path](../01-backend/README.md).
- **It exercises what makes mobile hard.** Lists, navigation, keyboards, poor networks, secure storage, permissions
  and store release all appear in a small app.

RealWorld's shared Playwright tests check web front ends only. For mobile, this page is the contract, and you write
the end-to-end tests yourself, with the flows listed in [Test Flows](#test-flows).

## Key Details

| Detail | Value |
|--------|-------|
| Repository | [realworld-apps/realworld](https://github.com/realworld-apps/realworld), MIT licence |
| API specification | `specs/api/openapi.yml` in the repository |
| API for day-to-day work | The public demo API, `https://api.realworld.show/api`. It uses HTTPS, so it works from simulators, emulators and real devices without network exceptions. Signed-in users see only their own content and the demo accounts' content. |
| Local API, optional | The official back end, [nitro-prisma-zod-realworld-example-app](https://github.com/realworld-apps/nitro-prisma-zod-realworld-example-app), serves `http://localhost:3000/api`. See [Using a Local Back End](#using-a-local-back-end). |

Sign up only with generated test data, never real names or email addresses.

## Screens

| Screen | What it shows and does |
|--------|------------------------|
| Home | Global Feed for everyone, and Your Feed for signed-in users; popular tags; filtering by a tag; loading more articles as the user scrolls; pull to refresh |
| Article | Title, author, date, tags and the body rendered from Markdown; favourite and follow; comments, with adding and deleting your own; editing and deleting your own article |
| Profile | The user's image, name and bio; follow; their articles and the articles they favourited |
| Sign-in and sign-up | The two forms, with the API's errors shown on the form |
| Editor | New article and edit article, with title, description, body and tags; an unsent draft is saved on the device |
| Settings | Image URL, username, bio, email and new password; sign out |

Signed-out users can read feeds, articles and profiles. The editor, settings, Your Feed, favouriting, following and
commenting need a signed-in user.

## Working with the API

- **Small data set.** Signed out, the demo API serves only four demo articles, one per tag. To test loading more,
  request small pages, such as `limit=2`, or sign up and write enough articles to fill several pages.
- **List items have no body.** Feeds return articles without `body`, so the Article screen loads
  `GET /articles/{slug}`.
- **Empty fields.** A profile's `image` and `bio` can be `null`. Show a placeholder.
- **Status codes.** The API returns 401 for a missing or bad token and for a wrong password, 409 when a username,
  email or article already exists, and 422 for validation errors, with the body `{"errors": {"field": ["message"]}}`.
- **The user object contains the token.** Sign-up, sign-in, `GET /user` and `PUT /user` return the user with its
  `token`. Store the token in secure storage, replace it with the one `PUT /user` returns, and never keep it in a
  query cache, a saved cache or logs.
- **Settings.** Send `password` only when the user typed a new one.

## Behaviour Rules

These rules match the web paths, adapted for mobile:

- **Starting the app.** If a token is stored, the app loads the current user. A 401 or 403 clears the token and shows
  the app signed out. Any other response, or no response, keeps the token and shows a "Connecting" message with a
  retry.
- **A session that ends.** A 401 on any request other than a form submit clears the token, keeps the user on the
  screen as signed out, and says the session ended.
- **Failed submits.** A failed submit stays on the form and shows the API's errors. A 401, 409 or 422 on a form
  never signs the user out. A network failure shows "Unable to connect".
- **Errors on screens.** A 404, a 500 or a network failure on an article or profile still shows the screen, with an
  error message and a retry.
- **Empty states.** An empty Your Feed says "Your feed is empty".
- **Article bodies.** The body is Markdown. Render it as native components, never by loading raw HTML into a web
  view. Open only `http` and `https` links, in the system browser or an in-app browser; every other link does
  nothing.
- **Ownership.** Edit and delete buttons appear only on the signed-in user's own articles and comments.
- **Deep links.** `conduit://article/<slug>` opens an article, `conduit://profile/<username>` opens a profile, and
  `conduit://editor` opens the editor. A link to a screen that needs sign-in shows sign-in first, then goes on to the
  screen the link asked for.

## The Token

After sign-in, the API returns a token that the app sends as `Authorization: Token <jwt>`. Store it only in the
platform's secure storage: the Keychain on iOS and storage encrypted with the Android Keystore on Android. Never
store it in plain preferences, files, caches or logs. Sign-out removes it and clears every cached piece of user data.

The code that handles sign-in and the session is Red Zone work under the
[AI Era Coding Guidelines](../../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only): write it
by hand, and have a senior engineer review it. That covers sign-up, sign-in and sign-out; storing the token; adding
it to requests; the startup session check and handling of 401 responses; route guards; and changing the email or
password in Settings.

## Test Flows

Write these end-to-end flows in your path's tool, such as Maestro or the platform's user interface (UI) test
framework. Each flow creates its own test user with generated data, so flows can run in any order:

1. Sign up, then sign out and sign in again
2. Write an article, see it in the profile, edit it and delete it
3. Comment on an article and delete the comment
4. Favourite and unfavourite an article, and follow and unfollow its author
5. Write enough articles with one new tag to fill more than one page, filter the feed by that tag, and load more by
   scrolling
6. Open an article from a deep link, and open `conduit://editor` signed out, sign in, and land on the editor
7. Turn the network off and check the "Unable to connect" and retry states

Flow 7 needs a device that can go offline from the test. Maestro can turn on aeroplane mode only on Android, so on
an iOS simulator cover the offline states with component tests instead, check them by hand once, and say how in the
pull request.

Find elements by their accessibility label or visible text where possible. Use test IDs only for elements with no
label, so the flows also check that the app is accessible.

## Using a Local Back End

The public demo API is the simplest choice. To use the local back end instead:

- **Android emulator:** use `http://10.0.2.2:3000/api`, because `localhost` inside the emulator is the emulator
  itself.
- **iOS simulator:** `http://localhost:3000/api` reaches your computer.
- **Real device:** start the back end so it listens on your network, for example with `HOST=0.0.0.0`, then use your
  computer's address on the local network. iOS asks the user for local-network permission.
- **Plain HTTP:** Android and iOS block unencrypted HTTP by default. Allow it only in debug builds, check that your
  path's project template already does so, and confirm that the release build cannot reach an `http://` address.

## Release Rules

- Distribute the practice app only through internal testing, such as TestFlight internal testing, Google Play
  internal testing or your build service's internal distribution, using developer accounts your lead approves.
- Never publish the practice app to a public store listing.
- Use the app for practice only. Do not ship it with real users' data, and do not copy its code into client work.

## Paths That Use It

- [React Native and Expo](./react-native-expo/README.md)
