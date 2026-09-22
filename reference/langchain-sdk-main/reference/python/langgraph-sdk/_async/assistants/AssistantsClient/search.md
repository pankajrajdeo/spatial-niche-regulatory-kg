---
title: "search"
description: "Search for assistants."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/assistants/AssistantsClient/search"
category: "reference"
tags: [reference, langgraph-sdk, async, assistants, assistantsclient, search]
---

# search

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/assistants/AssistantsClient/search)

Search for assistants.

## Signature

```python
search(
    self,
    *,
    metadata: Json = None,
    graph_id: str | None = None,
    name: str | None = None,
    limit: int = 10,
    offset: int = 0,
    sort_by: AssistantSortBy | None = None,
    sort_order: SortOrder | None = None,
    select: list[AssistantSelectField] | None = None,
    response_format: Literal['array', 'object'] = 'array',
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> AssistantsSearchResponse | list[Assistant]
```

## Description

???+ example "Example Usage"

```python
client = get_client(url="http://localhost:2024")
response = await client.assistants.search(
    metadata = {"name":"my_name"},
    graph_id="my_graph_id",
    limit=5,
    offset=5,
    response_format="object"
)
next_cursor = response["next"]
assistants = response["assistants"]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `metadata` | `Json` | No | Metadata to filter by. Exact match filter for each KV pair. (default: `None`) |
| `graph_id` | `str \| None` | No | The ID of the graph to filter by. The graph ID is normally set in your langgraph.json configuration. (default: `None`) |
| `name` | `str \| None` | No | The name of the assistant to filter by. The filtering logic will match assistants where 'name' is a substring (case insensitive) of the assistant name. (default: `None`) |
| `limit` | `int` | No | The maximum number of results to return. (default: `10`) |
| `offset` | `int` | No | The number of results to skip. (default: `0`) |
| `sort_by` | `AssistantSortBy \| None` | No | The field to sort by. (default: `None`) |
| `sort_order` | `SortOrder \| None` | No | The order to sort by. (default: `None`) |
| `select` | `list[AssistantSelectField] \| None` | No | Specific assistant fields to include in the response. (default: `None`) |
| `response_format` | `Literal['array', 'object']` | No | Controls the response shape. Use `"array"` (default) to return a bare list of assistants, or `"object"` to return a mapping containing assistants plus pagination metadata. Defaults to "array", though this default will be changed to "object" in a future release. (default: `'array'`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`AssistantsSearchResponse | list[Assistant]`

A list of assistants (when `response_format="array"`) or a mapping

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/assistants.py#L528)
