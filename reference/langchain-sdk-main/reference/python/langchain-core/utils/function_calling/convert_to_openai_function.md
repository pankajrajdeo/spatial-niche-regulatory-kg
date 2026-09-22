---
title: "convert_to_openai_function"
description: "Convert a raw function/class to an OpenAI function."
source: "https://reference.langchain.com/python/langchain-core/utils/function_calling/convert_to_openai_function"
category: "reference"
tags: [reference, langchain-core, utils, function_calling, convert_to_openai_function]
---

# convert_to_openai_function

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/function_calling/convert_to_openai_function)

Convert a raw function/class to an OpenAI function.

## Signature

```python
convert_to_openai_function(
    function: Mapping[str, Any] | type | Callable[..., Any] | BaseTool,
    *,
    strict: bool | None = None,
) -> dict[str, Any]
```

## Description

!!! warning "Behavior changed in `langchain-core` 0.3.16"

`description` and `parameters` keys are now optional. Only `name` is
required and guaranteed to be part of the output.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `function` | `Mapping[str, Any] \| type \| Callable[..., Any] \| BaseTool` | Yes | A dictionary, Pydantic `BaseModel` class, `TypedDict` class, a LangChain `Tool` object, or a Python function.  If a dictionary is passed in, it is assumed to already be a valid OpenAI function, a JSON schema with top-level `title` key specified, an Anthropic format tool, or an Amazon Bedrock Converse format tool. |
| `strict` | `bool \| None` | No | If `True`, model output is guaranteed to exactly match the JSON Schema provided in the function definition.  If `None`, `strict` argument will not be included in function definition. (default: `None`) |

## Returns

`dict[str, Any]`

A dict version of the passed in function which is compatible with the OpenAI
function-calling API.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/function_calling.py#L377)
