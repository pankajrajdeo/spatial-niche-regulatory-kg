---
title: "from_function"
description: "Initialize tool from a function."
source: "https://reference.langchain.com/python/langchain-core/tools/simple/Tool/from_function"
category: "reference"
tags: [reference, langchain-core, tools, simple, tool, from_function]
---

# from_function

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/simple/Tool/from_function)

Initialize tool from a function.

## Signature

```python
from_function(
    cls,
    func: Callable[..., Any] | None,
    name: str,
    description: str,
    return_direct: bool = False,
    args_schema: ArgsSchema | None = None,
    coroutine: Callable[..., Awaitable[Any]] | None = None,
    **kwargs: Any = {},
) -> Tool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Callable[..., Any] \| None` | Yes | The function to create the tool from. |
| `name` | `str` | Yes | The name of the tool. |
| `description` | `str` | Yes | The description of the tool. |
| `return_direct` | `bool` | No | Whether to return the output directly. (default: `False`) |
| `args_schema` | `ArgsSchema \| None` | No | The schema of the tool's input arguments. (default: `None`) |
| `coroutine` | `Callable[..., Awaitable[Any]] \| None` | No | The asynchronous version of the function. (default: `None`) |
| `**kwargs` | `Any` | No | Additional arguments to pass to the tool. (default: `{}`) |

## Returns

`Tool`

The tool.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/simple.py#L168)
