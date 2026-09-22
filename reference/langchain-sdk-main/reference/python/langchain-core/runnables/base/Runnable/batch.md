---
title: "batch"
description: "Default implementation runs invoke in parallel using a thread pool executor."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/batch"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, batch]
---

# batch

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/batch)

Default implementation runs invoke in parallel using a thread pool executor.

The default implementation of batch works well for IO bound runnables.

Subclasses must override this method if they can batch more efficiently;
e.g., if the underlying `Runnable` uses an API which supports a batch mode.

## Signature

```python
batch(
    self,
    inputs: list[Input],
    config: RunnableConfig | list[RunnableConfig] | None = None,
    *,
    return_exceptions: bool = False,
    **kwargs: Any | None = {},
) -> list[Output]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `inputs` | `list[Input]` | Yes | A list of inputs to the `Runnable`. |
| `config` | `RunnableConfig \| list[RunnableConfig] \| None` | No | A config to use when invoking the `Runnable`. The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys.  Please refer to `RunnableConfig` for more details. (default: `None`) |
| `return_exceptions` | `bool` | No | Whether to return exceptions instead of raising them. (default: `False`) |
| `**kwargs` | `Any \| None` | No | Additional keyword arguments to pass to the `Runnable`. (default: `{}`) |

## Returns

`list[Output]`

A list of outputs from the `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L931)
