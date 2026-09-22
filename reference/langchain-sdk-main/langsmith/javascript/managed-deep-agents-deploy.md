---
title: "Deploy a Managed Deep Agent"
description: "Test and deploy a Managed Deep Agent with the mda CLI."
source: "https://docs.langchain.com/langsmith/javascript/managed-deep-agents-deploy"
category: "docs"
tags: [docs, langsmith, javascript, managed-deep-agents-deploy]
---

# Deploy a Managed Deep Agent

> Test and deploy a Managed Deep Agent with the mda CLI.

Deploying a Managed Deep Agent compiles a code-first project into a managed LangGraph app, syncs deploy-owned context to [Context Hub](managed-deep-agents-context-hub.md), uploads the compiled source, and triggers a LangSmith hosted deployment build. The result is an [Agent Server](../agent-server-overview.md) deployment, including the Agent Server API and [MCP endpoint](managed-deep-agents-mcp-endpoint.md).

> [!NOTE]
> Managed Deep Agents is in **public [beta](../release-stages.md)** and available on [LangSmith Cloud](../cloud.md) in the US region only.

This page covers secrets routing and deploy options. To test the agent before deploying, see [Develop locally with LangSmith Studio](managed-deep-agents-local-development.md). For command flags, the deploy step list, and troubleshooting, see the [CLI reference](managed-deep-agents-cli.md).

## Prerequisites

Before you deploy, make sure you have:

* A workspace with Managed Deep Agents public beta access.

* A [LangSmith API key](../create-account-api-key.md) for that workspace, either in `.env` or your shell environment.

* The `mda` CLI installed from `managed-deepagents`.

* Project dependencies installed with `npm install` for TypeScript projects.

* Model provider credentials, such as `OPENAI_API_KEY`, in `.env`, your shell environment, or LangSmith workspace secrets.

The CLI targets US LangSmith Cloud by default.

## Deploy to LangSmith

Deploy the local project:

**npm**

```bash
npx mda deploy
```

**pnpm**

```bash
pnpm exec mda deploy
```

**bun**

```bash
bunx mda deploy
```

> [!TIP]
> `mda deploy` routes local project inputs to different managed surfaces:
>
> ```text
> instructions.md + skills/**  -> Context Hub deploy-owned context
> .env                         -> deploy auth + non-reserved hosted secrets, not archived
> project source files         -> .mda/build source archive -> hosted deployment
> schedules/**                 -> LangSmith cron jobs after the deployment is live
> ```

Set the deployment name explicitly when the directory name is not the name you want:

**npm**

```bash
npx mda deploy --name research-assistant
```

**pnpm**

```bash
pnpm exec mda deploy --name research-assistant
```

**bun**

```bash
bunx mda deploy --name research-assistant
```

Use `--deployment-type prod` when creating a production deployment:

**npm**

```bash
npx mda deploy --deployment-type prod
```

**pnpm**

```bash
pnpm exec mda deploy --deployment-type prod
```

**bun**

```bash
bunx mda deploy --deployment-type prod
```

Use `--no-wait` to trigger the build without polling for completion:

**npm**

```bash
npx mda deploy --no-wait
```

**pnpm**

```bash
pnpm exec mda deploy --no-wait
```

**bun**

```bash
bunx mda deploy --no-wait
```

When `--no-wait` is set, schedule reconciliation is skipped for that deploy invocation because the CLI exits before the deployment reaches `DEPLOYED`.

On success, the CLI prints the LangSmith deployment dashboard URL. For the full deploy step list, see the [CLI reference](managed-deep-agents-cli.md#deploy-projects).

## Secrets and environment files

`mda deploy` reads project `.env` values before shell environment variables. Use `.env` for the LangSmith API key that authenticates the deploy and for runtime secrets the hosted deployment needs:

**.env**

```text
LANGSMITH_API_KEY=<LANGSMITH_API_KEY>
OPENAI_API_KEY=<OPENAI_API_KEY>
GITHUB_MCP_TOKEN=<GITHUB_MCP_TOKEN>
DATABASE_URL=<DATABASE_URL>
```

`LANGSMITH_API_KEY`, `LANGGRAPH_HOST_API_KEY`, `LANGCHAIN_API_KEY`, and other platform variables are reserved. They can authenticate the deploy, but they are not uploaded as user-managed deployment secrets.

Non-reserved `.env` entries, such as model provider keys, MCP tokens, and custom tool credentials, are forwarded as hosted deployment secrets when `mda deploy` creates or updates the deployment. If the configured model requires a provider key, deploy fails before upload unless that key is available from `.env`, the shell environment, or LangSmith workspace secrets. When the provider key is only in the shell environment, `mda deploy` forwards it as a secret for that deploy.

Reserved platform variables, empty values, `.env`, and `.env.*` files are not copied into the compiled build archive.

For authentication key order and reserved variables, see the [CLI reference](managed-deep-agents-cli.md#authentication).

## Troubleshoot a deploy

For deploy troubleshooting, see the [CLI reference](managed-deep-agents-cli.md#troubleshooting).

If a deployment reaches `BUILD_FAILED` or `DEPLOY_FAILED`, open the printed deployment URL in LangSmith and inspect the revision logs.

## Next steps

#### [Agent Server](../agent-server-overview.md)
Explore the runtime that hosts the deployment.

#### [MCP endpoint](managed-deep-agents-mcp-endpoint.md)
Expose the deployed agent as a tool to MCP clients.

#### [Identity](managed-deep-agents-identity.md)
Authenticate callers and provide private threads.

#### [Schedules](managed-deep-agents-schedules.md)
Run agents on managed cron schedules.

#### [Custom tools](managed-deep-agents-tools.md)
Add authored LangChain tools to the agent definition.

#### [CLI reference](managed-deep-agents-cli.md)
Look up every `mda` command and flag.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-deploy.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
