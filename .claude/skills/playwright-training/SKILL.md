# Playwright Training

Comprehensive curriculum design for Playwright test automation. Bridges JavaScript fundamentals to production-ready automated testing.

## When to Use This Skill

Use this skill when:
- Teaching Playwright test automation
- Creating end-to-end testing curriculum
- Designing Playwright exercises and assessments
- Planning test automation learning paths

## Learning Path Structure

### Prerequisites
- JavaScript basics (variables, functions, arrays, objects)
- Basic understanding of HTML/CSS
- Familiarity with command line

### Phase 1: Playwright Foundations (2-3 weeks)
**Topics:**
- Introduction to Playwright
- Installation and setup
- Writing your first test
- Locators and selectors
- Basic assertions

**Learning Outcomes:**
- Set up Playwright in a project
- Write simple E2E tests
- Use locators to find elements
- Verify page state with assertions

### Phase 2: Test Design Patterns (3-4 weeks)
**Topics:**
- Page Object Model
- Test fixtures and hooks
- Parallel execution
- Handling waits and timeouts
- Test configuration

**Learning Outcomes:**
- Structure tests using best practices
- Use fixtures for test setup/teardown
- Configure test execution
- Handle timing issues

### Phase 3: Advanced Features (3-4 weeks)
**Topics:**
- Network mocking and interception
- Visual testing
- Trace viewer for debugging
- Cross-browser testing
- Mobile emulation

**Learning Outcomes:**
- Mock APIs and network requests
- Debug tests using traces
- Run tests across browsers and devices

### Phase 4: CI/CD Integration (2-3 weeks)
**Topics:**
- Running tests in CI
- Reporting and artifacts
- Test flakiness management
- Performance testing
- Scale considerations

**Learning Outcomes:**
- Integrate Playwright into CI pipelines
- Generate and analyze test reports
- Reduce flaky tests

### Phase 5: Production Practices (3-4 weeks)
**Topics:**
- Component testing
- API testing with Playwright
- Authentication workflows
- Data management
- Test organization strategies

**Learning Outcomes:**
- Test components in isolation
- Write API tests alongside E2E
- Manage test data effectively
- Organize large test suites

## Exercise Design Principles

### Progressive Complexity
1. **API exercises**: Focus on specific Playwright APIs
2. **Integration exercises**: Combine multiple concepts
3. **Real-world exercises**: Test actual applications
4. **Open-ended challenges**: Design tests for specifications

### Exercise Types
- **API practice**: Use specific locators, assertions, or features
- **Bug fixing**: Fix intentionally broken tests
- **Test creation**: Write tests from requirements
- **Refactoring**: Improve existing test code

### Exercise Structure
```markdown
## Exercise: [Title]

**Objective:** What Playwright concept is being practiced

**Prerequisites:** Required knowledge

**Instructions:**
1. Step-by-step guidance

**Expected Outcome:** What success looks like

**Hints:** [Spoiler sections]

**Solution:** [Hidden solution with explanation]
```

## Assessment Guidelines

### Skill Assessments
- Practical Playwright API usage
- Test writing from requirements
- Debugging broken tests
- Code review exercises

### Project Assessments
- Complete test suite for a web application
- CI/CD pipeline integration
- Documentation and test report

### Assessment Rubric Dimensions
1. **Test Coverage** (25%): Appropriate test scenarios covered
2. **Code Quality** (25%): Follows best practices and patterns
3. **Reliability** (25%): Tests are stable and non-flaky
4. **Maintainability** (25%): Easy to update and extend

## Resources

- References `.claude/templates/lesson-template.md` for lesson structure
- References `.claude/templates/exercise-template.md` for exercise format
- Follows `.claude/rules/automation-engineering-standards.md`