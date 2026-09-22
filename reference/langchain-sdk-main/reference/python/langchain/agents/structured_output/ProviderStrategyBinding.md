---
title: "ProviderStrategyBinding"
description: "Information for tracking native structured output metadata."
source: "https://reference.langchain.com/python/langchain/agents/structured_output/ProviderStrategyBinding"
category: "reference"
tags: [reference, langchain, agents, structured_output, providerstrategybinding]
---

# ProviderStrategyBinding

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/structured_output/ProviderStrategyBinding)

Information for tracking native structured output metadata.

This contains all necessary information to handle structured responses generated via
native provider output, including the original schema, its type classification, and
parsing logic for provider-enforced JSON.

## Signature

```python
ProviderStrategyBinding(
    self,
    schema: type[SchemaT] | dict[str, Any],
    schema_kind: SchemaKind,
)
```

## Extends

- `Generic[SchemaT]`

## Constructors

```python
__init__(
    self,
    schema: type[SchemaT] | dict[str, Any],
    schema_kind: SchemaKind,
) -> None
```

| Name | Type |
|------|------|
| `schema` | `type[SchemaT] \| dict[str, Any]` |
| `schema_kind` | `SchemaKind` |

## Properties

- `schema`
- `schema_kind`

## Methods

- [`from_schema_spec()`](https://reference.langchain.com/python/langchain/agents/structured_output/ProviderStrategyBinding/from_schema_spec)
- [`parse()`](https://reference.langchain.com/python/langchain/agents/structured_output/ProviderStrategyBinding/parse)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/structured_output.py#L372)
