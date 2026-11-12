# 06. Forms and Input

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-11 · **Next review:** 2027-02-11

Typing on a phone is slow and the keyboard covers half the screen. Good mobile forms ask for less, use the right
keyboard, and keep the field the user is typing in visible. Back to the [roadmap](./README.md).

## Text input

`TextInput` is the core component for typing. Its settings decide which keyboard appears and what the system offers
to fill in.

**What to learn:**

- Controlled inputs, and keyboard types for email addresses, URLs and plain text
- `autoComplete` and `textContentType`, so the system can offer saved passwords and email addresses
- `secureTextEntry` for passwords, and turning off auto-correct and auto-capitalise where they get in the way

**Resources:** [TextInput](https://reactnative.dev/docs/textinput), React Native documentation

**Level:** Practitioner · Core

## The keyboard

The on-screen keyboard can hide the field being typed in and the submit button. The app must move content out of
its way.

**What to learn:**

- `KeyboardAvoidingView` with a `behavior` set on both platforms, because Expo apps on Android draw edge to edge and
  the window no longer resizes for the keyboard
- Scroll views that keep the focused field visible, and `react-native-keyboard-controller` for long forms such as
  the editor
- Moving to the next field with the keyboard's return key, and submitting from the last field
- Closing the keyboard when the user taps outside a field or scrolls

**Resources:**

- [Keyboard handling](https://docs.expo.dev/guides/keyboard-handling/), Expo documentation
- [KeyboardAvoidingView](https://reactnative.dev/docs/keyboardavoidingview), React Native documentation

**Level:** Practitioner · Core

## Form libraries

A form library tracks each field's value, errors and whether it was touched, so you write less code by hand.

**What to learn:**

- React Hook Form with `Controller`, which connects the library to `TextInput`
- Disabling the submit button while the form is being sent

**Resources:** [React Hook Form](https://react-hook-form.com/)

**Level:** Practitioner · Core

## Schema validation with Zod

Zod describes the shape of valid data once, as a schema. The same schema validates the form and gives you a
TypeScript type.

**What to learn:**

- Writing a Zod schema for each form, and connecting it to React Hook Form with a resolver
- Showing the API's errors, such as "email has already been taken", next to the right field
- Why checks in the app are for the user's convenience: the API must validate everything again

**Resources:** [Zod documentation](https://zod.dev/)

**Level:** Practitioner · Core

## Accessible forms

Screen reader users need to know what each field is for and what went wrong.

**What to learn:**

- An accessibility label on every field, and errors announced when they appear
- Moving focus to the first field with an error after a failed submit
- Touch targets large enough for every button, including the tag remove buttons

**Resources:** [Accessibility](https://reactnative.dev/docs/accessibility), React Native documentation

**Level:** Practitioner · Core

## Project: Build the Forms

**Brief:** Build the four RealWorld forms: sign-in, sign-up, the article editor and settings. Validate each in the app
and show the errors the API returns. In this stage, sign-up and sign-in call the API through your stage 02 client,
extended with POST calls. Keep the returned token in memory only and never store it; stage 07 adds secure storage. The
sign-in and sign-up submit code is Red Zone work, so write it by hand. The editor and settings need a token, so stage 07
checks that they save.

**Size:** 3 days

**Verification**, checked by a reviewer:

- [ ] Each form has a Zod schema, and the form's TypeScript type comes from the schema
- [ ] Email fields use the email keyboard, and the sign-in fields set `autoComplete` and `textContentType` so the
  password AutoFill bar appears
- [ ] The focused field and the submit button stay visible above the keyboard on both platforms
- [ ] The return key moves to the next field, and the last field submits the form
- [ ] Submitting an empty or invalid form shows a message next to each problem field and does not call the API
- [ ] Errors from the API appear on the form, and a screen reader announces them
- [ ] The submit button is disabled while the form is being sent
- [ ] The returned token is held in memory only, and is not written to any storage
- [ ] Adding a tag in the editor does not submit the form

Previous: [05. Navigation](./05-navigation.md) · Next: [07. Working with APIs](./07-working-with-apis.md)
