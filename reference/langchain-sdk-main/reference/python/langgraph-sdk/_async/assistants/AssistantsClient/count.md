---
title: "count"
description: "Count assistants matching filters."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/assistants/AssistantsClient/count"
category: "reference"
tags: [reference, langgraph-sdk, async, assistants, assistantsclient, count]
---

# count

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/assistants/AssistantsClient/count)

Count assistants matching filters.

## Signature

```python
count(
    self,
    *,
    metadata: Json = None,
    graph_id: str | None = None,
    name: str | None = None,
    headers: Mapping[str, str] | None = None,
    params: QueryParamTypes | None = None,
) -> int
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `metadata` | `Json` | No | Metadata to filter by. Exact match for each key/value. (default: `None`) |
| `graph_id` | `str \| None` | No | Optional graph id to filter by. (default: `None`) |
| `name` | `str \| None` | No | Optional name to filter by. The filtering logic will match assistants where 'name' is a substring (case insensitive) of the assistant name. (default: `None`) |
| `headers` | `Mapping[str, str] \| None` | No | Optional custom headers to include with the request. (default: `None`) |
| `params` | `QueryParamTypes \| None` | No | Optional query parameters to include with the request. (default: `None`) |

## Returns

`int`

Number of assistants matching the criteria.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/assistants.py#L623)
