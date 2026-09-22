---
title: "pydantic_copy"
description: "Copy any Pydantic model, compatible with both v1 and v2."
source: "https://reference.langchain.com/python/langchain-core/tracers/_compat/pydantic_copy"
category: "reference"
tags: [reference, langchain-core, tracers, compat, pydantic_copy]
---

# pydantic_copy

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/_compat/pydantic_copy)

Copy any Pydantic model, compatible with both v1 and v2.

## Signature

```python
pydantic_copy(
    obj: T,
    **kwargs: Any = {},
) -> T
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `obj` | `T` | Yes | The Pydantic model to copy. |
| `**kwargs` | `Any` | No | Additional arguments passed to `model_copy`/`copy`. (default: `{}`) |

## Returns

`T`

A copy of the model.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/_compat.py#L83)
