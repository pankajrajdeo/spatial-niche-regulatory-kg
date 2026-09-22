---
title: "stream"
description: "First evaluates the condition, then delegate to True or False branch."
source: "https://reference.langchain.com/python/langchain-core/runnables/branch/RunnableBranch/stream"
category: "reference"
tags: [reference, langchain-core, runnables, branch, runnablebranch, stream]
---

# stream

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/branch/RunnableBranch/stream)

First evaluates the condition, then delegate to `True` or `False` branch.

## Signature

```python
stream(
    self,
    input: Input,
    config: RunnableConfig | None = None,
    **kwargs: Any | None = {},
) -> Iterator[Output]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `Input` | Yes | The input to the `Runnable`. |
| `config` | `RunnableConfig \| None` | No | The configuration for the `Runnable`. (default: `None`) |
| `**kwargs` | `Any \| None` | No | Additional keyword arguments to pass to the `Runnable`. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/branch.py#L291)
