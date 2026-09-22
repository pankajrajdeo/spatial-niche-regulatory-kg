---
title: "ModelRequest"
description: "Model request information for the agent."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/ModelRequest"
category: "reference"
tags: [reference, langchain, agents, middleware, types, modelrequest]
---

# ModelRequest

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/ModelRequest)

Model request information for the agent.

## Signature

```python
ModelRequest(
    self,
    *,
    model: BaseChatModel,
    messages: list[AnyMessage],
    system_message: SystemMessage | None = None,
    system_prompt: str | None = None,
    tool_choice: Any | None = None,
    tools: list[BaseTool | dict[str, Any]] | None = None,
    response_format: ResponseFormat[Any] | None = None,
    state: AgentState[Any] | None = None,
    runtime: Runtime[ContextT] | None = None,
    model_settings: dict[str, Any] | None = None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `BaseChatModel` | Yes | The chat model to use. |
| `messages` | `list[AnyMessage]` | Yes | List of messages (excluding system prompt). |
| `tool_choice` | `Any \| None` | No | Tool choice configuration. (default: `None`) |
| `tools` | `list[BaseTool \| dict[str, Any]] \| None` | No | List of available tools. (default: `None`) |
| `response_format` | `ResponseFormat[Any] \| None` | No | Response format specification. (default: `None`) |
| `state` | `AgentState[Any] \| None` | No | Agent state. (default: `None`) |
| `runtime` | `Runtime[ContextT] \| None` | No | Runtime context. (default: `None`) |
| `model_settings` | `dict[str, Any] \| None` | No | Additional model settings. (default: `None`) |
| `system_message` | `SystemMessage \| None` | No | System message instance (preferred). (default: `None`) |
| `system_prompt` | `str \| None` | No | System prompt string (deprecated, converted to `SystemMessage`). (default: `None`) |

## Extends

- `Generic[ContextT]`

## Constructors

```python
__init__(
    self,
    *,
    model: BaseChatModel,
    messages: list[AnyMessage],
    system_message: SystemMessage | None = None,
    system_prompt: str | None = None,
    tool_choice: Any | None = None,
    tools: list[BaseTool | dict[str, Any]] | None = None,
    response_format: ResponseFormat[Any] | None = None,
    state: AgentState[Any] | None = None,
    runtime: Runtime[ContextT] | None = None,
    model_settings: dict[str, Any] | None = None,
) -> None
```

| Name | Type |
|------|------|
| `model` | `BaseChatModel` |
| `messages` | `list[AnyMessage]` |
| `system_message` | `SystemMessage \| None` |
| `system_prompt` | `str \| None` |
| `tool_choice` | `Any \| None` |
| `tools` | `list[BaseTool \| dict[str, Any]] \| None` |
| `response_format` | `ResponseFormat[Any] \| None` |
| `state` | `AgentState[Any] \| None` |
| `runtime` | `Runtime[ContextT] \| None` |
| `model_settings` | `dict[str, Any] \| None` |

## Properties

- `model`
- `messages`
- `system_message`
- `tool_choice`
- `tools`
- `response_format`
- `state`
- `runtime`
- `model_settings`
- `system_prompt`

## Methods

- [`override()`](https://reference.langchain.com/python/langchain/agents/middleware/types/ModelRequest/override)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L87)
