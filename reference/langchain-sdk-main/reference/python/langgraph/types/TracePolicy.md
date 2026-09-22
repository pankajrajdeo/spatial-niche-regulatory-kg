---
title: "TracePolicy"
description: "Configuration for how a node's run is traced."
source: "https://reference.langchain.com/python/langgraph/types/TracePolicy"
category: "reference"
tags: [reference, langgraph, types, tracepolicy]
---

# TracePolicy

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/TracePolicy)

Configuration for how a node's run is traced.

Scope: this only transforms what the node's *own* run records. Child runs created
by a traced `bound` runnable and the root graph run are not affected. Plain
function nodes are traced with `trace=False`, so they have no such child runs.

Not intended to redact secrets. To redact inputs/outputs across all runs
(children included), use the LangSmith client's
`hide_inputs`/`hide_outputs`/`anonymizer` instead.

Each processor receives the node's raw input/output value (not a normalized
kwargs dict) and returns the value to record.

## Signature

```python
TracePolicy(
    self,
    *,
    process_inputs: Callable[[Any], Any] | None = None,
    process_outputs: Callable[[Any], Any] | None = None,
)
```

## Constructors

```python
__init__(
    self,
    *,
    process_inputs: Callable[[Any], Any] | None = None,
    process_outputs: Callable[[Any], Any] | None = None,
) -> None
```

| Name | Type |
|------|------|
| `process_inputs` | `Callable[[Any], Any] \| None` |
| `process_outputs` | `Callable[[Any], Any] \| None` |

## Properties

- `process_inputs`
- `process_outputs`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/types.py#L532)
