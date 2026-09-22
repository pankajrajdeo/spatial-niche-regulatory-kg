---
title: "aget_graph"
description: "Get graph by graph name."
source: "https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/aget_graph"
category: "reference"
tags: [reference, langgraph, pregel, remote, remotegraph, aget_graph]
---

# aget_graph

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/aget_graph)

Get graph by graph name.

This method calls `GET /assistants/{assistant_id}/graph`.

## Signature

```python
aget_graph(
    self,
    config: RunnableConfig | None = None,
    *,
    xray: int | bool = False,
    headers: dict[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> DrawableGraph
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | No | This parameter is not used. (default: `None`) |
| `xray` | `int \| bool` | No | Include graph representation of subgraphs. If an integer value is provided, only subgraphs with a depth less than or equal to the value will be included. (default: `False`) |

## Returns

`DrawableGraph`

The graph information for the assistant in JSON format.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/remote.py#L289)
