---
title: "files"
description: "Files in the filesystem. Uses DeltaChannel with snapshots every ~50 pregel steps to bound read depth."
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemState/files"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, filesystemstate, files]
---

# files

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemState/files)

Files in the filesystem. Uses DeltaChannel with snapshots every ~50 pregel steps to bound read depth.

## Signature

```python
files: Annotated[NotRequired[dict[str, FileData]], DeltaChannel(_file_data_delta_reducer, snapshot_frequency=50)]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/filesystem.py#L1195)
