---
title: "OutputTokenDetails"
description: "Breakdown of output token counts."
source: "https://reference.langchain.com/python/langchain-core/messages/ai/OutputTokenDetails"
category: "reference"
tags: [reference, langchain-core, messages, ai, outputtokendetails]
---

# OutputTokenDetails

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/ai/OutputTokenDetails)

Breakdown of output token counts.

Does *not* need to sum to full output token count. Does *not* need to have all keys.

## Signature

```python
OutputTokenDetails()
```

## Description

**Example:**

```python
{
    "audio": 10,
    "reasoning": 200,
}
```

May also hold extra provider-specific keys.

!!! version-added "Added in `langchain-core` 0.3.9"

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    audio: int,
    reasoning: int,
)
```

| Name | Type |
|------|------|
| `audio` | `int` |
| `reasoning` | `int` |

## Properties

- `audio`
- `reasoning`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/ai.py#L74)
