# 03. Framework Fundamentals

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Vue builds a page from components: single files that each hold the template, logic and styles for one part of the
interface. This stage covers the core ideas you use in every Vue file. Back to the [roadmap](./README.md).

## Single-file components and templates

A single-file component is a `.vue` file with a `<template>`, a `<script setup>` block and, often, a `<style>` block.
The template is HTML with a few extra features.

**What to learn:**

- Writing a component with `<script setup lang="ts">`, and naming it in PascalCase
- Template syntax: `{{ }}` for text, `:` to bind attributes and `@` to listen for events
- Splitting a page into components that each do one job

**Resources:**
[Template syntax](https://vuejs.org/guide/essentials/template-syntax.html), Vue documentation

**Level:** Practitioner · Core

## Props, events and slots

Props pass data from a parent component to a child. Events send messages back up, and slots let a component wrap
other content.

**What to learn:**

- Declaring typed props with `defineProps`, and treating them as read-only
- Emitting events with `defineEmits`, so a child tells its parent what happened instead of changing its data
- Using slots to build layout components such as cards

**Resources:**

- [Props](https://vuejs.org/guide/components/props.html), [Events](https://vuejs.org/guide/components/events.html)
  and [Slots](https://vuejs.org/guide/components/slots.html), Vue documentation

**Level:** Practitioner · Core

## Reactive state

Reactive state is data Vue tracks. When it changes, Vue updates the parts of the page that use it.

**What to learn:**

- `ref` for state, and reading and changing it with `.value` in script code
- `reactive` for objects, and why destructuring a reactive object loses reactivity
- Keeping state minimal, and calculating everything else from it

**Resources:**
[Reactivity fundamentals](https://vuejs.org/guide/essentials/reactivity-fundamentals.html), Vue documentation

**Level:** Practitioner · Core

## Rendering lists and conditions

Pages show lists of items, and different content in different situations, such as a loading message or an empty
list.

**What to learn:**

- Rendering lists with `v-for`, and why each item needs a stable `:key`
- Showing content with `v-if`, `v-else-if` and `v-else`, and when `v-show` fits better
- Handling loading, empty and error cases on every list

**Resources:**

- [List rendering](https://vuejs.org/guide/essentials/list.html) and
  [Conditional rendering](https://vuejs.org/guide/essentials/conditional.html), Vue documentation

**Level:** Practitioner · Core

## Handling events

Event handlers respond to clicks, typing and form submissions.

**What to learn:**

- Listening with `@click` and other events, and passing a method or an inline handler
- Event modifiers, such as `@submit.prevent` to stop a form's default submission
- Reading values from the event

**Resources:**
[Event handling](https://vuejs.org/guide/essentials/event-handling.html), Vue documentation

**Level:** Practitioner · Core

## Vue DevTools

The Vue DevTools browser extension shows the component tree, each component's props and state, and, from stage 04,
your Pinia stores.

**What to learn:**

- Inspecting props and state, and finding which component renders a part of the page

**Resources:** [Vue DevTools](https://devtools.vuejs.org/), Vue DevTools documentation

**Level:** Practitioner · Optional

## Project: Build the Home Page in Vue

**Brief:** Start a Vue and TypeScript app with `npm create vue@latest` and turn your stage 01 home page into
components. Load the articles and tags with your stage 02 API client from your local RealWorld back end.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] The page is split into components, such as header, article preview, tag list and footer, each with typed props
- [ ] Articles and tags load from the local back end through the stage 02 API client
- [ ] Every `v-for` has a stable `:key` from the data, not the array index
- [ ] The page shows a loading message, an empty-feed message and an error message in the right situations
- [ ] The markup still uses the class names from `specs/e2e/SELECTORS.md`
- [ ] The browser console shows no Vue warnings
- [ ] `vue-tsc` type checking and linting pass

Previous: [02. JavaScript and TypeScript](./02-javascript-and-typescript.md) · Next:
[04. State and Data Flow](./04-state-and-data-flow.md)
