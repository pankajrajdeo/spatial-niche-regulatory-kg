---
title: "AsyncCallbackManagerForRetrieverRun"
description: "Async callback manager for retriever run."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForRetrieverRun"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asynccallbackmanagerforretrieverrun]
---

# AsyncCallbackManagerForRetrieverRun

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForRetrieverRun)

Async callback manager for retriever run.

## Signature

```python
AsyncCallbackManagerForRetrieverRun(
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

- `AsyncParentRunManager`
- `RetrieverManagerMixin`

## Methods

- [`get_sync()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForRetrieverRun/get_sync)
- [`on_retriever_end()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForRetrieverRun/on_retriever_end)
- [`on_retriever_error()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForRetrieverRun/on_retriever_error)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L1302)
