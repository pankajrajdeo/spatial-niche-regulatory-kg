---
title: "on_retriever_start"
description: "Run when the retriever starts running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManager/on_retriever_start"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asynccallbackmanager, on_retriever_start]
---

# on_retriever_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManager/on_retriever_start)

Run when the retriever starts running.

## Signature

```python
on_retriever_start(
    self,
    serialized: dict[str, Any] | None,
    query: str,
    run_id: UUID | None = None,
    parent_run_id: UUID | None = None,
    **kwargs: Any = {},
) -> AsyncCallbackManagerForRetrieverRun
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serialized` | `dict[str, Any] \| None` | Yes | The serialized retriever. |
| `query` | `str` | Yes | The query. |
| `run_id` | `UUID \| None` | No | The ID of the run. (default: `None`) |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Returns

`AsyncCallbackManagerForRetrieverRun`

The async callback manager for the retriever run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L2163)
