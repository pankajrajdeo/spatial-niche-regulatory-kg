---
title: "RunnableBinding"
description: "Wrap a Runnable with additional functionality."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBinding"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablebinding]
---

# RunnableBinding

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBinding)

Wrap a `Runnable` with additional functionality.

A `RunnableBinding` can be thought of as a "runnable decorator" that
preserves the essential features of `Runnable`; i.e., batching, streaming,
and async support, while adding additional functionality.

Any class that inherits from `Runnable` can be bound to a `RunnableBinding`.
Runnables expose a standard set of methods for creating `RunnableBindings`
or sub-classes of `RunnableBindings` (e.g., `RunnableRetry`,
`RunnableWithFallbacks`) that add additional functionality.

These methods include:

- `bind`: Bind kwargs to pass to the underlying `Runnable` when running it.
- `with_config`: Bind config to pass to the underlying `Runnable` when running
    it.
- `with_listeners`:  Bind lifecycle listeners to the underlying `Runnable`.
- `with_types`: Override the input and output types of the underlying
    `Runnable`.
- `with_retry`: Bind a retry policy to the underlying `Runnable`.
- `with_fallbacks`: Bind a fallback policy to the underlying `Runnable`.

Example:
`bind`: Bind kwargs to pass to the underlying `Runnable` when running it.

```python
    # Create a Runnable binding that invokes the chat model with the
    # additional kwarg `stop=['-']` when running it.
    from langchain_openai import ChatOpenAI

    model = ChatOpenAI()
    model.invoke('Say "Parrot-MAGIC"', stop=["-"])  # Should return `Parrot`
    # Using it the easy way via `bind` method which returns a new
    # RunnableBinding
    runnable_binding = model.bind(stop=["-"])
    runnable_binding.invoke('Say "Parrot-MAGIC"')  # Should return `Parrot`
```
    Can also be done by instantiating a `RunnableBinding` directly (not
    recommended):

```python
    from langchain_core.runnables import RunnableBinding

    runnable_binding = RunnableBinding(
        bound=model,
        kwargs={"stop": ["-"]},  # <-- Note the additional kwargs
    )
    runnable_binding.invoke('Say "Parrot-MAGIC"')  # Should return `Parrot`
```

## Signature

```python
RunnableBinding(
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

## Extends

- `RunnableBindingBase[Input, Output]`

## Methods

- [`bind()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBinding/bind)
- [`with_config()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBinding/with_config)
- [`with_listeners()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBinding/with_listeners)
- [`with_types()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBinding/with_types)
- [`with_retry()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBinding/with_retry)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L6378)
