---
title: "on_chain_end"
description: "Print that we finished a chain."
source: "https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_chain_end"
category: "reference"
tags: [reference, langchain-core, callbacks, file, filecallbackhandler, on_chain_end]
---

# on_chain_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_chain_end)

Print that we finished a chain.

## Signature

```python
on_chain_end(
    self,
    outputs: dict[str, Any],
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `outputs` | `dict[str, Any]` | Yes | The outputs of the chain. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/file.py#L181)
