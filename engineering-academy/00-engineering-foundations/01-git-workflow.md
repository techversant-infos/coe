# Git Workflow

**Level:** Foundation
**Next:** [AI Usage](./02-ai-usage.md)

The source of truth is [Techversant Git Workflow](../../git/Techversant_Git_Workflow.md).

Use it for:

- Branch naming
- Conventional commits
- PR process
- Promotion flow from `dev` to `staging` to `main`
- Rollback guidance
- Release tagging

## Minimum Bar

- Create a branch from the correct base branch.
- Use conventional commit messages.
- Open a PR with a clear summary and test notes.
- Rebase or resolve conflicts without overwriting teammate work.
- Never force-push to shared branches unless the repo owner explicitly approves it.

## Common Mistakes To Avoid

- Branching from the wrong base branch.
- Mixing unrelated work into one PR.
- Writing commit messages that describe effort instead of outcome.
- Resolving conflicts by blindly accepting one side.
- Merging without test notes or rollback context.

## Practice Task

Take one recent merged PR and audit it against the workflow:

```text
Branch name:
Commit format:
PR summary:
Verification notes:
Rollback notes:
Reviewer feedback resolved:
```

Mark any missing item as a follow-up improvement, not as blame.

## Useful References

- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [GitHub pull request documentation](https://docs.github.com/en/pull-requests)
- [Pro Git book](https://git-scm.com/book/en/v2)
