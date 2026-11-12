# 04. State and Data Flow

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-11 · **Next review:** 2027-02-11

State is the data an app remembers, such as the selected feed or the signed-in user. Deciding where each piece of
state lives keeps an app simple to change. Back to the [roadmap](./README.md).

## Component state

Most state belongs to one component. React re-renders the component when its state changes.

**What to learn:**

- `useState` for values that change, such as the selected feed tab
- Updating objects and arrays by creating new ones, never by changing them in place
- Calculating values from state while rendering, instead of storing them separately

**Resources:** [State: a component's memory](https://react.dev/learn/state-a-components-memory), React documentation

**Level:** Practitioner · Core

## Sharing state between components

When two components need the same data, move the state up to their closest shared parent, or put it in a context.

**What to learn:**

- Lifting state up and passing it down as props
- Context for data many screens need, such as the signed-in user or the theme
- Why putting everything in context causes extra re-renders

**Resources:** [Sharing state between components](https://react.dev/learn/sharing-state-between-components), React
documentation

**Level:** Practitioner · Core

## Server state

Data from the API is a copy of what the server holds, and it goes out of date. A server-state library fetches,
caches and refreshes it for you.

**What to learn:**

- TanStack Query: queries, cache keys, loading and error states
- Infinite queries for feeds that load more articles as the user scrolls
- Pull to refresh, and refreshing when the app returns to the foreground or the network comes back

**Resources:** [React Native support](https://tanstack.com/query/latest/docs/framework/react/react-native), TanStack
Query documentation

**Level:** Practitioner · Core

## Effects and when to avoid them

Effects run code after rendering to sync with something outside React, such as an app-state listener. Many effects
in beginner code are not needed.

**What to learn:**

- When an effect is the right tool, and cleaning up listeners and timers when a screen closes
- Why fetching data in effects is error-prone, and why a server-state library handles it better

**Resources:** [You might not need an effect](https://react.dev/learn/you-might-not-need-an-effect), React
documentation

**Level:** Practitioner · Core

## Shared state libraries

Some apps need app-wide state that is not server data and changes too often to keep in context, such as a multi-step
form. Libraries such as Zustand handle this with less code.

**What to learn:**

- When context is enough and when a small store library helps

**Resources:** [Zustand](https://zustand.docs.pmnd.rs/)

**Level:** Practitioner · Optional

## Project: Add Feeds, Tags and Infinite Scroll

**Brief:** Extend the home screen with the Global Feed, popular tags and filtering by a tag. Load more articles as
the user scrolls, and refresh the feed when the user pulls down.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Articles load with TanStack Query, and each feed and tag has its own cache key
- [ ] Scrolling to the end loads the next page, using the API's `limit` and `offset` with a page size small enough to
  give at least two pages, such as `limit=2` against the demo API, without duplicate articles
- [ ] Choosing a tag filters the feed, and clearing it returns to the Global Feed
- [ ] Pull to refresh reloads the first page
- [ ] The feed refreshes when the app returns to the foreground after a set time, such as five minutes, recorded in
  the code
- [ ] No effect fetches data, and every listener or timer is cleaned up

Previous: [03. React Native Fundamentals](./03-react-native-fundamentals.md) · Next:
[05. Navigation](./05-navigation.md)
