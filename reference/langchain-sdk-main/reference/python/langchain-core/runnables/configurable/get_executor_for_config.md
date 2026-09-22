---
title: "get_executor_for_config"
description: "Get an executor for a config."
source: "https://reference.langchain.com/python/langchain-core/runnables/configurable/get_executor_for_config"
category: "reference"
tags: [reference, langchain-core, runnables, configurable, get_executor_for_config]
---

# get_executor_for_config

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/config/get_executor_for_config)

Get an executor for a config.

## Signature

```python
get_executor_for_config(
    config: RunnableConfig | None,
) -> Generator[Executor, None, None]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | Yes | The config. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/config.py#L659)
