# 06. Integration Engineering

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

The solution has to work inside the client's systems, not next to them. Integrating systems and APIs is named in
32% of FDE job postings ([Bloomberry](https://bloomberry.com/blog/i-analyzed-1000-forward-deployed-engineer-jobs-what-i-learned/)). Back to the [roadmap](./README.md).

## Working with legacy systems

Most clients run older systems that still matter. Change them carefully, in small steps.

**What to learn:**

- Mapping the code and its history before changing anything
- Tests that record current behaviour, so you notice what you break
- Replacing parts step by step instead of rewriting everything

**Resources:**

- [Legacy Assessment](../07-consulting/coldfusion/02-legacy-assessment/README.md): mapping architecture, technical
  debt and risks. Written for ColdFusion, but the method applies to any stack.
- [Strangler fig application](https://martinfowler.com/bliki/StranglerFigApplication.html)

**Level:** Practitioner · Core

## Integration patterns

Systems connect through APIs, webhooks, files, queues and batch jobs. Pick the one the client can support and run.

**What to learn:**

- Synchronous calls and asynchronous messages, and when each fits
- Retries, timeouts and duplicate messages
- File and batch integrations, which many clients still depend on

**Resources:**

- [REST API Best Practices](../../standards/general/rest-api-best-practices.md), for REST integrations
- [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/)

**Level:** Practitioner · Core

## Single sign-on (SSO) integration

Your solution should use the client's existing login and permissions. Integrate with their identity provider; never
build authentication yourself. Authentication and authorisation are Red Zone work.

**What to learn:**

- How OpenID Connect sign-in works on top of OAuth 2.0: the authorization code flow with PKCE, ID tokens, and
  checking the token's issuer, audience and expiry
- Mapping the client's groups and roles to permissions in your solution
- Escalating any change to authentication code to a senior engineer

**Resources:**

- [AI Era Coding Guidelines: Red Zone](../../standards/general/ai-era-coding-guidelines.md#22-red-zone-manual-only)
- [Security Audit Reference: tokens, OAuth 2.0 and OIDC](../../security/audit/security-audit-reference.md#94-tokens--jwt-oauth-20-oidc)
- [Security Audit Checklist](../../security/audit/security-audit-checklist.md)
- [How OpenID Connect works](https://openid.net/developers/how-connect-works/)

**Level:** Advanced · Core

## Email, ticketing and ERP integration

A solution only helps if the result reaches the tools people already use: their inbox, their ticketing system, their
ERP or spreadsheets.

**What to learn:**

- Reading from and writing to common business systems through their APIs
- Handling rate limits, outages and permission errors in those systems
- Testing against a sandbox before touching the client's live system

**Resources:** learn on engagements, with a lead.

**Level:** Practitioner · Core

## Access and release approvals

Clients control who gets access and when changes go live. Plan for their process from the first week.

**What to learn:**

- Requesting the access you need early, and only what you need
- Working with the client's CI, change approvals and release windows
- Keeping a record of what was released, when and with whose approval

**Resources:** learn on engagements, with a lead.

**Level:** Practitioner · Core

## Project: Connect the Assistant to a Ticketing Workflow

**Brief:** Extend the standards assistant from stage 04. When a new ticket arrives by webhook, from a mock ticketing
service you build or a vendor sandbox, the assistant drafts a reply. A support agent approves or edits it in a review
screen you add to the tracker from stage 02, and only then is it posted back to the ticket. The assistant looks up
ticket history through a read-only MCP tool you build. Users sign in with OpenID Connect against
[Keycloak running in Docker](https://www.keycloak.org/getting-started/getting-started-docker), standing in for the
client's identity provider.

Sign-in and the approval permission check are Red Zone work: use a well-known OpenID Connect library, write both by
hand without AI generation, and have a senior engineer review them.

**Size:** 4–5 days

**Verification**, checked by a senior engineer:

- [ ] Sending the same webhook twice creates one draft, not two
- [ ] When the ticketing service is down, the job retries with a growing delay and no ticket is lost
- [ ] Nothing is posted to a ticket without an approval recorded with a name and a time
- [ ] Users sign in through Keycloak, and a Keycloak group decides who may approve replies
- [ ] A senior engineer has reviewed and approved the sign-in and permission code
- [ ] The assistant reads ticket history only through your read-only MCP tool, and the tool rejects any write
- [ ] A written access request lists exactly which systems and permissions the integration needs, approved by your
  lead before you connect anything
- [ ] Integration tests cover the duplicate, outage and rejected-draft cases

Previous: [05. AI-Assisted Delivery](./05-ai-assisted-delivery.md) · Next: [07. Cloud and Operations](./07-cloud-and-operations.md)
