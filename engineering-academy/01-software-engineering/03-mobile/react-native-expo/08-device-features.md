# 08. Device Features

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-11 · **Next review:** 2027-02-11

Mobile apps can share content, work offline, send notifications and use the camera. Each feature adds permissions,
native code and new ways to fail. This stage adds a few of them to the practice app. Back to the
[roadmap](./README.md).

## Expo modules and native code

Expo's libraries give JavaScript access to device features. Some need native set-up, which Expo applies when it
builds the app.

**What to learn:**

- Finding an Expo library for a feature, and checking which platforms it supports
- Config plugins, which change the native iOS and Android projects at build time
- Why a library with native code needs a new development build, and when writing your own native module is
  justified

**Resources:** [Config plugins](https://docs.expo.dev/config-plugins/introduction/), Expo documentation

**Level:** Advanced · Core

## Sharing and opening links

Users share articles with friends, and open links from articles. Both should use the platform's own tools.

**What to learn:**

- The system share sheet, sharing an article's title and web address
- Opening links in an in-app browser with `expo-web-browser`, so users stay in the app

**Resources:**

- [Share](https://reactnative.dev/docs/share), React Native documentation
- [WebBrowser](https://docs.expo.dev/versions/latest/sdk/webbrowser/), Expo documentation

**Level:** Practitioner · Core

## Offline reading

Users expect to read what they already loaded, even without a connection. Saving the query cache on the device
makes the last feed and articles available offline.

**What to learn:**

- Persisting the TanStack Query cache to device storage, with a maximum age, and `gcTime` set to at least that age
- Showing that content is saved and may be out of date
- Never persisting data for a signed-in user after sign-out, and excluding the current-user query, which contains
  the token, with `shouldDehydrateQuery`

**Resources:**
[persistQueryClient](https://tanstack.com/query/latest/docs/framework/react/plugins/persistQueryClient), TanStack
Query documentation

**Level:** Advanced · Core

## Notifications

Notifications bring users back, but too many make them turn notifications off. Local notifications are scheduled by
the app; push notifications come from a server.

**What to learn:**

- Asking for notification permission at the moment it makes sense, and handling a refusal
- Scheduling a local notification, and opening the right screen when the user taps it
- How push notifications work through Apple's and Google's push services, and why they need a development build

**Resources:**

- [Notifications](https://docs.expo.dev/versions/latest/sdk/notifications/), Expo documentation
- [Push notifications overview](https://docs.expo.dev/push-notifications/overview/), Expo documentation

**Level:** Advanced · Core

## Camera and photos

Many client apps take photos or pick images from the library. The practice API stores image addresses, not files, so
this topic is for client work.

**What to learn:**

- Picking an image or taking a photo, with the permission request at the right moment
- Resizing an image before upload, and what location data photos can carry

**Resources:** [ImagePicker](https://docs.expo.dev/versions/latest/sdk/imagepicker/), Expo documentation

**Level:** Practitioner · Optional

## Project: Add Sharing, Offline Reading and Reminders

**Brief:** Add three device features to the practice app: share an article, read the last loaded feed and articles
offline, and save the editor draft on the device and remind the user to finish it with a local notification. Use a
development build.

**Size:** 3 days

**Verification**, checked by a reviewer:

- [ ] The article screen opens the system share sheet with the article's title and link
- [ ] Links in article bodies open in an in-app browser
- [ ] With the network off, the last loaded feed and articles still show, marked as saved
- [ ] Sign-out removes all saved user data, and the saved cache never contains the token
- [ ] The app asks for notification permission only when the user turns on draft reminders, and works normally if
  the user says no
- [ ] Tapping the reminder opens the editor with the draft
- [ ] The app runs from a development build on both platforms

Previous: [07. Working with APIs](./07-working-with-apis.md) · Next: [09. Testing](./09-testing.md)
