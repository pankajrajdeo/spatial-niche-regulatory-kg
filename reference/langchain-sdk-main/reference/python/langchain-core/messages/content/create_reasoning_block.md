---
title: "create_reasoning_block"
description: "Create a ReasoningContentBlock."
source: "https://reference.langchain.com/python/langchain-core/messages/content/create_reasoning_block"
category: "reference"
tags: [reference, langchain-core, messages, content, create_reasoning_block]
---

# create_reasoning_block

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/create_reasoning_block)

Create a `ReasoningContentBlock`.

## Signature

```python
create_reasoning_block(
    reasoning: str | None = None,
    id: str | None = None,
    index: int | str | None = None,
    **kwargs: Any = {},
) -> ReasoningContentBlock
```

## Description

!!! note

The `id` is generated automatically if not provided, using a UUID4 format
prefixed with `'lc_'` to indicate it is a LangChain-generated ID.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `reasoning` | `str \| None` | No | The reasoning text or thought summary. (default: `None`) |
| `id` | `str \| None` | No | Content block identifier.  Generated automatically if not provided. (default: `None`) |
| `index` | `int \| str \| None` | No | Index of block in aggregate response.  Used during streaming. (default: `None`) |

## Returns

`ReasoningContentBlock`

A properly formatted `ReasoningContentBlock`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/content.py#L1363)
