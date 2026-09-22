---
title: "get_usage_metadata_callback"
description: "Get usage metadata callback."
source: "https://reference.langchain.com/python/langchain-core/callbacks/usage/get_usage_metadata_callback"
category: "reference"
tags: [reference, langchain-core, callbacks, usage, get_usage_metadata_callback]
---

# get_usage_metadata_callback

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/usage/get_usage_metadata_callback)

Get usage metadata callback.

Get context manager for tracking usage metadata across chat model calls using
[`AIMessage.usage_metadata`][langchain.messages.AIMessage.usage_metadata].

## Signature

```python
get_usage_metadata_callback(
    name: str = 'usage_metadata_callback',
) -> Generator[UsageMetadataCallbackHandler, None, None]
```

## Description

**Example:**

```python
from langchain.chat_models import init_chat_model
from langchain_core.callbacks import get_usage_metadata_callback

llm_1 = init_chat_model(model="openai:gpt-5.5")
llm_2 = init_chat_model(model="anthropic:claude-haiku-4-5-20251001")

with get_usage_metadata_callback() as cb:
    llm_1.invoke("Hello")
    llm_2.invoke("Hello")
    print(cb.usage_metadata)
```

!!! version-added "Added in `langchain-core` 0.3.49"

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `name` | `str` | No | The name of the context variable. (default: `'usage_metadata_callback'`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/usage.py#L80)
