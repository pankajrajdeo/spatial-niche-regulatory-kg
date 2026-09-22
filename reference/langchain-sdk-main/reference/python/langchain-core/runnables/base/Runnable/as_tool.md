---
title: "as_tool"
description: "Create a BaseTool from a Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/as_tool"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, as_tool]
---

# as_tool

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/as_tool)

Create a `BaseTool` from a `Runnable`.

`as_tool` will instantiate a `BaseTool` with a name, description, and
`args_schema` from a `Runnable`. Where possible, schemas are inferred
from `runnable.get_input_schema`.

Alternatively (e.g., if the `Runnable` takes a dict as input and the specific
`dict` keys are not typed), the schema can be specified directly with
`args_schema`.

You can also pass `arg_types` to just specify the required arguments and their
types.

## Signature

```python
as_tool(
    self,
    args_schema: type[BaseModel] | None = None,
    *,
    name: str | None = None,
    description: str | None = None,
    arg_types: dict[str, type] | None = None,
) -> BaseTool
```

## Description

!!! example "`TypedDict` input"

```python
    from typing_extensions import TypedDict
    from langchain_core.runnables import RunnableLambda

    class Args(TypedDict):
        a: int
        b: list[int]

    def f(x: Args) -> str:
        return str(x["a"] * max(x["b"]))

    runnable = RunnableLambda(f)
    as_tool = runnable.as_tool()
    as_tool.invoke({"a": 3, "b": [1, 2]})
```

!!! example "`dict` input, specifying schema via `args_schema`"

```python
    from typing import Any
    from pydantic import BaseModel, Field
    from langchain_core.runnables import RunnableLambda

    def f(x: dict[str, Any]) -> str:
        return str(x["a"] * max(x["b"]))

    class FSchema(BaseModel):
        """Apply a function to an integer and list of integers."""

        a: int = Field(..., description="Integer")
        b: list[int] = Field(..., description="List of ints")

    runnable = RunnableLambda(f)
    as_tool = runnable.as_tool(FSchema)
    as_tool.invoke({"a": 3, "b": [1, 2]})
```

!!! example "`dict` input, specifying schema via `arg_types`"

```python
    from typing import Any
    from langchain_core.runnables import RunnableLambda

    def f(x: dict[str, Any]) -> str:
        return str(x["a"] * max(x["b"]))

    runnable = RunnableLambda(f)
    as_tool = runnable.as_tool(arg_types={"a": int, "b": list[int]})
    as_tool.invoke({"a": 3, "b": [1, 2]})
```

!!! example "`str` input"

```python
    from langchain_core.runnables import RunnableLambda

    def f(x: str) -> str:
        return x + "a"

    def g(x: str) -> str:
        return x + "z"

    runnable = RunnableLambda(f) | g
    as_tool = runnable.as_tool()
    as_tool.invoke("b")
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `args_schema` | `type[BaseModel] \| None` | No | The schema for the tool. (default: `None`) |
| `name` | `str \| None` | No | The name of the tool. (default: `None`) |
| `description` | `str \| None` | No | The description of the tool. (default: `None`) |
| `arg_types` | `dict[str, type] \| None` | No | A dictionary of argument names to types. (default: `None`) |

## Returns

`BaseTool`

A `BaseTool` instance.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L2707)
