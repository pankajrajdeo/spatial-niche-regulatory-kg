---
title: "custom_output_type"
description: "Override the output type of the underlying Runnable with a custom type."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/custom_output_type"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablebindingbase, custom_output_type]
---

# custom_output_type

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/custom_output_type)

Override the output type of the underlying `Runnable` with a custom type.

The type can be a Pydantic model, or a type annotation (e.g., `list[str]`).

## Signature

```python
custom_output_type: Any | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L5888)
