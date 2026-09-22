---
title: "SubagentRunStream"
description: "Typed sync handle for a nested named-agent execution."
source: "https://reference.langchain.com/python/langchain/agents/_subagent_transformer/SubagentRunStream"
category: "reference"
tags: [reference, langchain, agents, subagent_transformer, subagentrunstream]
---

# SubagentRunStream

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/_subagent_transformer/SubagentRunStream)

Typed sync handle for a nested named-agent execution.

Surfaces on `run.subagents` when a nested run's `lc_agent_name` differs
from its parent's (i.e., a `create_agent(name=...)` dispatched from a tool).

## Signature

```python
SubagentRunStream(
    self,
    mux: StreamMux,
    *,
    path: tuple[str, ...],
    graph_name: str | None = None,
    trigger_call_id: str | None = None,
    cause: LifecycleCause | None = None,
)
```

## Extends

- `SubgraphRunStream`

## Constructors

```python
__init__(
    self,
    mux: StreamMux,
    *,
    path: tuple[str, ...],
    graph_name: str | None = None,
    trigger_call_id: str | None = None,
    cause: LifecycleCause | None = None,
) -> None
```

| Name | Type |
|------|------|
| `mux` | `StreamMux` |
| `path` | `tuple[str, ...]` |
| `graph_name` | `str \| None` |
| `trigger_call_id` | `str \| None` |
| `cause` | `LifecycleCause \| None` |

## Properties

- `name`
- `cause`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/_subagent_transformer.py#L44)
