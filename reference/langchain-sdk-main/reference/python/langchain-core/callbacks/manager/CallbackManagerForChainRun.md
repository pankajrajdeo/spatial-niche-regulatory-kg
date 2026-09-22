---
title: "CallbackManagerForChainRun"
description: "Callback manager for chain run."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForChainRun"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanagerforchainrun]
---

# CallbackManagerForChainRun

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForChainRun)

Callback manager for chain run.

## Signature

```python
CallbackManagerForChainRun(
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

- `ParentRunManager`
- `ChainManagerMixin`

## Methods

- [`on_chain_end()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForChainRun/on_chain_end)
- [`on_chain_error()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForChainRun/on_chain_error)
- [`on_agent_action()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForChainRun/on_agent_action)
- [`on_agent_finish()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForChainRun/on_agent_finish)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L928)
