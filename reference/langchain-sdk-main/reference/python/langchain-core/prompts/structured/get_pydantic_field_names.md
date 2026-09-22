---
title: "get_pydantic_field_names"
description: "Get field names, including aliases, for a pydantic class."
source: "https://reference.langchain.com/python/langchain-core/prompts/structured/get_pydantic_field_names"
category: "reference"
tags: [reference, langchain-core, prompts, structured, get_pydantic_field_names]
---

# get_pydantic_field_names

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/utils/get_pydantic_field_names)

Get field names, including aliases, for a pydantic class.

## Signature

```python
get_pydantic_field_names(
    pydantic_cls: Any,
) -> set[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `pydantic_cls` | `Any` | Yes | Pydantic class. |

## Returns

`set[str]`

Field names.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/utils.py#L193)
