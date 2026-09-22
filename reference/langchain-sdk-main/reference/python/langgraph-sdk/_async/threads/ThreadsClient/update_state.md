---
title: "update_state"
description: "Update the state of a thread."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/update_state"
category: "reference"
tags: [reference, langgraph-sdk, async, threads, threadsclient, update_state]
---

# update_state

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/threads/ThreadsClient/update_state)

Update the state of a thread.

## Signature

```python
update_state(
    self,
    thread_id: str,
    values: dict[str, Any] | Sequence[dict] | None,
    *,
    as_node: str | None = None,
    checkpoint: Checkpoint | None = None,
    checkpoint_id: str | None = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> ThreadUpdateStateResponse
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024)
response = await client.threads.update_state(
    thread_id="my_thread_id",
    values={"messages":[{"role": "user", "content": "hello!"}]},
    as_node="my_node",
)
print(response)
```
```shell

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

{
    'checkpoint': {
        'thread_id': 'e2496803-ecd5-4e0c-a779-3226296181c2',
        'checkpoint_ns': '',
        'checkpoint_id': '1ef4a9b8-e6fb-67b1-8001-abd5184439d1',
        'checkpoint_map': {}
    }
}
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thread_id` | `str` | Yes | The ID of the thread to update. |
| `values` | `dict[str, Any] \| Sequence[dict] \| None` | Yes | The values to update the state with. |
| `as_node` | `str \| None` | No | Update the state as if this node had just executed. (default: `None`) |
| `checkpoint` | `Checkpoint \| None` | No | The checkpoint to update the state of. (default: `None`) |
| `checkpoint_id` | `str \| None` | No | (deprecated) The checkpoint ID to update the state of. (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`ThreadUpdateStateResponse`

Response after updating a thread's state.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/threads.py#L621)
