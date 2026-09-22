---
title: "dumpd"
description: "Return a dict representation of an object."
source: "https://reference.langchain.com/python/langchain-core/load/dumpd"
category: "reference"
tags: [reference, langchain-core, load, dumpd]
---

# dumpd

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/dump/dumpd)

Return a dict representation of an object.

## Signature

```python
dumpd(
    obj: Any,
) -> Any
```

## Description

**Note:**

Plain dicts containing an `'lc'` key are automatically escaped to prevent
confusion with LC serialization format. The escape marker is removed during
deserialization.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `obj` | `Any` | Yes | The object to dump. |

## Returns

`Any`

Dictionary that can be serialized to json using `json.dumps`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/load/dump.py#L105)
