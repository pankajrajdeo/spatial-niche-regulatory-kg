---
title: "SubgraphsDecoder"
description: "Discovers child subgraph handles and fans out events to active ones."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/decoders/SubgraphsDecoder"
category: "reference"
tags: [reference, langgraph-sdk, stream, decoders, subgraphsdecoder]
---

# SubgraphsDecoder

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/decoders/SubgraphsDecoder)

Discovers child subgraph handles and fans out events to active ones.

Mirrors the per-event body of `_SubgraphsProjection._subgraphs_iter`
(`_async/stream.py:963-1041`) plus `_apply_tasks_result`. Root-inbox
forwarding and terminal-status-on-close stay at the projection / wrapper
layer.

## Signature

```python
SubgraphsDecoder(
    self,
    scope: tuple[str, ...],
    handle_factory: Callable[..., Any],
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `scope` | `tuple[str, ...]` | Yes | Tuple-form namespace of this decoder's parent. `()` for root. |
| `handle_factory` | `Callable[..., Any]` | Yes | Keyword-only `(path, graph_name, trigger_call_id) -> handle`. |

## Constructors

```python
__init__(
    self,
    scope: tuple[str, ...],
    handle_factory: Callable[..., Any],
)
```

| Name | Type |
|------|------|
| `scope` | `tuple[str, ...]` |
| `handle_factory` | `Callable[..., Any]` |

## Methods

- [`feed()`](https://reference.langchain.com/python/langgraph-sdk/stream/decoders/SubgraphsDecoder/feed)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/stream/decoders.py#L257)
