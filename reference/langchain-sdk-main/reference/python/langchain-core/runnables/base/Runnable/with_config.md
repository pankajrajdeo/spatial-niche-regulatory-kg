---
title: "with_config"
description: "Bind config to a Runnable, returning a new Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/with_config"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, with_config]
---

# with_config

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/with_config)

Bind config to a `Runnable`, returning a new `Runnable`.

## Signature

```python
with_config(
    self,
    config: RunnableConfig | None = None,
    **kwargs: Any = {},
) -> Runnable[Input, Output]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | No | The config to bind to the `Runnable`. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments to pass to the `Runnable`. (default: `{}`) |

## Returns

`Runnable[Input, Output]`

A new `Runnable` with the config bound.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L1885)
