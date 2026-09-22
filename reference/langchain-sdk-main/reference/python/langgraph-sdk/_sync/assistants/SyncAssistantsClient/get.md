---
title: "get"
description: "Get an assistant by ID."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/assistants/SyncAssistantsClient/get"
category: "reference"
tags: [reference, langgraph-sdk, sync, assistants, syncassistantsclient, get]
---

# get

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/assistants/SyncAssistantsClient/get)

Get an assistant by ID.

## Signature

```python
get(
    self,
    assistant_id: str,
    *,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> Assistant
```

## Description

???+ example "Example Usage"

```python
assistant = client.assistants.get(
    assistant_id="my_assistant_id"
)
print(assistant)
```

```shell
----------------------------------------------------

{
    'assistant_id': 'my_assistant_id',
    'graph_id': 'agent',
    'created_at': '2024-06-25T17:10:33.109781+00:00',
    'updated_at': '2024-06-25T17:10:33.109781+00:00',
    'config': {},
    'context': {},
    'metadata': {'created_by': 'system'}
}
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `assistant_id` | `str` | Yes | The ID of the assistant to get OR the name of the graph (to use the default assistant). |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`Assistant`

`Assistant` Object.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/assistants.py#L45)
