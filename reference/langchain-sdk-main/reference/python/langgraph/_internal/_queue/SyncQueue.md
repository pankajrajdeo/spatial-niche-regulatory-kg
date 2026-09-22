---
title: "SyncQueue"
description: "Unbounded FIFO queue with a wait() method. Adapted from pure Python implementation of queue.SimpleQueue."
source: "https://reference.langchain.com/python/langgraph/_internal/_queue/SyncQueue"
category: "reference"
tags: [reference, langgraph, internal, queue, syncqueue]
---

# SyncQueue

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_queue/SyncQueue)

Unbounded FIFO queue with a wait() method.
Adapted from pure Python implementation of queue.SimpleQueue.

## Signature

```python
SyncQueue(
    self,
)
```

## Constructors

```python
__init__(
    self,
)
```

## Methods

- [`put()`](https://reference.langchain.com/python/langgraph/_internal/_queue/SyncQueue/put)
- [`get()`](https://reference.langchain.com/python/langgraph/_internal/_queue/SyncQueue/get)
- [`wait()`](https://reference.langchain.com/python/langgraph/_internal/_queue/SyncQueue/wait)
- [`empty()`](https://reference.langchain.com/python/langgraph/_internal/_queue/SyncQueue/empty)
- [`qsize()`](https://reference.langchain.com/python/langgraph/_internal/_queue/SyncQueue/qsize)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/_internal/_queue.py#L70)
