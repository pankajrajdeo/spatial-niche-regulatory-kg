---
title: "get_fields"
description: "Return the field names of a Pydantic model."
source: "https://reference.langchain.com/python/langchain-core/runnables/passthrough/get_fields"
category: "reference"
tags: [reference, langchain-core, runnables, passthrough, get_fields]
---

# get_fields

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/pydantic/get_fields)

Return the field names of a Pydantic model.

## Signature

```python
get_fields(
    model: type[BaseModel | BaseModelV1] | BaseModel | BaseModelV1,
) -> dict[str, FieldInfoV2] | dict[str, ModelField]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `type[BaseModel \| BaseModelV1] \| BaseModel \| BaseModelV1` | Yes | The Pydantic model or instance. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/pydantic.py#L330)
