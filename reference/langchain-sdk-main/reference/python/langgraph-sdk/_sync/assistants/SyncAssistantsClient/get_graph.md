---
title: "get_graph"
description: "Get the graph of an assistant by ID."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/assistants/SyncAssistantsClient/get_graph"
category: "reference"
tags: [reference, langgraph-sdk, sync, assistants, syncassistantsclient, get_graph]
---

# get_graph

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/assistants/SyncAssistantsClient/get_graph)

Get the graph of an assistant by ID.

## Signature

```python
get_graph(
    self,
    assistant_id: str,
    *,
    xray: int | bool = False,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> dict[str, list[dict[str, Any]]]
```

## Description

???+ example "Example Usage"

```python
client = get_sync_client(url="http://localhost:2024")
graph_info = client.assistants.get_graph(
    assistant_id="my_assistant_id"
)
print(graph_info)

--------------------------------------------------------------------------------------------------------------------------

{
    'nodes':
        [
            {'id': '__start__', 'type': 'schema', 'data': '__start__'},
            {'id': '__end__', 'type': 'schema', 'data': '__end__'},
            {'id': 'agent','type': 'runnable','data': {'id': ['langgraph', 'utils', 'RunnableCallable'],'name': 'agent'}},
        ],
    'edges':
        [
            {'source': '__start__', 'target': 'agent'},
            {'source': 'agent','target': '__end__'}
        ]
}
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `assistant_id` | `str` | Yes | The ID of the assistant to get the graph of. |
| `xray` | `int \| bool` | No | Include graph representation of subgraphs. If an integer value is provided, only subgraphs with a depth less than or equal to the value will be included. (default: `False`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`dict[str, list[dict[str, Any]]]`

The graph information for the assistant in JSON format.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/assistants.py#L92)
