---
title: "on_retry"
description: "Run on a retry event."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/RunManagerMixin/on_retry"
category: "reference"
tags: [reference, langchain-core, callbacks, base, runmanagermixin, on_retry]
---

# on_retry

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/RunManagerMixin/on_retry)

Run on a retry event.

## Signature

```python
on_retry(
    self,
    retry_state: RetryCallState,
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    **kwargs: Any = {},
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `retry_state` | `RetryCallState` | Yes | The retry state. |
| `run_id` | `UUID` | Yes | The ID of the current run. |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L455)
