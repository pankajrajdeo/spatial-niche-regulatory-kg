---
title: "agrep"
description: "Async version of grep."
source: "https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/agrep"
category: "reference"
tags: [reference, deepagents, backends, composite, compositebackend, agrep]
---

# agrep

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/agrep)

Async version of grep.

See `grep()` for detailed documentation on routing behavior and parameters.

## Signature

```python
agrep(
    self,
    pattern: str,
    path: str | None = None,
    glob: str | None = None,
    *,
    max_count: int | None = None,
) -> GrepResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/composite.py#L551)
