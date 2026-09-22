---
title: "on_retriever_start"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/tracers/base/AsyncBaseTracer/on_retriever_start"
category: "reference"
tags: [reference, langchain-core, tracers, base, asyncbasetracer, on_retriever_start]
---

# on_retriever_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/AsyncBaseTracer/on_retriever_start)

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
    name: str | None = None,
    **kwargs: Any = {},
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/base.py#L839)
