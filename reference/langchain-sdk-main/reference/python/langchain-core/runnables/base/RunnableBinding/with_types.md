---
title: "with_types"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBinding/with_types"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablebinding, with_types]
---

# with_types

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBinding/with_types)

## Signature

```python
with_types(
    self,
    input_type: type[Input] | BaseModel | None = None,
    output_type: type[Output] | BaseModel | None = None,
) -> Runnable[Input, Output]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L6520)
