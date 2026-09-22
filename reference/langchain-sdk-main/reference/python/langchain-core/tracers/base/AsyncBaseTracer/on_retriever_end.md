---
title: "on_retriever_end"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/tracers/base/AsyncBaseTracer/on_retriever_end"
category: "reference"
tags: [reference, langchain-core, tracers, base, asyncbasetracer, on_retriever_end]
---

# on_retriever_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/AsyncBaseTracer/on_retriever_end)

## Signature

```python
on_retriever_end(
    self,
    documents: Sequence[Document],
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    **kwargs: Any = {},
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/base.py#L887)
