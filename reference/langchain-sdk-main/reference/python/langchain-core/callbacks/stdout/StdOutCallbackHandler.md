---
title: "StdOutCallbackHandler"
description: "Callback handler that prints to std out."
source: "https://reference.langchain.com/python/langchain-core/callbacks/stdout/StdOutCallbackHandler"
category: "reference"
tags: [reference, langchain-core, callbacks, stdout, stdoutcallbackhandler]
---

# StdOutCallbackHandler

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/stdout/StdOutCallbackHandler)

Callback handler that prints to std out.

## Signature

```python
StdOutCallbackHandler(
    self,
    color: str | None = None,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `color` | `str \| None` | No | The color to use for the text. (default: `None`) |

## Extends

- `BaseCallbackHandler`

## Constructors

```python
__init__(
    self,
    color: str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `color` | `str \| None` |

## Properties

- `color`

## Methods

- [`on_chain_start()`](https://reference.langchain.com/python/langchain-core/callbacks/stdout/StdOutCallbackHandler/on_chain_start)
- [`on_chain_end()`](https://reference.langchain.com/python/langchain-core/callbacks/stdout/StdOutCallbackHandler/on_chain_end)
- [`on_agent_action()`](https://reference.langchain.com/python/langchain-core/callbacks/stdout/StdOutCallbackHandler/on_agent_action)
- [`on_tool_end()`](https://reference.langchain.com/python/langchain-core/callbacks/stdout/StdOutCallbackHandler/on_tool_end)
- [`on_text()`](https://reference.langchain.com/python/langchain-core/callbacks/stdout/StdOutCallbackHandler/on_text)
- [`on_agent_finish()`](https://reference.langchain.com/python/langchain-core/callbacks/stdout/StdOutCallbackHandler/on_agent_finish)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/stdout.py#L16)
