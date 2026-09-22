---
title: "aadd"
description: "Asynchronously add a sequence of addable objects together."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/aadd"
category: "reference"
tags: [reference, langchain-core, runnables, utils, aadd]
---

# aadd

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/aadd)

Asynchronously add a sequence of addable objects together.

## Signature

```python
aadd(
    addables: AsyncIterable[Addable],
) -> Addable | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `addables` | `AsyncIterable[Addable]` | Yes | The addable objects to add. |

## Returns

`Addable | None`

The result of adding the addable objects.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/utils.py#L560)
