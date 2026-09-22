---
title: "NonStandardContentBlock"
description: "Provider-specific content data."
source: "https://reference.langchain.com/python/langchain-core/messages/content/NonStandardContentBlock"
category: "reference"
tags: [reference, langchain-core, messages, content, nonstandardcontentblock]
---

# NonStandardContentBlock

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/NonStandardContentBlock)

Provider-specific content data.

This block contains data for which there is not yet a standard type.

The purpose of this block should be to simply hold a provider-specific payload.
If a provider's non-standard output includes reasoning and tool calls, it should be
the adapter's job to parse that payload and emit the corresponding standard
`ReasoningContentBlock` and `ToolCalls`.

Has no `extras` field, as provider-specific data should be included in the
`value` field.

!!! note "Factory function"

    `create_non_standard_block` may also be used as a factory to create a
    `NonStandardContentBlock`. Benefits include:

    * Automatic ID generation (when not provided)
    * Required arguments strictly validated at creation time

## Signature

```python
NonStandardContentBlock()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['non_standard'],
    id: NotRequired[str],
    value: dict[str, Any],
    index: NotRequired[int | str],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['non_standard']` |
| `id` | `NotRequired[str]` |
| `value` | `dict[str, Any]` |
| `index` | `NotRequired[int \| str]` |

## Properties

- `type`
- `id`
- `value`
- `index`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L790)
