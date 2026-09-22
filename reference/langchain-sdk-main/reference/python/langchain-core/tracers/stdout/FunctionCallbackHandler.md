---
title: "FunctionCallbackHandler"
description: "Tracer that calls a function with a single str parameter."
source: "https://reference.langchain.com/python/langchain-core/tracers/stdout/FunctionCallbackHandler"
category: "reference"
tags: [reference, langchain-core, tracers, stdout, functioncallbackhandler]
---

# FunctionCallbackHandler

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/stdout/FunctionCallbackHandler)

Tracer that calls a function with a single str parameter.

## Signature

```python
FunctionCallbackHandler(
    self,
    function: Callable[[str], None],
    **kwargs: Any = {},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `function` | `Callable[[str], None]` | Yes | The callback function to call. |

## Extends

- `BaseTracer`

## Constructors

```python
__init__(
    self,
    function: Callable[[str], None],
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `function` | `Callable[[str], None]` |

## Properties

- `name`
- `function_callback`

## Methods

- [`get_parents()`](https://reference.langchain.com/python/langchain-core/tracers/stdout/FunctionCallbackHandler/get_parents)
- [`get_breadcrumbs()`](https://reference.langchain.com/python/langchain-core/tracers/stdout/FunctionCallbackHandler/get_breadcrumbs)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/stdout.py#L48)
