---
title: "RunnableParallel"
description: "Runnable that runs a mapping of Runnables in parallel."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnableparallel]
---

# RunnableParallel

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel)

Runnable that runs a mapping of `Runnable`s in parallel.

Returns a mapping of their outputs.

`RunnableParallel` is one of the two main composition primitives,
alongside `RunnableSequence`. It invokes `Runnable`s concurrently, providing the
same input to each.

A `RunnableParallel` can be instantiated directly or by using a dict literal
within a sequence.

Here is a simple example that uses functions to illustrate the use of
`RunnableParallel`:

```python
    from langchain_core.runnables import RunnableLambda

    def add_one(x: int) -> int:
        return x + 1

    def mul_two(x: int) -> int:
        return x * 2

    def mul_three(x: int) -> int:
        return x * 3

    runnable_1 = RunnableLambda(add_one)
    runnable_2 = RunnableLambda(mul_two)
    runnable_3 = RunnableLambda(mul_three)

    sequence = runnable_1 | {  # this dict is coerced to a RunnableParallel
        "mul_two": runnable_2,
        "mul_three": runnable_3,
    }
    # Or equivalently:
    # sequence = runnable_1 | RunnableParallel(
    #     {"mul_two": runnable_2, "mul_three": runnable_3}
    # )
    # Also equivalently:
    # sequence = runnable_1 | RunnableParallel(
    #     mul_two=runnable_2,
    #     mul_three=runnable_3,
    # )

    sequence.invoke(1)
    await sequence.ainvoke(1)

    sequence.batch([1, 2, 3])
    await sequence.abatch([1, 2, 3])
```

`RunnableParallel` makes it easy to run `Runnable`s in parallel. In the below
example, we simultaneously stream output from two different `Runnable` objects:

```python
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.runnables import RunnableParallel
    from langchain_openai import ChatOpenAI

    model = ChatOpenAI()
    joke_chain = (
        ChatPromptTemplate.from_template("tell me a joke about {topic}") | model
    )
    poem_chain = (
        ChatPromptTemplate.from_template("write a 2-line poem about {topic}")
        | model
    )

    runnable = RunnableParallel(joke=joke_chain, poem=poem_chain)

    # Display stream
    output = {key: "" for key, _ in runnable.output_schema()}
    for chunk in runnable.stream({"topic": "bear"}):
        for key in chunk:
            output[key] = output[key] + chunk[key].content
        print(output)  # noqa: T201
```

## Signature

```python
RunnableParallel(
    self,
    steps__: Mapping[str, Runnable[Input, Any] | Callable[[Input], Any] | Mapping[str, Runnable[Input, Any] | Callable[[Input], Any]]] | None = None,
    **kwargs: Runnable[Input, Any] | Callable[[Input], Any] | Mapping[str, Runnable[Input, Any] | Callable[[Input], Any]] = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `steps__` | `Mapping[str, Runnable[Input, Any] \| Callable[[Input], Any] \| Mapping[str, Runnable[Input, Any] \| Callable[[Input], Any]]] \| None` | No | The steps to include. (default: `None`) |
| `**kwargs` | `Runnable[Input, Any] \| Callable[[Input], Any] \| Mapping[str, Runnable[Input, Any] \| Callable[[Input], Any]]` | No | Additional steps to include. (default: `{}`) |

## Extends

- `RunnableSerializable[Input, dict[str, Any]]`

## Constructors

```python
__init__(
    self,
    steps__: Mapping[str, Runnable[Input, Any] | Callable[[Input], Any] | Mapping[str, Runnable[Input, Any] | Callable[[Input], Any]]] | None = None,
    **kwargs: Runnable[Input, Any] | Callable[[Input], Any] | Mapping[str, Runnable[Input, Any] | Callable[[Input], Any]] = {},
) -> None
```

| Name | Type |
|------|------|
| `steps__` | `Mapping[str, Runnable[Input, Any] \| Callable[[Input], Any] \| Mapping[str, Runnable[Input, Any] \| Callable[[Input], Any]]] \| None` |

## Properties

- `steps__`
- `model_config`
- `InputType`
- `config_specs`

## Methods

- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/get_lc_namespace)
- [`get_name()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/get_name)
- [`get_input_schema()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/get_input_schema)
- [`get_output_schema()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/get_output_schema)
- [`get_graph()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/get_graph)
- [`invoke()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/ainvoke)
- [`transform()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/transform)
- [`stream()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/stream)
- [`atransform()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/atransform)
- [`astream()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/astream)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L3864)
