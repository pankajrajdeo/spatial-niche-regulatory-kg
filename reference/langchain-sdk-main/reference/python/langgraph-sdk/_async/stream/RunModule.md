---
title: "RunModule"
description: "Command dispatcher for run.start."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/stream/RunModule"
category: "reference"
tags: [reference, langgraph-sdk, async, stream, runmodule]
---

# RunModule

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/stream/RunModule)

Command dispatcher for `run.start`.

Bound to one `AsyncThreadStream`; accesses its transport and id allocator.

## Signature

```python
RunModule(
    self,
    owner: AsyncThreadStream,
)
```

## Constructors

```python
__init__(
    self,
    owner: AsyncThreadStream,
) -> None
```

| Name | Type |
|------|------|
| `owner` | `AsyncThreadStream` |

## Methods

- [`start()`](https://reference.langchain.com/python/langgraph-sdk/_async/stream/RunModule/start)
- [`respond()`](https://reference.langchain.com/python/langgraph-sdk/_async/stream/RunModule/respond)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/_async/stream.py#L160)
