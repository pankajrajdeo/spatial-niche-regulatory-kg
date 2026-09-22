---
title: "PlainTextContentBlock"
description: "Plaintext data (e.g., from a .txt or .md document)."
source: "https://reference.langchain.com/python/langchain-core/messages/content/PlainTextContentBlock"
category: "reference"
tags: [reference, langchain-core, messages, content, plaintextcontentblock]
---

# PlainTextContentBlock

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/PlainTextContentBlock)

Plaintext data (e.g., from a `.txt` or `.md` document).

!!! note

    A `PlainTextContentBlock` existed in `langchain-core<1.0.0`. Although the
    name has carried over, the structure has changed significantly. The only shared
    keys between the old and new versions are `type` and `text`, though the
    `type` value has changed from `'text'` to `'text-plain'`.

!!! note

    Title and context are optional fields that may be passed to the model. See
    Anthropic [example](https://platform.claude.com/docs/en/build-with-claude/citations#citable-vs-non-citable-content).

!!! note "Factory function"

    `create_plaintext_block` may also be used as a factory to create a
    `PlainTextContentBlock`. Benefits include:

    * Automatic ID generation (when not provided)
    * Required arguments strictly validated at creation time

## Signature

```python
PlainTextContentBlock()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['text-plain'],
    id: NotRequired[str],
    file_id: NotRequired[str],
    mime_type: Literal['text/plain'],
    index: NotRequired[int | str],
    url: NotRequired[str],
    base64: NotRequired[str],
    text: NotRequired[str],
    title: NotRequired[str],
    context: NotRequired[str],
    extras: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['text-plain']` |
| `id` | `NotRequired[str]` |
| `file_id` | `NotRequired[str]` |
| `mime_type` | `Literal['text/plain']` |
| `index` | `NotRequired[int \| str]` |
| `url` | `NotRequired[str]` |
| `base64` | `NotRequired[str]` |
| `text` | `NotRequired[str]` |
| `title` | `NotRequired[str]` |
| `context` | `NotRequired[str]` |
| `extras` | `NotRequired[dict[str, Any]]` |

## Properties

- `type`
- `id`
- `file_id`
- `mime_type`
- `index`
- `url`
- `base64`
- `text`
- `title`
- `context`
- `extras`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L651)
