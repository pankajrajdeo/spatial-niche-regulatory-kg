---
title: "tee"
description: "Subscribe and return n independent sync iterators."
source: "https://reference.langchain.com/python/langgraph/stream/stream_channel/StreamChannel/tee"
category: "reference"
tags: [reference, langgraph, stream, stream_channel, streamchannel, tee]
---

# tee

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/stream_channel/StreamChannel/tee)

Subscribe and return `n` independent sync iterators.

Each branch has its own buffer; items pulled from the
underlying cursor are copied into every branch. Branches are
naturally bounded by caller pace since the sync pump is
caller-driven.

## Signature

```python
tee(
    self,
    n: int = 2,
) -> tuple[Iterator[T], ...]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `n` | `int` | No | Number of branches to create. Must be >= 1. (default: `2`) |

## Returns

`tuple[Iterator[T], ...]`

A tuple of `n` iterators over the same underlying stream.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/stream/stream_channel.py#L245)
