---
title: "ThreadsUpdate"
description: "Parameters for updating a thread or run."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/ThreadsUpdate"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, threadsupdate]
---

# ThreadsUpdate

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/ThreadsUpdate)

Parameters for updating a thread or run.

Called for updates to a thread, thread version, or run
cancellation.

## Signature

```python
ThreadsUpdate()
```

## Extends

- `typing.TypedDict`

## Constructors

```python
__init__(
    thread_id: UUID,
    metadata: MetadataInput,
    action: typing.Literal['interrupt', 'rollback'] | None,
)
```

| Name | Type |
|------|------|
| `thread_id` | `UUID` |
| `metadata` | `MetadataInput` |
| `action` | `typing.Literal['interrupt', 'rollback'] \| None` |

## Properties

- `thread_id`
- `metadata`
- `action`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/auth/types.py#L485)
