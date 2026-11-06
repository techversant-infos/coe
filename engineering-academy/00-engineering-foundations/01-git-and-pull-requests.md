# 01. Git and Pull Requests

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Every change at Techversant moves through a branch and a reviewed pull request. Following one workflow means anyone
can review, release or roll back your work. Back to the [roadmap](./README.md).

## Branches and commits

A branch keeps your change separate until it is reviewed. A good commit message tells the next reader what changed
and why, without opening the diff.

**What to learn:**

- Branching from `main` with the Techversant naming pattern, such as `feature/fix-AGL-881-rounding`
- Writing Conventional Commits: a type such as `feat`, `fix` or `refactor`, an optional scope, and a short summary
  of the outcome, not the effort
- Keeping branches small and short-lived, and each commit focused on one change

**Resources:**

- [Branching model](../../standards/git/git-workflow.md#-branching-model) and
  [commit standard](../../standards/git/git-workflow.md#-commit-standard), in the Techversant Git workflow
- [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)
- [Pro Git](https://git-scm.com/book/en/v2), the free Git book

**Level:** Foundation · Core

## Pull requests

A pull request (PR) asks teammates to review your change before it merges. A clear PR is reviewed faster and
catches more problems.

**What to learn:**

- Opening a PR with a summary, the reason for the change, how you verified it and any risks
- Keeping one PR to one purpose, and small enough to review in one sitting
- Responding to review comments, and resolving each one with a change or an explanation
- Where PRs merge: on product projects, into `dev` first, then promoted to staging and `main`

**Resources:**

- [Developer workflow](../../standards/git/git-workflow.md#-developer-workflow-multi-stage-promotion-model), in the
  Techversant Git workflow
- [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests),
  GitHub documentation

**Level:** Foundation · Core

## Resolving conflicts

When two people change the same lines, Git asks you to choose. Resolving conflicts carefully keeps your teammates'
work safe.

**What to learn:**

- Rebasing on `origin/main` before your first push, and merging `main` into your branch after that, because
  Techversant never rebases a branch that has been pushed
- Reading a conflict, and combining both changes instead of accepting one side without thinking
- Never force-pushing to a shared branch

**Resources:**

- [Rebase safety guidelines](../../standards/git/git-workflow.md#-rebase-safety-guidelines), in the Techversant Git
  workflow
- [Basic merge conflicts](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging), in Pro Git

**Level:** Foundation · Core

## Releases and rollback

Code reaches production through environments, and every release is tagged so it can be rolled back.

**What to learn:**

- The promotion flow: development, then staging, then production
- Tagging releases, and why tags are never changed
- Rolling back with a tag instead of editing production by hand

**Resources:**

- [Promotion flow](../../standards/git/git-workflow.md#-promotion-flow) and
  [rollback](../../standards/git/git-workflow.md#-rollback--database-script-management), in the Techversant Git
  workflow

**Level:** Foundation · Core

## Cleaning up local history

Before you open a PR, you can tidy your own commits: combine small fixes and reword unclear messages. This is safe
only on a branch nobody else uses.

**What to learn:**

- Amending the last commit, and interactive rebase on your own branch
- Recovering a lost commit with `git reflog`

**Resources:** [Rewriting history](https://git-scm.com/book/en/v2/Git-Tools-Rewriting-History), in Pro Git

**Level:** Practitioner · Optional

## Project: Ship Your First Change

**Brief:** Set up the [practice app](./practice-app.md) and record the baseline test results. Then make one small
improvement, such as a clearer error message or a missing validation, and ship it through a branch and a reviewed
PR. Use a practice ticket ID such as `FND-1` in place of a Jira ID.

**Size:** 1–2 days

**Verification**, checked by a reviewer:

- [ ] The app runs locally, and the baseline API test results are recorded in the repository
- [ ] The branch name follows the Techversant pattern, such as `feature/fix-FND-1-article-error-message`
- [ ] Every commit message follows Conventional Commits and describes the outcome
- [ ] The PR description has a summary, the reason, how it was verified and any risks
- [ ] The PR contains only the one change, and the API tests still pass
- [ ] Every review comment is resolved with a change or a reply
- [ ] The reviewer pushes a conflicting commit to `main`, and you resolve the conflict by merging `main` into your
  branch, keeping both changes

Next: [02. Working with AI Tools](./02-working-with-ai-tools.md)
