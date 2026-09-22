---
title: "update"
description: "Update an assistant."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/assistants/AssistantsClient/update"
category: "reference"
tags: [reference, langgraph-sdk, async, assistants, assistantsclient, update]
---

# update

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/assistants/AssistantsClient/update)

Update an assistant.

Use this to point to a different graph, update the configuration, or change the metadata of an assistant.

## Signature

```python
update(
    self,
    assistant_id: str,
    *,
    graph_id: str | None = None,
    config: Config | None = None,
    context: Context | None = None,
    metadata: Json = None,
    name: str | None = None,
    headers: Mapping[str, str] | None = None,
    description: str | None = None,
    params: QueryParamTypes | None = None,
) -> Assistant
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024")
assistant = await client.assistants.update(
    assistant_id='e280dad7-8618-443f-87f1-8e41841c180f',
    graph_id="other-graph",
    context={"model_name": "anthropic"},
    metadata={"number":2}
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `assistant_id` | `str` | Yes | Assistant to update. |
| `graph_id` | `str \| None` | No | The ID of the graph the assistant should use. The graph ID is normally set in your langgraph.json configuration. If `None`, assistant will keep pointing to same graph. (default: `None`) |
| `config` | `Config \| None` | No | Configuration to use for the graph. (default: `None`) |
| `context` | `Context \| None` | No | Static context to add to the assistant. !!! version-added "Added in version 0.6.0" (default: `None`) |
| `metadata` | `Json` | No | Metadata to merge with existing assistant metadata. (default: `None`) |
| `name` | `str \| None` | No | The new name for the assistant. (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `description` | `str \| None` | No | Optional description of the assistant. The description field is available for langgraph-api server version>=0.0.45 (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`Assistant`

The updated assistant.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/assistants.py#L385)
