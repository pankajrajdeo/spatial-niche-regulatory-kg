---
title: "PIIDetectionError"
description: "Raised when configured to block on detected sensitive values."
source: "https://reference.langchain.com/python/langchain/agents/middleware/_redaction/PIIDetectionError"
category: "reference"
tags: [reference, langchain, agents, middleware, redaction, piidetectionerror]
---

# PIIDetectionError

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_redaction/PIIDetectionError)

Raised when configured to block on detected sensitive values.

## Signature

```python
PIIDetectionError(
    self,
    pii_type: str,
    matches: Sequence[PIIMatch],
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `pii_type` | `str` | Yes | Name of the detected sensitive type. |
| `matches` | `Sequence[PIIMatch]` | Yes | All matches that were detected for that type. |

## Extends

- `Exception`

## Constructors

```python
__init__(
    self,
    pii_type: str,
    matches: Sequence[PIIMatch],
) -> None
```

| Name | Type |
|------|------|
| `pii_type` | `str` |
| `matches` | `Sequence[PIIMatch]` |

## Properties

- `pii_type`
- `matches`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/_redaction.py#L29)
