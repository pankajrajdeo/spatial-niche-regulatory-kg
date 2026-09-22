---
title: "arun_with_retry"
description: "Run a task asynchronously with retries."
source: "https://reference.langchain.com/python/langgraph/pregel/_retry/arun_with_retry"
category: "reference"
tags: [reference, langgraph, pregel, retry, arun_with_retry]
---

# arun_with_retry

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_retry/arun_with_retry)

Run a task asynchronously with retries.

## Signature

```python
arun_with_retry(
    task: PregelExecutableTask,
    retry_policy: Sequence[RetryPolicy] | None,
    stream: bool = False,
    match_cached_writes: Callable[[], Awaitable[Sequence[PregelExecutableTask]]] | None = None,
    configurable: dict[str, Any] | None = None,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_retry.py#L685)
