---
title: "Manage Context Hub for Managed Deep Agents"
description: "Understand how Managed Deep Agents stores instructions, skills, and durable memory in LangSmith Context Hub."
source: "https://docs.langchain.com/langsmith/javascript/managed-deep-agents-context-hub"
category: "docs"
tags: [docs, langsmith, javascript, managed-deep-agents-context-hub]
---

# Manage Context Hub for Managed Deep Agents

> Understand how Managed Deep Agents stores instructions, skills, and durable memory in LangSmith Context Hub.

Managed Deep Agents stores deploy-owned instructions and skills, and optional durable memory, in [LangSmith Context Hub](../use-the-context-hub.md). That split lets you change agent behavior without rebuilding application code, while the project remains the source of truth for lasting instruction and skill updates.

> [!NOTE]
> Managed Deep Agents is in **public [beta](../release-stages.md)** and available on [LangSmith Cloud](../cloud.md) in the US region only.

## What lives in Context Hub

| Content        | Project source                                                                    | Synced on `mda deploy`                               | Writable by the agent         |
| -------------- | --------------------------------------------------------------------------------- | ---------------------------------------------------- | ----------------------------- |
| System prompt  | [`instructions.md`](managed-deep-agents-instructions.md)       | Yes                                                  | No                            |
| Skills         | [`skills/`](managed-deep-agents-skills.md)                     | Yes                                                  | No                            |
| Durable memory | Optional [`memory`](managed-deep-agents-memory.md) declaration | Enables the tree; does not overwrite existing memory | Yes, under `/memories/agent/` |

Tools, middleware, MCP connectors, channels, schedules, sandboxes, and the agent definition ship with the compiled deployment. They are not synced to Context Hub.

For ownership of managed runtime fields, see [Agent definition](managed-deep-agents-agent-definition.md).

## Source of truth

The project and Context Hub both hold copies of `instructions.md` and `skills/`. Which copy wins depends on where you make lasting changes and how you resolve conflicts on deploy.

* **Project files**: Treat `instructions.md` and `skills/` in the project as the source of truth for lasting changes. Each `mda deploy` syncs those files into the agent's Context Hub repo.
* **Context Hub edits**: Edit files in Context Hub when you need a quick change that should apply without a code redeploy. Those Hub edits stay live until a later deploy overwrites them, or until you choose to keep the Hub copy when a conflict prompt appears.
* **Durable memory**: Memory under `/memories/agent/` is agent-owned. Deploys enable the tree but do not overwrite content already stored there.

## How deploy syncs context

`mda deploy` syncs deploy-owned context as part of the deploy pipeline:

* **Instructions and skills**: Each deploy updates the agent's Context Hub repo from the project files. Later deploys sync the project copies again. For skills, deploys also remove deployed skill files that no longer exist locally.
* **Durable memory**: When memory is enabled, the deployment mounts one Context Hub tree at `/memories/agent/`. Deploys do not overwrite content already stored there.
* **Conflicts**: If `instructions.md` or `skills/` changed in Context Hub since the last `mda deploy`, the CLI stops before syncing and asks whether to overwrite the Context Hub copy with the project copy. The default answer keeps the Context Hub version and skips syncing that section. In a non-interactive shell there is no prompt. The deploy exits with an error, and you must re-run with `--context-strategy overwrite` or `--context-strategy keep-hub`. Re-running `mda deploy` on its own reports the same conflict again.
* **Concurrent edits**: If the repo changes during the sync itself, the deploy fails with a commit conflict. Re-run `mda deploy`.

Interactive conflict prompt:

```text
◇  Checked Context Hub context
│
▲  Context Hub instructions.md changed since the last MDA sync.
│
◆  Overwrite Hub-edited instructions.md with the local version?
│  ○ Yes / ● No
└
```

Non-interactive conflict (CI or redirected output):

```text
└  Context Hub instructions.md and skills/ changed since the last MDA sync. Re-run with --context-strategy overwrite or --context-strategy keep-hub.
```

| Strategy    | Effect                                                                                                 |
| ----------- | ------------------------------------------------------------------------------------------------------ |
| `overwrite` | Replace the Hub-edited `instructions.md` or `skills/` with the project copy, then continue the deploy. |
| `keep-hub`  | Keep the Context Hub version, skip syncing that section, and continue the deploy.                      |

For the full deploy step list and flags, see the [CLI reference](managed-deep-agents-cli.md#deploy-projects). For secrets routing and deploy options, see [Deploy an agent](managed-deep-agents-deploy.md).

## Edit context in LangSmith

After a successful deploy:

1. Open the deployment in LangSmith.
2. Use the Details sidebar link to the Context Hub repo that holds the deployment's instructions, skills, and memories. Archived repos are labeled when the context is no longer live.
3. Edit files in Context Hub when you need a quick change that should apply without a code redeploy.

For lasting changes, edit the project copies and redeploy. For how deploy resolves Hub edits, see [Source of truth](#source-of-truth).

For browsing commits, promoting environments, and Context Hub concepts outside Managed Deep Agents, see [Use the Context Hub](../use-the-context-hub.md) and [Context engineering concepts](../context-engineering-concepts.md).

## Local development

`mda dev` creates a local Context Hub mock for instructions, skills, and memory. Local Studio sessions do not create or update the hosted Context Hub repo for a deployment.

For more information, see [Develop locally with LangSmith Studio](managed-deep-agents-local-development.md).

## Choose where context belongs

| Goal                                                  | Use                                                                                                                                                                                                         |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Always-on system prompt                               | [Instructions](managed-deep-agents-instructions.md)                                                                                                                                      |
| Task-specific procedures                              | [Skills](managed-deep-agents-skills.md)                                                                                                                                                  |
| Knowledge the agent learns and retains across threads | [Memory](managed-deep-agents-memory.md)                                                                                                                                                  |
| Application logic and external calls                  | [Tools](managed-deep-agents-tools.md), [MCP connectors](managed-deep-agents-mcp-connectors.md), or [middleware](managed-deep-agents-middleware.md) |

## See also

* [Project structure](managed-deep-agents-project-structure.md)
* [Deploy an agent](managed-deep-agents-deploy.md)
* [Use the Context Hub](../use-the-context-hub.md)
* [Manage contexts with the SDK](../manage-contexts-sdk.md)

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-context-hub.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
