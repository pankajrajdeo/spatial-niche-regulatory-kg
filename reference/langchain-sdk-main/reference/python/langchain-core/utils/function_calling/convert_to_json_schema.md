---
title: "convert_to_json_schema"
description: "Convert a schema representation to a JSON schema."
source: "https://reference.langchain.com/python/langchain-core/utils/function_calling/convert_to_json_schema"
category: "reference"
tags: [reference, langchain-core, utils, function_calling, convert_to_json_schema]
---

# convert_to_json_schema

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/function_calling/convert_to_json_schema)

Convert a schema representation to a JSON schema.

## Signature

```python
convert_to_json_schema(
    schema: dict[str, Any] | type[BaseModel] | Callable[..., Any] | BaseTool,
    *,
    strict: bool | None = None,
) -> dict[str, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `schema` | `dict[str, Any] \| type[BaseModel] \| Callable[..., Any] \| BaseTool` | Yes | The schema to convert. |
| `strict` | `bool \| None` | No | If `True`, model output is guaranteed to exactly match the JSON Schema provided in the function definition.  If `None`, `strict` argument will not be included in function definition. (default: `None`) |

## Returns

`dict[str, Any]`

A JSON schema representation of the input schema.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/function_calling.py#L577)
