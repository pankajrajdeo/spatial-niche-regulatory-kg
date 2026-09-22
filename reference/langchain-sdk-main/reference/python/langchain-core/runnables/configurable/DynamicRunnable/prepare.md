---
title: "prepare"
description: "Prepare the Runnable for invocation."
source: "https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/prepare"
category: "reference"
tags: [reference, langchain-core, runnables, configurable, dynamicrunnable, prepare]
---

# prepare

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/prepare)

Prepare the `Runnable` for invocation.

## Signature

```python
prepare(
    self,
    config: RunnableConfig | None = None,
) -> tuple[Runnable[Input, Output], RunnableConfig]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | No | The configuration to use. (default: `None`) |

## Returns

`tuple[Runnable[Input, Output], RunnableConfig]`

The prepared `Runnable` and configuration.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/configurable.py#L119)
