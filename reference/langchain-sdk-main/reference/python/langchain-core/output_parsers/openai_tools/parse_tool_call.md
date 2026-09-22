---
title: "parse_tool_call"
description: "Parse a single tool call."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/openai_tools/parse_tool_call"
category: "reference"
tags: [reference, langchain-core, output_parsers, openai_tools, parse_tool_call]
---

# parse_tool_call

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/openai_tools/parse_tool_call)

Parse a single tool call.

## Signature

```python
parse_tool_call(
    raw_tool_call: dict[str, Any],
    *,
    partial: bool = False,
    strict: bool = False,
    return_id: bool = True,
) -> dict[str, Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `raw_tool_call` | `dict[str, Any]` | Yes | The raw tool call to parse. |
| `partial` | `bool` | No | Whether to parse partial JSON. (default: `False`) |
| `strict` | `bool` | No | Whether to allow non-JSON-compliant strings. (default: `False`) |
| `return_id` | `bool` | No | Whether to return the tool call id. (default: `True`) |

## Returns

`dict[str, Any] | None`

The parsed tool call.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/openai_tools.py#L26)
