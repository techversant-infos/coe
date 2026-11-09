# 03. Framework Fundamentals

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Angular builds a page from components: TypeScript classes with a template that shows one part of the interface.
This stage covers the core ideas you use in every Angular file, in Angular 22. Back to the [roadmap](./README.md).

## Components and templates

A component is a class with the `@Component` decorator, a selector and a template. Components are standalone by
default, and list the other components they use in `imports`.

**What to learn:**

- Creating components with the Angular command-line interface (CLI), and the parts of the `@Component` decorator
- Template syntax: `{{ }}` for text, `[ ]` to bind properties and `( )` to listen for events
- Splitting a page into components that each do one job

**Resources:** [Components](https://angular.dev/guide/components), Angular documentation

**Level:** Practitioner · Core

## Inputs and outputs

Inputs pass data from a parent component to a child. Outputs send events back up, and content projection lets a
component wrap other content.

**What to learn:**

- Declaring typed inputs with `input()` and `input.required()`, and treating them as read-only
- Emitting events with `output()`, so a child tells its parent what happened instead of changing its data
- Projecting content with `<ng-content>` to build layout components such as cards

**Resources:**

- [Inputs](https://angular.dev/guide/components/inputs) and [Outputs](https://angular.dev/guide/components/outputs),
  Angular documentation

**Level:** Practitioner · Core

## Signals

A signal holds a value and tells Angular when it changes, so Angular updates the parts of the page that read it.

**What to learn:**

- `signal()`, reading a signal by calling it, and changing it with `set` and `update`
- Updating objects and arrays by creating new ones
- Keeping state minimal, and calculating everything else from it

**Resources:** [Signals](https://angular.dev/guide/signals), Angular documentation

**Level:** Practitioner · Core

## Control flow

Pages show lists of items, and different content in different situations, such as a loading message or an empty
list.

**What to learn:**

- Rendering lists with `@for`, and why each item needs a stable `track` expression
- Showing content with `@if`, `@else` and `@switch`, and `@empty` for empty lists
- Handling loading, empty and error cases on every list

**Resources:** [Control flow](https://angular.dev/guide/templates/control-flow), Angular documentation

**Level:** Practitioner · Core

## Handling events

Event bindings respond to clicks, typing and form submissions.

**What to learn:**

- Binding events with `(click)` and other events, and passing `$event` when you need it
- Reading input values from the event
- Preventing a form's default submission when you handle it yourself

**Resources:** [Event listeners](https://angular.dev/guide/templates/event-listeners), Angular documentation

**Level:** Practitioner · Core

## Angular DevTools

The Angular DevTools browser extension shows the component tree, each component's inputs and state, and what
triggered change detection.

**What to learn:**

- Inspecting inputs and signals, and finding which component renders a part of the page

**Resources:** [Angular DevTools](https://angular.dev/tools/devtools), Angular documentation

**Level:** Practitioner · Optional

## Project: Build the Home Page in Angular

**Brief:** Start an Angular 22 app with the Angular CLI and turn your stage 01 home page into components. Load the
articles and tags with your stage 02 API client from your local RealWorld back end.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] The page is split into components, such as header, article preview, tag list and footer, each with typed
  inputs
- [ ] Articles and tags load from the local back end through the stage 02 API client
- [ ] Every `@for` tracks a stable value from the data, such as the slug, not the index
- [ ] The page shows a loading message, an empty-feed message and an error message in the right situations
- [ ] The markup still uses the class names from `specs/e2e/SELECTORS.md`
- [ ] The browser console shows no Angular warnings or errors
- [ ] The build passes with strict templates, and linting passes

Previous: [02. JavaScript and TypeScript](./02-javascript-and-typescript.md) · Next:
[04. State and Data Flow](./04-state-and-data-flow.md)
