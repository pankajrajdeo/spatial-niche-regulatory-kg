---
title: "pre_init"
description: "Decorator to run a function before model initialization."
source: "https://reference.langchain.com/python/langchain-core/utils/pydantic/pre_init"
category: "reference"
tags: [reference, langchain-core, utils, pydantic, pre_init]
---

# pre_init

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/pydantic/pre_init)

Decorator to run a function before model initialization.

## Signature

```python
pre_init(
    func: Callable[[Any, dict[str, Any]], Any],
) -> Callable[[Any, dict[str, Any]], Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Callable[[Any, dict[str, Any]], Any]` | Yes | The function to run before model initialization. |

## Returns

`Callable[[Any, dict[str, Any]], Any]`

The decorated function.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/pydantic.py#L130)
