# 01. iOS Platform and Design

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-18 · **Next review:** 2027-02-18

An iPhone app runs on a small screen, on a battery, on a network that comes and goes, inside rules set by Apple. This
stage covers how iOS works and how iPhone users expect apps to behave, before you write any code. Back to the
[roadmap](./README.md).

## Apple's design rules

iPhone users know how apps should look and move, because most apps follow Apple's Human Interface Guidelines. Users
notice when an app ignores them.

**What to learn:**

- Navigation patterns on iPhone: tab bars, navigation stacks with the back swipe, and sheets
- System fonts, SF Symbols (Apple's icon set) and standard controls, and when a custom design is worth the cost
- Screen sizes, safe areas around the Dynamic Island and the Home indicator, portrait and landscape, and iPhone
  compared with iPad

**Resources:**

- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines), Apple
- [SF Symbols](https://developer.apple.com/sf-symbols/), Apple

**Level:** Practitioner · Core

## The app lifecycle

iOS starts, suspends and stops apps without asking. An app must save what matters and recover cleanly when the user
comes back.

**What to learn:**

- Active, inactive and background states, and that iOS can end a suspended app at any time to free memory
- Saving a draft or the current screen so nothing is lost when the system closes the app
- Refreshing data when the app returns to the foreground, using SwiftUI's `scenePhase`

**Resources:** [ScenePhase](https://developer.apple.com/documentation/swiftui/scenephase), SwiftUI documentation

**Level:** Practitioner · Core

## Mobile accessibility

Many people use their iPhones with VoiceOver, larger text or Switch Control. Accessibility on iOS uses Apple's own
tools, not web standards.

**What to learn:**

- VoiceOver, Apple's screen reader, and testing every screen with it
- Accessibility labels, traits and values, and touch targets of at least 44 by 44 points
- Dynamic Type, the user's text size setting, and contrast that works in light and dark mode

**Resources:**

- [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility), Apple Human
  Interface Guidelines
- [Accessibility fundamentals](https://developer.apple.com/documentation/swiftui/accessibility-fundamentals), SwiftUI
  documentation

**Level:** Practitioner · Core

## Permissions and privacy

Access to the camera, location, contacts or notifications needs the user's permission, and Apple checks how an app
uses personal data.

**What to learn:**

- Asking for a permission only when the user starts the feature that needs it, with a purpose string in `Info.plist`
  that explains why
- Handling a refusal, with a way to open the app's page in the Settings app
- The privacy details Apple asks for: privacy labels on the App Store page, and the privacy manifest for the app and
  its packages

**Resources:**

- [Requesting access to protected resources](https://developer.apple.com/documentation/uikit/requesting-access-to-protected-resources),
  Apple
- [App privacy details](https://developer.apple.com/app-store/app-privacy-details/), Apple

**Level:** Practitioner · Core

## Mobile security basics

A phone can be lost, shared or compromised, and anyone can unpack an app's files. Plan what must never be stored or
shipped in the app.

**What to learn:**

- Why anything in the app bundle, such as an API key, can be read by anyone who downloads the app
- The Keychain for tokens, and never storing secrets in `UserDefaults`, plain files or logs
- App Transport Security, which blocks plain `http` connections by default, and why you should not turn it off
- The OWASP (Open Worldwide Application Security Project) Mobile Application Security Verification Standard
  (MASVS) as a checklist for mobile apps

**Resources:**

- [OWASP MASVS](https://mas.owasp.org/MASVS/)
- [Preventing insecure network connections](https://developer.apple.com/documentation/security/preventing-insecure-network-connections),
  Apple

**Level:** Practitioner · Core

## Project: Plan the App

**Brief:** Read the [practice app](../practice-app.md) page and plan the RealWorld iOS client before you write code.
Sketch every screen, show how users move between them, and list the permissions and data the app needs.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] Sketches cover every screen in the practice app, including loading, empty, error and signed-out states
- [ ] A navigation map shows the tabs, stacks and sheets, and where the back swipe goes on each screen
- [ ] The plan names the standard iOS controls and SF Symbols it uses, and explains any custom design
- [ ] An accessibility plan lists the label for every icon-only button and the order VoiceOver reads each screen
- [ ] A data list shows what the app stores on the device, where, and why; the token is in the Keychain only
- [ ] The plan lists every permission the app asks for, with the moment it asks, its purpose string and what happens
  if the user says no

Next: [02. Swift](./02-swift.md)
