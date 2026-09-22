---
title: "invoke"
description: "Invoke this Runnable synchronously."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda/invoke"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablelambda, invoke]
---

# invoke

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda/invoke)

Invoke this `Runnable` synchronously.

## Signature

```python
invoke(
    self,
    input: Input,
    config: RunnableConfig | None = None,
    **kwargs: Any | None = {},
) -> Output
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `Input` | Yes | The input to this `Runnable`. |
| `config` | `RunnableConfig \| None` | No | The config to use. (default: `None`) |
| `**kwargs` | `Any \| None` | No | Additional keyword arguments. (default: `{}`) |

## Returns

`Output`

The output of this `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L5301)
