---
title: "download_files"
description: "Download multiple files from the sandbox."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/download_files"
category: "reference"
tags: [reference, deepagents, backends, protocol, backendprotocol, download_files]
---

# download_files

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/BackendProtocol/download_files)

Download multiple files from the sandbox.

This API is designed to allow developers to use it either directly or
by exposing it to LLMs via custom tools.

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

Response order matches input order (`response[i] for paths[i]`).

Check the error field to determine success/failure per file.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/backends/protocol.py#L786)
