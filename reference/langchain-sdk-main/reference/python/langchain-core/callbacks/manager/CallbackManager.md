---
title: "CallbackManager"
description: "Callback manager for LangChain."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanager]
---

# CallbackManager

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager)

Callback manager for LangChain.

## Signature

```python
CallbackManager(
    self,
    handlers: list[BaseCallbackHandler],
    inheritable_handlers: list[BaseCallbackHandler] | None = None,
    parent_run_id: UUID | None = None,
    *,
    tags: list[str] | None = None,
    inheritable_tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
    inheritable_metadata: dict[str, Any] | None = None,
)
```

## Extends

- `BaseCallbackManager`

## Methods

- [`on_llm_start()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/on_llm_start)
- [`on_chat_model_start()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/on_chat_model_start)
- [`on_chain_start()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/on_chain_start)
- [`on_tool_start()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/on_tool_start)
- [`on_retriever_start()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/on_retriever_start)
- [`on_custom_event()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/on_custom_event)
- [`configure()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/configure)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L1377)
