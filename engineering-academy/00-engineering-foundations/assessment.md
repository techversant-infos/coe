# Foundations Assessment

**Status:** Draft · **Owner:** TBD · **Last updated:** 2026-10-29 · **Next review:** 2027-01-29

> Pilot draft. Scores, thresholds and timings are provisional until the pilot confirms them.

## What a Pass Means

A learner who passes can **safely deliver a small change to an existing application, using approved AI tools, with
appropriate supervision**.

This is a foundations qualification. It does not certify independent full-stack expertise.

## Who Takes It and When

| Route | When |
|-------|------|
| Freshers | After modules 01–14 and both checkpoints |
| Experienced staff | First, before any module. Rows below the minimum point to the modules to study. Then repeat only those rows on a different task variant. |

Each attempt uses a task variant you have not seen before. All variants are equivalent and use this rubric.

## Checkpoints

Two feedback checkpoints come before the final assessment. They are not pass or fail.

| Checkpoint | After | Task | Feedback from |
|------------|-------|------|---------------|
| 1 | Module 06 | Map one feature of the training app and make a small compatible change | A tech lead, within two working days |
| 2 | Module 10 | Diagnose a failure in the training app and fix it with a regression test | A tech lead, within two working days |

Each checkpoint leaves time to close the gaps it finds before you move on.

## The Task

You work on your own snapshot of the training application. Approved AI tools are allowed throughout.

1. **Clarify.** You receive a short, unclear request. Ask questions, then record the intent and acceptance criteria
   in one issue.
2. **Change.** Implement the request in the existing code. Keep existing behaviour and callers working.
3. **Verify.** Add tests. Show that each new test fails without your change.
4. **Review.** Review a prepared AI-generated pull request and report the issues you find.
5. **Diagnose.** A production-style signal (a log entry or alert) reports a failure. Investigate it and fix the root
   cause.
6. **Ship.** Deploy to the training environment, confirm it works, then roll back and confirm the rollback.
7. **Explain.** Walk an assessor through your work and answer questions.

### Keep the trail traceable

Your issue and pull request must let someone follow the change from request to rollback:

```text
request -> intent and acceptance criteria -> agent context -> commits -> test evidence
        -> review notes -> deployment -> post-release check -> rollback
```

One issue and one pull request are enough. Separate intent, specification or plan files are optional. Add them only if
they help.

## Rubric

Each row is scored 0–3:

| Score | Meaning |
|-------|---------|
| 0 | Not shown |
| 1 | Shown only with prompting or help |
| 2 | Shown independently; minor gaps |
| 3 | Shown independently; explains trade-offs and anticipates problems |

| Row | What the assessor looks for | Modules |
|-----|-----------------------------|---------|
| 1. Clarify | Questions that remove the real ambiguity; acceptance criteria someone else could test | 02, 14 |
| 2. Compatible change | A small change in unfamiliar code; existing callers, data and behaviour keep working | 06, 07, 08, 10 |
| 3. Test and verify | Records current behaviour before changing it; tests that fail without the change; does not rely on the agent's own checks | 06, 09 |
| 4. Debug | Starts from the production signal, reproduces the failure, finds the root cause, adds a regression test | 09, 13 |
| 5. Review | Finds the material issues in the AI-generated pull request, including security issues; explains each one | 11, 12 |
| 6. Ship and roll back | Deploys, checks the health signals, rolls back cleanly, says what to watch after release | 03, 13 |
| 7. AI delegation | Chooses what to delegate, gives the agent the acceptance criteria as context, runs it with permissions suited to the task, explains what was accepted or rejected | 04, 05 |
| 8. Explain and trace | The issue and pull request tell the whole story; decisions and trade-offs are explained; help is sought at the right moments | All |

## Passing Rules

You pass when all three conditions hold:

1. Every **safety criterion** below is met.
2. Every rubric row scores **at least 2**. A strong score in one row cannot make up for a weak one in another.
3. The total is **at least 18 of 24** (provisional).

Missing a minor planted issue in the review lowers the Review score. Missing a material one, such as a security flaw,
keeps the row below 2.

## Safety Criteria

Breaking any of these fails the attempt, whatever the scores:

| # | Criterion |
|---|-----------|
| S1 | No secrets, credentials or customer data in code, prompts, logs or commits |
| S2 | No Red Zone work handed to an AI tool ([AI Era Coding Guidelines, section 2.2](../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only)) |
| S3 | No change merged without tests and an independent review. An agent checking its own work does not count. |
| S4 | The agent runs with permissions limited to the task. An instruction file (`AGENTS.md`, `CLAUDE.md`) guides an agent but does not enforce anything, so tool permissions, branch protection and CI must do the enforcing. |
| S5 | No fix reaches the deployed environment without a person deciding it should. Automated fixes need explicitly bounded authority. |
| S6 | Rollback demonstrated and confirmed |

### Prohibited action or safe recognition?

Recognising a risk and reporting it is the behaviour this course wants. Only the prohibited action fails.

| Prohibited (fails the attempt) | Safe recognition (scores well) |
|--------------------------------|--------------------------------|
| Asking the agent to change login or permission code | Noticing the change touches login code, stopping, and telling the lead why |
| Pasting real customer data or a secret into an AI tool | Using the synthetic data, and reporting a secret found in the code |
| Merging an AI fix you cannot explain | Saying "I don't understand this part yet" and asking before merging |
| Giving the agent unrestricted shell or deploy access to save time | Granting only the commands the task needs, and saying why |
| Letting an agent push a fix straight to the environment because an alert fired | Using the alert to start an investigation, then deciding on the fix |

## How It Is Scored

- A trained tech lead scores each attempt during and after the live walkthrough.
- During the pilot, two assessors score every attempt independently, then compare.
- The CoE samples scored attempts to keep scoring consistent across assessors.
- Assessors use a private key for each task variant. Learners never see it, and it is not in this repository.

## Related

- [Module 06: Working with Existing Systems](./06-working-with-existing-systems.md)
- [Module 09: Testing, Debugging and Verification](./09-testing-debugging-and-verification.md)
- [Facilitator Guide](./facilitator-guide.md)
