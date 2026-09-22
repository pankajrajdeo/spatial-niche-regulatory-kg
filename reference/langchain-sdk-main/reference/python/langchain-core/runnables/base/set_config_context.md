---
title: "set_config_context"
description: "Set the child Runnable config + tracing context."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/set_config_context"
category: "reference"
tags: [reference, langchain-core, runnables, base, set_config_context]
---

# set_config_context

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/config/set_config_context)

Set the child Runnable config + tracing context.

## Signature

```python
set_config_context(
    config: RunnableConfig,
) -> Generator[Context, None, None]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig` | Yes | The config to set. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/config.py#L223)
