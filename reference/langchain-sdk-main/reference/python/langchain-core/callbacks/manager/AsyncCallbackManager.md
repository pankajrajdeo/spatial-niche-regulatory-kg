---
title: "AsyncCallbackManager"
description: "Async callback manager that handles callbacks from LangChain."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManager"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asynccallbackmanager]
---

# AsyncCallbackManager

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManager)

Async callback manager that handles callbacks from LangChain.

## Signature

```python
AsyncCallbackManager(
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

## Properties

- `is_async`

## Methods

- [`on_llm_start()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManager/on_llm_start)
- [`on_chat_model_start()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManager/on_chat_model_start)
- [`on_chain_start()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManager/on_chain_start)
- [`on_tool_start()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManager/on_tool_start)
- [`on_custom_event()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManager/on_custom_event)
- [`on_retriever_start()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManager/on_retriever_start)
- [`configure()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManager/configure)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L1859)
