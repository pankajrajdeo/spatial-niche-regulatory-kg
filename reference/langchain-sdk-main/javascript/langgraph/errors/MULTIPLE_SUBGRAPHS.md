---
title: "MULTIPLE_SUBGRAPHS"
description: "This error occurs when you call a subgraph inside a node multiple times, and the subgraph is compiled with checkpointer=True (continuations mode)."
source: "https://docs.langchain.com/oss/javascript/langgraph/errors/MULTIPLE_SUBGRAPHS"
category: "docs"
tags: [docs, javascript, langgraph, errors, multiple_subgraphs]
---

# MULTIPLE_SUBGRAPHS

This error occurs when you [call a subgraph inside a node](../use-subgraphs.md#call-a-subgraph-inside-a-node) multiple times, and the subgraph is compiled with `checkpointer=True` (continuations mode).

## Troubleshooting

Choose one of the following based on your requirements:

1. **Don't need interrupts?** Use `checkpointer: false` to opt out of checkpointing entirely:
```typescript
   const subgraph = subgraphBuilder.compile({ checkpointer: false });
```

2. **Need interrupts but not cross-invocation persistence?** Use the default inherited mode by omitting `checkpointer`:
```typescript
   const subgraph = subgraphBuilder.compile();
```
   Each invocation gets a unique namespace, so parallel execution works. The subgraph starts fresh each time but can use `interrupt()`.

3. **Need cross-invocation persistence?** Use `checkpointer: true`. LangGraph assigns each invocation a position-based namespace suffix (`calling_node`, `calling_node|1`, etc.) to prevent conflicts. For stable, name-based namespaces, wrap each subgraph with a unique node name — see [parallel subgraphs](../use-subgraphs.md#subgraph-persistence).

## Related

* [Subgraph persistence](../use-subgraphs.md#subgraph-persistence) — full comparison of checkpointer modes
* [Persistence](../persistence.md) — how checkpointers work in LangGraph

***

> [!NOTE]
> [Connect these docs](../../../use-these-docs.md) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/errors/MULTIPLE_SUBGRAPHS.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
