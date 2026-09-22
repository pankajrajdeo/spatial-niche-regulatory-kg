---
title: "get_function_first_arg_dict_keys"
description: "Get the keys of the first argument of a function if it is a dict."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/get_function_first_arg_dict_keys"
category: "reference"
tags: [reference, langchain-core, runnables, utils, get_function_first_arg_dict_keys]
---

# get_function_first_arg_dict_keys

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/get_function_first_arg_dict_keys)

Get the keys of the first argument of a function if it is a dict.

## Signature

```python
get_function_first_arg_dict_keys(
    func: Callable[..., Any],
) -> list[str] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Callable[..., Any]` | Yes | The function to check. |

## Returns

`list[str] | None`

The keys of the first argument if it is a dict, None otherwise.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/utils.py#L368)
