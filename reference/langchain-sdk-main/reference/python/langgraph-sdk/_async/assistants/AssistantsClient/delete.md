---
title: "delete"
description: "Delete an assistant."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/assistants/AssistantsClient/delete"
category: "reference"
tags: [reference, langgraph-sdk, async, assistants, assistantsclient, delete]
---

# delete

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/assistants/AssistantsClient/delete)

Delete an assistant.

## Signature

```python
delete(
    self,
    assistant_id: str,
    *,
    delete_threads: bool = False,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> None
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024")
await client.assistants.delete(
    assistant_id="my_assistant_id"
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `assistant_id` | `str` | Yes | The assistant ID to delete. |
| `delete_threads` | `bool` | No | If true, delete all threads with `metadata.assistant_id` matching this assistant, along with runs and checkpoints belonging to those threads. (default: `False`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`None`

`None`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/assistants.py#L452)
