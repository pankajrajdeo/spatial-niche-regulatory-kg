---
title: "atee"
description: "Subscribe and return n independent async iterators."
source: "https://reference.langchain.com/python/langgraph/stream/stream_channel/StreamChannel/atee"
category: "reference"
tags: [reference, langgraph, stream, stream_channel, streamchannel, atee]
---

# atee

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/stream_channel/StreamChannel/atee)

Subscribe and return `n` independent async iterators.

Caller-driven fan-out: each branch's `__anext__` either pops
from its own buffer or, under a shared `asyncio.Lock`, pulls
one item from the underlying cursor and distributes it to
every branch's buffer.

## Signature

```python
atee(
    self,
    n: int = 2,
) -> tuple[AsyncIterator[T], ...]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `n` | `int` | No | Number of branches to create. Must be >= 1. (default: `2`) |

## Returns

`AsyncIterator[T]`

A tuple of `n` async iterators over the same underlying

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/stream/stream_channel.py#L288)
