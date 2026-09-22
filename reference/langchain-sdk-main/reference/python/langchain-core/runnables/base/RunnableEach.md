---
title: "RunnableEach"
description: "RunnableEach class."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEach"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnableeach]
---

# RunnableEach

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEach)

RunnableEach class.

`Runnable` that calls another `Runnable` for each element of the input sequence.

It allows you to call multiple inputs with the bounded `Runnable`.

`RunnableEach` makes it easy to run multiple inputs for the `Runnable`.
In the below example, we associate and run three inputs
with a `Runnable`:

```python
    from langchain_core.runnables.base import RunnableEach
    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    prompt = ChatPromptTemplate.from_template("Tell me a short joke about
    {topic}")
    model = ChatOpenAI()
    output_parser = StrOutputParser()
    runnable = prompt | model | output_parser
    runnable_each = RunnableEach(bound=runnable)
    output = runnable_each.invoke([{'topic':'Computer Science'},
                                {'topic':'Art'},
                                {'topic':'Biology'}])
    print(output)  # noqa: T201

```

## Signature

```python
RunnableEach(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `RunnableEachBase[Input, Output]`

## Methods

- [`get_name()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEach/get_name)
- [`bind()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEach/bind)
- [`with_config()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEach/with_config)
- [`with_listeners()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEach/with_listeners)
- [`with_alisteners()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEach/with_alisteners)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L5734)
