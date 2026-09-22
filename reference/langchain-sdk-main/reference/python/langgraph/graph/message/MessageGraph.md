---
title: "MessageGraph"
description: "A StateGraph where every node receives a list of messages as input and returns one or more messages as output."
source: "https://reference.langchain.com/python/langgraph/graph/message/MessageGraph"
category: "reference"
tags: [reference, langgraph, graph, message, messagegraph]
---

# MessageGraph

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/message/MessageGraph)

A StateGraph where every node receives a list of messages as input and returns one or more messages as output.

MessageGraph is a subclass of StateGraph whose entire state is a single, append-only* list of messages.
Each node in a MessageGraph takes a list of messages as input and returns zero or more
messages as output. The `add_messages` function is used to merge the output messages from each node
into the existing list of messages in the graph's state.

## Signature

```python
MessageGraph(
    self,
)
```

## Extends

- `StateGraph`

## Constructors

```python
__init__(
    self,
) -> None
```

## ⚠️ Deprecated

MessageGraph is deprecated in langgraph 1.0.0, to be removed in 2.0.0. Please use StateGraph with a `messages` key instead.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/graph/message.py#L312)
