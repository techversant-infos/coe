# 10. Performance and Release

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-12 · **Next review:** 2027-02-12

A mobile app is finished when it starts quickly, scrolls smoothly, and reaches users through the stores with a safe
way to fix problems. This stage covers performance, builds, store rules, updates and crash reporting. Back to the
[roadmap](./README.md).

## Measuring performance

Users judge an app by how fast it starts and how smoothly it scrolls. Measure on a real, mid-range device in profile
mode, because debug builds are much slower.

**What to learn:**

- Running the app in profile mode, and reading the Performance view in Flutter DevTools
- Finding frames that take too long to draw, slow builds and expensive layouts, and the difference between work on the
  user interface (UI) thread and the raster thread, which turns each frame into pixels
- Fixing common causes: rebuilding too much, heavy list items, large images and work in `build` methods

**Resources:**

- [Performance](https://docs.flutter.dev/perf), Flutter documentation
- [Flutter performance profiling](https://docs.flutter.dev/perf/ui-performance), Flutter documentation

**Level:** Advanced · Core

## App size

A large download puts users off, especially on mobile data. Every package and asset adds to the size.

**What to learn:**

- Measuring size with `--analyze-size`, and reading the report in DevTools; it works only on release builds and
  cannot be combined with `--split-debug-info`, so make a separate build for the size report
- The download and install size of the whole app, as the stores report it
- Removing large or unused packages, and sizing images and fonts for phones

**Resources:** [Measuring your app's size](https://docs.flutter.dev/perf/app-size), Flutter documentation

**Level:** Advanced · Core

## Builds, flavours and signing

Store builds must be signed with keys that prove they come from the developer. Flavours give one code base separate
development and production builds, each with its own settings and app ID (the application ID on Android and the bundle
ID on iOS).

**What to learn:**

- Flavours for development and production, each with its own API address and app ID
- Signing Android builds with an upload key, and why the keystore and `key.properties` must never be committed
- Signing iOS builds in Xcode, and who in the team owns the signing certificates
- Version numbers in `pubspec.yaml`, such as `1.2.0+7`, where the build number after `+` rises with every store
  upload
- The app icon and splash screen for both platforms
- Upgrading Flutter regularly, because new store rules arrive with new versions

**Resources:**

- [Build and release an Android app](https://docs.flutter.dev/deployment/android) and
  [Build and release an iOS app](https://docs.flutter.dev/deployment/ios), Flutter documentation
- [Set up Flutter flavours for Android](https://docs.flutter.dev/deployment/flavors) and
  [Set up Flutter flavours for iOS and macOS](https://docs.flutter.dev/deployment/flavors-ios), Flutter documentation
- [Upgrading Flutter](https://docs.flutter.dev/release/upgrade), Flutter documentation
- [Keys and secrets management](../../../../security/audit/security-audit-reference.md#63-keys-and-secrets-management),
  in the Techversant security audit reference

**Level:** Advanced · Core

## Obfuscation and debug symbols

Release builds can hide Dart names with `--obfuscate`, which makes the app harder to read but does not protect
secrets. The debug symbols must be kept, or crash reports cannot be read.

**What to learn:**

- Building with `--obfuscate --split-debug-info`, and keeping the symbol files for every release
- Why obfuscation does not encrypt resources or stop reverse engineering

**Resources:** [Obfuscating Dart code](https://docs.flutter.dev/deployment/obfuscate), Flutter documentation

**Level:** Advanced · Core

## Store requirements

Apple and Google set rules for what apps may do and how they are built, and both review apps before release.

**What to learn:**

- Apple's App Review Guidelines and Google Play's policies, including the privacy details each store needs
- In-app account deletion for any app that lets users sign up, which Apple requires, and Apple's privacy manifest
  for the app and its packages
- Current build rules: App Store uploads must be built with Xcode 26 or later, and Google Play apps must target
  Android 16 (API level 36) or higher since 31 August 2026
- Internal and closed testing tracks, such as TestFlight on iOS and internal testing on Google Play, before any public
  release

**Resources:**

- [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) and
  [Upcoming requirements](https://developer.apple.com/news/upcoming-requirements/), Apple
- [Privacy manifest files](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files), Apple
- [Target API level requirements](https://support.google.com/googleplay/android-developer/answer/11926878), Google
  Play

**Level:** Advanced · Core

## Over-the-air updates

Flutter apps are compiled to native code, so a fix normally needs a new store release. Some teams use Shorebird to
send Dart changes to installed apps. It is fast, but it must not change what the app does in ways the store
reviewed.

**What to learn:**

- When a store release is the right way to ship a fix, and when an over-the-air patch is allowed
- Patches that target one release, rolling them out to testers first, and rolling a bad patch back

**Resources:** [Shorebird documentation](https://docs.shorebird.dev/)

**Level:** Advanced · Optional

## Crash reporting and security checks

When an app crashes on a user's phone, you need to know before the store reviews say so. Before release, check the
app against a mobile security standard.

**What to learn:**

- Sending crashes and errors to the monitoring tool your project uses, such as Sentry, with readable stack traces
- Uploading debug symbols after every build, so obfuscated stack traces can be read
- Never sending tokens, passwords or personal data in crash reports and logs
- The monitoring tool's upload token is a build secret: keep it in the build service's secret variables, never in a
  `--dart-define` value or the repository
- Checking the app against the OWASP (Open Worldwide Application Security Project) Mobile Application Security
  Verification Standard (MASVS), and confirming no secret is built into the app

**Resources:**

- [Sentry for Flutter](https://docs.sentry.io/platforms/dart/guides/flutter/), Sentry documentation
- [OWASP MASVS](https://mas.owasp.org/MASVS/)
- [What must never be logged](../../../../security/audit/security-audit-reference.md#112-what-must-never-be-logged),
  in the Techversant security audit reference

**Level:** Advanced · Core

## Project: Make It Release-Ready

**Brief:** Prepare the practice app for release: measure and improve performance, set up flavours, signing and
crash reporting, and distribute a build through internal testing only, as the
[practice app](../practice-app.md#release-rules) page requires. Have a senior engineer review the release set-up.

**Size:** 4 days

**Verification**, checked by a reviewer:

- [ ] The pull request records startup time and frame times while scrolling on a mid-range Android phone in profile
  mode, before and after one improvement
- [ ] An `--analyze-size` report shows the app's size, the pull request gives a reason for each of the largest
  packages, and it records the app's download size
- [ ] Development and production flavours have their own API address and app ID
- [ ] The build number rises with every upload, and no keystore, `key.properties`, certificate or upload token is in
  the repository
- [ ] Release builds use `--obfuscate --split-debug-info`, and the symbol files are kept outside the repository
- [ ] A tester installs a build through an internal testing track or TestFlight, never a public listing
- [ ] The Android build targets API level 36 or higher, and the iOS build uses Xcode 26 or later
- [ ] A test crash appears in the monitoring tool with a readable stack trace and no token or personal data
- [ ] A MASVS checklist is completed for storage, network, authentication, platform interaction and privacy
- [ ] Users can delete their account from the app, or the pull request explains how that would work against an API
  that has no delete endpoint
- [ ] A senior engineer has reviewed the release set-up, and the review is linked in the pull request

Previous: [09. Testing](./09-testing.md) · Back to the [roadmap](./README.md#capstone) for the capstone
