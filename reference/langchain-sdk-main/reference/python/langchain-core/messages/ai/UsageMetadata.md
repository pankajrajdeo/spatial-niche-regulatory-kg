---
title: "UsageMetadata"
description: "Usage metadata for a message, such as token counts."
source: "https://reference.langchain.com/python/langchain-core/messages/ai/UsageMetadata"
category: "reference"
tags: [reference, langchain-core, messages, ai, usagemetadata]
---

# UsageMetadata

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/ai/UsageMetadata)

Usage metadata for a message, such as token counts.

This is a standard representation of token usage that is consistent across models.

## Signature

```python
UsageMetadata()
```

## Description

**Example:**

```python
{
    "input_tokens": 350,
    "output_tokens": 240,
    "total_tokens": 590,
    "input_token_details": {
        "audio": 10,
        "cache_creation": 200,
        "cache_read": 100,
    },
    "output_token_details": {
        "audio": 10,
        "reasoning": 200,
    },
}
```

!!! warning "Behavior changed in `langchain-core` 0.3.9"

    Added `input_token_details` and `output_token_details`.

!!! note "LangSmith SDK"

    The LangSmith SDK also has a `UsageMetadata` class. While the two share fields,
    LangSmith's `UsageMetadata` has additional fields to capture cost information
    used by the LangSmith platform.

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    input_tokens: int,
    output_tokens: int,
    total_tokens: int,
    input_token_details: NotRequired[InputTokenDetails],
    output_token_details: NotRequired[OutputTokenDetails],
)
```

| Name | Type |
|------|------|
| `input_tokens` | `int` |
| `output_tokens` | `int` |
| `total_tokens` | `int` |
| `input_token_details` | `NotRequired[InputTokenDetails]` |
| `output_token_details` | `NotRequired[OutputTokenDetails]` |

## Properties

- `input_tokens`
- `output_tokens`
- `total_tokens`
- `input_token_details`
- `output_token_details`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/ai.py#L104)
