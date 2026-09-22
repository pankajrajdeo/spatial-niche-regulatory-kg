---
title: "FileCallbackHandler"
description: "Callback handler that writes to a file."
source: "https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler"
category: "reference"
tags: [reference, langchain-core, callbacks, file, filecallbackhandler]
---

# FileCallbackHandler

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler)

Callback handler that writes to a file.

This handler supports both context manager usage (recommended) and direct
instantiation (deprecated) for backwards compatibility.

## Signature

```python
FileCallbackHandler(
    self,
    filename: str,
    mode: str = 'a',
    color: str | None = None,
)
```

## Description

!!! note

When not used as a context manager, a deprecation warning will be issued on
first use. The file will be opened immediately in `__init__` and closed in
`__del__` or when `close()` is called explicitly.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `filename` | `str` | Yes | The file path to write to. |
| `mode` | `str` | No | The file open mode. Defaults to `'a'` (append). (default: `'a'`) |
| `color` | `str \| None` | No | Default color for text output. (default: `None`) |

## Extends

- `BaseCallbackHandler`

## Constructors

```python
__init__(
    self,
    filename: str,
    mode: str = 'a',
    color: str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `filename` | `str` |
| `mode` | `str` |
| `color` | `str \| None` |

## Properties

- `filename`
- `mode`
- `color`
- `file`

## Methods

- [`close()`](https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/close)
- [`on_chain_start()`](https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_chain_start)
- [`on_chain_end()`](https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_chain_end)
- [`on_agent_action()`](https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_agent_action)
- [`on_tool_end()`](https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_tool_end)
- [`on_text()`](https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_text)
- [`on_agent_finish()`](https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_agent_finish)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/file.py#L21)
