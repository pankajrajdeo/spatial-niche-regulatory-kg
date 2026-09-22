---
title: "convert_runnable_to_tool"
description: "Convert a Runnable into a BaseTool."
source: "https://reference.langchain.com/python/langchain-core/tools/convert/convert_runnable_to_tool"
category: "reference"
tags: [reference, langchain-core, tools, convert, convert_runnable_to_tool]
---

# convert_runnable_to_tool

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/convert/convert_runnable_to_tool)

Convert a `Runnable` into a `BaseTool`.

## Signature

```python
convert_runnable_to_tool(
    runnable: Runnable[Any, Any],
    args_schema: TypeBaseModel | None = None,
    *,
    name: str | None = None,
    description: str | None = None,
    arg_types: dict[str, type] | None = None,
) -> BaseTool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `runnable` | `Runnable[Any, Any]` | Yes | The `Runnable` to convert. |
| `args_schema` | `TypeBaseModel \| None` | No | The schema for the tool's input arguments. (default: `None`) |
| `name` | `str \| None` | No | The name of the tool. (default: `None`) |
| `description` | `str \| None` | No | The description of the tool. (default: `None`) |
| `arg_types` | `dict[str, type] \| None` | No | The types of the arguments. (default: `None`) |

## Returns

`BaseTool`

The tool.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/convert.py#L433)
