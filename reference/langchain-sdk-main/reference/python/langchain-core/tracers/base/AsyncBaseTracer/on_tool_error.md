---
title: "on_tool_error"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/tracers/base/AsyncBaseTracer/on_tool_error"
category: "reference"
tags: [reference, langchain-core, tracers, base, asyncbasetracer, on_tool_error]
---

# on_tool_error

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/AsyncBaseTracer/on_tool_error)

## Signature

```python
on_tool_error(
    self,
    error: BaseException,
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    **kwargs: Any = {},
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/base.py#L822)
