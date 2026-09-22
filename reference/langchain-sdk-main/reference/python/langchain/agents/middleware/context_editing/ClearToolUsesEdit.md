---
title: "ClearToolUsesEdit"
description: "Configuration for clearing tool outputs when token limits are exceeded."
source: "https://reference.langchain.com/python/langchain/agents/middleware/context_editing/ClearToolUsesEdit"
category: "reference"
tags: [reference, langchain, agents, middleware, context_editing, cleartoolusesedit]
---

# ClearToolUsesEdit

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/context_editing/ClearToolUsesEdit)

Configuration for clearing tool outputs when token limits are exceeded.

## Signature

```python
ClearToolUsesEdit(
    self,
    trigger: int = 100000,
    clear_at_least: int = 0,
    keep: int = 3,
    clear_tool_inputs: bool = False,
    exclude_tools: Sequence[str] = (),
    placeholder: str = DEFAULT_TOOL_PLACEHOLDER,
)
```

## Extends

- `ContextEdit`

## Constructors

```python
__init__(
    self,
    trigger: int = 100000,
    clear_at_least: int = 0,
    keep: int = 3,
    clear_tool_inputs: bool = False,
    exclude_tools: Sequence[str] = (),
    placeholder: str = DEFAULT_TOOL_PLACEHOLDER,
) -> None
```

| Name | Type |
|------|------|
| `trigger` | `int` |
| `clear_at_least` | `int` |
| `keep` | `int` |
| `clear_tool_inputs` | `bool` |
| `exclude_tools` | `Sequence[str]` |
| `placeholder` | `str` |

## Properties

- `trigger`
- `clear_at_least`
- `keep`
- `clear_tool_inputs`
- `exclude_tools`
- `placeholder`

## Methods

- [`apply()`](https://reference.langchain.com/python/langchain/agents/middleware/context_editing/ClearToolUsesEdit/apply)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a18de590e7ccf5c647fbf3d689e5f1a15f78e9f5/libs/langchain_v1/langchain/agents/middleware/context_editing.py#L57)
