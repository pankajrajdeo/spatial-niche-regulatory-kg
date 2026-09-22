---
title: "ExponentialJitterParams"
description: "Parameters for tenacity.wait_exponential_jitter."
source: "https://reference.langchain.com/python/langchain-core/runnables/retry/ExponentialJitterParams"
category: "reference"
tags: [reference, langchain-core, runnables, retry, exponentialjitterparams]
---

# ExponentialJitterParams

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/retry/ExponentialJitterParams)

Parameters for `tenacity.wait_exponential_jitter`.

## Signature

```python
ExponentialJitterParams()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    initial: float,
    max: float,
    exp_base: float,
    jitter: float,
)
```

| Name | Type |
|------|------|
| `initial` | `float` |
| `max` | `float` |
| `exp_base` | `float` |
| `jitter` | `float` |

## Properties

- `initial`
- `max`
- `exp_base`
- `jitter`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/retry.py#L35)
