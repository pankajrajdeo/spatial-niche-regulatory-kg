---
title: "ainvoke"
description: "Invoke this Runnable asynchronously."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda/ainvoke"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablelambda, ainvoke]
---

# ainvoke

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda/ainvoke)

Invoke this `Runnable` asynchronously.

## Signature

```python
ainvoke(
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L5332)
