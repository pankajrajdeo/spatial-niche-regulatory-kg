---
title: "model_json_schema"
description: "Return the JSON schema of a Pydantic model class of either major version."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/model_json_schema"
category: "reference"
tags: [reference, langchain-core, runnables, base, model_json_schema]
---

# model_json_schema

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/pydantic/model_json_schema)

Return the JSON schema of a Pydantic model class of either major version.

Dispatches to the correct method for Pydantic v1 (`schema`) or v2
(`model_json_schema`), so callers holding a `TypeBaseModel` don't have to
branch on the model's version themselves.

## Signature

```python
model_json_schema(
    model: TypeBaseModel,
) -> dict[str, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `TypeBaseModel` | Yes | The Pydantic model class. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/pydantic.py#L351)
