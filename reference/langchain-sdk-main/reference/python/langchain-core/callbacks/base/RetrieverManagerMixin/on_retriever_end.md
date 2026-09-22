---
title: "on_retriever_end"
description: "Run when Retriever ends running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/RetrieverManagerMixin/on_retriever_end"
category: "reference"
tags: [reference, langchain-core, callbacks, base, retrievermanagermixin, on_retriever_end]
---

# on_retriever_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/RetrieverManagerMixin/on_retriever_end)

Run when `Retriever` ends running.

## Signature

```python
on_retriever_end(
    self,
    documents: Sequence[Document],
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    **kwargs: Any = {},
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `documents` | `Sequence[Document]` | Yes | The documents retrieved. |
| `run_id` | `UUID` | Yes | The ID of the current run. |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L44)
