---
title: "awrap_tool_call"
description: "(async) Check the size of the tool call result and evict to filesystem if too large."
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/awrap_tool_call"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, filesystemmiddleware, awrap_tool_call]
---

# awrap_tool_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/awrap_tool_call)

(async) Check the size of the tool call result and evict to filesystem if too large.

## Signature

```python
awrap_tool_call(
    self,
    request: ToolCallRequest,
    handler: Callable[[ToolCallRequest], Awaitable[ToolMessage | Command]],
) -> ToolMessage | Command
```

## Description

**Note:**

Tool-execution exceptions (including `ToolException`) propagate
through this wrapper unhandled by design.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `request` | `ToolCallRequest` | Yes | The tool call request being processed. |
| `handler` | `Callable[[ToolCallRequest], Awaitable[ToolMessage \| Command]]` | Yes | The handler function to call with the modified request. |

## Returns

`ToolMessage | Command`

The raw `ToolMessage`, or a pseudo tool message with the `ToolResult` in state.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/filesystem.py#L3631)
