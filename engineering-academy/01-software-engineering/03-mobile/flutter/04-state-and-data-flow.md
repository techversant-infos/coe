# 04. State and Data Flow

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-12 · **Next review:** 2027-02-12

State is the data an app remembers, such as the selected feed or the signed-in user. Deciding where each piece of
state lives, and keeping it apart from the widgets, keeps an app simple to change. Back to the
[roadmap](./README.md).

## Widget state

Some state belongs to one widget, such as whether a tab is selected. A stateful widget keeps it and rebuilds when it
changes.

**What to learn:**

- `StatefulWidget` and `setState`, and keeping each piece of state in the smallest widget that needs it
- Disposing controllers, listeners and timers in `dispose`
- Why calling `setState` after a widget is gone causes an error, and checking `mounted` after `await`

**Resources:** [Adding interactivity to your Flutter app](https://docs.flutter.dev/ui/interactivity), Flutter
documentation

**Level:** Practitioner · Core

## App architecture

Flutter's architecture guide separates the interface from the data: views and view models on one side, and
repositories and services on the other. This keeps widgets small and logic testable.

**What to learn:**

- The layers: views, view models, repositories that own the data, and services that call the API
- Why widgets should not call the API directly
- `ChangeNotifier` and `ListenableBuilder`, Flutter's built-in way to rebuild a widget when a view model changes

**Resources:** [Guide to app architecture](https://docs.flutter.dev/app-architecture/guide), Flutter documentation

**Level:** Practitioner · Core

## State management with Riverpod

Riverpod is a widely used state management package. Providers create and cache values, such as the article feed, and
widgets rebuild when the values they watch change.

**What to learn:**

- Providers and `ref.watch`, and keeping providers outside the widget tree
- `AsyncValue`, which holds the loading, data or error state of data from the API
- Families for data that depends on a value, such as the articles for a tag

**Resources:** [Getting started](https://riverpod.dev/docs/introduction/getting_started), Riverpod documentation

**Level:** Practitioner · Core

## Server data and caching

Data from the API is a copy of what the server holds, and it goes out of date. Decide how long each piece stays
cached and when it reloads.

**What to learn:**

- Loading more articles as the user scrolls, using the API's `limit` and `offset`, without duplicates
- Pull to refresh with `RefreshIndicator`, and reloading when the app returns to the foreground
- Invalidating cached data after a change, so every screen shows the same values

**Resources:**

- [RefreshIndicator](https://api.flutter.dev/flutter/material/RefreshIndicator-class.html), Flutter API documentation
- [Implementing pull-to-refresh](https://riverpod.dev/docs/how_to/pull_to_refresh), Riverpod documentation

**Level:** Practitioner · Core

## Other state packages

Many client projects use Provider or Bloc instead of Riverpod. The ideas carry across: keep state out of widgets and
make every state explicit.

**What to learn:**

- Reading a Bloc or Provider code base, and mapping its parts to the architecture layers

**Resources:** [List of state management approaches](https://docs.flutter.dev/data-and-backend/state-mgmt/options),
Flutter documentation

**Level:** Practitioner · Optional

## Project: Add Feeds, Tags and Infinite Scroll

**Brief:** Extend the home screen with the Global Feed, popular tags and filtering by a tag. Load more articles as
the user scrolls, and refresh the feed when the user pulls down. Follow the architecture layers from this stage.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Widgets get data from view models or providers, and no widget calls the API directly
- [ ] Each feed and tag has its own cached state, and loading, data and error states are all shown
- [ ] Scrolling to the end loads the next page, with a page size small enough to give at least two pages, such as
  `limit=2` against the demo API, without duplicate articles
- [ ] Choosing a tag filters the feed, and clearing it returns to the Global Feed
- [ ] Pull to refresh reloads the first page
- [ ] The feed reloads when the app returns to the foreground after a set time, such as five minutes, recorded in the
  code
- [ ] Every controller, listener and timer is disposed, and no `setState` runs after a widget is gone

Previous: [03. Flutter Fundamentals](./03-flutter-fundamentals.md) · Next: [05. Navigation](./05-navigation.md)
