---
title: "TextContentBlock"
description: "Text output from a LLM."
source: "https://reference.langchain.com/python/langchain-core/messages/content/TextContentBlock"
category: "reference"
tags: [reference, langchain-core, messages, content, textcontentblock]
---

# TextContentBlock

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/TextContentBlock)

Text output from a LLM.

This typically represents the main text content of a message, such as the response
from a language model or the text of a user message.

!!! note "Factory function"

    `create_text_block` may also be used as a factory to create a
    `TextContentBlock`. Benefits include:

    * Automatic ID generation (when not provided)
    * Required arguments strictly validated at creation time

## Signature

```python
TextContentBlock()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['text'],
    id: NotRequired[str],
    text: str,
    annotations: NotRequired[list[Annotation]],
    index: NotRequired[int | str],
    extras: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['text']` |
| `id` | `NotRequired[str]` |
| `text` | `str` |
| `annotations` | `NotRequired[list[Annotation]]` |
| `index` | `NotRequired[int \| str]` |
| `extras` | `NotRequired[dict[str, Any]]` |

## Properties

- `type`
- `id`
- `text`
- `annotations`
- `index`
- `extras`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L207)
