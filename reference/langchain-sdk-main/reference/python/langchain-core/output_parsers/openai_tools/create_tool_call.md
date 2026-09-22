---
title: "create_tool_call"
description: "Create a ToolCall."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/openai_tools/create_tool_call"
category: "reference"
tags: [reference, langchain-core, output_parsers, openai_tools, create_tool_call]
---

# create_tool_call

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/create_tool_call)

Create a `ToolCall`.

## Signature

```python
create_tool_call(
    name: str,
    args: dict[str, Any],
    *,
    id: str | None = None,
    index: int | str | None = None,
    **kwargs: Any = {},
) -> ToolCall
```

## Description

!!! note

The `id` is generated automatically if not provided, using a UUID4 format
prefixed with `'lc_'` to indicate it is a LangChain-generated ID.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | `str` | Yes | The name of the tool to be called. |
| `args` | `dict[str, Any]` | Yes | The arguments to the tool call. |
| `id` | `str \| None` | No | An identifier for the tool call.  Generated automatically if not provided. (default: `None`) |
| `index` | `int \| str \| None` | No | Index of block in aggregate response.  Used during streaming. (default: `None`) |

## Returns

`ToolCall`

A properly formatted `ToolCall`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L1318)
