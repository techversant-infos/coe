# 05. Navigation

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-12 · **Next review:** 2027-02-12

Mobile apps move between screens with stacks, tabs and the system back gesture. The `go_router` package, maintained by
the Flutter team, gives every screen a path, which also makes deep links work. Back to the [roadmap](./README.md).

## Navigation basics

Flutter's `Navigator` keeps a stack of screens: pushing adds a screen on top, and popping goes back. Routing packages
build on it.

**What to learn:**

- Pushing and popping screens, and passing data to a new screen
- How the Android back gesture and the iOS back swipe pop the stack
- `PopScope`, to ask before leaving a screen with unsaved changes, such as the editor

**Resources:** [Navigation and routing](https://docs.flutter.dev/ui/navigation), Flutter documentation

**Level:** Practitioner · Core

## Routes with go_router

The `go_router` package describes the app as a list of routes with paths, such as `/article/:slug`. Moving to a screen
means going to its path.

**What to learn:**

- Defining routes and nested routes, and moving with `context.go` and `context.push`
- Path parameters, such as the article slug, and handling a missing or unknown value with a "not found" screen
- An error screen for paths that match no route

**Resources:** [go_router](https://pub.dev/packages/go_router), pub.dev

**Level:** Practitioner · Core

## Tabs

Tabs switch between top-level sections, and each tab keeps its own stack of screens. Users expect a tab to be where
they left it.

**What to learn:**

- `StatefulShellRoute` with a bottom navigation bar for Home, New Article and Profile
- Keeping each tab's stack and scroll position when the user switches tabs
- Tapping the current tab to go back to its first screen

**Resources:** [go_router](https://pub.dev/packages/go_router), pub.dev

**Level:** Practitioner · Core

## Redirects for signed-in screens

Some screens need a signed-in user. In `go_router`, `redirect` runs before every navigation and can send signed-out
users to sign-in.

**What to learn:**

- A `redirect` that checks the sign-in state, and `refreshListenable` so routes update when the user signs in or out
- Waiting for the stored sign-in state to load before deciding, so a signed-in user does not see sign-in for a moment
- Keeping the path the user asked for, such as in a `from` query parameter, and going there after sign-in
- Why a redirect in the app is only for convenience: the API must check every request itself. Redirects are part of
  the session code, so write them by hand

**Resources:** [Redirection](https://pub.dev/documentation/go_router/latest/topics/Redirection-topic.html), go_router
documentation

**Level:** Practitioner · Core

## Deep links

A deep link opens a specific screen, for example from an email or another app. Flutter passes incoming links to
`go_router`, which opens the matching route.

**What to learn:**

- Registering the `conduit` scheme in the Android manifest and the iOS `Info.plist`, and testing links on a
  simulator and an emulator
- In `conduit://article/<slug>`, `article` is the host part of the address, and `go_router` matches only the path, so
  turn each `conduit` link into an app path, such as `/article/<slug>`, in the top-level `redirect`, and test all
  three links
- Giving a deep-linked screen a sensible screen behind it, so the back action goes to Home
- Treating every value in a link as untrusted input

**Resources:**

- [Deep linking](https://docs.flutter.dev/ui/navigation/deep-linking), Flutter documentation
- [Deep linking](https://pub.dev/documentation/go_router/latest/topics/Deep%20linking-topic.html), go_router
  documentation

**Level:** Practitioner · Core

## App links and universal links

App links on Android and universal links on iOS open the app from normal `https` web addresses, falling back to the
website when the app is not installed. They need files hosted on the client's domain.

**What to learn:**

- How the domain proves it owns the app, and why custom schemes are less trusted

**Resources:**

- [Set up app links for Android](https://docs.flutter.dev/cookbook/navigation/set-up-app-links), Flutter documentation
- [Set up universal links for iOS](https://docs.flutter.dev/cookbook/navigation/set-up-universal-links), Flutter
  documentation

**Level:** Advanced · Optional

## Project: Add Every Screen and Deep Link

**Brief:** Add every screen from the [practice app](../practice-app.md) with `go_router`, using placeholder content
where data comes in later stages. Protect the screens that need sign-in, and add the three deep links.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Every screen in the practice app exists, with tabs and stacks as planned in stage 01
- [ ] Each tab keeps its own stack, and the Android back gesture and the iOS back swipe move through screens as the
  stage 01 plan describes
- [ ] Article and profile screens read their path parameter, and an unknown value shows a "not found" screen
- [ ] Signed-out users cannot open the editor, settings or Your Feed, and a temporary signed-in switch in the debug
  build shows the redirect working both ways; stage 07 removes the switch
- [ ] The redirect waits for the stored sign-in state before it decides
- [ ] `conduit://article/<slug>` and `conduit://profile/<username>` open the right screen on both platforms, with
  Home behind it
- [ ] `conduit://editor` opened while signed out shows sign-in, then goes on to the editor
- [ ] Leaving the editor with unsaved changes asks the user first

Previous: [04. State and Data Flow](./04-state-and-data-flow.md) · Next: [06. Forms and Input](./06-forms-and-input.md)
