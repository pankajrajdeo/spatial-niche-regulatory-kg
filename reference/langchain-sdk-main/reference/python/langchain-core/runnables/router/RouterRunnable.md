---
title: "RouterRunnable"
description: "Runnable that routes to a set of Runnable based on Input['key']."
source: "https://reference.langchain.com/python/langchain-core/runnables/router/RouterRunnable"
category: "reference"
tags: [reference, langchain-core, runnables, router, routerrunnable]
---

# RouterRunnable

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/router/RouterRunnable)

`Runnable` that routes to a set of `Runnable` based on `Input['key']`.

Returns the output of the selected Runnable.

## Signature

```python
RouterRunnable(
    self,
    runnables: Mapping[str, Runnable[Any, Output] | Callable[[Any], Output]],
)
```

## Description

**Example:**

```python
from langchain_core.runnables.router import RouterRunnable
from langchain_core.runnables import RunnableLambda

add = RunnableLambda(func=lambda x: x + 1)
square = RunnableLambda(func=lambda x: x**2)

router = RouterRunnable(runnables={"add": add, "square": square})
router.invoke({"key": "square", "input": 3})
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `runnables` | `Mapping[str, Runnable[Any, Output] \| Callable[[Any], Output]]` | Yes | A mapping of keys to `Runnable` objects. |

## Extends

- `RunnableSerializable[RouterInput, Output]`

## Constructors

```python
__init__(
    self,
    runnables: Mapping[str, Runnable[Any, Output] | Callable[[Any], Output]],
) -> None
```

| Name | Type |
|------|------|
| `runnables` | `Mapping[str, Runnable[Any, Output] \| Callable[[Any], Output]]` |

## Properties

- `runnables`
- `config_specs`
- `model_config`

## Methods

- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/runnables/router/RouterRunnable/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/runnables/router/RouterRunnable/get_lc_namespace)
- [`invoke()`](https://reference.langchain.com/python/langchain-core/runnables/router/RouterRunnable/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/runnables/router/RouterRunnable/ainvoke)
- [`batch()`](https://reference.langchain.com/python/langchain-core/runnables/router/RouterRunnable/batch)
- [`abatch()`](https://reference.langchain.com/python/langchain-core/runnables/router/RouterRunnable/abatch)
- [`stream()`](https://reference.langchain.com/python/langchain-core/runnables/router/RouterRunnable/stream)
- [`astream()`](https://reference.langchain.com/python/langchain-core/runnables/router/RouterRunnable/astream)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/router.py#L46)
