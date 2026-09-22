---
title: "get_function_nonlocals"
description: "Get the nonlocal variables accessed by a function."
source: "https://reference.langchain.com/python/langgraph/pregel/_utils/get_function_nonlocals"
category: "reference"
tags: [reference, langgraph, pregel, utils, get_function_nonlocals]
---

# get_function_nonlocals

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_utils/get_function_nonlocals)

Get the nonlocal variables accessed by a function.

## Signature

```python
get_function_nonlocals(
    func: Callable,
) -> list[Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Callable` | Yes | The function to check. |

## Returns

`list[Any]`

List[Any]: The nonlocal variables accessed by the function.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_utils.py#L140)
