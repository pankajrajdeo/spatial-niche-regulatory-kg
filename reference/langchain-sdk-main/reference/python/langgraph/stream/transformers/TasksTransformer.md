---
title: "TasksTransformer"
description: "Capture raw task events as a drainable stream."
source: "https://reference.langchain.com/python/langgraph/stream/transformers/TasksTransformer"
category: "reference"
tags: [reference, langgraph, stream, transformers, taskstransformer]
---

# TasksTransformer

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/transformers/TasksTransformer)

Capture raw task events as a drainable stream.

Surfaces `stream_mode="tasks"` data on `run.tasks` as a
`StreamChannel[dict[str, Any]]`. Each item is a task payload
(start or result).

`LifecycleTransformer` and `SubgraphTransformer` also consume
`tasks` events for subgraph discovery and lifecycle tracking.
This transformer captures the raw payloads independently for
consumers who need task-level detail.

Only events at the run's own scope are captured; task data from
deeper subgraphs is available on the respective subgraph handle's
`.tasks` projection.

Native transformer — `run.tasks` is a direct attribute.

## Signature

```python
TasksTransformer(
    self,
    scope: tuple[str, ...] = (),
)
```

## Extends

- `StreamTransformer`

## Constructors

```python
__init__(
    self,
    scope: tuple[str, ...] = (),
) -> None
```

| Name | Type |
|------|------|
| `scope` | `tuple[str, ...]` |

## Properties

- `required_stream_modes`

## Methods

- [`init()`](https://reference.langchain.com/python/langgraph/stream/transformers/TasksTransformer/init)
- [`process()`](https://reference.langchain.com/python/langgraph/stream/transformers/TasksTransformer/process)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/stream/transformers.py#L1002)
