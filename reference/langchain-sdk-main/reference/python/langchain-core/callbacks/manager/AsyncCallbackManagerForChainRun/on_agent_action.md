---
title: "on_agent_action"
description: "Run when agent action is received."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainRun/on_agent_action"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asynccallbackmanagerforchainrun, on_agent_action]
---

# on_agent_action

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainRun/on_agent_action)

Run when agent action is received.

## Signature

```python
on_agent_action(
    self,
    action: AgentAction,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `action` | `AgentAction` | Yes | The agent action. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L1086)
