# 08. Cloud, Containers and DevOps

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-05 · **Next review:** 2027-02-05

Many CFML applications still run on hand-built Windows servers. Containers, automated pipelines and cloud hosting make
them repeatable and easier to support. Back to the [roadmap](./README.md).

## Containers for CFML

Both main engines run well in containers.

**What to learn:**

- The CommandBox images from Ortus Solutions, which can run Lucee or Adobe ColdFusion
- Adobe's own ColdFusion images
- Passing configuration through environment variables and CFConfig instead of the administrator
- Keeping the container stateless: no uploads or sessions stored inside it

**Resources:**

- [CommandBox images on Docker Hub](https://hub.docker.com/r/ortussolutions/commandbox)
- [Adobe ColdFusion images on Docker Hub](https://hub.docker.com/r/adobecoldfusion/coldfusion)

**Level:** Practitioner · Core

## Licensing in containers and the cloud

Adobe ColdFusion licensing depends on edition, cores and the number of containers. Getting it wrong can be expensive.

**What to learn:**

- How Adobe counts cores for Standard and Enterprise editions
- How the ColdFusion 2025 subscription changes the cost model
- When to ask Adobe or a reseller for a written answer before you design the architecture

**Resources:**

- [Adobe ColdFusion product terms](https://wwwimages2.adobe.com/content/dam/cc/en/legal/servicetou/Adobe-ColdFusion-Product-Specific-Terms-en_US-20250225.pdf)
- [ColdFusion licensing for Docker containers, Adobe, 2019](https://coldfusion.adobe.com/2019/03/coldfusion-licensing-docker-containers/),
  older guidance to confirm against the current terms

**Level:** Advanced · Core

## Sessions and shared state

Several servers behind a load balancer need a shared place for sessions and cached data.

**What to learn:**

- Sticky sessions versus sessions stored in Redis or a database
- Moving application-scope data that must be shared
- Testing that a user stays logged in when a server stops

**Resources:** [Deep expertise guide, section 8](./reference/coldfusion-deep-expertise-guide.md#8-configure-session-management-for-clustered-environments)

**Level:** Advanced · Core

## CI/CD for CFML

Continuous integration and continuous delivery (CI/CD) means every change is tested and deployed the same way, by an
automated pipeline.

**What to learn:**

- Running TestBox in a pipeline with CommandBox
- Building and publishing a container image for each version
- Deploying to test and production with approval and rollback

**Resources:**

- [TestBox documentation](https://testbox.ortusbooks.com/)
- [Git Workflow](../../../standards/git/git-workflow.md), for branches and releases

**Level:** Practitioner · Core

## Cloud platforms

Know one major cloud well enough to host a CFML application safely.

**What to learn:**

- Running containers or virtual machines behind a load balancer
- Managed databases, shared file storage and secrets managers
- Logging, monitoring and cost alerts

**Resources:** [AWS documentation](https://docs.aws.amazon.com/), [Azure documentation](https://learn.microsoft.com/en-us/azure/)

**Level:** Practitioner · Core

## Infrastructure as code

Defining infrastructure in code lets the client's team see, review and recreate it.

**What to learn:** Terraform or OpenTofu basics: resources, variables, state, plan and apply.

**Resources:** [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)

**Level:** Advanced · Optional

## Project: Containerize and Ship the Practice App

**Brief:** Run the migrated practice app in containers, deploy it through a pipeline, and show it survives losing a
server.

**Size:** 3–4 days

**Verification**, checked by a senior engineer:

- [ ] A container image built from the repository, with configuration from environment variables and no secrets in
  the image
- [ ] The pipeline runs the TestBox suite and stops on any failure
- [ ] Pushing a version tag deploys to a test environment; production needs an approval step
- [ ] Two app containers behind a load balancer; stopping one does not log users out
- [ ] Uploaded files are stored outside the containers and survive a redeploy
- [ ] A rollback to the previous version, demonstrated and timed
- [ ] A licensing note: the edition, core count and cost this design would need for Adobe ColdFusion, or why Lucee
  needs none

Previous: [07. Upgrades and Migration](./07-upgrades-and-migration.md) · Next: [09. Modernizing the Application](./09-modernizing-the-application.md)
