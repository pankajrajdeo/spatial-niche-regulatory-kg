---
title: "UsageMetadataCallbackHandler"
description: "Callback Handler that tracks AIMessage.usage_metadata."
source: "https://reference.langchain.com/python/langchain-core/callbacks/usage/UsageMetadataCallbackHandler"
category: "reference"
tags: [reference, langchain-core, callbacks, usage, usagemetadatacallbackhandler]
---

# UsageMetadataCallbackHandler

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/usage/UsageMetadataCallbackHandler)

Callback Handler that tracks `AIMessage.usage_metadata`.

## Signature

```python
UsageMetadataCallbackHandler(
    self,
)
```

## Description

**Example:**

```python
from langchain.chat_models import init_chat_model
from langchain_core.callbacks import UsageMetadataCallbackHandler

llm_1 = init_chat_model(model="openai:gpt-5.5")
llm_2 = init_chat_model(model="anthropic:claude-haiku-4-5-20251001")

callback = UsageMetadataCallbackHandler()
result_1 = llm_1.invoke("Hello", config={"callbacks": [callback]})
result_2 = llm_2.invoke("Hello", config={"callbacks": [callback]})
callback.usage_metadata
```

!!! version-added "Added in `langchain-core` 0.3.49"

## Extends

- `BaseCallbackHandler`

## Constructors

```python
__init__(
    self,
) -> None
```

## Properties

- `usage_metadata`

## Methods

- [`on_llm_end()`](https://reference.langchain.com/python/langchain-core/callbacks/usage/UsageMetadataCallbackHandler/on_llm_end)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/usage.py#L18)
