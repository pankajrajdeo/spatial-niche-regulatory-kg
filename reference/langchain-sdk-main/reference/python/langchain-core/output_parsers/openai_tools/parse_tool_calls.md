---
title: "parse_tool_calls"
description: "Parse a list of tool calls."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/openai_tools/parse_tool_calls"
category: "reference"
tags: [reference, langchain-core, output_parsers, openai_tools, parse_tool_calls]
---

# parse_tool_calls

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/openai_tools/parse_tool_calls)

Parse a list of tool calls.

## Signature

```python
parse_tool_calls(
    raw_tool_calls: list[dict[str, Any]],
    *,
    partial: bool = False,
    strict: bool = False,
    return_id: bool = True,
) -> list[dict[str, Any]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `raw_tool_calls` | `list[dict[str, Any]]` | Yes | The raw tool calls to parse. |
| `partial` | `bool` | No | Whether to parse partial JSON. (default: `False`) |
| `strict` | `bool` | No | Whether to allow non-JSON-compliant strings. (default: `False`) |
| `return_id` | `bool` | No | Whether to return the tool call id. (default: `True`) |

## Returns

`list[dict[str, Any]]`

The parsed tool calls.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/openai_tools.py#L101)
