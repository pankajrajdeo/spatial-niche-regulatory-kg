---
title: "from_function"
description: "Create tool from a given function."
source: "https://reference.langchain.com/python/langchain-core/tools/structured/StructuredTool/from_function"
category: "reference"
tags: [reference, langchain-core, tools, structured, structuredtool, from_function]
---

# from_function

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/structured/StructuredTool/from_function)

Create tool from a given function.

A classmethod that helps to create a tool from a function.

## Signature

```python
from_function(
    cls,
    func: Callable[..., Any] | None = None,
    coroutine: Callable[..., Awaitable[Any]] | None = None,
    name: str | None = None,
    description: str | None = None,
    return_direct: bool = False,
    args_schema: ArgsSchema | None = None,
    infer_schema: bool = True,
    *,
    response_format: Literal['content', 'content_and_artifact'] = 'content',
    parse_docstring: bool = False,
    error_on_invalid_docstring: bool = False,
    **kwargs: Any = {},
) -> StructuredTool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Callable[..., Any] \| None` | No | The function from which to create a tool. (default: `None`) |
| `coroutine` | `Callable[..., Awaitable[Any]] \| None` | No | The async function from which to create a tool. (default: `None`) |
| `name` | `str \| None` | No | The name of the tool.  Defaults to the function name. (default: `None`) |
| `description` | `str \| None` | No | The description of the tool.  Defaults to the function docstring. (default: `None`) |
| `return_direct` | `bool` | No | Whether to return the result directly or as a callback. (default: `False`) |
| `args_schema` | `ArgsSchema \| None` | No | The schema of the tool's input arguments. (default: `None`) |
| `infer_schema` | `bool` | No | Whether to infer the schema from the function's signature. (default: `True`) |
| `response_format` | `Literal['content', 'content_and_artifact']` | No | The tool response format.  If `'content'` then the output of the tool is interpreted as the contents of a `ToolMessage`. If `'content_and_artifact'` then the output is expected to be a two-tuple corresponding to the `(content, artifact)` of a `ToolMessage`. (default: `'content'`) |
| `parse_docstring` | `bool` | No | If `infer_schema` and `parse_docstring`, will attempt to parse parameter descriptions from Google Style function docstrings. (default: `False`) |
| `error_on_invalid_docstring` | `bool` | No | if `parse_docstring` is provided, configure whether to raise `ValueError` on invalid Google Style docstrings. (default: `False`) |
| `**kwargs` | `Any` | No | Additional arguments to pass to the tool (default: `{}`) |

## Returns

`StructuredTool`

The tool.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/structured.py#L187)
