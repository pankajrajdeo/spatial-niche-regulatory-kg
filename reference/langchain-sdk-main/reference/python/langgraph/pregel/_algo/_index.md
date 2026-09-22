---
title: "reference/python/langgraph/pregel/_algo"
description: "Index of 20 pages and 3 subdirectories under reference/python/langgraph/pregel/_algo."
category: "index"
tags: [index, reference, python, langgraph, pregel, algo]
---

# reference/python/langgraph/pregel/_algo

20 pages here, 34 pages including subdirectories.

## Directories

- [Call/](Call/_index.md) - 6 pages
- [PregelTaskWrites/](PregelTaskWrites/_index.md) - 4 pages
- [WritesProtocol/](WritesProtocol/_index.md) - 4 pages

## Files

- [Call](Call.md) - - func - input - retry_policy - cache_policy - callbacks - timeout
- [GetNextVersion](GetNextVersion.md) - View source on GitHub
- [LAZY_ATOMIC_COUNTER_LOCK](LAZY_ATOMIC_COUNTER_LOCK.md) - View source on GitHub
- [LazyAtomicCounter](LazyAtomicCounter.md) - View source on GitHub
- [PUSH_TRIGGER](PUSH_TRIGGER.md) - View source on GitHub
- [PregelTaskWrites](PregelTaskWrites.md) - Simplest implementation of WritesProtocol, for usage with writes that don't originate from a runnable task, eg. graph input, update_state, etc.
- [SUPPORTS_EXC_NOTES](SUPPORTS_EXC_NOTES.md) - View source on GitHub
- [WritesProtocol](WritesProtocol.md) - Protocol for objects containing writes to be applied to checkpoint. Implemented by PregelTaskWrites and PregelExecutableTask.
- [apply_writes](apply_writes.md) - Apply writes from a set of tasks (usually the tasks from a Pregel step) to the checkpoint and channels, and return managed values writes to be applied externally.
- [checkpoint_null_version](checkpoint_null_version.md) - Get the null version for the checkpoint, if available.
- [increment](increment.md) - Default channel versioning function, increments the current int version.
- [local_read](local_read.md) - Function injected under CONFIG_KEY_READ in task config, to read current state. Used by conditional edges to read a copy of the state with reflecting the writes from that node only.
- [prepare_next_tasks](prepare_next_tasks.md) - Prepare the set of tasks that will make up the next Pregel step.
- [prepare_node_error_handler_task](prepare_node_error_handler_task.md) - Prepare an immediate node-level error handler task for a failed task.
- [prepare_push_task_functional](prepare_push_task_functional.md) - Prepare a push task with an attached caller. Used for the functional API.
- [prepare_push_task_send](prepare_push_task_send.md) - View source on GitHub
- [prepare_single_task](prepare_single_task.md) - Prepares a single task for the next Pregel step, given a task path, which uniquely identifies a PUSH or PULL task within the graph.
- [sanitize_untracked_values_in_send](sanitize_untracked_values_in_send.md) - Pop any values belonging to UntrackedValue channels in Send.arg for safe checkpointing.
- [should_interrupt](should_interrupt.md) - Check if the graph should be interrupted based on current state.
- [task_path_str](task_path_str.md) - Generate a string representation of the task path.
