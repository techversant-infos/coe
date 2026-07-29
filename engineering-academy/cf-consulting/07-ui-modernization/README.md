# Phase 7: UI/API Modernization

> Modernize the front end and APIs of ColdFusion applications without rewriting the back end.

---

## Pathway Metadata

| Field | Value |
|-------|-------|
| Pathway | Specialist Pathway |
| Best for | UI/API Specialist |
| Contribution level | Contributor → Lead |
| Take this when | You need to modernize a UI or expose CF functionality via APIs |
| Evidence of readiness | Completed UI or API modernization scope for an application |
| Next | [capstone/exercises/phase-7](../capstone/exercises/phase-7-ui.md) for practice |

---

## Overview

## Overview

Most legacy ColdFusion applications have outdated UIs. This phase covers practical approaches to modernizing the front end while keeping the CF back end — the most cost-effective modernization path.

## Learning Objectives

By the end of this phase, you will be able to:

- [ ] Assess UI modernization options for ColdFusion apps
- [ ] Implement Bootstrap for responsive design
- [ ] Build React/Vue components that call CF APIs
- [ ] Create CF REST APIs for front-end consumption
- [ ] Handle authentication between modern UI and CF back end
- [ ] Implement progressive enhancement patterns
- [ ] Ensure accessibility (WCAG) compliance
- [ ] Optimize front-end performance

## Prerequisites

- [Phase 1: ColdFusion Deep Expertise](../01-coldfusion-deep-expertise/)
- Basic understanding of modern JavaScript

## Topics

### 1. UI Modernization Strategies

**Option A: Bootstrap Refresh**
- Quick win for basic modernization
- Mobile responsiveness
- Component library
- Minimal changes to CF code

**Option B: React Integration**
- Modern SPA with CF back end
- API-first architecture
- Component reusability
- State management

**Option C: Vue Integration**
- Lighter alternative to React
- Progressive adoption
- Good CF integration stories
- Template syntax familiarity

**Option D: Next.js (Full Modernization)**
- Full rewrite with CF as API
- SSR/SSG capabilities
- Modern development experience
- When this makes sense

### 2. CF as API Backend

**REST API Development:**
```cfml
// Simple REST endpoint
component {

    remote function getUser(required numeric id) returnformat="json" {
        return userService.get(id);
    }

    remote function saveUser(required struct data) returnformat="json" {
        return userService.save(data);
    }

}
```

**Authentication:**
- JWT tokens
- Session management with API keys
- CORS configuration
- Rate limiting

**Error Handling:**
- Consistent error responses
- HTTP status codes
- Validation errors

### 3. Bootstrap Modernization

**Component Conversion:**
- Forms (cfinput → Bootstrap)
- Tables (cfgrid → DataTables)
- Navigation (custom → Bootstrap navbar)
- Modals (custom → Bootstrap modals)

**Responsive Design:**
- Grid system
- Breakpoints
- Mobile-first approach

### 4. React Integration

**Project Setup:**
- Create React App / Vite
- CFML API endpoints
- Build configuration

**Component Patterns:**
- Data fetching with fetch/axios
- Form handling
- State management
- Routing

**CF Integration:**
- API calls from React
- Authentication flow
- Error handling

### 5. Accessibility (A11Y)

- WCAG 2.1 requirements
- Semantic HTML
- ARIA attributes
- Keyboard navigation
- Screen reader testing
- Color contrast

### 6. Performance Optimization

- Lazy loading
- Code splitting
- Image optimization
- CDN usage
- Caching strategies

## Exercises

| Exercise | Focus | Expected Outcome |
|----------|-------|------------------|
| [Exercise 1: Bootstrap Refresh](./exercises/exercise-1.md) | Modernize a legacy form | Responsive Bootstrap form |
| [Exercise 2: CF REST API](./exercises/exercise-2.md) | Build API endpoints | Working REST API |
| [Exercise 3: React + CF](./exercises/exercise-3.md) | Connect React to CF API | Full CRUD SPA |
| [Exercise 4: Accessibility Audit](./exercises/exercise-4.md) | Fix accessibility issues | WCAG compliant interface |

## Assessment

Complete all exercises and pass the [phase assessment](./assessment.md) with 70% or higher.

## Resources

- [Bootstrap Documentation](https://getbootstrap.com/)
- [React Documentation](https://react.dev/)
- [Vue Documentation](https://vuejs.org/)
- [WCAG Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

## Time Estimate

| Activity | Hours |
|----------|-------|
| Lessons | 10 |
| Exercises | 8 |
| Assessment | 2 |
| **Total** | **20 hours** |

## Success Criteria

A developer completing this phase should be able to:

1. Recommend the right UI modernization approach for a given app
2. Build a CF REST API for front-end consumption
3. Integrate React or Vue with existing CF back end
4. Ensure accessibility compliance

## Next Phase

[Phase 8: Performance Engineering](../08-performance-engineering/) — Deep dive into ColdFusion performance optimization.
