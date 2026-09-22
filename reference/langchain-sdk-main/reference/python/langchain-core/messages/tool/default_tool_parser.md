---
title: "default_tool_parser"
description: "Best-effort parsing of tools."
source: "https://reference.langchain.com/python/langchain-core/messages/tool/default_tool_parser"
category: "reference"
tags: [reference, langchain-core, messages, tool, default_tool_parser]
---

# default_tool_parser

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/tool/default_tool_parser)

Best-effort parsing of tools.

## Signature

```python
default_tool_parser(
    raw_tool_calls: list[dict[str, Any]],
) -> tuple[list[ToolCall], list[InvalidToolCall]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `raw_tool_calls` | `list[dict[str, Any]]` | Yes | List of raw tool call dicts to parse. |

## Returns

`tuple[list[ToolCall], list[InvalidToolCall]]`

A list of tool calls and invalid tool calls.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/tool.py#L349)
