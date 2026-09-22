---
title: "check_package_version"
description: "Check the version of a package."
source: "https://reference.langchain.com/python/langchain-core/utils/utils/check_package_version"
category: "reference"
tags: [reference, langchain-core, utils, check_package_version]
---

# check_package_version

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/utils/check_package_version)

Check the version of a package.

## Signature

```python
check_package_version(
    package: str,
    lt_version: str | None = None,
    lte_version: str | None = None,
    gt_version: str | None = None,
    gte_version: str | None = None,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `package` | `str` | Yes | The name of the package. |
| `lt_version` | `str \| None` | No | The version must be less than this. (default: `None`) |
| `lte_version` | `str \| None` | No | The version must be less than or equal to this. (default: `None`) |
| `gt_version` | `str \| None` | No | The version must be greater than this. (default: `None`) |
| `gte_version` | `str \| None` | No | The version must be greater than or equal to this. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/348c9dc572599947d2d7d33d6a5b8b936e92a1d4/libs/core/langchain_core/utils/utils.py#L146)
