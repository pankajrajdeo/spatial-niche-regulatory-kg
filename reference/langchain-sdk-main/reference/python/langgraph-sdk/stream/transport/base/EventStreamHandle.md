---
title: "EventStreamHandle"
description: "Handle for one async filtered event stream."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/transport/base/EventStreamHandle"
category: "reference"
tags: [reference, langgraph-sdk, stream, transport, base, eventstreamhandle]
---

# EventStreamHandle

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/transport/base/EventStreamHandle)

Handle for one async filtered event stream.

## Signature

```python
EventStreamHandle(
    self,
    events: AsyncIterator[Event],
    ready: asyncio.Future[None],
    done: asyncio.Future[BaseException | None],
    close: Callable[[], Awaitable[None]],
)
```

## Constructors

```python
__init__(
    self,
    events: AsyncIterator[Event],
    ready: asyncio.Future[None],
    done: asyncio.Future[BaseException | None],
    close: Callable[[], Awaitable[None]],
) -> None
```

| Name | Type |
|------|------|
| `events` | `AsyncIterator[Event]` |
| `ready` | `asyncio.Future[None]` |
| `done` | `asyncio.Future[BaseException \| None]` |
| `close` | `Callable[[], Awaitable[None]]` |

## Properties

- `events`
- `ready`
- `done`
- `close`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/stream/transport/base.py#L14)
