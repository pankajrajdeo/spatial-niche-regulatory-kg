---
title: "warn_deprecated"
description: "Emit a deprecation warning with caller-controlled stack attribution."
source: "https://reference.langchain.com/python/deepagents/_api/deprecation/warn_deprecated"
category: "reference"
tags: [reference, deepagents, api, deprecation, warn_deprecated]
---

# warn_deprecated

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/_api/deprecation/warn_deprecated)

Emit a deprecation warning with caller-controlled stack attribution.

`langchain_core.warn_deprecated` formats a standard message but hardcodes
`stacklevel=4` in its internal `warnings.warn` call. That value targets a
decorator-wrapped frame layout; when called directly from a deprecated
method's body the warning is attributed one frame too high (above the
user's call site). This wrapper captures the formatted upstream warning
and re-emits it with an explicit `stacklevel`, so the warning points at
the user's call site.

## Signature

```python
warn_deprecated(
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
    stacklevel: int = 2,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `since` | `str` | Yes | Release at which this API became deprecated. |
| `message` | `str` | No | Override the default deprecation message. See upstream `langchain_core.warn_deprecated` for supported format specifiers. (default: `''`) |
| `name` | `str` | No | Name of the deprecated object. (default: `''`) |
| `alternative` | `str` | No | Alternative API the user may use instead. (default: `''`) |
| `alternative_import` | `str` | No | Alternative import path the user may use instead. (default: `''`) |
| `pending` | `bool` | No | If `True`, uses a `PendingDeprecationWarning` instead of a `DeprecationWarning`. Cannot be combined with `removal`. (default: `False`) |
| `obj_type` | `str` | No | Object type label (e.g., `"function"`, `"class"`). (default: `''`) |
| `addendum` | `str` | No | Additional text appended to the final message. (default: `''`) |
| `removal` | `str` | No | Expected removal version. Cannot be combined with `pending`. (default: `''`) |
| `package` | `str` | No | Package name attribution for the deprecation message. (default: `''`) |
| `stacklevel` | `int` | No | Frames above this call to attribute the warning to, using the same convention as `warnings.warn` (`1` = this call, `2` = the caller of the method body that invoked us, etc.). (default: `2`) |

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0f5a2b57fa5dbb3a7d8f16dc280cb5b1506ea8c0/libs/deepagents/deepagents/_api/deprecation.py#L39)
