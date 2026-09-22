---
title: "parse_json_markdown"
description: "Parse a JSON string from a Markdown string."
source: "https://reference.langchain.com/python/langchain-core/utils/json/parse_json_markdown"
category: "reference"
tags: [reference, langchain-core, utils, json, parse_json_markdown]
---

# parse_json_markdown

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/json/parse_json_markdown)

Parse a JSON string from a Markdown string.

## Signature

```python
parse_json_markdown(
    json_string: str,
    *,
    parser: Callable[[str], Any] = parse_partial_json,
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `json_string` | `str` | Yes | The Markdown string. |
| `parser` | `Callable[[str], Any]` | No | The parser to use. (default: `parse_partial_json`) |

## Returns

`Any`

The parsed JSON object as a Python dictionary.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/json.py#L142)
