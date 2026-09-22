---
title: "RunnablePick"
description: "Runnable that picks keys from dict[str, Any] inputs."
source: "https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePick"
category: "reference"
tags: [reference, langchain-core, runnables, passthrough, runnablepick]
---

# RunnablePick

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePick)

`Runnable` that picks keys from `dict[str, Any]` inputs.

`RunnablePick` class represents a `Runnable` that selectively picks keys from a
dictionary input. It allows you to specify one or more keys to extract
from the input dictionary.

!!! note "Return Type Behavior"
    The return type depends on the `keys` parameter:

    - When `keys` is a `str`: Returns the single value associated with that key
    - When `keys` is a `list`: Returns a dictionary containing only the selected
        keys

## Signature

```python
RunnablePick(
    self,
    keys: str | list[str],
    **kwargs: Any = {},
)
```

## Description

**Example:**

```python
from langchain_core.runnables.passthrough import RunnablePick

input_data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "country": "USA",
}

# Single key - returns the value directly
runnable_single = RunnablePick(keys="name")
result_single = runnable_single.invoke(input_data)
print(result_single)  # Output: "John"

# Multiple keys - returns a dictionary
runnable_multiple = RunnablePick(keys=["name", "age"])
result_multiple = runnable_multiple.invoke(input_data)
print(result_multiple)  # Output: {'name': 'John', 'age': 30}
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `keys` | `str \| list[str]` | Yes | A single key or a list of keys to pick from the input dictionary. |

## Extends

- `RunnableSerializable[dict[str, Any], Any]`

## Constructors

```python
__init__(
    self,
    keys: str | list[str],
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `keys` | `str \| list[str]` |

## Properties

- `keys`

## Methods

- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePick/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePick/get_lc_namespace)
- [`get_name()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePick/get_name)
- [`invoke()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePick/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePick/ainvoke)
- [`transform()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePick/transform)
- [`atransform()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePick/atransform)
- [`stream()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePick/stream)
- [`astream()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePick/astream)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/passthrough.py#L679)
