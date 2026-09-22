---
title: "build_extra_kwargs"
description: "Build extra kwargs from values and extra_kwargs."
source: "https://reference.langchain.com/python/langchain-core/utils/utils/build_extra_kwargs"
category: "reference"
tags: [reference, langchain-core, utils, build_extra_kwargs]
---

# build_extra_kwargs

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/utils/build_extra_kwargs)

Build extra kwargs from values and extra_kwargs.

!!! danger "DON'T USE"

    Kept for backwards-compatibility but should never have been public. Use the
    internal `_build_model_kwargs` function instead.

## Signature

```python
build_extra_kwargs(
    extra_kwargs: dict[str, Any],
    values: dict[str, Any],
    all_required_field_names: set[str],
) -> dict[str, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `extra_kwargs` | `dict[str, Any]` | Yes | Extra kwargs passed in by user. |
| `values` | `dict[str, Any]` | Yes | Values passed in by user. |
| `all_required_field_names` | `set[str]` | Yes | All required field names for the pydantic class. |

## Returns

`dict[str, Any]`

Extra kwargs.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/utils.py#L262)
