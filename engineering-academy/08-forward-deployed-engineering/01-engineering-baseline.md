# 01. Engineering Baseline

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

The habits and tools every FDE needs before working on client systems. Back to the [roadmap](./README.md).

## Engineering Foundations

The shared baseline every Techversant engineer completes: Git workflow, safe AI use, secure engineering,
communication and code quality.

**What to learn:** everything in the Foundations completion evidence.

**Resources:** [Engineering Foundations](../00-engineering-foundations/README.md)

**Level:** Foundation · Core

## Git and pull requests

A pull request is the record of a change: why it was made, what was tested and who reviewed it. On a client project
it is also how the client's team learns what you did.

**What to learn:**

- Branching and commit conventions
- Small pull requests with a clear description and test evidence
- Rebasing, resolving conflicts and reverting safely

**Resources:** [Git Workflow](../../standards/git/git-workflow.md)

**Level:** Foundation · Core

## TypeScript

Techversant's default delivery language: one strictly typed language for the UI, the API and background
jobs. About 35% of FDE job postings ask for it ([Bloomberry](https://bloomberry.com/blog/i-analyzed-1000-forward-deployed-engineer-jobs-what-i-learned/)).

**What to learn:**

- `strict` mode, types for API inputs and outputs, `null` handling
- Modules, async code and error handling
- Reading type errors instead of silencing them

**Resources:**

- [Node.js and TypeScript Best Practices](../../standards/nodejs/nodejs-typescript-best-practices.md)
- [TypeScript documentation](https://www.typescriptlang.org/docs/)

**Level:** Practitioner · Core

## Python

Python is the language FDE job postings ask for most, in about 66% of them ([Bloomberry](https://bloomberry.com/blog/i-analyzed-1000-forward-deployed-engineer-jobs-what-i-learned/)).
Most AI and data tools support it first, and many client teams build in it.

**What to learn:**

- Virtual environments and installing packages
- Reading and changing client scripts
- Data scripts and notebooks for quick analysis
- The Python SDKs of the AI providers you use

**Resources:** [The Python Tutorial](https://docs.python.org/3/tutorial/)

**Level:** Practitioner · Core

## Linux and the shell

Client servers, containers and CI runners are usually Linux. You will often work on machines you do not own, with
limited access.

**What to learn:**

- Files, permissions, processes and services
- Reading logs with `grep`, `tail` and `less`
- SSH, environment variables and small shell scripts

**Resources:** [The Linux Command Line](https://linuxcommand.org/tlcl.php)

**Level:** Practitioner · Core

## Data structures and algorithms

Enough to choose a sensible approach, spot slow code and pass technical interviews.

**What to learn:**

- Arrays, maps, sets, trees and queues, and when to use each
- Big-O reasoning for loops and queries
- Sorting, searching and recursion

**Resources:** [MIT 6.006 Introduction to Algorithms](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)

**Level:** Practitioner · Optional

## System design

Choosing an architecture that fits the client's size, budget and team, not the most impressive one.

**What to learn:**

- Monolith or services, synchronous or queued, cache or not
- Designing for failure: timeouts, retries, idempotency
- Explaining a design and its trade-offs to the client

**Resources:**

- [Architecture](../04-architecture/README.md) (planned academy path)
- [The System Design Primer](https://github.com/donnemartin/system-design-primer)

**Level:** Advanced · Core

## Project: Ship a Small Tool Through the Full Workflow

**Brief:** Build a command-line tool in TypeScript that reads a CSV file of synthetic support requests and prints a
summary: requests by status, requests by priority and the oldest open request. Write the same summary as a short
Python script and compare the results. Run both in a Linux container.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] `tsc --strict` passes with no `@ts-ignore` comments
- [ ] Tests cover an empty file, a malformed row and a normal file, and CI runs them on every push
- [ ] The TypeScript and Python versions print the same summary for the same file
- [ ] Both run in a Linux container from a clean checkout, following only the README
- [ ] The pull request follows the [Git Workflow](../../standards/git/git-workflow.md) and has a reviewer's approval
- [ ] You can explain how the tool would behave with one million rows

Back to the [roadmap](./README.md) · Next: [02. Full-Stack Delivery](./02-full-stack-delivery.md)
