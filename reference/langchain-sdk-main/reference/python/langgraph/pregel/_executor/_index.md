---
title: "reference/python/langgraph/pregel/_executor"
description: "Index of 7 pages and 2 subdirectories under reference/python/langgraph/pregel/_executor."
category: "index"
tags: [index, reference, python, langgraph, pregel, executor]
---

# reference/python/langgraph/pregel/_executor

7 pages here, 18 pages including subdirectories.

## Directories

- [AsyncBackgroundExecutor/](AsyncBackgroundExecutor/_index.md) - 6 pages
- [BackgroundExecutor/](BackgroundExecutor/_index.md) - 5 pages

## Files

- [AsyncBackgroundExecutor](AsyncBackgroundExecutor.md) - A context manager that runs async tasks in the background. Uses the current event loop to delegate tasks to asyncio tasks. On exit, - cancels any tasks with __cancel_on_exit__=True - waits for all...
- [BackgroundExecutor](BackgroundExecutor.md) - A context manager that runs sync tasks in the background. Uses a thread pool executor to delegate tasks to separate threads. On exit, - cancels any (not yet started) tasks with...
- [P](P.md) - View source on GitHub
- [Submit](Submit.md) - - Protocol[P, T]
- [T](T.md) - View source on GitHub
- [gated](gated.md) - A coroutine that waits for a semaphore before running another coroutine.
- [next_tick](next_tick.md) - A function that yields control to other threads before running another function.
