---
title: "get_child"
description: "Get a child callback manager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncParentRunManager/get_child"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asyncparentrunmanager, get_child]
---

# get_child

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncParentRunManager/get_child)

Get a child callback manager.

## Signature

```python
get_child(
    self,
    tag: str | None = None,
) -> AsyncCallbackManager
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tag` | `str \| None` | No | The tag for the child callback manager. (default: `None`) |

## Returns

`AsyncCallbackManager`

The child callback manager.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L686)
