---
title: "merge"
description: "Merge the callback manager with another callback manager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/merge"
category: "reference"
tags: [reference, langchain-core, callbacks, base, basecallbackmanager, merge]
---

# merge

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/merge)

Merge the callback manager with another callback manager.

May be overwritten in subclasses.

Primarily used internally within `merge_configs`.

## Signature

```python
merge(
    self,
    other: BaseCallbackManager,
) -> Self
```

## Description

**Example:**

```python
# Merging two callback managers`
from langchain_core.callbacks.manager import (
    CallbackManager,
    trace_as_chain_group,
)
from langchain_core.callbacks.stdout import StdOutCallbackHandler

manager = CallbackManager(handlers=[StdOutCallbackHandler()], tags=["tag2"])
with trace_as_chain_group("My Group Name", tags=["tag1"]) as group_manager:
    merged_manager = group_manager.merge(manager)
    print(merged_manager.handlers)
    # [
    #    <langchain_core.callbacks.stdout.StdOutCallbackHandler object at ...>,
    #    <langchain_core.callbacks.streaming_stdout.StreamingStdOutCallbackHandler object at ...>,
    # ]

    print(merged_manager.tags)
    #    ['tag2', 'tag1']
```

## Returns

`Self`

The merged callback manager of the same type as the current object.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L1051)
