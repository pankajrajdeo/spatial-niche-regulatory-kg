---
title: "awrap_tool_call"
description: "Async variant of wrap_tool_call."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware/awrap_tool_call"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, humanintheloopmiddleware, awrap_tool_call]
---

# awrap_tool_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware/awrap_tool_call)

Async variant of `wrap_tool_call`.

## Signature

```python
awrap_tool_call(
    self,
    request: ToolCallRequest,
    handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command[Any]]],
) -> ToolMessage | Command[Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ToolCallRequest` | Yes | The tool call request being executed. |
| `handler` | `Callable[[ToolCallRequest], Awaitable[ToolMessage \| Command[Any]]]` | Yes | Awaitable callable that executes the tool. |

## Returns

`ToolMessage | Command[Any]`

The tool result, with a note prepended when a reviewer edited the call.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L663)
