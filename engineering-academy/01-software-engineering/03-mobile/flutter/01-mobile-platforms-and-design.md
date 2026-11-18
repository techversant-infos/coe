# 01. Mobile Platforms and Design

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-12 · **Next review:** 2027-02-12

A mobile app runs on a small screen, on a battery, on a network that comes and goes, inside rules set by Apple and
Google. This stage covers how the platforms work and how users expect apps to behave, before you write any code.
Back to the [roadmap](./README.md).

## iOS and Android

Flutter builds one app for two platforms, and each has its own conventions. Users notice when an app ignores them,
even though Flutter draws the interface itself.

**What to learn:**

- How the platforms differ: navigation patterns, back behaviour (the Android back gesture and button), system
  fonts and controls
- Apple's Human Interface Guidelines and Google's Material Design, and the behaviour Flutter already adapts for
  each platform, such as scrolling, back navigation and text selection
- Screen sizes, safe areas around notches and system bars, portrait and landscape, and phones compared with tablets

**Resources:**

- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines), Apple
- [Material Design 3](https://m3.material.io/), Google

**Level:** Practitioner · Core

## The app lifecycle

The operating system starts, pauses and stops apps without asking. An app must save what matters and recover
cleanly when the user comes back.

**What to learn:**

- Foreground, background and terminated states, and what happens to a running request when the user leaves the app
- Saving a draft or the current screen so nothing is lost when the system closes the app
- Refreshing data when the app returns to the foreground

**Resources:** [AppLifecycleListener](https://api.flutter.dev/flutter/widgets/AppLifecycleListener-class.html),
Flutter API documentation

**Level:** Practitioner · Core

## Mobile accessibility

Many people use their phones with a screen reader, larger text or a switch device. Accessibility on mobile uses the
platform's own tools, not web standards.

**What to learn:**

- VoiceOver on iOS and TalkBack on Android, and testing every screen with them
- Accessibility labels, roles and states, and touch targets of at least 44 by 44 points on iOS and 48 by 48
  density-independent pixels on Android
- Supporting the user's text size setting, and contrast that works in light and dark mode

**Resources:**

- [Accessibility](https://docs.flutter.dev/ui/accessibility), Flutter documentation
- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility), Apple Human
  Interface Guidelines

**Level:** Practitioner · Core

## Permissions and privacy

Access to the camera, location, contacts or notifications needs the user's permission, and the stores check how an
app uses personal data.

**What to learn:**

- Asking for a permission only when the user starts the feature that needs it, and explaining why
- Handling "denied" and "denied permanently", with a way to open the system settings
- The privacy details each store asks for: Apple's privacy labels and Google Play's data safety form

**Resources:**

- [permission_handler](https://pub.dev/packages/permission_handler), the common Flutter package for permissions
- [App privacy details](https://developer.apple.com/app-store/app-privacy-details/), Apple, and
  [Data safety](https://support.google.com/googleplay/android-developer/answer/10787469), Google Play

**Level:** Practitioner · Core

## Mobile security basics

A phone can be lost, shared or compromised, and anyone can unpack an app's files. Plan what must never be stored or
shipped in the app.

**What to learn:**

- Why anything in the app bundle, such as an API key, can be read by anyone who downloads the app
- Secure storage for tokens, and never storing secrets in plain files or logs
- The OWASP (Open Worldwide Application Security Project) Mobile Application Security Verification Standard
  (MASVS) as a checklist for mobile apps

**Resources:**

- [OWASP MASVS](https://mas.owasp.org/MASVS/)
- [Obfuscating Dart code](https://docs.flutter.dev/deployment/obfuscate), Flutter documentation, on why secrets do
  not belong in an app

**Level:** Practitioner · Core

## Project: Plan the App

**Brief:** Read the [practice app](../practice-app.md) page and plan the RealWorld mobile client before you write
code. Sketch every screen, show how users move between them on each platform, and list the permissions and data the
app needs.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] Sketches cover every screen in the practice app, including loading, empty, error and signed-out states
- [ ] A navigation map shows the tabs and stacks, and how the Android back gesture behaves on each screen
- [ ] The plan notes where iOS and Android differ, and why each choice follows the platform
- [ ] An accessibility plan lists the label for every icon-only button and the order a screen reader reads each
  screen
- [ ] A data list shows what the app stores on the device, where, and why; the token is in secure storage only
- [ ] The plan lists every permission the app asks for, with the moment it asks and what happens if the user says no

Next: [02. Dart](./02-dart.md)
