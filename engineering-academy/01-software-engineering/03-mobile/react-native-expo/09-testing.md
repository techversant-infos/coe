# 09. Testing

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-11 · **Next review:** 2027-02-11

Tests let you change an app without fear of breaking it on a phone you do not own. A good mix has many fast
component tests, some tests against a mocked API, and a few end-to-end flows that drive the real app. Back to the
[roadmap](./README.md).

## Component tests

Component tests render one component, act on it the way a user would, and check what appears on screen. Expo
projects run them with Jest and the `jest-expo` preset.

**What to learn:**

- Rendering with React Native Testing Library, and finding elements by role, label or text
- Simulating taps and typing, and waiting for the screen to update
- Testing behaviour, not implementation details such as state variable names

**Resources:**

- [Unit testing with Jest](https://docs.expo.dev/develop/unit-testing/), Expo documentation
- [React Native Testing Library](https://oss.callstack.com/react-native-testing-library/)
- [Test levels](../../../00-engineering-foundations/07-testing-and-refactoring.md#test-levels), in Engineering
  Foundations

**Level:** Practitioner · Core

## Testing API calls

Tests should show what each screen does when the API is slow, fails or returns nothing, without a real back end.

**What to learn:**

- Replacing the API client or `fetch` with a test double that returns success, errors and delays
- Wrapping screens in a fresh TanStack Query client for each test, with retries turned off
- Testing the 401, 403, 404, 409, 422, 5xx and network-failure states from the practice app's rules

**Resources:** [Testing](https://tanstack.com/query/latest/docs/framework/react/guides/testing), TanStack Query
documentation

**Level:** Practitioner · Core

## End-to-end flows with Maestro

End-to-end flows drive the real app on a simulator or emulator, the way a user would. Maestro writes them as short YAML
(a plain-text settings format) files and waits for the screen automatically.

**What to learn:**

- Writing flows that tap, type and check what is on screen, using accessibility labels and visible text
- Creating test data, such as a new user, inside each flow, so flows are independent
- Running the same flows on iOS and Android, and knowing the limits: Maestro can turn on aeroplane mode only on
  Android

**Resources:** [Maestro documentation](https://docs.maestro.dev/)

**Level:** Advanced · Core

## Accessibility testing

Automated checks find some problems, such as missing labels. Screen readers and larger text find the rest.

**What to learn:**

- Using the platforms' checkers: Accessibility Inspector on iOS and Accessibility Scanner on Android
- Going through each flow with VoiceOver and TalkBack
- Checking every screen with the largest text size and in dark mode

**Resources:**

- [Accessibility Inspector](https://developer.apple.com/documentation/accessibility/accessibility-inspector), Apple
- [Accessibility Scanner](https://support.google.com/accessibility/android/answer/6376570), Google

**Level:** Advanced · Core

## Testing in continuous integration

Tests only protect the app when they run on every change. Component tests run on any server; end-to-end flows need
a simulator or emulator.

**What to learn:**

- Running type checks, linting and component tests on every pull request
- Running the Maestro flows on a build in continuous integration, such as with Expo Workflows (formerly EAS
  Workflows)

**Resources:** [Expo Workflows](https://docs.expo.dev/eas/workflows/introduction/), Expo documentation

**Level:** Advanced · Optional

## Project: Test Every Flow

**Brief:** Add component tests, tests against a mocked API and end-to-end flows to the practice app. Write every
flow listed on the [practice app](../practice-app.md#test-flows) page in Maestro.

**Size:** 4 days

**Verification**, checked by a reviewer:

- [ ] Component tests cover the article preview, the feed, every form and its validation errors
- [ ] Tests show each screen's response to 401, 403, 404, 409, 422, 5xx and network failures
- [ ] All seven practice-app test flows pass on an Android emulator, and flows 1–6 pass on an iOS simulator; the
  pull request explains how the offline states are covered on iOS
- [ ] Each flow creates its own test user with generated data, and flows pass in any order
- [ ] Flows find elements by accessibility label or text, and the pull request explains every test ID used
- [ ] Accessibility Inspector and Accessibility Scanner report no unresolved issues on the home, article and sign-in
  screens, the pull
  request explains any that remain,
  and VoiceOver and TalkBack can complete the sign-in flow
- [ ] Type checks, linting and component tests run in continuous integration, and a failing test blocks the merge

Previous: [08. Device Features](./08-device-features.md) · Next:
[10. Performance and Release](./10-performance-and-release.md)
