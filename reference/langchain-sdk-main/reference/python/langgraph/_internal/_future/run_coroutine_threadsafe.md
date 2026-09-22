---
title: "run_coroutine_threadsafe"
description: "Submit a coroutine object to a given event loop."
source: "https://reference.langchain.com/python/langgraph/_internal/_future/run_coroutine_threadsafe"
category: "reference"
tags: [reference, langgraph, internal, future, run_coroutine_threadsafe]
---

# run_coroutine_threadsafe

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_future/run_coroutine_threadsafe)

Submit a coroutine object to a given event loop.

Return an asyncio.Future to access the result.

## Signature

```python
run_coroutine_threadsafe(
    coro: Coroutine[None, None, T],
    loop: asyncio.AbstractEventLoop,
    *,
    lazy: bool,
    name: str | None = None,
    context: contextvars.Context | None = None,
) -> asyncio.Future[T]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/_internal/_future.py#L189)
