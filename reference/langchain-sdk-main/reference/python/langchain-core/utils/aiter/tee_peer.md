---
title: "tee_peer"
description: "An individual iterator of a tee."
source: "https://reference.langchain.com/python/langchain-core/utils/aiter/tee_peer"
category: "reference"
tags: [reference, langchain-core, utils, aiter, tee_peer]
---

# tee_peer

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/aiter/tee_peer)

An individual iterator of a `tee`.

This function is a generator that yields items from the shared iterator
`iterator`. It buffers items until the least advanced iterator has yielded them as
well.

The buffer is shared with all other peers.

## Signature

```python
tee_peer(
    iterator: AsyncIterator[T],
    buffer: deque[T],
    peers: list[deque[T]],
    lock: AbstractAsyncContextManager[Any],
) -> AsyncGenerator[T, None]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `iterator` | `AsyncIterator[T]` | Yes | The shared iterator. |
| `buffer` | `deque[T]` | Yes | The buffer for this peer. |
| `peers` | `list[deque[T]]` | Yes | The buffers of all peers. |
| `lock` | `AbstractAsyncContextManager[Any]` | Yes | The lock to synchronise access to the shared buffers. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/aiter.py#L103)
