---
title: "DynamicRunnable"
description: "Serializable Runnable that can be dynamically configured."
source: "https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable"
category: "reference"
tags: [reference, langchain-core, runnables, configurable, dynamicrunnable]
---

# DynamicRunnable

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable)

Serializable `Runnable` that can be dynamically configured.

A `DynamicRunnable` should be initiated using the `configurable_fields` or
`configurable_alternatives` method of a `Runnable`.

## Signature

```python
DynamicRunnable(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `RunnableSerializable[Input, Output]`

## Properties

- `default`
- `config`
- `model_config`
- `InputType`
- `OutputType`

## Methods

- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/get_lc_namespace)
- [`get_input_schema()`](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/get_input_schema)
- [`get_output_schema()`](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/get_output_schema)
- [`get_graph()`](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/get_graph)
- [`with_config()`](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/with_config)
- [`prepare()`](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/prepare)
- [`invoke()`](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/ainvoke)
- [`batch()`](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/batch)
- [`abatch()`](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/abatch)
- [`stream()`](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/stream)
- [`astream()`](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/astream)
- [`transform()`](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/transform)
- [`atransform()`](https://reference.langchain.com/python/langchain-core/runnables/configurable/DynamicRunnable/atransform)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/configurable.py#L50)
