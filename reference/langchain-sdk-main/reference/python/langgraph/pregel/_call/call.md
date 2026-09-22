---
title: "call"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/_call/call"
category: "reference"
tags: [reference, langgraph, pregel, call]
---

# call

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_call/call)

## Signature

```python
call(
    func: Callable[P, Awaitable[T]] | Callable[P, T],
    *args: Any = (),
    retry_policy: Sequence[RetryPolicy] | None = None,
    cache_policy: CachePolicy | None = None,
    timeout: float | timedelta | TimeoutPolicy | None = None,
    **kwargs: Any = {},
) -> SyncAsyncFuture[T]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_call.py#L258)
