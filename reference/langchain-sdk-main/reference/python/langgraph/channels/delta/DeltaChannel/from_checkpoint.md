---
title: "from_checkpoint"
description: "Initialize from a stored blob."
source: "https://reference.langchain.com/python/langgraph/channels/delta/DeltaChannel/from_checkpoint"
category: "reference"
tags: [reference, langgraph, channels, delta, deltachannel, from_checkpoint]
---

# from_checkpoint

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/channels/delta/DeltaChannel/from_checkpoint)

Initialize from a stored blob.

## Signature

```python
from_checkpoint(
    self,
    checkpoint: Any,
) -> Self
```

## Description

**Blob types:**

* `MISSING`: start empty; caller replays writes.
* `_DeltaSnapshot(value)`: restore value directly from snapshot.
* plain value (migration from old `BinaryOperatorAggregate` blobs):
  use directly.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/channels/delta.py#L118)
