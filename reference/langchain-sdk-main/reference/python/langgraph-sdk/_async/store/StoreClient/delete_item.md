---
title: "delete_item"
description: "Delete an item."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/store/StoreClient/delete_item"
category: "reference"
tags: [reference, langgraph-sdk, async, store, storeclient, delete_item]
---

# delete_item

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/store/StoreClient/delete_item)

Delete an item.

## Signature

```python
delete_item(
    self,
    namespace: Sequence[str],
    /,
    key: str,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> None
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024")
await client.store.delete_item(
    ["documents", "user123"],
    key="item456",
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | `str` | Yes | The unique identifier for the item. |
| `namespace` | `Sequence[str]` | Yes | Optional list of strings representing the namespace path. |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`None`

`None`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/store.py#L144)
