---
title: "subscribe_to"
description: "Add channels to subscribe to."
source: "https://reference.langchain.com/python/langgraph/pregel/main/NodeBuilder/subscribe_to"
category: "reference"
tags: [reference, langgraph, pregel, main, nodebuilder, subscribe_to]
---

# subscribe_to

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main/NodeBuilder/subscribe_to)

Add channels to subscribe to.

Node will be invoked when any of these channels are updated, with a dict of the
channel values as input.

## Signature

```python
subscribe_to(
    self,
    *channels: str = (),
    read: bool = True,
) -> Self
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `channels` | `str` | No | Channel name(s) to subscribe to (default: `()`) |
| `read` | `bool` | No | If `True`, the channels will be included in the input to the node. Otherwise, they will trigger the node without being sent in input. (default: `True`) |

## Returns

`Self`

Self for chaining

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/main.py#L258)
