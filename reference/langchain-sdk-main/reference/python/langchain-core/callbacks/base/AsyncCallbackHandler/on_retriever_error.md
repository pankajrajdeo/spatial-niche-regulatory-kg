---
title: "on_retriever_error"
description: "Run on retriever error."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_retriever_error"
category: "reference"
tags: [reference, langchain-core, callbacks, base, asynccallbackhandler, on_retriever_error]
---

# on_retriever_error

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_retriever_error)

Run on retriever error.

## Signature

```python
on_retriever_error(
    self,
    error: BaseException,
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `error` | `BaseException` | Yes | The error that occurred. |
| `run_id` | `UUID` | Yes | The ID of the current run. |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `tags` | `list[str] \| None` | No | The tags. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L961)
