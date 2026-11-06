# 09. Modernizing the Application

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-05

Modernization does not always mean leaving CFML. Adding APIs, a modern interface and AI features can extend an
application's life for years. Back to the [roadmap](./README.md).

## REST APIs in CFML

An API lets new front ends, mobile apps and other systems use the existing business logic.

**What to learn:**

- Building REST endpoints with the engine's REST support or a framework such as ColdBox
- Consistent responses, status codes and error formats
- Authentication for APIs, which is Red Zone work: write it by hand and have a senior engineer review it

**Resources:**

- [Deep expertise guide, section 9](./reference/coldfusion-deep-expertise-guide.md#9-implement-rest-apis-with-proper-error-handling)
- [REST API Best Practices](../../../standards/general/rest-api-best-practices.md)

**Level:** Practitioner · Core

## Separating the front end

Moving the interface to a modern framework, one screen at a time, is a lower-risk alternative to a rewrite.

**What to learn:**

- Replacing old UI tags such as `cfform`, `cfgrid` and `cfwindow`, which depend on outdated client libraries
- Serving a React or Vue front end that calls the CFML API
- Moving one screen at a time while the rest of the application keeps working

**Resources:**

- [React and Next.js Developer roadmap](../../01-software-engineering/02-frontend/react-nextjs/README.md)
- [React documentation](https://react.dev/learn)

**Level:** Practitioner · Core

## Accessibility

Many clients, especially in the public sector and healthcare, must meet accessibility standards.

**What to learn:** basics of WCAG 2.2, the Web Content Accessibility Guidelines: semantic HTML, keyboard use, labels, contrast and testing with a screen reader.

**Resources:** [WCAG 2.2 quick reference](https://www.w3.org/WAI/WCAG22/quickref/)

**Level:** Practitioner · Optional

## AI features in CFML

CFML applications can call AI services over HTTP like any other API, which makes features such as summaries, search and
classification possible without a rewrite.

**What to learn:**

- Calling an AI provider's API with `cfhttp`, with the key kept in a secrets store
- Handling timeouts, rate limits and errors, with a fallback when the service is down
- Keeping personal and client data out of prompts unless the client's contract allows it
- Measuring whether the feature works, with a set of real examples and expected results

**Resources:**

- [CF AI Integration Playbook](./deliverables/cf-ai-integration-playbook.md)
- [Forward Deployed Engineer roadmap: Applied AI](../../08-forward-deployed-engineering/04-applied-ai.md)

**Level:** Practitioner · Core

## Background work

Long tasks such as imports, reports and emails should not run inside a user's request.

**What to learn:**

- Scheduled tasks and how to make them safe to run twice
- `cfthread` for parallel work, and its limits
- Moving heavy work to a queue when the application grows

**Resources:** [Deep expertise guide, section 10](./reference/coldfusion-deep-expertise-guide.md#10-use-cfthread-for-parallel-processing-safely)

**Level:** Practitioner · Optional

## Project: Add an API and an AI Feature

**Brief:** Give the practice app a REST API for posts and comments, and add an AI feature that suggests a summary for
each new post, which the author can edit before publishing.

**Size:** 3–4 days

**Verification**, checked by a senior engineer:

- [ ] API endpoints for listing and reading posts and comments, following the REST API Best Practices, with tests
- [ ] Invalid requests return the right status code and a consistent error format
- [ ] The AI provider is approved by your lead, and the API key comes from an environment variable or secrets store
- [ ] When the AI service times out, the author can still publish, and the error is logged without post content
- [ ] An evaluation of 20 posts: each suggested summary is rated, and the results are written up with three failures
- [ ] Any API authentication was written by hand and reviewed by a senior engineer

Previous: [08. Cloud, Containers and DevOps](./08-cloud-containers-and-devops.md) · Next: [10. Client Consulting and Delivery](./10-client-consulting-and-delivery.md)
