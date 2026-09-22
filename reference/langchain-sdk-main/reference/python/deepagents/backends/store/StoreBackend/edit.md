---
title: "edit"
description: "Edit a file by replacing string occurrences."
source: "https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/edit"
category: "reference"
tags: [reference, deepagents, backends, store, storebackend, edit]
---

# edit

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/edit)

Edit a file by replacing string occurrences.

Returns `EditResult` on success or error.

## Signature

```python
edit(
    self,
    file_path: str,
    old_string: str,
    new_string: str,
    replace_all: bool = False,
) -> EditResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/store.py#L472)
