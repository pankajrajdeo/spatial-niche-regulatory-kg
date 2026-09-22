---
title: "assign"
description: "Merge the Dict input with the output produced by the mapping argument."
source: "https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePassthrough/assign"
category: "reference"
tags: [reference, langchain-core, runnables, passthrough, runnablepassthrough, assign]
---

# assign

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/passthrough/RunnablePassthrough/assign)

Merge the Dict input with the output produced by the mapping argument.

## Signature

```python
assign(
    cls,
    **kwargs: Runnable[dict[str, Any], Any] | Callable[[dict[str, Any]], Any] | Mapping[str, Runnable[dict[str, Any], Any] | Callable[[dict[str, Any]], Any]] = {},
) -> RunnableAssign
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `Runnable[dict[str, Any], Any] \| Callable[[dict[str, Any]], Any] \| Mapping[str, Runnable[dict[str, Any], Any] \| Callable[[dict[str, Any]], Any]]` | No | `Runnable`, `Callable` or a `Mapping` from keys to `Runnable` objects or `Callable`s. (default: `{}`) |

## Returns

`RunnableAssign`

A `Runnable` that merges the `dict` input with the output produced by the

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/passthrough.py#L205)
