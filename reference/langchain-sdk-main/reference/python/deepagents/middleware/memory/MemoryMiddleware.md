---
title: "MemoryMiddleware"
description: "Middleware for loading agent memory from AGENTS.md files."
source: "https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware"
category: "reference"
tags: [reference, deepagents, middleware, memory, memorymiddleware]
---

# MemoryMiddleware

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware)

Middleware for loading agent memory from `AGENTS.md` files.

Loads memory content from configured sources and injects into the system
prompt. Supports multiple sources that are combined together. See
constructor for the full argument list.

## Signature

```python
MemoryMiddleware(
    self,
    *,
    backend: BackendProtocol,
    sources: list[str],
    add_cache_control: bool = False,
    system_prompt: str | None = MEMORY_SYSTEM_PROMPT,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `backend` | `BackendProtocol` | Yes | Backend instance for reading memory sources. |
| `sources` | `list[str]` | Yes | List of memory file paths to load (e.g., `["~/.deepagents/AGENTS.md", "./.deepagents/AGENTS.md"]`).  Display names are automatically derived from the paths.  Sources are loaded in order. |
| `add_cache_control` | `bool` | No | If `True`, tag the last system-message content block with `cache_control: {"type": "ephemeral"}` when the request model is `ChatAnthropic`.  This creates a second prompt-cache breakpoint that pairs with `AnthropicPromptCachingMiddleware`'s breakpoint on the static system prompt, keeping the memory block boundary cached across turns (memory content would otherwise shift after every update and invalidate the prefix cache).  No-ops on non-Anthropic models; Bedrock and Vertex wrappers do not qualify. (default: `False`) |
| `system_prompt` | `str \| None` | No | System-prompt fragment template. Must contain a `{agent_memory}` slot for runtime memory substitution. Pass `None` to skip appending entirely (memory is still loaded into `state["memory_contents"]`). (default: `MEMORY_SYSTEM_PROMPT`) |

## Extends

- `AgentMiddleware[MemoryState, ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    *,
    backend: BackendProtocol,
    sources: list[str],
    add_cache_control: bool = False,
    system_prompt: str | None = MEMORY_SYSTEM_PROMPT,
) -> None
```

| Name | Type |
|------|------|
| `backend` | `BackendProtocol` |
| `sources` | `list[str]` |
| `add_cache_control` | `bool` |
| `system_prompt` | `str \| None` |

## Properties

- `trace_policy`
- `state_schema`
- `sources`
- `system_prompt`

## Methods

- [`before_agent()`](https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware/before_agent)
- [`abefore_agent()`](https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware/abefore_agent)
- [`modify_request()`](https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware/modify_request)
- [`wrap_model_call()`](https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/deepagents/middleware/memory/MemoryMiddleware/awrap_model_call)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/middleware/memory.py#L180)
