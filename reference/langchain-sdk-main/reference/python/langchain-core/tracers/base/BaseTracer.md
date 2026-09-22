---
title: "BaseTracer"
description: "Base interface for tracers."
source: "https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer"
category: "reference"
tags: [reference, langchain-core, tracers, base, basetracer]
---

# BaseTracer

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer)

Base interface for tracers.

## Signature

```python
BaseTracer(
    self,
    *,
    _schema_format: Literal['original', 'streaming_events', 'original+chat'] = 'original',
    run_map: dict[str, Run] | None = None,
    order_map: dict[UUID, tuple[UUID, str]] | None = None,
    _external_run_ids: dict[str, int] | None = None,
    **kwargs: Any = {},
)
```

## Extends

- `_TracerCore`
- `BaseCallbackHandler`
- `ABC`

## Methods

- [`on_chat_model_start()`](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_chat_model_start)
- [`on_llm_start()`](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_llm_start)
- [`on_llm_new_token()`](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_llm_new_token)
- [`on_retry()`](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_retry)
- [`on_llm_end()`](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_llm_end)
- [`on_llm_error()`](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_llm_error)
- [`on_chain_start()`](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_chain_start)
- [`on_chain_end()`](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_chain_end)
- [`on_chain_error()`](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_chain_error)
- [`on_tool_start()`](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_tool_start)
- [`on_tool_end()`](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_tool_end)
- [`on_tool_error()`](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_tool_error)
- [`on_retriever_start()`](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_retriever_start)
- [`on_retriever_error()`](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_retriever_error)
- [`on_retriever_end()`](https://reference.langchain.com/python/langchain-core/tracers/base/BaseTracer/on_retriever_end)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/base.py#L33)
