---
title: "VideoContentBlock"
description: "Video data."
source: "https://reference.langchain.com/python/langchain-core/messages/content/VideoContentBlock"
category: "reference"
tags: [reference, langchain-core, messages, content, videocontentblock]
---

# VideoContentBlock

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/VideoContentBlock)

Video data.

!!! note "Factory function"

    `create_video_block` may also be used as a factory to create a
    `VideoContentBlock`. Benefits include:

    * Automatic ID generation (when not provided)
    * Required arguments strictly validated at creation time

## Signature

```python
VideoContentBlock()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['video'],
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
| `type` | `Literal['video']` |
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L549)
