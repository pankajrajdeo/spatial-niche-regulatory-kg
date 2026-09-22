---
title: "BaseCallbackHandler"
description: "Base callback handler."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackHandler"
category: "reference"
tags: [reference, langchain-core, callbacks, base, basecallbackhandler]
---

# BaseCallbackHandler

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackHandler)

Base callback handler.

## Signature

```python
BaseCallbackHandler()
```

## Extends

- `LLMManagerMixin`
- `ChainManagerMixin`
- `ToolManagerMixin`
- `RetrieverManagerMixin`
- `CallbackManagerMixin`
- `RunManagerMixin`

## Properties

- `raise_error`
- `run_inline`
- `ignore_llm`
- `ignore_retry`
- `ignore_chain`
- `ignore_agent`
- `ignore_retriever`
- `ignore_chat_model`
- `ignore_custom_event`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L496)
