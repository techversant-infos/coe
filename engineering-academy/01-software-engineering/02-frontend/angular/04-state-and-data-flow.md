# 04. State and Data Flow

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

As an app grows, deciding where each piece of state lives, and how it flows between components, becomes the main
design question. Getting it right keeps components simple and bugs rare. Back to the [roadmap](./README.md).

## Computed signals

A computed signal calculates a value from other signals, and Angular keeps it up to date. Most values that depend
on state should be computed, not stored.

**What to learn:**

- `computed()` for derived values, such as the articles to show for the selected tag
- `linkedSignal()` for state that resets when another value changes, such as the page number when the tag changes
- Keeping computed signals free of side effects

**Resources:** [Signals](https://angular.dev/guide/signals), Angular documentation

**Level:** Practitioner · Core

## Effects and when to avoid them

An effect runs code when the signals it reads change, such as saving a draft to storage. Many effects in real
projects should be computed signals instead.

**What to learn:**

- `effect()`, and the cleanup function it can register
- Using a computed or linked signal instead of an effect that copies one signal into another
- Why loading data belongs in a resource or a service, covered in stage 07, rather than in an effect

**Resources:** [Signals](https://angular.dev/guide/signals), Angular documentation

**Level:** Practitioner · Core

## Services and dependency injection

A service holds logic and state that several components share, such as the signed-in user. Angular creates it and
passes it to the components that ask for it.

**What to learn:**

- Creating a service with `@Service()`, and getting it with `inject()`
- Services that hold signals for shared state, and exposing them as read-only
- Providing a service for one part of the app instead of the whole app

**Resources:**
[Dependency injection](https://angular.dev/guide/di), Angular documentation

**Level:** Practitioner · Core

## RxJS and signals

Angular's HTTP client and router return RxJS observables. Interop functions move values between observables and
signals.

**What to learn:**

- Observables, and operators such as `map` and `switchMap`; `switchMap` cancels an earlier request when a newer one
  starts
- `toSignal` and `toObservable`, and unsubscribing automatically when a component is destroyed

**Resources:** [RxJS interop](https://angular.dev/ecosystem/rxjs-interop), Angular documentation

**Level:** Practitioner · Core

## View queries

A view query points to an element or child component, for example to move focus to an input.

**What to learn:**

- `viewChild()` to reach an element after the view is created
- Using it to focus an input or scroll to an element
- Why reaching into elements is an escape hatch, not a replacement for state

**Resources:** [Components](https://angular.dev/guide/components), Angular documentation

**Level:** Practitioner · Core

## Shared state libraries

Larger apps sometimes use a library, such as NgRx SignalStore, for state shared across many pages. Most apps need
less than you think: data from the server belongs in a resource (stage 07).

**What to learn:**

- When a shared store helps, and when services with signals are enough
- The library your project already uses

**Resources:** [NgRx SignalStore](https://ngrx.io/guide/signals/signal-store)

**Level:** Advanced · Optional

## Project: Add Feeds, Tags and Pagination

**Brief:** Make the home page interactive: switch between the global feed and a tag feed, page through articles, and
move the data loading into a service.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] Clicking a tag shows only articles with that tag. The Global Feed, Your Feed and tag tabs are
  `a.nav-link`, and only the current one has the `active` class.
- [ ] Pagination shows the right page of articles, and the current page has the `active` class, as the selector
  contract requires
- [ ] Data loading lives in a service, such as `ArticleService`, used by the home page
- [ ] A newer request replaces an earlier one, and a late response from the earlier request is ignored
- [ ] No effect copies one signal into another; derived values are computed or linked signals
- [ ] Angular DevTools shows each piece of state in one place only

Previous: [03. Framework Fundamentals](./03-framework-fundamentals.md) · Next: [05. Routing](./05-routing.md)
