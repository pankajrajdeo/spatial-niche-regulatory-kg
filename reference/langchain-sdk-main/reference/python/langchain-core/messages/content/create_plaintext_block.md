---
title: "create_plaintext_block"
description: "Create a PlainTextContentBlock."
source: "https://reference.langchain.com/python/langchain-core/messages/content/create_plaintext_block"
category: "reference"
tags: [reference, langchain-core, messages, content, create_plaintext_block]
---

# create_plaintext_block

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/create_plaintext_block)

Create a `PlainTextContentBlock`.

## Signature

```python
create_plaintext_block(
    text: str | None = None,
    url: str | None = None,
    base64: str | None = None,
    file_id: str | None = None,
    title: str | None = None,
    context: str | None = None,
    id: str | None = None,
    index: int | str | None = None,
    **kwargs: Any = {},
) -> PlainTextContentBlock
```

## Description

!!! note

The `id` is generated automatically if not provided, using a UUID4 format
prefixed with `'lc_'` to indicate it is a LangChain-generated ID.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str \| None` | No | The plaintext content. (default: `None`) |
| `url` | `str \| None` | No | URL of the plaintext file. (default: `None`) |
| `base64` | `str \| None` | No | Base64-encoded plaintext data. (default: `None`) |
| `file_id` | `str \| None` | No | ID of the plaintext file from a file storage system. (default: `None`) |
| `title` | `str \| None` | No | Title of the text data. (default: `None`) |
| `context` | `str \| None` | No | Context or description of the text content. (default: `None`) |
| `id` | `str \| None` | No | Content block identifier.  Generated automatically if not provided. (default: `None`) |
| `index` | `int \| str \| None` | No | Index of block in aggregate response.  Used during streaming. (default: `None`) |

## Returns

`PlainTextContentBlock`

A properly formatted `PlainTextContentBlock`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L1255)
