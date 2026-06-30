# Academy Migration TODO

This file tracks the migration from standalone learning paths to the Techversant Engineering Academy structure.

## Priority Order

1. Rearrange existing learning paths into the academy structure.
2. Correct internal cross-links.
3. Verify current state and record gaps.
4. Complete the QA path first.
5. Complete remaining academy TODOs in the right order.

## Current Status

| Area | Status | Notes |
|---|---|---|
| Academy root navigation | Complete | Root README links to all disciplines and guidance layers |
| Engineering foundations | Complete | Dev Excellence + foundation one-pagers migrated |
| Software engineering | In progress | React and Next.js pilot-ready; backend/mobile TODO |
| Quality engineering | In progress | Playwright split-track pilot-ready; manual testing TODO |
| AI engineering | Skeleton | Placeholder index files only; full curricula needed |
| Learning levels | Complete | All four levels defined; now connected to content |
| Career progression | Complete | 4 files: transition-overview, junior-to-senior, senior-to-team-lead, lead-to-architect |

## Polish Phase (v1.0) — Done

- Added **Level** labels (Foundation/Practitioner/Advanced/Expert) to all content files
- Added **Next Level** links in content file headers
- Added **Guidance Layers** section to all discipline READMEs (00–06)
- All disciplines now reference Learning Levels and Career Progression

## Known Gaps

- Backend learning paths need academy-native structure.
- Mobile learning paths need dedicated curriculum beyond stack translation.
- Manual testing path needs a proper foundation curriculum.
- AI-assisted development/testing/prompt engineering paths need full curricula.
- Career progression guidance should be added after the structure settles.
- Legacy `learning-paths/` folders remain as compatibility copies until existing links are migrated.

## QA Path Next Steps

1. Review [Manual Tester to Automation Engineer](./02-quality-engineering/automation/playwright/manual-to-automation.md).
2. Review [Automation Engineer to Senior Automation Engineer](./02-quality-engineering/automation/playwright/senior-automation.md).
3. Finish [Manual Testing](./02-quality-engineering/manual-testing/README.md) as a proper foundation path.
4. Add a QA capstone rubric and manager sign-off checklist.
5. Add topic-specific learning links only where they support a precise skill.
