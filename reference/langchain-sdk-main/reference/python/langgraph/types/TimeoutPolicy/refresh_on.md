---
title: "refresh_on"
description: "Which signals refresh idle_timeout."
source: "https://reference.langchain.com/python/langgraph/types/TimeoutPolicy/refresh_on"
category: "reference"
tags: [reference, langgraph, types, timeoutpolicy, refresh_on]
---

# refresh_on

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/TimeoutPolicy/refresh_on)

Which signals refresh `idle_timeout`.

`"auto"` refreshes on standard graph progress signals and explicit heartbeats.
`"heartbeat"` refreshes only on explicit `runtime.heartbeat()` calls.

## Signature

```python
refresh_on: Literal['auto', 'heartbeat'] = 'auto'
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/types.py#L476)
