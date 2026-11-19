# 10. Performance and Release

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-18 · **Next review:** 2027-02-18

An iPhone app is finished when it starts quickly, scrolls smoothly, and reaches users through the App Store with a
safe way to fix problems. This stage covers performance, builds, App Store rules, updates and crash reporting. Back
to the [roadmap](./README.md).

## Measuring performance

Users judge an app by how fast it starts and how smoothly it scrolls. Measure on a real iPhone in a Release build,
because Debug builds are slower.

**What to learn:**

- Profiling with Instruments: the Time Profiler, the Hangs instrument and the SwiftUI instrument
- Finding views that update too often, slow work on the main actor and large images
- Startup time, hangs and memory as Xcode Organizer reports them from users' devices after release

**Resources:**
[Improving app responsiveness](https://developer.apple.com/documentation/xcode/improving-app-responsiveness), Xcode
documentation

**Level:** Advanced · Core

## App size

A large download puts users off, especially on mobile data. Every package, image and font adds to the size.

**What to learn:**

- The App Thinning Size Report, created when you archive the app (covered in the next topic), and the sizes App Store
  Connect shows for each device
- Removing large or unused packages, and keeping images in the asset catalogue so each device downloads only its size

**Resources:** [Reducing your app's size](https://developer.apple.com/documentation/xcode/reducing-your-app-s-size),
Xcode documentation

**Level:** Advanced · Core

## Builds, schemes and signing

App Store builds must be signed with a certificate and provisioning profile from the team's Apple Developer account.
Schemes and build configurations give one project separate development and production builds.

**What to learn:**

- Schemes and build configurations for development and production, each with its own API address and bundle ID
- Automatic signing, certificates and provisioning profiles, who in the team owns the Apple Developer account, and why
  signing files and keys must never be committed
- The version and build numbers (`MARKETING_VERSION` and `CURRENT_PROJECT_VERSION`), where the build number rises
  with every upload
- The app icon and launch screen, and archiving and uploading a build from Xcode
- Upgrading Xcode each year, because new App Store rules arrive with new software development kits (SDKs)

**Resources:**

- [Customising the build schemes for a project](https://developer.apple.com/documentation/xcode/customizing-the-build-schemes-for-a-project),
  Xcode documentation
- [Distributing your app for beta testing and releases](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases),
  Xcode documentation
- [Keys and secrets management](../../../../security/audit/security-audit-reference.md#63-keys-and-secrets-management),
  in the Techversant security audit reference

**Level:** Advanced · Core

## App Store requirements

Apple sets rules for what apps may do and how they are built, and reviews every app before release.

**What to learn:**

- Apple's App Review Guidelines, and the privacy details App Store Connect needs
- In-app account deletion for any app that lets users sign up, which Apple requires, and the privacy manifest for the
  app and its packages
- Current build rules: App Store uploads must be built with the iOS 26 SDK or later, which means Xcode 26 or later,
  and from April 2027 with the iOS 27 SDK or later
- TestFlight internal and external testing, before any public release

**Resources:**

- [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/), Apple
- [App Store submissions now open for the latest OS releases](https://developer.apple.com/news/?id=k1mtkt1k), Apple
- [Privacy manifest files](https://developer.apple.com/documentation/bundleresources/privacy-manifest-files), Apple
- [TestFlight](https://developer.apple.com/testflight/), Apple

**Level:** Advanced · Core

## Releasing updates

Native iOS apps cannot change their code without a new App Store release. Plan how each release reaches users and how
to limit the damage when one goes wrong.

**What to learn:**

- Phased release, which spreads an update over seven days and can be paused if problems appear
- Why the App Review Guidelines forbid downloading code that changes what the app does, and what remote settings and
  feature flags may still change
- Keeping the app working with older API responses while users update at different times

**Resources:**
[Release a version update in phases](https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases),
App Store Connect Help

**Level:** Advanced · Core

## Crash reporting and security checks

When an app crashes on a user's iPhone, you need to know before users complain in App Store reviews. Before release,
check the app against a mobile security standard.

**What to learn:**

- Crash reports in Xcode Organizer, and the debug symbol files (dSYMs) that make them readable
- Sending crashes and errors to the monitoring tool your project uses, such as Sentry, and uploading dSYMs after every
  build
- Never sending tokens, passwords or personal data in crash reports and logs
- The monitoring tool's upload token is a build secret: keep it in the build service's secret variables, never in an
  `.xcconfig` file, `Info.plist` or the repository
- Checking the app against the OWASP (Open Worldwide Application Security Project) Mobile Application Security
  Verification Standard (MASVS), and confirming no secret is built into the app

**Resources:**

- [Acquiring crash reports and diagnostic logs](https://developer.apple.com/documentation/xcode/acquiring-crash-reports-and-diagnostic-logs),
  Xcode documentation
- [Sentry for iOS](https://docs.sentry.io/platforms/apple/guides/ios/), Sentry documentation
- [OWASP MASVS](https://mas.owasp.org/MASVS/)
- [What must never be logged](../../../../security/audit/security-audit-reference.md#112-what-must-never-be-logged),
  in the Techversant security audit reference

**Level:** Advanced · Core

## Project: Make It Release-Ready

**Brief:** Prepare the practice app for release: measure and improve performance, set up schemes, signing and crash
reporting, and distribute a build through TestFlight internal testing only, using developer accounts your lead approves,
as the
[practice app](../practice-app.md#release-rules) page requires. Have a senior engineer review the release set-up.

**Size:** 4 days

**Verification**, checked by a reviewer:

- [ ] The pull request records startup time and an Instruments trace of scrolling the feed on an iPhone in a Release
  build, before and after one improvement
- [ ] An App Thinning Size Report shows the app's size, and the pull request gives a reason for each of the largest
  packages
- [ ] Development and production schemes have their own API address and bundle ID
- [ ] The build number rises with every upload, and no certificate, private key, profile or upload token is in the
  repository
- [ ] A tester installs a build through TestFlight internal testing, never a public listing
- [ ] The build uses Xcode 26 or later with the iOS 26 SDK or later, and the pull request notes the April 2027 move to
  the iOS 27 SDK
- [ ] A test crash appears in the monitoring tool with a readable stack trace and no token or personal data
- [ ] A MASVS checklist is completed for storage, network, authentication, platform interaction and privacy
- [ ] Users can delete their account from the app, or the pull request explains how that would work against an API
  that has no delete endpoint
- [ ] A senior engineer has reviewed the release set-up, and the review is linked in the pull request

Previous: [09. Testing](./09-testing.md) · Back to the [roadmap](./README.md#capstone) for the capstone
