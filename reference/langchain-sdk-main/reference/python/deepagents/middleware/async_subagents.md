---
title: "async_subagents"
description: "Middleware for async subagents running on remote Agent Protocol servers."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents]
---

# async_subagents

> **Module** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents)

Middleware for async subagents running on remote Agent Protocol servers.

Async subagents use the LangGraph SDK to launch background runs on remote
[Agent Protocol](https://github.com/langchain-ai/agent-protocol) servers.
Unlike synchronous subagents (which block until completion), async subagents
return a task ID immediately, allowing the main agent to monitor progress and
send updates while the subagent works.

Compatible with LangGraph Platform (managed) and self-hosted servers.

## Properties

- `logger`
- `ASYNC_TASK_TOOL_DESCRIPTION`

## Methods

- [`append_to_system_message()`](https://reference.langchain.com/python/deepagents/middleware/async_subagents/append_to_system_message)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/async_subagents.py)
