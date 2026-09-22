---
title: "RunnableBindingBase"
description: "Runnable that delegates calls to another Runnable with a set of kwargs."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablebindingbase]
---

# RunnableBindingBase

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase)

`Runnable` that delegates calls to another `Runnable` with a set of `**kwargs`.

Use only if creating a new `RunnableBinding` subclass with different `__init__`
args.

See documentation for `RunnableBinding` for more details.

## Signature

```python
RunnableBindingBase(
    self,
    *,
    bound: Runnable[Input, Output],
    kwargs: Mapping[str, Any] | None = None,
    config: RunnableConfig | None = None,
    config_factories: list[Callable[[RunnableConfig], RunnableConfig]] | None = None,
    custom_input_type: type[Input] | BaseModel | None = None,
    custom_output_type: type[Output] | BaseModel | None = None,
    **other_kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `bound` | `Runnable[Input, Output]` | Yes | The underlying `Runnable` that this `Runnable` delegates calls to. |
| `kwargs` | `Mapping[str, Any] \| None` | No | optional kwargs to pass to the underlying `Runnable`, when running the underlying `Runnable` (e.g., via `invoke`, `batch`, `transform`, or `stream` or async variants) (default: `None`) |
| `config` | `RunnableConfig \| None` | No | optional config to bind to the underlying `Runnable`. (default: `None`) |
| `config_factories` | `list[Callable[[RunnableConfig], RunnableConfig]] \| None` | No | optional list of config factories to apply to the config before binding to the underlying `Runnable`. (default: `None`) |
| `custom_input_type` | `type[Input] \| BaseModel \| None` | No | Specify to override the input type of the underlying `Runnable` with a custom type. (default: `None`) |
| `custom_output_type` | `type[Output] \| BaseModel \| None` | No | Specify to override the output type of the underlying `Runnable` with a custom type. (default: `None`) |
| `**other_kwargs` | `Any` | No | Unpacked into the base class. (default: `{}`) |

## Extends

- `RunnableSerializable[Input, Output]`

## Constructors

```python
__init__(
    self,
    *,
    bound: Runnable[Input, Output],
    kwargs: Mapping[str, Any] | None = None,
    config: RunnableConfig | None = None,
    config_factories: list[Callable[[RunnableConfig], RunnableConfig]] | None = None,
    custom_input_type: type[Input] | BaseModel | None = None,
    custom_output_type: type[Output] | BaseModel | None = None,
    **other_kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `bound` | `Runnable[Input, Output]` |
| `kwargs` | `Mapping[str, Any] \| None` |
| `config` | `RunnableConfig \| None` |
| `config_factories` | `list[Callable[[RunnableConfig], RunnableConfig]] \| None` |
| `custom_input_type` | `type[Input] \| BaseModel \| None` |
| `custom_output_type` | `type[Output] \| BaseModel \| None` |

## Properties

- `bound`
- `kwargs`
- `config`
- `config_factories`
- `custom_input_type`
- `custom_output_type`
- `model_config`
- `InputType`
- `OutputType`
- `config_specs`

## Methods

- [`get_name()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/get_name)
- [`get_input_schema()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/get_input_schema)
- [`get_output_schema()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/get_output_schema)
- [`get_graph()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/get_graph)
- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/get_lc_namespace)
- [`invoke()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/ainvoke)
- [`batch()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/batch)
- [`abatch()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/abatch)
- [`batch_as_completed()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/batch_as_completed)
- [`abatch_as_completed()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/abatch_as_completed)
- [`stream()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/stream)
- [`astream()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/astream)
- [`stream_events()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/stream_events)
- [`astream_events()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/astream_events)
- [`transform()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/transform)
- [`atransform()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/atransform)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L5851)
