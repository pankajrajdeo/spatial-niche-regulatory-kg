---
title: "before_agent"
description: "Load memory content before agent execution (synchronous)."
source: "https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware/before_agent"
category: "reference"
tags: [reference, deepagents, middleware, memory, memorymiddleware, before_agent]
---

# before_agent

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware/before_agent)

Load memory content before agent execution (synchronous).

Loads memory from all configured sources and stores in state.
Only loads if not already present in state.

## Signature

```python
before_agent(
    self,
    state: MemoryState,
    runtime: Runtime,
    config: RunnableConfig,
) -> MemoryStateUpdate | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `MemoryState` | Yes | Current agent state. |
| `runtime` | `Runtime` | Yes | Runtime context. |
| `config` | `RunnableConfig` | Yes | Runnable config. |

## Returns

`MemoryStateUpdate | None`

State update with memory_contents populated.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/memory.py#L279)
