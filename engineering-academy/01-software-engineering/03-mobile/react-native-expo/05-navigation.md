# 05. Navigation

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-11 · **Next review:** 2027-02-11

Mobile apps move between screens with stacks, tabs and the system back gesture, not with page loads. Expo Router
builds navigation from your files, much like routing in a web framework. Back to the [roadmap](./README.md).

## File-based routing

In Expo Router, each file in the `app` folder is a screen, and the folder structure decides the navigation.

**What to learn:**

- How files and folders map to screens, and layout files (`_layout.tsx`) that wrap a group of screens
- Moving between screens with `Link` and the router, and going back
- Groups in brackets, such as `(tabs)`, that organise files without changing the URL

**Resources:**

- [Introduction to Expo Router](https://docs.expo.dev/router/introduction/), Expo documentation
- [Layouts](https://docs.expo.dev/router/basics/navigation-layouts/), Expo documentation

**Level:** Practitioner · Core

## Stacks and tabs

A stack shows one screen on top of another, with a back action. Tabs switch between top-level sections. Most apps
combine them.

**What to learn:**

- A tab bar for Home, New Article and Profile, with a stack inside each tab
- Screen titles, header buttons and how the Android back gesture moves through stacks and tabs
- Keeping each tab's place when the user switches tabs

**Resources:** [Tabs](https://docs.expo.dev/router/advanced/tabs/), Expo documentation

**Level:** Practitioner · Core

## Route parameters

A screen often depends on a value in its route, such as the article slug or the username.

**What to learn:**

- Dynamic routes, such as `article/[slug].tsx`, and reading the parameter with `useLocalSearchParams`
- Typing parameters, and handling a missing or unknown value with a "not found" state

**Resources:** [URL parameters](https://docs.expo.dev/router/reference/url-parameters/), Expo documentation

**Level:** Practitioner · Core

## Protected routes

Some screens need a signed-in user. Expo Router can show or hide groups of screens based on the sign-in state.

**What to learn:**

- `Stack.Protected` with a guard, so signed-out users cannot reach the editor or settings
- Waiting for the stored sign-in state to load before deciding, so a signed-in user does not see the sign-in screen
  for a moment
- Saving the screen a signed-out user asked for, and going there after sign-in, because `Stack.Protected` sends
  them to the first available screen instead
- Why a guard in the app is only for convenience: the API must check every request itself. Route guards are part of
  the session code, so write them by hand

**Resources:** [Authentication](https://docs.expo.dev/router/advanced/authentication/), Expo documentation

**Level:** Practitioner · Core

## Deep links

A deep link opens a specific screen, for example from an email or another app. Every screen in Expo Router has a
URL, so deep links mostly work once the app has a scheme.

**What to learn:**

- Setting the app's scheme, such as `conduit`, and testing links in a development build on a simulator and an
  emulator; Expo Go uses its own `exp://` scheme
- Setting the stack's anchor screen, so a deep-linked article has Home behind it and the back action works
- What happens when a deep link points to a screen that needs sign-in
- Treating every value in a link as untrusted input

**Resources:**

- [Linking overview](https://docs.expo.dev/linking/overview/), Expo documentation
- [Link into your app](https://docs.expo.dev/linking/into-your-app/) and
  [Router settings](https://docs.expo.dev/router/advanced/router-settings/), Expo documentation

**Level:** Practitioner · Core

## Universal links and app links

Universal links on iOS and app links on Android open the app from normal `https` web addresses, falling back to the
website when the app is not installed. They need files hosted on the client's domain.

**What to learn:**

- How the domain proves it owns the app, and why custom schemes are less trusted

**Resources:** [Linking overview](https://docs.expo.dev/linking/overview/), Expo documentation

**Level:** Advanced · Optional

## Project: Add Every Screen and Deep Link

**Brief:** Add every screen from the [practice app](../practice-app.md) with Expo Router, using placeholder content
where data comes in later stages. Protect the screens that need sign-in, and add the three deep links.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Every screen in the practice app exists, with tabs and stacks as planned in stage 01
- [ ] The Android back gesture and the iOS back swipe move through screens as the stage 01 plan describes
- [ ] Article and profile screens read their parameter, and an unknown value shows a "not found" state
- [ ] Signed-out users cannot open the editor, settings or Your Feed, and a temporary signed-in switch in the
  development build shows the guard working both ways; stage 07 removes the switch
- [ ] The guard waits for the stored sign-in state before it redirects
- [ ] `conduit://article/<slug>` and `conduit://profile/<username>` open the right screen on both platforms, with
  Home behind it
- [ ] `conduit://editor` opened while signed out shows sign-in, then goes on to the editor

Previous: [04. State and Data Flow](./04-state-and-data-flow.md) · Next: [06. Forms and Input](./06-forms-and-input.md)
