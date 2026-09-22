---
title: "submit"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/_executor/AsyncBackgroundExecutor/submit"
category: "reference"
tags: [reference, langgraph, pregel, executor, asyncbackgroundexecutor, submit]
---

# submit

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_executor/AsyncBackgroundExecutor/submit)

## Signature

```python
submit(
    self,
    fn: Callable[P, Awaitable[T]],
    *args: P.args = (),
    __name__: str | None = None,
    __cancel_on_exit__: bool = False,
    __reraise_on_exit__: bool = True,
    __next_tick__: bool = False,
    **kwargs: P.kwargs = {},
) -> asyncio.Future[T]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_executor.py#L142)
