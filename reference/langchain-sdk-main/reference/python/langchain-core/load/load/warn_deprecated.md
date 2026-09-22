---
title: "warn_deprecated"
description: "Display a standardized deprecation."
source: "https://reference.langchain.com/python/langchain-core/load/load/warn_deprecated"
category: "reference"
tags: [reference, langchain-core, load, warn_deprecated]
---

# warn_deprecated

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_api/deprecation/warn_deprecated)

Display a standardized deprecation.

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
) -> None
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

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/_api/deprecation.py#L480)
