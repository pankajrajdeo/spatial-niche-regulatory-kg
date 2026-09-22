---
title: "node_data_json"
description: "Convert the data of a node to a JSON-serializable format."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph/node_data_json"
category: "reference"
tags: [reference, langchain-core, runnables, graph, node_data_json]
---

# node_data_json

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph/node_data_json)

Convert the data of a node to a JSON-serializable format.

## Signature

```python
node_data_json(
    node: Node,
    *,
    with_schemas: bool = False,
) -> dict[str, str | dict[str, Any]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `node` | `Node` | Yes | The `Node` to convert. |
| `with_schemas` | `bool` | No | Whether to include the schema of the data if it is a Pydantic model. (default: `False`) |

## Returns

`dict[str, str | dict[str, Any]]`

A dictionary with the type of the data and the data itself.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/graph.py#L199)
