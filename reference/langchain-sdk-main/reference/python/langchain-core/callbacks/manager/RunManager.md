---
title: "RunManager"
description: "Synchronous run manager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/RunManager"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, runmanager]
---

# RunManager

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/RunManager)

Synchronous run manager.

## Signature

```python
RunManager(
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

- `BaseRunManager`

## Methods

- [`on_text()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/RunManager/on_text)
- [`on_retry()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/RunManager/on_retry)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L546)
