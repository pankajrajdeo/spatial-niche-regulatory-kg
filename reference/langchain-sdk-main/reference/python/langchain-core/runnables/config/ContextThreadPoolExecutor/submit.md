---
title: "submit"
description: "Submit a function to the executor."
source: "https://reference.langchain.com/python/langchain-core/runnables/config/ContextThreadPoolExecutor/submit"
category: "reference"
tags: [reference, langchain-core, runnables, config, contextthreadpoolexecutor, submit]
---

# submit

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/config/ContextThreadPoolExecutor/submit)

Submit a function to the executor.

## Signature

```python
submit(
    self,
    func: Callable[P, T],
    *args: P.args = (),
    **kwargs: P.kwargs = {},
) -> Future[T]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Callable[P, T]` | Yes | The function to submit. |
| `*args` | `P.args` | No | The positional arguments to the function. (default: `()`) |
| `**kwargs` | `P.kwargs` | No | The keyword arguments to the function. (default: `{}`) |

## Returns

`Future[T]`

The future for the function.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/config.py#L610)
