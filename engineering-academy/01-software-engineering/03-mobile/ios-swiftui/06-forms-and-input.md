# 06. Forms and Input

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-18 · **Next review:** 2027-02-18

Typing on a phone is slow and the keyboard covers half the screen. Good iPhone forms ask for less, use the right
keyboard, and keep the field the user is typing in visible. Back to the [roadmap](./README.md).

## Text fields

`TextField`, `SecureField` and `TextEditor` are SwiftUI's views for typing. Their modifiers decide which keyboard
appears and what the system offers to fill in.

**What to learn:**

- `TextField` bound to state, `SecureField` for passwords, and `TextEditor` for the article body
- `.keyboardType` for email addresses and URLs, and `.textContentType` so the system knows what each field holds
- Turning off auto-correction and capitalisation where they get in the way, such as in email and username fields

**Resources:** [TextField](https://developer.apple.com/documentation/swiftui/textfield), SwiftUI documentation

**Level:** Practitioner · Core

## The keyboard and focus

The keyboard can hide the field being typed in and the submit button. The app must keep them visible and move focus
in a sensible order.

**What to learn:**

- How SwiftUI moves content out of the keyboard's way, and scroll views that keep the focused field visible
- `@FocusState`, `.submitLabel` and `.onSubmit`, so the return key moves to the next field and submits from the last
- Closing the keyboard when the user scrolls or taps outside a field, such as with `.scrollDismissesKeyboard`

**Resources:** [FocusState](https://developer.apple.com/documentation/swiftui/focusstate), SwiftUI documentation

**Level:** Practitioner · Core

## Validation

Each form checks its fields before sending them, and shows the API's errors when the server rejects them.

**What to learn:**

- Validation rules in the model, not in the view, with an error message for each field
- Showing the API's errors, such as "email has already been taken", next to the right field
- Why checks in the app are for the user's convenience: the API must validate everything again

**Resources:** [Input validation](../../../../security/audit/security-audit-reference.md#71-input-validation), in the
Techversant security audit reference

**Level:** Practitioner · Core

## Password AutoFill

iOS can fill in saved email addresses and passwords, and suggest strong passwords on sign-up, which makes signing in
faster and safer.

**What to learn:**

- `.textContentType(.username)`, `.password` and `.newPassword` on the sign-in and sign-up fields
- How strong password suggestions work, and how the Associated Domains capability links the app to a website, so iOS can
  offer that website's saved passwords

**Resources:** [Password AutoFill](https://developer.apple.com/documentation/security/password-autofill), Apple

**Level:** Practitioner · Core

## Accessible forms

VoiceOver users need to know what each field is for and what went wrong.

**What to learn:**

- A visible label on every field, which VoiceOver also reads, and `.accessibilityLabel` where the label is an icon
- Announcing errors after a failed submit, and moving focus to the first field with an error
- Touch targets large enough for every button, including the tag remove buttons, at every text size

**Resources:**
[Accessibility fundamentals](https://developer.apple.com/documentation/swiftui/accessibility-fundamentals), SwiftUI
documentation

**Level:** Practitioner · Core

## Pickers and other controls

Client apps often need dates, choices and numbers. SwiftUI has standard controls for each, which work with VoiceOver
and Dynamic Type without extra code.

**What to learn:**

- `Picker`, `DatePicker`, `Toggle` and `Stepper`, and when each suits the data

**Resources:** [Controls and indicators](https://developer.apple.com/documentation/swiftui/controls-and-indicators),
SwiftUI documentation

**Level:** Practitioner · Optional

## Project: Build the Forms

**Brief:** Build the four RealWorld forms: sign-in, sign-up, the article editor and settings. Validate each in the app
and show the errors the API returns. In this stage, sign-up and sign-in call the API through your stage 02 client,
extended with POST calls. Keep the returned token in memory only and never store it; stage 07 adds the Keychain. The
sign-in and sign-up submit code, and the email and password change in Settings, are Red Zone work, so write them by
hand. The editor and settings need a token, so stage 07 checks that they save.

**Size:** 3 days

**Verification**, checked by a reviewer:

- [ ] Each form validates every field, and the rules match the API's requirements
- [ ] Email fields use the email keyboard, and the sign-in and sign-up fields have the right `.textContentType`
- [ ] The focused field and the submit button stay visible above the keyboard
- [ ] The return key moves to the next field, and the last field submits the form
- [ ] Submitting an empty or invalid form shows a message next to each problem field and does not call the API
- [ ] Errors from the API appear on the form, and VoiceOver announces them
- [ ] The submit button is disabled while the form is being sent
- [ ] The returned token is held in memory only, and is not written to any storage
- [ ] Adding a tag in the editor does not submit the form

Previous: [05. Navigation](./05-navigation.md) · Next: [07. Working with APIs](./07-working-with-apis.md)
