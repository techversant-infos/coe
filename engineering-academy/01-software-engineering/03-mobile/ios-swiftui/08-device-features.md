# 08. Device Features

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-18 · **Next review:** 2027-02-18

iPhone apps can share content, work offline, send notifications and use the camera. Each feature adds permissions,
settings and new ways to fail. This stage adds a few of them to the practice app. Back to the
[roadmap](./README.md).

## Apple frameworks and capabilities

iOS gives native apps direct access to its frameworks. Some features also need a capability, which adds an entitlement
(a permission Apple signs into the app) and may need set-up in the Apple Developer account.

**What to learn:**

- Finding the Apple framework for a feature before reaching for a third-party package
- Adding capabilities in Xcode, such as Push Notifications and Associated Domains, and the purpose strings in
  `Info.plist` that permissions need
- Checking a third-party package's maintenance, licence and privacy manifest before you add it

**Resources:** [Capabilities](https://developer.apple.com/documentation/xcode/capabilities), Xcode documentation

**Level:** Advanced · Core

## Sharing and opening links

Users share articles with friends, and open links from articles. Both should use the system's own tools.

**What to learn:**

- The system share sheet with `ShareLink`, sharing an article's title and link
- Opening web links in an in-app browser with `SFSafariViewController`, shown in SwiftUI through
  `UIViewControllerRepresentable` as in stage 03, or in Safari

**Resources:**

- [ShareLink](https://developer.apple.com/documentation/swiftui/sharelink), SwiftUI documentation
- [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller), Apple

**Level:** Practitioner · Core

## Offline reading

Users expect to read what they already loaded, even without a connection. Saving recent data on the device makes the
last feed and articles available offline.

**What to learn:**

- A repository that shows saved data first and updates it from the API
- Choosing local storage: `UserDefaults` for small settings, and SwiftData or files for lists of articles
- Showing that content is saved and may be out of date, and deleting a signed-in user's saved data on sign-out

**Resources:** [SwiftData](https://developer.apple.com/documentation/swiftdata), Apple

**Level:** Advanced · Core

## Notifications

Notifications bring users back, but too many make them turn notifications off. Local notifications are scheduled by
the app; push notifications come from a server through the Apple Push Notification service (APNs).

**What to learn:**

- Asking for notification permission at the moment it makes sense, and handling a refusal
- Scheduling a local notification with the User Notifications framework, and opening the right screen when the user
  taps it
- How push notifications work: the app sends its push device token to your server, linked to the signed-in user,
  and the server removes the link on sign-out

**Resources:**
[Scheduling a notification locally from your app](https://developer.apple.com/documentation/usernotifications/scheduling-a-notification-locally-from-your-app),
Apple

**Level:** Advanced · Core

## Camera and photos

Many client apps take photos or pick images from the library. The practice API stores image addresses, not files, so
this topic is for client work.

**What to learn:**

- Picking images with `PhotosPicker`, which needs no photo library permission, and the camera, which does
- Resizing an image before upload, and what location data photos can carry

**Resources:** [PhotosPicker](https://developer.apple.com/documentation/photosui/photospicker), Apple

**Level:** Practitioner · Optional

## Project: Add Sharing, Offline Reading and Reminders

**Brief:** Add three device features to the practice app: share an article, read the last loaded feed and articles
offline, and save the editor draft on the device and remind the user to finish it with a local notification.

**Size:** 3 days

**Verification**, checked by a reviewer:

- [ ] The article screen opens the system share sheet with the article's title and link
- [ ] Links in article bodies open in `SFSafariViewController` or Safari
- [ ] With the network off, the last loaded feed and articles still show, marked as saved
- [ ] Sign-out removes all saved user data, and saved data never contains the token
- [ ] The app asks for notification permission only when the user turns on draft reminders, and works normally if
  the user says no
- [ ] Tapping the reminder opens the editor with the draft
- [ ] The pull request lists every capability, permission and third-party package added, with the reason for each

Previous: [07. Working with APIs](./07-working-with-apis.md) · Next: [09. Testing](./09-testing.md)
