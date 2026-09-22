---
title: "LastValue"
description: "Stores the last value received, can receive at most one value per step."
source: "https://reference.langchain.com/python/langgraph/channels/last_value/LastValue"
category: "reference"
tags: [reference, langgraph, channels, last_value, lastvalue]
---

# LastValue

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/channels/last_value/LastValue)

Stores the last value received, can receive at most one value per step.

## Signature

```python
LastValue(
    self,
    typ: Any,
    key: str = '',
)
```

## Extends

- `Generic[Value]`
- `BaseChannel[Value, Value, Value]`

## Constructors

```python
__init__(
    self,
    typ: Any,
    key: str = '',
) -> None
```

| Name | Type |
|------|------|
| `typ` | `Any` |
| `key` | `str` |

## Properties

- `value`
- `ValueType`
- `UpdateType`

## Methods

- [`copy()`](https://reference.langchain.com/python/langgraph/channels/last_value/LastValue/copy)
- [`from_checkpoint()`](https://reference.langchain.com/python/langgraph/channels/last_value/LastValue/from_checkpoint)
- [`update()`](https://reference.langchain.com/python/langgraph/channels/last_value/LastValue/update)
- [`get()`](https://reference.langchain.com/python/langgraph/channels/last_value/LastValue/get)
- [`is_available()`](https://reference.langchain.com/python/langgraph/channels/last_value/LastValue/is_available)
- [`checkpoint()`](https://reference.langchain.com/python/langgraph/channels/last_value/LastValue/checkpoint)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/644815f9e5bc52ad8f7a5227a456227e9c3e639b/libs/langgraph/langgraph/channels/last_value.py#L20)
