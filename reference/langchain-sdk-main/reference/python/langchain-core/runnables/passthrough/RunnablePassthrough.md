---
title: "RunnablePassthrough"
description: "Runnable to passthrough inputs unchanged or with additional keys."
source: "https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePassthrough"
category: "reference"
tags: [reference, langchain-core, runnables, passthrough, runnablepassthrough]
---

# RunnablePassthrough

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePassthrough)

Runnable to passthrough inputs unchanged or with additional keys.

This `Runnable` behaves almost like the identity function, except that it
can be configured to add additional keys to the output, if the input is a
dict.

The examples below demonstrate this `Runnable` works using a few simple
chains. The chains rely on simple lambdas to make the examples easy to execute
and experiment with.

## Signature

```python
RunnablePassthrough(
    self,
    func: Callable[[Other], None] | Callable[[Other, RunnableConfig], None] | Callable[[Other], Awaitable[None]] | Callable[[Other, RunnableConfig], Awaitable[None]] | None = None,
    afunc: Callable[[Other], Awaitable[None]] | Callable[[Other, RunnableConfig], Awaitable[None]] | None = None,
    *,
    input_type: type[Other] | None = None,
    **kwargs: Any = {},
)
```

## Description

In some cases, it may be useful to pass the input through while adding some
keys to the output. In this case, you can use the `assign` method:

```python
    from langchain_core.runnables import RunnablePassthrough

    def fake_llm(prompt: str) -> str:  # Fake LLM for the example
        return "completion"

    runnable = {
        "llm1": fake_llm,
        "llm2": fake_llm,
    } | RunnablePassthrough.assign(
        total_chars=lambda inputs: len(inputs["llm1"] + inputs["llm2"])
    )

    runnable.invoke("hello")
    # {'llm1': 'completion', 'llm2': 'completion', 'total_chars': 20}
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Callable[[Other], None] \| Callable[[Other, RunnableConfig], None] \| Callable[[Other], Awaitable[None]] \| Callable[[Other, RunnableConfig], Awaitable[None]] \| None` | No | Function to be called with the input. (default: `None`) |
| `afunc` | `Callable[[Other], Awaitable[None]] \| Callable[[Other, RunnableConfig], Awaitable[None]] \| None` | No | Async function to be called with the input. (default: `None`) |
| `input_type` | `type[Other] \| None` | No | Type of the input. (default: `None`) |

## Extends

- `RunnableSerializable[Other, Other]`

## Constructors

```python
__init__(
    self,
    func: Callable[[Other], None] | Callable[[Other, RunnableConfig], None] | Callable[[Other], Awaitable[None]] | Callable[[Other, RunnableConfig], Awaitable[None]] | None = None,
    afunc: Callable[[Other], Awaitable[None]] | Callable[[Other, RunnableConfig], Awaitable[None]] | None = None,
    *,
    input_type: type[Other] | None = None,
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `func` | `Callable[[Other], None] \| Callable[[Other, RunnableConfig], None] \| Callable[[Other], Awaitable[None]] \| Callable[[Other, RunnableConfig], Awaitable[None]] \| None` |
| `afunc` | `Callable[[Other], Awaitable[None]] \| Callable[[Other, RunnableConfig], Awaitable[None]] \| None` |
| `input_type` | `type[Other] \| None` |

## Properties

- `input_type`
- `func`
- `afunc`
- `InputType`
- `OutputType`

## Methods

- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePassthrough/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePassthrough/get_lc_namespace)
- [`assign()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePassthrough/assign)
- [`invoke()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePassthrough/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePassthrough/ainvoke)
- [`transform()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePassthrough/transform)
- [`atransform()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePassthrough/atransform)
- [`stream()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePassthrough/stream)
- [`astream()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePassthrough/astream)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/passthrough.py#L74)
