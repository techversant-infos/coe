# 03. SwiftUI Fundamentals

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-18 · **Next review:** 2027-05-18

SwiftUI is Apple's framework for building interfaces in Swift. You describe what each screen shows for the current
data, and SwiftUI updates the screen when the data changes. Back to the [roadmap](./README.md).

## Xcode, the Simulator and previews

Xcode is the app you write, run, debug and ship iOS apps with. Previews show a view as you edit it, without running
the whole app.

**What to learn:**

- Creating an iOS app project, running it in the iOS Simulator and on your own iPhone
- `#Preview`, and previews with sample data, dark mode and the largest text size
- Reading build errors, warnings and the console while the app runs

**Resources:** [Previews in Xcode](https://developer.apple.com/documentation/swiftui/previews-in-xcode), SwiftUI
documentation

**Level:** Practitioner · Core

## Views and modifiers

Everything on screen is a view, from a line of text to a whole screen. You change how a view looks with modifiers,
and build screens by putting small views inside larger ones.

**What to learn:**

- Views as structs with a `body`, and splitting a screen into small views that each do one job
- Modifiers such as `.padding()` and `.font(.headline)`, and why their order matters
- Why `body` should be fast and free of side effects, because SwiftUI can call it many times

**Resources:** [SwiftUI tutorials](https://developer.apple.com/tutorials/swiftui), Apple

**Level:** Practitioner · Core

## Layout

SwiftUI lays out views with stacks, spacers and frames. Each parent offers its children a size, and each child
chooses its own size within it.

**What to learn:**

- `HStack`, `VStack`, `ZStack`, `Spacer` and `.frame`, and how a parent proposes a size to its children
- Safe areas, so content is not hidden by the Dynamic Island or the Home indicator
- Layouts that still work at the largest Dynamic Type sizes, such as with `ViewThatFits`

**Resources:** [Layout fundamentals](https://developer.apple.com/documentation/swiftui/layout-fundamentals), SwiftUI
documentation

**Level:** Practitioner · Core

## Lists and loading data

Feeds are long, and a list must stay smooth while it scrolls. Lists also need data from the API, which takes time to
arrive.

**What to learn:**

- `List` and `LazyVStack` with `ForEach`, and stable identity through `Identifiable`, such as the article slug
- The `.task` modifier, which starts loading when a view appears and cancels the work when it disappears
- Loading, empty and error states for every list, with a retry on error

**Resources:** [Lists](https://developer.apple.com/documentation/swiftui/lists), SwiftUI documentation

**Level:** Practitioner · Core

## Images, colours and dark mode

Users choose light or dark mode, and images come from the network in different sizes. Both affect every screen.

**What to learn:**

- Colours from the asset catalogue with light and dark versions, and system colours that adapt on their own
- Loading remote images, such as avatars, with `AsyncImage`, a placeholder and a fallback when the URL fails
- SF Symbols in buttons and labels, sized with the text around them

**Resources:** [AsyncImage](https://developer.apple.com/documentation/swiftui/asyncimage), SwiftUI documentation

**Level:** Practitioner · Core

## UIKit and existing apps

UIKit is Apple's older interface framework, and many client apps still use it. SwiftUI and UIKit can work together in
one app.

**What to learn:**

- Reading a UIKit code base: view controllers, storyboards and Auto Layout
- Showing a UIKit view in SwiftUI with `UIViewRepresentable`, and a SwiftUI view in UIKit with `UIHostingController`

**Resources:** [UIKit integration](https://developer.apple.com/documentation/swiftui/uikit-integration), SwiftUI
documentation

**Level:** Practitioner · Optional

## Project: Build the Home Screen

**Brief:** Start an iOS app in Xcode 27 with SwiftUI and a minimum iOS version of iOS 18, and build the home screen
from your stage 01 sketches. Load the articles and tags with your stage 02 API client.

**Size:** 2–3 days

**Verification**, checked by a reviewer:

- [ ] The app runs in the iOS Simulator and on an iPhone, and screenshots are in the pull request
- [ ] The screen is split into small views, such as article preview, tag list and header, each with typed properties
- [ ] The feed uses `List` or `LazyVStack`, with the slug as each article's identity
- [ ] Data loads in `.task`, and the screen shows loading, empty and error states, with a retry on error
- [ ] Avatars load with a placeholder, and a broken image URL shows a fallback
- [ ] Light and dark mode both have readable text, colours come from the asset catalogue or the system, and content
  stays inside the safe areas
- [ ] The build has no warnings, and every screen works at the largest Dynamic Type size
- [ ] Each view has a preview with sample data

Previous: [02. Swift](./02-swift.md) · Next: [04. State and Data Flow](./04-state-and-data-flow.md)
