---
title: "on_retriever_error"
description: "Run when retriever errors."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForRetrieverRun/on_retriever_error"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanagerforretrieverrun, on_retriever_error]
---

# on_retriever_error

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForRetrieverRun/on_retriever_error)

Run when retriever errors.

## Signature

```python
on_retriever_error(
    self,
    error: BaseException,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `error` | `BaseException` | Yes | The error. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L1276)
