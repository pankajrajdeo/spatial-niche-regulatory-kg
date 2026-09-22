---
title: "astream"
description: "Asynchronously stream graph steps for a single input."
source: "https://reference.langchain.com/python/langgraph/pregel/main/Pregel/astream"
category: "reference"
tags: [reference, langgraph, pregel, main, astream]
---

# astream

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main/Pregel/astream)

Asynchronously stream graph steps for a single input.

## Signature

```python
astream(
    self,
    input: InputT | Command | None,
    config: RunnableConfig | None = None,
    *,
    context: ContextT | None = None,
    stream_mode: StreamMode | Sequence[StreamMode] | None = None,
    print_mode: StreamMode | Sequence[StreamMode] = (),
    output_keys: str | Sequence[str] | None = None,
    interrupt_before: All | Sequence[str] | None = None,
    interrupt_after: All | Sequence[str] | None = None,
    durability: Durability | None = None,
    control: RunControl | None = None,
    subgraphs: bool = False,
    debug: bool | None = None,
    version: Literal['v1', 'v2'] = 'v1',
    **kwargs: Unpack[DeprecatedKwargs] = {},
) -> AsyncIterator[dict[str, Any] | Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `InputT \| Command \| None` | Yes | The input to the graph. |
| `config` | `RunnableConfig \| None` | No | The configuration to use for the run. (default: `None`) |
| `context` | `ContextT \| None` | No | The static context to use for the run. !!! version-added "Added in version 0.6.0" (default: `None`) |
| `stream_mode` | `StreamMode \| Sequence[StreamMode] \| None` | No | The mode to stream output, defaults to `self.stream_mode`.  Options are:  - `"values"`: Emit all values in the state after each step, including interrupts.     When used with functional API, values are emitted once at the end of the workflow. - `"updates"`: Emit only the node or task names and updates returned by the nodes or tasks after each step.     If multiple updates are made in the same step (e.g. multiple nodes are run) then those updates are emitted separately. - `"custom"`: Emit custom data from inside nodes or tasks using `StreamWriter`. - `"messages"`: Emit LLM messages token-by-token together with metadata for any LLM invocations inside nodes or tasks.     - Will be emitted as 2-tuples `(LLM token, metadata)`. - `"checkpoints"`: Emit an event when a checkpoint is created, in the same format as returned by `get_state()`. - `"tasks"`: Emit events when tasks start and finish, including their results and errors. - `"debug"`: Emit debug events with as much information as possible for each step.  You can pass a list as the `stream_mode` parameter to stream multiple modes at once. The streamed outputs will be tuples of `(mode, data)`.  See [LangGraph streaming guide](../../../../../../langgraph/streaming.md) for more details. (default: `None`) |
| `print_mode` | `StreamMode \| Sequence[StreamMode]` | No | Accepts the same values as `stream_mode`, but only prints the output to the console, for debugging purposes.  Does not affect the output of the graph in any way. (default: `()`) |
| `output_keys` | `str \| Sequence[str] \| None` | No | The keys to stream, defaults to all non-context channels. (default: `None`) |
| `interrupt_before` | `All \| Sequence[str] \| None` | No | Nodes to interrupt before, defaults to all nodes in the graph. (default: `None`) |
| `interrupt_after` | `All \| Sequence[str] \| None` | No | Nodes to interrupt after, defaults to all nodes in the graph. (default: `None`) |
| `durability` | `Durability \| None` | No | The durability mode for the graph execution, defaults to `"async"`.  Options are:  - `"sync"`: Changes are persisted synchronously before the next step starts. - `"async"`: Changes are persisted asynchronously while the next step executes. - `"exit"`: Changes are persisted only when the graph exits. (default: `None`) |
| `control` | `RunControl \| None` | No | Optional run control used to request cooperative drain. (default: `None`) |
| `subgraphs` | `bool` | No | Whether to stream events from inside subgraphs, defaults to `False`.  If `True`, the events will be emitted as tuples `(namespace, data)`, or `(namespace, mode, data)` if `stream_mode` is a list, where `namespace` is a tuple with the path to the node where a subgraph is invoked, e.g. `("parent_node:<task_id>", "child_node:<task_id>")`.  See [LangGraph streaming guide](../../../../../../langgraph/streaming.md) for more details. (default: `False`) |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/main.py#L3063)
