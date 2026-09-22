---
title: "model_validate"
description: "Validate obj against a Pydantic model class of either major version."
source: "https://reference.langchain.com/python/langchain-core/utils/pydantic/model_validate"
category: "reference"
tags: [reference, langchain-core, utils, pydantic, model_validate]
---

# model_validate

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/pydantic/model_validate)

Validate `obj` against a Pydantic model class of either major version.

Dispatches to the correct method for Pydantic v1 (`parse_obj`) or v2
(`model_validate`), so callers holding a `TypeBaseModel` don't have to
branch on the model's version themselves.

## Signature

```python
model_validate(
    model: TypeBaseModel,
    obj: Any,
) -> PydanticBaseModel
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `TypeBaseModel` | Yes | The Pydantic model class to validate against. |
| `obj` | `Any` | Yes | The object to validate. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/pydantic.py#L372)
