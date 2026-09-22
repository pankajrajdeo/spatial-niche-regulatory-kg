---
title: "bulk_update_state"
description: "Apply updates to the graph state in bulk. Requires a checkpointer to be set."
source: "https://reference.langchain.com/python/langgraph/pregel/main/Pregel/bulk_update_state"
category: "reference"
tags: [reference, langgraph, pregel, main, bulk_update_state]
---

# bulk_update_state

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main/Pregel/bulk_update_state)

Apply updates to the graph state in bulk. Requires a checkpointer to be set.

## Signature

```python
bulk_update_state(
    self,
    config: RunnableConfig,
    supersteps: Sequence[Sequence[StateUpdate]],
) -> RunnableConfig
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig` | Yes | The config to apply the updates to. |
| `supersteps` | `Sequence[Sequence[StateUpdate]]` | Yes | A list of supersteps, each including a list of updates to apply sequentially to a graph state.  Each update is a tuple of the form `(values, as_node, task_id)` where `task_id` is optional. |

## Returns

`RunnableConfig`

The updated config.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/main.py#L1590)
