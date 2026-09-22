---
title: "channels_from_checkpoint"
description: "Hydrate channels from a checkpoint."
source: "https://reference.langchain.com/python/langgraph/pregel/_checkpoint/channels_from_checkpoint"
category: "reference"
tags: [reference, langgraph, pregel, checkpoint, channels_from_checkpoint]
---

# channels_from_checkpoint

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/channels_from_checkpoint)

Hydrate channels from a checkpoint.

For most channels, `spec.from_checkpoint(checkpoint["channel_values"][k])`
is sufficient. `DeltaChannel` is the exception: when the channel is
absent from `channel_values`, an ancestor walk via
`saver.get_delta_channel_history` is required to find the nearest seed
(`_DeltaSnapshot` blob or pre-migration plain value) and accumulate
the writes between it and the target. All delta channels needing
replay are batched into a single saver call.

## Signature

```python
channels_from_checkpoint(
    specs: Mapping[str, BaseChannel | ManagedValueSpec],
    checkpoint: Checkpoint,
    *,
    saver: BaseCheckpointSaver | None = None,
    config: RunnableConfig | None = None,
) -> tuple[Mapping[str, BaseChannel], ManagedValueMapping]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_checkpoint.py#L229)
