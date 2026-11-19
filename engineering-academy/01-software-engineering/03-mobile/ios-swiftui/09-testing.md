# 09. Testing

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-18 · **Next review:** 2027-05-18

Tests let you change an app without fear of breaking it on an iPhone you do not own. A good mix has many fast unit
tests, some tests against a stubbed API, and a few user interface (UI) tests that drive the real app. Back to the
[roadmap](./README.md).

## Unit tests

Unit tests check one type or function, such as a model or the API client, without drawing anything on screen. New
tests use Swift Testing; older projects use XCTest, and both can run in the same test target.

**What to learn:**

- `@Test`, `#expect` and `#require`, and grouping tests in a suite
- Parameterised tests, which run one test with many inputs, such as every invalid email format
- Testing models by giving them fake services instead of real ones, and testing `async` code

**Resources:**

- [Swift Testing](https://developer.apple.com/documentation/testing), Apple
- [Test levels](../../../00-engineering-foundations/07-testing-and-refactoring.md#test-levels), in Engineering
  Foundations

**Level:** Practitioner · Core

## Testing API calls

Tests should show what each screen's model does when the API is slow, fails or returns nothing, without a real back
end.

**What to learn:**

- Replacing the network with a `URLProtocol` stub, or the API service with a fake that returns success, errors and
  delays
- Starting each test with fresh state, so tests pass in any order
- Testing the 401, 403, 404, 409, 422, 5xx and network-failure states from the practice app's rules

**Resources:** [URLProtocol](https://developer.apple.com/documentation/foundation/urlprotocol), Apple

**Level:** Practitioner · Core

## UI tests

UI tests launch the real app in the Simulator and tap, type and check what is on screen, the way a user would. They
use the XCUIAutomation framework with XCTest.

**What to learn:**

- Finding elements by accessibility label or visible text, and adding an `accessibilityIdentifier` only where there
  is neither
- Creating test data, such as a new user, inside each test, and passing launch arguments (values the test hands to the
  app when it starts) to choose the test settings
- Opening deep links from a test with `XCUIApplication.open(_:)`, and the limits: a test cannot turn off the
  Simulator's network, so the offline states need a launch argument that makes the network layer fail

**Resources:** [XCUIAutomation](https://developer.apple.com/documentation/xcuiautomation), Apple

**Level:** Advanced · Core

## Accessibility testing

Automated checks find some problems, such as missing labels, small touch targets and text that does not fit. VoiceOver
and larger text find the rest.

**What to learn:**

- `performAccessibilityAudit()` in UI tests, and Accessibility Inspector in Xcode
- Going through each flow with VoiceOver
- Checking every screen with the largest Dynamic Type size and in dark mode

**Resources:**
[Performing accessibility audits for your app](https://developer.apple.com/documentation/accessibility/performing-accessibility-audits-for-your-app),
Apple

**Level:** Advanced · Core

## Testing in continuous integration

Tests only protect the app when they run on every change. Unit tests and UI tests both need a Mac with Xcode, such as
Xcode Cloud or a macOS runner.

**What to learn:**

- Running the formatter, the linter and `xcodebuild test` on every pull request
- Running UI tests on more than one simulated device, such as a small and a large iPhone

**Resources:** [Xcode Cloud](https://developer.apple.com/documentation/xcode/xcode-cloud), Xcode documentation

**Level:** Advanced · Core

## Project: Test Every Flow

**Brief:** Add unit tests, tests against a stubbed API and UI tests to the practice app. Write every flow listed on
the [practice app](../practice-app.md#test-flows) page as a UI test.

**Size:** 4 days

**Verification**, checked by a reviewer:

- [ ] Swift Testing tests cover the API client, the repositories and the models, including form validation
- [ ] Tests show each screen's response to 401, 403, 404, 409, 422, 5xx and network failures
- [ ] Practice-app flows 1–6 pass as UI tests in the Simulator, and flow 6 opens its links with
  `XCUIApplication.open(_:)`
- [ ] Flow 7's offline states are tested with a launch argument that makes the network layer fail, checked once by
  hand with the network off, and the pull request explains how
- [ ] Each flow creates its own test user with generated data, and flows pass in any order
- [ ] UI tests find elements by accessibility label or text, and the pull request explains every identifier used
- [ ] `performAccessibilityAudit()` passes on the home, article and sign-in screens, or the pull request explains each
  remaining issue, and VoiceOver can complete the sign-in flow
- [ ] Formatting, linting and unit tests run in continuous integration, and a failing test blocks the merge

Previous: [08. Device Features](./08-device-features.md) · Next:
[10. Performance and Release](./10-performance-and-release.md)
