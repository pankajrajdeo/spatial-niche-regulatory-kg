---
title: "StateNodeSpec"
description: "- Generic[NodeInputT, ContextT]"
source: "https://reference.langchain.com/python/langgraph/graph/_node/StateNodeSpec"
category: "reference"
tags: [reference, langgraph, graph, node, statenodespec]
---

# StateNodeSpec

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/_node/StateNodeSpec)

## Signature

```python
StateNodeSpec(
    self,
    runnable: StateNode[NodeInputT, ContextT],
    metadata: dict[str, Any] | None,
    input_schema: type[NodeInputT],
    retry_policy: RetryPolicy | Sequence[RetryPolicy] | None,
    cache_policy: CachePolicy | None,
    is_error_handler: bool = False,
    error_handler_node: str | None = None,
    ends: tuple[str, ...] | dict[str, str] | None = EMPTY_SEQ,
    defer: bool = False,
    timeout: TimeoutPolicy | None = None,
    trace_policy: TracePolicy | None = None,
)
```

## Extends

- `Generic[NodeInputT, ContextT]`

## Constructors

```python
__init__(
    self,
    runnable: StateNode[NodeInputT, ContextT],
    metadata: dict[str, Any] | None,
    input_schema: type[NodeInputT],
    retry_policy: RetryPolicy | Sequence[RetryPolicy] | None,
    cache_policy: CachePolicy | None,
    is_error_handler: bool = False,
    error_handler_node: str | None = None,
    ends: tuple[str, ...] | dict[str, str] | None = EMPTY_SEQ,
    defer: bool = False,
    timeout: TimeoutPolicy | None = None,
    trace_policy: TracePolicy | None = None,
) -> None
```

| Name | Type |
|------|------|
| `runnable` | `StateNode[NodeInputT, ContextT]` |
| `metadata` | `dict[str, Any] \| None` |
| `input_schema` | `type[NodeInputT]` |
| `retry_policy` | `RetryPolicy \| Sequence[RetryPolicy] \| None` |
| `cache_policy` | `CachePolicy \| None` |
| `is_error_handler` | `bool` |
| `error_handler_node` | `str \| None` |
| `ends` | `tuple[str, ...] \| dict[str, str] \| None` |
| `defer` | `bool` |
| `timeout` | `TimeoutPolicy \| None` |
| `trace_policy` | `TracePolicy \| None` |

## Properties

- `runnable`
- `metadata`
- `input_schema`
- `retry_policy`
- `cache_policy`
- `is_error_handler`
- `error_handler_node`
- `ends`
- `defer`
- `timeout`
- `trace_policy`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/graph/_node.py#L90)
