# 08. Device Features

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-12 · **Next review:** 2027-02-12

Mobile apps can share content, work offline, send notifications and use the camera. Each feature adds permissions,
native code and new ways to fail. This stage adds a few of them to the practice app. Back to the
[roadmap](./README.md).

## Plugins and native code

Flutter reaches device features through plugins: packages with Dart code on top and native iOS and Android code
underneath.

**What to learn:**

- Choosing a plugin: platform support, maintenance and the permissions it adds, checked on pub.dev
- The native set-up many plugins need, such as entries in `Info.plist` and the Android manifest
- Platform channels, for calling your own native code when no plugin fits, and when that is justified

**Resources:**
[Writing custom platform-specific code](https://docs.flutter.dev/platform-integration/platform-channels), Flutter
documentation

**Level:** Advanced · Core

## Sharing and opening links

Users share articles with friends, and open links from articles. Both should use the platform's own tools.

**What to learn:**

- The system share sheet with `share_plus`, sharing an article's title and web address
- Opening links in an in-app browser view or the system browser with `url_launcher`

**Resources:**

- [share_plus](https://pub.dev/packages/share_plus), pub.dev
- [url_launcher](https://pub.dev/packages/url_launcher), pub.dev

**Level:** Practitioner · Core

## Offline reading

Users expect to read what they already loaded, even without a connection. Saving recent data on the device makes the
last feed and articles available offline.

**What to learn:**

- An offline-first repository that reads saved data first and updates it from the API
- Choosing local storage: `shared_preferences` for small settings, and a database such as Drift for lists of articles
- Showing that content is saved and may be out of date, and deleting a signed-in user's saved data on sign-out

**Resources:** [Offline-first support](https://docs.flutter.dev/app-architecture/design-patterns/offline-first),
Flutter documentation

**Level:** Advanced · Core

## Notifications

Notifications bring users back, but too many make them turn notifications off. Local notifications are scheduled by
the app; push notifications come from a server.

**What to learn:**

- Asking for notification permission at the moment it makes sense, and handling a refusal
- Scheduling a local notification with `flutter_local_notifications`, and opening the right screen when the user taps
  it
- How push notifications work through Apple's and Google's push services

**Resources:** [flutter_local_notifications](https://pub.dev/packages/flutter_local_notifications), pub.dev

**Level:** Advanced · Core

## Camera and photos

Many client apps take photos or pick images from the library. The practice API stores image addresses, not files, so
this topic is for client work.

**What to learn:**

- Picking an image or taking a photo with `image_picker`, with the permission request at the right moment
- Resizing an image before upload, and what location data photos can carry

**Resources:** [image_picker](https://pub.dev/packages/image_picker), pub.dev

**Level:** Practitioner · Optional

## Project: Add Sharing, Offline Reading and Reminders

**Brief:** Add three device features to the practice app: share an article, read the last loaded feed and articles
offline, and save the editor draft on the device and remind the user to finish it with a local notification.

**Size:** 3 days

**Verification**, checked by a reviewer:

- [ ] The article screen opens the system share sheet with the article's title and link
- [ ] Links in article bodies open in an in-app browser view or the system browser
- [ ] With the network off, the last loaded feed and articles still show, marked as saved
- [ ] Sign-out removes all saved user data, and saved data never contains the token
- [ ] The app asks for notification permission only when the user turns on draft reminders, and works normally if
  the user says no
- [ ] Tapping the reminder opens the editor with the draft
- [ ] The pull request lists every plugin added, with its platform support and the permissions it needs

Previous: [07. Working with APIs](./07-working-with-apis.md) · Next: [09. Testing](./09-testing.md)
