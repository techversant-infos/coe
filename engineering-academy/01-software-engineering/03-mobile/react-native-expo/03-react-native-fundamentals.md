# 03. React Native Fundamentals

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-11 · **Next review:** 2027-02-11

React Native builds the screen from components, like React on the web, but the components become real iOS and
Android views instead of HTML. This stage covers the core ideas you use in every screen. Back to the
[roadmap](./README.md).

## Expo projects and development builds

Expo creates and runs React Native projects. Expo Go lets you try an app straight away, while a development build is
your own debug app with exactly the native libraries your project needs.

**What to learn:**

- Creating a project with `create-expo-app`, and running it on an iOS simulator, an Android emulator and a phone
- When Expo Go is enough, and when you need a development build, such as for a library with its own native code
- Fast Refresh, and reading errors and logs while the app runs

**Resources:**

- [Introduction to development builds](https://docs.expo.dev/develop/development-builds/introduction/), Expo
  documentation
- [Get started with React Native](https://reactnative.dev/docs/environment-setup), React Native documentation

**Level:** Practitioner · Core

## Components and JSX

A screen is built from small components, written in JSX (JavaScript XML), an HTML-like syntax that describes what
to show. React Native has its own core components, such as `View`, `Text`,
`Image` and `Pressable`, instead of HTML elements.

**What to learn:**

- Writing function components with typed props, and splitting a screen into components that each do one job
- Core components: `View` for layout, `Text` for all text, `Pressable` for anything the user taps
- Why every piece of text must sit inside a `Text` component

**Resources:**

- [React fundamentals](https://reactnative.dev/docs/intro-react), React Native documentation
- [Learn React](https://react.dev/learn), React documentation

**Level:** Practitioner · Core

## Styling and layout

React Native styles look like CSS, but they are JavaScript objects, and layout always uses flexbox. Each component
is styled on its own; there is no global stylesheet.

**What to learn:**

- `StyleSheet.create`, and how flexbox differs from the web: the default direction is a column
- Sizes in density-independent units, and layouts that work on small phones and tablets
- Safe areas, so content is not hidden by notches, rounded corners or system bars

**Resources:**

- [Layout with Flexbox](https://reactnative.dev/docs/flexbox), React Native documentation
- [Safe areas](https://docs.expo.dev/develop/user-interface/safe-areas/), Expo documentation

**Level:** Practitioner · Core

## Lists

Feeds are long, and rendering every item at once makes an app slow. List components render only what is on screen.

**What to learn:**

- `FlatList` with a stable `keyExtractor`, such as the article slug, not the index
- Empty, loading and error states for every list, and a header for the tag list
- FlashList, a faster list library, and when the extra dependency is worth it

**Resources:**

- [Optimizing FlatList configuration](https://reactnative.dev/docs/optimizing-flatlist-configuration), React Native
  documentation
- [FlashList](https://shopify.github.io/flash-list/)

**Level:** Practitioner · Core

## Images, themes and dark mode

Images come from the network in different sizes, and users choose light or dark mode. Both affect every screen.

**What to learn:**

- Loading remote images, such as avatars, with `expo-image`, with a placeholder and a fallback when the URL fails
- Reading the system colour scheme with `useColorScheme`, and keeping colours in one theme object
- Checking contrast in light and dark mode

**Resources:**

- [Image](https://docs.expo.dev/versions/latest/sdk/image/), Expo documentation
- [Color themes](https://docs.expo.dev/develop/user-interface/color-themes/), Expo documentation

**Level:** Practitioner · Core

## Platform-specific code

Most code runs on both platforms, but some behaviour should differ. React Native lets you branch by platform where
you need to.

**What to learn:**

- `Platform.OS` and `Platform.select` for small differences
- Separate `.ios.tsx` and `.android.tsx` files when a whole component differs
- Testing every change on both platforms, not only the one on your desk

**Resources:**
[Platform-specific code](https://reactnative.dev/docs/platform-specific-code), React Native documentation

**Level:** Practitioner · Core

## React Native DevTools

React Native DevTools shows the component tree, each component's props and state, network requests and console
output from the app. You use it every day to find bugs.

**What to learn:**

- Opening DevTools from the running app, and finding which component draws a part of the screen
- The Network panel for API calls, and the Profiler panel for slow renders

**Resources:** [React Native DevTools](https://reactnative.dev/docs/react-native-devtools), React Native
documentation

**Level:** Practitioner · Core

## Project: Build the Home Screen

**Brief:** Start an Expo SDK (software development kit) 58 app in TypeScript and build the home screen from your stage
01 sketches. Load the
articles and tags with your stage 02 API client.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] The app runs on an iOS simulator and an Android emulator, and screenshots of both are in the pull request
- [ ] The screen is split into components, such as article preview, tag list and header, each with typed props
- [ ] The feed uses a list component with the slug as the key, not the index
- [ ] The screen shows loading, empty and error states, with a retry on error
- [ ] Avatars load with a placeholder, and a broken image URL shows a fallback
- [ ] Light and dark mode both have readable text, and content stays inside the safe areas
- [ ] TypeScript strict mode and linting pass with no errors

Previous: [02. JavaScript and TypeScript](./02-javascript-and-typescript.md) · Next:
[04. State and Data Flow](./04-state-and-data-flow.md)
