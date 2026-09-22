---
title: "list_namespaces"
description: "List namespaces with optional match conditions."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/store/StoreClient/list_namespaces"
category: "reference"
tags: [reference, langgraph-sdk, async, store, storeclient, list_namespaces]
---

# list_namespaces

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/store/StoreClient/list_namespaces)

List namespaces with optional match conditions.

## Signature

```python
list_namespaces(
    self,
    prefix: list[str] | None = None,
    suffix: list[str] | None = None,
    max_depth: int | None = None,
    limit: int = 100,
    offset: int = 0,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> ListNamespaceResponse
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024")
namespaces = await client.store.list_namespaces(
    prefix=["documents"],
    max_depth=3,
    limit=10,
    offset=0
)
print(namespaces)

----------------------------------------------------------------

[
    ["documents", "user123", "reports"],
    ["documents", "user456", "invoices"],
    ...
]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `prefix` | `list[str] \| None` | No | Optional list of strings representing the prefix to filter namespaces. (default: `None`) |
| `suffix` | `list[str] \| None` | No | Optional list of strings representing the suffix to filter namespaces. (default: `None`) |
| `max_depth` | `int \| None` | No | Optional integer specifying the maximum depth of namespaces to return. (default: `None`) |
| `limit` | `int` | No | Maximum number of namespaces to return (default is 100). (default: `100`) |
| `offset` | `int` | No | Number of namespaces to skip before returning results (default is 0). (default: `0`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`ListNamespaceResponse`

A list of namespaces matching the criteria.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/store.py#L256)
