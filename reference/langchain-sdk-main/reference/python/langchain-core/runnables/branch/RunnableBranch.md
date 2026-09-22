---
title: "RunnableBranch"
description: "Runnable that selects which branch to run based on a condition."
source: "https://reference.langchain.com/python/langchain-core/runnables/branch/RunnableBranch"
category: "reference"
tags: [reference, langchain-core, runnables, branch, runnablebranch]
---

# RunnableBranch

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/branch/RunnableBranch)

`Runnable` that selects which branch to run based on a condition.

The `Runnable` is initialized with a list of `(condition, Runnable)` pairs and
a default branch.

When operating on an input, the first condition that evaluates to True is
selected, and the corresponding `Runnable` is run on the input.

If no condition evaluates to `True`, the default branch is run on the input.

## Signature

```python
RunnableBranch(
    self,
    *branches: tuple[Runnable[Input, bool] | Callable[[Input], bool] | Callable[[Input], Awaitable[bool]], RunnableLike[Input, Output]] | RunnableLike[Input, Output] = (),
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `*branches` | `tuple[Runnable[Input, bool] \| Callable[[Input], bool] \| Callable[[Input], Awaitable[bool]], RunnableLike[Input, Output]] \| RunnableLike[Input, Output]` | No | A list of `(condition, Runnable)` pairs. Defaults a `Runnable` to run if no condition is met. (default: `()`) |

## Extends

- `RunnableSerializable[Input, Output]`

## Constructors

```python
__init__(
    self,
    *branches: tuple[Runnable[Input, bool] | Callable[[Input], bool] | Callable[[Input], Awaitable[bool]], RunnableLike[Input, Output]] | RunnableLike[Input, Output] = (),
) -> None
```

## Properties

- `branches`
- `default`
- `model_config`
- `config_specs`

## Methods

- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/runnables/branch/RunnableBranch/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/runnables/branch/RunnableBranch/get_lc_namespace)
- [`get_input_schema()`](https://reference.langchain.com/python/langchain-core/runnables/branch/RunnableBranch/get_input_schema)
- [`invoke()`](https://reference.langchain.com/python/langchain-core/runnables/branch/RunnableBranch/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/runnables/branch/RunnableBranch/ainvoke)
- [`stream()`](https://reference.langchain.com/python/langchain-core/runnables/branch/RunnableBranch/stream)
- [`astream()`](https://reference.langchain.com/python/langchain-core/runnables/branch/RunnableBranch/astream)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/branch.py#L43)
