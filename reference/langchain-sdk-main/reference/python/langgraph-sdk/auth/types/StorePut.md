---
title: "StorePut"
description: "Operation to store, update, or delete an item in the store."
source: "https://reference.langchain.com/python/langgraph-sdk/auth/types/StorePut"
category: "reference"
tags: [reference, langgraph-sdk, auth, types, storeput]
---

# StorePut

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/auth/types/StorePut)

Operation to store, update, or delete an item in the store.

This dict is mutable — auth handlers can modify `namespace` to enforce
access scoping (e.g., prepending the user's identity).

## Signature

```python
StorePut()
```

## Extends

- `typing.TypedDict`

## Constructors

```python
__init__(
    namespace: tuple[str, ...],
    key: str,
    value: dict[str, typing.Any] | None,
    index: typing.Literal[False] | list[str] | None,
)
```

| Name | Type |
|------|------|
| `namespace` | `tuple[str, ...]` |
| `key` | `str` |
| `value` | `dict[str, typing.Any] \| None` |
| `index` | `typing.Literal[False] \| list[str] \| None` |

## Properties

- `namespace`
- `key`
- `value`
- `index`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/d5f4b2aa960940effc8430165ab3604038e817af/libs/sdk-py/langgraph_sdk/auth/types.py#L936)
