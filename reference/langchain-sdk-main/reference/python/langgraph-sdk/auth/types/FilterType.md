---
title: "FilterType"
description: "Type Alias in langgraph_sdk"
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/FilterType"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, filtertype]
---

# FilterType

> **Type Alias** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/FilterType)

Response type for authorization handlers.

## Signature

```python
FilterType = dict[str, str | dict[typing.Literal['$eq', '$contains'], str] | dict[typing.Literal['$contains'], list[str]]] | dict[str, str]
```

## Description

**Supports exact matches and operators:**

- Exact match shorthand: {"field": "value"}
- Exact match: {"field": {"$eq": "value"}}
- Contains (membership): {"field": {"$contains": "value"}}
- Contains (subset containment): {"field": {"$contains": ["value1", "value2"]}}

Subset containment is only supported by newer versions of the LangGraph dev server;
install langgraph-runtime-inmem >= 0.14.1 to use this filter variant.

???+ example "Examples"

    Simple exact match filter for the resource owner:

```python
    filter = {"owner": "user-abcd123"}
```

    Explicit version of the exact match filter:

```python
    filter = {"owner": {"$eq": "user-abcd123"}}
```

    Containment (membership of a single element):

```python
    filter = {"participants": {"$contains": "user-abcd123"}}
```

    Containment (subset containment; all values must be present, but order doesn't matter):

```python
    filter = {"participants": {"$contains": ["user-abcd123", "user-efgh456"]}}
```

    Combining filters (treated as a logical `AND`):

```python
    filter = {"owner": "user-abcd123", "participants": {"$contains": "user-efgh456"}}
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/auth/types.py#L58)
