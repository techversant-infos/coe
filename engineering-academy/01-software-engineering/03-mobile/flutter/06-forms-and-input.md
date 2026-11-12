# 06. Forms and Input

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-12 · **Next review:** 2027-02-12

Typing on a phone is slow and the keyboard covers half the screen. Good mobile forms ask for less, use the right
keyboard, and keep the field the user is typing in visible. Back to the [roadmap](./README.md).

## Text fields

`TextField` and `TextFormField` are Flutter's widgets for typing. Their settings decide which keyboard appears and
what the system offers to fill in.

**What to learn:**

- `TextEditingController`, and disposing it when the screen closes
- Keyboard types for email addresses, URLs and plain text, and `obscureText` for passwords
- Turning off auto-correct and capitalisation where they get in the way, such as in email and username fields

**Resources:** [Create and style a text field](https://docs.flutter.dev/cookbook/forms/text-input), Flutter
documentation

**Level:** Practitioner · Core

## The keyboard and focus

The on-screen keyboard can hide the field being typed in and the submit button. The app must move content out of its
way and move focus in a sensible order.

**What to learn:**

- How `Scaffold` resizes for the keyboard, and scroll views that keep the focused field visible
- `textInputAction` and `FocusNode`, so the return key moves to the next field and submits from the last one
- Closing the keyboard when the user taps outside a field

**Resources:** [Focus and text fields](https://docs.flutter.dev/cookbook/forms/focus), Flutter documentation

**Level:** Practitioner · Core

## Validation

A `Form` groups fields so they can be validated together. Each field's validator returns an error message or `null`.

**What to learn:**

- `Form` with a `GlobalKey<FormState>`, and `TextFormField` validators
- Showing the API's errors, such as "email has already been taken", next to the right field
- Why checks in the app are for the user's convenience: the API must validate everything again

**Resources:** [Build a form with validation](https://docs.flutter.dev/cookbook/forms/validation), Flutter
documentation

**Level:** Practitioner · Core

## Autofill

The system can fill in saved email addresses and passwords, which makes signing in faster and safer.

**What to learn:**

- `AutofillGroup` around the sign-in and sign-up fields, and `autofillHints` on each field
- Asking the system to save the new password after sign-up

**Resources:** [AutofillGroup](https://api.flutter.dev/flutter/widgets/AutofillGroup-class.html), Flutter API
documentation

**Level:** Practitioner · Core

## Accessible forms

Screen reader users need to know what each field is for and what went wrong.

**What to learn:**

- A visible label on every field, which screen readers also read
- Errors that screen readers announce, and moving focus to the first field with an error after a failed submit
- Touch targets large enough for every button, including the tag remove buttons

**Resources:** [Accessibility](https://docs.flutter.dev/ui/accessibility), Flutter documentation

**Level:** Practitioner · Core

## Form packages

Long forms with many fields and rules can use a package such as `flutter_form_builder` or `reactive_forms`, which
track values and errors for you.

**What to learn:**

- When the built-in `Form` is enough and when a package saves code

**Resources:** [flutter_form_builder](https://pub.dev/packages/flutter_form_builder), pub.dev

**Level:** Practitioner · Optional

## Project: Build the Forms

**Brief:** Build the four RealWorld forms: sign-in, sign-up, the article editor and settings. Validate each in the
app and show the errors the API returns. In this stage, sign-up and sign-in call the API through your stage 02
client, extended with POST calls. Keep the returned token in memory only and never store it; stage 07 adds secure
storage. The sign-in and sign-up submit code is Red Zone work, so write it by hand. The editor and settings need a
token, so stage 07 checks that they save.

**Size:** 3 days

**Verification**, checked by a reviewer:

- [ ] Each form validates every field, and the rules match the API's requirements
- [ ] Email fields use the email keyboard, and the sign-in fields are in an `AutofillGroup` with `autofillHints`
- [ ] The focused field and the submit button stay visible above the keyboard on both platforms
- [ ] The return key moves to the next field, and the last field submits the form
- [ ] Submitting an empty or invalid form shows a message next to each problem field and does not call the API
- [ ] Errors from the API appear on the form, and a screen reader announces them
- [ ] The submit button is disabled while the form is being sent
- [ ] The returned token is held in memory only, and is not written to any storage
- [ ] Adding a tag in the editor does not submit the form

Previous: [05. Navigation](./05-navigation.md) · Next: [07. Working with APIs](./07-working-with-apis.md)
