---
title: "bind_tools"
description: "Bind tools to the model."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/bind_tools"
category: "reference"
tags: [reference, langchain-core, language_models, chat_models, basechatmodel, bind_tools]
---

# bind_tools

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/bind_tools)

Bind tools to the model.

## Signature

```python
bind_tools(
    self,
    tools: Sequence[builtins.dict[str, Any] | type | Callable[..., Any] | BaseTool],
    *,
    tool_choice: str | None = None,
    **kwargs: Any = {},
) -> Runnable[LanguageModelInput, AIMessage]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tools` | `Sequence[builtins.dict[str, Any] \| type \| Callable[..., Any] \| BaseTool]` | Yes | Sequence of tools to bind to the model. |
| `tool_choice` | `str \| None` | No | The tool to use. If "any" then any tool can be used. (default: `None`) |

## Returns

`Runnable[LanguageModelInput, AIMessage]`

A Runnable that returns a message.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/language_models/chat_models.py#L2366)
