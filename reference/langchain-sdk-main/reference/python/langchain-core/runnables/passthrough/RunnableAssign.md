---
title: "RunnableAssign"
description: "Runnable that assigns key-value pairs to dict[str, Any] inputs."
source: "https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnableAssign"
category: "reference"
tags: [reference, langchain-core, runnables, passthrough, runnableassign]
---

# RunnableAssign

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnableAssign)

Runnable that assigns key-value pairs to `dict[str, Any]` inputs.

The `RunnableAssign` class takes input dictionaries and, through a
`RunnableParallel` instance, applies transformations, then combines
these with the original data, introducing new key-value pairs based
on the mapper's logic.

## Signature

```python
RunnableAssign(
    self,
    mapper: RunnableParallel[dict[str, Any]],
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `mapper` | `RunnableParallel[dict[str, Any]]` | Yes | A `RunnableParallel` instance that will be used to transform the input dictionary. |

## Extends

- `RunnableSerializable[dict[str, Any], dict[str, Any]]`

## Constructors

```python
__init__(
    self,
    mapper: RunnableParallel[dict[str, Any]],
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `mapper` | `RunnableParallel[dict[str, Any]]` |

## Properties

- `mapper`
- `config_specs`

## Methods

- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnableAssign/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnableAssign/get_lc_namespace)
- [`get_name()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnableAssign/get_name)
- [`get_input_schema()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnableAssign/get_input_schema)
- [`get_output_schema()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnableAssign/get_output_schema)
- [`get_graph()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnableAssign/get_graph)
- [`invoke()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnableAssign/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnableAssign/ainvoke)
- [`transform()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnableAssign/transform)
- [`atransform()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnableAssign/atransform)
- [`stream()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnableAssign/stream)
- [`astream()`](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnableAssign/astream)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/passthrough.py#L352)
