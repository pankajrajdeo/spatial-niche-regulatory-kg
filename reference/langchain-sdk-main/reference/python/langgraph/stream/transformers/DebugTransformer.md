---
title: "DebugTransformer"
description: "Capture debug events as a drainable stream."
source: "https://reference.langchain.com/python/langgraph/stream/transformers/DebugTransformer"
category: "reference"
tags: [reference, langgraph, stream, transformers, debugtransformer]
---

# DebugTransformer

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/transformers/DebugTransformer)

Capture debug events as a drainable stream.

Surfaces `stream_mode="debug"` data on `run.debug` as a
`StreamChannel[dict[str, Any]]`. Each item is a debug event with
step-level detail (checkpoint snapshots, task payloads, and
task results wrapped with step number and timestamp).

Only events at the run's own scope are captured; debug data from
deeper subgraphs is available on the respective subgraph handle's
`.debug` projection.

Native transformer — `run.debug` is a direct attribute.

## Signature

```python
DebugTransformer(
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

- [`init()`](https://reference.langchain.com/python/langgraph/stream/transformers/DebugTransformer/init)
- [`process()`](https://reference.langchain.com/python/langgraph/stream/transformers/DebugTransformer/process)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/stream/transformers.py#L966)
