---
title: "reference/python/langgraph/types"
description: "Index of 40 pages and 28 subdirectories under reference/python/langgraph/types."
category: "index"
tags: [index, reference, python, langgraph, types]
---

# reference/python/langgraph/types

40 pages here, 160 pages including subdirectories.

## Directories

- [CacheKey/](CacheKey/_index.md) - 3 pages
- [CachePolicy/](CachePolicy/_index.md) - 2 pages
- [CheckpointPayload/](CheckpointPayload/_index.md) - 6 pages
- [CheckpointStreamPart/](CheckpointStreamPart/_index.md) - 3 pages
- [CheckpointTask/](CheckpointTask/_index.md) - 6 pages
- [Command/](Command/_index.md) - 5 pages
- [CustomStreamPart/](CustomStreamPart/_index.md) - 3 pages
- [DebugStreamPart/](DebugStreamPart/_index.md) - 3 pages
- [GraphOutput/](GraphOutput/_index.md) - 2 pages
- [Interrupt/](Interrupt/_index.md) - 4 pages
- [MessagesStreamPart/](MessagesStreamPart/_index.md) - 3 pages
- [Overwrite/](Overwrite/_index.md) - 2 pages
- [PregelExecutableTask/](PregelExecutableTask/_index.md) - 13 pages
- [PregelTask/](PregelTask/_index.md) - 7 pages
- [RetryPolicy/](RetryPolicy/_index.md) - 6 pages
- [Send/](Send/_index.md) - 3 pages
- [StateSnapshot/](StateSnapshot/_index.md) - 8 pages
- [StateUpdate/](StateUpdate/_index.md) - 3 pages
- [TaskPayload/](TaskPayload/_index.md) - 5 pages
- [TaskResultPayload/](TaskResultPayload/_index.md) - 5 pages
- [TasksStreamPart/](TasksStreamPart/_index.md) - 3 pages
- [TimeoutPolicy/](TimeoutPolicy/_index.md) - 4 pages
- [TracePolicy/](TracePolicy/_index.md) - 2 pages
- [UpdatesStreamPart/](UpdatesStreamPart/_index.md) - 3 pages
- [ValuesStreamPart/](ValuesStreamPart/_index.md) - 4 pages
- [_DebugCheckpointPayload/](_DebugCheckpointPayload/_index.md) - 4 pages
- [_DebugTaskPayload/](_DebugTaskPayload/_index.md) - 4 pages
- [_DebugTaskResultPayload/](_DebugTaskResultPayload/_index.md) - 4 pages

## Files

- [All](All.md) - Special value to indicate that graph should interrupt on all nodes.
- [CacheKey](CacheKey.md) - Cache key for a task.
- [CachePolicy](CachePolicy.md) - Configuration for caching nodes.
- [CheckpointPayload](CheckpointPayload.md) - Payload for a checkpoint event.
- [CheckpointStreamPart](CheckpointStreamPart.md) - Stream part emitted for stream_mode="checkpoints".
- [CheckpointTask](CheckpointTask.md) - A task entry within a CheckpointPayload.
- [Checkpointer](Checkpointer.md) - Type Alias in langgraph
- [Command](Command.md) - One or more commands to update the graph's state and send messages to nodes.
- [CustomStreamPart](CustomStreamPart.md) - Stream part emitted for stream_mode="custom".
- [DebugPayload](DebugPayload.md) - Wrapper payload for debug events. Discriminate on type.
- [DebugStreamPart](DebugStreamPart.md) - Stream part emitted for stream_mode="debug".
- [Durability](Durability.md) - Durability mode for the graph execution.
- [GraphOutput](GraphOutput.md) - Typed container returned by invoke() / ainvoke() with version="v2".
- [Interrupt](Interrupt.md) - Information about an interrupt that occurred in a node.
- [KeyFuncT](KeyFuncT.md) - View source on GitHub
- [MessagesStreamPart](MessagesStreamPart.md) - Stream part emitted for stream_mode="messages".
- [N](N.md) - View source on GitHub
- [OutputT](OutputT.md) - View source on GitHub
- [Overwrite](Overwrite.md) - Bypass a reducer and write the wrapped value directly to a BinaryOperatorAggregate channel.
- [PregelExecutableTask](PregelExecutableTask.md) - - name - input - proc - writes - config - triggers - retry_policy - cache_key - id - path - writers - subgraphs - timeout
- [PregelTask](PregelTask.md) - A Pregel task.
- [RetryPolicy](RetryPolicy.md) - Configuration for retrying nodes.
- [Send](Send.md) - A message or packet to send to a specific node in the graph.
- [StateSnapshot](StateSnapshot.md) - Snapshot of the state of the graph at the beginning of a step.
- [StateT](StateT.md) - View source on GitHub
- [StateUpdate](StateUpdate.md) - - NamedTuple
- [StreamMode](StreamMode.md) - How the stream method should emit outputs.
- [StreamPart](StreamPart.md) - A discriminated union of all v2 stream part types.
- [StreamWriter](StreamWriter.md) - Callable that accepts a single argument and writes it to the output stream. Always injected into nodes if requested as a keyword argument, but it's a no-op when not using stream_mode="custom".
- [TaskPayload](TaskPayload.md) - Payload for a task start event.
- [TaskResultPayload](TaskResultPayload.md) - Payload for a task result event.
- [TasksStreamPart](TasksStreamPart.md) - Stream part emitted for stream_mode="tasks".
- [TimeoutPolicy](TimeoutPolicy.md) - Configuration for timing out node attempts.
- [ToolOutputMixin](ToolOutputMixin.md) - View source on GitHub
- [TracePolicy](TracePolicy.md) - Configuration for how a node's run is traced.
- [UpdatesStreamPart](UpdatesStreamPart.md) - Stream part emitted for stream_mode="updates".
- [ValuesStreamPart](ValuesStreamPart.md) - Stream part emitted for stream_mode="values".
- [ensure_valid_checkpointer](ensure_valid_checkpointer.md) - View source on GitHub
- [interrupt](interrupt.md) - Interrupt the graph with a resumable exception from within a node.
- [omit_payload](omit_payload.md) - TracePolicy helper that records an empty payload, dropping the value entirely.
