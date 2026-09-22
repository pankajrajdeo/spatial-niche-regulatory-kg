---
title: "run_timeout"
description: "Hard wall-clock cap (in seconds) for a single node attempt."
source: "https://reference.langchain.com/python/langgraph/types/TimeoutPolicy/run_timeout"
category: "reference"
tags: [reference, langgraph, types, timeoutpolicy, run_timeout]
---

# run_timeout

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/TimeoutPolicy/run_timeout)

Hard wall-clock cap (in seconds) for a single node attempt.

This timeout is never refreshed by progress signals or `runtime.heartbeat()`.

## Signature

```python
run_timeout: float | timedelta | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/types.py#L467)
