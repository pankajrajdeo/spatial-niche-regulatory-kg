---
title: "SubagentTransformer"
description: "Promote nested named agents into typed handles on run.subagents."
source: "https://reference.langchain.com/python/langchain/agents/_subagent_transformer/SubagentTransformer"
category: "reference"
tags: [reference, langchain, agents, subagent_transformer, subagenttransformer]
---

# SubagentTransformer

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/_subagent_transformer/SubagentTransformer)

Promote nested named agents into typed handles on `run.subagents`.

The base `_TasksLifecycleBase` records each namespace's `lc_agent_name`
(set by `create_agent(name=...)`) and, on every task start, fires
`_on_started` with the resolved `graph_name` and a `cause` for genuine
subagent boundaries. This transformer gates on that boundary using the
inherited `_lc_by_ns` map: a nested run is a subagent when it carries an
`lc_agent_name`. Same-named nested agents (e.g. a subagent that invokes
itself) are surfaced; unnamed agents (`None`) are excluded. Trade-off: a
non-agent subgraph that inherited the parent's name will also surface.

On the first matching task start it builds a child mux and emits a typed
handle on `run.subagents`, then forwards subsequent child-scope events into
that handle so the nested run can be consumed independently.

## Signature

```python
SubagentTransformer(
    self,
    scope: tuple[str, ...] = (),
)
```

## Extends

- `_TasksLifecycleBase`

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

- `supports_sync`

## Methods

- [`init()`](https://reference.langchain.com/python/langchain/agents/_subagent_transformer/SubagentTransformer/init)
- [`process()`](https://reference.langchain.com/python/langchain/agents/_subagent_transformer/SubagentTransformer/process)
- [`aprocess()`](https://reference.langchain.com/python/langchain/agents/_subagent_transformer/SubagentTransformer/aprocess)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/_subagent_transformer.py#L120)
