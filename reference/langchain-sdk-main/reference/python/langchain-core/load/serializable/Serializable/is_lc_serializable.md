---
title: "is_lc_serializable"
description: "Is this class serializable?"
source: "https://reference.langchain.com/python/langchain-core/load/serializable/Serializable/is_lc_serializable"
category: "reference"
tags: [reference, langchain-core, load, serializable, is_lc_serializable]
---

# is_lc_serializable

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/serializable/Serializable/is_lc_serializable)

Is this class serializable?

By design, even if a class inherits from `Serializable`, it is not serializable
by default. This is to prevent accidental serialization of objects that should
not be serialized.

## Signature

```python
is_lc_serializable(
    cls,
) -> bool
```

## Returns

`bool`

Whether the class is serializable. Default is `False`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/load/serializable.py#L138)
