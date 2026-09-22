---
title: "ReasoningContentBlock"
description: "Reasoning output from a LLM."
source: "https://reference.langchain.com/python/langchain-core/messages/content/ReasoningContentBlock"
category: "reference"
tags: [reference, langchain-core, messages, content, reasoningcontentblock]
---

# ReasoningContentBlock

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/ReasoningContentBlock)

Reasoning output from a LLM.

!!! note "Factory function"

    `create_reasoning_block` may also be used as a factory to create a
    `ReasoningContentBlock`. Benefits include:

    * Automatic ID generation (when not provided)
    * Required arguments strictly validated at creation time

## Signature

```python
ReasoningContentBlock()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['reasoning'],
    id: NotRequired[str],
    reasoning: NotRequired[str],
    index: NotRequired[int | str],
    extras: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['reasoning']` |
| `id` | `NotRequired[str]` |
| `reasoning` | `NotRequired[str]` |
| `index` | `NotRequired[int \| str]` |
| `extras` | `NotRequired[dict[str, Any]]` |

## Properties

- `type`
- `id`
- `reasoning`
- `index`
- `extras`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L456)
