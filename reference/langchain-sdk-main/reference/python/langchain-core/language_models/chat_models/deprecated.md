---
title: "deprecated"
description: "Decorator to mark a function, a class, or a property as deprecated."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_models/deprecated"
category: "reference"
tags: [reference, langchain-core, language_models, chat_models, deprecated]
---

# deprecated

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_api/deprecation/deprecated)

Decorator to mark a function, a class, or a property as deprecated.

When deprecating a classmethod, a staticmethod, or a property, the `@deprecated`
decorator should go *under* `@classmethod` and `@staticmethod` (i.e., `deprecated`
should directly decorate the underlying callable), but *over* `@property`.

When deprecating a class `C` intended to be used as a base class in a multiple
inheritance hierarchy, `C` *must* define an `__init__` method (if `C` instead
inherited its `__init__` from its own base class, then `@deprecated` would mess up
`__init__` inheritance when installing its own (deprecation-emitting) `C.__init__`).

Parameters are the same as for `warn_deprecated`, except that *obj_type* defaults to
'class' if decorating a class, 'attribute' if decorating a property, and 'function'
otherwise.

## Signature

```python
deprecated(
    since: str,
    *,
    message: str = '',
    name: str = '',
    alternative: str = '',
    alternative_import: str = '',
    pending: bool = False,
    obj_type: str = '',
    addendum: str = '',
    removal: str = '',
    package: str = '',
) -> Callable[[T], T]
```

## Description

**Example:**

```python
@deprecated("1.4.0")
def the_function_to_deprecate():
    pass
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `since` | `str` | Yes | The release at which this API became deprecated. |
| `message` | `str` | No | Override the default deprecation message.  The `%(since)s`, `%(name)s`, `%(alternative)s`, `%(obj_type)s`, `%(addendum)s`, and `%(removal)s` format specifiers will be replaced by the values of the respective arguments passed to this function. (default: `''`) |
| `name` | `str` | No | The name of the deprecated object. (default: `''`) |
| `alternative` | `str` | No | An alternative API that the user may use in place of the deprecated API.  The deprecation warning will tell the user about this alternative if provided. (default: `''`) |
| `alternative_import` | `str` | No | An alternative import that the user may use instead. (default: `''`) |
| `pending` | `bool` | No | If `True`, uses a `PendingDeprecationWarning` instead of a `DeprecationWarning`.  Cannot be used together with removal. (default: `False`) |
| `obj_type` | `str` | No | The object type being deprecated. (default: `''`) |
| `addendum` | `str` | No | Additional text appended directly to the final message. (default: `''`) |
| `removal` | `str` | No | The expected removal version.  With the default (an empty string), no removal version is shown in the warning message.  Cannot be used together with pending. (default: `''`) |
| `package` | `str` | No | The package of the deprecated object. (default: `''`) |

## Returns

`Callable[[T], T]`

A decorator to mark a function or class as deprecated.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/_api/deprecation.py#L120)
