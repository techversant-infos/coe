# Foundations Facilitator Guide

**Status:** Draft · **Owner:** TBD · **Last updated:** 2026-10-29 · **Next review:** 2027-01-29

> For the people who run the Foundations pilot and score assessments. Learners do not need this guide.

## What the Pilot Tests

The pilot checks whether the course design works before anyone writes the remaining twelve modules. It is built around
one realistic change and one failure investigation in the training application.

| In the pilot | Status |
|--------------|--------|
| [Module 06: Working with Existing Systems](./06-working-with-existing-systems.md) | Full draft |
| [Module 09: Testing, Debugging and Verification](./09-testing-debugging-and-verification.md) | Full draft |
| Checkpoint 1 | Short task after module 06 |
| [Assessment](./assessment.md) | Full task on a fresh variant |
| Modules 01–05, 07, 08 | A 30-minute briefing from the facilitator, using the outlines in the [README](./README.md#pilot-draft) |

## Cohort and Roles

- **Learners:** 4–6, mixing freshers and experienced engineers. All should work in TypeScript, the training app's
  stack, so the language does not distract from the skills being assessed.
- **Facilitator:** runs the briefings, answers questions, records timings and where learners struggle.
- **Assessors:** at least two trained tech leads. During the pilot, both score every attempt independently.
- **CoE reviewer:** joins the calibration session and reviews the pilot results.

## Before the Pilot

1. **Collect the baseline.** For each participant, take three recent pull requests and one debugging task from real
   work. Score them on the transfer measures in [After the Pilot](#after-the-pilot). Without this baseline, transfer
   cannot be measured.
2. **Prepare the learner snapshots.** Each learner gets a clean repository for the variant assigned to them, generated
   from the assessor repository with no history. Branches are not a security boundary: anyone who can read a
   repository can fetch all its branches.
3. **Run the leak check.** Search each snapshot, including its full history, for variant names, defect descriptions
   and key terms from the assessor key. Record the result.
4. **Calibrate the assessors.** Score one sample attempt together, discuss each disagreement, then agree what each
   score means for each row.

## Running It

- **Pairs help.** Pair learners for module exercises, not for checkpoints or the assessment.
- **Use the real code.** Teach from the training application, not toy examples. Every exercise should explore or
  improve it.
- **Review the work, not only the result.** Feedback on a checkpoint covers how the learner got there: their map,
  their tests, what they accepted from the agent and why.
- **Record timings per stage:** understand, clarify, change, verify, review, diagnose, ship, explain. The time budget
  depends on these numbers.
- **Record struggles.** Note where learners got stuck, which instructions they misread and which questions they asked.
  These notes drive the revisions.

## Scoring

1. Each assessor scores independently against the [rubric](./assessment.md#rubric) during and after the walkthrough.
2. Check the [safety criteria](./assessment.md#safety-criteria) first. A prohibited action fails the attempt.
   Recognising a risk and reporting it scores well.
3. Compare scores and record every row where the assessors differ by more than one point, with the reason.
4. Give the learner feedback on each row below 3, with one concrete example from their work.

## Exit Criteria

The pilot passes when all of these are true:

| Criterion | Measure |
|-----------|---------|
| Learners can complete the work | At least 80% finish the module exercises and the assessment without the facilitator taking over |
| Timings fit | The median time for each stage is within 25% of the estimate |
| Assessors broadly agree | Scores are within one point on at least 80% of rows, and the assessors agree on every safety criterion |
| No assessment material leaks | The leak check finds nothing in any snapshot, and no learner reports seeing assessment material |
| Learners explain their decisions | Every passing learner explains, unprompted, at least one thing they rejected from AI output |

If a criterion fails, revise the course and run a second pilot before writing the remaining modules.

## After the Pilot

1. **Revise** modules 06 and 09, the rubric and the time budget based on the timings, struggles and assessor
   disagreements.
2. **Update the repository rules.** Rewrite `.claude/rules/` and the `.claude/commands/` that assume the old phase
   layout, so they fit the flat Foundations structure. Record the reason for each change.
3. **Check transfer** 6–8 weeks after the pilot. Score each participant's next three pull requests and one debugging
   task on the same measures as the baseline:
   - requirements and acceptance criteria are clearer;
   - tests cover the change and fail without it;
   - fewer review rounds are needed for correctness issues;
   - AI use is disclosed, verified and stays out of the Red Zone.
4. **Write the remaining modules** only once the pilot passes.

## Related

- [Foundations README](./README.md)
- [Assessment](./assessment.md)
- [AI Era Coding Guidelines](../../standards/general/ai-era-coding-guidelines.md)
