---
title: "awrap_tool_call"
description: "Async version of wrap_tool_call."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_emulator/LLMToolEmulator/awrap_tool_call"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_emulator, llmtoolemulator, awrap_tool_call]
---

# awrap_tool_call

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_emulator/LLMToolEmulator/awrap_tool_call)

Async version of `wrap_tool_call`.

Emulate tool execution using LLM if tool should be emulated.

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
| `request` | `ToolCallRequest` | Yes | Tool call request to potentially emulate. |
| `handler` | `Callable[[ToolCallRequest], Awaitable[ToolMessage \| Command[Any]]]` | Yes | Async callback to execute the tool (can be called multiple times). |

## Returns

`ToolMessage | Command[Any]`

ToolMessage with emulated response if tool should be emulated,
otherwise calls handler for normal execution.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/tool_emulator.py#L198)
