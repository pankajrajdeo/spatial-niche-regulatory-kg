---
title: "set_node_defaults"
description: "Set default node policies that apply to every node in this graph."
source: "https://reference.langchain.com/python/langgraph/graph/state/StateGraph/set_node_defaults"
category: "reference"
tags: [reference, langgraph, graph, state, stategraph, set_node_defaults]
---

# set_node_defaults

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/set_node_defaults)

Set default node policies that apply to every node in this graph.

Per-node values passed to `add_node` always take precedence over these
defaults. Defaults are applied at `compile()` time. Policies set here
are **not** inherited by subgraphs.

`retry_policy` and `timeout` defaults apply to **all** nodes,
including error-handler nodes. `cache_policy` and `error_handler`
defaults only apply to regular nodes -- caching error-handler results
is unsafe, and handlers must never catch themselves.

## Signature

```python
set_node_defaults(
    self,
    *,
    retry_policy: RetryPolicy | Sequence[RetryPolicy] | None = None,
    cache_policy: CachePolicy | None = None,
    error_handler: StateNode[Any, ContextT] | None = None,
    timeout: float | timedelta | TimeoutPolicy | None = None,
) -> Self
```

## Description

**Example:**

```python
graph = (
    StateGraph(State)
    .set_node_defaults(
        retry_policy=RetryPolicy(max_attempts=3),
        error_handler=my_fallback_handler,
    )
    .add_node("a", node_a)
    .add_node("b", node_b, retry_policy=custom_retry)  # overrides default
    .add_edge(START, "a")
    .compile()
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `retry_policy` | `RetryPolicy \| Sequence[RetryPolicy] \| None` | No | Default retry policy for nodes that don't specify their own via `add_node(..., retry_policy=...)`. Also applies to error-handler nodes. (default: `None`) |
| `cache_policy` | `CachePolicy \| None` | No | Default cache policy for nodes that don't specify their own via `add_node(..., cache_policy=...)`. Does **not** apply to error-handler nodes. (default: `None`) |
| `error_handler` | `StateNode[Any, ContextT] \| None` | No | Default error handler invoked when any regular node raises and does not have its own `error_handler` set via `add_node`. The handler is **not** invoked when an error-handler node itself raises -- handler failures fail the run. (default: `None`) |
| `timeout` | `float \| timedelta \| TimeoutPolicy \| None` | No | Default timeout policy for nodes that don't specify their own via `add_node(..., timeout=...)`. Also applies to error-handler nodes. Accepts a `TimeoutPolicy`, a number of seconds (`float`), or a `timedelta`. (default: `None`) |

## Returns

`Self`

The builder instance, for chaining.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/graph/state.py#L272)
