---
title: "xor_args"
description: "Validate specified keyword args are mutually exclusive."
source: "https://reference.langchain.com/python/langchain-core/utils/utils/xor_args"
category: "reference"
tags: [reference, langchain-core, utils, xor_args]
---

# xor_args

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/utils/xor_args)

Validate specified keyword args are mutually exclusive.

## Signature

```python
xor_args(
    *arg_groups: tuple[str, ...] = (),
) -> Callable[..., Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `*arg_groups` | `tuple[str, ...]` | No | Groups of mutually exclusive keyword args. (default: `()`) |

## Returns

`Callable[..., Any]`

Decorator that validates the specified keyword args are mutually exclusive.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/utils.py#L24)
