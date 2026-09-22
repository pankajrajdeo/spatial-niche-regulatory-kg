---
title: "BaseTool"
description: "Base class for all LangChain tools."
source: "https://reference.langchain.com/python/langchain-core/tools/base/BaseTool"
category: "reference"
tags: [reference, langchain-core, tools, base, basetool]
---

# BaseTool

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool)

Base class for all LangChain tools.

This abstract class defines the interface that all LangChain tools must implement.

Tools are components that can be called by agents to perform specific actions.

## Signature

```python
BaseTool(
    self,
    **kwargs: Any = {},
)
```

## Extends

- `RunnableSerializable[str | dict[str, Any] | ToolCall, Any]`

## Constructors

```python
__init__(
    self,
    **kwargs: Any = {},
) -> None
```

## Properties

- `name`
- `description`
- `args_schema`
- `return_direct`
- `verbose`
- `callbacks`
- `tags`
- `metadata`
- `handle_tool_error`
- `handle_validation_error`
- `response_format`
- `extras`
- `model_config`
- `is_single_input`
- `args`
- `tool_call_schema`

## Methods

- [`model_copy()`](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/model_copy)
- [`get_input_schema()`](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/get_input_schema)
- [`invoke()`](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/ainvoke)
- [`run()`](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/run)
- [`arun()`](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/arun)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/base.py#L433)
