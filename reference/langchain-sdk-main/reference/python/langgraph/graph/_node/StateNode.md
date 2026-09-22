---
title: "StateNode"
description: "Type Alias in langgraph"
source: "https://reference.langchain.com/python/langgraph/graph/_node/StateNode"
category: "reference"
tags: [reference, langgraph, graph, node, statenode]
---

# StateNode

> **Type Alias** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/_node/StateNode)

## Signature

```python
StateNode: TypeAlias = _Node[NodeInputT] | _NodeWithConfig[NodeInputT] | _NodeWithWriter[NodeInputT] | _NodeWithStore[NodeInputT] | _NodeWithWriterStore[NodeInputT] | _NodeWithConfigWriter[NodeInputT] | _NodeWithConfigStore[NodeInputT] | _NodeWithConfigWriterStore[NodeInputT] | _NodeWithRuntime[NodeInputT, ContextT] | Runnable[NodeInputT, Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/graph/_node.py#L76)
