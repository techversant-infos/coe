# Quality Engineering

This section contains QA and test automation learning paths.

The first priority is the Playwright automation path because it gives manual testers a practical route into automation engineering.

## Current Status and Rating

| Area | Current state | Rating |
|---|---|---|
| Manual testing fundamentals | Baseline now defined; needs pilot exercises and mentor examples | 6/10 |
| Playwright automation | Strongest area; split tracks for manual-to-automation and senior automation are ready for pilot review | 8/10 |
| Automation strategy | Good starter guidance; needs project examples, metrics templates, and quality gate examples | 7/10 |
| API, accessibility, performance | Covered in automation path, but still needs deeper standalone references for advanced QA engineers | 6/10 |
| AI-assisted testing | Planned and linked, but still TODO | 4/10 |

**Overall rating:** 7/10 draft. The section is useful for a pilot batch, especially for Playwright automation, but it is not yet a complete QA academy. The biggest missing pieces are deeper manual testing practice, quality metrics, contract testing, visual regression, mobile/device testing, and AI-assisted testing examples.

## Paths

| Area | Path | Status |
|---|---|---|
| Manual testing | [Manual Testing](./manual-testing/README.md) | Baseline draft |
| Automation | [Playwright Automation](./automation/playwright/README.md) | Pilot-ready draft |
| Strategy | [Automation Strategy](./strategy/automation-strategy.md) | Draft |
| Assessment | [QA Capstone Rubric](./capstone-qa-rubric.md) | Draft |

## Guidance Layers

- [Learning Levels](../learning-levels/) - understand Foundation / Practitioner / Advanced / Expert
- [Career Progression](../career-progression/transition-overview.md) - see your upgrade path
- [Developer Excellence Curriculum](../00-engineering-foundations/dev-excellence/curriculum.md) - shared engineering discipline, testing fundamentals, and code review
- [AI Assisted Testing](../06-ai-engineering/ai-assisted-testing/README.md) - planned AI support path for QA work

## Recommended Order

1. Manual testing fundamentals, if needed
2. [Manual Tester to Automation Engineer](./automation/playwright/manual-to-automation.md)
3. [Automation Engineer to Senior Automation Engineer](./automation/playwright/senior-automation.md)
4. [Automation Strategy](./strategy/automation-strategy.md)

## Coverage Map

| Topic | Current coverage | Recommended next step |
|---|---|---|
| Test case design | Manual testing baseline | Add project-specific examples from active products |
| Exploratory testing | Manual testing baseline | Add session-charter examples and defect notes |
| Bug reporting | Manual testing baseline | Add one internal sample bug report |
| UI automation | Playwright path | Pilot with one real app and collect feedback |
| API automation | Playwright path and REST API standards | Add contract testing guidance if teams adopt Pact or schema checks |
| Accessibility testing | Senior automation path | Add keyboard navigation checklist and axe-core example |
| Performance testing | Senior automation path | Add k6/Lighthouse split once tooling is standardized |
| Visual regression | Mentioned in gap analysis | Add a focused Playwright `toHaveScreenshot()` topic if product teams need it |
| Mobile/device testing | Covered lightly | Link to mobile testing path when available |
| Quality metrics | Strategy draft | Add dashboard template after pilot |
| AI-assisted testing | TODO path | Add prompt examples and review guardrails |

## Useful Tutorials and References

Prefer official documentation first, then use videos/courses to reinforce practice.

| Topic | Resource |
|---|---|
| Playwright official docs | [Playwright Getting Started](https://playwright.dev/docs/intro), [Locators](https://playwright.dev/docs/locators), [Trace Viewer](https://playwright.dev/docs/trace-viewer), [API Testing](https://playwright.dev/docs/api-testing), [CI](https://playwright.dev/docs/ci) |
| Playwright videos | [Playwright YouTube channel](https://www.youtube.com/@Playwrightdev), [Playwright learn videos](https://playwright.dev/docs/intro#learn) |
| Automation courses | [Test Automation University](https://testautomationu.applitools.com/) |
| Testing community | [Ministry of Testing YouTube](https://www.youtube.com/@MinistryofTesting), [Ministry of Testing](https://www.ministryoftesting.com/) |
| Web accessibility | [W3C WAI Tutorials](https://www.w3.org/WAI/tutorials/), [Deque axe-core Playwright](https://github.com/dequelabs/axe-core-npm/tree/develop/packages/playwright) |
| Performance basics | [web.dev Core Web Vitals](https://web.dev/vitals/), [Lighthouse docs](https://developer.chrome.com/docs/lighthouse/overview) |
| API quality | [REST API Best Practices](../../general/rest-api-best-practices.md), [Google Testing Blog: Test Pyramid](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html) |
