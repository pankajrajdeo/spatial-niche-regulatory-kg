---
title: "on_retry"
description: "Run when a retry is received."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/RunManager/on_retry"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, runmanager, on_retry]
---

# on_retry

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/RunManager/on_retry)

Run when a retry is received.

## Signature

```python
on_retry(
    self,
    retry_state: RetryCallState,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `retry_state` | `RetryCallState` | Yes | The retry state. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L573)
