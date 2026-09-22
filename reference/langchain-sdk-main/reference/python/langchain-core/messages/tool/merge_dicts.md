---
title: "merge_dicts"
description: "Merge dictionaries."
source: "https://reference.langchain.com/python/langchain-core/messages/tool/merge_dicts"
category: "reference"
tags: [reference, langchain-core, messages, tool, merge_dicts]
---

# merge_dicts

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/_merge/merge_dicts)

Merge dictionaries.

Merge many dicts, handling specific scenarios where a key exists in both
dictionaries but has a value of `None` in `'left'`. In such cases, the method uses
the value from `'right'` for that key in the merged dictionary.

## Signature

```python
merge_dicts(
    left: dict[str, Any],
    *others: dict[str, Any] = (),
) -> dict[str, Any]
```

## Description

**Example:**

If `left = {"function_call": {"arguments": None}}` and
`right = {"function_call": {"arguments": "{\n"}}`, then, after merging, for the
key `'function_call'`, the value from `'right'` is used, resulting in
`merged = {"function_call": {"arguments": "{\n"}}`.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `left` | `dict[str, Any]` | Yes | The first dictionary to merge. |
| `others` | `dict[str, Any]` | No | The other dictionaries to merge. (default: `()`) |

## Returns

`dict[str, Any]`

The merged dictionary.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/_merge.py#L6)
