---
title: "StreamMode"
description: "How the stream method should emit outputs."
source: "https://reference.langchain.com/python/langgraph/types/StreamMode"
category: "reference"
tags: [reference, langgraph, types, streammode]
---

# StreamMode

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/StreamMode)

How the stream method should emit outputs.

- `"values"`: Emit all values in the state after each step, including interrupts.
    When used with functional API, values are emitted once at the end of the workflow.
- `"updates"`: Emit only the node or task names and updates returned by the nodes or tasks after each step.
    If multiple updates are made in the same step (e.g. multiple nodes are run) then those updates are emitted separately.
- `"custom"`: Emit custom data using from inside nodes or tasks using `StreamWriter`.
- `"messages"`: Emit LLM messages token-by-token together with metadata for any LLM invocations inside nodes or tasks.
- `"checkpoints"`: Emit an event when a checkpoint is created, in the same format as returned by `get_state()`.
- `"tasks"`: Emit events when tasks start and finish, including their results and errors.
- `"debug"`: Emit `"checkpoints"` and `"tasks"` events for debugging purposes.

## Signature

```python
StreamMode = Literal['values', 'updates', 'checkpoints', 'tasks', 'debug', 'messages', 'custom']
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/types.py#L122)
