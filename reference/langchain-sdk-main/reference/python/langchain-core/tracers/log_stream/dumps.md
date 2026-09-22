---
title: "dumps"
description: "Return a JSON string representation of an object."
source: "https://reference.langchain.com/python/langchain-core/tracers/log_stream/dumps"
category: "reference"
tags: [reference, langchain-core, tracers, log_stream, dumps]
---

# dumps

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/dump/dumps)

Return a JSON string representation of an object.

## Signature

```python
dumps(
    obj: Any,
    *,
    pretty: bool = False,
    **kwargs: Any = {},
) -> str
```

## Description

**Note:**

Plain dicts containing an `'lc'` key are automatically escaped to prevent
confusion with LC serialization format. The escape marker is removed during
deserialization.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `obj` | `Any` | Yes | The object to dump. |
| `pretty` | `bool` | No | Whether to pretty print the json.  If `True`, the json will be indented by either 2 spaces or the amount provided in the `indent` kwarg. (default: `False`) |
| `**kwargs` | `Any` | No | Additional arguments to pass to `json.dumps` (default: `{}`) |

## Returns

`str`

A JSON string representation of the object.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/load/dump.py#L70)
