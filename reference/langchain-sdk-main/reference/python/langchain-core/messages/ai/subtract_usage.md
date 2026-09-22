---
title: "subtract_usage"
description: "Recursively subtract two UsageMetadata objects."
source: "https://reference.langchain.com/python/langchain-core/messages/ai/subtract_usage"
category: "reference"
tags: [reference, langchain-core, messages, ai, subtract_usage]
---

# subtract_usage

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/ai/subtract_usage)

Recursively subtract two `UsageMetadata` objects.

Token counts cannot be negative so the actual operation is `max(left - right, 0)`.

## Signature

```python
subtract_usage(
    left: UsageMetadata | None,
    right: UsageMetadata | None,
) -> UsageMetadata
```

## Description

**Example:**

```python
from langchain_core.messages.ai import subtract_usage

left = UsageMetadata(
    input_tokens=5,
    output_tokens=10,
    total_tokens=15,
    input_token_details=InputTokenDetails(cache_read=4),
)
right = UsageMetadata(
    input_tokens=3,
    output_tokens=8,
    total_tokens=11,
    output_token_details=OutputTokenDetails(reasoning=4),
)

subtract_usage(left, right)
```

results in

```python
UsageMetadata(
    input_tokens=2,
    output_tokens=2,
    total_tokens=4,
    input_token_details=InputTokenDetails(cache_read=4),
    output_token_details=OutputTokenDetails(reasoning=0),
)
```

Args:
left: The first `UsageMetadata` object.
right: The second `UsageMetadata` object.

## Returns

`UsageMetadata`

The resulting `UsageMetadata` after subtraction.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/ai.py#L794)
