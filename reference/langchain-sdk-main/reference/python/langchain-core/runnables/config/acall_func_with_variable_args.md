---
title: "acall_func_with_variable_args"
description: "Async call function that may optionally accept a run_manager and/or config."
source: "https://reference.langchain.com/python/langchain-core/runnables/config/acall_func_with_variable_args"
category: "reference"
tags: [reference, langchain-core, runnables, config, acall_func_with_variable_args]
---

# acall_func_with_variable_args

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/config/acall_func_with_variable_args)

Async call function that may optionally accept a run_manager and/or config.

## Signature

```python
acall_func_with_variable_args(
    func: Callable[[Input], Awaitable[Output]] | Callable[[Input, RunnableConfig], Awaitable[Output]] | Callable[[Input, AsyncCallbackManagerForChainRun], Awaitable[Output]] | Callable[[Input, AsyncCallbackManagerForChainRun, RunnableConfig], Awaitable[Output]],
    input: Input,
    config: RunnableConfig,
    run_manager: AsyncCallbackManagerForChainRun | None = None,
    **kwargs: Any = {},
) -> Awaitable[Output]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Callable[[Input], Awaitable[Output]] \| Callable[[Input, RunnableConfig], Awaitable[Output]] \| Callable[[Input, AsyncCallbackManagerForChainRun], Awaitable[Output]] \| Callable[[Input, AsyncCallbackManagerForChainRun, RunnableConfig], Awaitable[Output]]` | Yes | The function to call. |
| `input` | `Input` | Yes | The input to the function. |
| `config` | `RunnableConfig` | Yes | The config to pass to the function. |
| `run_manager` | `AsyncCallbackManagerForChainRun \| None` | No | The run manager to pass to the function. (default: `None`) |
| `**kwargs` | `Any` | No | The keyword arguments to pass to the function. (default: `{}`) |

## Returns

`Awaitable[Output]`

The output of the function.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/config.py#L529)
