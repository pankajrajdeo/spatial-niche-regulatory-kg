---
title: "ProviderStrategy"
description: "Use the model provider's native structured output method."
source: "https://reference.langchain.com/python/langchain/agents/structured_output/ProviderStrategy"
category: "reference"
tags: [reference, langchain, agents, structured_output, providerstrategy]
---

# ProviderStrategy

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/structured_output/ProviderStrategy)

Use the model provider's native structured output method.

## Signature

```python
ProviderStrategy(
    self,
    schema: type[SchemaT] | dict[str, Any],
    *,
    strict: bool | None = None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `schema` | `type[SchemaT] \| dict[str, Any]` | Yes | Schema to enforce via the provider's native structured output. |
| `strict` | `bool \| None` | No | Whether to request strict provider-side schema enforcement. (default: `None`) |

## Extends

- `Generic[SchemaT]`

## Constructors

```python
__init__(
    self,
    schema: type[SchemaT] | dict[str, Any],
    *,
    strict: bool | None = None,
) -> None
```

| Name | Type |
|------|------|
| `schema` | `type[SchemaT] \| dict[str, Any]` |
| `strict` | `bool \| None` |

## Properties

- `schema`
- `schema_spec`

## Methods

- [`to_model_kwargs()`](https://reference.langchain.com/python/langchain/agents/structured_output/ProviderStrategy/to_model_kwargs)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/structured_output.py#L270)
