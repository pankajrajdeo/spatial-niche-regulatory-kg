---
title: "override"
description: "Replace the request with a new request with the given overrides."
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/ModelRequest/override"
category: "reference"
tags: [reference, langchain, agents, middleware, types, modelrequest, override]
---

# override

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/ModelRequest/override)

Replace the request with a new request with the given overrides.

Returns a new `ModelRequest` instance with the specified attributes replaced.

This follows an immutable pattern, leaving the original request unchanged.

## Signature

```python
override(
    self,
    **overrides: Unpack[_ModelRequestOverrides] = {},
) -> ModelRequest[ContextT]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**overrides` | `Unpack[_ModelRequestOverrides]` | No | Keyword arguments for attributes to override.  Supported keys:  - `model`: `BaseChatModel` instance - `system_prompt`: deprecated, use `system_message` instead - `system_message`: `SystemMessage` instance - `messages`: `list` of messages - `tool_choice`: Tool choice configuration - `tools`: `list` of available tools - `response_format`: Response format specification - `model_settings`: Additional model settings - `state`: Agent state dictionary (default: `{}`) |

## Returns

`ModelRequest[ContextT]`

New `ModelRequest` instance with specified overrides applied.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/types.py#L203)
