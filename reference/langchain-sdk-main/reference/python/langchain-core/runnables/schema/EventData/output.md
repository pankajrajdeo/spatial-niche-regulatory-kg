---
title: "output"
description: "The output of the Runnable that generated the event."
source: "https://reference.langchain.com/python/langchain-core/runnables/schema/EventData/output"
category: "reference"
tags: [reference, langchain-core, runnables, schema, eventdata, output]
---

# output

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/schema/EventData/output)

The output of the `Runnable` that generated the event.

Outputs will only be available at the *END* of the `Runnable`.

For most `Runnable` objects, this field can be inferred from the `chunk` field,
though there might be some exceptions for special a cased `Runnable` (e.g., like
chat models), which may return more information.

## Signature

```python
output: Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/schema.py#L33)
