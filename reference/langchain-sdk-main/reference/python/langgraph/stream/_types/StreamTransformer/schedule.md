---
title: "schedule"
description: "Schedule a coroutine tied to this transformer's lifecycle."
source: "https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/schedule"
category: "reference"
tags: [reference, langgraph, stream, types, streamtransformer, schedule]
---

# schedule

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/schedule)

Schedule a coroutine tied to this transformer's lifecycle.

The mux holds the task reference, awaits all scheduled tasks
during `aclose()` before calling `afinalize()`, and cancels
them on `afail()`. Authors don't need to track tasks or
implement the last-task-closes-the-log dance.

Requires a running event loop — call only under `astream()`.
Set `requires_async = True` on the class so registration under
sync `stream()` fails fast with a clear message.

## Signature

```python
schedule(
    self,
    coro: Coroutine[Any, Any, Any],
    *,
    on_error: Literal['log', 'raise'] = 'log',
) -> asyncio.Task[Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `coro` | `Coroutine[Any, Any, Any]` | Yes | The coroutine to run. Its lifecycle is owned by the mux from this point on. |
| `on_error` | `Literal['log', 'raise']` | No | `"log"` (default) catches and logs any exception the coroutine raises, so a single failure doesn't tear down the run. `"raise"` lets the exception propagate when the mux joins pendings, converting the close path into the fail path. (default: `'log'`) |

## Returns

`asyncio.Task[Any]`

The asyncio Task. Authors rarely need to await it directly

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/stream/_types.py#L233)
