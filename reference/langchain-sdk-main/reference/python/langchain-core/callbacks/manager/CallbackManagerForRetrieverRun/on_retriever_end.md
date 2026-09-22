---
title: "on_retriever_end"
description: "Run when retriever ends running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForRetrieverRun/on_retriever_end"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanagerforretrieverrun, on_retriever_end]
---

# on_retriever_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForRetrieverRun/on_retriever_end)

Run when retriever ends running.

## Signature

```python
on_retriever_end(
    self,
    documents: Sequence[Document],
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `documents` | `Sequence[Document]` | Yes | The retrieved documents. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L1251)
