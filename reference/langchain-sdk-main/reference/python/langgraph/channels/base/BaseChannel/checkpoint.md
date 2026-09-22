---
title: "checkpoint"
description: "Return a serializable representation of the channel's current state."
source: "https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/checkpoint"
category: "reference"
tags: [reference, langgraph, channels, base, basechannel, checkpoint]
---

# checkpoint

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/checkpoint)

Return a serializable representation of the channel's current state.

Raises `EmptyChannelError` if the channel is empty (never updated yet),
or doesn't support checkpoints.

## Signature

```python
checkpoint(
    self,
) -> Checkpoint | Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/channels/base.py#L49)
