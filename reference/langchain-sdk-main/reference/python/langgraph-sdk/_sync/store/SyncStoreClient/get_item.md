---
title: "get_item"
description: "Retrieve a single item."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/store/SyncStoreClient/get_item"
category: "reference"
tags: [reference, langgraph-sdk, sync, store, syncstoreclient, get_item]
---

# get_item

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/store/SyncStoreClient/get_item)

Retrieve a single item.

## Signature

```python
get_item(
    self,
    namespace: Sequence[str],
    /,
    key: str,
    *,
    refresh_ttl: bool | None = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> Item
```

## Description

???+ example "Example Usage"

```python
client = get_sync_client(url="http://localhost:8123")
item = client.store.get_item(
    ["documents", "user123"],
    key="item456",
)
print(item)
```

```shell
----------------------------------------------------------------

{
    'namespace': ['documents', 'user123'],
    'key': 'item456',
    'value': {'title': 'My Document', 'content': 'Hello World'},
    'created_at': '2024-07-30T12:00:00Z',
    'updated_at': '2024-07-30T12:00:00Z'
}
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | `str` | Yes | The unique identifier for the item. |
| `namespace` | `Sequence[str]` | Yes | Optional list of strings representing the namespace path. |
| `refresh_ttl` | `bool \| None` | No | Whether to refresh the TTL on this read operation. If `None`, uses the store's default behavior. (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |

## Returns

`Item`

The retrieved item.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/store.py#L87)
