# 04. State and Data Flow

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

As an app grows, deciding where each piece of state lives, and how it flows between components, becomes the main
design question. Getting it right keeps components simple and bugs rare. Back to the [roadmap](./README.md).

## Lifting state up

When two components need the same state, move it to their closest shared parent and pass it down as props.

**What to learn:**

- Spotting state that two components need to share
- Moving it to the closest common parent, and passing setters down as props
- Keeping each piece of state in exactly one place

**Resources:**
[Sharing state between components](https://react.dev/learn/sharing-state-between-components), React documentation

**Level:** Practitioner · Core

## Reducers and context

A reducer collects all the ways state can change in one function. Context passes data deep into the tree without
threading props through every level.

**What to learn:**

- `useReducer` for state with several related changes
- `createContext` and `useContext` for data many components need, such as the signed-in user
- Why context is not a replacement for all props, and how it affects re-rendering

**Resources:**

- [Extracting state logic into a reducer](https://react.dev/learn/extracting-state-logic-into-a-reducer) and
  [Passing data deeply with context](https://react.dev/learn/passing-data-deeply-with-context), React documentation

**Level:** Practitioner · Core

## Effects and when to avoid them

An effect syncs a component with something outside React, such as a browser API or a subscription. Many effects in
real projects are unnecessary and cause bugs.

**What to learn:**

- `useEffect`, its dependency array, and cleanup functions
- Calculating values during rendering instead of copying them into state with an effect
- Avoiding infinite loops and race conditions when an effect fetches data

**Resources:**

- [Synchronizing with effects](https://react.dev/learn/synchronizing-with-effects) and
  [You might not need an effect](https://react.dev/learn/you-might-not-need-an-effect), React documentation

**Level:** Practitioner · Core

## Refs

A ref holds a value that does not trigger a re-render, or points to a DOM element, for example to move focus.

**What to learn:**

- `useRef` for values that change without re-rendering
- Using a ref to focus an input or scroll to an element
- Why refs are an escape hatch, not a way to avoid state

**Resources:** [Referencing values with refs](https://react.dev/learn/referencing-values-with-refs), React documentation

**Level:** Practitioner · Core

## Custom hooks

A custom hook is a function that starts with `use` and wraps logic you want to reuse, such as loading data or
reading the signed-in user.

**What to learn:**

- Extracting repeated stateful logic into a custom hook
- Naming hooks clearly and keeping each one focused
- The rules of hooks: call them at the top level, never inside conditions or loops

**Resources:**
[Reusing logic with custom hooks](https://react.dev/learn/reusing-logic-with-custom-hooks), React documentation

**Level:** Practitioner · Core

## Shared state libraries

Larger apps sometimes use a library, such as Zustand or Redux Toolkit, for state shared across many pages. Most apps
need less than you think: data from the server belongs in a server-state tool (stage 07).

**What to learn:**

- When a shared store helps, and when props, context and server state are enough
- The library your project already uses

**Resources:** [Zustand](https://zustand.docs.pmnd.rs/) and [Redux Toolkit](https://redux-toolkit.js.org/)

**Level:** Advanced · Optional

## Project: Add Feeds, Tags and Pagination

**Brief:** Make the home page interactive: switch between the global feed and a tag feed, page through articles, and
move the data loading into a custom hook.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Clicking a tag shows only articles with that tag, and the feed tabs show which feed is active
- [ ] Pagination shows the right page of articles, and the current page has the `active` class, as the selector
  contract requires
- [ ] Data loading lives in a custom hook, such as `useArticles`, used by the home page
- [ ] The hook ignores the result of an earlier request that finishes after a newer one
- [ ] No effect copies props or other state into state; derived values are calculated during rendering
- [ ] React Developer Tools shows each piece of state in one component only

Previous: [03. Framework Fundamentals](./03-framework-fundamentals.md) · Next: [05. Routing](./05-routing.md)
