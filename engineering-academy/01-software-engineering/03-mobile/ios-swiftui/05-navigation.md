# 05. Navigation

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-18 · **Next review:** 2027-02-18

iPhone apps move between screens with stacks, tabs and sheets, and users go back with a swipe from the left edge.
SwiftUI drives navigation from data, which also makes deep links work. Back to the [roadmap](./README.md).

## Navigation stacks

A navigation stack shows one screen on top of another: pushing adds a screen, and going back removes it. In SwiftUI,
the stack can be driven by an array of values.

**What to learn:**

- `NavigationStack` with `NavigationLink(value:)` and `.navigationDestination(for:)`
- Holding the stack in a path, such as an array of routes, so code can push, pop and go back to the first screen
- Titles, toolbars and the back swipe, and why you should not replace the system back button

**Resources:** [NavigationStack](https://developer.apple.com/documentation/swiftui/navigationstack), SwiftUI
documentation

**Level:** Practitioner · Core

## Tabs

Tabs switch between top-level sections, and each tab keeps its own stack of screens. Users expect a tab to be where
they left it.

**What to learn:**

- `TabView` with `Tab` for Home and Profile, each with its own `NavigationStack`, and a New Article button in the
  toolbar that opens the editor as a sheet
- Keeping each tab's path and scroll position when the user switches tabs
- Going back to a tab's first screen when the user taps the tab they are already on

**Resources:** [TabView](https://developer.apple.com/documentation/swiftui/tabview), SwiftUI documentation

**Level:** Practitioner · Core

## Sheets and confirmation

Sheets show a task on top of the current screen, such as writing an article. Alerts and confirmation dialogs ask the
user before something cannot be undone.

**What to learn:**

- `.sheet` and `.fullScreenCover`, and dismissing them with the `dismiss` environment action
- `.interactiveDismissDisabled`, which blocks swiping the editor sheet down while it has unsaved changes, and a
  confirmation dialog on its Cancel button
- `.alert` and `.confirmationDialog` before deleting an article or a comment

**Resources:** [Modal presentations](https://developer.apple.com/documentation/swiftui/modal-presentations), SwiftUI
documentation

**Level:** Practitioner · Core

## Signed-in screens

Some screens need a signed-in user. Before showing one, the app checks the session and shows sign-in first if the user
is signed out.

**What to learn:**

- One place in the code that decides whether a destination needs sign-in, using the session model from the
  environment
- Waiting for the stored sign-in state to load before deciding, so a signed-in user does not see sign-in for a moment
- Remembering the screen the user asked for, and going there after sign-in
- Why these checks in the app are only for convenience: the API must check every request itself. They are part of the
  session code, so write them by hand

**Resources:** [Environment](https://developer.apple.com/documentation/swiftui/environment), SwiftUI documentation

**Level:** Practitioner · Core

## Deep links

A deep link opens a specific screen, for example from an email or another app. iOS passes the link to the app, and
the app turns it into navigation.

**What to learn:**

- Registering the `conduit` scheme as a URL type for the app target (the part of the Xcode project that builds the app),
  and receiving links with `.onOpenURL`
- In `conduit://article/<slug>`, `article` is the `host` of the URL and the slug is in its path, so read both and
  turn the link into a route in your navigation path
- Giving a deep-linked screen a sensible screen behind it, so going back leads to Home
- Treating every value in a link as untrusted input, and testing links in the Simulator with `xcrun simctl openurl`

**Resources:**

- [Defining a custom URL scheme for your app](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app),
  Apple
- [onOpenURL(perform:)](https://developer.apple.com/documentation/swiftui/view/onopenurl(perform:)), SwiftUI
  documentation

**Level:** Practitioner · Core

## Universal links

Universal links open the app from normal `https` web addresses, and open the website when the app is not installed.
They need a file hosted on the client's domain.

**What to learn:**

- The Associated Domains entitlement and the `apple-app-site-association` file, and why custom schemes are less
  trusted

**Resources:**
[Supporting universal links in your app](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app),
Apple

**Level:** Advanced · Optional

## Project: Add Every Screen and Deep Link

**Brief:** Add every screen from the [practice app](../practice-app.md), using placeholder content where data comes
in later stages. Protect the screens that need sign-in, and add the three deep links.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Every screen in the practice app exists, with tabs, stacks and sheets as planned in stage 01
- [ ] Each tab keeps its own stack, and the back swipe moves through screens as the stage 01 plan describes
- [ ] Article and profile screens read their route value; stage 07 adds the 404 state for an unknown slug or username
- [ ] Signed-out users cannot open the editor, settings or Your Feed, and a temporary signed-in switch that only Debug
  builds include (wrap it in `#if DEBUG`) shows the check working both ways; stage 07 removes the switch
- [ ] The check waits for the stored sign-in state before it decides
- [ ] `conduit://article/<slug>` and `conduit://profile/<username>` open the right screen, with Home behind it
- [ ] `conduit://editor` opened while signed out shows sign-in, then goes on to the editor
- [ ] With unsaved changes, swiping the editor down is blocked, and Cancel asks the user first

Previous: [04. State and Data Flow](./04-state-and-data-flow.md) · Next: [06. Forms and Input](./06-forms-and-input.md)
