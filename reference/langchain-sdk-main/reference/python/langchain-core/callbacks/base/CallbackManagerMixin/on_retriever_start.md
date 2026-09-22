---
title: "on_retriever_start"
description: "Run when the Retriever starts running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/CallbackManagerMixin/on_retriever_start"
category: "reference"
tags: [reference, langchain-core, callbacks, base, callbackmanagermixin, on_retriever_start]
---

# on_retriever_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/CallbackManagerMixin/on_retriever_start)

Run when the `Retriever` starts running.

## Signature

```python
on_retriever_start(
    self,
    serialized: dict[str, Any],
    query: str,
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
    **kwargs: Any = {},
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serialized` | `dict[str, Any]` | Yes | The serialized `Retriever`. |
| `query` | `str` | Yes | The query. |
| `run_id` | `UUID` | Yes | The ID of the current run. |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `tags` | `list[str] \| None` | No | The tags. (default: `None`) |
| `metadata` | `dict[str, Any] \| None` | No | The metadata. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L363)
