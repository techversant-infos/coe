# 03. Flutter Fundamentals

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-12 · **Next review:** 2027-02-12

Flutter builds the screen from widgets: small objects that describe part of the interface. Flutter draws them itself
with its Impeller engine, instead of using the platform's own views. This stage covers the core ideas you use in every
screen. Back to the [roadmap](./README.md).

## Projects, devices and hot reload

The Flutter command-line tool creates, runs and builds apps. Hot reload shows code changes in the running app in
about a second.

**What to learn:**

- Creating a project with `flutter create`, and running it on an iOS simulator, an Android emulator and a phone
- `flutter doctor`, to check that the tools for each platform are set up
- Hot reload compared with hot restart, and reading errors and logs while the app runs

**Resources:** [Install Flutter](https://docs.flutter.dev/get-started/install), Flutter documentation

**Level:** Practitioner · Core

## Widgets

Everything on screen is a widget, from a line of text to a whole page. You build a screen by putting small widgets
inside larger ones.

**What to learn:**

- Stateless widgets with typed constructor parameters, and splitting a screen into widgets that each do one job
- The `build` method, and why it should be fast and free of side effects
- `const` constructors, which let Flutter skip rebuilding widgets that never change

**Resources:** [Building user interfaces with Flutter](https://docs.flutter.dev/ui), Flutter documentation

**Level:** Practitioner · Core

## Layout

Flutter layout uses widgets too: rows, columns, padding and constraints. Each widget gets size limits from its parent
and chooses its size within them.

**What to learn:**

- `Row`, `Column`, `Expanded`, `Padding` and `SizedBox`, and the rule that constraints go down and sizes go up
- Fixing overflow errors, the yellow and black stripes on the screen
- `SafeArea`, so content is not hidden by notches, rounded corners or system bars, and layouts that work on tablets

**Resources:**

- [Layouts in Flutter](https://docs.flutter.dev/ui/layout), Flutter documentation
- [Adaptive and responsive design](https://docs.flutter.dev/ui/adaptive-responsive), Flutter documentation

**Level:** Practitioner · Core

## Lists

Feeds are long, and building every item at once makes an app slow. Builder lists create only the items on screen.

**What to learn:**

- `ListView.builder` and `ListView.separated`, and a stable `Key` for each item, such as the article slug
- Empty, loading and error states for every list, and a header for the tag list
- Showing data from a `Future` with `FutureBuilder`, including its loading and error states
- Slivers, for screens that combine a header and a list in one scroll

**Resources:** [Work with long lists](https://docs.flutter.dev/cookbook/lists/long-lists), Flutter documentation

**Level:** Practitioner · Core

## Themes, images and dark mode

Users choose light or dark mode, and images come from the network in different sizes. Both affect every screen.

**What to learn:**

- `ThemeData` with a colour scheme for light and dark mode, and reading colours from the theme instead of hard-coding
  them
- Loading remote images, such as avatars, with a placeholder and a fallback when the URL fails, for example with
  `cached_network_image`
- Material widgets, Cupertino widgets, and when to use adaptive widgets that match each platform

**Resources:**

- [Use themes to share colours and font styles](https://docs.flutter.dev/cookbook/design/themes), Flutter
  documentation
- [Display images from the internet](https://docs.flutter.dev/cookbook/images/network-image), Flutter documentation

**Level:** Practitioner · Core

## Flutter DevTools

Flutter DevTools shows the widget tree, network calls, memory and the time each frame takes. You use it every day to
find bugs.

**What to learn:**

- The widget inspector, to find which widget draws a part of the screen and why it has its size
- The Network view for API calls, and the Performance view for slow frames

**Resources:** [Flutter and Dart DevTools](https://docs.flutter.dev/tools/devtools), Flutter documentation

**Level:** Practitioner · Core

## Project: Build the Home Screen

**Brief:** Start a Flutter 3.50 app and build the home screen from your stage 01 sketches. Load the articles and tags
with your stage 02 API client.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] The app runs on an iOS simulator and an Android emulator, and screenshots of both are in the pull request
- [ ] The screen is split into widgets, such as article preview, tag list and header, each with typed parameters
- [ ] The feed uses `ListView.builder`, with the slug as each item's key
- [ ] The screen shows loading, empty and error states, with a retry on error
- [ ] Avatars load with a placeholder, and a broken image URL shows a fallback
- [ ] Light and dark mode both have readable text, colours come from the theme, and content stays inside the safe
  areas
- [ ] `dart analyze` reports no warnings, and the app shows no overflow errors at the largest text size

Previous: [02. Dart](./02-dart.md) · Next: [04. State and Data Flow](./04-state-and-data-flow.md)
