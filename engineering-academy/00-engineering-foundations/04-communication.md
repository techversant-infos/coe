# Engineering Communication

**Level:** Foundation
**Next:** [Developer Excellence Curriculum](./05-dev-excellence/01-curriculum.md)

Communication is part of engineering quality. A technically correct change can still fail if the intent, risk, rollout, or handoff is unclear.

## Minimum Bar

- Write PR descriptions that explain what changed, why it changed, and how it was verified.
- Include screenshots, logs, or traces when they help reviewers understand behavior.
- Ask review questions instead of issuing commands when discussing trade-offs.
- Document important design decisions with an ADR or short architecture note.
- Make blockers visible early with the current state, attempted fixes, and the decision needed.
- Use concrete dates, owners, links, and next actions in status updates.

## Templates

### PR Summary

```text
## Summary
## Why
## Verification
## Risks / Rollback
## Reviewer Notes
```

### Blocker Update

```text
Current state:
What I tried:
What I learned:
Decision needed:
Owner:
Needed by:
```

### Handoff Note

```text
Context:
Files / links:
How to verify:
Known risks:
Next action:
```

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

## Useful References

- [Google Technical Writing Courses](https://developers.google.com/tech-writing)
- [ADR GitHub organization](https://adr.github.io/)
