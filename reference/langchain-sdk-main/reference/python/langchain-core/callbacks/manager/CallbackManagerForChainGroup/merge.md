---
title: "merge"
description: "Merge the group callback manager with another callback manager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForChainGroup/merge"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanagerforchaingroup, merge]
---

# merge

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForChainGroup/merge)

Merge the group callback manager with another callback manager.

Overwrites the merge method in the base class to ensure that the parent run
manager is preserved. Keeps the `parent_run_manager` from the current object.

## Signature

```python
merge(
    self: CallbackManagerForChainGroup,
    other: BaseCallbackManager,
) -> CallbackManagerForChainGroup
```

## Description

**Example:**

```python
# Merging two callback managers
from langchain_core.callbacks.manager import (
    CallbackManager,
    trace_as_chain_group,
)
from langchain_core.callbacks.stdout import StdOutCallbackHandler

manager = CallbackManager(handlers=[StdOutCallbackHandler()], tags=["tag2"])
with trace_as_chain_group("My Group Name", tags=["tag1"]) as group_manager:
    merged_manager = group_manager.merge(manager)
    print(type(merged_manager))
    # <class 'langchain_core.callbacks.manager.CallbackManagerForChainGroup'>

    print(merged_manager.handlers)
    # [
    #    <langchain_core.callbacks.stdout.LangChainTracer object at ...>,
    #    <langchain_core.callbacks.streaming_stdout.StdOutCallbackHandler object at ...>,
    # ]

    print(merged_manager.tags)
    #    ['tag2', 'tag1']
```

## Returns

`CallbackManagerForChainGroup`

A copy of the current object with the handlers, tags, and other attributes

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/manager.py#L1772)
