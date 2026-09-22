---
title: "is_pydantic_v2_subclass"
description: "Check if the given class is Pydantic v2-like."
source: "https://reference.langchain.com/python/langchain-core/utils/pydantic/is_pydantic_v2_subclass"
category: "reference"
tags: [reference, langchain-core, utils, pydantic, is_pydantic_v2_subclass]
---

# is_pydantic_v2_subclass

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/pydantic/is_pydantic_v2_subclass)

Check if the given class is Pydantic v2-like.

## Signature

```python
is_pydantic_v2_subclass(
    cls: type,
) -> TypeGuard[type[BaseModel]]
```

## Returns

`TypeGuard[type[BaseModel]]`

`True` if the given class is a subclass of Pydantic `BaseModel` 2.x.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/pydantic.py#L88)
