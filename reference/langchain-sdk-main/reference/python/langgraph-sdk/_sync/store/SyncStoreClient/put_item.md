---
title: "put_item"
description: "Store or update an item."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/store/SyncStoreClient/put_item"
category: "reference"
tags: [reference, langgraph-sdk, sync, store, syncstoreclient, put_item]
---

# put_item

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/store/SyncStoreClient/put_item)

Store or update an item.

## Signature

```python
put_item(
    self,
    namespace: Sequence[str],
    /,
    key: str,
    value: Mapping[str, Any],
    index: Literal[False] | list[str] | None = None,
    ttl: int | None = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> None
```

## Description

???+ example "Example Usage"

```python
client = get_sync_client(url="http://localhost:8123")
client.store.put_item(
    ["documents", "user123"],
    key="item456",
    value={"title": "My Document", "content": "Hello World"}
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `namespace` | `Sequence[str]` | Yes | A list of strings representing the namespace path. |
| `key` | `str` | Yes | The unique identifier for the item within the namespace. |
| `value` | `Mapping[str, Any]` | Yes | A dictionary containing the item's data. |
| `index` | `Literal[False] \| list[str] \| None` | No | Controls search indexing - None (use defaults), False (disable), or list of field paths to index. (default: `None`) |
| `ttl` | `int \| None` | No | Optional time-to-live in minutes for the item, or None for no expiration. (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`None`

`None`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/store.py#L35)
