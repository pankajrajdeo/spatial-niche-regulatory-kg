---
title: "prepare_single_task"
description: "Prepares a single task for the next Pregel step, given a task path, which uniquely identifies a PUSH or PULL task within the graph."
source: "https://reference.langchain.com/python/langgraph/pregel/_algo/prepare_single_task"
category: "reference"
tags: [reference, langgraph, pregel, algo, prepare_single_task]
---

# prepare_single_task

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_algo/prepare_single_task)

Prepares a single task for the next Pregel step, given a task path, which
uniquely identifies a PUSH or PULL task within the graph.

## Signature

```python
prepare_single_task(
    task_path: tuple[Any, ...],
    task_id_checksum: str | None,
    *,
    checkpoint: Checkpoint,
    checkpoint_id_bytes: bytes,
    checkpoint_null_version: V | None,
    pending_writes: list[PendingWrite],
    processes: Mapping[str, PregelNode],
    channels: Mapping[str, BaseChannel],
    managed: ManagedValueMapping,
    config: RunnableConfig,
    step: int,
    stop: int,
    for_execution: bool,
    store: BaseStore | None = None,
    checkpointer: BaseCheckpointSaver | None = None,
    manager: None | ParentRunManager | AsyncParentRunManager = None,
    input_cache: dict[INPUT_CACHE_KEY_TYPE, Any] | None = None,
    cache_policy: CachePolicy | None = None,
    retry_policy: Sequence[RetryPolicy] = (),
) -> None | PregelTask | PregelExecutableTask
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_algo.py#L524)
