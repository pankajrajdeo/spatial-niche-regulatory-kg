---
title: "stream_events"
description: "Forward stream_events to the bound runnable with bound kwargs merged."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/stream_events"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnablebindingbase, stream_events]
---

# stream_events

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableBindingBase/stream_events)

Forward `stream_events` to the bound runnable with bound kwargs merged.

For `version="v3"`, the bound runnable's typed stream object (e.g.
`ChatModelStream`) is returned. For `version="v1"` / `"v2"`, dispatches
to the base `Runnable.stream_events`.

Without this override, `__getattr__` would drop `self.kwargs` — losing
tools bound via `bind_tools`, `stop` sequences, etc.

## Signature

```python
stream_events(
    self,
    input: Input,
    config: RunnableConfig | None = None,
    *,
    version: Literal['v1', 'v2', 'v3'] = 'v2',
    **kwargs: Any = {},
) -> Iterator[StreamEvent] | Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L6231)
