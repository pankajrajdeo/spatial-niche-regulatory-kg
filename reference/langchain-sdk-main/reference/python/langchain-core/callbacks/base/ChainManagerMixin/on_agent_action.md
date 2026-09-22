---
title: "on_agent_action"
description: "Run on agent action."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/ChainManagerMixin/on_agent_action"
category: "reference"
tags: [reference, langchain-core, callbacks, base, chainmanagermixin, on_agent_action]
---

# on_agent_action

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/ChainManagerMixin/on_agent_action)

Run on agent action.

## Signature

```python
on_agent_action(
    self,
    action: AgentAction,
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    **kwargs: Any = {},
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `action` | `AgentAction` | Yes | The agent action. |
| `run_id` | `UUID` | Yes | The ID of the current run. |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L206)
