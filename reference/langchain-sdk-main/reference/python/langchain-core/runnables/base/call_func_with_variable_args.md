---
title: "call_func_with_variable_args"
description: "Call function that may optionally accept a run_manager and/or config."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/call_func_with_variable_args"
category: "reference"
tags: [reference, langchain-core, runnables, base, call_func_with_variable_args]
---

# call_func_with_variable_args

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/config/call_func_with_variable_args)

Call function that may optionally accept a run_manager and/or config.

## Signature

```python
call_func_with_variable_args(
    func: Callable[[Input], Output] | Callable[[Input, RunnableConfig], Output] | Callable[[Input, CallbackManagerForChainRun], Output] | Callable[[Input, CallbackManagerForChainRun, RunnableConfig], Output],
    input: Input,
    config: RunnableConfig,
    run_manager: CallbackManagerForChainRun | None = None,
    **kwargs: Any = {},
) -> Output
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Callable[[Input], Output] \| Callable[[Input, RunnableConfig], Output] \| Callable[[Input, CallbackManagerForChainRun], Output] \| Callable[[Input, CallbackManagerForChainRun, RunnableConfig], Output]` | Yes | The function to call. |
| `input` | `Input` | Yes | The input to the function. |
| `config` | `RunnableConfig` | Yes | The config to pass to the function. |
| `run_manager` | `CallbackManagerForChainRun \| None` | No | The run manager to pass to the function. (default: `None`) |
| `**kwargs` | `Any` | No | The keyword arguments to pass to the function. (default: `{}`) |

## Returns

`Output`

The output of the function.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/config.py#L497)
