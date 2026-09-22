---
title: "Citation"
description: "Annotation for citing data from a document."
source: "https://reference.langchain.com/python/langchain-core/messages/content/Citation"
category: "reference"
tags: [reference, langchain-core, messages, content, citation]
---

# Citation

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/Citation)

Annotation for citing data from a document.

!!! note

    `start`/`end` indices refer to the **response text**,
    not the source text. This means that the indices are relative to the model's
    response, not the original document (as specified in the `url`).

!!! note "Factory function"

    `create_citation` may also be used as a factory to create a `Citation`.
    Benefits include:

    * Automatic ID generation (when not provided)
    * Required arguments strictly validated at creation time

## Signature

```python
Citation()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['citation'],
    id: NotRequired[str],
    url: NotRequired[str],
    title: NotRequired[str],
    start_index: NotRequired[int],
    end_index: NotRequired[int],
    cited_text: NotRequired[str],
    extras: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['citation']` |
| `id` | `NotRequired[str]` |
| `url` | `NotRequired[str]` |
| `title` | `NotRequired[str]` |
| `start_index` | `NotRequired[int]` |
| `end_index` | `NotRequired[int]` |
| `cited_text` | `NotRequired[str]` |
| `extras` | `NotRequired[dict[str, Any]]` |

## Properties

- `type`
- `id`
- `url`
- `title`
- `start_index`
- `end_index`
- `cited_text`
- `extras`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L126)
