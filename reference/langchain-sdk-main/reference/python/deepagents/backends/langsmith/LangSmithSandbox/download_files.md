---
title: "download_files"
description: "Download multiple files from the LangSmith sandbox."
source: "https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox/download_files"
category: "reference"
tags: [reference, deepagents, backends, langsmith, langsmithsandbox, download_files]
---

# download_files

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/langsmith/LangSmithSandbox/download_files)

Download multiple files from the LangSmith sandbox.

Supports partial success. Individual downloads may fail without
affecting others.

## Signature

```python
download_files(
    self,
    paths: list[str],
) -> list[FileDownloadResponse]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `paths` | `list[str]` | Yes | List of file paths to download. |

## Returns

`list[FileDownloadResponse]`

List of `FileDownloadResponse` objects, one per input path.

Response order matches input order.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/langsmith.py#L294)
