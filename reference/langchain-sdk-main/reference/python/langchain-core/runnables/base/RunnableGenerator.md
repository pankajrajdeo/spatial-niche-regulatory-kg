---
title: "RunnableGenerator"
description: "Runnable that runs a generator function."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableGenerator"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablegenerator]
---

# RunnableGenerator

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableGenerator)

`Runnable` that runs a generator function.

`RunnableGenerator`s can be instantiated directly or by using a generator within
a sequence.

`RunnableGenerator`s can be used to implement custom behavior, such as custom
output parsers, while preserving streaming capabilities. Given a generator function
with a signature `Iterator[A] -> Iterator[B]`, wrapping it in a
`RunnableGenerator` allows it to emit output chunks as soon as they are streamed
in from the previous step.

!!! note
    If a generator function has a `signature A -> Iterator[B]`, such that it
    requires its input from the previous step to be completed before emitting chunks
    (e.g., most LLMs need the entire prompt available to start generating), it can
    instead be wrapped in a `RunnableLambda`.

Here is an example to show the basic mechanics of a `RunnableGenerator`:

```python
    from typing import Any, AsyncIterator, Iterator

    from langchain_core.runnables import RunnableGenerator

    def gen(input: Iterator[Any]) -> Iterator[str]:
        for token in ["Have", " a", " nice", " day"]:
            yield token

    runnable = RunnableGenerator(gen)
    runnable.invoke(None)  # "Have a nice day"
    list(runnable.stream(None))  # ["Have", " a", " nice", " day"]
    runnable.batch([None, None])  # ["Have a nice day", "Have a nice day"]

    # Async version:
    async def agen(input: AsyncIterator[Any]) -> AsyncIterator[str]:
        for token in ["Have", " a", " nice", " day"]:
            yield token

    runnable = RunnableGenerator(agen)
    await runnable.ainvoke(None)  # "Have a nice day"
    [p async for p in runnable.astream(None)]  # ["Have", " a", " nice", " day"]
```

`RunnableGenerator` makes it easy to implement custom behavior within a streaming
context. Below we show an example:

```python
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.runnables import RunnableGenerator, RunnableLambda
    from langchain_openai import ChatOpenAI
    from langchain_core.output_parsers import StrOutputParser

    model = ChatOpenAI()
    chant_chain = (
        ChatPromptTemplate.from_template("Give me a 3 word chant about {topic}")
        | model
        | StrOutputParser()
    )

    def character_generator(input: Iterator[str]) -> Iterator[str]:
        for token in input:
            if "," in token or "." in token:
                yield "👏" + token
            else:
                yield token

    runnable = chant_chain | character_generator
    assert type(runnable.last) is RunnableGenerator
    "".join(runnable.stream({"topic": "waste"}))  # Reduce👏, Reuse👏, Recycle👏.

    # Note that RunnableLambda can be used to delay streaming of one step in a
    # sequence until the previous step is finished:
    def reverse_generator(input: str) -> Iterator[str]:
        # Yield characters of input in reverse order.
        for character in input[::-1]:
            yield character

    runnable = chant_chain | RunnableLambda(reverse_generator)
    "".join(runnable.stream({"topic": "waste"}))  # ".elcycer ,esuer ,ecudeR"
```

## Signature

```python
RunnableGenerator(
    self,
    transform: Callable[[Iterator[Input]], Iterator[Output]] | Callable[[AsyncIterator[Input]], AsyncIterator[Output]],
    atransform: Callable[[AsyncIterator[Input]], AsyncIterator[Output]] | None = None,
    *,
    name: str | None = None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `transform` | `Callable[[Iterator[Input]], Iterator[Output]] \| Callable[[AsyncIterator[Input]], AsyncIterator[Output]]` | Yes | The transform function. |
| `atransform` | `Callable[[AsyncIterator[Input]], AsyncIterator[Output]] \| None` | No | The async transform function. (default: `None`) |
| `name` | `str \| None` | No | The name of the `Runnable`. (default: `None`) |

## Extends

- `Runnable[Input, Output]`

## Constructors

```python
__init__(
    self,
    transform: Callable[[Iterator[Input]], Iterator[Output]] | Callable[[AsyncIterator[Input]], AsyncIterator[Output]],
    atransform: Callable[[AsyncIterator[Input]], AsyncIterator[Output]] | None = None,
    *,
    name: str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `transform` | `Callable[[Iterator[Input]], Iterator[Output]] \| Callable[[AsyncIterator[Input]], AsyncIterator[Output]]` |
| `atransform` | `Callable[[AsyncIterator[Input]], AsyncIterator[Output]] \| None` |
| `name` | `str \| None` |

## Properties

- `name`
- `InputType`
- `OutputType`

## Methods

- [`get_input_schema()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableGenerator/get_input_schema)
- [`get_output_schema()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableGenerator/get_output_schema)
- [`transform()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableGenerator/transform)
- [`stream()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableGenerator/stream)
- [`invoke()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableGenerator/invoke)
- [`atransform()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableGenerator/atransform)
- [`astream()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableGenerator/astream)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableGenerator/ainvoke)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L4399)
