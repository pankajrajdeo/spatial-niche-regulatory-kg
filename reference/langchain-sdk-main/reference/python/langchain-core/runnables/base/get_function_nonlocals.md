---
title: "get_function_nonlocals"
description: "Get the nonlocal variables accessed by a function."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/get_function_nonlocals"
category: "reference"
tags: [reference, langchain-core, runnables, base, get_function_nonlocals]
---

# get_function_nonlocals

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/get_function_nonlocals)

Get the nonlocal variables accessed by a function.

## Signature

```python
get_function_nonlocals(
    func: Callable[..., Any],
) -> list[Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Callable[..., Any]` | Yes | The function to check. |

## Returns

`list[Any]`

The nonlocal variables accessed by the function.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/utils.py#L410)
