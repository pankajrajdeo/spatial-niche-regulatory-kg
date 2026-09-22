---
title: "add_usage"
description: "Recursively add two UsageMetadata objects."
source: "https://reference.langchain.com/python/langchain-core/tracers/langchain/add_usage"
category: "reference"
tags: [reference, langchain-core, tracers, langchain, add_usage]
---

# add_usage

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/ai/add_usage)

Recursively add two UsageMetadata objects.

## Signature

```python
add_usage(
    left: UsageMetadata | None,
    right: UsageMetadata | None,
) -> UsageMetadata
```

## Description

**Example:**

```python
from langchain_core.messages.ai import add_usage

left = UsageMetadata(
    input_tokens=5,
    output_tokens=0,
    total_tokens=5,
    input_token_details=InputTokenDetails(cache_read=3),
)
right = UsageMetadata(
    input_tokens=0,
    output_tokens=10,
    total_tokens=10,
    output_token_details=OutputTokenDetails(reasoning=4),
)

add_usage(left, right)
```

results in

```python
UsageMetadata(
    input_tokens=5,
    output_tokens=10,
    total_tokens=15,
    input_token_details=InputTokenDetails(cache_read=3),
    output_token_details=OutputTokenDetails(reasoning=4),
)
```

Args:
left: The first `UsageMetadata` object.
right: The second `UsageMetadata` object.

## Returns

`UsageMetadata`

The sum of the two `UsageMetadata` objects.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/messages/ai.py#L735)
