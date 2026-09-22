---
title: "aedit"
description: "Async version of edit using native store async methods."
source: "https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/aedit"
category: "reference"
tags: [reference, deepagents, backends, store, storebackend, aedit]
---

# aedit

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/aedit)

Async version of edit using native store async methods.

This avoids sync calls in async context by using `store.aget`/`aput` directly.

## Signature

```python
aedit(
    self,
    file_path: str,
    old_string: str,
    new_string: str,
    replace_all: bool = False,
) -> EditResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/store.py#L510)
