---
title: "chain"
description: "Decorate a function to make it a Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/chain"
category: "reference"
tags: [reference, langchain-core, runnables, base, chain]
---

# chain

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/chain)

Decorate a function to make it a `Runnable`.

Sets the name of the `Runnable` to the name of the function.
Any runnables called by the function will be traced as dependencies.

## Signature

```python
chain(
    func: Callable[[Input], Output] | Callable[[Input], Iterator[Output]] | Callable[[Input], Coroutine[Any, Any, Output]] | Callable[[Input], AsyncIterator[Output]],
) -> Runnable[Input, Output]
```

## Description

**Example:**

```python
from langchain_core.runnables import chain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

@chain
def my_func(fields):
    prompt = PromptTemplate("Hello, {name}!")
    model = OpenAI()
    formatted = prompt.invoke(**fields)

    for chunk in model.stream(formatted):
        yield chunk
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Callable[[Input], Output] \| Callable[[Input], Iterator[Output]] \| Callable[[Input], Coroutine[Any, Any, Output]] \| Callable[[Input], AsyncIterator[Output]]` | Yes | A `Callable`. |

## Returns

`Runnable[Input, Output]`

A `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L6691)
