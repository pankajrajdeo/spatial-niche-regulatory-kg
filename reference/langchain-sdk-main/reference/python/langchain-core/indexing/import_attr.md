---
title: "import_attr"
description: "Import an attribute from a module located in a package."
source: "https://reference.langchain.com/python/langchain-core/indexing/import_attr"
category: "reference"
tags: [reference, langchain-core, indexing, import_attr]
---

# import_attr

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_import_utils/import_attr)

Import an attribute from a module located in a package.

This utility function is used in custom `__getattr__` methods within `__init__.py`
files to dynamically import attributes.

## Signature

```python
import_attr(
    attr_name: str,
    module_name: str | None,
    package: str | None,
) -> object
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `attr_name` | `str` | Yes | The name of the attribute to import. |
| `module_name` | `str \| None` | Yes | The name of the module to import from.  If `None`, the attribute is imported from the package itself. |
| `package` | `str \| None` | Yes | The name of the package where the module is located. |

## Returns

`object`

The imported attribute.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/_import_utils.py#L4)
