---
title: "get_callback_manager_for_config"
description: "Get a callback manager for a config."
source: "https://reference.langchain.com/python/langgraph/_internal/_config/get_callback_manager_for_config"
category: "reference"
tags: [reference, langgraph, internal, config, get_callback_manager_for_config]
---

# get_callback_manager_for_config

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_config/get_callback_manager_for_config)

Get a callback manager for a config.

## Signature

```python
get_callback_manager_for_config(
    config: RunnableConfig,
    tags: Sequence[str] | None = None,
) -> CallbackManager
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig` | Yes | The config. |

## Returns

`CallbackManager`

The callback manager.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/_internal/_config.py#L236)
