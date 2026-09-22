---
title: "heartbeat"
description: "Record progress for the current node's idle_timeout."
source: "https://reference.langchain.com/python/langgraph/runtime/Runtime/heartbeat"
category: "reference"
tags: [reference, langgraph, runtime, heartbeat]
---

# heartbeat

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/runtime/Runtime/heartbeat)

Record progress for the current node's `idle_timeout`.

Call this from inside long-running work that does not naturally emit
writes, stream chunks, child tasks, or LangChain callback events, to
prevent the node from being treated as idle. It is also the only
progress signal honored under `TimeoutPolicy(refresh_on="heartbeat")`.
Outside an idle-timed attempt this is a no-op.

## Signature

```python
heartbeat: Callable[[], None] = field(default=_no_op_heartbeat)
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/runtime.py#L209)
