---
title: "AsyncCallbackHandler"
description: "Base async callback handler."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler"
category: "reference"
tags: [reference, langchain-core, callbacks, base, asynccallbackhandler]
---

# AsyncCallbackHandler

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler)

Base async callback handler.

## Signature

```python
AsyncCallbackHandler()
```

## Extends

- `BaseCallbackHandler`

## Methods

- [`on_llm_start()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_llm_start)
- [`on_chat_model_start()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_chat_model_start)
- [`on_llm_new_token()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_llm_new_token)
- [`on_llm_end()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_llm_end)
- [`on_llm_error()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_llm_error)
- [`on_stream_event()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_stream_event)
- [`on_chain_start()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_chain_start)
- [`on_chain_end()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_chain_end)
- [`on_chain_error()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_chain_error)
- [`on_tool_start()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_tool_start)
- [`on_tool_end()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_tool_end)
- [`on_tool_error()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_tool_error)
- [`on_text()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_text)
- [`on_retry()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_retry)
- [`on_agent_action()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_agent_action)
- [`on_agent_finish()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_agent_finish)
- [`on_retriever_start()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_retriever_start)
- [`on_retriever_end()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_retriever_end)
- [`on_retriever_error()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_retriever_error)
- [`on_custom_event()`](https://reference.langchain.com/python/langchain-core/callbacks/base/AsyncCallbackHandler/on_custom_event)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L548)
