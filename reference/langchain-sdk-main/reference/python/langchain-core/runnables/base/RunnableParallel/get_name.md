---
title: "get_name"
description: "Get the name of the Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/get_name"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnableparallel, get_name]
---

# get_name

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/get_name)

Get the name of the `Runnable`.

## Signature

```python
get_name(
    self,
    suffix: str | None = None,
    *,
    name: str | None = None,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `suffix` | `str \| None` | No | The suffix to use. (default: `None`) |
| `name` | `str \| None` | No | The name to use. (default: `None`) |

## Returns

`str`

The name of the `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L3996)
