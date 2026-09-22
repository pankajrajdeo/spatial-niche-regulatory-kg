---
title: "beta"
description: "Decorator to mark a function, a class, or a property as beta."
source: "https://reference.langchain.com/python/langchain-core/_api/beta_decorator/beta"
category: "reference"
tags: [reference, langchain-core, api, beta_decorator, beta]
---

# beta

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_api/beta_decorator/beta)

Decorator to mark a function, a class, or a property as beta.

When marking a classmethod, a staticmethod, or a property, the `@beta` decorator
should go *under* `@classmethod` and `@staticmethod` (i.e., `beta` should directly
decorate the underlying callable), but *over* `@property`.

When marking a class `C` intended to be used as a base class in a multiple
inheritance hierarchy, `C` *must* define an `__init__` method (if `C` instead
inherited its `__init__` from its own base class, then `@beta` would mess up
`__init__` inheritance when installing its own (annotation-emitting) `C.__init__`).

## Signature

```python
beta(
    *,
    message: str = '',
    name: str = '',
    obj_type: str = '',
    addendum: str = '',
) -> Callable[[T], T]
```

## Description

**Example:**

```python
@beta
def the_function_to_annotate():
    pass
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `message` | `str` | No | Override the default beta message.  The %(since)s, %(name)s, %(alternative)s, %(obj_type)s, %(addendum)s, and %(removal)s format specifiers will be replaced by the values of the respective arguments passed to this function. (default: `''`) |
| `name` | `str` | No | The name of the beta object. (default: `''`) |
| `obj_type` | `str` | No | The object type being beta. (default: `''`) |
| `addendum` | `str` | No | Additional text appended directly to the final message. (default: `''`) |

## Returns

`Callable[[T], T]`

A decorator which can be used to mark functions or classes as beta.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/_api/beta_decorator.py#L32)
