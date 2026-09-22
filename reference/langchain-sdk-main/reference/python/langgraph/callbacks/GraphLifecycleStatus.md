---
title: "GraphLifecycleStatus"
description: "Type Alias in langgraph"
source: "https://reference.langchain.com/python/langgraph/callbacks/GraphLifecycleStatus"
category: "reference"
tags: [reference, langgraph, callbacks, graphlifecyclestatus]
---

# GraphLifecycleStatus

> **Type Alias** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/callbacks/GraphLifecycleStatus)

Allowed lifecycle statuses reported in graph lifecycle callback events.

## Signature

```python
GraphLifecycleStatus: TypeAlias = Literal['input', 'pending', 'done', 'interrupt_before', 'interrupt_after', 'out_of_steps']
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/callbacks.py#L31)
