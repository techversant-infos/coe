# 09. Testing

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-12 · **Next review:** 2027-02-12

Tests let you change an app without fear of breaking it on a phone you do not own. Flutter has three kinds: many
fast unit and widget tests, and a few integration tests that drive the real app. Back to the [roadmap](./README.md).

## Unit tests

Unit tests check one function or class, such as a view model or the API client, without drawing anything on screen.

**What to learn:**

- Writing tests with the `test` package: `group`, `test`, `expect` and matchers
- Testing view models and repositories by giving them test doubles instead of real services
- Testing asynchronous code and streams

**Resources:**

- [An introduction to unit testing](https://docs.flutter.dev/cookbook/testing/unit/introduction), Flutter
  documentation
- [Test levels](../../../00-engineering-foundations/07-testing-and-refactoring.md#test-levels), in Engineering
  Foundations

**Level:** Practitioner · Core

## Widget tests

Widget tests build one widget or screen in a test environment, act on it the way a user would, and check what
appears. They run in seconds, without a device.

**What to learn:**

- `testWidgets`, `WidgetTester`, and finding widgets by text, type, key or semantics label
- Tapping and typing, then calling `pump` or `pumpAndSettle` so the screen updates
- Testing behaviour, not implementation details such as private state

**Resources:** [An introduction to widget testing](https://docs.flutter.dev/cookbook/testing/widget/introduction),
Flutter documentation

**Level:** Practitioner · Core

## Testing API calls

Tests should show what each screen does when the API is slow, fails or returns nothing, without a real back end.

**What to learn:**

- Replacing the API service with a fake or a `mocktail` mock that returns success, errors and delays
- Overriding Riverpod providers in tests, so each test starts with fresh state
- Testing the 401, 403, 404, 409, 422, 5xx and network-failure states from the practice app's rules

**Resources:**

- [mocktail](https://pub.dev/packages/mocktail), pub.dev
- [Testing your providers](https://riverpod.dev/docs/how_to/testing), Riverpod documentation

**Level:** Practitioner · Core

## Integration tests

Integration tests run the real app on a simulator, an emulator or a phone. Flutter's `integration_test` package
drives the app from inside, and tools such as Patrol and Maestro can also tap system dialogs and settings.

**What to learn:**

- Writing integration tests with `integration_test`, and running them on both platforms
- Creating test data, such as a new user, inside each test, so tests are independent
- Using Maestro or Patrol for what `integration_test` cannot do from inside the app, such as permission dialogs,
  opening a deep link and turning off the network, and knowing the limits: Maestro can turn on aeroplane mode only on
  Android

**Resources:**

- [Integration testing](https://docs.flutter.dev/testing/integration-tests), Flutter documentation
- [Patrol documentation](https://patrol.leancode.co/)
- [Maestro documentation](https://docs.maestro.dev/)

**Level:** Advanced · Core

## Accessibility testing

Automated checks find some problems, such as small touch targets and missing labels. Screen readers and larger text
find the rest.

**What to learn:**

- Flutter's accessibility guidelines in widget tests, such as `meetsGuideline(androidTapTargetGuideline)` and
  `meetsGuideline(labeledTapTargetGuideline)`
- Going through each flow with VoiceOver and TalkBack
- Checking every screen with the largest text size and in dark mode

**Resources:** [Accessibility testing](https://docs.flutter.dev/ui/accessibility/accessibility-testing), Flutter
documentation

**Level:** Advanced · Core

## Testing in continuous integration

Tests only protect the app when they run on every change. Unit and widget tests run on any server; integration tests
need a simulator or emulator.

**What to learn:**

- Running `dart format`, `flutter analyze` and `flutter test` on every pull request
- Running integration tests on a build in continuous integration

**Resources:** [Continuous delivery with Flutter](https://docs.flutter.dev/deployment/cd), Flutter documentation

**Level:** Advanced · Optional

## Project: Test Every Flow

**Brief:** Add unit tests, widget tests, tests against a mocked API and integration tests to the practice app. Write the
flows listed on the [practice app](../practice-app.md#test-flows) page with `integration_test`, and use Maestro or
Patrol for flow 6 (deep links) and flow 7 (offline).

**Size:** 4 days

**Verification**, checked by a reviewer:

- [ ] Unit tests cover the API client, the repositories and the view models
- [ ] Widget tests cover the article preview, the feed, every form and its validation errors
- [ ] Tests show each screen's response to 401, 403, 404, 409, 422, 5xx and network failures
- [ ] All seven practice-app test flows pass on an Android emulator, and flows 1–6 pass on an iOS simulator; the pull
  request explains how the offline states are covered on iOS
- [ ] Each flow creates its own test user with generated data, and flows pass in any order
- [ ] Tests find widgets by text or semantics label, and the pull request explains every key used
- [ ] Widget tests check the tap target and label guidelines on the home, article and sign-in screens, and VoiceOver
  and TalkBack can complete the sign-in flow
- [ ] Formatting, analysis, unit tests and widget tests run in continuous integration, and a failing test blocks the
  merge

Previous: [08. Device Features](./08-device-features.md) · Next:
[10. Performance and Release](./10-performance-and-release.md)
