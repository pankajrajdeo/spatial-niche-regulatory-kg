---
title: "on_agent_finish"
description: "Run on the agent end."
source: "https://reference.langchain.com/python/langchain-core/callbacks/stdout/StdOutCallbackHandler/on_agent_finish"
category: "reference"
tags: [reference, langchain-core, callbacks, stdout, stdoutcallbackhandler, on_agent_finish]
---

# on_agent_finish

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/stdout/StdOutCallbackHandler/on_agent_finish)

Run on the agent end.

## Signature

```python
on_agent_finish(
    self,
    finish: AgentFinish,
    color: str | None = None,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `finish` | `AgentFinish` | Yes | The agent finish. |
| `color` | `str \| None` | No | The color to use for the text. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/stdout.py#L112)
