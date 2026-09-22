---
title: "from_schema_spec"
description: "Create an OutputToolBinding instance from a SchemaSpec."
source: "https://reference.langchain.com/python/langchain/agents/structured_output/OutputToolBinding/from_schema_spec"
category: "reference"
tags: [reference, langchain, agents, structured_output, outputtoolbinding, from_schema_spec]
---

# from_schema_spec

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/structured_output/OutputToolBinding/from_schema_spec)

Create an `OutputToolBinding` instance from a `SchemaSpec`.

## Signature

```python
from_schema_spec(
    cls,
    schema_spec: _SchemaSpec[SchemaT],
) -> Self
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `schema_spec` | `_SchemaSpec[SchemaT]` | Yes | The `SchemaSpec` to convert |

## Returns

`Self`

An `OutputToolBinding` instance with the appropriate tool created

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/structured_output.py#L337)
