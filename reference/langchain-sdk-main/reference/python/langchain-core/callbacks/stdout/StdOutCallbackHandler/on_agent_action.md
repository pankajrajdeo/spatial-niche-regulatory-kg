---
title: "on_agent_action"
description: "Run on agent action."
source: "https://reference.langchain.com/python/langchain-core/callbacks/stdout/StdOutCallbackHandler/on_agent_action"
category: "reference"
tags: [reference, langchain-core, callbacks, stdout, stdoutcallbackhandler, on_agent_action]
---

# on_agent_action

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/stdout/StdOutCallbackHandler/on_agent_action)

Run on agent action.

## Signature

```python
on_agent_action(
    self,
    action: AgentAction,
    color: str | None = None,
    **kwargs: Any = {},
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `action` | `AgentAction` | Yes | The agent action. |
| `color` | `str \| None` | No | The color to use for the text. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/stdout.py#L56)
