---
title: "replay_writes"
description: "Apply ancestor writes oldest-to-newest via a single reducer call."
source: "https://reference.langchain.com/python/langgraph/channels/delta/DeltaChannel/replay_writes"
category: "reference"
tags: [reference, langgraph, channels, delta, deltachannel, replay_writes]
---

# replay_writes

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/channels/delta/DeltaChannel/replay_writes)

Apply ancestor writes oldest-to-newest via a single reducer call.

If any write is an Overwrite, the last one in the sequence acts as
the reset point: its value becomes the new base and only writes
after it are passed to the reducer.

## Signature

```python
replay_writes(
    self,
    writes: Sequence[PendingWrite],
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/channels/delta.py#L139)
