---
title: "recast_checkpoint_ns"
description: "Remove task IDs from checkpoint namespace."
source: "https://reference.langchain.com/python/langgraph/pregel/main/recast_checkpoint_ns"
category: "reference"
tags: [reference, langgraph, pregel, main, recast_checkpoint_ns]
---

# recast_checkpoint_ns

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_config/recast_checkpoint_ns)

Remove task IDs from checkpoint namespace.

## Signature

```python
recast_checkpoint_ns(
    ns: str,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `ns` | `str` | Yes | The checkpoint namespace with task IDs. |

## Returns

`str`

The checkpoint namespace without task IDs.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/_internal/_config.py#L38)
