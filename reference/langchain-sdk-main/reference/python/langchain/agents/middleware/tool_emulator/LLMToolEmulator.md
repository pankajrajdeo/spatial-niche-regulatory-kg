---
title: "LLMToolEmulator"
description: "Emulates specified tools using an LLM instead of executing them."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_emulator/LLMToolEmulator"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_emulator, llmtoolemulator]
---

# LLMToolEmulator

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_emulator/LLMToolEmulator)

Emulates specified tools using an LLM instead of executing them.

This middleware allows selective emulation of tools for testing purposes.

By default (when `tools=None`), all tools are emulated. You can specify which
tools to emulate by passing a list of tool names or `BaseTool` instances.

## Signature

```python
LLMToolEmulator(
    self,
    *,
    tools: list[str | BaseTool] | None = None,
    model: str | BaseChatModel | None = None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tools` | `list[str \| BaseTool] \| None` | No | List of tool names (`str`) or `BaseTool` instances to emulate.  If `None`, ALL tools will be emulated.  If empty list, no tools will be emulated. (default: `None`) |
| `model` | `str \| BaseChatModel \| None` | No | Model to use for emulation.  Defaults to `'anthropic:claude-sonnet-4-5-20250929'`, which requires `langchain-anthropic` to be installed.  !!! warning "Deprecated"     Relying on the implicit default is deprecated and will be     removed in a future release, since it makes this middleware     depend on `langchain-anthropic` even when unspecified. Pass     `model` explicitly instead.  Can be a model identifier string or `BaseChatModel` instance. (default: `None`) |

## Extends

- `AgentMiddleware[AgentState[Any], ContextT]`
- `Generic[ContextT]`

## Constructors

```python
__init__(
    self,
    *,
    tools: list[str | BaseTool] | None = None,
    model: str | BaseChatModel | None = None,
) -> None
```

| Name | Type |
|------|------|
| `tools` | `list[str \| BaseTool] \| None` |
| `model` | `str \| BaseChatModel \| None` |

## Properties

- `transformers`
- `emulate_all`
- `tools_to_emulate`
- `model`

## Methods

- [`wrap_tool_call()`](https://reference.langchain.com/python/langchain/agents/middleware/tool_emulator/LLMToolEmulator/wrap_tool_call)
- [`awrap_tool_call()`](https://reference.langchain.com/python/langchain/agents/middleware/tool_emulator/LLMToolEmulator/awrap_tool_call)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/tool_emulator.py#L29)
