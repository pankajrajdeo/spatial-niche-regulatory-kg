---
title: "compile"
description: "Compiles the StateGraph into a CompiledStateGraph object."
source: "https://reference.langchain.com/python/langgraph/graph/state/StateGraph/compile"
category: "reference"
tags: [reference, langgraph, graph, state, stategraph, compile]
---

# compile

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/state/StateGraph/compile)

Compiles the `StateGraph` into a `CompiledStateGraph` object.

The compiled graph implements the `Runnable` interface and can be invoked,
streamed, batched, and run asynchronously.

## Signature

```python
compile(
    self,
    checkpointer: Checkpointer = None,
    *,
    cache: BaseCache | None = None,
    store: BaseStore | None = None,
    interrupt_before: All | list[str] | None = None,
    interrupt_after: All | list[str] | None = None,
    debug: bool = False,
    name: str | None = None,
    transformers: Sequence[Callable[[tuple[str, ...]], Any]] | None = None,
) -> CompiledStateGraph[StateT, ContextT, InputT, OutputT]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `checkpointer` | `Checkpointer` | No | A checkpoint saver object or flag.  If provided, this `Checkpointer` serves as a fully versioned "short-term memory" for the graph, allowing it to be paused, resumed, and replayed from any point.  If `None`, it may inherit the parent graph's checkpointer when used as a subgraph.  If `False`, it will not use or inherit any checkpointer.  **Important**: When a checkpointer is enabled, you should pass a `thread_id` in the config when invoking the graph:  ```python config = {"configurable": {"thread_id": "my-thread"}} graph.invoke(inputs, config) ```  The `thread_id` is the key used to store and retrieve checkpoints. Use a unique ID for independent runs, or reuse the same ID to accumulate state across invocations (e.g., for conversation memory). (default: `None`) |
| `interrupt_before` | `All \| list[str] \| None` | No | An optional list of node names to interrupt before. (default: `None`) |
| `interrupt_after` | `All \| list[str] \| None` | No | An optional list of node names to interrupt after. (default: `None`) |
| `debug` | `bool` | No | A flag indicating whether to enable debug mode. (default: `False`) |
| `name` | `str \| None` | No | The name to use for the compiled graph. (default: `None`) |
| `transformers` | `Sequence[Callable[[tuple[str, ...]], Any]] \| None` | No | Optional sequence of `StreamTransformer` classes or configured factories. Classes and factories are instantiated per run whenever `stream_events(version="v3")` / `astream_events(version="v3")` is called and are propagated to subgraph scopes. Custom factories should follow the standard `StreamTransformer` constructor shape by accepting `scope` as their first argument. Appended after the built-in stream transformers. (default: `None`) |

## Returns

`CompiledStateGraph[StateT, ContextT, InputT, OutputT]`

The compiled `StateGraph`.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/graph/state.py#L1177)
