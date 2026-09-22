---
title: "on_agent_finish"
description: "Run when agent finish is received."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainRun/on_agent_finish"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asynccallbackmanagerforchainrun, on_agent_finish]
---

# on_agent_finish

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainRun/on_agent_finish)

Run when agent finish is received.

## Signature

```python
on_agent_finish(
    self,
    finish: AgentFinish,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `finish` | `AgentFinish` | Yes | The agent finish. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L1106)
