---
title: "vformat"
description: "Format a string using only keyword arguments."
source: "https://reference.langchain.com/python/langchain-core/utils/formatting/StrictFormatter/vformat"
category: "reference"
tags: [reference, langchain-core, utils, formatting, strictformatter, vformat]
---

# vformat

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/formatting/StrictFormatter/vformat)

Format a string using only keyword arguments.

Overrides the base `vformat` to reject positional arguments, ensuring all
substitutions are explicit and named.

## Signature

```python
vformat(
    self,
    format_string: str,
    args: Sequence[Any],
    kwargs: Mapping[str, Any],
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `format_string` | `str` | Yes | A string containing replacement fields (e.g., `'{name}'`). |
| `args` | `Sequence[Any]` | Yes | Positional arguments (must be empty). |
| `kwargs` | `Mapping[str, Any]` | Yes | Keyword arguments for substitution into the format string. |

## Returns

`str`

The formatted string with all replacement fields substituted.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/formatting.py#L23)
