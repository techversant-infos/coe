# 10. Performance and Release

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-11 · **Next review:** 2027-02-11

A mobile app is finished when it starts quickly, scrolls smoothly, and reaches users through the stores with a safe
way to fix problems. This stage covers performance, builds, store rules, updates and crash reporting. Back to the
[roadmap](./README.md).

## Measuring performance

Users judge an app by how fast it starts and how smoothly it scrolls. Measure on a real, mid-range device in a
release build, because development builds are much slower.

**What to learn:**

- Startup time, dropped frames while scrolling, and memory use, measured in a release build
- Finding slow renders with the React Native DevTools profiler in a development build, then confirming each
  improvement with timings from a release build
- Fixing common causes: heavy list items, large images and work done on every render

**Resources:** [Performance overview](https://reactnative.dev/docs/performance), React Native documentation

**Level:** Advanced · Core

## App size

A large download puts users off, especially on mobile data. Every library adds to the size.

**What to learn:**

- Analysing the JavaScript bundle with Expo Atlas, and removing large or unused libraries
- The download and install size of the whole app, as the build and the stores report it
- Sizing images and other assets for phones

**Resources:**

- [Analyzing JavaScript bundles](https://docs.expo.dev/guides/analyzing-bundles/), Expo documentation
- [Understanding app size](https://docs.expo.dev/distribution/app-size/), Expo documentation

**Level:** Advanced · Core

## Builds and signing

Store builds must be signed with keys that prove they come from the developer. Expo Build, formerly called EAS
Build and part of Expo Application Services, creates signed iOS and Android builds in the cloud.

**What to learn:**

- Build profiles in `eas.json` for development, preview and production
- App signing credentials, who owns them, and why they must never be committed to the repository
- Internal distribution, so testers install builds without a store listing
- Version numbers and build numbers that rise with every store upload, managed by the build service
- The app icon and splash screen for both platforms
- Upgrading the Expo software development kit (SDK) each year, because new store rules arrive with new SDK versions

**Resources:**

- [Expo Build](https://docs.expo.dev/build/introduction/) and
  [App version management](https://docs.expo.dev/build-reference/app-versions/), Expo documentation
- [Upgrade Expo SDK](https://docs.expo.dev/workflow/upgrading-expo-sdk-walkthrough/), Expo documentation
- [App credentials](https://docs.expo.dev/app-signing/app-credentials/), Expo documentation
- [Keys and secrets management](../../../../security/audit/security-audit-reference.md#63-keys-and-secrets-management),
  in the Techversant security audit reference

**Level:** Advanced · Core

## Store requirements

Apple and Google set rules for what apps may do and how they are built, and both review apps before release.

**What to learn:**

- Apple's App Review Guidelines and Google Play's policies, including the privacy details each store needs
- In-app account deletion for any app that lets users sign up, which Apple requires, and Apple's privacy manifest
  for the app and its libraries
- Current build rules: App Store uploads must be built with Xcode 26 or later, and Google Play apps must target
  Android 16 (API level 36) or higher since 31 August 2026
- Internal and closed testing tracks, before any public release

**Resources:**

- [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) and
  [Upcoming requirements](https://developer.apple.com/news/upcoming-requirements/), Apple
- [Privacy manifests](https://docs.expo.dev/guides/apple-privacy/), Expo documentation
- [Target API level requirements](https://support.google.com/googleplay/android-developer/answer/11926878), Google
  Play

**Level:** Advanced · Core

## Over-the-air updates

Expo Update, formerly called EAS Update, sends JavaScript and asset changes to installed apps without a store release.
It is fast, but it must not
change what the app does in ways the store reviewed.

**What to learn:**

- Runtime versions, which stop an update reaching a build whose native code does not match
- Channels for preview and production, and rolling an update out gradually
- Rolling back a bad update, and the store rules on what an update may change

**Resources:**

- [Expo Update](https://docs.expo.dev/eas-update/introduction/), Expo documentation
- [Runtime versions](https://docs.expo.dev/eas-update/runtime-versions/), Expo documentation

**Level:** Advanced · Core

## Crash reporting and security checks

When an app crashes on a user's phone, you need to know before the store reviews say so. Before release, check the
app against a mobile security standard.

**What to learn:**

- Sending crashes and errors to the monitoring tool your project uses, such as Sentry, with readable stack traces
- Never sending tokens, passwords or personal data in crash reports and logs
- The monitoring tool's upload token is a build secret: keep it in the build service's secret variables, never in an
  `EXPO_PUBLIC_` variable or the repository, and upload source maps after every update as well as every build
- Checking the app against the OWASP (Open Worldwide Application Security Project) Mobile Application Security
  Verification Standard (MASVS), and confirming no secret is built into the app

**Resources:**

- [Using Sentry](https://docs.expo.dev/guides/using-sentry/), Expo documentation
- [OWASP MASVS](https://mas.owasp.org/MASVS/)
- [What must never be logged](../../../../security/audit/security-audit-reference.md#112-what-must-never-be-logged),
  in the Techversant security audit reference

**Level:** Advanced · Core

## Project: Make It Release-Ready

**Brief:** Prepare the practice app for release: measure and improve performance, set up build profiles and crash
reporting, deliver an over-the-air update, and distribute it through internal testing only, as the
[practice app](../practice-app.md#release-rules) page requires. Have a senior engineer review the release set-up.

**Size:** 4 days

**Verification**, checked by a reviewer:

- [ ] The pull request records startup time and scrolling smoothness on a mid-range Android phone in a release build,
  before and after one improvement
- [ ] An Expo Atlas report shows the bundle, the pull request gives a reason for each of the largest libraries, and
  it records the app's download size
- [ ] `eas.json` has development, preview and production profiles, build numbers rise automatically, and no signing
  credential or upload token is in the repository
- [ ] A tester installs a preview build through internal distribution or an internal testing track, never a public
  listing
- [ ] An over-the-air update reaches the preview build, and the pull request shows how to roll it back
- [ ] The Android build targets API level 36 or higher, and the iOS build uses Xcode 26 or later
- [ ] A test crash appears in the monitoring tool with a readable stack trace and no token or personal data
- [ ] A MASVS checklist is completed for storage, network, authentication, platform interaction and privacy
- [ ] Users can delete their account from the app, or the pull request explains how that would work against an API
  that has no delete endpoint
- [ ] A senior engineer has reviewed the release set-up, and the review is linked in the pull request

Previous: [09. Testing](./09-testing.md) · Back to the [roadmap](./README.md#capstone) for the capstone
