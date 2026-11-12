# Mobile Paths

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-12 · **Next review:** 2027-02-12

A mobile developer builds the iOS and Android apps clients put in their users' hands. Each mobile path teaches one
stack through the same ten stages, and the projects build a complete mobile client for the RealWorld blogging app.
Back to [Software Engineering](../README.md).

## Paths

| Path | Status |
|------|--------|
| [React Native and Expo](./react-native-expo/README.md) | Draft |
| [Flutter](./flutter/README.md) | Draft |
| iOS: Swift and SwiftUI | Planned |
| Android: Kotlin and Jetpack Compose | Planned |

## Choosing a Path

- **React Native and Expo:** one TypeScript code base for iOS and Android. The natural next step for React
  developers.
- **Flutter:** one Dart code base for iOS and Android, with its own rendering engine.
- **iOS and Android:** native apps, for clients who need platform-specific features or a native code base.

## The Ten Stages

Every mobile path uses these stages, so you can move between stacks and compare them:

1. Mobile Platforms and Design
2. The language: TypeScript, Dart, Swift or Kotlin
3. Framework Fundamentals
4. State and Data Flow
5. Navigation
6. Forms and Input
7. Working with APIs
8. Device Features
9. Testing
10. Performance and Release

Sign-in, token storage and the session code in stage 07 are Red Zone work: you write that code by hand, and a senior
engineer reviews it.

## The Practice App

Every path builds the same [practice app](./practice-app.md): a RealWorld mobile client that uses the same API as the
web paths. Start with [Engineering Foundations](../../00-engineering-foundations/README.md), whose topics include
notes for mobile code.
