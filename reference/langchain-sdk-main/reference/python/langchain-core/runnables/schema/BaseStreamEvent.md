---
title: "BaseStreamEvent"
description: "Streaming event."
source: "https://reference.langchain.com/python/langchain-core/runnables/schema/BaseStreamEvent"
category: "reference"
tags: [reference, langchain-core, runnables, schema, basestreamevent]
---

# BaseStreamEvent

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/schema/BaseStreamEvent)

Streaming event.

Schema of a streaming event which is produced from the `astream_events` method.

## Signature

```python
BaseStreamEvent()
```

## Description

**Example:**

```python
from langchain_core.runnables import RunnableLambda

async def reverse(s: str) -> str:
    return s[::-1]

chain = RunnableLambda(func=reverse)

events = [event async for event in chain.astream_events("hello")]

# Will produce the following events
# (where some fields have been omitted for brevity):
[
    {
        "data": {"input": "hello"},
        "event": "on_chain_start",
        "metadata": {},
        "name": "reverse",
        "tags": [],
    },
    {
        "data": {"chunk": "olleh"},
        "event": "on_chain_stream",
        "metadata": {},
        "name": "reverse",
        "tags": [],
    },
    {
        "data": {"output": "olleh"},
        "event": "on_chain_end",
        "metadata": {},
        "name": "reverse",
        "tags": [],
    },
]
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    event: str,
    run_id: str,
    tags: NotRequired[list[str]],
    metadata: NotRequired[dict[str, Any]],
    parent_ids: Sequence[str],
)
```

| Name | Type |
|------|------|
| `event` | `str` |
| `run_id` | `str` |
| `tags` | `NotRequired[list[str]]` |
| `metadata` | `NotRequired[dict[str, Any]]` |
| `parent_ids` | `Sequence[str]` |

## Properties

- `event`
- `run_id`
- `tags`
- `metadata`
- `parent_ids`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/schema.py#L56)
