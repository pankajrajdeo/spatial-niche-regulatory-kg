---
title: "on_retriever_end"
description: "Run when the Retriever ends running."
source: "https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_retriever_end"
category: "reference"
tags: [reference, langchain-core, tracers, base, basetracer, on_retriever_end]
---

# on_retriever_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_retriever_end)

Run when the `Retriever` ends running.

## Signature

```python
on_retriever_end(
    self,
    documents: Sequence[Document],
    *,
    run_id: UUID,
    **kwargs: Any = {},
) -> Run
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `documents` | `Sequence[Document]` | Yes | The documents. |
| `run_id` | `UUID` | Yes | The run ID. |
| `**kwargs` | `Any` | No | Additional arguments. (default: `{}`) |

## Returns

`Run`

The run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/base.py#L520)
