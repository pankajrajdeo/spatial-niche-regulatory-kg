---
title: "model_copy"
description: "Copy the tool, clearing the schema memo if update affects it."
source: "https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/model_copy"
category: "reference"
tags: [reference, langchain-core, tools, base, basetool, model_copy]
---

# model_copy

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/model_copy)

Copy the tool, clearing the schema memo if `update` affects it.

`model_copy` writes `update` directly to the copy's `__dict__` without
going through `__setattr__`, and private attributes (including the
memo) carry over to the copy, so the memo is cleared here when the
update touches one of the fields the schema is built from.

## Signature

```python
model_copy(
    self,
    *,
    update: Mapping[str, Any] | None = None,
    deep: bool = False,
) -> Self
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/tools/base.py#L644)
