---
title: "AssistantsSearch"
description: "Payload for searching assistants."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/AssistantsSearch"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, assistantssearch]
---

# AssistantsSearch

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/AssistantsSearch)

Payload for searching assistants.

???+ example "Examples"

```python
    search_params = {
        "graph_id": "graph123",
        "metadata": {"owner": "user123"},
        "limit": 10,
        "offset": 0
    }
```

## Signature

```python
AssistantsSearch()
```

## Extends

- `typing.TypedDict`

## Constructors

```python
__init__(
    graph_id: str | None,
    metadata: MetadataInput,
    limit: int,
    offset: int,
)
```

| Name | Type |
|------|------|
| `graph_id` | `str \| None` |
| `metadata` | `MetadataInput` |
| `limit` | `int` |
| `offset` | `int` |

## Properties

- `graph_id`
- `metadata`
- `limit`
- `offset`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/auth/types.py#L714)
