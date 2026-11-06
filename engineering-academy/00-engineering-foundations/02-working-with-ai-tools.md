# 02. Working with AI Tools

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

AI coding assistants such as Claude Code, Codex, Cursor and Copilot can save hours, but you stay accountable for
every line you commit. This stage covers Techversant's rules for using them well and safely. Back to the
[roadmap](./README.md).

## Delegation levels

Before each task, decide how much the AI does. Techversant uses four levels: full delegate, collaborate, human-led
and never delegate.

**What to learn:**

- The four levels and the kinds of task that fit each, such as test stubs (full delegate), business logic
  (collaborate) and system design (human-led)
- The three-question delegation test: can you verify the output quickly, does it need knowledge the AI lacks, and
  could a wrong output reach production unnoticed?
- The rule behind all of it: delegate the typing, never the thinking

**Resources:**

- [Delegation levels](../../standards/general/ai-era-coding-guidelines.md#21-delegation-levels), in the Techversant
  AI Era Coding Guidelines

**Level:** Foundation · Core

## Giving AI context

An AI tool only knows what you tell it. Clear, specific requests with the right context get far better results.

**What to learn:**

- Stating the goal, the constraints and the definition of done in your request
- Pointing the tool at the files, standards and examples that matter
- Keeping prompts that worked, so your team can reuse them

**Resources:**

- [Prompt discipline](../../standards/general/ai-era-coding-guidelines.md#71-prompt-discipline), in the Techversant
  AI Era Coding Guidelines. Its example prompt is for a login API, which is Red Zone work: copy the structure, not
  the task.
- [Developer handbook prompts](../../ai/prompts/developer-handbook-full.md), Techversant's prompt templates

**Level:** Foundation · Core

## Checking AI output

AI output can look right and still be wrong: invented functions, missed edge cases or insecure code. You review it
as carefully as a teammate's code, and you never commit what you cannot explain.

**What to learn:**

- Reading every line, and running the code and its tests before you commit
- Checking edge cases and failure paths, not only the happy path
- Breaking large generated blocks into small functions you understand

**Resources:**

- [Human-in-the-loop](../../standards/general/ai-era-coding-guidelines.md#31-human-in-the-loop-mandatory) and
  [debugging AI output](../../standards/general/ai-era-coding-guidelines.md#62-debugging-ai-output), in the
  Techversant AI Era Coding Guidelines

**Level:** Foundation · Core

## Disclosure and data rules

Your team needs to know where AI helped, and client data must never reach a tool that is not approved for it.

**What to learn:**

- Disclosing AI help in your commit messages, in the format your project uses
- Using only AI tools Techversant has approved
- Never pasting secrets or tokens into any AI tool, and pasting client code, client data or personal data only into
  a tool approved for it
- Checking that generated code does not copy licensed code into the project

**Resources:**

- [AI usage disclosure](../../standards/general/ai-era-coding-guidelines.md#32-ai-usage-disclosure) and
  [data and IP compliance](../../standards/general/ai-era-coding-guidelines.md#53-data--ip-compliance), in the
  Techversant AI Era Coding Guidelines

**Level:** Foundation · Core

## Red Zone work

Some work is too sensitive for AI generation. You write it by hand, and a senior engineer reviews it.

**What to learn:**

- The Red Zone: authentication and authorization, encryption and key management, personal data and payment
  handling, and production database migrations
- Recognizing when an everyday task, such as a small login fix, falls in the Red Zone
- Asking a senior engineer before you start Red Zone work, not after

**Resources:**

- [Red Zone](../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only), in the Techversant AI Era
  Coding Guidelines
- [AI team best practices](../../ai/guides/ai-team-best-practices.md), Techversant

**Level:** Foundation · Core

## Project: Explore and Test with an AI Assistant

**Brief:** Use an AI assistant approved by Techversant to learn one module of the practice app, such as articles or
comments, and to draft unit tests for it. Review and fix the tests yourself, then write a short review note on what
the AI got right and wrong.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] A written summary of the module, in your own words, is correct when checked against the code
- [ ] The delegation level for each task is written down with a reason, using the three-question test
- [ ] At least five new tests are merged through a reviewed PR, and they all pass
- [ ] The review note lists at least two things you changed or rejected in the AI's output, and why
- [ ] No secrets, tokens or personal data appear in the prompts you kept
- [ ] AI help is disclosed in the commit messages
- [ ] You can explain every line of the merged tests when the reviewer asks

Previous: [01. Git and Pull Requests](./01-git-and-pull-requests.md) · Next: [03. Clean Code](./03-clean-code.md)
