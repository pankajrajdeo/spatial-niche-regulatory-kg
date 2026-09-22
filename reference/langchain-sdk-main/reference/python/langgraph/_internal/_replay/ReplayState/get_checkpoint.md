---
title: "get_checkpoint"
description: "Load the right checkpoint for a subgraph during replay."
source: "https://reference.langchain.com/python/langgraph/_internal/_replay/ReplayState/get_checkpoint"
category: "reference"
tags: [reference, langgraph, internal, replay, replaystate, get_checkpoint]
---

# get_checkpoint

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_replay/ReplayState/get_checkpoint)

Load the right checkpoint for a subgraph during replay.

On the first call for a given subgraph namespace, returns the latest
checkpoint created *before* the replay point. On subsequent calls
(e.g. the same subgraph in a later loop iteration), falls back to
normal latest-checkpoint loading.

## Signature

```python
get_checkpoint(
    self,
    checkpoint_ns: str,
    checkpointer: BaseCheckpointSaver,
    checkpoint_config: RunnableConfig,
) -> CheckpointTuple | None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/_internal/_replay.py#L52)
