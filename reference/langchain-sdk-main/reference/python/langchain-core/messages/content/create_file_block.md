---
title: "create_file_block"
description: "Create a FileContentBlock."
source: "https://reference.langchain.com/python/langchain-core/messages/content/create_file_block"
category: "reference"
tags: [reference, langchain-core, messages, content, create_file_block]
---

# create_file_block

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/create_file_block)

Create a `FileContentBlock`.

## Signature

```python
create_file_block(
    *,
    url: str | None = None,
    base64: str | None = None,
    file_id: str | None = None,
    mime_type: str | None = None,
    id: str | None = None,
    index: int | str | None = None,
    **kwargs: Any = {},
) -> FileContentBlock
```

## Description

!!! note

The `id` is generated automatically if not provided, using a UUID4 format
prefixed with `'lc_'` to indicate it is a LangChain-generated ID.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `url` | `str \| None` | No | URL of the file. (default: `None`) |
| `base64` | `str \| None` | No | Base64-encoded file data. (default: `None`) |
| `file_id` | `str \| None` | No | ID of the file from a file storage system. (default: `None`) |
| `mime_type` | `str \| None` | No | MIME type of the file.  Required for base64 data. (default: `None`) |
| `id` | `str \| None` | No | Content block identifier.  Generated automatically if not provided. (default: `None`) |
| `index` | `int \| str \| None` | No | Index of block in aggregate response.  Used during streaming. (default: `None`) |

## Returns

`FileContentBlock`

A properly formatted `FileContentBlock`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L1189)
