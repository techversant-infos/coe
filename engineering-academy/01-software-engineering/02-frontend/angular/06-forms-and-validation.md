# 06. Forms and Validation

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Forms are where users give the app data: signing in, writing an article, changing settings. A good form tells people
clearly what went wrong and how to fix it, and works for keyboard and screen reader users. Back to the
[roadmap](./README.md).

## Signal Forms

Signal Forms, stable in Angular 22, build a form from a signal that holds the form's data. Angular tracks each
field's value, errors and state as signals.

**What to learn:**

- Creating a form with `form()` from a signal model, and binding inputs with `[formField]`
- Why `[formField]` replaces each input's `name` with a generated value, and keeping the names the contract needs, such
  as `name="email"`, by wrapping the input in a small custom control (`FormValueControl`)
- Built-in validators, such as `required`, `email` and `minLength`, declared in the form's schema
- Submitting with `submit()` or `[formRoot]`, disabling the button while `submitting()` is true, and returning
  errors from the API so they show on the right fields

**Resources:**

- [Signal Forms overview](https://angular.dev/guide/forms/signals/overview) and
  [Form submission](https://angular.dev/guide/forms/signals/form-submission), Angular documentation

**Level:** Practitioner · Core

## Schema validation with Zod

Zod describes the shape of valid data once, as a schema. The same schema validates the form and gives you the
TypeScript type.

**What to learn:**

- Writing a schema with required fields, lengths and email checks
- Getting the TypeScript type from a schema with `z.infer`
- Validating a Signal Form with a Zod schema through `validateStandardSchema`
- Why the browser checks are for the user's convenience, and the API must validate everything again

**Resources:**

- [validateStandardSchema](https://angular.dev/api/forms/signals/validateStandardSchema), Angular documentation
- [Input validation](../../../../security/audit/security-audit-reference.md#71-input-validation), in the Techversant
  security audit reference

**Level:** Practitioner · Core

## Reactive forms

Most existing Angular projects use reactive forms, built from `FormGroup` and `FormControl`. You need them to work on
those projects.

**What to learn:**

- `FormGroup`, `FormControl` and built-in validators, and reading a control's errors
- How reactive forms compare with Signal Forms, and following what your project uses

**Resources:** [Reactive forms](https://angular.dev/guide/forms/reactive-forms), Angular documentation

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

## Project: Build the Forms

**Brief:** Build the four RealWorld forms with Signal Forms: sign-in, sign-up, the article editor and settings.
Validate each one in the browser, and show the errors the API returns. In this stage, sign-up and sign-in call the API
directly through your stage 02 client, extended with POST calls. The editor and settings need a token, so stage 07
checks that they save.

**Size:** 3 days

**Verification**, checked by a reviewer:

- [ ] The four forms use the field names and button text from `specs/e2e/SELECTORS.md`, checked in the rendered page,
  because `[formField]` replaces `name` attributes
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
