---
title: "astream_events"
description: "Async-stream events from this remote graph."
source: "https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/astream_events"
category: "reference"
tags: [reference, langgraph, pregel, remote, remotegraph, astream_events]
---

# astream_events

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/astream_events)

Async-stream events from this remote graph.

For `version="v3"`, awaits to an `_AsyncRemoteGraphRunStream`, matching
the local `Pregel.astream_events(version="v3")` awaitable contract:
`async with await rg.astream_events(..., version="v3") as run`. For
`version="v1"`/`"v2"`, raises NotImplementedError (use `astream`).

## Signature

```python
astream_events(
    self,
    input: Any,
    config: RunnableConfig | None = None,
    *,
    version: Literal['v1', 'v2', 'v3'] = 'v2',
    interrupt_before: All | Sequence[str] | None = None,
    interrupt_after: All | Sequence[str] | None = None,
    control: Any = None,
    transformers: Sequence[Any] | None = None,
    headers: dict[str, str] | None = None,
    **kwargs: Any = {},
) -> Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/remote.py#L1080)
