---
title: "get_color_mapping"
description: "Get mapping for items to a support color."
source: "https://reference.langchain.com/python/langchain-core/utils/input/get_color_mapping"
category: "reference"
tags: [reference, langchain-core, utils, input, get_color_mapping]
---

# get_color_mapping

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/input/get_color_mapping)

Get mapping for items to a support color.

## Signature

```python
get_color_mapping(
    items: list[str],
    excluded_colors: list[str] | None = None,
) -> dict[str, str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `items` | `list[str]` | Yes | The items to map to colors. |
| `excluded_colors` | `list[str] \| None` | No | The colors to exclude. (default: `None`) |

## Returns

`dict[str, str]`

The mapping of items to colors.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/input.py#L14)
