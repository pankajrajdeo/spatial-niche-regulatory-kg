---
title: "on_agent_action"
description: "Handle agent action by writing the action log."
source: "https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_agent_action"
category: "reference"
tags: [reference, langchain-core, callbacks, file, filecallbackhandler, on_agent_action]
---

# on_agent_action

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_agent_action)

Handle agent action by writing the action log.

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
| `action` | `AgentAction` | Yes | The agent action containing the log to write. |
| `color` | `str \| None` | No | Color override for this specific output.  If `None`, uses `self.color`. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/file.py#L192)
