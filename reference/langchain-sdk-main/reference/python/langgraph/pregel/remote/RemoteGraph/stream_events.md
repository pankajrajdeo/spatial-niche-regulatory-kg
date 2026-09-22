---
title: "stream_events"
description: "Stream events from this remote graph."
source: "https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/stream_events"
category: "reference"
tags: [reference, langgraph, pregel, remote, remotegraph, stream_events]
---

# stream_events

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/remote/RemoteGraph/stream_events)

Stream events from this remote graph.

For `version="v3"`, returns a `_RemoteGraphRunStream` whose surface
matches the local `GraphRunStream`. For other versions, delegates to
`Runnable.stream_events`.

## Signature

```python
stream_events(
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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/remote.py#L1033)
