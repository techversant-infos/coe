# Contributing to CoE Standards

Thank you for helping improve Techversant's engineering standards. This guide explains how to propose changes, update existing documents, and maintain quality across the repository.

---

## Types of Contributions

| Type | Description | Examples |
|------|-------------|----------|
| **New Standard** | Add a new technology stack or practice | Go coding standards, Flutter guidelines |
| **Update** | Revise existing standards | Add new security requirement, update API conventions |
| **Correction** | Fix errors or outdated information | Broken links, deprecated tooling |
| **Audit Finding** | Document a compliance issue | Gaps discovered during audit |
| **Tooling** | Add CI/CD, scripts, or templates | Markdown lint, PR templates |

---

## Contribution Process

### Step 1: Create an Issue First

Before writing any content, create an issue to:
- Describe what needs to be added/updated
- Explain why this is needed
- Get early feedback from CoE team

**Issue Templates:**
- [Standards Update Request](.github/ISSUE_TEMPLATE/standards-update.md)
- [Audit Finding](.github/ISSUE_TEMPLATE/audit-finding.md)
- [Security Concern](.github/ISSUE_TEMPLATE/security-issue.md)
- [General Issue](.github/ISSUE_TEMPLATE/general.md)

### Step 2: Propose a Change

1. **Fork the repository** (if external) or create a branch
2. **Branch naming:** `docs/update-<short-description>` or `docs/add-<stack>-standards`
3. **Make your changes** following the document structure below
4. **Preview** the markdown renders correctly
5. **Submit a PR** with the issue linked

### Step 3: Review Process

| Document Type | Reviewer | Approval Required |
|---------------|----------|-------------------|
| New technology standard | CoE Lead + Stack Lead | Yes (2 approvals) |
| Update to existing standard | CoE Lead | Yes (1 approval) |
| Fix/correction | CoE Team | Yes (1 approval) |
| Audit documents | Audit Lead | Yes (2 approvals) |
| Security documents | Security Lead | Yes (2 approvals) |

### Step 4: Merge & Publish

- CoE lead merges after approval
- Standards take effect immediately upon merge to `main`
- Announcement in #coe-updates channel (if internal Slack)

---

## Document Standards

### Required Front Matter

All documents must include:

```markdown
**Version:** X.Y
**Issued by:** Techversant Center of Excellence (CoE)
**Effective Date:** Month YYYY
**Contributors:** Name1, Name2
```

### Required Sections

| Section | Required For |
|---------|--------------|
| Purpose / Introduction | All documents |
| Table of Contents | Documents > 3 sections |
| Related Documents | All documents |
| Document Owner + Review Cycle | All documents |

### Formatting Rules

- Use **markdown tables** for comparisons, checklists, and structured data
- Use **code blocks** with language hints (```php, ```javascript)
- Use **checkboxes** (`- [ ]`) for audit checklists
- Keep line length under 120 characters
- Use consistent heading hierarchy: H1 → H2 → H3 (no skipping)
- Avoid emoji in headings (use Unicode icons in tables if needed)

### Naming Conventions

| File Type | Convention | Example |
|-----------|------------|---------|
| Documents | kebab-case + descriptive | `nodejs-typescript-best-practices.md` |
| Folders | lowercase, plural | `audit/`, `php/` |
| Sections | Title Case | `## Code Quality`, `### Authentication` |

---

## Version Control

### Semantic Versioning for Documents

| Change | Version Bump | Example |
|--------|-------------|---------|
| Minor clarification, typo fix | Patch (1.0 → 1.1) | `**Version:** 1.1` |
| New section, expanded content | Minor (1.0 → 2.0) | `**Version:** 2.0` |
| Breaking change, major rewrite | Major (1.0 → 2.0) | `**Version:** 2.0` |

### Changelog

Maintain a changelog in each major document for significant updates:

```markdown
## Changelog

### v1.2 (May 2026)
- Added Section 4.3 on API rate limiting
- Updated OWASP Top 10 alignment to 2024
- Fixed broken link to security headers reference

### v1.1 (Feb 2026)
- Initial release
```

---

## Proposing New Technology Standards

### Criteria for Inclusion

A new technology standard should be added when:
- [ ] At least two projects actively using the technology
- [ ] A Technology Lead identified who will maintain the standards
- [ ] Business need validated (not every tech gets a standard)
- [ ] CoE approval obtained before creating documents

### Required Documents for New Stack

1. `*-best-practices.md` — Architecture, patterns, tools
2. `*-style-guide.md` — Formatting, naming, documentation
3. `*-code-review-checklist.md` — What to check during reviews

### Request Process

1. Create an issue with: technology, projects using it, proposed lead
2. CoE reviews for business justification
3. CoE approves and assigns lead
4. Lead creates documents following this guide
5. CoE reviews and merges

---

## Security Sensitive Changes

If your change involves:
- Authentication mechanisms
- Encryption standards
- Data handling (especially PII)
- API security

**You must:**
1. Get Security Lead review before merge
2. Include threat analysis in the PR description
3. Reference related compliance requirements (ISO/GDPR)

---

## Getting Help

| Need | Contact |
|------|---------|
| Questions about standards | CoE Team |
| Report a security issue | Security Lead |
| Propose a new standard | CoE Lead |
| Audit-related | Audit Team |

---

**Document Owner:** CoE Team
**Last Updated:** May 2026