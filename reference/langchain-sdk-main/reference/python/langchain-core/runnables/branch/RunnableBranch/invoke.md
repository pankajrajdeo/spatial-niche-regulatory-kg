---
title: "invoke"
description: "First evaluates the condition, then delegate to True or False branch."
source: "https://reference.langchain.com/python/langchain-core/runnables/branch/RunnableBranch/invoke"
category: "reference"
tags: [reference, langchain-core, runnables, branch, runnablebranch, invoke]
---

# invoke

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/branch/RunnableBranch/invoke)

First evaluates the condition, then delegate to `True` or `False` branch.

## Signature

```python
invoke(
    self,
    input: Input,
    config: RunnableConfig | None = None,
    **kwargs: Any = {},
) -> Output
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `Input` | Yes | The input to the `Runnable`. |
| `config` | `RunnableConfig \| None` | No | The configuration for the `Runnable`. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments to pass to the `Runnable`. (default: `{}`) |

## Returns

`Output`

The output of the branch that was run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/branch.py#L184)
