---
title: "metadata"
description: "Metadata associated with the Runnable that generated this event."
source: "https://reference.langchain.com/python/langchain-core/runnables/schema/BaseStreamEvent/metadata"
category: "reference"
tags: [reference, langchain-core, runnables, schema, basestreamevent, metadata]
---

# metadata

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/schema/BaseStreamEvent/metadata)

Metadata associated with the `Runnable` that generated this event.

Metadata can either be bound to a `Runnable` using

    `.with_config({"metadata": { "foo": "bar" }})`

or passed at run time using

    `.astream_events(..., {"metadata": {"foo": "bar"}})`.

## Signature

```python
metadata: NotRequired[dict[str, Any]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/schema.py#L138)
