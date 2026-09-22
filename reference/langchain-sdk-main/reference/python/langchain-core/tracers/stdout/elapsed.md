---
title: "elapsed"
description: "Get the elapsed time of a run."
source: "https://reference.langchain.com/python/langchain-core/tracers/stdout/elapsed"
category: "reference"
tags: [reference, langchain-core, tracers, stdout, elapsed]
---

# elapsed

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/stdout/elapsed)

Get the elapsed time of a run.

## Signature

```python
elapsed(
    run: Any,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run` | `Any` | Yes | any object with a `start_time` and `end_time` attribute. |

## Returns

`str`

A string with the elapsed time in seconds or milliseconds if time is less than a
second.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tracers/stdout.py#L30)
