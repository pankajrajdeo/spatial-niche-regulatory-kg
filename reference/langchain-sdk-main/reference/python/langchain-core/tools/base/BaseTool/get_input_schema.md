---
title: "get_input_schema"
description: "The tool's input schema."
source: "https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/get_input_schema"
category: "reference"
tags: [reference, langchain-core, tools, base, basetool, get_input_schema]
---

# get_input_schema

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/get_input_schema)

The tool's input schema.

## Signature

```python
get_input_schema(
    self,
    config: RunnableConfig | None = None,
) -> TypeBaseModel
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | No | The configuration for the tool. (default: `None`) |

## Returns

`TypeBaseModel`

The input schema for the tool.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/base.py#L740)
