# 04. State and Data Flow

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

As an app grows, deciding where each piece of state lives, and how it flows between components, becomes the main
design question. Getting it right keeps components simple and bugs rare. Back to the [roadmap](./README.md).

## Computed properties

A computed property calculates a value from other state, and Vue keeps it up to date. Most values that depend on
state should be computed, not stored.

**What to learn:**

- `computed` for derived values, such as the articles to show for the selected tag
- Why computed values are cached until the state they read changes
- Keeping computed properties free of side effects

**Resources:** [Computed properties](https://vuejs.org/guide/essentials/computed.html), Vue documentation

**Level:** Practitioner · Core

## Watchers and when to avoid them

A watcher runs code when state changes, such as loading data when a page number changes. Many watchers in real
projects should be computed properties instead.

**What to learn:**

- `watch` and `watchEffect`, and when each fits
- Cancelling outdated work with `onWatcherCleanup`, so a slow earlier request cannot overwrite a newer one
- Using a computed property instead of a watcher that copies state into other state

**Resources:** [Watchers](https://vuejs.org/guide/essentials/watchers.html), Vue documentation

**Level:** Practitioner · Core

## Provide and inject

Provide and inject pass data deep into the component tree without threading props through every level.

**What to learn:**

- `provide` and `inject`, with typed injection keys
- Why provide and inject are not a replacement for props, and when a store fits better

**Resources:** [Provide and inject](https://vuejs.org/guide/components/provide-inject.html), Vue documentation

**Level:** Practitioner · Core

## Template refs

A template ref points to an element on the page, for example to move focus to an input.

**What to learn:**

- `useTemplateRef` to reach an element after the component has mounted
- Using a ref to focus an input or scroll to an element
- Why reaching into elements is an escape hatch, not a replacement for state

**Resources:** [Template refs](https://vuejs.org/guide/essentials/template-refs.html), Vue documentation

**Level:** Practitioner · Core

## Composables

A composable is a function, named with `use`, that wraps stateful logic you want to reuse, such as loading data or
reading the signed-in user.

**What to learn:**

- Extracting repeated logic into a composable that returns refs
- Accepting refs or getters as arguments, so a composable reacts when its inputs change
- Naming composables clearly and keeping each one focused

**Resources:** [Composables](https://vuejs.org/guide/reusability/composables.html), Vue documentation

**Level:** Practitioner · Core

## Pinia stores

Pinia is Vue's official library for state shared across many pages, such as the signed-in user. Data from the server
belongs in a server-state tool (stage 07), not in a store.

**What to learn:**

- Defining a store with `defineStore` in the setup style, and reading it with `storeToRefs`
- When a store helps, and when props, composables and server state are enough

**Resources:** [Pinia documentation](https://pinia.vuejs.org/)

**Level:** Practitioner · Core

## Project: Add Feeds, Tags and Pagination

**Brief:** Make the home page interactive: switch between the global feed and a tag feed, page through articles, and
move the data loading into a composable.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Clicking a tag shows only articles with that tag. The Global Feed, Your Feed and tag tabs are
  `a.nav-link`, and only the current one has the `active` class.
- [ ] Pagination shows the right page of articles, and the current page has the `active` class, as the selector
  contract requires
- [ ] Data loading lives in a composable, such as `useArticles`, used by the home page
- [ ] The composable ignores the result of an earlier request that finishes after a newer one
- [ ] No watcher copies props or other state into state; derived values are computed properties
- [ ] Vue DevTools shows each piece of state in one place only

Previous: [03. Framework Fundamentals](./03-framework-fundamentals.md) · Next: [05. Routing](./05-routing.md)
