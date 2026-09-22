---
title: "parse"
description: "Parse tool arguments according to the schema."
source: "https://reference.langchain.com/python/langchain/agents/structured_output/OutputToolBinding/parse"
category: "reference"
tags: [reference, langchain, agents, structured_output, outputtoolbinding, parse]
---

# parse

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/structured_output/OutputToolBinding/parse)

Parse tool arguments according to the schema.

## Signature

```python
parse(
    self,
    tool_args: dict[str, Any],
) -> SchemaT | dict[str, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tool_args` | `dict[str, Any]` | Yes | The arguments from the tool call |

## Returns

`SchemaT | dict[str, Any]`

The parsed response according to the schema type

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/structured_output.py#L357)
