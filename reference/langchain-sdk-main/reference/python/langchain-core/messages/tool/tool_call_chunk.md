---
title: "tool_call_chunk"
description: "Create a tool call chunk."
source: "https://reference.langchain.com/python/langchain-core/messages/tool/tool_call_chunk"
category: "reference"
tags: [reference, langchain-core, messages, tool, tool_call_chunk]
---

# tool_call_chunk

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/tool/tool_call_chunk)

Create a tool call chunk.

## Signature

```python
tool_call_chunk(
    *,
    name: str | None = None,
    args: str | None = None,
    id: str | None = None,
    index: int | None = None,
) -> ToolCallChunk
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | `str \| None` | No | The name of the tool to be called. (default: `None`) |
| `args` | `str \| None` | No | The arguments to the tool call as a JSON string. (default: `None`) |
| `id` | `str \| None` | No | An identifier associated with the tool call. (default: `None`) |
| `index` | `int \| None` | No | The index of the tool call in a sequence. (default: `None`) |

## Returns

`ToolCallChunk`

The created tool call chunk.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/tool.py#L303)
