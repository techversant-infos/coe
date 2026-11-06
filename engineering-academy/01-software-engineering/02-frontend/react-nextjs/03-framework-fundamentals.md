# 03. Framework Fundamentals

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

React builds a page from components: small functions that each show one part of the interface. This stage covers
the core ideas you use in every React file. Back to the [roadmap](./README.md).

## Components and JSX

A component is a function that returns JSX, an HTML-like syntax that describes what to show. A page is a tree of
components.

**What to learn:**

- Writing a component, and naming it with a capital letter
- JSX rules: one parent element, `className` instead of `class`, and JavaScript inside `{}`
- Splitting a page into components that each do one job

**Resources:**

- [Your first component](https://react.dev/learn/your-first-component) and
  [Writing markup with JSX](https://react.dev/learn/writing-markup-with-jsx), React documentation

**Level:** Practitioner · Core

## Props and children

Props pass data from a parent component to a child, like arguments to a function. `children` lets a component wrap
other content.

**What to learn:**

- Passing props, and typing them with TypeScript
- Treating props as read-only
- Using `children` to build layout components such as cards

**Resources:** [Passing props to a component](https://react.dev/learn/passing-props-to-a-component), React documentation

**Level:** Practitioner · Core

## State

State is data a component remembers between renders, such as which tab is selected. Changing state makes React show
the new version of the page.

**What to learn:**

- `useState`, and why you call the setter instead of changing the value directly
- Updating objects and arrays by creating new ones
- Keeping state minimal, and calculating everything else from it

**Resources:**
[State: a component's memory](https://react.dev/learn/state-a-components-memory), React documentation

**Level:** Practitioner · Core

## Rendering lists and conditions

Pages show lists of items, and different content in different situations, such as a loading message or an empty
list.

**What to learn:**

- Rendering lists with `map`, and why each item needs a stable `key`
- Showing content conditionally with `&&` and the ternary operator
- Handling loading, empty and error cases on every list

**Resources:**

- [Rendering lists](https://react.dev/learn/rendering-lists) and
  [Conditional rendering](https://react.dev/learn/conditional-rendering), React documentation

**Level:** Practitioner · Core

## Handling events

Event handlers respond to clicks, typing and form submissions.

**What to learn:**

- Passing a function to `onClick` and other event props, without calling it
- Reading input values from the event
- Preventing a form's default submission when you handle it yourself

**Resources:** [Responding to events](https://react.dev/learn/responding-to-events), React documentation

**Level:** Practitioner · Core

## React Developer Tools

The React Developer Tools browser extension shows the component tree, each component's props and state, and what
caused a re-render.

**What to learn:**

- Inspecting props and state, and finding which component renders a part of the page

**Resources:** [React Developer Tools](https://react.dev/learn/react-developer-tools), React documentation

**Level:** Practitioner · Optional

## Project: Build the Home Page in React

**Brief:** Start a React and TypeScript app with Vite and turn your stage 01 home page into components. Load the
articles and tags with your stage 02 API client from your local RealWorld back end.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] The page is split into components, such as header, article preview, tag list and footer, each with typed props
- [ ] Articles and tags load from the local back end through the stage 02 API client
- [ ] Every list item has a stable `key` from the data, not the array index
- [ ] The page shows a loading message, an empty-feed message and an error message in the right situations
- [ ] The markup still uses the class names from `specs/e2e/SELECTORS.md`
- [ ] The browser console shows no React warnings
- [ ] The build passes type checking and linting

Previous: [02. JavaScript and TypeScript](./02-javascript-and-typescript.md) · Next:
[04. State and Data Flow](./04-state-and-data-flow.md)
