---
title: "set_handler"
description: "Set handler as the only handler on the callback manager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/set_handler"
category: "reference"
tags: [reference, langchain-core, callbacks, base, basecallbackmanager, set_handler]
---

# set_handler

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/set_handler)

Set handler as the only handler on the callback manager.

## Signature

```python
set_handler(
    self,
    handler: BaseCallbackHandler,
    inherit: bool = True,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `handler` | `BaseCallbackHandler` | Yes | The handler to set. |
| `inherit` | `bool` | No | Whether to inherit the handler. (default: `True`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/base.py#L1154)
