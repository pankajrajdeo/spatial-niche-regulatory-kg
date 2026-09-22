---
title: "Add custom middleware to Managed Deep Agents"
description: "Add built-in or custom middleware to a managed deep agent."
source: "https://docs.langchain.com/langsmith/managed-deep-agents-middleware"
category: "docs"
tags: [docs, langsmith, managed-deep-agents-middleware]
---

# Add custom middleware to Managed Deep Agents

> Add built-in or custom middleware to a managed deep agent.

Middleware adds behavior around model calls, tool calls, and the agent lifecycle. Like [custom tools](python/managed-deep-agents-tools.md), MDA does not discover middleware automatically. Import it and pass it to the agent definition.

> [!NOTE]
> Managed Deep Agents is in **public [beta](release-stages.md)** and available on [LangSmith Cloud](cloud.md) in the US region only.

Put custom middleware under `middleware/`, import it into the agent entry, and pass it to the agent definition:

```text
my-agent/
  agent.py
  middleware/
    audit.py
```

For the full project layout, see [Project structure](python/managed-deep-agents-project-structure.md).

The managed runtime still owns `backend`, `store`, `checkpointer`, `memory`, `skills`, and the system prompt. Middleware should focus on agent behavior around model calls, tool calls, and lifecycle hooks.

## Add middleware

Use middleware to redact PII, enforce call limits, retry failures, fall back between models, select models dynamically, or log and inspect tool calls.

### Use prebuilt middleware
You can use LangChain [prebuilt middleware](../langchain/middleware/built-in.md) directly in the agent definition:

**agent.py**

```python
from langchain.agents.middleware import ModelCallLimitMiddleware, PIIMiddleware
from managed_deepagents import define_deep_agent

agent = define_deep_agent(
    name="support-agent",
    model="openai:gpt-5.5",
    middleware=[
        PIIMiddleware("email", strategy="redact", apply_to_input=True),
        ModelCallLimitMiddleware(run_limit=50),
    ],
)
```

### Define custom middleware (Optional)
For a more advanced option, define [custom middleware](../langchain/middleware/custom.md) in a local module.

> [!NOTE]
> Middleware is a shared LangChain primitive. Managed Deep Agents always invoke the agent with `ainvoke` and `astream`, so custom middleware must use async hooks. Synchronous hooks remain available when you call [Deep Agents](../deepagents/overview.md) with `invoke` or `stream`.

**middleware/audit.py**

```python
from collections.abc import Awaitable, Callable

from langchain.agents.middleware import wrap_tool_call
from langchain.messages import ToolMessage
from langchain.tools.tool_node import ToolCallRequest
from langgraph.types import Command

@wrap_tool_call
async def log_tool_calls(
    request: ToolCallRequest,
    handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command]],
) -> ToolMessage | Command:
    print(f"Calling tool: {request.tool_call['name']}")
    result = await handler(request)
    print(f"Finished tool: {request.tool_call['name']}")
    return result
```

Import the middleware into the project-root agent entry and pass it in the `middleware` list:

**agent.py**

```python
from managed_deepagents import define_deep_agent

from middleware.audit import log_tool_calls

agent = define_deep_agent(
    name="support-agent",
    model="openai:gpt-5.5",
    middleware=[log_tool_calls],
)
```

Your middleware imports should work the same way they do in a normal local Python project.

## Use runtime context

Middleware can read per-run context through the normal LangChain runtime APIs. Use context for user IDs, organization IDs, feature flags, request metadata, or credentials that should not be part of the model prompt by default.

For examples, see [Custom middleware](../langchain/middleware/custom.md).

## Deployment

`mda dev` and `mda deploy` copy project files into the compiled build, including modules under `middleware/`. Middleware is not synced to Context Hub; it ships with the agent code.

## When to use middleware

| Concept                                                                | Kind             | How it reaches the agent                |
| ---------------------------------------------------------------------- | ---------------- | --------------------------------------- |
| **Middleware**                                                         | Application code | Import and pass in the agent definition |
| **[Custom tools](python/managed-deep-agents-tools.md)**        | Application code | Import and pass in the agent definition |
| **[Instructions](python/managed-deep-agents-instructions.md)** | Managed context  | Always-on system prompt                 |

For more information, see [Project structure](python/managed-deep-agents-project-structure.md).

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-middleware.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
