---
title: "SyncRunModule"
description: "Command dispatcher for run.start."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/stream/SyncRunModule"
category: "reference"
tags: [reference, langgraph-sdk, sync, stream, syncrunmodule]
---

# SyncRunModule

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/stream/SyncRunModule)

Command dispatcher for `run.start`.

Bound to one `SyncThreadStream`; accesses its transport and id allocator.

## Signature

```python
SyncRunModule(
    self,
    owner: SyncThreadStream,
)
```

## Constructors

```python
__init__(
    self,
    owner: SyncThreadStream,
) -> None
```

| Name | Type |
|------|------|
| `owner` | `SyncThreadStream` |

## Methods

- [`start()`](https://reference.langchain.com/python/langgraph-sdk/_sync/stream/SyncRunModule/start)
- [`respond()`](https://reference.langchain.com/python/langgraph-sdk/_sync/stream/SyncRunModule/respond)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_sync/stream.py#L203)
