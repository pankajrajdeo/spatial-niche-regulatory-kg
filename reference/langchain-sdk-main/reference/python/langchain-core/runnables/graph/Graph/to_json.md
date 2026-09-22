---
title: "to_json"
description: "Convert the graph to a JSON-serializable format."
source: "https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/to_json"
category: "reference"
tags: [reference, langchain-core, runnables, graph, to_json]
---

# to_json

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/graph/Graph/to_json)

Convert the graph to a JSON-serializable format.

## Signature

```python
to_json(
    self,
    *,
    with_schemas: bool = False,
) -> dict[str, list[dict[str, Any]]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `with_schemas` | `bool` | No | Whether to include the schemas of the nodes if they are Pydantic models. (default: `False`) |

## Returns

`dict[str, list[dict[str, Any]]]`

A dictionary with the nodes and edges of the graph.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/graph.py#L266)
