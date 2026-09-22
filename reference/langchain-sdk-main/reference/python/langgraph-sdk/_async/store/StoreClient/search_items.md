---
title: "search_items"
description: "Search for items within a namespace prefix."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/store/StoreClient/search_items"
category: "reference"
tags: [reference, langgraph-sdk, async, store, storeclient, search_items]
---

# search_items

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/store/StoreClient/search_items)

Search for items within a namespace prefix.

## Signature

```python
search_items(
    self,
    namespace_prefix: Sequence[str],
    /,
    filter: Mapping[str, Any] | None = None,
    limit: int = 10,
    offset: int = 0,
    query: str | None = None,
    refresh_ttl: bool | None = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> SearchItemsResponse
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024")
items = await client.store.search_items(
    ["documents"],
    filter={"author": "John Doe"},
    limit=5,
    offset=0
)
print(items)
```
```shell

----------------------------------------------------------------

{
    "items": [
        {
            "namespace": ["documents", "user123"],
            "key": "item789",
            "value": {
                "title": "Another Document",
                "author": "John Doe"
            },
            "created_at": "2024-07-30T12:00:00Z",
            "updated_at": "2024-07-30T12:00:00Z"
        },
        # ... additional items ...
    ]
}
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `namespace_prefix` | `Sequence[str]` | Yes | List of strings representing the namespace prefix. |
| `filter` | `Mapping[str, Any] \| None` | No | Optional dictionary of key-value pairs to filter results. (default: `None`) |
| `limit` | `int` | No | Maximum number of items to return (default is 10). (default: `10`) |
| `offset` | `int` | No | Number of items to skip before returning results (default is 0). (default: `0`) |
| `query` | `str \| None` | No | Optional query for natural language search. (default: `None`) |
| `refresh_ttl` | `bool \| None` | No | Whether to refresh the TTL on items returned by this search. If `None`, uses the store's default behavior. (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`SearchItemsResponse`

A list of items matching the search criteria.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/store.py#L180)
