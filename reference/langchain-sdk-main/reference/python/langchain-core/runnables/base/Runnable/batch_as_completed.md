---
title: "batch_as_completed"
description: "Run invoke in parallel on a list of inputs."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/batch_as_completed"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, batch_as_completed]
---

# batch_as_completed

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/batch_as_completed)

Run `invoke` in parallel on a list of inputs.

Yields results as they complete.

## Signature

```python
batch_as_completed(
    self,
    inputs: Sequence[Input],
    config: RunnableConfig | Sequence[RunnableConfig] | None = None,
    *,
    return_exceptions: bool = False,
    **kwargs: Any | None = {},
) -> Iterator[tuple[int, Output | Exception]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `inputs` | `Sequence[Input]` | Yes | A list of inputs to the `Runnable`. |
| `config` | `RunnableConfig \| Sequence[RunnableConfig] \| None` | No | A config to use when invoking the `Runnable`.  The config supports standard keys like `'tags'`, `'metadata'` for tracing purposes, `'max_concurrency'` for controlling how much work to do in parallel, and other keys.  Please refer to `RunnableConfig` for more details. (default: `None`) |
| `return_exceptions` | `bool` | No | Whether to return exceptions instead of raising them. (default: `False`) |
| `**kwargs` | `Any \| None` | No | Additional keyword arguments to pass to the `Runnable`. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L1001)
