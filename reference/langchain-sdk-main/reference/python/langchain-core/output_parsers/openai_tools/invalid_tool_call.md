---
title: "invalid_tool_call"
description: "Create an invalid tool call."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/openai_tools/invalid_tool_call"
category: "reference"
tags: [reference, langchain-core, output_parsers, openai_tools, invalid_tool_call]
---

# invalid_tool_call

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/tool/invalid_tool_call)

Create an invalid tool call.

## Signature

```python
invalid_tool_call(
    *,
    name: str | None = None,
    args: str | None = None,
    id: str | None = None,
    error: str | None = None,
) -> InvalidToolCall
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | `str \| None` | No | The name of the tool to be called. (default: `None`) |
| `args` | `str \| None` | No | The arguments to the tool call as a JSON string. (default: `None`) |
| `id` | `str \| None` | No | An identifier associated with the tool call. (default: `None`) |
| `error` | `str \| None` | No | An error message associated with the tool call. (default: `None`) |

## Returns

`InvalidToolCall`

The created invalid tool call.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/tool.py#L326)
