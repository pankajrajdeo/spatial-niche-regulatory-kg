---
title: "get_all_basemodel_annotations"
description: "Get all annotations from a Pydantic BaseModel and its parents."
source: "https://reference.langchain.com/python/langchain-core/tools/base/get_all_basemodel_annotations"
category: "reference"
tags: [reference, langchain-core, tools, base, get_all_basemodel_annotations]
---

# get_all_basemodel_annotations

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/get_all_basemodel_annotations)

Get all annotations from a Pydantic `BaseModel` and its parents.

## Signature

```python
get_all_basemodel_annotations(
    cls: TypeBaseModel | Any,
    *,
    default_to_bound: bool = True,
) -> dict[str, type | TypeVar]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `cls` | `TypeBaseModel \| Any` | Yes | The Pydantic `BaseModel` class. |
| `default_to_bound` | `bool` | No | Whether to default to the bound of a `TypeVar` if it exists. (default: `True`) |

## Returns

`dict[str, type | TypeVar]`

`dict` of field names to their type annotations.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/base.py#L1830)
