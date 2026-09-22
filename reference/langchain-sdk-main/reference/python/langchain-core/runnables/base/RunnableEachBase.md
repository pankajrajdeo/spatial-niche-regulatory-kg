---
title: "RunnableEachBase"
description: "RunnableEachBase class."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEachBase"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnableeachbase]
---

# RunnableEachBase

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEachBase)

RunnableEachBase class.

`Runnable` that calls another `Runnable` for each element of the input sequence.

Use only if creating a new `RunnableEach` subclass with different `__init__`
args.

See documentation for `RunnableEach` for more details.

## Signature

```python
RunnableEachBase(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `RunnableSerializable[Sequence[Input], list[Output]]`

## Properties

- `bound`
- `model_config`
- `InputType`
- `OutputType`
- `config_specs`

## Methods

- [`get_input_schema()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEachBase/get_input_schema)
- [`get_output_schema()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEachBase/get_output_schema)
- [`get_graph()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEachBase/get_graph)
- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEachBase/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEachBase/get_lc_namespace)
- [`invoke()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEachBase/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEachBase/ainvoke)
- [`astream_events()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableEachBase/astream_events)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L5577)
