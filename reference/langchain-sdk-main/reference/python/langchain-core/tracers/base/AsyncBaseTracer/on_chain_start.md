---
title: "on_chain_start"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/tracers/base/AsyncBaseTracer/on_chain_start"
category: "reference"
tags: [reference, langchain-core, tracers, base, asyncbasetracer, on_chain_start]
---

# on_chain_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/AsyncBaseTracer/on_chain_start)

## Signature

```python
on_chain_start(
    self,
    serialized: dict[str, Any],
    inputs: dict[str, Any],
    *,
    run_id: UUID,
    tags: list[str] | None = None,
    parent_run_id: UUID | None = None,
    metadata: dict[str, Any] | None = None,
    run_type: str | None = None,
    name: str | None = None,
    **kwargs: Any = {},
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/base.py#L718)
