---
title: "create"
description: "Create a new assistant."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/assistants/AssistantsClient/create"
category: "reference"
tags: [reference, langgraph-sdk, async, assistants, assistantsclient, create]
---

# create

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/assistants/AssistantsClient/create)

Create a new assistant.

Useful when graph is configurable and you want to create different assistants based on different configurations.

## Signature

```python
create(
    self,
    graph_id: str | None,
    config: Config | None = None,
    *,
    context: Context | None = None,
    metadata: Json = None,
    assistant_id: str | None = None,
    if_exists: OnConflictBehavior | None = None,
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
assistant = await client.assistants.create(
    graph_id="agent",
    context={"model_name": "openai"},
    metadata={"number":1},
    assistant_id="my-assistant-id",
    if_exists="do_nothing",
    name="my_name"
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph_id` | `str \| None` | Yes | The ID of the graph the assistant should use. The graph ID is normally set in your langgraph.json configuration. |
| `config` | `Config \| None` | No | Configuration to use for the graph. (default: `None`) |
| `metadata` | `Json` | No | Metadata to add to assistant. (default: `None`) |
| `context` | `Context \| None` | No | Static context to add to the assistant. !!! version-added "Added in version 0.6.0" (default: `None`) |
| `assistant_id` | `str \| None` | No | Assistant ID to use, will default to a random UUID if not provided. (default: `None`) |
| `if_exists` | `OnConflictBehavior \| None` | No | How to handle duplicate creation. Defaults to 'raise' under the hood. Must be either 'raise' (raise error if duplicate), or 'do_nothing' (return existing assistant). (default: `None`) |
| `name` | `str \| None` | No | The name of the assistant. Defaults to 'Untitled' under the hood. (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `description` | `str \| None` | No | Optional description of the assistant. The description field is available for langgraph-api server version>=0.0.45 (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`Assistant`

The created assistant.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/assistants.py#L314)
