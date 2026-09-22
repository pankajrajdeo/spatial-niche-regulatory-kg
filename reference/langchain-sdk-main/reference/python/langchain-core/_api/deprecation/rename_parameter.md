---
title: "rename_parameter"
description: "Decorator indicating that parameter old of func is renamed to new."
source: "https://reference.langchain.com/python/langchain-core/_api/deprecation/rename_parameter"
category: "reference"
tags: [reference, langchain-core, api, deprecation, rename_parameter]
---

# rename_parameter

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_api/deprecation/rename_parameter)

Decorator indicating that parameter *old* of *func* is renamed to *new*.

The actual implementation of *func* should use *new*, not *old*. If *old* is passed
to *func*, a `DeprecationWarning` is emitted, and its value is used, even if *new*
is also passed by keyword.

## Signature

```python
rename_parameter(
    *,
    since: str,
    removal: str,
    old: str,
    new: str,
) -> Callable[[Callable[_P, _R]], Callable[_P, _R]]
```

## Description

**Example:**

```python
@_api.rename_parameter("3.1", "bad_name", "good_name")
def func(good_name): ...
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `since` | `str` | Yes | The version in which the parameter was renamed. |
| `removal` | `str` | Yes | The version in which the old parameter will be removed. |
| `old` | `str` | Yes | The old parameter name. |
| `new` | `str` | Yes | The new parameter name. |

## Returns

`Callable[[Callable[_P, _R]], Callable[_P, _R]]`

A decorator indicating that a parameter was renamed.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/_api/deprecation.py#L589)
