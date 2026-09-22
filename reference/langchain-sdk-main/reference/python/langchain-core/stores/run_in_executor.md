---
title: "run_in_executor"
description: "Run a function in an executor."
source: "https://reference.langchain.com/python/langchain-core/stores/run_in_executor"
category: "reference"
tags: [reference, langchain-core, stores, run_in_executor]
---

# run_in_executor

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/config/run_in_executor)

Run a function in an executor.

## Signature

```python
run_in_executor(
    executor_or_config: Executor | RunnableConfig | None,
    func: Callable[P, T],
    *args: P.args = (),
    **kwargs: P.kwargs = {},
) -> T
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `executor_or_config` | `Executor \| RunnableConfig \| None` | Yes | The executor or config to run in. |
| `func` | `Callable[P, T]` | Yes | The function. |
| `*args` | `P.args` | No | The positional arguments to the function. (default: `()`) |
| `**kwargs` | `P.kwargs` | No | The keyword arguments to the function. (default: `{}`) |

## Returns

`T`

The output of the function.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/config.py#L678)
