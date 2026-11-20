# 01. Language Fundamentals

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-20 · **Next review:** 2027-05-20

CFML (ColdFusion Markup Language) is the language; Lucee and Adobe ColdFusion are the engines that run it. Most client
code you meet mixes two styles, tags and script, so you learn to read both and write new code in script. Solid CFML
makes every ColdBox feature in the next stages easier to understand. Back to the [roadmap](./README.md).

## Running CFML with CommandBox

CommandBox starts a CFML server from any folder with one command, so every developer runs the same engine and
version. You use it on every stage of this path.

**What to learn:**

- Installing CommandBox, and starting a named server on your computer, such as
  `box server start name=cfml-fundamentals cfengine=lucee@7.1 host=127.0.0.1 port=8500`
- Choosing the engine and version with `cfengine`, recording the version you use, and stopping the server when you
  finish
- Reading an error page: the template, the line number and the message
- Looking inside a page with `<cfdump var="#variables#">` or `writeDump(variables)`, and removing every dump before
  you commit, because a dump can show data to anyone who opens the page

**Resources:**

- [Getting started with CommandBox](https://docs.lucee.org/guides/getting-started/commandbox.html), Lucee
  documentation
- [Multi-engine support](https://commandbox.ortusbooks.com/embedded-server/multi-engine-support), CommandBox
  documentation
- [Debugging](https://learncfinaweek.com/course/index/section/Error_Handling_and_Debugging/item/Debugging.html),
  Learn CF in a Week

**Level:** Practitioner · Core

## Tags, script and variables

CFML can be written as tags, such as `<cfset>`, inside `.cfm` templates, or as script, which looks like JavaScript.
Older applications are mostly tags. Techversant writes new logic in script and keeps tags for HTML output.

**What to learn:**

- `<cfset>` and `<cfoutput>` in tags, and the same work in a `<cfscript>` block
- Simple values: strings, numbers, booleans (`true` and `false`) and dates, made with `createDate()` and shown with
  `dateFormat()`
- `#` around an expression to output it, such as `#variables.requestCount#`
- Comments: `<!--- ... --->` in templates, and `//` or `/* ... */` in script

**Resources:**

- [Setting variables](https://learncfinaweek.com/course/index/section/Basics/item/Setting_Variables.html),
  [Script vs. tag](https://learncfinaweek.com/course/index/section/Basics/item/Script_vs_Tag.html),
  [Data types](https://learncfinaweek.com/course/index/section/Basics/item/Datatypes.html) and
  [Commenting](https://learncfinaweek.com/course/index/section/Basics/item/Commenting.html), Learn CF in a Week
- [CFScript best practices](../../../../standards/coldfusion/coldfusion-style-guide.md#5-cfscript-best-practices), in
  the Techversant ColdFusion style guide

**Level:** Practitioner · Core

## Arrays, structs, lists and queries

Most CFML code moves records around: an array of structs from a form, or a query of rows from the database. Lists
appear everywhere in older code.

**What to learn:**

- Arrays (which start at 1, not 0), structs, and an array of structs; reading keys with dot and bracket notation
- Checking for a missing key with `structKeyExists()`, and handling an empty array
- Lists: a string of values with a separator, such as `"all,open,closed"`, with `listLen()` and `listFindNoCase()`.
  Use arrays for new data, and read lists confidently in old code
- Query objects: rows and named columns, building one in memory with `queryNew()`, and looping over its rows

**Resources:**

- [Data types](https://learncfinaweek.com/course/index/section/Basics/item/Datatypes.html) and
  [Databases](https://learncfinaweek.com/course/index/section/Data_Handling/item/Databases.html), Learn CF in a Week
- [queryNew()](https://docs.lucee.org/reference/functions/querynew.html), Lucee documentation

**Level:** Practitioner · Core

## Decisions and loops

Decisions choose what a page does, and loops repeat work for each record. Both have a tag form and a script form.

**What to learn:**

- `<cfif>`, `<cfelseif>` and `<cfelse>`, and `if`, `else if` and `else` in script
- Comparison operators in both styles, such as `EQ` and `NEQ` in tags and `==` and `!=` in script
- `<cfloop>` over an array, a list, a query and a range, and `for` loops in script
- Naming the loop variable so it does not overwrite another variable on the page

**Resources:**

- [Decision making](https://learncfinaweek.com/course/index/section/Decision_Making_and_Scopes/item/Decision_Making.html)
  and [Looping](https://learncfinaweek.com/course/index/section/Looping/item/Looping.html), Learn CF in a Week

**Level:** Practitioner · Core

## Scopes and request input

A scope is a named collection of variables. Knowing which scope a value comes from prevents the most common CFML bug,
and treating browser input with care prevents the most common security bugs.

**What to learn:**

- `variables` for the page, `local` and `arguments` inside a function, and `url` and `form` for browser input
- Giving missing input a default with `<cfparam name="url.status" default="all">`, or `param` in script
- Trimming, normalising and checking input against the allowed values before you use it
- The unscoped lookup: when code names a variable without a scope, such as `status`, the engine searches scopes in a
  fixed order. Outside a function, both engines check `variables` first, so a page variable can hide the browser's
  value. Lucee then checks `url` and `form`; Adobe ColdFusion's security updates since March 2024 stop there and
  throw an error instead, unless `this.searchImplicitScopes` is turned on. Name the scope every time
- Encoding every value you output in HTML with `encodeForHTML()`, so a value from the browser cannot run as script

**Resources:**

- [Scopes](https://www.learncfinaweek.com/course/index/section/Decision_Making_and_Scopes/item/Scopes.html), Learn CF
  in a Week
- [Scope](https://docs.lucee.org/guides/developing-with-lucee-server/scope.html), Lucee documentation
- [Security practices](../../../../standards/coldfusion/coldfusion-style-guide.md#7-security-practices), in the
  Techversant ColdFusion style guide

**Level:** Practitioner · Core

## Functions and components

A function does one job with named inputs and a return value. A component, a `.cfc` file, groups related functions,
like a class. Pages read input and show HTML; components do the work.

**What to learn:**

- Writing a function with typed arguments, a default value and a return type, such as
  `public array function filterByStatus(required array requests, string status = "all")`
- Creating a component with `new RequestService()`, and keeping its working variables in `local`
- Recognising includes, custom tags and `Application.cfc` when you read an older application; stage 02 covers
  `Application.cfc`

**Resources:**

- [Functions](https://learncfinaweek.com/course/index/section/Code_Reuse/item/Functions.html),
  [Components](https://learncfinaweek.com/course/index/section/Code_Reuse/item/Components.html),
  [Includes](https://learncfinaweek.com/course/index/section/Code_Reuse/item/Includes.html) and
  [Custom tags](https://learncfinaweek.com/course/index/section/Code_Reuse/item/Custom_Tags.html), Learn CF in a Week
- [Component design](../../../../standards/coldfusion/coldfusion-style-guide.md#8-component-design), in the
  Techversant ColdFusion style guide

**Level:** Practitioner · Core

## Code style and naming

A shared style keeps reviews about behaviour, not formatting. Techversant's ColdFusion style guide sets the rules for
names, layout and script.

**What to learn:**

- The naming rules for files, components, functions and variables
- Indentation and layout for tags and script
- Formatting code automatically before every commit

**Resources:**

- [Code formatting and syntax](../../../../standards/coldfusion/coldfusion-style-guide.md#3-code-formatting--syntax)
  and [Naming conventions](../../../../standards/coldfusion/coldfusion-style-guide.md#4-naming-conventions), in the
  Techversant ColdFusion style guide
- [ColdFusion best practices](../../../../standards/coldfusion/coldfusion-best-practices.md), Techversant

**Level:** Practitioner · Core

## Project: Build and Debug a Service-Request List

**Brief:** Before you use a framework, build a small CFML page that lists service requests and filters them by
status, then fix a scope bug in an older page. Use only the sample data below, and run everything on Lucee 7.1 with
CommandBox.

| ID | Title | Status | Created |
|----|-------|--------|---------|
| 101 | Reset demo account | open | 2026-11-10 |
| 102 | Update sample report | closed | 2026-11-11 |
| 103 | Review test dashboard | open | 2026-11-12 |

1. Keep the sample data as an array of structs in `sample-requests.cfm`, with each date made by `createDate()`.
2. Write `RequestService.cfc` with
   `public array function filterByStatus(required array requests, string status = "all")`.
3. Write `index.cfm`: read `url.status`, default it to `all`, trim it, make it lower case, and allow only `all`,
   `open`, `closed` or `pending`. Pass the checked value to the component and show the titles and dates, an empty
   state or a validation message.
4. Add this older page as `legacy.cfm`. Open `legacy.cfm?status=closed`: it shows the two open requests. Find which
   scope the page reads, and fix it.

```cfm
<cfinclude template="sample-requests.cfm">
<cfparam name="url.status" default="all">
<!--- The author set a default tab here, and later meant "status" to be the browser's value. --->
<cfset status = "open">
<cfset variables.requestService = new RequestService()>

<cfif NOT listFindNoCase("all,open,closed,pending", trim(status))>
  <p>Choose all, open, closed, or pending.</p>
<cfelse>
  <cfset variables.results = variables.requestService.filterByStatus(variables.requests, lCase(trim(status)))>
  <cfif arrayLen(variables.results) EQ 0>
    <p>No matching requests.</p>
  <cfelse>
    <ul>
      <cfloop array="#variables.results#" index="variables.result">
        <cfoutput><li>#encodeForHTML(variables.result.title)#</li></cfoutput>
      </cfloop>
    </ul>
  </cfif>
</cfif>
```

**Size:** 1 day

**Verification**, checked by a reviewer:

- [ ] The README records the Lucee version and the command that starts the server, and the reviewer starts the app
  from it
- [ ] The pull request notes the template and line an error page reported for a deliberate mistake, which you then
  reverted
- [ ] `index.cfm` shows all three requests with no status or `all`; 101 and 103 for `open` or `OPEN`; 102 for
  `closed`; an empty state for `pending`; and a validation message for an empty or unknown value
- [ ] The component returns a new array, uses only `arguments` and `local` inside the function, and does no input
  checking or HTML
- [ ] `legacy.cfm` reads `url.status` by name, and the pull request gives the failing URL, the wrong output, the scope
  the engine used and why, and the result after the fix
- [ ] Every value output in HTML goes through `encodeForHTML()`, and no dumps remain
- [ ] The code follows the Techversant ColdFusion style guide for names, scopes and indentation
- [ ] In the review, you add a request with the status `pending`, show the filter change, and explain the `url`,
  `variables`, `local` and `arguments` scopes in your code

Next: [02. The Framework](./02-the-framework.md)
