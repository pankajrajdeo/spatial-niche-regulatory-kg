---
title: "on_chain_start"
description: "Print that we are entering a chain."
source: "https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_chain_start"
category: "reference"
tags: [reference, langchain-core, callbacks, file, filecallbackhandler, on_chain_start]
---

# on_chain_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_chain_start)

Print that we are entering a chain.

## Signature

```python
on_chain_start(
    self,
    serialized: dict[str, Any],
    inputs: dict[str, Any],
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serialized` | `dict[str, Any]` | Yes | The serialized chain information. |
| `inputs` | `dict[str, Any]` | Yes | The inputs to the chain. |
| `**kwargs` | `Any` | No | Additional keyword arguments that may contain `'name'`. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/callbacks/file.py#L162)
