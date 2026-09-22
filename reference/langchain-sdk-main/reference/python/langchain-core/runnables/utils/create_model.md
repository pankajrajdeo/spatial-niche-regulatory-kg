---
title: "create_model"
description: "Create a Pydantic model with the given field definitions."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/create_model"
category: "reference"
tags: [reference, langchain-core, runnables, utils, create_model]
---

# create_model

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/pydantic/create_model)

Create a Pydantic model with the given field definitions.

Please use `create_model_v2` instead of this function.

## Signature

```python
create_model(
    model_name: str,
    module_name: str | None = None,
    /,
    **field_definitions: Any = {},
) -> type[BaseModel]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model_name` | `str` | Yes | The name of the model. |
| `module_name` | `str \| None` | No | The name of the module where the model is defined.  This is used by Pydantic to resolve any forward references. (default: `None`) |
| `**field_definitions` | `Any` | No | The field definitions for the model. (default: `{}`) |

## Returns

`type[BaseModel]`

The created model.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/pydantic.py#L484)
