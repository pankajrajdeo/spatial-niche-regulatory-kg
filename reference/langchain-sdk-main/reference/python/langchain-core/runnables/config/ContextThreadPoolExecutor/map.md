---
title: "map"
description: "Map a function to multiple iterables."
source: "https://reference.langchain.com/python/langchain-core/runnables/config/ContextThreadPoolExecutor/map"
category: "reference"
tags: [reference, langchain-core, runnables, config, contextthreadpoolexecutor, map]
---

# map

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/config/ContextThreadPoolExecutor/map)

Map a function to multiple iterables.

## Signature

```python
map(
    self,
    fn: Callable[..., T],
    *iterables: Iterable[Any] = (),
    **kwargs: Any = {},
) -> Iterator[T]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `fn` | `Callable[..., T]` | Yes | The function to map. |
| `*iterables` | `Iterable[Any]` | No | The iterables to map over. (default: `()`) |
| `timeout` | `unknown` | Yes | The timeout for the map. |
| `chunksize` | `unknown` | Yes | The chunksize for the map. |

## Returns

`Iterator[T]`

The iterator for the mapped function.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/config.py#L630)
