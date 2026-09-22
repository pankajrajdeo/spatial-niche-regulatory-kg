---
title: "put"
description: "Put the item on the queue."
source: "https://reference.langchain.com/python/langgraph/_internal/_queue/SyncQueue/put"
category: "reference"
tags: [reference, langgraph, internal, queue, syncqueue, put]
---

# put

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_queue/SyncQueue/put)

Put the item on the queue.

The optional 'block' and 'timeout' arguments are ignored, as this method
never blocks.  They are provided for compatibility with the Queue class.

## Signature

```python
put(
    self,
    item,
    block = True,
    timeout = None,
)
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/_internal/_queue.py#L79)
