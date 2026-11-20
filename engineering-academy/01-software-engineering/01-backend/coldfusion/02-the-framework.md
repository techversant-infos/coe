# 02. The Framework

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-20 · **Next review:** 2027-05-20

ColdBox gives a ColdFusion Markup Language (CFML) application a structure, a set of tools and a way of doing common
jobs, so every new Techversant ColdFusion API feels familiar. Trace a request through `Application.cfc` and ColdBox
to see where your code fits. This stage uses ColdBox 8.2 or later in the 8.x series. Back to the [roadmap](./README.md).

## Application.cfc and the request lifecycle

Every CFML application starts with `Application.cfc`. It names the application, sets its options and runs code at
the start and end of each request, with or without a framework.

**What to learn:**

- `this.name`, application and session timeouts, and the events `onApplicationStart`, `onRequestStart`,
  `onRequestEnd` and `onError`
- Turning off the unscoped lookup of browser input, so a missing scope fails instead of reading `url` or `form` by
  accident: `this.scopeCascading = "strict"` on Lucee, and `this.searchImplicitScopes = false` on Adobe ColdFusion,
  which current updates set by default
- How ColdBox's own `Application.cfc` hands each request to the framework

**Resources:**

- [Application.cfc](https://learncfinaweek.com/course/index/section/Application_cfc/item/Application_cfc.html),
  Learn CF in a Week
- [Application variables](https://helpx.adobe.com/coldfusion/cfml-reference/application-cfc-reference/application-variables.html),
  Adobe ColdFusion documentation
- [ColdFusion best practices](../../../../standards/coldfusion/coldfusion-best-practices.md), Techversant:
  the Application.cfc section

**Level:** Practitioner · Core

## ColdBox projects and CommandBox

CommandBox creates a ColdBox project from a template and installs packages from ForgeBox, the CFML package
registry. Every ColdBox project has the same folders, so you can find your way around any of them.

**What to learn:**

- Creating an API project from the REST template, such as `coldbox create app name=realworld-api skeleton=rest`
- What lives in `config`, `handlers`, `models`, `interceptors`, `modules` and `tests`
- `box.json` and `server.json`: the packages, engine and port the project needs, and why both are committed
- Removing the template's sample `Auth` handler and user model: stage 06 writes sign-in by hand

**Resources:**

- [Installation](https://coldbox.ortusbooks.com/getting-started/installation),
  [Application templates](https://coldbox.ortusbooks.com/getting-started/application-templates),
  [60-minute quick start](https://coldbox.ortusbooks.com/for-newbies/60-minute-quick-start) and
  [Conventions](https://coldbox.ortusbooks.com/getting-started/conventions), ColdBox documentation
- [Configuring your server](https://commandbox.ortusbooks.com/embedded-server/configuring-your-server), CommandBox
  documentation

**Level:** Practitioner · Core

## Routing and handlers

The router maps a method and URL to a handler action. A handler groups the actions for one resource, like a
controller.

**What to learn:**

- Routes in `config/Router.cfc`: route parameters, HTTP methods, route groups and the `/api` prefix
- Handlers that extend `coldbox.system.RestHandler`, which returns JSON and turns errors into JSON responses, and
  its default response envelope, which stage 03 replaces with the RealWorld shape
- The request context `event` and the response object `event.getResponse()`, and keeping business logic out of
  handlers

**Resources:**

- [Routing](https://coldbox.ortusbooks.com/the-basics/routing),
  [Event handlers](https://coldbox.ortusbooks.com/the-basics/event-handlers),
  [Request context](https://coldbox.ortusbooks.com/the-basics/request-context) and
  [RestHandler](https://coldbox.ortusbooks.com/digging-deeper/rest-handler), ColdBox documentation

**Level:** Practitioner · Core

## Interceptors

Interceptors run at set points in every request, such as before a handler runs or after the response is ready. Use
them for work that every request needs, such as adding a request ID or checking the sign-in token.

**What to learn:**

- Writing an interceptor, registering it in `config/ColdBox.cfc`, and the main points such as `preProcess` and
  `postProcess`
- Route middleware, added in ColdBox 8.2, for work that only some routes need
- When to use an interceptor, route middleware or a handler's `preHandler`

**Resources:**

- [Interceptors](https://coldbox.ortusbooks.com/the-basics/interceptors),
  [Core interception points](https://coldbox.ortusbooks.com/the-basics/interceptors/core-interception-points)
  and [Middleware](https://coldbox.ortusbooks.com/the-basics/routing/routing-dsl/middleware), ColdBox documentation

**Level:** Practitioner · Core

## WireBox and models

WireBox, ColdBox's dependency injection library, creates your models and passes in what they need, so handlers stay
small and models can be tested on their own.

**What to learn:**

- Models in the `models` folder, injected with `property name="articleService" inject="ArticleService";`
- Singletons, and why a singleton must never keep data for one request in its `variables` scope
- Keeping the work in models and services, and limiting the handler to reading input and returning a response

**Resources:**

- [Models](https://coldbox.ortusbooks.com/the-basics/models), ColdBox documentation
- [WireBox](https://wirebox.ortusbooks.com/), Ortus documentation
- [ColdFusion best practices](../../../../standards/coldfusion/coldfusion-best-practices.md), Techversant:
  the dependency injection section

**Level:** Practitioner · Core

## Views, layouts and HTML

Many CFML applications build their pages on the server. ColdBox renders a view inside a layout, the same job older
applications do with header and footer includes.

**What to learn:**

- A page handler that extends `coldbox.system.EventHandler`, setting a view with `event.setView()` and passing data
  to it in `prc`
- Layouts in `layouts` and views in `views`, and semantic HTML: headings, lists, links and forms with labels
- A stylesheet file instead of inline styles, and a layout that works on a phone screen
- Encoding every value in a view with `encodeForHTML()`

**Resources:**

- [Layouts and views](https://coldbox.ortusbooks.com/the-basics/layouts-and-views), ColdBox documentation
- [Structuring content with HTML](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content)
  and [CSS styling basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics), MDN Web
  Docs
- [Semantic HTML](../../02-frontend/react-nextjs/01-html-css-and-accessibility.md#semantic-html), in the React and
  Next.js roadmap

**Level:** Practitioner · Core

## Configuration and environments

Settings that change between your machine, staging and production live in environment variables, never in code.

**What to learn:**

- What a new machine needs: CommandBox and Git. `server.json` sets the engine and the Java version, such as
  `"jvm": {"javaVersion": "openjdk21_jre"}`, and CommandBox downloads both on the first start
- `config/ColdBox.cfc`, the environment settings in it, and reading environment variables with
  `getSystemSetting()`
- Installing the CommandBox `commandbox-dotenv` module to load local settings from `.env`. Commit
  `.env.example` with example values and keep your local `.env` out of Git.
- Turning off debug output outside your own machine, and protecting the framework's restart URL with a password

**Resources:**

- [Configuration](https://coldbox.ortusbooks.com/getting-started/configuration) and
  [Configuration directives](https://coldbox.ortusbooks.com/getting-started/configuration/coldbox.cfc/configuration-directives),
  ColdBox documentation
- [CommandBox dotenv module](https://www.forgebox.io/view/commandbox-dotenv), ForgeBox
- [Keys and secrets management](../../../../security/audit/security-audit-reference.md#63-keys-and-secrets-management),
  in the Techversant security audit reference

**Level:** Practitioner · Core

## Reading older CFML applications

Many client applications use an older framework, such as FW/1 or Fusebox, or none at all. You need to find where a
request starts and which file does the work before you change anything.

**What to learn:**

- Spotting the framework from the files: `Application.cfc` or `Application.cfm`, `index.cfm` with `fuseaction` or
  `action` in the URL, and folders such as `controllers` or `circuits`
- Tracing one request from the URL to the query and the output
- Changing only what the task needs, and matching the style of the code around it

**Resources:**

- [Framework detection](../../../07-consulting/coldfusion/05-assessing-legacy-applications.md#framework-detection) and
  [Understanding inherited code](../../../07-consulting/coldfusion/04-maintaining-legacy-applications.md#understanding-inherited-code),
  in the Senior ColdFusion Consultant roadmap
- [ColdFusion best practices](../../../../standards/coldfusion/coldfusion-best-practices.md), Techversant:
  the joining an existing project section

**Level:** Practitioner · Optional

## Project: Start the API

**Brief:** Create a ColdBox 8.x project for your RealWorld API on Lucee 7.1, and add the first endpoint,
`GET /api/tags`, returning `{"tags": []}` for now. Add a home page at `/` that shows the same tags, rendered on the
server; stage 03 adds browser code to it.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] `box.json` pins the exact ColdBox 8.x version used for the project. Use at least 8.2.0 for route middleware.
  `server.json` pins Lucee 7.1 and the Java version.
- [ ] Starting with CommandBox and Git, the reviewer installs the CLI module with `box install commandbox-dotenv`,
  clones the project, and copies `.env.example` to `.env` in the project folder. The reviewer fills in the local
  values documented in the README, runs `box install` and `box server start` there, and verifies that the app starts
  and uses its local settings
- [ ] `GET /api/tags` returns status 200 and exactly `{"tags": []}`, with the key in lower case and no `data`
  envelope
- [ ] The home page uses a layout and a view, links a stylesheet, shows "No tags yet" while the list is empty, and
  encodes every value it outputs
- [ ] An unknown path under `/api` returns a JSON 404, not an HTML page
- [ ] An interceptor adds a request ID to every response header and log line, and has a simple TestBox spec;
  stage 08 covers testing in depth
- [ ] `Application.cfc` sets `this.scopeCascading = "strict"` and `this.searchImplicitScopes = false`
- [ ] Git ignores `.env`, `.env.example` lists every setting, and code reads settings through the ColdBox
  configuration
- [ ] The README explains how to install, run and test the project

Previous: [01. Language Fundamentals](./01-language-fundamentals.md) · Next:
[03. HTTP and REST APIs](./03-http-and-rest-apis.md)
