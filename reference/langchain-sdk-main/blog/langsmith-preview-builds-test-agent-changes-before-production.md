---
title: "LangSmith Preview Builds: Test agent changes before production"
description: "Preview Builds let teams test pull request branches in temporary, production-like LangSmith deployments before merging agent changes."
source: "https://www.langchain.com/blog/langsmith-preview-builds-test-agent-changes-before-production"
category: "blog"
published: "2026-08-20T16:39:00.000Z"
author: "LangChain Accounts"
tags: [blog, langsmith-preview-builds-test-agent-changes-before-production]
---

# LangSmith Preview Builds: Test agent changes before production

Preview Builds are a new LangSmith Deployment feature that make it easier to test agent changes before merging.

Instead of creating a new deployment for every pull request, you can spin up a temporary, production-like deployment from a PR branch. Your team can run the proposed agent, share it with collaborators, inspect its behavior in the same environment, and tear it down when you’re done.

A pull request can change prompts, tools, models, dependencies, or integrations. The impact of those changes often becomes clear only when the agent runs. Local testing helps during development, but it rarely gives the rest of the team a consistent place to review behavior before the change reaches production.

Preview Builds give each PR its own staging environment for your agent. Teams can test changes in LangSmith Deployment before merging, without adding extra deployment setup to their CI/CD workflow.

## Test branches in a deployed environment

When a pull request triggers a Preview Build, LangSmith deploys the source branch in an isolated environment linked to the parent deployment. The preview runs the code under review without updating the parent.

This gives teams a place to test the full agent. Reviewers can try prompts, exercise tool calls, inspect traces, and check how the agent behaves with its configured dependencies and services. They can also test failure paths and edge cases that may not appear in code review.

Because the preview runs as a deployment, collaborators do not need to clone the repository or reproduce the developer’s local setup. Everyone reviews the same version of the agent in the same environment.

## Keep previews in sync with pull requests

LangSmith builds the latest commit from the pull request’s source branch on a short-lived preview deployment. When someone pushes another commit to the branch, LangSmith automatically creates a new revision of that preview deployment.

This keeps the preview useful throughout review. A developer can respond to feedback, push an update, and ask collaborators to test the change again without creating another environment or merging unfinished work. The pull request remains the place for code discussion, while the preview provides a running version of the proposed change.

Teams can choose how pull requests trigger previews:

- **Every PR** creates a preview for each pull request opened against the deployment branch.
- **Label only** creates a preview after someone adds a configured GitHub label.

Every PR works well when most changes need behavioral review. Label only gives teams more control when previews should run only for selected changes.

## Give collaborators a shared review environment

Agent reviews often involve people outside the team writing the code. Product managers may want to check the user experience, domain experts may need to validate terminology or policy behavior, and QA may want to test known failure cases.

A preview deployment gives those collaborators a shared artifact tied to the pull request. They can test the proposed agent directly and leave feedback while the change is still easy to revise. Engineers can use the same preview to inspect tool calls and traces behind a response.

Teams can also run multiple preview deployments at once. Separate pull requests remain isolated, so reviewers can compare changes without moving a shared staging deployment between branches.

## Control preview usage and cleanup

Preview Builds include controls for managing temporary environments easily:

- **Idle TTL** sets how long a preview can remain inactive after its latest revision. LangSmith deletes the preview after that period expires.
- **Max concurrent previews** limits how many previews can run for a parent deployment at the same time.
- Teams can delete a preview manually at any point. Deleting the parent deployment also deletes its preview deployments.

Preview deployments copy the parent deployment’s secrets when they’re created and keep that initial set unless you override them. For sensitive services, use credentials scoped to preview workloads rather than production, especially if previews can be created from pull requests by external or less-trusted contributors.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6a872ed8e203ddde0ba95d18_preview-builds-settings.png)

## Enable Preview Builds

Preview Builds are available in Public Beta for deployments connected through the GitHub integration on LangSmith Cloud.

Open **Deployment Settings**, find **Preview Builds**, and enable the feature. Choose **Every PR** or **Label only**, configure the idle TTL and concurrency limit, then save your changes.

The next qualifying pull request will create a preview deployment from its source branch. Share it with the people reviewing the change, push updates as needed, and merge after the agent behaves the way you expect.

[Log in or sign up](https://smith.langchain.com/) to LangSmith to try Preview Builds | [Read the docs](../langsmith/preview-builds.md#preview-builds)
