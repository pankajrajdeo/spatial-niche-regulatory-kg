---
title: "add"
description: "Add a sequence of addable objects together."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/add"
category: "reference"
tags: [reference, langchain-core, runnables, utils, add]
---

# add

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/add)

Add a sequence of addable objects together.

## Signature

```python
add(
    addables: Iterable[Addable],
) -> Addable | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `addables` | `Iterable[Addable]` | Yes | The addable objects to add. |

## Returns

`Addable | None`

The result of adding the addable objects.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/runnables/utils.py#L545)
