---
title: "invoke"
description: "Run the graph with a single input and config."
source: "https://reference.langchain.com/python/langgraph/pregel/main/Pregel/invoke"
category: "reference"
tags: [reference, langgraph, pregel, main, invoke]
---

# invoke

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main/Pregel/invoke)

Run the graph with a single input and config.

## Signature

```python
invoke(
    self,
    input: InputT | Command | None,
    config: RunnableConfig | None = None,
    *,
    context: ContextT | None = None,
    stream_mode: StreamMode = 'values',
    print_mode: StreamMode | Sequence[StreamMode] = (),
    output_keys: str | Sequence[str] | None = None,
    interrupt_before: All | Sequence[str] | None = None,
    interrupt_after: All | Sequence[str] | None = None,
    durability: Durability | None = None,
    control: RunControl | None = None,
    version: Literal['v1', 'v2'] = 'v1',
    **kwargs: Any = {},
) -> dict[str, Any] | Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `InputT \| Command \| None` | Yes | The input data for the graph. It can be a dictionary or any other type. |
| `config` | `RunnableConfig \| None` | No | The configuration for the graph run. (default: `None`) |
| `context` | `ContextT \| None` | No | The static context to use for the run. !!! version-added "Added in version 0.6.0" (default: `None`) |
| `stream_mode` | `StreamMode` | No | The stream mode for the graph run. (default: `'values'`) |
| `print_mode` | `StreamMode \| Sequence[StreamMode]` | No | Accepts the same values as `stream_mode`, but only prints the output to the console, for debugging purposes.  Does not affect the output of the graph in any way. (default: `()`) |
| `output_keys` | `str \| Sequence[str] \| None` | No | The output keys to retrieve from the graph run. (default: `None`) |
| `interrupt_before` | `All \| Sequence[str] \| None` | No | The nodes to interrupt the graph run before. (default: `None`) |
| `interrupt_after` | `All \| Sequence[str] \| None` | No | The nodes to interrupt the graph run after. (default: `None`) |
| `durability` | `Durability \| None` | No | The durability mode for the graph execution, defaults to `"async"`.  Options are:  - `"sync"`: Changes are persisted synchronously before the next step starts. - `"async"`: Changes are persisted asynchronously while the next step executes. - `"exit"`: Changes are persisted only when the graph exits. (default: `None`) |
| `control` | `RunControl \| None` | No | Optional run control used to request cooperative drain. (default: `None`) |
| `version` | `Literal['v1', 'v2']` | No | The streaming format version. `"v1"` (default) returns the traditional format, `"v2"` returns `StreamPart` typed dicts when `stream_mode` is not `"values"`. (default: `'v1'`) |
| `**kwargs` | `Any` | No | Additional keyword arguments to pass to the graph run. (default: `{}`) |

## Returns

`dict[str, Any] | Any`

The output of the graph run. If `stream_mode` is `"values"`, it returns the latest output.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/main.py#L3836)
