---
title: "atransform"
description: "Transform inputs to outputs."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/atransform"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnable, atransform]
---

# atransform

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/Runnable/atransform)

Transform inputs to outputs.

Default implementation of atransform, which buffers input and calls `astream`.

Subclasses must override this method if they can start producing output while
input is still being generated.

## Signature

```python
atransform(
    self,
    input: AsyncIterator[Input],
    config: RunnableConfig | None = None,
    **kwargs: Any | None = {},
) -> AsyncIterator[Output]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `AsyncIterator[Input]` | Yes | An async iterator of inputs to the `Runnable`. |
| `config` | `RunnableConfig \| None` | No | The config to use for the `Runnable`. (default: `None`) |
| `**kwargs` | `Any \| None` | No | Additional keyword arguments to pass to the `Runnable`. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/base.py#L1805)
