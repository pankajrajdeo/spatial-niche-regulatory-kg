---
title: "InputTokenDetails"
description: "Breakdown of input token counts."
source: "https://reference.langchain.com/python/langchain-core/messages/ai/InputTokenDetails"
category: "reference"
tags: [reference, langchain-core, messages, ai, inputtokendetails]
---

# InputTokenDetails

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/ai/InputTokenDetails)

Breakdown of input token counts.

Does *not* need to sum to full input token count. Does *not* need to have all keys.

## Signature

```python
InputTokenDetails()
```

## Description

**Example:**

```python
{
    "audio": 10,
    "cache_creation": 200,
    "cache_read": 100,
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
    cache_creation: int,
    cache_read: int,
)
```

| Name | Type |
|------|------|
| `audio` | `int` |
| `cache_creation` | `int` |
| `cache_read` | `int` |

## Properties

- `audio`
- `cache_creation`
- `cache_read`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/ai.py#L38)
