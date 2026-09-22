---
title: "BackgroundExecutor"
description: "A context manager that runs sync tasks in the background. Uses a thread pool executor to delegate tasks to separate threads. On exit, - cancels any (not yet started) tasks with..."
source: "https://reference.langchain.com/python/langgraph/pregel/_executor/BackgroundExecutor"
category: "reference"
tags: [reference, langgraph, pregel, executor, backgroundexecutor]
---

# BackgroundExecutor

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_executor/BackgroundExecutor)

A context manager that runs sync tasks in the background.
Uses a thread pool executor to delegate tasks to separate threads.
On exit,
- cancels any (not yet started) tasks with `__cancel_on_exit__=True`
- waits for all tasks to finish
- re-raises the first exception from tasks with `__reraise_on_exit__=True`

## Signature

```python
BackgroundExecutor(
    self,
    config: RunnableConfig,
)
```

## Extends

- `AbstractContextManager`

## Constructors

```python
__init__(
    self,
    config: RunnableConfig,
) -> None
```

| Name | Type |
|------|------|
| `config` | `RunnableConfig` |

## Properties

- `stack`
- `executor`
- `tasks`

## Methods

- [`submit()`](https://reference.langchain.com/python/langgraph/pregel/_executor/BackgroundExecutor/submit)
- [`done()`](https://reference.langchain.com/python/langgraph/pregel/_executor/BackgroundExecutor/done)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/pregel/_executor.py#L40)
