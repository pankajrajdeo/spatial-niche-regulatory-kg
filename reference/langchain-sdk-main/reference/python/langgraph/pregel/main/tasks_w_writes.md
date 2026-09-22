---
title: "tasks_w_writes"
description: "Apply writes / subgraph states to tasks to be returned in a StateSnapshot."
source: "https://reference.langchain.com/python/langgraph/pregel/main/tasks_w_writes"
category: "reference"
tags: [reference, langgraph, pregel, main, tasks_w_writes]
---

# tasks_w_writes

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/debug/tasks_w_writes)

Apply writes / subgraph states to tasks to be returned in a StateSnapshot.

## Signature

```python
tasks_w_writes(
    tasks: Iterable[PregelTask | PregelExecutableTask],
    pending_writes: list[PendingWrite] | None,
    states: dict[str, RunnableConfig | StateSnapshot] | None,
    output_keys: str | Sequence[str],
) -> tuple[PregelTask, ...]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/debug.py#L209)
