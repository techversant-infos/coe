# 09. Testing, Debugging and Verification

**Status:** Draft · **Owner:** TBD · **Last updated:** 2026-10-29 · **Next review:** 2027-01-29

**Level:** Foundation · **Time:** about 2.5 hours (50 minutes reading, 100 minutes practice) · **Pilot draft**

## Learning Objectives

By the end of this module, you will be able to:

- [ ] Choose the right level of test for a change, and write it in Arrange-Act-Assert form
- [ ] Prove that a test can fail, including tests an AI agent wrote
- [ ] Investigate a failure from a production signal: reproduce it, read the evidence and find the root cause
- [ ] Tell a fix for the root cause apart from a fix that hides the symptom
- [ ] Treat an AI-suggested fix as a hypothesis, and verify it independently before it ships

## Why This Matters

Tests and debugging are how you know a change works, whoever wrote the code. With AI agents writing more of the code,
verification becomes a larger share of your job, not a smaller one.

An agent can write a change, write tests for it and report that everything passes, all in one step. If the tests
check the wrong thing, nothing in that loop notices. Your independent check is what makes the result trustworthy.

## Part 1: Tests That Protect You

### Pick the level

| Level | Checks | Training app example | Speed |
|-------|--------|----------------------|-------|
| Unit | One function or module on its own | `calculateDueDate` returns Monday 09:00 for a Saturday due date | Milliseconds |
| API (integration) | A route, the service and the database together | `GET /api/requests?assignee=7` returns only that person's open requests | Seconds |
| End-to-end | A user flow through the real UI | A support lead filters the list and sees the right rows | Tens of seconds |

Most of your tests belong at the unit and API levels. Keep end-to-end tests for the few flows that must never break.

### Write it in three parts

Arrange the inputs, act once, then assert the result:

```typescript
// api/test/due-date.test.ts
import { expect, it } from "vitest";
import { calculateDueDate } from "../src/requests/due-date.ts";

it("gives a low-priority request raised on Monday a Thursday due date", () => {
  // Arrange: Monday 10:00 UTC
  const created = new Date("2026-11-09T10:00:00Z");

  // Act
  const due = calculateDueDate("low", created);

  // Assert: 72 hours later
  expect(due.toISOString()).toBe("2026-11-12T10:00:00.000Z");
});
```

### Prove the test can fail

A test that cannot fail protects nothing. After you write a test, break the code on purpose and watch the test fail.
For example, change `low: 72` to `low: 48`, run the test, see it fail, then undo the change.

Do this for agent-written tests too. Watch for these patterns:

- **Copied output:** the test asserts whatever the code returns today, with no reasoning about what is correct. That
  suits a test that records existing behaviour, not a test for new behaviour.
- **Mocked subject:** the test replaces the very function it claims to test, so it only checks the mock.
- **Weakened test:** a failing test was edited or deleted until it passed. Always read test changes in a diff.

## Part 2: Debugging From a Signal

A failure usually reaches you as a signal: an alert, an error log, a failed job or a user report. The signal starts an
investigation. It does not decide the fix.

Work through the same loop every time:

1. **Reproduce.** Make the failure happen on demand, locally or in the training environment. A failure you cannot
   reproduce is one you cannot confirm you fixed.
2. **Read the evidence.** Logs, stack traces, recent deployments and the data involved.
3. **Form one hypothesis.** "The job fails when a request has no assignee" is testable. "Something is wrong with the
   job" is not.
4. **Narrow it down.** Test the hypothesis with the smallest experiment you can.
5. **Fix the root cause.** Then add a test that fails without your fix.
6. **Watch after release.** Confirm the signal stops.

### Read the log and the stack trace

The training app writes structured logs, one JSON object per line:

```json
{"level":"error","time":"2026-11-10T02:00:01.204Z","job":"sla-check","err":{"type":"TypeError","message":"Cannot read properties of null (reading 'email')","stack":"TypeError: Cannot read properties of null (reading 'email')\n    at runSlaCheck (/app/api/src/jobs/sla-check.ts:6:43)"},"msg":"sla-check failed"}
```

Read it in this order:

1. **`time` and `job`:** when it happened and which part of the system failed.
2. **`err.message`:** the code tried to read `email` from something that was `null`.
3. **The first stack frame:** `sla-check.ts`, line 6. Start reading the code there.

### Narrow it down with history

If the job worked in an earlier release, `git bisect` finds the commit that broke it by halving the range each step:

```bash
git bisect start
git bisect bad                 # the current commit fails
git bisect good v1.3.0         # the last release where the job ran cleanly
# Git checks out a commit in the middle. Run your reproduction, then mark the result:
npm run job:sla-check
git bisect good                # or: git bisect bad
# Repeat until Git names the first bad commit, then return to where you started:
git bisect reset
```

### Root cause or symptom?

| Symptom fix | Root-cause fix |
|-------------|----------------|
| Wraps the failing line in `try`/`catch` and logs a warning | Finds why the value is `null` and handles that case on purpose |
| Skips the records that crash the job | Decides what should happen to those records, with the requirement owner |
| Raises a timeout until the error goes away | Finds what got slower |

A symptom fix makes the signal disappear while the real problem continues out of sight.

### Across the stack

| Layer | Where the evidence is |
|-------|-----------------------|
| UI | The browser console and the network tab: the request sent and the response received |
| API | Structured logs, found by request ID; the status code and error body |
| Background job | The job's log, run history and retries |
| Data | Constraint errors, slow query logs, and the actual rows involved |

## Part 3: Verifying an AI-Suggested Fix

Agents are good at suggesting fixes quickly. Treat each suggestion as a hypothesis and check it before you accept it:

- **Does it explain the evidence?** It should account for the log, the stack trace and when the failure started.
- **Does it fix the cause or hide the symptom?** Use the table above.
- **Is there a failing test first?** Write the test, see it fail, then apply the fix and see it pass.
- **What else does it change?** Read the whole diff, not only the lines near the error.
- **Who reviews it?** A person other than the author reviews every change. An agent reviewing its own work does not
  count.

### Automated fixes need bounded authority

Some teams let agents act on production signals. Before an agent may fix anything without a person deciding first, its
authority must be written down and enforced: which systems, which kinds of change, which limits, and how a person
undoes it.

Enforcement lives in tool permissions, branch protection and CI. An instruction in `AGENTS.md` or `CLAUDE.md` guides
an agent, but nothing stops an agent from ignoring it. Without that written, enforced authority, a signal leads to an
investigation and a person decides on the fix.

## Exercise: The Overnight SLA Check

**Objective:** Investigate a failure from a production signal, reject a symptom fix and ship a root-cause fix with a
regression test.

**Prerequisites:** Module 06. The training application running locally.

**Signal:** Since release v1.4.0, the overnight job that emails people about overdue requests fails every night. The
log entry is the one shown in Part 2.

Here is the job as you find it:

```typescript
// api/src/jobs/sla-check.ts
import type { SlaCheckDeps } from "./types.ts";

export async function runSlaCheck(now: Date, deps: SlaCheckDeps): Promise<void> {
  const overdue = await deps.findOverdueRequests(now);
  for (const request of overdue) {
    await deps.sendEmail(request.assignee.email, `Request ${request.id} is overdue`);
  }
}
```

Your agent suggests this fix:

```typescript
for (const request of overdue) {
  if (!request.assignee) continue; // skip requests without an assignee
  await deps.sendEmail(request.assignee.email, `Request ${request.id} is overdue`);
}
```

**Instructions:**

1. Reproduce the failure locally with the seeded data. Write down the command you used.
2. Use the stack trace and `git bisect` to find the commit that introduced the failure.
3. Explain the root cause in two or three sentences in your issue.
4. Decide whether to accept the agent's fix. Write your reasoning in the pull request.
5. Write a regression test that fails on the current code. Then fix the root cause and make it pass.
6. Ask a reviewer to check the pull request before it merges.

**Expected outcome:** An issue with the root cause, a pull request with a failing-then-passing regression test, and a
written decision on the agent's fix.

<details>
<summary>Reveal a model solution</summary>

**Root cause.** Release v1.4.0 let the web form create requests without an assignee, so the `assignee` column became
nullable. The `OverdueRequest` type still says every request has an assignee, so the compiler never warned about
`request.assignee.email`. The first unassigned overdue request crashes the job, and no one after it is notified.

**The agent's fix hides the symptom.** The job stops crashing, but unassigned overdue requests are skipped. Those have
no owner, so they are the requests most likely to be forgotten. Reject the fix and say why.

**Start by correcting the type.** The type must match the data:

```typescript
// api/src/jobs/types.ts
export interface Assignee {
  id: number;
  email: string;
}

export interface OverdueRequest {
  id: number;
  title: string;
  // null since the web form started allowing unassigned requests
  assignee: Assignee | null;
}

export interface SlaCheckDeps {
  findOverdueRequests: (now: Date) => Promise<OverdueRequest[]>;
  sendEmail: (to: string, subject: string) => Promise<void>;
  teamLeadEmail: string;
}
```

With strict type checking on, the compiler now reports `'request.assignee' is possibly 'null'` at the old line. It
will report every other unsafe use too.

**Decide the behaviour with the owner.** The support policy in the training app says unassigned overdue requests go
to the support team lead. If you cannot find a rule like that, ask before you choose one.

**Write the regression test first:**

```typescript
// api/test/sla-check.test.ts
import { describe, expect, it } from "vitest";
import { runSlaCheck } from "../src/jobs/sla-check.ts";
import type { OverdueRequest } from "../src/jobs/types.ts";

describe("runSlaCheck", () => {
  it("sends the overdue notice to the team lead when a request has no assignee", async () => {
    // Arrange
    const unassigned: OverdueRequest = { id: 42, title: "Printer offline", assignee: null };
    const sentTo: string[] = [];
    const deps = {
      findOverdueRequests: async () => [unassigned],
      sendEmail: async (to: string) => {
        sentTo.push(to);
      },
      teamLeadEmail: "support-lead@example.test",
    };

    // Act
    await runSlaCheck(new Date("2026-11-10T02:00:00Z"), deps);

    // Assert
    expect(sentTo).toEqual(["support-lead@example.test"]);
  });
});
```

On the old code this test fails with the same `TypeError` as the log.

**Then fix the cause:**

```typescript
// api/src/jobs/sla-check.ts
import type { SlaCheckDeps } from "./types.ts";

export async function runSlaCheck(now: Date, deps: SlaCheckDeps): Promise<void> {
  const overdue = await deps.findOverdueRequests(now);
  for (const request of overdue) {
    // An unassigned request has no owner yet, so the team lead must hear about it
    const recipient = request.assignee === null ? deps.teamLeadEmail : request.assignee.email;
    await deps.sendEmail(recipient, `Request ${request.id} is overdue`);
  }
}
```

**After release,** check the next night's log for a clean run of `sla-check` and confirm the team lead received the
unassigned notices.

Do not log the recipient's email address to prove it worked. Email addresses are personal data. Log the request ID and
whether the notice went to the assignee or the team lead.

</details>

## Common Mistakes

- Fixing before reproducing, then being unable to show the fix worked.
- Accepting a fix because the error stopped, without checking what the change does to the data.
- Trusting an agent's "all tests pass" without running the tests and reading them.
- Logging personal data while debugging and leaving it in the code.

## Self-Check

- [ ] I can choose between a unit, API and end-to-end test for a change, and explain why.
- [ ] I can show that a test fails when the behaviour it protects breaks.
- [ ] I can walk from a log entry to the line of code and the commit that caused it.
- [ ] I can explain why a fix addresses the root cause, not the symptom.
- [ ] I can explain what limits must be written down and enforced before an agent may fix production issues on its
  own.

## References

- [AI Era Coding Guidelines](../../standards/general/ai-era-coding-guidelines.md): test ownership and debugging AI
  output
- [CoE Security Checklist](../../security/audit/security-audit-checklist.md): logging and personal data
- [Module 06: Working with Existing Systems](./06-working-with-existing-systems.md)

**Next:** [Module 10: APIs and Data Boundaries](./README.md#pilot-draft) (outline only during the pilot)
