---
title: "aread"
description: "Async version of read using native store async methods."
source: "https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/aread"
category: "reference"
tags: [reference, deepagents, backends, store, storebackend, aread]
---

# aread

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/aread)

Async version of read using native store async methods.

This avoids sync calls in async context by using `store.aget` directly.

## Signature

```python
aread(
    self,
    file_path: str,
    offset: int = 0,
    limit: int = 2000,
) -> ReadResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/store.py#L401)
