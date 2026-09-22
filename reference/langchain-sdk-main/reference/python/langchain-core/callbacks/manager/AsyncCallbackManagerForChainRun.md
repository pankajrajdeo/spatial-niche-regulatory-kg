---
title: "AsyncCallbackManagerForChainRun"
description: "Async callback manager for chain run."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainRun"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asynccallbackmanagerforchainrun]
---

# AsyncCallbackManagerForChainRun

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainRun)

Async callback manager for chain run.

## Signature

```python
AsyncCallbackManagerForChainRun(
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
- `ChainManagerMixin`

## Methods

- [`get_sync()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainRun/get_sync)
- [`on_chain_end()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainRun/on_chain_end)
- [`on_chain_error()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainRun/on_chain_error)
- [`on_agent_action()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainRun/on_agent_action)
- [`on_agent_finish()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForChainRun/on_agent_finish)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L1018)
