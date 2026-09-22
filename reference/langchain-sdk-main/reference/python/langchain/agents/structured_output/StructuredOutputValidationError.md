---
title: "StructuredOutputValidationError"
description: "Raised when structured output tool call arguments fail to parse according to the schema."
source: "https://reference.langchain.com/python/langchain/agents/structured_output/StructuredOutputValidationError"
category: "reference"
tags: [reference, langchain, agents, structured_output, structuredoutputvalidationerror]
---

# StructuredOutputValidationError

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/structured_output/StructuredOutputValidationError)

Raised when structured output tool call arguments fail to parse according to the schema.

## Signature

```python
StructuredOutputValidationError(
    self,
    tool_name: str,
    source: Exception,
    ai_message: AIMessage,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tool_name` | `str` | Yes | The name of the tool that failed. |
| `source` | `Exception` | Yes | The exception that occurred. |
| `ai_message` | `AIMessage` | Yes | The AI message that contained the invalid structured output. |

## Extends

- `StructuredOutputError`

## Constructors

```python
__init__(
    self,
    tool_name: str,
    source: Exception,
    ai_message: AIMessage,
) -> None
```

| Name | Type |
|------|------|
| `tool_name` | `str` |
| `source` | `Exception` |
| `ai_message` | `AIMessage` |

## Properties

- `tool_name`
- `source`
- `ai_message`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/structured_output.py#L60)
