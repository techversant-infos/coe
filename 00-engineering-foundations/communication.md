# Engineering Communication

Communication is part of engineering quality. A technically correct change can still fail if the intent, risk, rollout, or handoff is unclear.

## Minimum Bar

- Write PR descriptions that explain what changed, why it changed, and how it was verified.
- Include screenshots, logs, or traces when they help reviewers understand behavior.
- Ask review questions instead of issuing commands when discussing trade-offs.
- Document important design decisions with an ADR or short architecture note.
- Make blockers visible early with the current state, attempted fixes, and the decision needed.

## Practice Task

Take a recent PR and rewrite its description using this structure:

```text
## Summary
## Why
## Verification
## Risks / Rollback
## Reviewer Notes
```

Ask a teammate whether they could review the PR without extra context.