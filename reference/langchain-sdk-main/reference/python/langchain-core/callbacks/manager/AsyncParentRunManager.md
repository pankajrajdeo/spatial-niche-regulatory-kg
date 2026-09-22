---
title: "AsyncParentRunManager"
description: "Async parent run manager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncParentRunManager"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asyncparentrunmanager]
---

# AsyncParentRunManager

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncParentRunManager)

Async parent run manager.

## Signature

```python
AsyncParentRunManager(
    self,
    *,
    run_id: UUID,
    handlers: list[BaseCallbackHandler],
    inheritable_handlers: list[BaseCallbackHandler],
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    inheritable_tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
    inheritable_metadata: dict[str, Any] | None = None,
)
```

## Extends

- `AsyncRunManager`

## Methods

- [`get_child()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncParentRunManager/get_child)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L683)
