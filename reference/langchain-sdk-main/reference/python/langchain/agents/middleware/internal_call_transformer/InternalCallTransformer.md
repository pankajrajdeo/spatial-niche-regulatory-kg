---
title: "InternalCallTransformer"
description: "Keep internal model calls out of run.messages and the raw event log."
source: "https://reference.langchain.com/python/langchain/agents/middleware/internal_call_transformer/InternalCallTransformer"
category: "reference"
tags: [reference, langchain, agents, middleware, internal_call_transformer, internalcalltransformer]
---

# InternalCallTransformer

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/internal_call_transformer/InternalCallTransformer)

Keep internal model calls out of `run.messages` and the raw event log.

Used by middleware that makes internal model calls and runs before built-in
transformers.

For tagged events, streamed `message-start` events are marked as tool-role and
whole-`AIMessage` payloads are cleared so `MessagesTransformer` ignores them.
The mutated events are then dropped from the raw log.

Only events within this transformer's scope are modified.

## Signature

```python
InternalCallTransformer(
    self,
    scope: tuple[str, ...] = (),
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `scope` | `tuple[str, ...]` | No | The namespace tuple the owning mux is scoped to. (default: `()`) |

## Extends

- `StreamTransformer`

## Constructors

```python
__init__(
    self,
    scope: tuple[str, ...] = (),
) -> None
```

| Name | Type |
|------|------|
| `scope` | `tuple[str, ...]` |

## Properties

- `before_builtins`
- `required_stream_modes`

## Methods

- [`init()`](https://reference.langchain.com/python/langchain/agents/middleware/internal_call_transformer/InternalCallTransformer/init)
- [`process()`](https://reference.langchain.com/python/langchain/agents/middleware/internal_call_transformer/InternalCallTransformer/process)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/internal_call_transformer.py#L43)
