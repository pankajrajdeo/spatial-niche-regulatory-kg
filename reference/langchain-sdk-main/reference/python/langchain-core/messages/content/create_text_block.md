---
title: "create_text_block"
description: "Create a TextContentBlock."
source: "https://reference.langchain.com/python/langchain-core/messages/content/create_text_block"
category: "reference"
tags: [reference, langchain-core, messages, content, create_text_block]
---

# create_text_block

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/create_text_block)

Create a `TextContentBlock`.

## Signature

```python
create_text_block(
    text: str,
    *,
    id: str | None = None,
    annotations: list[Annotation] | None = None,
    index: int | str | None = None,
    **kwargs: Any = {},
) -> TextContentBlock
```

## Description

!!! note

The `id` is generated automatically if not provided, using a UUID4 format
prefixed with `'lc_'` to indicate it is a LangChain-generated ID.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The text content of the block. |
| `id` | `str \| None` | No | Content block identifier.  Generated automatically if not provided. (default: `None`) |
| `annotations` | `list[Annotation] \| None` | No | `Citation`s and other annotations for the text. (default: `None`) |
| `index` | `int \| str \| None` | No | Index of block in aggregate response.  Used during streaming. (default: `None`) |

## Returns

`TextContentBlock`

A properly formatted `TextContentBlock`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L950)
