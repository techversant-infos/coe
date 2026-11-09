# 01. HTML, CSS and Accessibility

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Every Vue component ends up as HTML and CSS in the browser. Getting the markup right makes pages usable by
everyone, including people using a keyboard or a screen reader, and makes everything later easier. Back to the
[roadmap](./README.md).

## Semantic HTML

Semantic HTML uses the element that matches the meaning: a `button` for actions, a link for navigation, a `nav` for
navigation menus, headings in order. Browsers, search engines and assistive technology all rely on it.

**What to learn:**

- Landmarks such as `header`, `nav`, `main` and `footer`, and headings that follow a logical order
- Choosing between a link (goes somewhere) and a button (does something)
- Labelling every form field, and giving images useful `alt` text, or empty `alt` text for decorative images

**Resources:**

- [HTML elements reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements), MDN
- [Structuring content with HTML](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content),
  MDN

**Level:** Practitioner · Core

## CSS layout

Flexbox lays things out in one direction, such as a row of buttons. Grid lays things out in rows and columns, such
as a page with a sidebar.

**What to learn:**

- The box model, and how margin, border and padding affect size
- Flexbox for rows and columns of items, and Grid for two-dimensional layouts
- How the cascade and specificity decide which rule wins

**Resources:** [CSS layout](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout), MDN

**Level:** Practitioner · Core

## Responsive design

Client users open the same page on phones, tablets and wide screens. A responsive page adapts to all of them.

**What to learn:**

- The viewport meta tag, and designing for small screens first
- Media queries, and relative units such as `rem` and `%`
- Images that scale, and touch targets large enough to tap

**Resources:**
[Responsive design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design),
MDN

**Level:** Practitioner · Core

## Accessibility basics

Accessibility means people with disabilities can use the page. The Web Content Accessibility Guidelines (WCAG) 2.2
are the W3C standard, and many clients are required by law or contract to meet level AA.

**What to learn:**

- Keyboard use: every action reachable with Tab, Enter and Space, with a visible focus outline
- Colour contrast, and never using colour alone to carry meaning
- When to use ARIA attributes, and why native HTML elements come first

**Resources:**

- [WCAG 2.2 at a glance](https://www.w3.org/WAI/standards-guidelines/wcag/glance/), W3C
- [Accessibility](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility), MDN

**Level:** Practitioner · Core

## Styling approaches

Vue projects style components in different ways: scoped styles inside each component, CSS Modules, or utility
classes such as Tailwind CSS. Follow what your project uses.

**What to learn:**

- How scoped styles and CSS Modules keep styles local to one component
- How utility-first CSS, such as Tailwind CSS, works, and its trade-offs

**Resources:** [Tailwind CSS documentation](https://tailwindcss.com/docs)

**Level:** Practitioner · Optional

## Project: Build the Pages in HTML and CSS

**Brief:** Before writing any JavaScript, build three RealWorld pages as static HTML: the home page, an article page
and the sign-in page. Start from the RealWorld [templates](https://docs.realworld.show/specifications/frontend/templates/)
and the shared stylesheet described on the [practice app](../practice-app.md) page.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] The three pages use the class names and form field names from `specs/e2e/SELECTORS.md`
- [ ] Each page has `header`, `nav`, `main` and `footer` landmarks, and headings in order
- [ ] Every form field has a label, and every meaningful image has `alt` text
- [ ] Every link and button can be reached and used with the keyboard alone, with a visible focus outline
- [ ] The stylesheet's colour variables are overridden, as the practice app page describes, so text has a contrast
  of at least 4.5:1
- [ ] An automated check with axe, for example the axe DevTools browser extension, reports no serious or critical
  issues on any of the three pages
- [ ] The pages are usable at 375 pixels wide and at 1440 pixels wide, with no horizontal scrolling

Next: [02. JavaScript and TypeScript](./02-javascript-and-typescript.md)
