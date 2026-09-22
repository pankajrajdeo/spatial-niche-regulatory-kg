---
title: "CallbackManagerForLLMRun"
description: "Callback manager for LLM run."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForLLMRun"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanagerforllmrun]
---

# CallbackManagerForLLMRun

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForLLMRun)

Callback manager for LLM run.

## Signature

```python
CallbackManagerForLLMRun(
    self,
    *,
    run_id: UUID,
    handlers: list[BaseCallbackHandler],
    inheritable_handlers: list[BaseCallbackHandler],
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    inheritable_tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
    inheritable_metadata: dict[str, Any] | None = None,
)
```

## Extends

- `RunManager`
- `LLMManagerMixin`

## Methods

- [`on_llm_new_token()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForLLMRun/on_llm_new_token)
- [`on_llm_end()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForLLMRun/on_llm_end)
- [`on_llm_error()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForLLMRun/on_llm_error)
- [`on_stream_event()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForLLMRun/on_stream_event)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L705)
