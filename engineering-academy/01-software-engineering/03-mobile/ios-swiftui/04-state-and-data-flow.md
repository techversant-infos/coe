# 04. State and Data Flow

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-18 · **Next review:** 2027-05-18

State is the data an app remembers, such as the selected feed or the signed-in user. Deciding where each piece of
state lives, and keeping it apart from the views, keeps an app simple to change. Back to the [roadmap](./README.md).

## View state

Some state belongs to one view, such as whether a tab is selected. SwiftUI keeps it for the view and redraws the view
when it changes.

**What to learn:**

- `@State` for values a view owns, and `@Binding` to let a child view change its parent's value
- Keeping each piece of state in the smallest view that needs it, and marking `@State` properties `private`
- Why a view's stored properties are recreated often, and why `@State` survives when they do not

**Resources:**
[Managing user interface state](https://developer.apple.com/documentation/swiftui/managing-user-interface-state),
SwiftUI documentation

**Level:** Practitioner · Core

## Observable models

Data that several views share, such as a feed, lives in a model class. The `@Observable` macro makes every view that
reads the model update when its data changes.

**What to learn:**

- `@Observable` classes, and how SwiftUI tracks which properties each view reads
- Owning a model with `@State`, passing it down, and `@Bindable` for editing its properties
- Sharing app-wide models, such as the session, through the environment with `.environment` and `@Environment`

**Resources:**
[Managing model data in your app](https://developer.apple.com/documentation/swiftui/managing-model-data-in-your-app),
SwiftUI documentation

**Level:** Practitioner · Core

## App architecture

Keeping the interface apart from the data keeps views small and logic testable. A common split is views, models that
hold screen state, repositories that own the data, and services that call the API.

**What to learn:**

- The layers, and why views should not call the API directly
- Passing services into models through their initialisers or the environment, so tests can replace them
- Choosing between models per screen and shared models, and writing the choice down in the project README

**Resources:** [Model data](https://developer.apple.com/documentation/swiftui/model-data), SwiftUI documentation

**Level:** Practitioner · Core

## Server data and caching

Data from the API is a copy of what the server holds, and it goes out of date. Decide how long each piece stays
cached and when it reloads.

**What to learn:**

- Loading more articles as the user scrolls, using the API's `limit` and `offset`, without duplicates
- Pull to refresh with `.refreshable`, and reloading when the app returns to the foreground
- Updating cached data after a change, so every screen shows the same values

**Resources:** [refreshable(action:)](https://developer.apple.com/documentation/swiftui/view/refreshable(action:)),
SwiftUI documentation

**Level:** Practitioner · Core

## Other state approaches

Older client apps use `ObservableObject` and Combine, and some teams use The Composable Architecture. The ideas carry
across: keep state out of views and make every state explicit.

**What to learn:**

- Reading `ObservableObject`, `@Published` and `@StateObject` code, and moving it to `@Observable`

**Resources:**
[Migrating from the Observable Object protocol to the Observable macro](https://developer.apple.com/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro),
SwiftUI documentation

**Level:** Practitioner · Optional

## Project: Add Feeds, Tags and Infinite Scroll

**Brief:** Extend the home screen with the Global Feed, popular tags and filtering by a tag. Load more articles as
the user scrolls, and refresh the feed when the user pulls down. Follow the architecture layers from this stage.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Views get data from models, and no view calls the API directly
- [ ] Each feed and tag has its own state, and loading, data and error states are all shown
- [ ] Scrolling to the end loads the next page, with a page size small enough to give at least two pages, such as
  `limit=2` against the demo API, without duplicate articles
- [ ] Choosing a tag filters the feed, and clearing it returns to the Global Feed
- [ ] Pull to refresh reloads the first page
- [ ] The feed reloads when the app returns to the foreground after a set time, such as five minutes, recorded in the
  code
- [ ] Loading stops when the user leaves a screen, and no task keeps running after its view is gone

Previous: [03. SwiftUI Fundamentals](./03-swiftui-fundamentals.md) · Next: [05. Navigation](./05-navigation.md)
