---
title: "Deep Agents Code"
description: "Terminal coding agent built on the Deep Agents SDK"
source: "https://docs.langchain.com/oss/python/deepagents/cli/overview"
category: "docs"
tags: [docs, deepagents, cli]
---

# Deep Agents Code

> Terminal coding agent built on the Deep Agents SDK

Deep Agents Code (`dcode`) is an open source coding agent built on the [Deep Agents SDK](../quickstart.md).
It works with any large language model and supports switching providers or models.
Persistent memory carries context across conversations, customizable skills shape behavior, and approval controls gate code execution.

## Get started

Run the following command to install Deep Agents Code and launch an interactive session:

```bash
curl -LsSf https://langch.in/dcode | bash
dcode
```

See the [Quickstart](../code/quickstart.md) to add provider credentials, run your first task, and learn interactive mode.

> **Video:** [Deep Agents Code terminal demo](https://mintcdn.com/langchain-5e9cc07a/RVTbVyxmLiI04cgS/oss/images/deepagents/dcode-small.mp4?fit=max&auto=format&n=RVTbVyxmLiI04cgS&q=85&s=0d35e29a34f349183e83bd3d1eceb68b)

## Capabilities

#### [Remote sandboxes](../code/remote-sandboxes.md)
Run agent tools remotely instead of on your local machine.

#### [Goals and rubrics](../code/goals-and-rubrics.md)
Define measurable objectives or grading criteria so the agent can check whether work is done.

#### [Subagents](../code/subagents.md)
Delegate work to task-specific subagents for parallel execution.

#### [Memory](../code/memory-and-skills.md#memory)
Store and retrieve information across sessions, including project conventions and learned patterns.

#### [Context compaction](../code/quickstart.md#interactive-mode)
Summarize older messages and offload originals to storage.

#### [Human-in-the-loop](../code/quickstart.md#interactive-mode)
Require human approval for sensitive tool operations.

#### [Skills](../code/memory-and-skills.md#skills)
Extend agent capabilities with custom expertise and instructions.

#### [MCP tools](../code/mcp-tools.md)
Load external tools from Model Context Protocol servers.

#### [Tracing](../code/quickstart.md#trace-with-langsmith)
Trace agent operations in LangSmith for observability and debugging.

## Next steps

#### [Quickstart](../code/quickstart.md)
Install Deep Agents Code, run your first task, and use interactive or non-interactive modes.

#### [Configuration](../code/configuration.md)
Set up credentials, `config.toml`, environment variables, hooks, and CLI flags.

***

> [!NOTE]
> [Connect these docs](../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/code/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
