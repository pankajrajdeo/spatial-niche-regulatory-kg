---
title: "from_checkpoint"
description: "Return a new identical channel, optionally initialized from a checkpoint."
source: "https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/from_checkpoint"
category: "reference"
tags: [reference, langgraph, channels, base, basechannel, from_checkpoint]
---

# from_checkpoint

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/from_checkpoint)

Return a new identical channel, optionally initialized from a checkpoint.

If the checkpoint contains complex data structures, they should be copied.

## Signature

```python
from_checkpoint(
    self,
    checkpoint: Checkpoint | Any,
) -> Self
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/channels/base.py#L60)
