---
title: "ensure_config"
description: "Ensure that a config is a dict with all keys present."
source: "https://reference.langchain.com/python/langchain-core/runnables/passthrough/ensure_config"
category: "reference"
tags: [reference, langchain-core, runnables, passthrough, ensure_config]
---

# ensure_config

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/config/ensure_config)

Ensure that a config is a dict with all keys present.

## Signature

```python
ensure_config(
    config: RunnableConfig | None = None,
) -> RunnableConfig
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | No | The config to ensure. (default: `None`) |

## Returns

`RunnableConfig`

The ensured config.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/config.py#L255)
