---
title: "upload_files"
description: "Upload multiple files to the sandbox."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/upload_files"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, upload_files]
---

# upload_files

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/upload_files)

Upload multiple files to the sandbox.

Implementations must support partial success - catch exceptions per-file
and return errors in `FileUploadResponse` objects rather than raising.

Upload files is responsible for ensuring that the parent path exists
(if user permissions allow the user to write to the given directory)

## Signature

```python
upload_files(
    self,
    files: list[tuple[str, bytes]],
) -> list[FileUploadResponse]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/sandbox.py#L1972)
