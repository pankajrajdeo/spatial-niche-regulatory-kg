---
title: "prepare_push_task_functional"
description: "Prepare a push task with an attached caller. Used for the functional API."
source: "https://reference.langchain.com/python/langgraph/pregel/_algo/prepare_push_task_functional"
category: "reference"
tags: [reference, langgraph, pregel, algo, prepare_push_task_functional]
---

# prepare_push_task_functional

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_algo/prepare_push_task_functional)

Prepare a push task with an attached caller. Used for the functional API.

## Signature

```python
prepare_push_task_functional(
    task_path: tuple[str, tuple, int, str, Call],
    task_id_checksum: str | None,
    *,
    checkpoint: Checkpoint,
    checkpoint_id_bytes: bytes,
    pending_writes: list[PendingWrite],
    channels: Mapping[str, BaseChannel],
    managed: ManagedValueMapping,
    config: RunnableConfig,
    step: int,
    stop: int,
    for_execution: bool,
    store: BaseStore | None = None,
    checkpointer: BaseCheckpointSaver | None = None,
    manager: None | ParentRunManager | AsyncParentRunManager = None,
    cache_policy: CachePolicy | None = None,
    retry_policy: Sequence[RetryPolicy] = (),
    parent_ns: str,
    task_id_func: _TaskIDFn,
) -> PregelTask | PregelExecutableTask
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_algo.py#L800)
