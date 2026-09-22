---
title: "RunnableLambda"
description: "RunnableLambda converts a python callable into a Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablelambda]
---

# RunnableLambda

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda)

`RunnableLambda` converts a python callable into a `Runnable`.

Wrapping a callable in a `RunnableLambda` makes the callable usable
within either a sync or async context.

`RunnableLambda` can be composed as any other `Runnable` and provides
seamless integration with LangChain tracing.

`RunnableLambda` is best suited for code that does not need to support
streaming. If you need to support streaming (i.e., be able to operate
on chunks of inputs and yield chunks of outputs), use `RunnableGenerator`
instead.

Note that if a `RunnableLambda` returns an instance of `Runnable`, that
instance is invoked (or streamed) during execution.

## Signature

```python
RunnableLambda(
    self,
    func: Callable[[Input], Iterator[Output]] | Callable[[Input], Runnable[Input, Output]] | Callable[[Input], Output] | Callable[[Input, RunnableConfig], Output] | Callable[[Input, CallbackManagerForChainRun], Output] | Callable[[Input, CallbackManagerForChainRun, RunnableConfig], Output] | Callable[[Input], Awaitable[Output]] | Callable[[Input], AsyncIterator[Output]] | Callable[[Input, RunnableConfig], Awaitable[Output]] | Callable[[Input, AsyncCallbackManagerForChainRun], Awaitable[Output]] | Callable[[Input, AsyncCallbackManagerForChainRun, RunnableConfig], Awaitable[Output]],
    afunc: Callable[[Input], Awaitable[Output]] | Callable[[Input], AsyncIterator[Output]] | Callable[[Input, RunnableConfig], Awaitable[Output]] | Callable[[Input, AsyncCallbackManagerForChainRun], Awaitable[Output]] | Callable[[Input, AsyncCallbackManagerForChainRun, RunnableConfig], Awaitable[Output]] | None = None,
    name: str | None = None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Callable[[Input], Iterator[Output]] \| Callable[[Input], Runnable[Input, Output]] \| Callable[[Input], Output] \| Callable[[Input, RunnableConfig], Output] \| Callable[[Input, CallbackManagerForChainRun], Output] \| Callable[[Input, CallbackManagerForChainRun, RunnableConfig], Output] \| Callable[[Input], Awaitable[Output]] \| Callable[[Input], AsyncIterator[Output]] \| Callable[[Input, RunnableConfig], Awaitable[Output]] \| Callable[[Input, AsyncCallbackManagerForChainRun], Awaitable[Output]] \| Callable[[Input, AsyncCallbackManagerForChainRun, RunnableConfig], Awaitable[Output]]` | Yes | Either sync or async callable |
| `afunc` | `Callable[[Input], Awaitable[Output]] \| Callable[[Input], AsyncIterator[Output]] \| Callable[[Input, RunnableConfig], Awaitable[Output]] \| Callable[[Input, AsyncCallbackManagerForChainRun], Awaitable[Output]] \| Callable[[Input, AsyncCallbackManagerForChainRun, RunnableConfig], Awaitable[Output]] \| None` | No | An async callable that takes an input and returns an output. (default: `None`) |
| `name` | `str \| None` | No | The name of the `Runnable`. (default: `None`) |

## Extends

- `Runnable[Input, Output]`

## Constructors

```python
__init__(
    self,
    func: Callable[[Input], Iterator[Output]] | Callable[[Input], Runnable[Input, Output]] | Callable[[Input], Output] | Callable[[Input, RunnableConfig], Output] | Callable[[Input, CallbackManagerForChainRun], Output] | Callable[[Input, CallbackManagerForChainRun, RunnableConfig], Output] | Callable[[Input], Awaitable[Output]] | Callable[[Input], AsyncIterator[Output]] | Callable[[Input, RunnableConfig], Awaitable[Output]] | Callable[[Input, AsyncCallbackManagerForChainRun], Awaitable[Output]] | Callable[[Input, AsyncCallbackManagerForChainRun, RunnableConfig], Awaitable[Output]],
    afunc: Callable[[Input], Awaitable[Output]] | Callable[[Input], AsyncIterator[Output]] | Callable[[Input, RunnableConfig], Awaitable[Output]] | Callable[[Input, AsyncCallbackManagerForChainRun], Awaitable[Output]] | Callable[[Input, AsyncCallbackManagerForChainRun, RunnableConfig], Awaitable[Output]] | None = None,
    name: str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `func` | `Callable[[Input], Iterator[Output]] \| Callable[[Input], Runnable[Input, Output]] \| Callable[[Input], Output] \| Callable[[Input, RunnableConfig], Output] \| Callable[[Input, CallbackManagerForChainRun], Output] \| Callable[[Input, CallbackManagerForChainRun, RunnableConfig], Output] \| Callable[[Input], Awaitable[Output]] \| Callable[[Input], AsyncIterator[Output]] \| Callable[[Input, RunnableConfig], Awaitable[Output]] \| Callable[[Input, AsyncCallbackManagerForChainRun], Awaitable[Output]] \| Callable[[Input, AsyncCallbackManagerForChainRun, RunnableConfig], Awaitable[Output]]` |
| `afunc` | `Callable[[Input], Awaitable[Output]] \| Callable[[Input], AsyncIterator[Output]] \| Callable[[Input, RunnableConfig], Awaitable[Output]] \| Callable[[Input, AsyncCallbackManagerForChainRun], Awaitable[Output]] \| Callable[[Input, AsyncCallbackManagerForChainRun, RunnableConfig], Awaitable[Output]] \| None` |
| `name` | `str \| None` |

## Properties

- `afunc`
- `func`
- `name`
- `InputType`
- `OutputType`
- `deps`
- `config_specs`

## Methods

- [`get_input_schema()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda/get_input_schema)
- [`get_output_schema()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda/get_output_schema)
- [`get_graph()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda/get_graph)
- [`invoke()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda/ainvoke)
- [`transform()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda/transform)
- [`stream()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda/stream)
- [`atransform()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda/atransform)
- [`astream()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableLambda/astream)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L4703)
