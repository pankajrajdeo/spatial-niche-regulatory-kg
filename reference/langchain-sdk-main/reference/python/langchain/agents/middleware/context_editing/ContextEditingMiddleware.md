---
title: "ContextEditingMiddleware"
description: "Automatically prune tool results to manage context size."
source: "https://reference.langchain.com/python/langchain/agents/middleware/context_editing/ContextEditingMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, context_editing, contexteditingmiddleware]
---

# ContextEditingMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/context_editing/ContextEditingMiddleware)

Automatically prune tool results to manage context size.

The middleware applies a sequence of edits when the total input token count exceeds
configured thresholds.

Currently the `ClearToolUsesEdit` strategy is supported, aligning with Anthropic's
`clear_tool_uses_20250919` behavior [(read more)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool).

## Signature

```python
ContextEditingMiddleware(
    self,
    *,
    edits: Iterable[ContextEdit] | None = None,
    token_count_method: Literal['approximate', 'model'] = 'approximate',
    token_counter: TokenCounter | None = None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `edits` | `Iterable[ContextEdit] \| None` | No | Sequence of edit strategies to apply.  Defaults to a single `ClearToolUsesEdit` mirroring Anthropic defaults. (default: `None`) |
| `token_count_method` | `Literal['approximate', 'model']` | No | Whether to use approximate token counting (faster, less accurate) or exact counting implemented by the chat model (potentially slower, more accurate).  Ignored when `token_counter` is provided. (default: `'approximate'`) |
| `token_counter` | `TokenCounter \| None` | No | Optional custom function counting tokens for a sequence of messages. Takes precedence over `token_count_method` when provided, mirroring `SummarizationMiddleware`. Useful when the built-in approximation is inaccurate for a workload (e.g. CJK-heavy conversations) or when a provider-specific tokenizer should be used without implementing `get_num_tokens_from_messages`. (default: `None`) |

## Extends

- `AgentMiddleware[AgentState[ResponseT], ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    *,
    edits: Iterable[ContextEdit] | None = None,
    token_count_method: Literal['approximate', 'model'] = 'approximate',
    token_counter: TokenCounter | None = None,
) -> None
```

| Name | Type |
|------|------|
| `edits` | `Iterable[ContextEdit] \| None` |
| `token_count_method` | `Literal['approximate', 'model']` |
| `token_counter` | `TokenCounter \| None` |

## Properties

- `edits`
- `token_count_method`
- `token_counter`

## Methods

- [`wrap_model_call()`](https://reference.langchain.com/python/langchain/agents/middleware/context_editing/ContextEditingMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/langchain/agents/middleware/context_editing/ContextEditingMiddleware/awrap_model_call)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/context_editing.py#L187)
