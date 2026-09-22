---
title: "wait"
description: "If queue is empty, wait until an item is available."
source: "https://reference.langchain.com/python/langgraph/_internal/_queue/AsyncQueue/wait"
category: "reference"
tags: [reference, langgraph, internal, queue, asyncqueue, wait]
---

# wait

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_queue/AsyncQueue/wait)

If queue is empty, wait until an item is available.

Copied from Queue.get(), removing the call to .get_nowait(),
ie. this doesn't consume the item, just waits for it.

## Signature

```python
wait(
    self,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/_internal/_queue.py#L17)
