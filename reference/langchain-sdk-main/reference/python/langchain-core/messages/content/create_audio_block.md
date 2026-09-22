---
title: "create_audio_block"
description: "Create an AudioContentBlock."
source: "https://reference.langchain.com/python/langchain-core/messages/content/create_audio_block"
category: "reference"
tags: [reference, langchain-core, messages, content, create_audio_block]
---

# create_audio_block

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/create_audio_block)

Create an `AudioContentBlock`.

## Signature

```python
create_audio_block(
    *,
    url: str | None = None,
    base64: str | None = None,
    file_id: str | None = None,
    mime_type: str | None = None,
    id: str | None = None,
    index: int | str | None = None,
    **kwargs: Any = {},
) -> AudioContentBlock
```

## Description

!!! note

The `id` is generated automatically if not provided, using a UUID4 format
prefixed with `'lc_'` to indicate it is a LangChain-generated ID.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `url` | `str \| None` | No | URL of the audio. (default: `None`) |
| `base64` | `str \| None` | No | Base64-encoded audio data. (default: `None`) |
| `file_id` | `str \| None` | No | ID of the audio file from a file storage system. (default: `None`) |
| `mime_type` | `str \| None` | No | MIME type of the audio.  Required for base64 data. (default: `None`) |
| `id` | `str \| None` | No | Content block identifier.  Generated automatically if not provided. (default: `None`) |
| `index` | `int \| str \| None` | No | Index of block in aggregate response.  Used during streaming. (default: `None`) |

## Returns

`AudioContentBlock`

A properly formatted `AudioContentBlock`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L1123)
