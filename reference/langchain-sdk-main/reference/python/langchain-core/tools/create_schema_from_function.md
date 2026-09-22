---
title: "create_schema_from_function"
description: "Create a Pydantic schema from a function's signature."
source: "https://reference.langchain.com/python/langchain-core/tools/create_schema_from_function"
category: "reference"
tags: [reference, langchain-core, tools, create_schema_from_function]
---

# create_schema_from_function

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/create_schema_from_function)

Create a Pydantic schema from a function's signature.

## Signature

```python
create_schema_from_function(
    model_name: str,
    func: Callable[..., Any],
    *,
    filter_args: Sequence[str] | None = None,
    parse_docstring: bool = False,
    error_on_invalid_docstring: bool = False,
    include_injected: bool = True,
) -> TypeBaseModel
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model_name` | `str` | Yes | Name to assign to the generated Pydantic schema. |
| `func` | `Callable[..., Any]` | Yes | Function to generate the schema from. |
| `filter_args` | `Sequence[str] \| None` | No | Optional list of arguments to exclude from the schema.  Defaults to `FILTERED_ARGS`. (default: `None`) |
| `parse_docstring` | `bool` | No | Whether to parse the function's docstring for descriptions for each argument. (default: `False`) |
| `error_on_invalid_docstring` | `bool` | No | If `parse_docstring` is provided, configure whether to raise `ValueError` on invalid Google Style docstrings. (default: `False`) |
| `include_injected` | `bool` | No | Whether to include injected arguments in the schema.  Defaults to `True`, since we want to include them in the schema when *validating* tool inputs. (default: `True`) |

## Returns

`TypeBaseModel`

A Pydantic model with the same arguments as the function.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/base.py#L263)
