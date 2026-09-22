---
title: "stream_events"
description: "Stream events from this graph."
source: "https://reference.langchain.com/python/langgraph/pregel/main/Pregel/stream_events"
category: "reference"
tags: [reference, langgraph, pregel, main, stream_events]
---

# stream_events

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main/Pregel/stream_events)

Stream events from this graph.

For `version="v1"` / `"v2"`, yields `StreamEvent` dicts (see
`Runnable.stream_events`). For `version="v3"`, returns a
`GraphRunStream` whose typed projections the caller drives by
iterating — no background thread.

!!! warning

    The `version="v3"` API is experimental and may change.

Builds a `StreamMux` from the built-in transformers, this
graph's compile-time `stream_transformers`, and any additional
`transformers=` supplied at the call site. `run.output`,
`run.interrupted`, and `run.interrupts` work regardless of
which transformers are registered.

## Signature

```python
stream_events(
    self,
    input: InputT | Command | None,
    config: RunnableConfig | None = None,
    *,
    version: Literal['v1', 'v2', 'v3'] = 'v2',
    interrupt_before: All | Sequence[str] | None = None,
    interrupt_after: All | Sequence[str] | None = None,
    control: RunControl | None = None,
    transformers: Sequence[Callable[[tuple[str, ...]], Any]] | None = None,
    **kwargs: Any = {},
) -> Any
```

## Description

**Note:**

Nesting v1 `stream(stream_mode="messages")` inside a node
of a `stream_events(version="v3")` run is not fully
supported. The outer v3 messages handler reroutes
`BaseChatModel.invoke` through the v2 event protocol, so
the inner v1 handler does not see `on_llm_new_token`
chunks. The inner stream still yields a finalized message
via `on_llm_end`. Use `stream_events(version="v3")` for the
inner graph as well, or call `chat_model.stream(...)`
explicitly, to get token-level streaming.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `InputT \| Command \| None` | Yes | Graph input. |
| `config` | `RunnableConfig \| None` | No | Optional runnable config. (default: `None`) |
| `version` | `Literal['v1', 'v2', 'v3']` | No | Streaming-event schema version. `"v3"` selects the content-block-centric streaming protocol. (default: `'v2'`) |
| `interrupt_before` | `All \| Sequence[str] \| None` | No | Nodes to interrupt before, if any. Only used for `version="v3"`. (default: `None`) |
| `interrupt_after` | `All \| Sequence[str] \| None` | No | Nodes to interrupt after, if any. Only used for `version="v3"`. (default: `None`) |
| `control` | `RunControl \| None` | No | Optional run control used to request cooperative drain. Only used for `version="v3"`. (default: `None`) |
| `transformers` | `Sequence[Callable[[tuple[str, ...]], Any]] \| None` | No | Extra transformer classes or configured factories appended after compile-time `stream_transformers`. Factories are called as `factory(scope)` so they can propagate to subgraph scopes. Only used for `version="v3"`. (default: `None`) |
| `**kwargs` | `Any` | No | For `version="v1"`/`"v2"`, forwarded to `Runnable.stream_events`. For `version="v3"`, forwarded to the underlying `stream(...)` call (e.g. `context`, `durability`, `output_keys`, `print_mode`, `debug`). `stream_mode` and `subgraphs` are not accepted under `version="v3"` and raise `TypeError` if supplied; v3 owns them. (default: `{}`) |

## Returns

`Any`

For `version="v3"`, a `GraphRunStream` the caller iterates

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/main.py#L3638)
