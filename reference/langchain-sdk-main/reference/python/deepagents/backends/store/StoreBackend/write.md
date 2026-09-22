---
title: "write"
description: "Write content to a file, creating it or overwriting it if it already exists."
source: "https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/write"
category: "reference"
tags: [reference, deepagents, backends, store, storebackend, write]
---

# write

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/write)

Write content to a file, creating it or overwriting it if it already exists.

Returns `WriteResult` on success or error.

## Signature

```python
write(
    self,
    file_path: str,
    content: str,
) -> WriteResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/store.py#L428)
