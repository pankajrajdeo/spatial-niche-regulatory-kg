---
title: "bind"
description: "Bind arguments to a Runnable, returning a new Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/bind"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, bind]
---

# bind

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/bind)

Bind arguments to a `Runnable`, returning a new `Runnable`.

Useful when a `Runnable` in a chain requires an argument that is not
in the output of the previous `Runnable` or included in the user input.

## Signature

```python
bind(
    self,
    **kwargs: Any = {},
) -> Runnable[Input, Output]
```

## Description

**Example:**

```python
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="llama3.1")

# Without bind
chain = model | StrOutputParser()

chain.invoke("Repeat quoted words exactly: 'One two three four five.'")
# Output is 'One two three four five.'

# With bind
chain = model.bind(stop=["three"]) | StrOutputParser()

chain.invoke("Repeat quoted words exactly: 'One two three four five.'")
# Output is 'One two'
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `Any` | No | The arguments to bind to the `Runnable`. (default: `{}`) |

## Returns

`Runnable[Input, Output]`

A new `Runnable` with the arguments bound.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L1851)
