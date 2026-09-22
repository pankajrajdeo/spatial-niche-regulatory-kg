---
title: "awrap_tool_call"
description: "Async version of wrap_tool_call."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_error/ToolErrorMiddleware/awrap_tool_call"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_error, toolerrormiddleware, awrap_tool_call]
---

# awrap_tool_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_error/ToolErrorMiddleware/awrap_tool_call)

Async version of `wrap_tool_call`.

Uses `aon_error` if provided, otherwise the sync `on_error`. The sync path never
awaits.

## Signature

```python
awrap_tool_call(
    self,
    request: ToolCallRequest,
    handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command[Any]]],
) -> ToolMessage | Command[Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/tool_error.py#L175)
