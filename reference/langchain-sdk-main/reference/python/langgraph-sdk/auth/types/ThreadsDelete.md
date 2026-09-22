---
title: "ThreadsDelete"
description: "Parameters for deleting a thread."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/ThreadsDelete"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, threadsdelete]
---

# ThreadsDelete

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/ThreadsDelete)

Parameters for deleting a thread.

Called for deletes to a thread, thread version, or run

## Signature

```python
ThreadsDelete()
```

## Extends

- `typing.TypedDict`

## Constructors

```python
__init__(
    thread_id: UUID,
    run_id: UUID | None,
)
```

| Name | Type |
|------|------|
| `thread_id` | `UUID` |
| `run_id` | `UUID \| None` |

## Properties

- `thread_id`
- `run_id`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/auth/types.py#L502)
