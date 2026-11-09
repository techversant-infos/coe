# 06. Forms and Validation

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Forms are where users give the app data: signing in, writing an article, changing settings. A good form tells people
clearly what went wrong and how to fix it, and works for keyboard and screen reader users. Back to the
[roadmap](./README.md).

## Controlled inputs

A controlled input takes its value from React state, and updates the state on every change. React then always knows
what the form holds.

**What to learn:**

- Controlled and uncontrolled inputs, and when each fits
- Handling text fields, checkboxes, selects and text areas
- Disabling the submit button while a form is being sent, so it is not sent twice

**Resources:**
[Reacting to input with state](https://react.dev/learn/reacting-to-input-with-state), React documentation

**Level:** Practitioner · Core

## React Hook Form

React Hook Form manages form state, validation and submission with little code, and keeps re-rendering low on large
forms.

**What to learn:**

- Registering fields with `register`, and handling submission with `handleSubmit`
- Reading field errors from `formState`
- Setting default values, such as the current settings on a settings form

**Resources:** [Get started](https://react-hook-form.com/get-started), React Hook Form documentation

**Level:** Practitioner · Core

## Schema validation with Zod

Zod describes the shape of valid data once, as a schema. The same schema validates the form and gives you the
TypeScript type.

**What to learn:**

- Writing a schema with required fields, lengths and email checks
- Getting the TypeScript type from a schema with `z.infer`
- Connecting a schema to React Hook Form through its resolver
- Why the browser checks are for the user's convenience, and the API must validate everything again

**Resources:**

- [Zod documentation](https://zod.dev/)
- [Input validation](../../../../security/audit/security-audit-reference.md#71-input-validation), in the Techversant
  security audit reference

**Level:** Practitioner · Core

## Accessible error messages

An error message only helps if everyone can find it. Screen reader users need to hear it, and everyone needs to
know which field it belongs to.

**What to learn:**

- Linking each message to its field with `aria-describedby`, and marking invalid fields with `aria-invalid`
- Moving focus to the first invalid field, or to an error summary, after a failed submit
- Writing messages that say how to fix the problem, not only that something is wrong

**Resources:**
[Validating input](https://www.w3.org/WAI/tutorials/forms/validation/) and
[Notifying users](https://www.w3.org/WAI/tutorials/forms/notifications/), W3C forms tutorial

**Level:** Practitioner · Core

## Form actions in React 19

React 19 lets you pass a function to a form's `action` prop. React runs it on submit and tracks whether it is still
running. Next.js uses the same feature for Server Actions in stage 08.

**What to learn:**

- Passing a function to `<form action={...}>`
- `useActionState` for the result of the last submission, such as an error message
- `useFormStatus` for showing that a form is being sent

**Resources:** [useActionState](https://react.dev/reference/react/useActionState), React documentation

**Level:** Advanced · Core

## Project: Build the Forms

**Brief:** Build the four RealWorld forms: sign-in, sign-up, the article editor and settings. Validate each one in
the browser, and show the errors the API returns. In this stage, sign-up and sign-in call the API directly
through your stage 02 client, extended with POST calls. The editor and settings need a token, so stage 07 checks
that they save.

**Size:** 3 days

**Verification**, checked by a reviewer:

- [ ] The four forms use the field names and button text from `specs/e2e/SELECTORS.md`
- [ ] Each form has a Zod schema, and the TypeScript type for the form comes from the schema
- [ ] Submitting an empty or invalid form shows a message next to each problem field, and does not call the API
- [ ] Errors from the API, such as an email address that is already taken, appear in the `.error-messages` list
- [ ] Each message is linked to its field, and focus moves to the first problem after a failed submit
- [ ] The submit button is disabled while the form is being sent
- [ ] Pressing Enter in the editor's tag input adds the tag to the list without submitting the form
- [ ] Every submit button has `type="submit"`, as the RealWorld test helpers expect
- [ ] The settings page's sign-out button has `type="button"` and sits outside the settings form, because the tests
  click the first submit button on the page

Previous: [05. Routing](./05-routing.md) · Next: [07. Working with APIs](./07-working-with-apis.md)
