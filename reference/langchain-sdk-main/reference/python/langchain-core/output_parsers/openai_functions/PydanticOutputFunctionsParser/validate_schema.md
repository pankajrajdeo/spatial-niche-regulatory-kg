---
title: "validate_schema"
description: "Validate the Pydantic schema."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/openai_functions/PydanticOutputFunctionsParser/validate_schema"
category: "reference"
tags: [reference, langchain-core, output_parsers, openai_functions, pydanticoutputfunctionsparser, validate_schema]
---

# validate_schema

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/openai_functions/PydanticOutputFunctionsParser/validate_schema)

Validate the Pydantic schema.

## Signature

```python
validate_schema(
    cls,
    values: dict[str, Any],
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `values` | `dict[str, Any]` | Yes | The values to validate. |

## Returns

`Any`

The validated values.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/output_parsers/openai_functions.py#L229)
