# 06. Working with Existing Systems

**Status:** Draft · **Owner:** TBD · **Last updated:** 2026-10-29 · **Next review:** 2027-01-29

**Level:** Foundation · **Time:** about 2 hours (40 minutes reading, 80 minutes practice) · **Pilot draft**

## Learning Objectives

By the end of this module, you will be able to:

- [ ] Map how one feature of an unfamiliar application works, from the screen to the database
- [ ] Use an AI agent to explore code, and check its explanation against the code itself
- [ ] Write a test that records what the code does today, before you change it
- [ ] Make the smallest change that meets the acceptance criteria and keeps existing callers working
- [ ] Recognise when to stop and ask instead of changing more

## Why This Matters

Most of the code you change at work was written by someone else, often years ago. It has users, callers and data that
depend on how it behaves today, including its odd parts.

A change that works on its own but breaks one of those dependents is a failed change. This module teaches you to
understand first, record what exists, and then change as little as you can.

> **Note:** Feeling lost in a new codebase is normal, even for senior engineers. The skill is having a method, not
> knowing everything already.

## Map Before You Change

Follow one feature from end to end before you touch it. In the training application (a service-request tracker), the
request list works like this:

```text
web/src/pages/RequestList.tsx      the screen that shows the list
  -> GET /api/requests             the HTTP call it makes
api/src/requests/requests.routes.ts    reads the query, returns JSON
  -> requests.service.ts           business rules, such as "open only"
  -> requests.repository.ts        the SQL query
db/migrations/                     the table the data lives in
```

Build a map like this for any feature you change. These steps get you there:

1. **Read the guidance files.** Start with `README.md` and `AGENTS.md`. They say how to run the app and which folders
   need care.
2. **Run the application.** Click through the feature, so you know what users see.
3. **Follow one call.** Start at the screen, find the HTTP call, then follow it into the API and down to the query.
4. **Find the tests.** Existing tests show what the team cared about. Missing tests show where changes are risky.
5. **Read the history.** History often explains code that looks wrong.

```bash
# Every commit that touched the file, newest first
git log --oneline -- api/src/requests/requests.service.ts

# Who last changed lines 10-30, and in which commit
git blame -L 10,30 api/src/requests/requests.service.ts
```

### Explore with an agent, then check

An AI agent can draft the map quickly. Give it the question and a narrow scope:

```text
Explain how GET /api/requests works in this repository. List each file it passes
through, in order, with the function names. Do not change any files.
```

Treat the answer as a draft. Open each file it names and confirm the functions exist and do what it says. Agents can
describe code that is not there, or miss a branch that matters.

> **Note:** "Do not change any files" in a prompt is a request, not a control. When you only want exploration, use
> your tool's permission settings to allow reading files and nothing else.

## Record What the Code Does Today

Before you change code, write a test that records its current behaviour. Some teams call this a characterisation
test. It protects behaviour you did not mean to change.

Here is a function from the training application that sets each request's due date:

```typescript
// api/src/requests/due-date.ts
export type Priority = "low" | "normal" | "urgent";

// Response targets agreed with the support team, in hours
const HOURS_BY_PRIORITY: Record<Priority, number> = { low: 72, normal: 24, urgent: 4 };

export function calculateDueDate(priority: Priority, createdAt: Date): Date {
  const due = new Date(createdAt.getTime() + HOURS_BY_PRIORITY[priority] * 60 * 60 * 1000);

  // Nobody works weekends, so a due date on Saturday or Sunday moves to Monday 09:00 UTC
  const day = due.getUTCDay();
  if (day === 6 || day === 0) {
    const daysToMonday = day === 6 ? 2 : 1;
    due.setUTCDate(due.getUTCDate() + daysToMonday);
    due.setUTCHours(9, 0, 0, 0);
  }
  return due;
}
```

Write tests that describe what it does now, not what you think it should do:

```typescript
// api/test/due-date.current.test.ts
import { describe, expect, it } from "vitest";
import { calculateDueDate } from "../src/requests/due-date.ts";

describe("calculateDueDate: current behaviour", () => {
  it("adds 24 hours to a normal request raised on a weekday", () => {
    const created = new Date("2026-11-03T10:00:00Z"); // Tuesday
    expect(calculateDueDate("normal", created).toISOString()).toBe("2026-11-04T10:00:00.000Z");
  });

  it("moves a due date that lands on Saturday to Monday 09:00 UTC", () => {
    const created = new Date("2026-11-06T12:00:00Z"); // Friday; +24 hours is Saturday
    expect(calculateDueDate("normal", created).toISOString()).toBe("2026-11-09T09:00:00.000Z");
  });

  it("gives an urgent request raised on Friday night a Monday due date", () => {
    const created = new Date("2026-11-06T22:00:00Z"); // Friday; +4 hours is Saturday
    expect(calculateDueDate("urgent", created).toISOString()).toBe("2026-11-09T09:00:00.000Z");
  });
});
```

All three tests pass. The third one records something surprising: an urgent request raised on Friday night waits
about 59 hours.

That may be a bug, or it may be what the business agreed. Do not fix it as a side effect of another task. Write it in
the issue as a question for the person who owns the requirement. A test that records odd behaviour is a useful
outcome.

## Make the Smallest Compatible Change

When you change the code, keep everything that already depends on it working:

- **Add, don't remove.** Add new fields, parameters and functions. Removing or renaming them breaks callers you may
  not know about.
- **Make new inputs optional,** with a default that keeps the old behaviour.
- **Keep changes in one place.** A change that touches 15 files for a one-line requirement needs a second look.

### Across the stack

Compatibility means something different in each layer:

| Layer | Compatible | Breaks callers |
|-------|------------|----------------|
| API | A new optional query parameter; a new field in the response | A renamed field; a parameter that becomes required |
| Data | A new nullable column; a new table | Dropping or renaming a column that running code still reads |
| UI | A new control that leaves existing flows unchanged | Moving or relabelling a control people and tests rely on |

For data, change in two steps: add the new column first, then remove the old one in a later release once nothing
reads it. Production database migrations are Red Zone work, so a person writes them and a senior engineer reviews them.

## When to Stop and Ask

Stop and ask your lead before you continue when:

- the change touches a Red Zone area, such as login, permissions, encryption, personal data or payments;
- the code behaves in a way you cannot explain, and the history does not help;
- there are no tests and the change is risky;
- the change keeps growing beyond what the request needed.

Asking at the right moment is a skill the assessment rewards. Guessing quietly is not.

## With AI Agents

| Delegate | Check yourself |
|----------|----------------|
| A first map of how a feature works | Every file and function the map names exists and behaves as described |
| Drafting tests that record current behaviour | Each test asserts real current behaviour and would fail if that behaviour changed |
| A first version of a small change, with the acceptance criteria as context | The diff is small, keeps old behaviour, and touches nothing outside the task |

An agent reporting that "all tests pass" is not evidence on its own. Run the tests yourself and read the diff.

## Exercise: Filter the Request List by Assignee

**Objective:** Make a compatible change to existing code, using an agent for part of it, and explain what you
accepted and rejected.

**Prerequisites:** Modules 01–05. The training application running locally.

**Request:** Support leads want to see only the open requests assigned to one person.

**Acceptance criteria:**

- `GET /api/requests?assignee=7` returns only the open requests assigned to user 7.
- `GET /api/requests` with no parameter returns exactly what it returns today.
- A value that is not a whole number returns `400` with an error code.

**Instructions:**

1. Map the request list from the screen to the query. Write the map in your issue, in five lines or fewer.
2. Write a test that records today's response for `GET /api/requests`. It must pass before you change anything.
3. Ask your agent for the change. Give it the acceptance criteria. Limit its permissions to editing files in `api/src`
   and `api/test` and running the tests.
4. Review the agent's diff line by line. In your pull request, list what you accepted, what you changed and why.
5. Add tests for the new behaviour. Undo your change briefly and confirm the new tests fail without it.

**Expected outcome:** One small pull request. The test from step 2 still passes. The new tests cover all three
acceptance criteria. The pull request lists what you accepted and rejected from the agent.

<details>
<summary>Reveal a model solution</summary>

The service gains an optional filter. Existing callers pass nothing, so they get the same result as before:

```typescript
// api/src/requests/requests.service.ts (changed part)
export interface ListFilters {
  // Optional, so every existing caller keeps working without passing it
  assigneeId?: number;
}

export async function listOpenRequests(filters: ListFilters = {}): Promise<ServiceRequest[]> {
  const open = await findOpenRequests();
  if (filters.assigneeId === undefined) {
    return open;
  }
  return open.filter((request) => request.assigneeId === filters.assigneeId);
}
```

The route keeps the old path unchanged and validates the new input strictly:

```typescript
// api/src/requests/requests.routes.ts
import { Router } from "express";
import { listOpenRequests } from "./requests.service.ts";

export const requestsRouter = Router();

requestsRouter.get("/", async (req, res) => {
  const rawAssignee = req.query.assignee;

  // No assignee parameter: behave exactly as before
  if (rawAssignee === undefined) {
    res.json({ data: await listOpenRequests() });
    return;
  }

  // Accept digits only; reject empty, decimal, negative and repeated values instead of guessing
  if (typeof rawAssignee !== "string" || !/^[0-9]+$/.test(rawAssignee)) {
    res.status(400).json({ error: { code: "INVALID_ASSIGNEE", message: "assignee must be a whole number" } });
    return;
  }

  res.json({ data: await listOpenRequests({ assigneeId: Number(rawAssignee) }) });
});
```

Things a reviewer looks for in your pull request:

- `?assignee=7&assignee=8` arrives as an array, and `?assignee=` as an empty string. Both must return `400`, not an
  empty list.
- A common agent draft uses `Number(value)` alone. That turns an empty value into `0` and quietly returns nothing.
  Catching that is the kind of rejection to list.
- Filtering in the service is fine for this data size. If the list were large, the filter would belong in the SQL
  query. Say which you chose and why.

</details>

## Common Mistakes

- Changing code before running it, so you cannot tell your change from existing behaviour.
- "Fixing" odd behaviour you found on the way, without asking the person who owns the requirement.
- Accepting an agent's map of the code without opening the files.
- Making a new parameter required, which breaks every existing caller.

## Self-Check

- [ ] I can draw the path of one feature from the screen to the database.
- [ ] I can write a test that records current behaviour, including behaviour I think is wrong.
- [ ] I can explain why a change is compatible for each layer it touches.
- [ ] I can name the moments when I should stop and ask.

## References

- [AI Era Coding Guidelines](../../standards/general/ai-era-coding-guidelines.md): delegation levels and the Red Zone
- [REST API Best Practices](../../standards/general/rest-api-best-practices.md): versioning and error format
- [Git Workflow](../../standards/git/git-workflow.md): branches and pull requests
- [Module 09: Testing, Debugging and Verification](./09-testing-debugging-and-verification.md)

**Next:** [Module 07: Clean Code](./README.md#pilot-draft) (outline only during the pilot)
