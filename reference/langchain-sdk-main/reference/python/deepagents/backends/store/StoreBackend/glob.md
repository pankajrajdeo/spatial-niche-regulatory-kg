---
title: "glob"
description: "Find files matching a glob pattern in the store."
source: "https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/glob"
category: "reference"
tags: [reference, deepagents, backends, store, storebackend, glob]
---

# glob

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/glob)

Find files matching a glob pattern in the store.

Matching follows the shared backend contract -- see `BackendProtocol.glob`.
A bare pattern is basename-at-any-depth, so `*.py` matches nested files.
A refused pattern is returned as `GlobResult(error=...)`, not raised.

## Signature

```python
glob(
    self,
    pattern: str,
    path: str | None = None,
) -> GlobResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/store.py#L613)
