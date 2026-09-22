---
title: "FileContentBlock"
description: "File data that doesn't fit into other multimodal block types."
source: "https://reference.langchain.com/python/langchain-core/messages/content/FileContentBlock"
category: "reference"
tags: [reference, langchain-core, messages, content, filecontentblock]
---

# FileContentBlock

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/FileContentBlock)

File data that doesn't fit into other multimodal block types.

This block is intended for files that are not images, audio, or plaintext. For
example, it can be used for PDFs, Word documents, etc.

If the file is an image, audio, or plaintext, you should use the corresponding
content block type (e.g., `ImageContentBlock`, `AudioContentBlock`,
`PlainTextContentBlock`).

!!! note "Factory function"

    `create_file_block` may also be used as a factory to create a
    `FileContentBlock`. Benefits include:

    * Automatic ID generation (when not provided)
    * Required arguments strictly validated at creation time

## Signature

```python
FileContentBlock()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['file'],
    id: NotRequired[str],
    file_id: NotRequired[str],
    mime_type: NotRequired[str],
    index: NotRequired[int | str],
    url: NotRequired[str],
    base64: NotRequired[str],
    extras: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['file']` |
| `id` | `NotRequired[str]` |
| `file_id` | `NotRequired[str]` |
| `mime_type` | `NotRequired[str]` |
| `index` | `NotRequired[int \| str]` |
| `url` | `NotRequired[str]` |
| `base64` | `NotRequired[str]` |
| `extras` | `NotRequired[dict[str, Any]]` |

## Properties

- `type`
- `id`
- `file_id`
- `mime_type`
- `index`
- `url`
- `base64`
- `extras`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L721)
