# Facilitator Guide

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

This guide is for the senior engineer or lead who runs the [Engineering Foundations roadmap](./README.md) for a
cohort. Learners do not need it. The eight-week plan is in the roadmap's
[How to Use It](./README.md#how-to-use-it) section.

## Before the First Session

- Keep the cohort small, around four to six engineers, ideally from more than one team and stack.
- Pair the engineers up for the whole cohort. Discussing a topic with a partner is where most of the learning
  happens.
- Make sure everyone has the [practice app](./practice-app.md) running, its baseline tests recorded, and a practice
  repository where they can open pull requests.
- Agree who reviews each project. You can share reviews with other senior engineers, but one person should own each
  learner's sign-off.

## Running a Session

- **One session, one stage, one project.** Do not combine stages, apart from the pairs in the eight-week plan.
- **Start from real code.** Open the practice app and show the problem in its code before naming the principle.
- **Change code live.** Refactor in front of the group and explain each decision as you make it, including the
  options you rejected.
- **Show before and after.** Every topic has a "before" (the problem) and an "after" (the fix). Over time, learners
  start to spot the "before" in their own pull requests.
- **Connect it to real work.** Where you can, tell a story from a Techversant project: a bug, a review discussion
  or a slow change this habit would have prevented. Leave out client names and anything confidential.

## Reviewing Projects

- The review is where most of the teaching happens. Give each project a proper code review, using the
  [review checklist](./09-code-review.md#the-review-checklist).
- Check every item in the project's verification checklist. If an item is not met, say what is missing and let the
  learner fix it; do not sign off a partial project.
- Model the feedback style from stage 09: objective comments, questions rather than instructions, and labels for
  must fix, should consider and nit.

## Watch For

- **AI doing the thinking.** If a learner cannot explain a line they committed, ask them to rework it. The rules are
  in [stage 02](./02-working-with-ai-tools.md).
- **Red Zone work.** The bookmark ownership check in stages 06–08 is authorization, so it is Red Zone work: make
  sure it is written by hand and reviewed by a senior engineer. No project needs authentication or encryption code.
  If a learner starts writing some, stop them and point them to a senior engineer.
- **Projects growing too large.** Keep each project to its stated size. A smaller, finished project teaches more than
  a large, unfinished one.

## After the Cohort

- Run the capstone for each learner, as described in the [roadmap](./README.md#capstone).
- Write one page on what worked, what did not and what you would change, and send it to the CoE Team as a proposed
  change to this roadmap, following [Contributing to CoE Standards](../../CONTRIBUTING.md).
